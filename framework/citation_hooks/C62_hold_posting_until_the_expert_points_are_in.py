# -*- coding: utf-8 -*-
"""Citation hook C62: hold Zenodo and ResearchGate until every expert point is in the PDF.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C62', 'on': ('zenodo', 'researchgate'), 'title': 'hold Zenodo and ResearchGate until every expert point is in the PDF', 'cool': 1800, 'detect': False,
        'rule': 'When an expert has written about a paper, nothing new is posted to Zenodo or ResearchGate until each point the expert made is answered in the PDF and the author has said to post. GitHub may carry the corrected version first.'}

def check(ch, p):
    f, t = T.tex(p)
    return bool(f) and bool(re.search(r"informed the author|personal communication", t))

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
