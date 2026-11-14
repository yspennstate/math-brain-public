# -*- coding: utf-8 -*-
"""Citation hook C16: the GitHub paper ships its bibliography.

One of the sixteen citation hooks run by cite_hooks_run.py (an agent, 11 Nov 2026). Written at the author's request.
"""

HOOK = {'id': 'C16',
 'on': ('github',),
 'title': 'the GitHub paper ships its bibliography',
 'rule': 'A paper pushed to GitHub ships the .bib or thebibliography it was compiled with and a PDF compiled from '
         'the pushed sources; run python ~/.claude/dreaming/paper_release_guard.py check <paper.tex> and read the '
         'compile log for undefined citations before the push.'}


if __name__ == "__main__":
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
