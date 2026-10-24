import json,pathlib,requests,concurrent.futures
qs={
'openalex_citing':'https://api.openalex.org/works?filter=cites:doi:10.48550/arXiv.2609.09972&per_page=20',
'semantic_citing':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.09972/citations?fields=title,year,externalIds&limit=100',
'arxiv_continuity':'https://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20(all:continuity%20OR%20all:percolation)%20AND%20submittedDate:[202609090000%20TO%20202610112359]&max_results=50&sortBy=submittedDate&sortOrder=descending',
'haggstrom':'https://projecteuclid.org/journals/annals-of-probability/volume-25/issue-3/Infinite-clusters-in-dependent-automorphism-invariant-percolation-on-trees/10.1214/aop/1024404517.pdf',
'pemantle':'https://www.math.upenn.edu/~pemantle/papers/contact.pdf'
}
def g(k,u):
 try:
  r=requests.get(u,timeout=35);pathlib.Path(k+('.pdf' if r.content.startswith(b'%PDF') else '.txt')).write_bytes(r.content);return {'service':k,'url':u,'status':r.status_code,'bytes':len(r.content),'date':'2026-10-11'}
 except Exception as e:return {'service':k,'url':u,'error':str(e),'date':'2026-10-11'}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:a=list(ex.map(lambda kv:g(*kv),qs.items()))
p=pathlib.Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+a,indent=2));print(json.dumps(a,indent=2))
