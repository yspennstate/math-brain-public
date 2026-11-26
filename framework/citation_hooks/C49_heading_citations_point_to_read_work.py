# -*- coding: utf-8 -*-
"""Citation hook C49: a citation in a theorem heading points to work you have read.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C49', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'a citation in a theorem heading points to work you have read', 'cool': 1800, 'detect': True,
        'rule': "\\begin{theorem}[\\cite{X}] asserts that X contains the statement. If X is in preparation, unpublished or unread, attribute in words ('known to X', 'X, personal communication') instead."}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    bib = T.bibitems(t)
    for m in re.finditer(r"\\begin\{(?:theorem|lemma|proposition|corollary)\}\[([^\]]*)\]", t):
        for k in T.cites(m.group(1)):
            if k in bib and T.UNREAD.search(bib[k]):
                return True
    return False

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
