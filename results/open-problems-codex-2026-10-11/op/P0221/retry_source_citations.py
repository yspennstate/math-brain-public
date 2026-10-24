from research import fetch,ROOT
qs={
'semantic_source_retry':'https://api.semanticscholar.org/graph/v1/paper/19d8db39ea0a731ef6ad138eee9d4d572ec6dc5a?fields=title,year,externalIds,citations.title,citations.year,citations.externalIds',
'frieze_paper_current':'https://www.math.cmu.edu/~af1p/Texfiles/Purchasing.pdf',
}
with (ROOT/'LITERATURE.md').open('a',encoding='utf-8') as f:
 for item in qs.items():
  a,b,c,d=fetch(item);f.write(f'\n2026-10-11 | {a} | {b} | {c} ({d} bytes)\n');print(a,c,d,flush=True)
import pymupdf
try:
 doc=pymupdf.open(stream=(ROOT/'frieze_paper_current.txt').read_bytes(),filetype='pdf')
 (ROOT/'purchasing_current_extracted.txt').write_text('\n'.join(p.get_text() for p in doc),encoding='utf-8')
except Exception as e:print(e)
