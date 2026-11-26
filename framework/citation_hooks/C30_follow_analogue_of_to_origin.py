# -*- coding: utf-8 -*-
"""Citation hook C30: follow 'an analogue of' back to the origin.

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S

HOOK = {'id': 'C30', 'on': ('github', 'zenodo', 'credit'), 'title': "follow 'an analogue of' back to the origin", 'cool': 1800,
        'rule': 'When the result you cite says it is an analogue, extension or adaptation of an earlier one, open the earlier one and cite it too, with its number.'}


if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
