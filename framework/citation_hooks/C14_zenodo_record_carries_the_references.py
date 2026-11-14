# -*- coding: utf-8 -*-
"""Citation hook C14: the Zenodo record carries the references.

One of the sixteen citation hooks run by cite_hooks_run.py (an agent, 11 Nov 2026). His words, 11 Nov 2026 07:1x:
"when we write and publish math paper, i think we need to be more carful to cite all relevent source,s ... make 10-20
hooks ensureing that all agents that are about to submit a paper to github, researchgate o rzendono get a rptop telling
them to check all citaztions mand make sure that all revlenet citatios were cited"
"""

HOOK = {'id': 'C14',
 'on': ('zenodo',),
 'cool': 1200,
 'title': 'the Zenodo record carries the references',
 'rule': "On Zenodo, fill the record's References field with the same list as the PDF, add Related identifiers (the "
         "problem's source paper with 'cites' / the GitHub repo or arXiv version with 'is identical to'), and upload "
         'the FINAL PDF whose bibliography passed these checks: a published Zenodo version and its DOI cannot be '
         'deleted.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
