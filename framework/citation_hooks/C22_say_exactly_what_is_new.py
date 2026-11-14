# -*- coding: utf-8 -*-
"""Citation hook C22: say exactly what is new.

One of the ten credit hooks C17..C26 run by cite_hooks_run.py (an agent, 14 Nov 2026). Written at the author's request.
Attribution in the body stays a neutral present-tense clause (C13).
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
