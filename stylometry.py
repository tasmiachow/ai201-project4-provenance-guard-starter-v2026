"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.

    Scale: 0 upward, usually 0.2–1.0. Higher means more varied, which reads
    as more human. Under two sentences there's nothing to compare, so 0.0.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]   # "..." alone isn't a sentence

    if len(lengths) < 2:
        return 0.0

    return round(statistics.stdev(lengths) / statistics.mean(lengths), 4)


# Spread cut-offs. At or below SPREAD_AI sentences march in step (AI-like);
# at or above SPREAD_HUMAN they're lumpy (human-like); a straight line between.
# Calibration: stiff AI-style paragraph 0.12, plain human 0.20, lumpy human 1.47.
SPREAD_AI = 0.10
SPREAD_HUMAN = 0.50


def _ramp(value: float, ai_end: float, human_end: float) -> float:
    """
    Place a raw measure on 0–1 between its two cut-offs: 1.0 at ai_end, 0.0 at
    human_end, a straight line between. Works whichever way round they are.
    """
    position = (value - ai_end) / (human_end - ai_end)
    return round(1.0 - min(max(position, 0.0), 1.0), 4)


def spread_score(text: str) -> float:
    """
    sentence_length_spread flipped onto 0–1. **Higher means more likely AI.**

    Under two sentences returns 0.5: no spread to measure is not evidence of
    AI, and calling it 1.0 would accuse every one-line submission.
    """
    if len([s for s in sentences(text) if words(s)]) < 2:
        return 0.5
    return _ramp(sentence_length_spread(text), SPREAD_AI, SPREAD_HUMAN)


# Words per window. Plain TTR falls as text gets longer, so it's averaged over
# a sliding window of this many words instead, which keeps lengths comparable.
TTR_WINDOW = 40


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words.

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.

    So past TTR_WINDOW words this is the average TTR of every TTR_WINDOW-word
    stretch (a moving-average TTR). Shorter text gets the plain ratio.
    """
    tokens = words(text)
    if not tokens:
        return 0.0
    if len(tokens) <= TTR_WINDOW:
        return round(len(set(tokens)) / len(tokens), 4)

    windows = len(tokens) - TTR_WINDOW + 1
    total = sum(len(set(tokens[i:i + TTR_WINDOW])) for i in range(windows))
    return round(total / (windows * TTR_WINDOW), 4)


# TTR cut-offs. These run the OPPOSITE way to the module docstring's guess:
# on the calibration texts the AI-style ones had the wider vocabulary
# (0.87–0.92) and every human one sat at 0.83–0.84. Check against real AI.
TTR_AI = 0.90
TTR_HUMAN = 0.83


def ttr_score(text: str) -> float:
    """type_token_ratio onto 0–1. **Higher means more likely AI.**"""
    return _ramp(type_token_ratio(text), TTR_AI, TTR_HUMAN)


# Full stops and commas are left out: everyone uses them. These are the marks
# that vary between writers. Apostrophes are left out too, because "he'd"
# would count as punctuation.
EXPRESSIVE_PUNCTUATION = r"[;:!?()\"“”—–]"


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length.

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.

    Counts only EXPRESSIVE_PUNCTUATION, per word. 0 upward, usually under 0.1.
    """
    tokens = words(text)
    if not tokens:
        return 0.0
    marks = re.findall(EXPRESSIVE_PUNCTUATION, text)
    return round(len(marks) / len(tokens), 4)


# Punctuation cut-offs. The AI-style calibration texts used none of these
# marks at all; the two human ones with any voice used about 0.06–0.07.
PUNCT_AI = 0.0
PUNCT_HUMAN = 0.06


def punctuation_score(text: str) -> float:
    """punctuation_density onto 0–1. **Higher means more likely AI.**"""
    return _ramp(punctuation_density(text), PUNCT_AI, PUNCT_HUMAN)


# ── Combining them ───────────────────────────────────────────────────────────

# How much each measure counts. They add to 1. Spread gets the most because it
# was the only one that put a real story clearly on the human side.
WEIGHT_SPREAD = 0.4
WEIGHT_TTR = 0.3
WEIGHT_PUNCTUATION = 0.3

# Below this many words style has too little to go on: every word is unique and
# there's no room for punctuation, so a short note would read as AI.
MIN_STYLE_WORDS = TTR_WINDOW


def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.**

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.

    Each measure is first put on 0–1 between its own two cut-offs, flipped so
    higher always means AI (all three needed flipping or setting that way),
    then they're averaged with the weights above. Under MIN_STYLE_WORDS words
    it scores a neutral 0.5 rather than guess.
    """
    if len(words(text)) < MIN_STYLE_WORDS:
        return 0.5

    score = (
        WEIGHT_SPREAD * spread_score(text)
        + WEIGHT_TTR * ttr_score(text)
        + WEIGHT_PUNCTUATION * punctuation_score(text)
    )
    return round(score, 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"                         raw      0-1 (higher = more likely AI)")
    print(f"sentence_length_spread   {sentence_length_spread(text):<8} {spread_score(text)}")
    print(f"type_token_ratio         {type_token_ratio(text):<8} {ttr_score(text)}")
    print(f"punctuation_density      {punctuation_density(text):<8} {punctuation_score(text)}")
    print(f"style_signal                      {style_signal(text)}")
