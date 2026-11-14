# -*- coding: utf-8 -*-
"""Citation hook C01: check every citation before the paper goes up.

One of the sixteen citation hooks run by cite_hooks_run.py (an agent, 11 Nov 2026). His words, 11 Nov 2026 07:1x:
"when we write and publish math paper, i think we need to be more carful to cite all relevent source,s ... make 10-20
hooks ensureing that all agents that are about to submit a paper to github, researchgate o rzendono get a rptop telling
them to check all citaztions mand make sure that all revlenet citatios were cited"
"""

HOOK = {'id': 'C01',
 'massive': True,
 'on': ('github', 'zenodo', 'researchgate', 'prompt'),
 'cool': 600,
 'title': 'check every citation before the paper goes up',
 'rule': 'His order (11 Nov): before a paper goes to GitHub, ResearchGate or Zenodo, check ALL citations and make '
         'sure EVERY relevant source is cited. A missing citation on a posted paper is a public mistake under his '
         'name and is hard to take back (Zenodo DOIs are permanent). Do the checks below on the final .tex/.pdf now; '
         'if any fails, fix the paper and stop the upload until it passes.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
