# -*- coding: utf-8 -*-
"""Citation hook C12: count and coverage smell test.

One of the sixteen citation hooks run by cite_hooks_run.py (an agent, 11 Nov 2026). His words, 11 Nov 2026 07:1x:
"when we write and publish math paper, i think we need to be more carful to cite all relevent source,s ... make 10-20
hooks ensureing that all agents that are about to submit a paper to github, researchgate o rzendono get a rptop telling
them to check all citaztions mand make sure that all revlenet citatios were cited"
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
