# -*- coding: utf-8 -*-
"""Citation hook C37: every displayed theorem that is not new carries its source in the heading or the next line.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C37', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'every displayed theorem that is not new carries its source in the heading or the next line', 'cool': 1800, 'detect': True,
        'rule': 'A theorem, lemma or corollary taken from or known to others carries the name in its heading ([Rubin], [known to A and B]) or a citation in its first line. Read each environment and ask: whose is this?'}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    bare = 0
    for m in re.finditer(r"\\begin\{(?:theorem|lemma|proposition|corollary)\}(?!\[)", t):
        if "\\cite" not in t[m.end():t.find("\\end{", m.end())]:
            bare += 1
    return bare >= 2 and bool(re.search(r"known to|due to|not claimed as new|informed the author", t, re.I))

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
