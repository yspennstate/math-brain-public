# -*- coding: utf-8 -*-
"""Citation hook C25: credit is accurate and in proportion.

One of the ten credit hooks C17..C26 run by cite_hooks_run.py (an agent, 14 Nov 2026). Written at the author's request.
Attribution in the body stays a neutral present-tense clause (C13).
"""

HOOK = {'id': 'C25',
 'on': ('credit', 'writing', 'github', 'zenodo', 'researchgate'),
 'title': 'credit is accurate and in proportion',
 'rule': 'Credit the people whose results carry the proof, the most important first, and not a list of famous names. '
         'Every person named in the introduction or the declaration has a cited work in the bibliography, and the '
         'cited work really contains what we credit to it. Check the theorem number and read the statement.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
