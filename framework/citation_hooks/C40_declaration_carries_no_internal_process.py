# -*- coding: utf-8 -*-
"""Citation hook C40: the AI declaration says who did what, not what went wrong inside.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C40', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'the AI declaration says who did what, not what went wrong inside', 'cool': 1800, 'detect': True,
        'rule': "The declaration records which system wrote which part and whose mathematics it rests on. Lines about what the AI missed, failed to find, or got corrected are internal: they go in private notes, never in the paper."}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    d = S.declaration(t)
    return bool(d) and bool(re.search(r"did\s+not\s+(?:identify|find|locate|notice)|failed to|missed|overlooked|was corrected|were corrected|mistak", d, re.I))

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
