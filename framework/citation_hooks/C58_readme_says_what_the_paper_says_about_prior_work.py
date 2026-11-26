# -*- coding: utf-8 -*-
"""Citation hook C58: the GitHub README says what the paper says about prior work.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C58', 'on': ('github', 'zenodo', 'researchgate'), 'title': 'the GitHub README says what the paper says about prior work', 'cool': 1800, 'detect': True,
        'rule': "The repo front page is what most people read. If the paper says results were known, the README has a 'Prior work' paragraph with the same names, and does not say 'the paper proves' without 'not claimed as new'."}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    r = os.path.join(T.repo_dir(f), "README.md")
    if not os.path.isfile(r):
        return False
    rt = open(r, encoding="utf-8", errors="replace").read()
    return bool(re.search(r"known to|informed the author|not claimed as new", t)) and not re.search(r"prior work|known to|not claimed as new", rt, re.I)

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
