import re
import sys
from pathlib import Path
import pymupdf

pdf = Path(sys.argv[1])
doc = pymupdf.open(pdf)
mode = sys.argv[2] if len(sys.argv) > 2 else 'index'
if mode == 'intro':
    for i in range(min(6, len(doc))):
        print(f'\n===== PDF INDEX {i} =====\n')
        print(doc[i].get_text()[:6200])
elif mode == 'index':
    terms = ('regeneration', 'ballisticity', 'finite mean', 'integrab', 'theorem 1.', 'proposition 1.', 'proof of the main', 'key lemma')
    for i, page in enumerate(doc):
        t = page.get_text()
        hits = []
        for term in terms:
            for m in list(re.finditer(re.escape(term), t, re.I))[:2]:
                hits.append((m.start(), term, ' '.join(t[max(0,m.start()-80):m.end()+130].split())))
        if hits:
            print(f'PDF index {i}:')
            for _, term, context in sorted(hits)[:4]:
                print(f'  {term}: {context}')
elif mode == 'pages':
    for i in map(int, sys.argv[3:]):
        print(f'\n===== PDF INDEX {i} =====\n')
        print(doc[i].get_text())
