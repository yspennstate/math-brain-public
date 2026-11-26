# -*- coding: utf-8 -*-
"""Citation hook C31: names are copied from the bibliography, never typed from memory.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S

HOOK = {'id': 'C31', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'names are copied from the bibliography, never typed from memory', 'cool': 1800,
        'rule': 'Every author name in the text, the abstract, a hosting page or a letter about the paper is copied from the bibliography entry, which is itself checked against the first page of the cited paper.'}


if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
