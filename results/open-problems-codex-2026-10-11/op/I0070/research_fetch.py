import requests, pathlib, json, concurrent.futures, datetime
ROOT=pathlib.Path(__file__).parent
queries={
 'arxiv':'https://export.arxiv.org/api/query?search_query=all:%22Agresti%22+AND+all:%22regularity%22&max_results=30&sortBy=submittedDate&sortOrder=descending',
 'openalex':'https://api.openalex.org/works?search=Nonlinear%20SPDEs%20and%20maximal%20regularity&per-page=15',
 'crossref':'https://api.crossref.org/works?query.bibliographic=Agresti%20Veraar%20Nonlinear%20SPDEs%20maximal%20regularity&rows=15',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query=Agresti%20Veraar%20regularity&limit=30&fields=title,authors,year,url,externalIds',
 'github':'https://api.github.com/search/repositories?q=Agresti+Veraar+regularity',
 'arxiv_source':'https://arxiv.org/pdf/2501.18561',
 'arxiv_lead':'https://arxiv.org/pdf/2509.07803',
}
def fetch(item):
 key,url=item
 try:
  r=requests.get(url,timeout=45,headers={'User-Agent':'probability-research/1.0'})
  fn=ROOT/(key+('.pdf' if 'pdf/' in url else '.json'))
  fn.write_bytes(r.content)
  result={'service':key,'url':url,'date':'2026-10-12','status':r.status_code,'bytes':len(r.content)}
  if 'pdf/' in url and r.content.startswith(b'%PDF'):
   import pymupdf
   d=pymupdf.open(fn)
   (ROOT/(key+'.txt')).write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
 except Exception as e: result={'service':key,'url':url,'date':'2026-10-12','error':str(e)}
 return result
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
 results=list(ex.map(fetch,queries.items()))
(ROOT/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print(json.dumps(results,indent=2))
