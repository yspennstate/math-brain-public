# -*- coding: utf-8 -*-
"""Citation hook C03: cite where the problem was posed.

One of the sixteen citation hooks run by cite_hooks_run.py (an agent, 11 Nov 2026). Written at the author's request.
"""

HOOK = {'id': 'C03',
 'on': ('github', 'zenodo', 'researchgate'),
 'title': 'cite where the problem was posed',
 'rule': 'The paper, book or problem list where the question was first posed is cited, with its exact problem '
         "number, section or page (e.g. 'Problem 24 in [3]'), and so is the source the list took it from if it is a "
         'reprint.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
