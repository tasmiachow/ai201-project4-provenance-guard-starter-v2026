"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            "This is a story about an egg named Booboo. The last thing he remembered was being on a lush farm, seeing the beautiful blue sky, and feeling the gentle breeze of the wind. When he woke, he was in a completely dark, isolated space, and he was freezing. Before Booboo was about to be devastated, the door opened, and he saw the light appear. He was surrounded by other objects he’d never seen before: a ketchup bottle, a chocolate, yogurt, etc. More importantly, he saw a little girl picking out the yogurt before she slammed the door shut, turning his vision back into darkness. When the fridge closed, Mr.Ketchup Bottle had flipped the light switch back on. The other foods were all chatting and dancing. He was amazed, he was right on the top shelf. As Booboo made his way down, he asked Mr.Ketchup Bottle, 'Hey, are you cold?'",
            "The short graphic stories about Sierra Leone and neighboring countries all shared the same fate of the inaccessibility of healthcare. Unfortunately, the women in the graphics went through many tragedies and traumas before getting access to proper medical attention. The societal pressures women face also add to their injustices and leave them to navigate painful situations alone. The short story, The Devil at My Door from Kadiatu explores how society has conspired against women to explain the unknown or for personal motives. A similar example would be the Salem Witch Trials. Women were sentenced to death based on mindless accusations and rumors. Thankfully in Kadiatu’s villages, the ignorance wasn’t violent and she was able to receive proper child-birthing assistance. The experiences that these women had to face while reaching motherhood, were devastating and unfortunately, many women in these villages face the same issues. The villagers' ignorance and lack of medical resources resulted in many casualties. I hope that one day, society can become more resilient to fear-mongering and women can stop being the scapegoat.",
            # 3–10 — Bartleby essay, split into eight pieces (one per paragraph;
            # the long second paragraph is split in two).
            'Bartleby, the Scrivener: A Story of Wall-Street by Herman Melville is a short fictional story about the complexities of emptiness. Throughout the novel, Bartleby becomes increasingly unresponsive until he refuses to live. His descent into apathy and withdrawal from society can be interpreted as the progression of depression.',
            "Melville characterizes Bartleby as an isolated, emotionless, and reserved man. At the beginning of the story, Bartleby efficiently completes all his mundane tasks. The narrator starts to describe his work as “silent, pale, and mechanical” (Melville, 6) Bartleby’s dissociation from his work mirrors his internal void. Melville's choice of pale to describe Bartleby’s work can signify sickness.",
            "Further, into the novel, when Bartleby is asked to perform tasks, he responds with, “I would prefer not to.” This phrase, repeated throughout the story, serves as a metaphor for Bartleby's withdrawal from societal norms.  It indicates a passive resistance to the demands of society, which aligns with the actions of those experiencing depression.",
            "Bartleby's relationship with work illustrates his struggle with depression. He initially excels as a scrivener but gradually succumbs to a paralyzing sense of indifference. He disengages with his tasks, allowing them to accumulate and go unfinished. This withdrawal from productive activities is a common symptom of depression, where even once enjoyable or manageable tasks become loathsome.",
            'Bartleby’s mantra, “I would prefer not to” transcends into his eating habits. He survived off of a few biscuits and morsels of cheese but then continuously resisted eating. His passive decline to eat or dine is often a symptom of depression but also reveals his refusal to continue living. Bartleby’s detached state is what allowed him to starve to death. The narrator further describes Bartleby as “sedate, motionless, and still” which can be used to describe a dead man walking. The word motionless can showcase Bartlby’s state of mind, that although he is in a living realm, he has already passed on to the next life.',
            "Moreover, Bartleby's physical environment reflects his internal state. The gloomy office space he inhabits is described as “pallidly neat, pitiably respectable, incurably forlorn” (Melville, 6). —---(add more) This setting contributes to a sense of entrapment, emphasizing his inability to escape his own despair.",
            "Melville’s use of language and narrative style also contributes to the portrayal of Bartleby's depression. The narrator's tone is often detached and clinical, reflecting the dehumanizing environment of Wall Street. This tone serves to heighten the contrast with Bartleby's emotional state, emphasizing his alienation from the world around him. —contrast it with turkey and nippers",
            "In conclusion, Herman Melville's 'Bartleby, the Scrivener' provides a compelling exploration of depression through the character of Bartleby. Through his isolation, disengagement from work, and refusal to conform, Bartleby embodies the struggles of an individual facing profound turmoil. Melville's adept use of language and setting further showcases Bartleby's emotional state. The story sheds light on the inner workings of a mind grappling with depression.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 2,
        # Inputs spread across your score range, so you can check all three
        # labels are actually reachable.
        "texts": [
            "The importance of effective time management cannot be overstated in today's fast-paced work environment. Professionals who develop strong organizational habits are better positioned to meet deadlines and reduce stress. There are several key strategies that can help individuals improve their productivity. First, prioritization is essential. By identifying the most important tasks and addressing them first, workers can ensure that critical objectives are met. Second, minimizing distractions plays a significant role. Setting aside dedicated blocks of time for concentrated work is widely considered beneficial. Finally, regular breaks are important for maintaining performance.",
            "I didn't sleep. Not properly, anyway — I lay there listening to the boiler tick and thinking about the thing I'd said to Marcus at the pub, which was stupid, and which he will absolutely bring up again. Twice now. So: coffee, and the long way round to work, and a plan. The plan lasted until about ten past nine, when Priya asked how the weekend was and I said \"fine\" in the voice that means it wasn't, and she put her mug down and looked at me. That's the trouble with Priya. She notices.",
            "Time management matters more than people admit, especially now that work moves as fast as it does. If you're organised you hit deadlines, and you're less frazzled doing it. A few things actually help. Prioritise — work out what genuinely matters and do that first. Cut the interruptions; notifications wreck focus and the damage is worse than it feels at the time. And take breaks, short ones, often.",
        ],
    },
    # A bad-input criterion looks like this. Uncomment and adjust if that's one
    # of your five — these are raw request bodies, sent exactly as written.
    #
    {
        "name": "bad input",
        "criterion": 3,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},          # no text field at all
            {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
            {"text": None, "creator_id": "eval_bad_null"},
        ],
    },

    # TODO: add what your remaining criteria need.
    #
    # A criterion about the appeal path can't be tested by sending text alone;
    # it needs a submission first and then an appeal against the content_id
    # that came back. You'll need to test that one by hand, or extend this file
    # and run_eval.py to do it. Saying which you did is part of the write-up.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
