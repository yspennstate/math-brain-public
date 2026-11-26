# -*- coding: utf-8 -*-
"""Citation hook C48: a 'personal communication' says only what the person wrote.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C48', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': "a 'personal communication' says only what the person wrote", 'cool': 1800, 'detect': False,
        'rule': "Each clause after 'X informed the author' or '(personal communication)' must be in X's own message. Keep the message beside the .tex, and reread it clause by clause before posting; do not widen 'most' to 'all' or 'cycles' to 'graphs'."}

def check(ch, p):
    f, t = T.tex(p)
    return bool(f) and bool(re.search(r"informed the author|personal communication|private communication", t))

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
