# -*- coding: utf-8 -*-
"""Citation hook C50: an in-preparation or thesis entry says where it is cited or who told you.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C50', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'an in-preparation or thesis entry says where it is cited or who told you', 'cool': 1800, 'detect': True,
        'rule': "A bibliography entry you could not open (in preparation, a thesis not online) says where it is cited ('cited in [4] and [8]') or who told you about it ('according to A. Author'), and carries a year when one is known."}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    for k, e in T.bibitems(t).items():
        if (T.UNREAD.search(e) or re.search(r"thesis", e, re.I)) and not re.search(r"arXiv|doi|\\url", e):
            if not re.search(r"cited\s+in|\\cite|according to", e) and not re.search(r"according to [A-Z][a-z]+.{0,160}?\\cite\{" + re.escape(k), t, re.S):
                return True
    return False

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
