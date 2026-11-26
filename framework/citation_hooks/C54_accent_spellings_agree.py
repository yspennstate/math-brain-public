# -*- coding: utf-8 -*-
"""Citation hook C54: a name is spelled the same way everywhere (accents included).

One of the citation and credit hooks run by cite_hooks_run.py. Written at the author's request.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cite_tex_scan as S
import cite_tex_scan2 as T

HOOK = {'id': 'C54', 'on': ('github', 'zenodo', 'researchgate', 'credit'), 'title': 'a name is spelled the same way everywhere (accents included)', 'cool': 1800, 'detect': True,
        'rule': 'Bena\\"im in one place and Benaim in another, or Polya and P\\\'olya, reads as unread references. Copy each name from its bibliography entry.'}

def check(ch, p):
    f, t = T.tex(p)
    if not f:
        return False
    acc = set(re.findall(r"([A-Z][a-z]*\\[\"'`^~][{]?[a-z][}]?[a-z]*)", t))
    for w in acc:
        plain = re.sub(r"\\[\"'`^~][{]?([a-z])[}]?", r"\1", w)
        if re.search(r"\b" + re.escape(plain) + r"\b", t):
            return True
    return False

if __name__ == "__main__":
    import cite_hook_core as C
    print(C.render([HOOK], set(HOOK["on"])))
