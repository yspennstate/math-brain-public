import requests,pathlib,json,concurrent.futures
qs=[('openalex_retry','https://api.openalex.org/works?search=Long-Range%20Correlation%20Sine&per_page=10'),('openalex_citing','https://api.openalex.org/works?filter=cites:doi:10.48550/arXiv.2603.15289&per_page=100'),('semantic_retry','https://api.semanticscholar.org/graph/v1/paper/ARXIV:2603.15289?fields=title,year,citations.title,citations.year,citations.externalIds'),('arxiv_recent','https://export.arxiv.org/api/query?search_query=all:sine%20AND%20all:beta%20AND%20submittedDate:[202603160000%20TO%20202610112359]&max_results=100&sortBy=submittedDate&sortOrder=descending')]
def f(q):
 n,u=q
 try:r=requests.get(u,timeout=40);pathlib.Path('search_'+n+'.txt').write_text(r.text,encoding='utf8');v=f'HTTP {r.status_code}';print(n,v,flush=True)
 except Exception as e:v=str(e)
 return dict(date='2026-10-11',service=n,url=u,outcome=v)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rs=list(ex.map(f,qs))
p=pathlib.Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+rs,indent=2),encoding='utf8')
