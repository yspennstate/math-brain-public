# -*- coding: utf-8 -*-
"""Citation hook C38: the AI declaration names the humans the results rest on.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C38', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'the AI declaration names the humans the results rest on', 'cool': 1800, 'detect': True,
        'rule': 'The AI declaration names, with citations, the mathematicians whose results, constructions and questions the paper rests on, and anyone who has said the results were known to them. Two or more \\cite in the declaration is the floor.'}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    d = S.declaration(t)
    return bool(d) and len(set(T.cites(d))) < 2

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
