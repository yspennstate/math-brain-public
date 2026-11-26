# -*- coding: utf-8 -*-
"""Citation hook C46: a construction from the literature is named after its author.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C46', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'a construction from the literature is named after its author', 'cool': 1800, 'detect': True,
        'rule': "An embedding, coupling, urn representation or martingale borrowed from the literature is named (Rubin's construction, Athreya-Karlin embedding, Kesten-Stigum) and cited to the paper that published it, not only to a survey."}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    for s in S.sentences(S.body(t)):
        if re.search(r"\b(embedding|coupling|construction|representation)\b", s) and re.search(r"classical|standard|well[- ]known|usual", s) \
           and not re.search(r"[A-Z][a-z]+'s (?:construction|embedding|coupling)|[A-Z][a-z]+--[A-Z]", s):
            return True
    return False

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
