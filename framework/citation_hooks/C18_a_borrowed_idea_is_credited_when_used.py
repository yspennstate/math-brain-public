# -*- coding: utf-8 -*-
"""Citation hook C18: a borrowed idea is credited when it is used.

One of the ten credit hooks C17..C26 run by cite_hooks_run.py (an agent, 14 Nov 2026). Written at the author's request.
Attribution in the body stays a neutral present-tense clause (C13).
"""

HOOK = {'id': 'C18',
 'on': ('develop', 'draft'),
 'title': 'a borrowed idea is credited when it is used',
 'rule': "The moment a proof uses someone else's lemma, estimate, construction or trick, add a CREDITS.md line "
         '(name, cite key, which step) and put the \\cite at that step in the .tex. Credit written at the end is '
         'credit forgotten.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
