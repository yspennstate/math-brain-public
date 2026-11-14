# -*- coding: utf-8 -*-
"""Citation hook C06: every borrowed lemma has a source.

One of the sixteen citation hooks run by cite_hooks_run.py (an agent, 11 Nov 2026). Written at the author's request.
"""

HOOK = {'id': 'C06',
 'on': ('github', 'zenodo', 'researchgate', 'draft'),
 'title': 'every borrowed lemma has a source',
 'rule': 'Every theorem, lemma, inequality, construction or technique taken from the literature carries a citation '
         'with its theorem or section number at the point it is used - including the standard ones (a named '
         'inequality, a coupling, a martingale or entropy method) and the originator of the method, not only a '
         'textbook.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
