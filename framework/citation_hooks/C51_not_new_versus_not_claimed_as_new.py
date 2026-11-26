# -*- coding: utf-8 -*-
"""Citation hook C51: 'none of the results is new' only if that is the expert's verdict.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C51', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': "'none of the results is new' only if that is the expert's verdict", 'cool': 1800, 'detect': True,
        'rule': "'None of the results is new' asserts a fact about the whole literature. If the expert said 'most', write 'most' and the expert's name; for the rest write 'not claimed as new'."}

def check(ch, p):
    f, t = T.tex(p)
    return bool(f) and bool(re.search(r"(none of the results[^.]{0,40}is new|the results are not new)", t, re.I))

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
