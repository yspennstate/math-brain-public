# -*- coding: utf-8 -*-
"""Citation hook C15: ResearchGate gets the final PDF and its references.

One of the sixteen citation hooks run by cite_hooks_run.py (an agent, 11 Nov 2026). His words, 11 Nov 2026 07:1x:
"when we write and publish math paper, i think we need to be more carful to cite all relevent source,s ... make 10-20
hooks ensureing that all agents that are about to submit a paper to github, researchgate o rzendono get a rptop telling
them to check all citaztions mand make sure that all revlenet citatios were cited"
"""

HOOK = {'id': 'C15',
 'on': ('researchgate',),
 'cool': 1200,
 'title': 'ResearchGate gets the final PDF and its references',
 'rule': 'On ResearchGate, upload only the final checked PDF, check that the parsed reference list matches the '
         "bibliography (fix entries ResearchGate failed to match), and link the cited authors' and our own related "
         'publications where it offers to.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
