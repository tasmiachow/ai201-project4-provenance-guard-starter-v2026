# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

Provenance Guard is a small web service that takes a piece of writing and guesses whether a person or an AI tool wrote it, by checking how predictable the words are and how the writing is shaped, then labelling it "probably human", "unsure", or "has a lot in common with AI". Every decision is saved in a log, and a writer who thinks their label is wrong can appeal it so a person reviews it.

### Path a Submission Takes
1. The /submit route (app.py) receives it. A writer sends their text and a creator ID to the web service. The route pulls those two out of the request and checks the text is usable (not missing, empty, or enormous). It gives the submission a unique content ID, which is what lets the writer find and appeal this decision later.

2. The model signal (detector.py) reads it for predictability. A small language model (GPT-2), running on this machine, measures how surprised it is by each word. This is called perplexity. Text the model could easily have guessed scores closer to 1, meaning "likely AI". Surprising, wandering text scores closer to 0. This step adds the model score.

3. The style signal (stylometry.py) measures its shape. Without understanding any of the words, it looks at three things: whether sentence lengths vary or stay even, how often the vocabulary repeats, and how much punctuation there is and what kinds. Even sentences, excessive punctuation, and exapansive vocabulary push toward AI. Lumpy, varied writing pushes toward human. This step adds the style score, on the same 0–1 scale and pointing the same way.

4. The combining rule (scoring.py, combine_signals) merges the two scores into one. It weighs the model score against the style score using the weights in config.py and produces a single combined score from 0 (confidently human) to 1 (confidently AI). When the two signals disagree, this rule decides what happens, so this is where the service chooses which way it would rather be wrong.

5. The label step (scoring.py, score_to_label) turns the number into words. It compares the combined score to the two thresholds in config.py. A score at or below the lower one counts as human, at or above the upper one counts as AI, and anything in between is unsure. This step adds the guess (human / unsure / AI) and the label text, a plain sentence written for someone who has never heard the word "threshold".

6. The audit log (audit.py) records the decision. Before anything goes back to the writer, one line is added to logs/audit.jsonl. It holds the time, content ID, creator ID, both signal scores, the combined score, the guess, the label, and a status of "decided". The log is append-only. If the writer appeals later, the appeal is written after this entry and the original decision is never overwritten.

7. The response goes back to the reader. The route returns the content ID, the guess, a confidence, the label text, and both signal scores. The label sentence is what the person actually sees. The content ID is their way into /appeal if they think the label is wrong.


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** Perplexity

**Why that might differ between human and AI writing:** High perplexity points to human writing because the text was hard to predict. Low perplexity points to AI.

**What it can't see:** Humans can also write common, and ordinary senteces. 

### Signal two — the style signal

**What it measures:** Shape

**Why that might differ between human and AI writing:** generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

**What it can't see:** Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose to make it seem non-ai.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** The combined score is the plain average of the model score and the style score. Both run from 0 (human) to 1 (AI). When the two signals disagree strongly, the average lands in the middle, so the text is labelled "unsure". Neither signal can call something AI on its own.

**The numbers:** model weight 0.5, style weight 0.5. Above 0.65 is labelled AI, below 0.35 is labelled human, and anything in between is unsure for now.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| human | 0.000 - 0.499 | Most likely written by a person. |
| unsure | 0.50 - 0.6499 | We can't tell whether this was written by a person or with help from AI. |
| AI | 0.650 - 1.00 | This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

It says help from AI, and directly admits it can't discern if it's written by a person vs. help from ai tool.

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "This is a story about an egg named Booboo. The last thing he remembered was being on a lush farm, seeing the beautiful blue sky, and feeling the gentle breeze of the wind. When he woke, he was in a completely dark, isolated space, and he was freezing. Before Booboo was about to be devastated, the door opened, and he saw the light appear. He was surrounded by other objects he had never seen before: a ketchup bottle, a chocolate, yogurt, etc. More importantly, he saw a little girl picking out the yogurt before she slammed the door shut, turning his vision back into darkness. When the fridge closed, Mr.Ketchup Bottle had flipped the light switch back on. The other foods were all chatting and dancing. He was amazed; he was right on the top shelf. As Booboo made his way down, he asked Mr.Ketchup Bottle, \"Hey, are you cold?\"", "creator_id": "tasmia"}'
```

```json
{
  "combined_score": 0.505,
  "confidence": 0.505,
  "content_id": "d34761ca-6ce3-4d6c-9fb9-0b327a345dc7",
  "guess": "unsure",
  "label": "We can't tell whether this was written by a person or with help from AI.",
  "model_score": 0.732,
  "style_score": 0.2781
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "d34761ca-6ce3-4d6c-9fb9-0b327a345dc7", "reasoning": "I wrote this story myself for class. The common phrases like gentle breeze are just how I write descriptions, not AI."}'
```

```json
{
  "content_id": "d34761ca-6ce3-4d6c-9fb9-0b327a345dc7",
  "message": "Thanks — your appeal has been recorded and a person will review this decision. The original label stays on record beside your appeal.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.505,
      "content_id": "d34761ca-6ce3-4d6c-9fb9-0b327a345dc7",
      "creator_id": "tasmia",
      "guess": "unsure",
      "label": "We can't tell whether this was written by a person or with help from AI.",
      "model_score": 0.732,
      "status": "decided",
      "style_score": 0.2781,
      "timestamp": "2026-11-04T06:25:35+00:00"
    },
    {
      "content_id": "d34761ca-6ce3-4d6c-9fb9-0b327a345dc7",
      "creator_id": "tasmia",
      "event": "appeal",
      "reasoning": "I wrote this story myself for class. The common phrases like gentle breeze are just how I write descriptions, not AI.",
      "status": "under_review",
      "timestamp": "2026-11-04T06:25:35+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* I asked AI to explain what the two signals measured. 
- *What came back:* It explained that detector.py measured perplexity and a higher perplexity pointed towards human (less predicatble text) and stylometry more punctuation led to more likely being AI.
- *What I changed:* n/a

**Moment 2**

- *What I asked for:* I asked AI to run the test cases and put in its own bus story. 
- *What came back:* It was able to produce the results in the audit log.
- *What I changed:* N/A

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
