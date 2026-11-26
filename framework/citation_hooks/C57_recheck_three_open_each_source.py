# -*- coding: utf-8 -*-
"""Citation hook C57: recheck 3: every bibliography entry has its source opened on disk.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C57', 'on': ('github', 'zenodo', 'researchgate'), 'title': 'recheck 3: every bibliography entry has its source opened on disk', 'cool': 1800, 'detect': False,
        'rule': 'Pass three: for each bibliography entry there is a file you opened (a src/ or sources/ folder beside the paper, or a note of where it was read). Cite only what was read; an entry with no source opened is marked or removed.'}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    d = T.repo_dir(f)
    for sub in ("src", "sources", os.path.join("..", "src")):
        q = os.path.join(d, sub)
        if os.path.isdir(q):
            n = len([x for x in os.listdir(q) if not x.startswith(".")])
            return n < max(1, len(T.bibitems(t)) // 2)
    return len(T.bibitems(t)) >= 3

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
