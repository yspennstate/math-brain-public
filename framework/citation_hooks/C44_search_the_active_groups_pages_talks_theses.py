# -*- coding: utf-8 -*-
"""Citation hook C44: search the active group's home pages, talks and student theses.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C44', 'on': ('github', 'zenodo', 'researchgate'), 'title': "search the active group's home pages, talks and student theses", 'cool': 1800, 'detect': False,
        'rule': "When three or more cited works share an author, that group is active on the topic. Before posting, open their home pages, talk lists, recent arXiv postings and their students' theses (MSc and PhD), and search the talk titles for the paper's objects. Known-to-the-field results are often only in talks."}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    from collections import Counter
    c = Counter()
    for e in T.bibitems(t).values():
        for n in set(T.surnames(e)):
            c[n] += 1
    return any(v >= 3 for v in c.values()) or any(v >= 2 for v in c.values())

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
