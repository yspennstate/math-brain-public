# -*- coding: utf-8 -*-
"""Citation hook C17: the credit ledger starts with the attack.

One of the ten credit hooks C17..C26 run by cite_hooks_run.py (an agent, 14 Nov 2026). Written at the author's request.
Attribution in the body stays a neutral present-tense clause (C13).
"""

HOOK = {'id': 'C17',
 'on': ('develop',),
 'title': 'the credit ledger starts with the attack',
 'rule': 'Before working on the problem, write CREDITS.md in the paper folder: who posed it, who proved the results '
         'the attack will lean on, and for each one the cite key, the result, and how we expect to use it. '
         'problem_recall.py, math_recall.py and a literature search fill it; the introduction and the AI declaration '
         'are later written from it.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
