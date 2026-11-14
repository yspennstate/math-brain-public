# -*- coding: utf-8 -*-
"""Citation hook C22: say exactly what is new.

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

HOOK = {'id': 'C22',
 'on': ('writing', 'github', 'zenodo', 'researchgate'),
 'title': 'say exactly what is new',
 'rule': 'One paragraph of the introduction says what this paper adds, stated against the paragraph before it: '
         '"Theorem 1.2 removes the logarithm in [7]"; "the case d >= 3 was open." If a result is a new proof of a '
         'known theorem, it says so.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
