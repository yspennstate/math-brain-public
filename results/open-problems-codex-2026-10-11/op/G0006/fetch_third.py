import urllib.request, pathlib, json, concurrent.futures
urls={
'openalex_citing':'https://api.openalex.org/works?filter=cites:arxiv:2609.09972&per-page=25',
'crossref_since':'https://api.crossref.org/works?query.bibliographic=contact%20process%20percolation&filter=from-pub-date:2026-09-09&rows=30',
'arxiv_sharpness':'https://export.arxiv.org/api/query?search_query=ti:%22Sharpness%20of%20the%20percolation%20transition%22&max_results=10'
}
def f(k,u):
 try:
  with urllib.request.urlopen(u,timeout=30) as r: b=r.read(); code=r.status
  pathlib.Path(k+'.txt').write_bytes(b); return dict(service=k,url=u,status=code,bytes=len(b))
 except Exception as e: return dict(service=k,url=u,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex: r=list(ex.map(lambda x:f(*x),urls.items()))
pathlib.Path('search_log_3.json').write_text(json.dumps(r,indent=2),encoding='utf8')
for x in r: print(json.dumps(x))
