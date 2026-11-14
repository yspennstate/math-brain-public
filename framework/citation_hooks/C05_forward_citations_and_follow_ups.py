# -*- coding: utf-8 -*-
"""Citation hook C05: forward citations of the source paper.

One of the sixteen citation hooks run by cite_hooks_run.py (an agent, 11 Nov 2026). Written at the author's request.
"""

HOOK = {'id': 'C05',
 'on': ('github', 'zenodo', 'researchgate'),
 'title': 'forward citations of the source paper',
 'rule': "Open the 'cited by' list of the paper that posed the problem and of each main prior result (Google "
         'Scholar, Semantic Scholar). A later paper that solved or advanced the question must be cited, and if it '
         'already proves our result the paper changes its claim before it is posted.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
