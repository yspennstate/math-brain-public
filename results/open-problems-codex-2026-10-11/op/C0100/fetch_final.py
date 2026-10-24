import requests,json,pathlib,concurrent.futures
jobs={'github_identity':'https://api.github.com/search/repositories?q=sandpile+identity&per_page=30','semantic_citations':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1611.00411/citations?fields=title,year,externalIds&limit=100'}
def f(k,u):
 try:
  r=requests.get(u,timeout=35);pathlib.Path(k+'.json').write_bytes(r.content)
  return dict(service=k,url=u,status=r.status_code,date='2026-10-12',bytes=len(r.content))
 except Exception as e:return dict(service=k,url=u,error=str(e),date='2026-10-12')
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:r=list(ex.map(lambda x:f(*x),jobs.items()))
p=pathlib.Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+r,indent=2));print(json.dumps(r,indent=2))
