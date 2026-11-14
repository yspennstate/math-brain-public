# -*- coding: utf-8 -*-
"""Citation hook C20: the introduction names the mathematicians.

One of the ten credit hooks C17..C26 run by cite_hooks_run.py (an agent, 14 Nov 2026). Written at the author's request.
Attribution in the body stays a neutral present-tense clause (C13).
"""

HOOK = {'id': 'C20',
 'on': ('writing', 'github', 'zenodo', 'researchgate'),
 'title': 'the introduction names the mathematicians',
 'rule': 'In its first page, the introduction names the people whose work the paper most depends on, each with a '
         'citation: "The problem was posed by Aldous [2]. Lyons and Peres [11] proved ... and the method here '
         'follows Benjamini and Schramm [4]." These are their names and their results, not "previous work" or "the '
         'literature".'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
