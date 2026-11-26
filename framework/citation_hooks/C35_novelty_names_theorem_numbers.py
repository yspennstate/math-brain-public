# -*- coding: utf-8 -*-
"""Citation hook C35: a claim of what is new names the theorem numbers and nothing else.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C35', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'a claim of what is new names the theorem numbers and nothing else', 'cool': 1800, 'detect': True,
        'rule': "Where the paper says something is new, it names the statements by number and every other statement carries its source. If an expert has said the results are known, nothing is claimed as new; write 'not claimed as new', not 'not new' unless that is the expert's verdict."}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    for s in S.sentences(S.body(t)):
        if T.NEWCLAIM.search(s) and not re.search(r"\\ref\{", s) and not re.search(r"not claimed as new|not new", s):
            return True
    return False

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
