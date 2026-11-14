# -*- coding: utf-8 -*-
"""Citation hook C11: is the result already in the literature.

One of the sixteen citation hooks run by cite_hooks_run.py (an agent, 11 Nov 2026). His words, 11 Nov 2026 07:1x:
"when we write and publish math paper, i think we need to be more carful to cite all relevent source,s ... make 10-20
hooks ensureing that all agents that are about to submit a paper to github, researchgate o rzendono get a rptop telling
them to check all citaztions mand make sure that all revlenet citatios were cited"
"""

HOOK = {'id': 'C11',
 'on': ('github', 'zenodo', 'researchgate'),
 'title': 'is the result already in the literature',
 'rule': 'Search for the RESULT itself, not only the problem: the main formula, the constant, the extremal example, '
         'the statement in other words. If it is already published (even as a remark or an exercise), cite it, '
         'attribute it and restate our contribution (a new proof, an extension) - never present a known result as '
         'new.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
