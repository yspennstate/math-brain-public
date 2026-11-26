# -*- coding: utf-8 -*-
"""Citation hook C47: exponential clocks in an urn or reinforced walk are Rubin's construction.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C47', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': "exponential clocks in an urn or reinforced walk are Rubin's construction", 'cool': 1800, 'detect': True,
        'rule': "Independent exponential (Yule, Poisson) processes behind an urn or reinforced random walk are Rubin's construction, published by B. Davis, Reinforced random walk, PTRF 84 (1990) 203-229; see Pemantle's survey Section 2.3. Name it."}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    return bool(re.search(r"exponential|Yule", t)) and bool(re.search(r"urn|reinforc", t, re.I)) and "Rubin" not in t

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
