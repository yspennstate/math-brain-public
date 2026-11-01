import urllib.request,concurrent.futures,json,pathlib,urllib.parse
queries={
 'openalex_doi':'https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2505.19104',
 'openalex_source_filter':'https://api.openalex.org/works?filter=title.search:'+urllib.parse.quote('Distributional Limit Theory for Optimal Transport')+'&per-page=5',
 'arxiv_specific':'http://export.arxiv.org/api/query?search_query='+urllib.parse.quote('(all:"Euclidean" AND all:"empirical" AND all:"transport") OR (all:"transport" AND all:"separated rectangles") OR (all:"transport" AND all:"separated squares")')+'&max_results=50&sortBy=submittedDate&sortOrder=descending'}
def f(k,u):
 try:
  with urllib.request.urlopen(u,timeout=35) as r:b=r.read()
  pathlib.Path(k+'.txt').write_bytes(b);return {'service':k,'url':u,'date':'2026-10-12','status':'ok'}
 except Exception as e:return {'service':k,'url':u,'date':'2026-10-12','status':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:r=list(ex.map(lambda kv:f(*kv),queries.items()))
pathlib.Path('search_log4.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
