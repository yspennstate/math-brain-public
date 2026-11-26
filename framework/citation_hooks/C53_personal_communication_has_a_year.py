# -*- coding: utf-8 -*-
"""Citation hook C53: a personal communication carries the year.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C53', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'a personal communication carries the year', 'cool': 1800, 'detect': True,
        'rule': "Write '(A. Author, personal communication, 2026)'. Without a year the reader cannot place it against the paper's date."}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    for s in S.sentences(t):
        if re.search(r"personal communication", s) and not re.search(r"(19|20)\d\d", s):
            return True
    return False

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
