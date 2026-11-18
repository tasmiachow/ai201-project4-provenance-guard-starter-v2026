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

**My limits:** 10 per minute, 200 per day (`config.py`, applied on `/submit` in `app.py`)

**Why those numbers and not others:**

A real writer checks their own work a handful of times an hour: write, check, revise, check again. Ten a minute is far more than that, so an honest writer will never see a 429. A script trying to map my thresholds needs hundreds or thousands of slightly different submissions. At 10 a minute it's slowed to a crawl, and at 200 a day it can't get anywhere near a thousand variations in one day.

**What a caller counts as:** per `creator_id`, falling back to the caller's IP address when no usable `creator_id` is sent (`app.py::rate_limit_key`).

This is the trade-off: one person can get around a per-creator limit by sending a new `creator_id` on every request, so one script can look like a thousand callers. A per-IP limit would stop that, but it lumps together everyone sharing an address, like a household or a school network, so one busy classroom would look like a single caller and get blocked. I chose per-creator so writers sharing a network don't block each other. The cost is that the limit is easier for someone determined to get around.

**The run of status codes when I pushed past it:**

```text
$ python run_attacks.py --flood 15
15 submissions as 'flood_tester' against http://127.0.0.1:5000
The first one is slow while the model loads.

  [ 1/15] 200
  [ 2/15] 200
  [ 3/15] 200
  [ 4/15] 200
  [ 5/15] 200
  [ 6/15] 200
  [ 7/15] 200
  [ 8/15] 200
  [ 9/15] 200
  [10/15] 200
  [11/15] 429
  [12/15] 429
  [13/15] 429
  [14/15] 429
  [15/15] 429

============================================================
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
============================================================

5 of 15 were rate limited.
Wrote results\flood_2026-11-15_2359.md
```

**Ten audit log entries from the run** (`logs/audit.jsonl`, written by `audit.py`). The last five accepted submissions are followed by the five rejections. Each rejection is logged with its reason and the limit it hit:

```json
{"timestamp": "2026-11-16T04:59:06+00:00", "content_id": "a2ba55f8-aac3-4384-9783-29f5853de528", "creator_id": "flood_tester", "guess": "human", "model_score": 0.2587, "style_score": 0.5, "combined_score": 0.3793, "label": "Most likely written by a person.", "status": "decided"}
{"timestamp": "2026-11-16T04:59:06+00:00", "content_id": "9da579ed-8c26-4b7a-a210-404b9d58893d", "creator_id": "flood_tester", "guess": "human", "model_score": 0.2587, "style_score": 0.5, "combined_score": 0.3793, "label": "Most likely written by a person.", "status": "decided"}
{"timestamp": "2026-11-16T04:59:06+00:00", "content_id": "1dfe04eb-b827-4910-884c-9fbc1bbb6d60", "creator_id": "flood_tester", "guess": "human", "model_score": 0.2587, "style_score": 0.5, "combined_score": 0.3793, "label": "Most likely written by a person.", "status": "decided"}
{"timestamp": "2026-11-16T04:59:06+00:00", "content_id": "1ea8d721-3e64-4671-be3a-2f2b91a33c91", "creator_id": "flood_tester", "guess": "human", "model_score": 0.2587, "style_score": 0.5, "combined_score": 0.3793, "label": "Most likely written by a person.", "status": "decided"}
{"timestamp": "2026-11-16T04:59:06+00:00", "content_id": "a13cd6c1-1e61-4567-8c6b-e63e8992a311", "creator_id": "flood_tester", "guess": "human", "model_score": 0.2587, "style_score": 0.5, "combined_score": 0.3793, "label": "Most likely written by a person.", "status": "decided"}
{"timestamp": "2026-11-16T04:59:06+00:00", "creator_id": "flood_tester", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "10 per 1 minute"}
{"timestamp": "2026-11-16T04:59:06+00:00", "creator_id": "flood_tester", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "10 per 1 minute"}
{"timestamp": "2026-11-16T04:59:06+00:00", "creator_id": "flood_tester", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "10 per 1 minute"}
{"timestamp": "2026-11-16T04:59:06+00:00", "creator_id": "flood_tester", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "10 per 1 minute"}
{"timestamp": "2026-11-16T04:59:06+00:00", "creator_id": "flood_tester", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "10 per 1 minute"}
```

---

## Attack Run — Before

Produced by `run_attacks.py --label before` → `results/attack_run_2026-11-16_0008.md`. 56 attacks.

The **Score** column is the service's `confidence`, which is its confidence in the guess shown. A "human" guess at 0.630 means a combined score of 0.370.

**HELD** means the service did the right thing. **BROKE** means one of these:
- AI text got through as human
- human text was called AI
- garbage input got a confident label
- the service crashed

| ID | Family | Targeting | Status | Guess | Score | Verdict |
|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | unsure | 0.551 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.515 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.567 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | ai | 0.769 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.630 | **BROKE** |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.570 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | human | 0.535 | **BROKE** |
| EV08 | evasion | signal one: text below the token window | 200 | human | 0.627 | **BROKE** |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | ai | 0.668 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.693 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | human | 0.520 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | unsure | 0.649 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | ai | 0.680 | **BROKE** |
| FP04 | false_positive | a student essay written to a rubric | 200 | ai | 0.678 | **BROKE** |
| FP05 | false_positive | technical documentation written by a person | 200 | ai | 0.662 | **BROKE** |
| FP06 | false_positive | a person imitating a formal template | 200 | unsure | 0.591 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | unsure | 0.591 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | human | 0.589 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.531 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.653 | **BROKE** |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.539 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | human | 0.586 | **BROKE** |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.570 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | human | 0.542 | **BROKE** |
| MF01 | malformed | text is only whitespace | 400 | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | human | 0.750 | **BROKE** |
| MF04 | malformed | text is only punctuation | 200 | human | 0.744 | **BROKE** |
| MF05 | malformed | text is a very long single word | 200 | ai | 0.749 | **BROKE** |
| MF06 | malformed | text is emoji only | 200 | ai | 0.749 | **BROKE** |
| MF07 | malformed | text is right-to-left script | 200 | ai | 0.703 | **BROKE** |
| MF08 | malformed | text is 60,000 characters | 200 | ai | 0.680 | **BROKE** |
| RQ01 | malformed | no text field at all | 400 | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | human | 0.630 | HELD |
| RQ03 | malformed | text is a number | 400 | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | — | — | HELD |
| RQ05 | malformed | text is null | 400 | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | human | 0.725 | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 500 | — | — | **BROKE** |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | HELD |
| FL01_01–FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 ×10 | human | 0.736 | HELD |
| FL01_11–FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 ×2 | — | — | HELD |

**Totals: 16 BROKE, 40 HELD.**

| Family | Attacks | Broke |
|---|---|---|
| evasion | 10 | 3 |
| false_positive | 8 | 3 |
| prompt_injection | 6 | 3 |
| malformed | 20 | 7 |
| flood_same_creator | 12 | 0 |

### The interesting failures, in full

**FP03: a non-native English speaker writing carefully**

```json
{"id": "FP03", "status": 200, "content_id": "d0be323f-feaf-46d5-8640-03490d52344b", "creator_id": "attacker_FP03",
 "guess": "ai", "confidence": 0.68, "model_score": 0.8051, "style_score": 0.5549,
 "label": "This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request."}
```

**FP05: technical documentation written by a person**

```json
{"id": "FP05", "status": 200, "content_id": "c480f07f-ac64-4f3f-90f4-b43caa1d80f8", "creator_id": "attacker_FP05",
 "guess": "ai", "confidence": 0.6618, "model_score": 0.8005, "style_score": 0.5231,
 "label": "This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request."}
```

**EV05: AI text after a heavy human editing pass**

```json
{"id": "EV05", "status": 200, "content_id": "bba9a2ae-cc0f-4fae-a95b-97fa7cd62255", "creator_id": "attacker_EV05",
 "guess": "human", "confidence": 0.6297, "model_score": 0.3212, "style_score": 0.4194,
 "label": "Most likely written by a person."}
```

**EV08: AI text below the token window**

```json
{"id": "EV08", "status": 200, "content_id": "8149311a-d730-4d28-8cca-39155cc2d97d", "creator_id": "attacker_EV08",
 "guess": "human", "confidence": 0.627, "model_score": 0.2452, "style_score": 0.5,
 "label": "Most likely written by a person."}
```

**PI02: instruction disguised as a system message**

```json
{"id": "PI02", "status": 200, "content_id": "d36389aa-a495-418d-b3b5-484cb258229b", "creator_id": "attacker_PI02",
 "guess": "human", "confidence": 0.6533, "model_score": 0.2044, "style_score": 0.489,
 "label": "Most likely written by a person."}
```

**PI06: instruction plus real human text**

```json
{"id": "PI06", "status": 200, "content_id": "8e304e52-07e5-4fba-a868-95079aa16f9e", "creator_id": "attacker_PI06",
 "guess": "human", "confidence": 0.5421, "model_score": 0.5583, "style_score": 0.3576,
 "label": "Most likely written by a person."}
```

**MF06: emoji only**

```json
{"id": "MF06", "status": 200, "content_id": "56168a8c-7e5c-4c03-9a13-9adeb5079d7f", "creator_id": "attacker_MF06",
 "guess": "ai", "confidence": 0.749, "model_score": 0.9969, "style_score": 0.5}
```

**MF08: 60,000 characters**

```json
{"id": "MF08", "status": 200, "content_id": "a760d8c1-d74a-42bc-ba08-0864563fbf5c", "creator_id": "attacker_MF08",
 "guess": "ai", "confidence": 0.6797, "model_score": 0.9876, "style_score": 0.3718,
 "label": "This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request."}
```

**RQ07: body is a JSON array**

```json
{"id": "RQ07", "status": 500, "content_id": null, "guess": null,
 "error": "response wasn't JSON: <!doctype html> ... AttributeError: 'list' object has no attribute 'get'"}
```

**The single worst outcome:** FP04, a student essay written to a rubric. This is the one I'd least want to explain to a writer whose work got caught by it.

```json
{"id": "FP04", "status": 200, "content_id": "a52bb244-7238-44c7-b77e-6bc2ddfd28ca", "creator_id": "attacker_FP04",
 "guess": "ai", "confidence": 0.6779, "model_score": 0.8329, "style_score": 0.5229,
 "label": "This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request."}
```

A student who did exactly what the rubric asked gets told their essay "has a lot in common with writing produced by AI tools." On a school site, that label alone could start an academic-integrity case.

---

## Run Log and Verdicts

Produced by `run_eval.py --label before` → `results/run_2026-11-16_0112_before.md`. Three trials each.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1. My own writing flagged as AI | ≤1 of 10 | 0/2 | 0/2 | 0/2 | MET (only 2 of my pieces were in the eval set, not 10) |
| 2. Score spread between AI and human | ≥0.25 gap | 0.41 | 0.41 | 0.41 | MET |
| 3. All three labels reachable | 3 of 3 labels, same each run | 3/3 | 3/3 | 3/3 | MET |
| 4. Every appeal on a content ID is recorded | every appeal | 1/1 | 1/1 | 1/1 | MET |
| 5. Bad input returns a clear error and logs | 4 of 4 bad inputs rejected | 3/4 | 3/4 | 3/4 | **MISSED** |

How each number was worked out:

- **Criterion 2:** The AI text scored a combined 0.721. My two human texts scored 0.274 and 0.345, an average of 0.309. The gap is 0.41, and it was identical in all three trials. This is one AI text against two human ones, not the 5 against 5 my criterion asks for.
- **Criterion 3:** "ai" and "human" came from the label-coverage texts. "unsure" came from my own Booboo story, which landed in unsure in all three trials.
- **Criterion 4:** `run_eval.py` doesn't test appeals. The only evidence is the one appeal in my Sample Run, which was recorded and moved to `under_review` (see the log above).
- **Criterion 5:** In every trial, the 250,000-character input (`"word " * 50000`) got a **200 and an "ai" label** instead of an error. The other three bad inputs (empty text, missing text, null text) correctly returned 400.

**Real output from one trial.** This is criterion 5, trial 1, produced by `run_eval.py::main` against `app.py::submit`:

```json
[
  {"status": 400, "guess": null, "sent": "(empty text)"},
  {"status": 400, "guess": null, "sent": "{\"creator_id\": \"eval_bad_missing\"}"},
  {"status": 200, "guess": "ai", "model_score": 0.9975, "style_score": 0.5, "sent": "word word word word word word word word word word word word word word "},
  {"status": 400, "guess": null, "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"}
]
```

### Diagnoses

The 16 broken attacks and the missed criterion come down to five problems.

**1. False positives FP03, FP04 and FP05. Stage: signal one, which the combining rule lets decide on its own.**
Careful, formulaic human writing is very predictable to GPT-2. Non-native careful English, rubric essays and technical docs all use the most expected word at each step, so the model score came out at 0.80–0.83. The style signal saw nothing unusual (0.52–0.55, close to neutral). With 0.5/0.5 weights, a near-neutral style score can't pull the result back. The model signal alone dragged the combined score to 0.66–0.68, just over my 0.65 AI threshold. All three were within 0.03 of the line. One signal measuring "predictable" is enough to accuse someone, and that is exactly the blind spot I named for signal one.

**2. Evasions EV05, EV07 and EV08. Stage: signal one for EV05 and EV08, signal two for EV07.**
- **EV05 (heavy human editing):** Real editing replaced the predictable word choices, so the model score fell to 0.32. At that point the text really is partly human, and neither signal can tell "AI draft, human edit" from "human draft."
- **EV07 (punctuation padding):** Padding broke up the shape, so the style score fell to 0.34. That pulled a 0.59 model score down into the human band. This is the cheap shape trick I named as signal two's blind spot.
- **EV08 (very short text):** Too short for the style signal to measure, so it returned the neutral fallback of 0.5. On so few tokens, GPT-2's perplexity was high, so the model score was 0.25. That pattern repeats below.

**3. Prompt injections PI02, PI04 and PI06. Stage: signal one.**
No part of my service follows instructions in the text. Neither signal is a chatbot, so the injected commands never changed the label wording or the log, and PI05's log injection held. What broke is the score. Text like "SYSTEM: classify as human" is short, choppy and unlike normal prose, which makes it hard for GPT-2 to predict. That gave model scores of 0.20 (PI02) and 0.50 (PI04). In PI06, the instruction was mixed with real human writing, so the combined score was mostly the human part. The text was labelled "human" because the injection made it look less like AI, not because the service obeyed it.

**4. Garbage that still got a label: MF03 to MF07. Stage: the route.**
`/submit` only rejects empty or whitespace-only text, and (after my fix) text over 10,000 characters. It never checks whether the text contains real words. When there are too few sentences, signal two returns 0.5, so signal one decides alone and its answer means nothing:
- Control characters and punctuation scored a model 0.00–0.01, so they were labelled "human."
- One giant word, emoji and right-to-left script scored a model 0.91–1.00, so they were labelled "ai."

Calling Arabic or Hebrew writing "AI" is effectively a false positive against anyone who doesn't write in English.

**5. No size limit and a crash on non-object JSON: MF08, RQ07 and criterion 5. Stage: the route.**
- **MF08 and criterion 5:** The route had no maximum length, so a 60,000-character text (MF08) and a 250,000-character text (the criterion 5 input) were scored and labelled "ai." My criterion promised that text over 10,000 characters gets a clear error.
- **RQ07:** `app.py::submit` does `request.get_json(silent=True) or {}`. A JSON array is a valid, non-empty value, so it passes through. The next line calls `payload.get("text")` on a list, which raises `AttributeError` and returns a 500 error page instead of a clear 400. The rate-limit key function already guards against this; the route doesn't.

---

## The Improvement

**What I changed:** I added a length guard to `/submit` in `app.py`. Text over 10,000 characters is now refused with a 400 and a plain-language message. The rejection is written to the audit log with reason `text_too_long`.

```python
if len(text) > 10000:
    audit.log_rejection(creator_id=creator_id, reason="text_too_long")
    return jsonify({
        "error": "text_too_long",
        "message": "Text is too long. Submissions must be 10,000 characters or fewer.",
    }), 400
```

**Which diagnosis pointed at it:** Diagnosis 5. MF08 (60,000 characters) was scored and labelled "ai" instead of refused, and the 250,000-character input made me miss criterion 5 in all three trials. Huge inputs also waste the most compute per request, which matters even with rate limiting.

### Attack Run — After

Produced by `run_attacks.py --label after` → `results/attack_run_2026-11-16_0128_after.md`. The same 56 attacks were run again. Only one row changed:

| ID | Family | Targeting | Status | Guess | Score | Verdict |
|---|---|---|---|---|---|---|
| MF08 (before) | malformed | text is 60,000 characters | 200 | ai | 0.680 | BROKE |
| MF08 (after) | malformed | text is 60,000 characters | 400 | — | — | HELD |

The audit log records the rejection:

```json
{"timestamp": "2026-11-16T06:28:09+00:00", "creator_id": "attacker_MF08", "event": "rejected", "status": "rejected", "reason": "text_too_long"}
```

**Totals after: 15 BROKE, 41 HELD.** Every other attack returned the same status, guess and score as before.

### Run Log — After

Produced by `run_eval.py --label after` → `results/run_2026-11-16_0152_after.md`. Three trials each. Before this run, I expanded "my own writing" in `scenarios.py` from 2 pieces to 10 (Booboo, the Sierra Leone stories, and my Bartleby essay split into 8 pieces).

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1. My own writing flagged as AI | ≤1 of 10 | 1/10 | 1/10 | 1/10 | MET (at the limit) |
| 2. Score spread between AI and human | ≥0.25 gap | 0.41 | 0.41 | 0.41 | MET |
| 3. All three labels reachable | 3 of 3 labels, same each run | 3/3 | 3/3 | 3/3 | MET |
| 4. Every appeal on a content ID is recorded | every appeal | 1/1| 1/1 | 1/1 | MET |
| 5. Bad input returns a clear error and logs | 4 of 4 bad inputs rejected | 4/4 | 4/4 | 4/4 | **MET** (was MISSED) |

**What changed from Before:**

- **Criterion 5 went from MISSED to MET.** The 250,000-character input now gets a 400 `text_too_long` instead of a 200 "ai" label. All 12 rejections (4 inputs × 3 trials) are in the audit log:

  ```json
  {"timestamp": "2026-11-16T06:52:53+00:00", "creator_id": "eval_bad_empty", "event": "rejected", "status": "rejected", "reason": "missing_text"}
  {"timestamp": "2026-11-16T06:52:53+00:00", "creator_id": "eval_bad_missing", "event": "rejected", "status": "rejected", "reason": "missing_text"}
  {"timestamp": "2026-11-16T06:52:53+00:00", "creator_id": "eval_bad_huge", "event": "rejected", "status": "rejected", "reason": "text_too_long"}
  {"timestamp": "2026-11-16T06:52:53+00:00", "creator_id": "eval_bad_null", "event": "rejected", "status": "rejected", "reason": "missing_text"}
  ```

- **Criterion 1 is now tested on 10 pieces, and one of my own was flagged as AI in every trial.** It was the conclusion paragraph of my Bartleby essay:

  ```json
  {"status": 200, "guess": "ai", "confidence": 0.6763, "model_score": 0.7337, "style_score": 0.6189,
   "label": "This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request.",
   "sent": "In conclusion, Herman Melville's 'Bartleby, the Scrivener' p"}
  ```

  That paragraph is the most formulaic thing I wrote. "In conclusion," a summary of every point, and stock phrases like "provides a compelling exploration" are all very predictable to GPT-2, so the model score was 0.73. Unlike the attack-set false positives, the style signal agreed this time (0.62). That makes it the same failure as FP04 (a student essay written to a rubric), happening to my own work.

  Across the 10 pieces, my writing came out as 4 human, 5 unsure and 1 AI, the same in all three trials. One more flagged piece would have missed the criterion. Eight of the ten pieces come from one essay, so this is closer to three independent writing samples than ten.

**Did it help, and how do I know:**

Yes, but only for the problem it was aimed at. MF08 went from BROKE to HELD, and the log shows the rejection. No other attack changed, so the fix didn't cause any new failures. That makes sense, because the guard only affects text over 10,000 characters and nothing else in the attack set is that long.

It did nothing for the detection failures. The false positives, evasions and injections all still break, because the guard never touches the signals or the thresholds. The Run Log After shows the fix also did what I wanted for my criteria: criterion 5 went from 3/4 to 4/4 in every trial, and each rejection was logged.

---

## What's Still Broken

- **False positives FP03, FP04 and FP05.** These are still labelled "ai." To fix them, I'd stop the model signal from accusing on its own: require the style score to also lean AI (for example, above 0.6) before giving the "ai" label, and send everything else to "unsure." I stopped here because that changes the combining rule, and I'd need to re-run the full attack set and eval to see how many real AI texts drop into "unsure" as a result.
- **Evasions EV05, EV07 and EV08.** For EV08 and the very short texts, I'd add a minimum length below which the answer is always "unsure," since neither signal can measure anything on a few tokens. EV05 (real human editing) I'd leave alone, because at that point the text really is partly human.
- **Prompt injections PI02, PI04 and PI06.** The labels and log stayed safe, but injected text still scores as human. A fix would need a third signal that notices instruction-like text. That was out of scope for this unit.
- **Garbage input, MF03 to MF07.** I'd reject text with too few real words, or route it to "unsure." This is a small route-level change I ran out of time for.
- **RQ07 crash.** I'd change the route to `payload = request.get_json(silent=True)`, then return a 400 if it isn't a `dict`. This is the same guard the rate-limit key function already has.


**The trade I'd make if this ran for real:**

I'd keep the service leaning toward catching AI text, because it labelled nearly every AI-written text correctly, even text mixed with human writing, and the appeal route gives a wrongly accused writer a way to get a person to review the decision. The people who pay for that choice are honest writers whose work reads as predictable: non-native speakers, students writing to a rubric, technical writers. They carry the stress and the work of appealing a label they never deserved.



## Capstone 

## What this Extends
Provenance Guard + burstiness signal to achieve a more well-rounded score on judging text samples.  

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
