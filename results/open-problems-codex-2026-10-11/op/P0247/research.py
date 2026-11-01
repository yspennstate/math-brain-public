from pathlib import Path
import urllib.request, urllib.parse, json, time, concurrent.futures
ROOT=Path(__file__).parent
queries=[
('source','https://www.stat.berkeley.edu/~aldous/RWG/book.pdf'),
('arxiv','https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"last visited" AND all:"random walk"')+'&max_results=20'),
('openalex','https://api.openalex.org/works?search='+urllib.parse.quote('last visited vertex transitive random walk')+'&per-page=15'),
('crossref','https://api.crossref.org/works?query='+urllib.parse.quote('last visited vertex random walk transitive')+'&rows=15'),
('semantic','https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('last visited vertex random walk')+'&limit=15&fields=title,authors,year,url,abstract'),
('github','https://api.github.com/search/repositories?q='+urllib.parse.quote('last visited vertex random walk')),
('openalex_source','https://api.openalex.org/works?search='+urllib.parse.quote('Reversible Markov Chains and Random Walks on Graphs')+'&per-page=5'),
]
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'P0247-mathematical-research/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  ROOT.joinpath(name+('.pdf' if name=='source' else '.txt')).write_bytes(data)
  return name,url,'OK '+str(len(data))
 except Exception as e:return name,url,repr(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 results=list(ex.map(fetch,queries))
with ROOT.joinpath('LITERATURE.md').open('a',encoding='utf-8') as f:
 f.write('\nSearch batch, 2026-10-12 (direct HTTP):\n')
 for name,url,result in results:
  f.write(f'- {name}: {url}\n  Result: {result}; raw response saved when successful.\n')
for r in results: print(r)
try:
 import pymupdf
 doc=pymupdf.open(ROOT/'source.pdf')
 text='\n'.join(p.get_text() for p in doc)
 ROOT.joinpath('source_full.txt').write_text(text,encoding='utf-8')
 for i,p in enumerate(doc):
  t=p.get_text()
  if 'Open Problem 7.10' in t:
   print('PDF PAGE',i+1,t)
except Exception as e:print('PDF extraction',repr(e))
