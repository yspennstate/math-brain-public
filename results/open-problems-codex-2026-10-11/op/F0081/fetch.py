import urllib.request, pathlib, concurrent.futures, json, datetime
p=pathlib.Path('.')
queries={
'source':'https://arxiv.org/pdf/0712.1867',
'arxiv':'https://export.arxiv.org/api/query?search_query=all:%22stable%20matching%22%20AND%20all:Poisson&max_results=50',
'openalex':'https://api.openalex.org/works?search=two%20colour%20stable%20Poisson%20matching&per-page=50',
'crossref':'https://api.crossref.org/works?query=stable%20Poisson%20matching&rows=30',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query=stable%20Poisson%20matching&limit=30&fields=title,authors,year,abstract,url,externalIds',
'github':'https://api.github.com/search/repositories?q=stable+Poisson+matching'}
def fetch(k,u):
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'Research-F0081/1.0'})
  with urllib.request.urlopen(req,timeout=50) as r: data=r.read()
  name=k+('.pdf' if k=='source' else '.json' if k not in ['arxiv'] else '.xml')
  (p/name).write_bytes(data)
  return {'service':k,'url':u,'date':'2026-10-11','file':name,'bytes':len(data)}
 except Exception as e: return {'service':k,'url':u,'date':'2026-10-11','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: results=list(ex.map(lambda kv:fetch(*kv),queries.items()))
(p/'search_log.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
try:
 import pymupdf
 doc=pymupdf.open('source.pdf')
 (p/'source.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+page.get_text() for i,page in enumerate(doc)),encoding='utf-8')
 print('PDF extracted',len(doc))
except Exception as e: print('PDF extraction',e)
