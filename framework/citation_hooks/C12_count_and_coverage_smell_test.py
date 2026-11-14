# -*- coding: utf-8 -*-
"""Citation hook C12: count and coverage smell test.

One of the sixteen citation hooks run by cite_hooks_run.py (an agent, 11 Nov 2026). Written at the author's request.
"""

HOOK = {'id': 'C12',
 'on': ('github', 'zenodo', 'researchgate'),
 'title': 'count and coverage smell test',
 'rule': 'Read the bibliography as a referee would: a research paper with only a handful of references, or one '
         "citing none of the problem's well-known authors, surveys or recent work (last five years), is missing "
         "sources. His 21 Sep words: 'all relevant citation should be cited'."}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
