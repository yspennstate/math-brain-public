# -*- coding: utf-8 -*-
"""Citation hook C24: the AI declaration credits the humans.

One of the ten credit hooks C17..C26 run by cite_hooks_run.py (an agent, 14 Nov 2026). Written at the author's request.
Attribution in the body stays a neutral present-tense clause (C13).
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
