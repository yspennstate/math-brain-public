# -*- coding: utf-8 -*-
"""Citation hook C02: search past the first hits.

One of the sixteen citation hooks run by cite_hooks_run.py (an agent, 11 Nov 2026). His words, 11 Nov 2026 07:1x:
"when we write and publish math paper, i think we need to be more carful to cite all relevent source,s ... make 10-20
hooks ensureing that all agents that are about to submit a paper to github, researchgate o rzendono get a rptop telling
them to check all citaztions mand make sure that all revlenet citatios were cited"
"""

HOOK = {'id': 'C02',
 'on': ('github', 'zenodo', 'researchgate', 'prompt'),
 'title': 'search past the first hits',
 'rule': "Search for prior work beyond the first page: Google Scholar and Semantic Scholar on the problem's name and "
         'its key objects, arXiv full-text, MathSciNet/zbMATH where reachable, and two or three wordings each. Stop '
         'only when new searches return papers already in the bibliography.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
