import requests,pathlib,concurrent.futures,json,datetime
qs={
'arxiv_quantile':'https://export.arxiv.org/api/query?search_query=all:%22quantile%20process%22&start=0&max_results=80&sortBy=lastUpdatedDate&sortOrder=descending',
'arxiv_source':'https://export.arxiv.org/api/query?id_list=2505.19104,2502.01254',
'arxiv_bobkov':'https://export.arxiv.org/api/query?search_query=ti:%22One-dimensional%20empirical%20measures%22&max_results=5',
'bobkov':'https://arxiv.org/pdf/1407.0938',
'openalex_retry':'https://api.openalex.org/works?filter=title.search:Distributional%20Limit%20Theory%20for%20Optimal%20Transport&per_page=5',
'semantic_source':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2505.19104?fields=title,year,citations.title,citations.year,citations.externalIds',
'crossref_exact':'https://api.crossref.org/works?query.title=Necessary%20and%20sufficient%20conditions%20quantile%20process&rows=15',
'github_more':'https://api.github.com/search/repositories?q=%22quantile+process%22',
}
def run(k,u):
 try:
  r=requests.get(u,timeout=60); pathlib.Path('search_'+k+('.pdf' if k=='bobkov' else '.txt')).write_bytes(r.content)
  return {'service':k,'url':u,'date':str(datetime.date.today()),'http_status':r.status_code,'bytes':len(r.content)}
 except Exception as e:return {'service':k,'url':u,'date':str(datetime.date.today()),'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:r=list(ex.map(lambda kv:run(*kv),qs.items()))
pathlib.Path('search_more_log.json').write_text(json.dumps(r,indent=2),encoding='utf-8');print(json.dumps(r,indent=2))
