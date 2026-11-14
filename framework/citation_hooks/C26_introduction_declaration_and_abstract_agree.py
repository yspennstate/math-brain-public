# -*- coding: utf-8 -*-
"""Citation hook C26: introduction, declaration and abstract agree.

One of the ten credit hooks C17..C26 run by cite_hooks_run.py (an agent, 14 Nov 2026). Written at the author's request.
Attribution in the body stays a neutral present-tense clause (C13).
"""

HOOK = {'id': 'C26',
 'on': ('github', 'zenodo', 'researchgate'),
 'title': 'introduction, declaration and abstract agree',
 'rule': 'Before posting, read the abstract, the introduction and the AI declaration side by side. They name the '
         'same people, agree on what was known and what is new, and the abstract never claims as new anything the '
         'introduction credits to someone else. CREDITS.md and the bibliography agree with all three.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
