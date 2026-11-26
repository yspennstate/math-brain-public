# -*- coding: utf-8 -*-
"""Citation hook C39: the AI declaration says which system wrote which part.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C39', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'the AI declaration says which system wrote which part', 'cool': 1800, 'detect': True,
        'rule': "Name each AI system and, for each, what it wrote: which proofs, which computations, which text, which referee corrections. 'AI tools were used' is not a declaration."}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    d = S.declaration(t)
    return bool(d) and not (T.SYSTEM.search(d) and T.DIDVERB.search(d))

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
