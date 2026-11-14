# -*- coding: utf-8 -*-
"""Citation hook C07: every reference is real and correct.

One of the sixteen citation hooks run by cite_hooks_run.py (an agent, 11 Nov 2026). Written at the author's request.
"""

HOOK = {'id': 'C07',
 'on': ('github', 'zenodo', 'researchgate', 'draft'),
 'title': 'every reference is real and correct',
 'rule': 'Check each bibliography entry against the real record: the DOI or arXiv id resolves, and authors, title, '
         'journal, volume, year and pages match it. No entry from memory alone; a reference that cannot be verified '
         'is removed or replaced, never guessed. Prefer the published version and give the arXiv id beside it.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
