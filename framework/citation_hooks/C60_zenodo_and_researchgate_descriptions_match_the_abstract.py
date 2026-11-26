# -*- coding: utf-8 -*-
"""Citation hook C60: the Zenodo and ResearchGate descriptions match the new abstract.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C60', 'on': ('zenodo', 'researchgate'), 'title': 'the Zenodo and ResearchGate descriptions match the new abstract', 'cool': 1800, 'detect': True,
        'rule': 'Paste the new abstract, attribution clause included, into the Zenodo description and the ResearchGate abstract. An old description that calls the results new contradicts the PDF beside it.'}

def check(ch, p):
    f, t = T.tex(p)
    return bool(f) and bool(re.search(r"known to|due to|not claimed as new", T.abstract(t)))

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
