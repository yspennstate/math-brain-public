# -*- coding: utf-8 -*-
"""Citation hook C21: say exactly what existed before.

One of the ten credit hooks C17..C26 run by cite_hooks_run.py (an agent, 14 Nov 2026). Written at the author's request.
Attribution in the body stays a neutral present-tense clause (C13).
"""

HOOK = {'id': 'C21',
 'on': ('writing', 'github', 'zenodo', 'researchgate'),
 'title': 'say exactly what existed before',
 'rule': 'One paragraph of the introduction states the prior results precisely: the best bound with its constant, '
         'the special cases that were settled, the conjecture and who made it, the numerical evidence, each with a '
         'citation. A reader should be able to say from this paragraph alone where the problem stood before this '
         'paper.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
