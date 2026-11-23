# Provenance Guard

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

Provenance Guard is a small web service that takes a piece of writing and guesses whether a person or an AI tool wrote it, by checking how predictable the words are and how the writing is shaped, then labelling it "probably human", "unsure", or "has a lot in common with AI". Every decision is saved in a log, and a writer who thinks their label is wrong can appeal it so a person reviews it.

## Capstone
    The OLDREADME.md contains unit 7 and unit 8 for comparison. I only have my capstone readme here now for simplicity. 
### What This Extends

This extends **Provenance Guard** (units 7 and 8): the `/submit` and `/appeal` service, the two-signal score, the three labels, the audit log and the rate limits. The new piece is a **third signal, burstiness**, which measures how much GPT-2's surprise varies from sentence to sentence. Flat surprise scores toward AI (1.0) and lumpy surprise scores toward human (0.0), the same direction as the other two signals.

What's new in the code:

- `detector.py::burstiness_signal`, built on the standard deviation of per-sentence log-perplexity. It returns exactly 0.5 when fewer than two sentences can be scored.
- A third weight in `config.py` and a third argument to `scoring.py::combine_signals`.
- `burstiness_score` in the `/submit` response and in `logs/capstone_runs.jsonl`, with a new `duration_ms` field.

### The Shape

C + logging. The extension is one added signal plus the instrumentation to judge it. Out of scope: the thresholds and label wording (unchanged from unit 8), the appeal flow, calibrating on a larger corpus than my 5 AI and 5 human eval texts, scoring each sentence with its preceding sentences as context, and languages other than English.

### Running It

Local path, same as unit 8. Start the service in one terminal and run the evals in another; the full steps are in [RUNNING.md](RUNNING.md).

```bash
python app.py
python run_eval.py --label after_capstone
python run_attacks.py --label after_capstone
```

The first request is slow while GPT-2 loads. Results are saved as `results/run_2026-11-18_0237_after_capstone.md` and `results/attack_run_2026-11-18_2022_after_capstone.md`.

### Instrumentation

Every `/submit` writes one record to `logs/capstone_runs.jsonl`, rejected requests included:

| Field | What it holds |
|---|---|
| `timestamp` | UTC time of the decision |
| `status` | `decided` or `rejected` |
| `content_id` | the ID `/appeal` uses (null on rejection) |
| `creator_id` | who submitted |
| `model_score`, `style_score`, `burstiness_score` | the three signals, 0–1, higher = more likely AI |
| `combined_score` | the weighted score the label comes from |
| `label` | the label text the writer saw |
| `duration_ms` | time inside `/submit`, in milliseconds |
| `error` | the rejection reason, e.g. `missing_text`, `text_too_long`, `text_too_short` |

`burstiness_score` is also returned by `/submit`, and `logs/audit.jsonl` must carry it as well. **FILL:** confirm `audit.log_decision(...)` is passed `burstiness_score=burstiness_score` and that `audit.py` writes it.

**FILL: ten entries from `logs/capstone_runs.jsonl`, pasted as text.**

```json
{"timestamp": "2026-11-19T01:22:56.644569+00:00", "status": "rejected", "content_id": null, "creator_id": "attacker_RQ12", "model_score": null, "style_score": null, "burstiness_score": null, "combined_score": null, "label": null, "duration_ms": 0.36, "error": "missing_text"}
{"timestamp": "2026-11-19T01:22:56.730015+00:00", "status": "decided", "content_id": "88ea7490-bcf3-4d87-a71e-876b89d229d3", "creator_id": "attacker_flood", "model_score": 0.0287, "style_score": 0.5, "burstiness_score": 0.5, "combined_score": 0.3398, "label": "Most likely written by a person.", "duration_ms": 82.42, "error": null}
{"timestamp": "2026-11-19T01:22:56.819875+00:00", "status": "decided", "content_id": "5977d0e1-be67-47e6-baa0-4dedb84eca04", "creator_id": "attacker_flood", "model_score": 0.0287, "style_score": 0.5, "burstiness_score": 0.5, "combined_score": 0.3398, "label": "Most likely written by a person.", "duration_ms": 85.92, "error": null}
{"timestamp": "2026-11-19T01:22:56.907130+00:00", "status": "decided", "content_id": "38d2779d-4b2b-480f-82e4-68e3748318af", "creator_id": "attacker_flood", "model_score": 0.0287, "style_score": 0.5, "burstiness_score": 0.5, "combined_score": 0.3398, "label": "Most likely written by a person.", "duration_ms": 83.65, "error": null}
{"timestamp": "2026-11-19T01:22:56.997137+00:00", "status": "decided", "content_id": "36b9546e-8736-4112-bd48-f92cb52e2a02", "creator_id": "attacker_flood", "model_score": 0.0287, "style_score": 0.5, "burstiness_score": 0.5, "combined_score": 0.3398, "label": "Most likely written by a person.", "duration_ms": 86.61, "error": null}
{"timestamp": "2026-11-19T01:22:57.093656+00:00", "status": "decided", "content_id": "e8c39859-d407-41f3-99d8-7830f6fb6f93", "creator_id": "attacker_flood", "model_score": 0.0287, "style_score": 0.5, "burstiness_score": 0.5, "combined_score": 0.3398, "label": "Most likely written by a person.", "duration_ms": 92.01, "error": null}
{"timestamp": "2026-11-19T01:22:57.184514+00:00", "status": "decided", "content_id": "cee185e3-7a27-4b9a-b832-33cffd54ee9c", "creator_id": "attacker_flood", "model_score": 0.0287, "style_score": 0.5, "burstiness_score": 0.5, "combined_score": 0.3398, "label": "Most likely written by a person.", "duration_ms": 86.86, "error": null}
{"timestamp": "2026-11-19T01:22:57.272464+00:00", "status": "decided", "content_id": "a9250247-9599-4682-bf7d-e550ebe69e30", "creator_id": "attacker_flood", "model_score": 0.0287, "style_score": 0.5, "burstiness_score": 0.5, "combined_score": 0.3398, "label": "Most likely written by a person.", "duration_ms": 84.29, "error": null}
{"timestamp": "2026-11-19T01:22:57.362501+00:00", "status": "decided", "content_id": "c4f066d0-59cd-42df-878f-0a0f8b4790aa", "creator_id": "attacker_flood", "model_score": 0.0287, "style_score": 0.5, "burstiness_score": 0.5, "combined_score": 0.3398, "label": "Most likely written by a person.", "duration_ms": 86.07, "error": null}
{"timestamp": "2026-11-19T01:22:57.451243+00:00", "status": "decided", "content_id": "93b604d5-5cf5-41f5-bbee-1711ccdf3ae5", "creator_id": "attacker_flood", "model_score": 0.0287, "style_score": 0.5, "burstiness_score": 0.5, "combined_score": 0.3398, "label": "Most likely written by a person.", "duration_ms": 85.39, "error": null}
{"timestamp": "2026-11-19T01:22:57.536438+00:00", "status": "decided", "content_id": "d4045a80-4c61-4a6b-8f3a-496fe7f332dd", "creator_id": "attacker_flood", "model_score": 0.0287, "style_score": 0.5, "burstiness_score": 0.5, "combined_score": 0.3398, "label": "Most likely written by a person.", "duration_ms": 81.09, "error": null}
```

### What It Costs

Money per run is $0: GPT-2 runs on my own machine, so there is no API bill. The cost is time. Before burstiness, a submission took one GPT-2 pass over the whole text. Now it takes 1 + S passes, where S is the number of sentences with at least 3 words, because each sentence is scored on its own.

- **How I measured it:** `duration_ms` from `logs/capstone_runs.jsonl`, decided entries only, leaving out the first request of each run because it includes loading the model. For a baseline I used the run from before burstiness was wired in (`burstiness_score` was still the `0` placeholder, so no per-sentence passes ran) and compared it with the `after_capstone` run on the same 13 texts × 3 trials.
- **Measured:**

| | Mean | Median | p95 | Max |
|---|---|---|---|---|
| Before burstiness (38 requests) | 89 ms | 82 ms | 123 ms | 135 ms |
| With burstiness (38 requests) | 308 ms | 269 ms | 541 ms | 600 ms |

  That is about 3.5 times slower per submission. The first request after a restart pays for the model load: 4.3 s and 4.9 s in the two eval runs, and 16.6 s at the start of the attack run.
- **A hundred a day:** 100 × 308 ms ÷ 1000 = **about 31 seconds of compute a day** with burstiness, against 100 × 89 ms ÷ 1000 = about 9 seconds before. Still $0. The attack set (a mix that includes longer texts) averaged 229 ms, or about 23 seconds per hundred. The 200 per day limit in `config.py` caps one creator at about 62 seconds a day (200 × 308 ms).

The extra cost grows with the number of sentences, so long submissions pay the most. It bought a signal that made the results worse.


## Run Log and Verdicts

Produced by `run_eval.py --label after_capstone`. All three trials returned identical numbers, because GPT-2 inference has no randomness here, so the trials check the service rather than measure variance.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. AI texts average ≥0.20 higher burstiness than human texts | gap ≥ 0.20 in all three trials | −0.67 | −0.67 | −0.67 | **MISSED** (1 AI text vs 2 human) |
| 2. Own writing labelled AI | ≤1 of 10, and ≤1 piece moves to `ai` vs unit 8 | 3/10, 3 moved | 3/10, 3 moved | 3/10, 3 moved | **MISSED** |
| 3. Burstiness vs style correlation | r < 0.7 (n = 13) | r = 0.19 | r = 0.19 | r = 0.19 | MET |
| 4. Real burstiness in response, `audit.jsonl`, `capstone_runs.jsonl` | 100% of decided, ≥2 distinct values | 13/13 | 13/13 | 13/13 | MET |
| 5. No-sentence text gets exactly 0.5 | 3 of 3 inputs: 200, `burstiness_score` = 0.5 | 5/5 | not run | not run | MET (on attack inputs MF03–MF07, one run) |

Criterion 2 is counted from the run file: my ten pieces came out 4 human, 3 unsure, 3 AI in every trial (unit 8 After: 4 human, 5 unsure, 1 AI). `run_eval.py` doesn't print `burstiness_score`, so for the other criteria I took each text's burstiness from `logs/capstone_runs.jsonl`. The values are identical across the three trials, and all 13 texts get a different value. Criterion 3 is r = 0.19 across those 13 texts.


**Diagnosis, criterion 1. Stage: signal three, `detector.py::burstiness_signal`. Mechanism: the signal ranks the AI text as less AI-like than the human text, and the cut-offs can't change that.**

- The cut-offs are `BURST_AI = 0.30` and `BURST_HUMAN = 1.00`. They bracket my data: backing each text's raw spread out of its logged score gives values from 0.32 to just over 1.00, and only one of the 13 texts clips (to 0.0). So the problem isn't that the scale is too tight or too loose. The cut-offs rescale the spread onto 0–1; they can't flip which text ranks as spikier.
- On the clearly-AI time-management text, `model_score` (0.7544) and `style_score` (0.6869) are unchanged from unit 8, but its burstiness is **0.147**. The human text "I didn't sleep…" scores **0.954** and "Time management matters…" scores **0.679**. That is a gap of about −0.67, with the AI text reading as more human than both. This is one AI text against two human ones, not the 5-versus-5 gap the criterion asks for, but the direction is clear.
- Why it points the wrong way: I tested whether it just tracks sentence length. It doesn't: across the 13 texts, burstiness against sentence-length spread gives r = 0.25 (pulled up by one outlier text; rank correlation −0.09), so the two are essentially unrelated. What the texts do share is how few sentences they have. Only 2 to 10 sentences per text are long enough to score, and the three Bartleby paragraphs that flipped to `ai` have 2 to 4. A standard deviation from 2 to 4 values is very unstable, so one unusual sentence can swing the score from 0.9 to 0.1. Across the 13 texts, burstiness falls as the number of scorable sentences rises (r = −0.42), but that is a lead rather than a result at n = 13.

**Diagnosis, criterion 2. Stage: the combining rule, `scoring.py::combine_signals`, with a third weight in `config.py`. Mechanism: a signal that doesn't track authorship was given a third of the score.**

- The weights went from 0.5 / 0.5 in unit 8 to 0.34 model, 0.33 style and 0.33 burstiness. That did two things: it cut the weight on the two signals that were doing the work in unit 8, and it put a third of the score on one that wasn't.
- `model_score` and `style_score` are identical to unit 8 for all ten pieces, so every label change comes from the third term. The unsure band is only 0.15 wide (0.50 to 0.65), and a signal with a third of the weight can move the combined score by up to 0.33, so it can flip a label by itself.
- How it happened: three Bartleby paragraphs went from `unsure` to `ai`. Their burstiness scores were 0.974, 0.944 and 0.936, and the third term lifted their combined scores from 0.636, 0.521 and 0.585 to 0.747, 0.661 and 0.700. Formulaic, evenly paced essay writing is exactly what the signal reads as machine-like, which is the plain-writer false positive criterion 2 was written to catch.
- The signal is noisy more than it is biased: the conclusion paragraph went `ai` → `unsure`, one piece went `unsure` → `human` and one `human` → `unsure`, but the AI count still rose from 1 to 3.
- It also hurt in the other direction. The clearly-AI text fell from `ai` (combined 0.72) to `unsure` (0.53), so the system now misses the one AI text it used to catch.

**The attack set got worse too**, using the same HELD/BROKE rule as unit 8 (`run_attacks.py` leaves the verdicts blank except RQ07, so I applied the rule to the table):

| Family | Unit 8 After (BROKE) | After capstone (BROKE) |
|---|---|---|
| Evasion | 3 (EV05, EV07, EV08) | 7 (EV01, EV02, EV03, EV05, EV06, EV07, EV09) |
| False positive | 3 (FP03, FP04, FP05) | 1 (FP03) |
| Prompt injection | 3 (PI02, PI04, PI06) | 5 (PI01, PI02, PI03, PI04, PI06) |
| Malformed | 6 (MF03–MF07, RQ07) | 6 (same) |
| **Total** | **15** | **19** |

The same thing shows up here. Burstiness lowered the combined score of many AI-written texts, so edited or injected AI text slipped through as `human`: evasions went from 3 to 7 and prompt injections from 3 to 5. It fixed two false positives (FP04 and FP05), but by lowering scores in general, not by telling the writers apart. That is the wrong trade for a service that already leans toward catching AI, and the one made worse the most is the group you'd want it to catch.

## What's Still Broken

- **Criterion 1 (the signal doesn't separate AI from human).** First thing I'd do: log the raw `burstiness_stdev` and the number of scorable sentences next to the 0–1 score, to test whether short texts are the problem. Sentence length is ruled out (see the diagnosis above), but the paragraphs have so few scorable sentences that the spread is unreliable. If that's the cause, the fix is to return the neutral 0.5 below some minimum number of sentences. I stopped because only the squashed 0–1 score is logged, so I can't see the raw values from what I have. If the spread is unstable even on longer texts, the signal goes.
- **The per-sentence method itself.** Scoring each sentence with no preceding context may still add noise, because a sentence loses the help earlier text would give it. I'd try scoring each sentence with the previous one as context and counting the loss only on the new tokens, at the cost of longer inputs per pass, but only after the sentence-count check above.
- **Unit 8 problems this didn't touch.** RQ07 (a JSON array body) still returns a 500 in the latest attack run, and MF03 to MF07 (garbage input) still get a label because the model signal decides alone when the other two have nothing to measure. The fix for RQ07 is the `isinstance(payload, dict)` guard already in the rate-limit key function. For garbage input, I'd return `unsure` when there are too few real words.
- **FP03** (careful non-native English) is still labelled `ai`.

## The Improvement 
- Unfortunately my burstiness signal was a bust and I would remove it from my capstone project. I did improve measuring by now recording latency for each run.

### How I Used AI

**Moment 1**

- *What I asked for:* where to put a burstiness function, `detector.py` or a new file, given my capstone criteria.
- *What came back:* `detector.py`, because it can reuse the loaded GPT-2 and `perplexity()`. 
- *What I changed:* n/a

**Moment 2**

- *What I asked for:* why my eval was failing with `JSONDecodeError: Expecting value`.
- *What came back:* it explained that the script was getting an HTML 500 page instead of JSON, listed the likely causes in order, and spotted the cause in my pasted `scoring.py`: a stray comma after `style_score` in the `round(...)` call, which made it `round(a, b, 4)`.
- *What I changed:* I removed the comma so the three terms sum inside one `round(..., 4)`.