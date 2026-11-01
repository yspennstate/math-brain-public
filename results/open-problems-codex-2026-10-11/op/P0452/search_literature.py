import urllib.request,urllib.parse,json,concurrent.futures,datetime
from pathlib import Path
queries=[('arxiv','http://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"Erlang Weighted Tree" OR all:"La-Kabkab"')+'&max_results=30'),('arxiv_https','https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"bilateral" AND all:"random graph"')+'&max_results=30'),('openalex','https://api.openalex.org/works?search='+urllib.parse.quote('Erlang Weighted Tree')+'&per-page=30'),('openalex_bilateral','https://api.openalex.org/works?search='+urllib.parse.quote('bilateral random graph')+'&per-page=30'),('crossref','https://api.crossref.org/works?query='+urllib.parse.quote('Erlang Weighted Tree')+'&rows=15'),('semantic','https://api.semanticscholar.org/graph/v1/paper/ARXIV:2002.03993?fields=title,year,citationCount,citations.title,citations.year,citations.externalIds'),('github','https://api.github.com/search/repositories?q='+urllib.parse.quote('"Erlang Weighted Tree"'))]
def fetch(q):
 name,url=q
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'P0452-research/1.0'})
  data=urllib.request.urlopen(req,timeout=40).read().decode(); Path(name+'.response.txt').write_text(data,encoding='utf-8'); status='OK'
 except Exception as e: data=str(e);status='ERROR '+data
 return name,url,status
results=list(concurrent.futures.ThreadPoolExecutor(max_workers=7).map(fetch,queries))
with Path('LITERATURE.md').open('a',encoding='utf-8') as f:
 f.write('# Literature searches, 2026-10-12\n\n')
 for name,url,status in results:f.write(f'- {name}: `{url}` ? {status}; raw response: {name}.response.txt\n')
for row in results: print(row)
