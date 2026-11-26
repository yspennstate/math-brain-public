# -*- coding: utf-8 -*-
"""Citation hook C56: recheck 2: most citations carry a pinpoint (Theorem, Lemma, Section).

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C56', 'on': ('github', 'zenodo', 'researchgate'), 'title': 'recheck 2: most citations carry a pinpoint (Theorem, Lemma, Section)', 'cool': 1800, 'detect': True,
        'rule': 'Pass two: a citation without a pinpoint is one nobody checked. Give the theorem, lemma, section or equation for each use of a cited result; a bare \\cite is for the paper as a whole only.'}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    body = S.body(t)
    allc = re.findall(r"\\cite\*?(\[[^\]]*\])?\{", body)
    if len(allc) < 6:
        return False
    pin = sum(1 for a in allc if a)
    return pin * 3 < len(allc)

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
