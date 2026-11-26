# -*- coding: utf-8 -*-
"""Citation hook C28: a novelty claim follows a forward-literature search.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S

HOOK = {'id': 'C28', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'a novelty claim follows a forward-literature search', 'cool': 1800,
        'rule': "Before a sentence says a result is new, first, or not known to the authors, search forward from the papers that posed the question (who cites them, with the question's words) and read what turns up. Write in the notes which searches were run."}

def check(ch, p):
    f = S.find_tex(p)
    if not f:
        return True   # no .tex found: fire as a plain reminder
    return bool(re.search(r"not aware of|to (?:our|the author'?s) knowledge|\bfor the first time\b|\bis new\b|\bare new\b", S.text(f), re.I))

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
