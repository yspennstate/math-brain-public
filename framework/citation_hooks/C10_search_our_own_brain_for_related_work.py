# -*- coding: utf-8 -*-
"""Citation hook C10: search the brain for related work.

One of the sixteen citation hooks run by cite_hooks_run.py (an agent, 11 Nov 2026). Written at the author's request.
"""

HOOK = {'id': 'C10',
 'on': ('github', 'zenodo', 'researchgate', 'prompt'),
 'title': 'search the brain for related work',
 'rule': 'Ask the brain what we already know about the problem before posting: python '
         '~/.claude/dreaming/problem_recall.py <id> and python ~/.claude/dreaming/math_recall.py "<object>" --or '
         '"<author>" --or "<method>". Papers it names that bear on the result are cited; our own earlier papers on '
         'the same problem or method are cited too.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
