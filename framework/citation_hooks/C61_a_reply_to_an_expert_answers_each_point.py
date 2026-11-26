# -*- coding: utf-8 -*-
"""Citation hook C61: a reply to an expert answers each point the expert made with the line that fixes it.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C61', 'on': ('github', 'zenodo', 'researchgate'), 'title': 'a reply to an expert answers each point the expert made with the line that fixes it', 'cool': 1800, 'detect': False,
        'rule': "Reread the expert's message sentence by sentence; for each point, the reply says what changed and where. Never send a reply that says the paper credits people before checking the attached version does. Promises (taking it down, writing first from now on) are the author's to make: mark them for the author."}

def check(ch, p):
    f, t = T.tex(p)
    return bool(f) and bool(re.search(r"informed the author", t))

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
