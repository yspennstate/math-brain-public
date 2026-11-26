# -*- coding: utf-8 -*-
"""Citation hook C41: the declaration and the introduction credit the same people.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C41', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'the declaration and the introduction credit the same people', 'cool': 1800, 'detect': True,
        'rule': "Every citation in the AI declaration also appears in the introduction, and the introduction's 'what is known' people appear in the declaration. Two lists of credit that disagree read as careless."}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    d = set(T.cites(S.declaration(t)))
    i = set(T.cites(T.intro(t)))
    return bool(d) and bool(i) and bool(d - i - {"MathBrainPaper", "MathBrainRepo", "BrainFramework"})

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
