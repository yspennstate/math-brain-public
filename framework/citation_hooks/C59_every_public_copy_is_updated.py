# -*- coding: utf-8 -*-
"""Citation hook C59: every public copy carries the corrected attribution.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C59', 'on': ('github', 'zenodo', 'researchgate'), 'title': 'every public copy carries the corrected attribution', 'cool': 1800, 'detect': False,
        'rule': 'A correction on GitHub alone leaves the old claim on Zenodo, ResearchGate and Google Scholar. List every public copy (Zenodo versions and description, the ResearchGate file and abstract, the README) and update each, or tell the author which still carry the old claim. Zenodo is permanent: a new version, never a silent edit.'}

def check(ch, p):
    f, t = T.tex(p)
    return bool(f)

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
