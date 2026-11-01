from research import fetch,ROOT
import concurrent.futures,urllib.parse as U
qs={
'semantic_source':'https://api.semanticscholar.org/graph/v1/paper/19d8db39ea0a731ef6ad138eee9d4d572ec6dc5a?fields=title,authors,year,externalIds,citations.title,citations.year,citations.externalIds',
'frieze_papers':'https://www.math.cmu.edu/~af1p/papers.html',
'arxiv_budget':'https://arxiv.org/pdf/2207.07251',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex: rs=list(ex.map(fetch,qs.items()))
with (ROOT/'LITERATURE.md').open('a',encoding='utf-8') as f:
 for a,b,c,d in rs:f.write(f'\n2026-10-11 | {a} | {b} | {c} ({d} bytes)\n')
for r in rs:print(r)
import pymupdf
try:
 doc=pymupdf.open(stream=(ROOT/'arxiv_budget.txt').read_bytes(),filetype='pdf')
 (ROOT/'budget_extracted.txt').write_text('\n'.join(p.get_text() for p in doc),encoding='utf-8')
except Exception as e:print(e)
