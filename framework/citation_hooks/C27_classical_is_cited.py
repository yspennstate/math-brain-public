# -*- coding: utf-8 -*-
"""Citation hook C27: a classical result is cited, not just called classical.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S

HOOK = {'id': 'C27', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'a classical result is cited, not just called classical', 'cool': 1800,
        'rule': 'A sentence that calls something classical, well known or standard carries a citation to a source you have opened, or the sentence goes. Constructions borrowed from the literature (an embedding, a martingale, a Lyapunov function) are named and credited where they are used.'}

def check(ch, p):
    f = S.find_tex(p)
    if not f:
        return True   # no .tex found: fire as a plain reminder
    for s in S.sentences(S.body(S.text(f))):
        if re.search(r"\b(classical|well[- ]known|standard (?:argument|fact|result)|it is known)\b", s, re.I) and "\\cite" not in s:
            return True
    return False

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
