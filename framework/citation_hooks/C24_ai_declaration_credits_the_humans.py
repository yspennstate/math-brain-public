# -*- coding: utf-8 -*-
"""Citation hook C24: the AI declaration credits the humans.

One of the ten credit hooks C17..C26 run by cite_hooks_run.py (an agent, 14 Nov 2026). His words, 14 Nov
2026 23:34:
"tell all of agents working on posting math manuscripts that i want the AI in the beginning of the paper, in the
introduction, and in the AI declaration to essentially acknowledge the mathematicians who together their work was
most important for the manuscripts, and say clearly what existed before, what is new, and how the new ideas are
related to old ideas, make 10 hooks about this in the brain during the math development and writing and
acknowledgment phase, and make sure that this kind of stuff is embedded in the papers, with citations, that way we
can give the humans who made the biggest contributions to the solutions ... them and their results credit"
Attribution in the body stays a neutral present-tense clause (his 15 Sep rule, C13).
"""

HOOK = {'id': 'C24',
 'on': ('credit', 'github', 'zenodo', 'researchgate'),
 'title': 'the AI declaration credits the humans',
 'rule': 'The AI declaration says in a few factual sentences which system produced what. It also names the '
         'mathematicians whose results the solution rests on, with citations, and says that those results are '
         'theirs: "The argument rests on the work of A [1], B and C [4]; the new steps are Sections 3 and 4." It is '
         'a short record, not a diary.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
