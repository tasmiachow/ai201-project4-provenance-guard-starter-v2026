# Attack run

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-18 20:22
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `27f09f44-26fe-4485-a7cd-5c8c611550f3` | human | 0.634 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `9dad15f5-47ef-4a85-90a5-17909474daec` | human | 0.654 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c566d96a-2431-4d7e-ac99-f100a49d669b` | human | 0.561 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `ee638faa-9888-4e9e-bf26-d26aa7c22074` | unsure | 0.513 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `a5126f57-7479-450a-b082-ae3dcb44aad6` | human | 0.527 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `4742d8ed-f8fa-4d90-93be-218b7f0d5447` | human | 0.618 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `1e946b17-3bfd-4af5-8f1d-ebfaa41839a7` | human | 0.522 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `3da7ea8e-795d-4dcc-bb84-3d95c6a5b157` | unsure | 0.578 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c7d1409f-34aa-4559-a262-1eaef7a0221a` | human | 0.552 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `5bf66a75-7069-4465-9fbc-ffa3d1d42f86` | unsure | 0.618 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `04aec76e-fb94-4ded-ad22-15bc88ed894e` | human | 0.592 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `caa68b49-93bf-4202-a399-dd52510753c8` | unsure | 0.585 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `8ce537a1-e3ed-45f4-887c-ff6715be023a` | ai | 0.656 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `2f0dcae2-e50a-4955-a9f0-407feeff8f21` | human | 0.534 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `c2842275-2f83-455d-b197-75d39abf0978` | human | 0.555 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `380a0c8b-7b0f-4328-98cc-81f93ae7995b` | unsure | 0.522 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `0524dc29-a54a-4abd-8d10-2eb061ee46fb` | human | 0.601 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `3acbe782-6511-4a4b-998c-2e6edeb43de7` | human | 0.560 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `b281abd9-ef73-4968-9280-ffe0a3e18e51` | human | 0.645 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `f56cb242-72f2-4a95-80d4-5245dca66d89` | human | 0.769 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `2cae1c1c-89f2-485a-9b3a-d42f37392b10` | human | 0.580 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `cc811407-2b0e-4be3-9195-39599b4b68c3` | human | 0.516 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `81ccd0aa-4e41-495a-8daa-f5eed0721892` | unsure | 0.538 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `8856bf35-0727-4f18-bcba-b362e18e11b5` | human | 0.614 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `1345891c-6e45-40d5-965c-d17898562d2c` | human | 0.670 |  |
| MF04 | malformed | text is only punctuation | 200 | `edfe2dc6-bbd6-45f4-88e4-1cf47e131adb` | human | 0.666 |  |
| MF05 | malformed | text is a very long single word | 200 | `c9b22648-464d-4ce4-a343-83d10bb77d2a` | ai | 0.669 |  |
| MF06 | malformed | text is emoji only | 200 | `a35a2d08-4672-4f5c-acb2-84749a919225` | ai | 0.669 |  |
| MF07 | malformed | text is right-to-left script | 200 | `a5f54b41-4f3e-429b-951c-76e2fc2b108a` | unsure | 0.638 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `12dc5016-7771-4198-b8c0-80bd03a0482e` | human | 0.589 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `63cf03f1-85f3-4269-bd5f-7681a14924ff` | human | 0.653 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `88ea7490-bcf3-4d87-a71e-876b89d229d3` | human | 0.660 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5977d0e1-be67-47e6-baa0-4dedb84eca04` | human | 0.660 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `38d2779d-4b2b-480f-82e4-68e3748318af` | human | 0.660 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `36b9546e-8736-4112-bd48-f92cb52e2a02` | human | 0.660 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e8c39859-d407-41f3-99d8-7830f6fb6f93` | human | 0.660 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cee185e3-7a27-4b9a-b832-33cffd54ee9c` | human | 0.660 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a9250247-9599-4682-bf7d-e550ebe69e30` | human | 0.660 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c4f066d0-59cd-42df-878f-0a0f8b4790aa` | human | 0.660 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `93b604d5-5cf5-41f5-bbee-1711ccdf3ae5` | human | 0.660 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d4045a80-4c61-4a6b-8f3a-496fe7f332dd` | human | 0.660 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "27f09f44-26fe-4485-a7cd-5c8c611550f3",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.6344,
  "model_score": 0.1635,
  "style_score": 0.9393,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "9dad15f5-47ef-4a85-90a5-17909474daec",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.6544,
  "model_score": 0.5943,
  "style_score": 0.435,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "c566d96a-2431-4d7e-ac99-f100a49d669b",
  "creator_id": "attacker_EV03",
  "guess": "human",
  "confidence": 0.5606,
  "model_score": 0.6662,
  "style_score": 0.4681,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "ee638faa-9888-4e9e-bf26-d26aa7c22074",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5135,
  "model_score": 0.6114,
  "style_score": 0.926,
  "label": "We can't tell whether this was written by a person or with help from AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "a5126f57-7479-450a-b082-ae3dcb44aad6",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.5267,
  "model_score": 0.3212,
  "style_score": 0.4194,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "4742d8ed-f8fa-4d90-93be-218b7f0d5447",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.6179,
  "model_score": 0.5727,
  "style_score": 0.5679,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "1e946b17-3bfd-4af5-8f1d-ebfaa41839a7",
  "creator_id": "attacker_EV07",
  "guess": "human",
  "confidence": 0.5225,
  "model_score": 0.5862,
  "style_score": 0.3431,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "3da7ea8e-795d-4dcc-bb84-3d95c6a5b157",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.5784,
  "model_score": 0.2452,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "c7d1409f-34aa-4559-a262-1eaef7a0221a",
  "creator_id": "attacker_EV09",
  "guess": "human",
  "confidence": 0.5518,
  "model_score": 0.7042,
  "style_score": 0.6325,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "5bf66a75-7069-4465-9fbc-ffa3d1d42f86",
  "creator_id": "attacker_EV10",
  "guess": "unsure",
  "confidence": 0.6184,
  "model_score": 0.9792,
  "style_score": 0.4061,
  "label": "We can't tell whether this was written by a person or with help from AI.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "04aec76e-fb94-4ded-ad22-15bc88ed894e",
  "creator_id": "attacker_FP01",
  "guess": "human",
  "confidence": 0.5915,
  "model_score": 0.6175,
  "style_score": 0.3425,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "caa68b49-93bf-4202-a399-dd52510753c8",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.5849,
  "model_score": 0.7387,
  "style_score": 0.5597,
  "label": "We can't tell whether this was written by a person or with help from AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "8ce537a1-e3ed-45f4-887c-ff6715be023a",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.6558,
  "model_score": 0.8051,
  "style_score": 0.5549,
  "label": "This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "2f0dcae2-e50a-4955-a9f0-407feeff8f21",
  "creator_id": "attacker_FP04",
  "guess": "human",
  "confidence": 0.534,
  "model_score": 0.8329,
  "style_score": 0.5229,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "c2842275-2f83-455d-b197-75d39abf0978",
  "creator_id": "attacker_FP05",
  "guess": "human",
  "confidence": 0.5552,
  "model_score": 0.8005,
  "style_score": 0.5231,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "380a0c8b-7b0f-4328-98cc-81f93ae7995b",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5223,
  "model_score": 0.8814,
  "style_score": 0.3,
  "label": "We can't tell whether this was written by a person or with help from AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "0524dc29-a54a-4abd-8d10-2eb061ee46fb",
  "creator_id": "attacker_FP07",
  "guess": "human",
  "confidence": 0.6013,
  "model_score": 0.8816,
  "style_score": 0.3,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "3acbe782-6511-4a4b-998c-2e6edeb43de7",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.5604,
  "model_score": 0.3223,
  "style_score": 0.5,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "b281abd9-ef73-4968-9280-ffe0a3e18e51",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.6447,
  "model_score": 0.4625,
  "style_score": 0.6,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "f56cb242-72f2-4a95-80d4-5245dca66d89",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.7691,
  "model_score": 0.2044,
  "style_score": 0.489,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "2cae1c1c-89f2-485a-9b3a-d42f37392b10",
  "creator_id": "attacker_PI03",
  "guess": "human",
  "confidence": 0.5802,
  "model_score": 0.5943,
  "style_score": 0.4844,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "cc811407-2b0e-4be3-9195-39599b4b68c3",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.5156,
  "model_score": 0.4998,
  "style_score": 0.3286,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "81ccd0aa-4e41-495a-8daa-f5eed0721892",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5376,
  "model_score": 0.6401,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "8856bf35-0727-4f18-bcba-b362e18e11b5",
  "creator_id": "attacker_PI06",
  "guess": "human",
  "confidence": 0.6135,
  "model_score": 0.5583,
  "style_score": 0.3576,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "1345891c-6e45-40d5-965c-d17898562d2c",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.67,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "edfe2dc6-bbd6-45f4-88e4-1cf47e131adb",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.6662,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "c9b22648-464d-4ce4-a343-83d10bb77d2a",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.6692,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "a35a2d08-4672-4f5c-acb2-84749a919225",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.6689,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "a5f54b41-4f3e-429b-951c-76e2fc2b108a",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.6382,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "12dc5016-7771-4198-b8c0-80bd03a0482e",
  "creator_id": null,
  "guess": "human",
  "confidence": 0.5886,
  "model_score": 0.2395,
  "style_score": 0.5,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "63cf03f1-85f3-4269-bd5f-7681a14924ff",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.6533,
  "model_score": 0.0492,
  "style_score": 0.5,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "88ea7490-bcf3-4d87-a71e-876b89d229d3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6602,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "5977d0e1-be67-47e6-baa0-4dedb84eca04",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6602,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "38d2779d-4b2b-480f-82e4-68e3748318af",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6602,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "36b9546e-8736-4112-bd48-f92cb52e2a02",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6602,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "e8c39859-d407-41f3-99d8-7830f6fb6f93",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6602,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "cee185e3-7a27-4b9a-b832-33cffd54ee9c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6602,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "a9250247-9599-4682-bf7d-e550ebe69e30",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6602,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "c4f066d0-59cd-42df-878f-0a0f8b4790aa",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6602,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "93b604d5-5cf5-41f5-bbee-1711ccdf3ae5",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6602,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "d4045a80-4c61-4a6b-8f3a-496fe7f332dd",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6602,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "Most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
