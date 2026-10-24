import urllib.request, pathlib, concurrent.futures, json, datetime
root=pathlib.Path('.')
urls={
'source':'https://arxiv.org/pdf/1705.04787',
'arxiv':'https://export.arxiv.org/api/query?search_query=all:%22Derrida-Retaux%22&start=0&max_results=60&sortBy=submittedDate&sortOrder=descending',
'openalex':'https://api.openalex.org/works?search=Derrida%20Retaux&per-page=100',
'crossref':'https://api.crossref.org/works?query=Derrida%20Retaux&rows=60',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query=Derrida%20Retaux&limit=100&fields=title,year,authors,abstract,externalIds,url',
'github':'https://api.github.com/search/repositories?q=Derrida+Retaux&per_page=50'
}
def fetch(item):
 k,u=item
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'ProbabilityResearch/1.0'})
  with urllib.request.urlopen(req,timeout=50) as r: data=r.read()
  root.joinpath(k+('.pdf' if k=='source' else '.json' if k!='arxiv' else '.xml')).write_bytes(data)
  return k,u,'OK '+str(len(data))
 except Exception as e:return k,u,repr(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: results=list(ex.map(fetch,urls.items()))
with open('LITERATURE.md','a',encoding='utf8') as f:
 f.write('# Literature search\n\nSearch date: 2026-10-11 (session date).\n\n')
 for k,u,s in results:f.write(f'- {k}: `{u}` — {s}\n')
print(json.dumps(results,indent=2))
try:
 import pymupdf
 doc=pymupdf.open('source.pdf');root.joinpath('source.txt').write_text('\n'.join(f'\nPAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
 print(root.joinpath('source.txt').read_text(encoding='utf8')[:18000])
except Exception as e:print('PDF extraction:',repr(e))
