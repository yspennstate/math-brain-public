import requests, concurrent.futures, json, pathlib, datetime
queries={
 'oa_exact':'https://api.openalex.org/works?search=%22Hunt%27s%20hypothesis%22&per-page=100',
 'oa_cites':'https://api.openalex.org/works?filter=cites:W2968964261&per-page=100',
 'cr_exact':'https://api.crossref.org/works?query.title=Hunt%27s%20hypothesis&rows=100',
 'arxiv_retry':'https://export.arxiv.org/api/query?search_query=all:Hunt%20AND%20all:subordinator&max_results=30',
 'oa_getoor':'https://api.openalex.org/works?search=%22Getoor%22%20%22conjecture%22&per-page=100',
 'github_exact':'https://api.github.com/search/repositories?q=%22Hunt%27s+hypothesis%22&per_page=100',
}
def f(kv):
 k,u=kv
 try:
  r=requests.get(u,timeout=55,headers={'User-Agent':'E0025 research'})
  pathlib.Path(k+'.txt').write_text(r.text,encoding='utf8')
  out={'service':k,'url':u,'date':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':r.status_code,'bytes':len(r.content)}
 except Exception as e: out={'service':k,'url':u,'error':str(e)}
 print(json.dumps(out),flush=True)
 return out
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as p: results=list(p.map(f,queries.items()))
pathlib.Path('search_followup.json').write_text(json.dumps(results,indent=2),encoding='utf8')
