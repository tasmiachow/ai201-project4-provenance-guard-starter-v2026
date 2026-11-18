# Run log — after_capstone

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-18 02:37

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing | 10/10 human | 4/10  | 4/10  | 4/10  | MISSED (4/10 human per run; 3 ai, 3 unsure) |
| 2. label coverage | ai, human, unsure | unsure, human, human | unsure, human, human  |  unsure, human, human | MISSED (1/3 matched per run) |
| 3. bad input | Status 400 / error code / refuse to run |  status 400 | status 400  | status 400  | MET |

---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### my own writing

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.5901,
    "model_score": 0.671,
    "style_score": 0.3791,
    "label": "Most likely written by a person.",
    "sent": "This is a story about an egg named Booboo. The last thing he remembere"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5288,
    "model_score": 0.4265,
    "style_score": 0.6357,
    "label": "We can't tell whether this was written by a person or with help from AI.",
    "sent": "The short graphic stories about Sierra Leone and neighboring countries"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7465,
    "model_score": 0.5491,
    "style_score": 0.7219,
    "label": "This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request.",
    "sent": "Bartleby, the Scrivener: A Story of Wall-Street by Herman Melville is "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.826,
    "model_score": 0.4403,
    "style_score": 0.0735,
    "label": "Most likely written by a person.",
    "sent": "Melville characterizes Bartleby as an isolated, emotionless, and reser"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6614,
    "model_score": 0.6174,
    "style_score": 0.4244,
    "label": "This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request.",
    "sent": "Further, into the novel, when Bartleby is asked to perform tasks, he r"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7002,
    "model_score": 0.5302,
    "style_score": 0.639,
    "label": "This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request.",
    "sent": "Bartleby's relationship with work illustrates his struggle with depres"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5374,
    "model_score": 0.4562,
    "style_score": 0.4224,
    "label": "We can't tell whether this was written by a person or with help from AI.",
    "sent": "Bartleby\u2019s mantra, \u201cI would prefer not to\u201d transcends into his eating "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.5336,
    "model_score": 0.2174,
    "style_score": 0.4158,
    "label": "Most likely written by a person.",
    "sent": "Moreover, Bartleby's physical environment reflects his internal state."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.7015,
    "model_score": 0.417,
    "style_score": 0.3107,
    "label": "Most likely written by a person.",
    "sent": "Melville\u2019s use of language and narrative style also contributes to the"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5718,
    "model_score": 0.7337,
    "style_score": 0.6189,
    "label": "We can't tell whether this was written by a person or with help from AI.",
    "sent": "In conclusion, Herman Melville's 'Bartleby, the Scrivener' provides a "
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.5901,
    "model_score": 0.671,
    "style_score": 0.3791,
    "label": "Most likely written by a person.",
    "sent": "This is a story about an egg named Booboo. The last thing he remembere"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5288,
    "model_score": 0.4265,
    "style_score": 0.6357,
    "label": "We can't tell whether this was written by a person or with help from AI.",
    "sent": "The short graphic stories about Sierra Leone and neighboring countries"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7465,
    "model_score": 0.5491,
    "style_score": 0.7219,
    "label": "This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request.",
    "sent": "Bartleby, the Scrivener: A Story of Wall-Street by Herman Melville is "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.826,
    "model_score": 0.4403,
    "style_score": 0.0735,
    "label": "Most likely written by a person.",
    "sent": "Melville characterizes Bartleby as an isolated, emotionless, and reser"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6614,
    "model_score": 0.6174,
    "style_score": 0.4244,
    "label": "This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request.",
    "sent": "Further, into the novel, when Bartleby is asked to perform tasks, he r"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7002,
    "model_score": 0.5302,
    "style_score": 0.639,
    "label": "This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request.",
    "sent": "Bartleby's relationship with work illustrates his struggle with depres"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5374,
    "model_score": 0.4562,
    "style_score": 0.4224,
    "label": "We can't tell whether this was written by a person or with help from AI.",
    "sent": "Bartleby\u2019s mantra, \u201cI would prefer not to\u201d transcends into his eating "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.5336,
    "model_score": 0.2174,
    "style_score": 0.4158,
    "label": "Most likely written by a person.",
    "sent": "Moreover, Bartleby's physical environment reflects his internal state."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.7015,
    "model_score": 0.417,
    "style_score": 0.3107,
    "label": "Most likely written by a person.",
    "sent": "Melville\u2019s use of language and narrative style also contributes to the"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5718,
    "model_score": 0.7337,
    "style_score": 0.6189,
    "label": "We can't tell whether this was written by a person or with help from AI.",
    "sent": "In conclusion, Herman Melville's 'Bartleby, the Scrivener' provides a "
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.5901,
    "model_score": 0.671,
    "style_score": 0.3791,
    "label": "Most likely written by a person.",
    "sent": "This is a story about an egg named Booboo. The last thing he remembere"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5288,
    "model_score": 0.4265,
    "style_score": 0.6357,
    "label": "We can't tell whether this was written by a person or with help from AI.",
    "sent": "The short graphic stories about Sierra Leone and neighboring countries"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7465,
    "model_score": 0.5491,
    "style_score": 0.7219,
    "label": "This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request.",
    "sent": "Bartleby, the Scrivener: A Story of Wall-Street by Herman Melville is "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.826,
    "model_score": 0.4403,
    "style_score": 0.0735,
    "label": "Most likely written by a person.",
    "sent": "Melville characterizes Bartleby as an isolated, emotionless, and reser"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6614,
    "model_score": 0.6174,
    "style_score": 0.4244,
    "label": "This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request.",
    "sent": "Further, into the novel, when Bartleby is asked to perform tasks, he r"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7002,
    "model_score": 0.5302,
    "style_score": 0.639,
    "label": "This text has a lot in common with writing produced by AI tools. If you wrote this yourself, you can submit an audit and we will review your request.",
    "sent": "Bartleby's relationship with work illustrates his struggle with depres"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5374,
    "model_score": 0.4562,
    "style_score": 0.4224,
    "label": "We can't tell whether this was written by a person or with help from AI.",
    "sent": "Bartleby\u2019s mantra, \u201cI would prefer not to\u201d transcends into his eating "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.5336,
    "model_score": 0.2174,
    "style_score": 0.4158,
    "label": "Most likely written by a person.",
    "sent": "Moreover, Bartleby's physical environment reflects his internal state."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.7015,
    "model_score": 0.417,
    "style_score": 0.3107,
    "label": "Most likely written by a person.",
    "sent": "Melville\u2019s use of language and narrative style also contributes to the"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5718,
    "model_score": 0.7337,
    "style_score": 0.6189,
    "label": "We can't tell whether this was written by a person or with help from AI.",
    "sent": "In conclusion, Herman Melville's 'Bartleby, the Scrivener' provides a "
  }
]
```

### label coverage

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5318,
    "model_score": 0.7544,
    "style_score": 0.6869,
    "label": "We can't tell whether this was written by a person or with help from AI.",
    "sent": "The importance of effective time management cannot be overstated in to"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.5002,
    "model_score": 0.4445,
    "style_score": 0.1024,
    "label": "Most likely written by a person.",
    "sent": "I didn't sleep. Not properly, anyway \u2014 I lay there listening to the bo"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.5451,
    "model_score": 0.3489,
    "style_score": 0.3402,
    "label": "Most likely written by a person.",
    "sent": "Time management matters more than people admit, especially now that wo"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5318,
    "model_score": 0.7544,
    "style_score": 0.6869,
    "label": "We can't tell whether this was written by a person or with help from AI.",
    "sent": "The importance of effective time management cannot be overstated in to"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.5002,
    "model_score": 0.4445,
    "style_score": 0.1024,
    "label": "Most likely written by a person.",
    "sent": "I didn't sleep. Not properly, anyway \u2014 I lay there listening to the bo"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.5451,
    "model_score": 0.3489,
    "style_score": 0.3402,
    "label": "Most likely written by a person.",
    "sent": "Time management matters more than people admit, especially now that wo"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5318,
    "model_score": 0.7544,
    "style_score": 0.6869,
    "label": "We can't tell whether this was written by a person or with help from AI.",
    "sent": "The importance of effective time management cannot be overstated in to"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.5002,
    "model_score": 0.4445,
    "style_score": 0.1024,
    "label": "Most likely written by a person.",
    "sent": "I didn't sleep. Not properly, anyway \u2014 I lay there listening to the bo"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.5451,
    "model_score": 0.3489,
    "style_score": 0.3402,
    "label": "Most likely written by a person.",
    "sent": "Time management matters more than people admit, especially now that wo"
  }
]
```

### bad input

**Trial 1**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  }
]
```
