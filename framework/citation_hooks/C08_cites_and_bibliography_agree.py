# -*- coding: utf-8 -*-
"""Citation hook C08: every cite resolves, every entry is cited.

One of the sixteen citation hooks run by cite_hooks_run.py (an agent, 11 Nov 2026). His words, 11 Nov 2026 07:1x:
"when we write and publish math paper, i think we need to be more carful to cite all relevent source,s ... make 10-20
hooks ensureing that all agents that are about to submit a paper to github, researchgate o rzendono get a rptop telling
them to check all citaztions mand make sure that all revlenet citatios were cited"
"""

HOOK = {'id': 'C08',
 'on': ('github', 'zenodo', 'researchgate', 'draft'),
 'title': 'every cite resolves, every entry is cited',
 'rule': "Compile the final .tex: no 'Citation undefined' warnings, no [?] or ?? in the PDF, every \\cite key exists "
         'in the bibliography and every bibliography entry is cited in the text (an uncited entry is either cited '
         'where it bears or dropped).'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
