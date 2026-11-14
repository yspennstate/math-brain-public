# -*- coding: utf-8 -*-
"""Citation hook C06: every borrowed lemma has a source.

One of the sixteen citation hooks run by cite_hooks_run.py (an agent, 11 Nov 2026). His words, 11 Nov 2026 07:1x:
"when we write and publish math paper, i think we need to be more carful to cite all relevent source,s ... make 10-20
hooks ensureing that all agents that are about to submit a paper to github, researchgate o rzendono get a rptop telling
them to check all citaztions mand make sure that all revlenet citatios were cited"
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
