import requests, concurrent.futures, json, datetime, pathlib
base=pathlib.Path(__file__).resolve().parent
queries={
 'arxiv_http': 'http://export.arxiv.org/api/query?search_query=all:%22Hunt%27s%20hypothesis%22&start=0&max_results=60&sortBy=submittedDate&sortOrder=descending',
 'arxiv_https': 'https://export.arxiv.org/api/query?search_query=all:%22Hunt%27s%20hypothesis%22&start=0&max_results=60&sortBy=submittedDate&sortOrder=descending',
 'openalex_search':'https://api.openalex.org/works?search=Hunt%20hypothesis%20subordinators&per-page=100',
 'openalex_source':'https://api.openalex.org/works?search=Hunt%27s%20hypothesis%20for%20Markov%20processes%20survey%20and%20beyond&per-page=10',
 'crossref':'https://api.crossref.org/works?query=Hunt%20hypothesis%20subordinators&rows=60',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query=Hunt%20hypothesis%20subordinator&limit=100&fields=title,authors,year,externalIds,url,abstract',
 'semantic_source':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1908.06825?fields=title,year,citations.title,citations.year,citations.externalIds',
 'github':'https://api.github.com/search/repositories?q=Hunt+hypothesis+subordinator&per_page=100',
}
def fetch(item):
 name,url=item
 try:
  r=requests.get(url,timeout=65,headers={'User-Agent':'E0025-research/1.0'})
  (base/(name+'.txt')).write_text(r.text,encoding='utf8')
  result={'service':name,'url':url,'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':r.status_code,'bytes':len(r.content)}
 except Exception as e: result={'service':name,'url':url,'error':str(e)}
 print(json.dumps(result),flush=True)
 return result
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: results=list(pool.map(fetch,queries.items()))
(base/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
