import pathlib,urllib.request,json,concurrent.futures,datetime
p=pathlib.Path('.')
queries={
'source':'https://arxiv.org/pdf/0712.1867',
'arxiv':'https://export.arxiv.org/api/query?search_query=all:noncrossing%20AND%20all:Poisson&max_results=30',
'openalex':'https://api.openalex.org/works?search=Poisson%20matching%20noncrossing&per-page=30',
'crossref':'https://api.crossref.org/works?query=Poisson%20matching%20noncrossing&rows=20',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query=Poisson%20matching%20noncrossing&limit=20&fields=title,authors,year,externalIds,url',
'github':'https://api.github.com/search/repositories?q=Poisson+matching+noncrossing',
'openalex_source':'https://api.openalex.org/works?search=Poisson%20matching%20Holroyd%20Pemantle%20Peres%20Schramm&per-page=5'}
def fetch(item):
 k,u=item
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'F0082 research literature check'})
  with urllib.request.urlopen(req,timeout=45) as r: b=r.read()
  (p/(k+('.pdf' if k=='source' else '.json' if k not in ['arxiv'] else '.xml'))).write_bytes(b)
  return k,u,'OK',len(b)
 except Exception as e:return k,u,str(e),0
results=list(concurrent.futures.ThreadPoolExecutor(max_workers=7).map(fetch,queries.items()))
with open('LITERATURE.md','w',encoding='utf8') as f:
 f.write('# Literature audit\n\nSearch date: 2026-10-11 (machine local date).\n\n')
 for k,u,s,n in results:f.write(f'- {k}: {u} — {s}, {n} bytes.\n')
print(results)
try:
 import pymupdf
 doc=pymupdf.open('source.pdf');text='\n'.join(f'\nPDF PAGE {i+1}\n'+page.get_text() for i,page in enumerate(doc));p.joinpath('source.txt').write_text(text,encoding='utf8');print(text[-16000:])
except Exception as e:print(e)
