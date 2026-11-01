import urllib.request, urllib.parse, pathlib, concurrent.futures, json, datetime
root=pathlib.Path(__file__).resolve().parent
queries=[
('source','https://www.mi.uni-koeln.de/~drewitz/SpringerRI.pdf'),
('arxiv','https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:interlacements AND all:Sierpinski')+'&max_results=30'),
('openalex','https://api.openalex.org/works?search='+urllib.parse.quote('random interlacements Sierpinski gasket')+'&per-page=30'),
('crossref','https://api.crossref.org/works?query='+urllib.parse.quote('random interlacements Sierpinski gasket')+'&rows=20'),
('semantic','https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('random interlacements Sierpinski gasket')+'&limit=30&fields=title,authors,year,url,externalIds,abstract'),
('github','https://api.github.com/search/repositories?q='+urllib.parse.quote('interlacements Sierpinski')),
('openalex_book','https://api.openalex.org/works?search='+urllib.parse.quote('An introduction to random interlacements')+'&per-page=5')]
def fetch(pair):
 name,url=pair
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'MathematicalResearch/1.0'})
  with urllib.request.urlopen(req,timeout=50) as r: data=r.read()
  (root/(name+('.pdf' if name=='source' else '.json' if name!='arxiv' else '.xml'))).write_bytes(data)
  out=f'{name}: OK {len(data)} bytes'
 except Exception as e: out=f'{name}: ERROR {e}'
 with (root/'LITERATURE.md').open('a',encoding='utf8') as f: f.write(f'\n- 2026-10-11 | {name} | `{url}` | {out}\n')
 return out
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
 for result in ex.map(fetch,queries): print(result)
try:
 import pymupdf
 doc=pymupdf.open(root/'source.pdf'); (root/'source.txt').write_text('\n'.join(p.get_text() for p in doc),encoding='utf8')
 print('PDF extracted')
except Exception as e: print('PDF extraction:',e)
