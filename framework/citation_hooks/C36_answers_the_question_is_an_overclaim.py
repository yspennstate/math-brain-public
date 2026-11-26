# -*- coding: utf-8 -*-
"""Citation hook C36: 'answers the question of X' is checked against X's question.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C36', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': "'answers the question of X' is checked against X's question", 'cool': 1800, 'detect': True,
        'rule': "'This answers the question of X' is true only when X's own question is the one solved, in X's model. For an analogue, a variant, or a special case, say which, and leave X's question open in the text."}

def check(ch, p):
    f, t = T.tex(p)
    return bool(f) and bool(re.search(r"\b(answers|resolves|settles|solves) (?:the|a|an) (?:open )?(?:question|problem|conjecture)", t, re.I))

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
