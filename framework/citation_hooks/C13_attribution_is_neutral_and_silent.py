# -*- coding: utf-8 -*-
"""Citation hook C13: attribution is neutral and silent.

One of the sixteen citation hooks run by cite_hooks_run.py (an agent, 11 Nov 2026). His words, 11 Nov 2026 07:1x:
"when we write and publish math paper, i think we need to be more carful to cite all relevent source,s ... make 10-20
hooks ensureing that all agents that are about to submit a paper to github, researchgate o rzendono get a rptop telling
them to check all citaztions mand make sure that all revlenet citatios were cited"
"""

HOOK = {'id': 'C13',
 'on': ('github', 'zenodo', 'researchgate', 'draft'),
 'title': 'attribution is neutral and silent',
 'rule': "State attributions in one neutral present-tense clause ('The operator W was introduced by Jamilov [4]'). A "
         'corrected or added citation is simply there: no sentence about a search, an earlier version or a '
         'correction (his 15 Sep paper rule).'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
