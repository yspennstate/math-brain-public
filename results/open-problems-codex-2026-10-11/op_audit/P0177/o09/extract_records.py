from pathlib import Path
import pymupdf
ROOT=Path(__file__).resolve().parent
claim=Path('~/brain_workers/TRIO_1011/op/P0177')
for name in ['ATTEMPT.md','STATUS.md','CLAIMS.jsonl','LITERATURE.md']:
    lines=(claim/name).read_text(encoding='utf-8').splitlines()
    (ROOT/(name+'.numbered.txt')).write_text('\n'.join(f'{i}: {line}' for i,line in enumerate(lines,1)),encoding='utf-8')
    if name=='ATTEMPT.md':
        print('\n'.join(f'{i}: {line}' for i,line in enumerate(lines,1)),flush=True)
doc=pymupdf.open(ROOT/'arxiv_source.pdf')
(ROOT/'arxiv_source.txt').write_text('\n'.join(p.get_text() for p in doc),encoding='utf-8')
for i,p in enumerate(doc):
    tx=p.get_text()
    if any(word in tx for word in ['Problem 4.6','(2.14)','(4.13)']):
        print(f'FRESH ARXIV PDF PAGE {i+1}\n'+tx,flush=True)
