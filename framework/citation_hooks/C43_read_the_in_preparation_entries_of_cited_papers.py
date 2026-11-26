# -*- coding: utf-8 -*-
"""Citation hook C43: open the cited papers' bibliographies for work in preparation.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C43', 'on': ('github', 'zenodo', 'researchgate'), 'title': "open the cited papers' bibliographies for work in preparation", 'cool': 1800, 'detect': False,
        'rule': "A cited paper's bibliography often lists the same group's work 'in preparation' on exactly your question (a 'part II' cited for years in the group's published papers). Before claiming anything: grep every cited paper's references for 'in preparation', 'preprint', 'manuscript', 'forthcoming', 'thesis'."}

def check(ch, p):
    f, t = T.tex(p)
    return bool(f) and len(T.bibitems(t)) >= 3

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
