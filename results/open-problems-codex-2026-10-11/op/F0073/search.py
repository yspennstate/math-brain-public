import urllib.request,urllib.parse,json,concurrent.futures,time
from pathlib import Path
base=Path('.')
queries=[('source','https://arxiv.org/pdf/math/0509695'),('arxiv','https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"entropic repulsion" AND (all:"convex" OR all:"pinned")','max_results':40})),('openalex','https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'entropic repulsion convex pinned','per-page':30})),('source_openalex','https://api.openalex.org/works/https://doi.org/10.1214/154957806000000050'),('crossref','https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'entropic repulsion pinned convex interface','rows':25})),('semantic','https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':'entropic repulsion convex pinned','limit':30,'fields':'title,authors,year,externalIds,abstract,url'})),('github','https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'entropic repulsion convex'}))]
def get(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'F0073-mathematics-research/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  base.joinpath(name+('.pdf' if name=='source' else '.json' if name!='arxiv' else '.xml')).write_bytes(data)
  return name,url,'OK '+str(len(data))
 except Exception as e:return name,url,repr(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
 results=list(pool.map(get,queries))
with base.joinpath('LITERATURE.md').open('a',encoding='utf8') as f:
 for n,u,s in results:f.write(f'\n- 2026-10-12 | {n} | `{u}` | {s}\n')
for r in results:print(r)
try:
 import pymupdf
 doc=pymupdf.open('source.pdf')
 base.joinpath('source.txt').write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
 print('PDF extracted',len(doc))
except Exception as e:print('PDF extraction',e)
