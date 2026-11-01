import urllib.request, urllib.parse, concurrent.futures, pathlib, json, datetime
queries=[('arxiv_http','http://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"activated random walk" AND (all:"fixation" OR all:"stabilization")')+'&start=0&max_results=60&sortBy=submittedDate&sortOrder=descending'),('arxiv_https','https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"activated random walks"')+'&max_results=80&sortBy=submittedDate&sortOrder=descending'),('openalex_search','https://api.openalex.org/works?search=activated%20random%20walk%20fixation%20time&per-page=50'),('openalex_source','https://api.openalex.org/works?search=Activated%20random%20walks%20on%20Z&per-page=10'),('crossref','https://api.crossref.org/works?query=activated%20random%20walk%20stabilization%20time&rows=40'),('semantic','https://api.semanticscholar.org/graph/v1/paper/search?query=activated%20random%20walk%20fixation%20time&limit=50&fields=title,authors,year,externalIds,abstract,url'),('github','https://api.github.com/search/repositories?q=activated+random+walk&per_page=30')]
def run(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'D0093-math-research/1.0'})
  raw=urllib.request.urlopen(req,timeout=45).read(); pathlib.Path(name+'.json' if name not in ('arxiv_http','arxiv_https') else name+'.xml').write_bytes(raw)
  result={'service':name,'query_url':url,'date':'2026-10-12','status':'success','bytes':len(raw)}
 except Exception as e: result={'service':name,'query_url':url,'date':'2026-10-12','status':str(e)}
 with open('search_log.jsonl','a',encoding='utf8') as f: f.write(json.dumps(result)+'\n')
 return result
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
 for r in pool.map(run,queries): print(r,flush=True)
