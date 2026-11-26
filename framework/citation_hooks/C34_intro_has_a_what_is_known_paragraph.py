# -*- coding: utf-8 -*-
"""Citation hook C34: the introduction has a paragraph on what was known.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C34', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'the introduction has a paragraph on what was known', 'cool': 1800, 'detect': True,
        'rule': "Before the paper's own statements, one paragraph says what was known and by whom (published work, talks, theses, work in preparation that the field cites), and which of the paper's statements it covers. Label it plainly ('What is known', 'Earlier work')."}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    return not re.search(r"(what is known|earlier work|previous work|prior work|related work|known results|background)", T.intro(t), re.I)

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
