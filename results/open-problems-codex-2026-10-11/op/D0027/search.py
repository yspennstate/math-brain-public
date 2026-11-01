from pathlib import Path
import urllib.request,urllib.parse,json,concurrent.futures,datetime
queries={
'arxiv_http':'http://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"FA-1f"')+'&max_results=30&sortBy=submittedDate&sortOrder=descending',
'arxiv_https':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"facilitated" AND all:"relaxation"')+'&max_results=30&sortBy=submittedDate&sortOrder=descending',
'openalex':'https://api.openalex.org/works?search='+urllib.parse.quote('FA-1f relaxation')+'&per-page=30',
'openalex_source':'https://api.openalex.org/works?search='+urllib.parse.quote('Long time behaviour of one facilitated kinetically constrained models')+'&per-page=5',
'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote('FA-1f relaxation')+'&rows=30',
'semanticscholar':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('FA-1f')+'&limit=30&fields=title,authors,year,externalIds,url,abstract',
'semanticscholar_citations':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2510.20461/citations?fields=title,authors,year,externalIds&limit=100',
'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('"FA-1f"'),
'arxiv_html':'https://arxiv.org/html/2510.20461v1'
}
def run(item):
 k,u=item
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'MathematicalResearch/1.0'})
  with urllib.request.urlopen(req,timeout=35) as r: b=r.read()
  Path(k+'.response').write_bytes(b)
  return k,u,'OK',len(b)
 except Exception as e:
  Path(k+'.response').write_text(str(e),encoding='utf8');return k,u,'ERROR',str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=9) as ex:
 results=list(ex.map(run,queries.items()))
Path('search_log.json').write_text(json.dumps({'date':'2026-10-11','results':results},indent=2),encoding='utf8')
for r in results:print(r,flush=True)
