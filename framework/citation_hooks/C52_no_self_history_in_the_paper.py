# -*- coding: utf-8 -*-
"""Citation hook C52: the paper does not narrate its own history.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C52', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'the paper does not narrate its own history', 'cool': 1800, 'detect': True,
        'rule': "No 'the first version', 'an earlier version', 'was corrected after', 'added after X wrote'. State the attribution in the present tense; the version history belongs in the commit log and private notes."}

def check(ch, p):
    f, t = T.tex(p)
    return bool(f) and bool(re.search(r"first version|earlier version|previous version|was corrected|were added after|added after [A-Z]", S.body(t) + S.declaration(t), re.I))

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
