import requests, concurrent.futures, json, pathlib, datetime
queries = {
 'arxiv': 'https://export.arxiv.org/api/query?search_query=all:quantile%20AND%20all:process%20AND%20all:Lp&start=0&max_results=30&sortBy=submittedDate&sortOrder=descending',
 'openalex_search': 'https://api.openalex.org/works?search=quantile%20process%20Lp&per-page=30',
 'openalex_source': 'https://api.openalex.org/works?search=Distributional%20Limit%20Theory%20for%20Optimal%20Transport&per-page=5',
 'crossref': 'https://api.crossref.org/works?query=quantile%20process%20Lp&rows=20',
 'semantic': 'https://api.semanticscholar.org/graph/v1/paper/search?query=quantile%20process%20Lp&limit=20&fields=title,authors,year,externalIds,url,abstract',
 'github': 'https://api.github.com/search/repositories?q=quantile+process+Lp',
 'beare_pdf': 'https://arxiv.org/pdf/2502.01254',
}
def run(k,u):
 try:
  r=requests.get(u,timeout=65,headers={'User-Agent':'MathematicalResearch/1.0'}); suffix='.pdf' if k.endswith('pdf') else '.txt'
  pathlib.Path('search_'+k+suffix).write_bytes(r.content)
  return {'service':k,'url':u,'date':str(datetime.date.today()),'http_status':r.status_code,'bytes':len(r.content)}
 except Exception as e: return {'service':k,'url':u,'date':str(datetime.date.today()),'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex: results=list(ex.map(lambda kv:run(*kv),queries.items()))
pathlib.Path('search_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
