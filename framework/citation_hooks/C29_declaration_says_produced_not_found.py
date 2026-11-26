# -*- coding: utf-8 -*-
"""Citation hook C29: the AI declaration says what each system produced, not what it found.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S

HOOK = {'id': 'C29', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'the AI declaration says what each system produced, not what it found', 'cool': 1800,
        'rule': 'In the AI declaration write which system proposed, wrote, computed or checked what. Do not write that a system found, discovered or first proved something; whether a result is new is said once, in the introduction, with citations.'}

def check(ch, p):
    f = S.find_tex(p)
    return (not f) or bool(re.search(r"\b(found|discovered|first proved|invented)\b", S.declaration(S.text(f)), re.I))

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
