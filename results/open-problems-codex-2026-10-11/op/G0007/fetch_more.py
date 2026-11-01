import requests,pathlib,json,concurrent.futures
q={
'arxiv_exact':'https://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20all:%22regular%20tree%22&sortBy=submittedDate&sortOrder=descending&max_results=30',
'openalex_retry':'https://api.openalex.org/works?filter=locations.source.id:s4306400194&search=2609.09972&per_page=5',
'openalex_doi':'https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2609.09972',
'semantic_search':'https://api.semanticscholar.org/graph/v1/paper/search?query=Percolation%20contact%20process%20regular%20tree&limit=10&fields=title,authors,year,externalIds',
'github_retry':'https://api.github.com/search/repositories?q=2609.09972',
'crossref_since':'https://api.crossref.org/works?query=contact%20process%20tree%20percolation%20continuity&filter=from-pub-date:2026-09-09&rows=20',
'author':'https://arxiv.org/search/?query=Fernley%2C+John&searchtype=author&abstracts=show&order=-announced_date_first&size=50'
}
def f(k,u):
 try:
  r=requests.get(u,timeout=35);pathlib.Path(k+'.txt').write_bytes(r.content);return {'service':k,'url':u,'status':r.status_code,'bytes':len(r.content),'date':'2026-10-11'}
 except Exception as e:return {'service':k,'url':u,'error':str(e),'date':'2026-10-11'}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:a=list(ex.map(lambda kv:f(*kv),q.items()))
p=pathlib.Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+a,indent=2));print(json.dumps(a,indent=2))
