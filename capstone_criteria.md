# Capstone acceptance criteria: Provenance Guard + burstiness signal

**What `burstiness_score` means here:** how much the model's surprise (per-sentence perplexity from GPT-2) varies from sentence to sentence. Flat, even surprise scores toward AI. Lumpy surprise, with some sentences very predictable and others not, scores toward human. It runs 0 (human) to 1 (AI), the same direction as `model_score` and `style_score`.

**How the five split:** criteria 1–3 test the burstiness signal and its false-positive impact. Criterion 4 covers logging. Criterion 5 is the failure path: what happens when burstiness can't be measured.

---

## 1. The AI texts average at least 0.20 higher burstiness than the human texts, in all three trials.

Across 5 clearly-AI texts and 5 clearly-human texts, the average `burstiness_score` of the AI set is at least 0.20 higher than the average of the human set. This has to hold in each of the three `run_eval.py` trials.

**Why this target:** A third signal only earns its place if it tells the two groups apart. I'm using 0.20 rather than the 0.25 I used for the combined score because burstiness is a noisier measure on short texts, so I'm asking for a clear gap, not a perfect one. If the gap is smaller than this, the signal is adding noise, and I'd rather drop it than weight it.

---

## 2. Adding burstiness doesn't add false positives: at most 1 of my own pieces is labelled AI.

On my 10 own-writing pieces in `scenarios.py`, at most 1 is labelled `ai` in each trial. Compared with the unit 8 After run (`results/run_2026-11-16_0152_after.md`), no more than 1 piece moves from `human` or `unsure` to `ai`.

**Why this target:** The expensive mistake is accusing a real writer, and this is the criterion that measures it. In unit 8, my Bartleby conclusion paragraph was the one piece labelled AI, and it was formulaic, not machine-written. A burstiness signal that rewards uniform sentences could push more of my plain, even-paced writing over the line. This criterion checks that the new signal doesn't make the false-positive problem worse.

---

## 3. Burstiness is a separate measurement, not a copy of the style signal: correlation below 0.7.

Across the 13 texts in my "my own writing" and "label coverage" scenarios, the Pearson correlation between `burstiness_score` and `style_score` is below 0.7 in each of the three trials.

**Why this target:** `stylometry.py` already measures sentence-length spread. If burstiness just reproduces that, the shape of the text gets counted twice and the combined score leans harder on one measurement than I intended. A correlation of 0.7 or more means the third signal adds almost nothing. With only 13 texts the number is rough, so I'll report it with the sample size.

---

## 4. Every decided submission records a real burstiness score in all three places it should appear.

For every submission that gets a `decided` status across the three `run_eval.py` trials, `burstiness_score` is present (not null, not the `0` placeholder) in the `/submit` response, in `logs/audit.jsonl`, and in `logs/capstone_runs.jsonl`. That is 100% of decided submissions. Within each trial, the 13 texts produce at least 2 distinct burstiness values, so the field isn't a constant.

**Why this target:** Unit 9 diagnoses problems from these logs. In unit 8 I learned that a problem which leaves no trace is one I can't find. The current code writes `burstiness_score = 0 #placeholder`, so a null-check alone would pass a field that is always zero. Requiring distinct values catches that case.

---

## 5. Text with no countable sentences gets a neutral burstiness of 0.5, never a crash or an extreme score.

Three inputs with no countable sentences: `"!!!!!"`, `". . . . . . . ."`, and a single 60-character word. Each is submitted three times, once per trial. In all 9 submissions, the response is a 200 with `burstiness_score` exactly `0.5` and a label. None return a 500, and none return `0` or `1`.

**Why this target:** A signal that can't measure something should say "no evidence," not an extreme. A score of 0 or 1 on text with no sentences would clear or accuse a writer for a reason that has nothing to do with their writing. The 0.5 fallback matches what `stylometry.py` already does for texts with fewer than two sentences. A 500 would also hide the failure from the writer, which is the same problem as the unit 7 crash on non-object JSON.
