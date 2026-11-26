# -*- coding: utf-8 -*-
"""Citation hook C45: write to the people working on the question before posting a new-looking result.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C45', 'on': ('github', 'zenodo', 'researchgate'), 'title': 'write to the people working on the question before posting a new-looking result', 'cool': 1800, 'detect': False,
        'rule': "A result that looks new in an area with an active group goes to that group before it is posted: a short email with the statement and the question 'is this known?'. Whether to write first and when to post is the author's call; the email is ours to draft."}

def check(ch, p):
    f, t = T.tex(p)
    return bool(f) and bool(T.NEWCLAIM.search(S.body(t)))

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
