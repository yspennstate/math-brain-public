# -*- coding: utf-8 -*-
"""Citation hook C33: the introduction says who did what, with citations.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C33', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'the introduction says who did what, with citations', 'cool': 1800, 'detect': True,
        'rule': "The introduction names, with a pinpoint citation, who introduced the model, who proved each earlier result the paper uses, and who knew or proved what the paper states. A sentence 'X introduced', 'X proved', 'due to X', 'known to X' with \\cite is the minimum; an introduction with none is a paper that has not said what it stands on."}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    for s in S.sentences(T.intro(t)):
        if re.search(r"\b(introduced|proved|showed|due to|known to|obtained|established|conjectured|posed)\b", s) and "\\cite" in s:
            return False
    return True

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
