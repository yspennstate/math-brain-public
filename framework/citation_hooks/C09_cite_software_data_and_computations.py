# -*- coding: utf-8 -*-
"""Citation hook C09: cite software, data and computations.

One of the sixteen citation hooks run by cite_hooks_run.py (an agent, 11 Nov 2026). Written at the author's request.
"""

HOOK = {'id': 'C09',
 'on': ('github', 'zenodo', 'researchgate'),
 'title': 'cite software, data and computations',
 'rule': 'Computations are cited: the software and version (SageMath, Lean/mathlib, a SAT or LP solver, Python '
         'libraries), OEIS sequences, data sets and any computer-assisted proof or certificate, with where the code '
         'lives.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
