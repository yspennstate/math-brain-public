# -*- coding: utf-8 -*-
"""Citation hook C55: recheck 1: reread every sentence that says new, first, prove or show.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C55', 'on': ('github', 'zenodo', 'researchgate'), 'title': 'recheck 1: reread every sentence that says new, first, prove or show', 'cool': 1800, 'detect': False,
        'rule': "Pass one before any push: list every sentence with 'new', 'first', 'we prove', 'we show', 'our result' and, for each, name the earlier work you checked it against. A sentence you cannot defend to the field's experts goes."}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    n = sum(1 for s in S.sentences(S.body(t)) if re.search(r"\b(new|first|we prove|we show|our result)\b", s, re.I))
    return n >= 1

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
