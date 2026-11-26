# -*- coding: utf-8 -*-
"""Citation hook C42: the abstract says what was known, if the body does.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C42', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'the abstract says what was known, if the body does', 'cool': 1800, 'detect': True,
        'rule': 'If the body says some results were known to others, the abstract says so in one clause. Most readers, the experts included, see only the abstract.'}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    a = T.abstract(t)
    return bool(a) and bool(re.search(r"known to|due to|informed the author", S.body(t))) and not re.search(r"known|due to|not claimed as new|Rubin|construction of", a)

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
