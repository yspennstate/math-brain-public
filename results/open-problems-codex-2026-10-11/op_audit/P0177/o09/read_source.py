from pathlib import Path
import pymupdf
from audit_checks import fetch
ROOT=Path(__file__).resolve().parent
p=ROOT/'published_source.pdf'
if not p.exists() or p.stat().st_size<10000:
    p=Path('~/brain_workers/TRIO_1011/op/P0177/source.pdf')
    print('Journal download failed; reading claimant saved journal PDF read-only',flush=True)
doc=pymupdf.open(p)
text='\n'.join(f'PDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc))
(ROOT/'published_source.txt').write_text(text,encoding='utf-8')
for i,p in enumerate(doc):
    tx=p.get_text()
    if any(word in tx for word in ['Problem 4.6','(2.14)','(4.13)','Proposition 3.4','(2.9)']):
        print(f'PDF PAGE {i+1}\n'+tx,flush=True)
