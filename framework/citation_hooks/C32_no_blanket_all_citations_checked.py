# -*- coding: utf-8 -*-
"""Citation hook C32: no blanket claim that every citation was checked.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S

HOOK = {'id': 'C32', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'no blanket claim that every citation was checked', 'cool': 1800,
        'rule': 'Do not write that all citations were checked. Check them, and let the pinpoint citations (Lemma, Theorem, Section numbers) show it.'}

def check(ch, p):
    f = S.find_tex(p)
    return (not f) or bool(re.search(r"\b(each|every|all)\s+(citation|reference)s?\s+(was|were|has been|have been)\s+(checked|verified)", S.text(f), re.I))

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
