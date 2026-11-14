# -*- coding: utf-8 -*-
"""Citation hook C19: mark each statement known, adapted or new.

One of the ten credit hooks C17..C26 run by cite_hooks_run.py (an agent, 14 Nov 2026). Written at the author's request.
Attribution in the body stays a neutral present-tense clause (C13).
"""

HOOK = {'id': 'C19',
 'on': ('develop', 'writing'),
 'title': 'mark each statement known, adapted or new',
 'rule': 'Label every theorem, lemma and proposition as known (cited, statement as published), adapted (cited, and '
         'say what changed) or new. Before the paper is written up, keep the label next to each statement in the '
         'draft or in CREDITS.md. Nothing reaches the introduction as new without passing through this list.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
