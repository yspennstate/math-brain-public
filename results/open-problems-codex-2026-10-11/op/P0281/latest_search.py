import urllib.request, urllib.parse,json,concurrent.futures
from pathlib import Path
urls={'arxiv_recent.xml':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:TASEP AND all:concavity AND submittedDate:[202503190000 TO 202610122359]')+'&max_results=40','crossref_target.json':'https://api.crossref.org/works?query.bibliographic='+urllib.parse.quote('TASEP transition log concavity')+'&filter=from-pub-date:2025-03-19&rows=20','openalex_source_retry.json':'https://api.openalex.org/works?filter=title.search:'+urllib.parse.quote('All roads to KPZ')+'&per-page=5','github_broad.json':'https://api.github.com/search/repositories?q='+urllib.parse.quote('TASEP concavity'),'semantic_recent.json':'https://api.semanticscholar.org/graph/v1/paper/search/bulk?query='+urllib.parse.quote('TASEP log concavity')+'&year=2025-&fields=title,year,authors,url'}
def f(it):
 k,u=it
 try:
  r=urllib.request.urlopen(u,timeout=30);b=r.read();Path(k).write_bytes(b);return[k,u,r.status,len(b)]
 except Exception as e:return[k,u,str(e)]
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=5).map(f,urls.items()));Path('search_log_4.json').write_text(json.dumps(r,indent=2));print(r)
