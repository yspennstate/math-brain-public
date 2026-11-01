import requests, pathlib, concurrent.futures, json, datetime
root=pathlib.Path('.')
queries={
'source_pdf':'https://arxiv.org/pdf/2609.09972',
'source_abs':'https://arxiv.org/abs/2609.09972',
'arxiv':'http://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20all:percolation&sortBy=submittedDate&sortOrder=descending&max_results=30',
'openalex':'https://api.openalex.org/works?search=Percolation%20of%20the%20contact%20process%20on%20the%20regular%20tree&per-page=10',
'crossref':'https://api.crossref.org/works?query.title=Percolation%20of%20the%20contact%20process%20on%20the%20regular%20tree&rows=10',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.09972?fields=title,authors,year,citationCount,citations.title,citations.year,citations.externalIds',
'github':'https://api.github.com/search/repositories?q=%22contact+process%22+percolation'
}
def get(k,u):
 try:
  r=requests.get(u,timeout=45); p=root/(k+('.pdf' if k.endswith('pdf') else '.txt')); p.write_bytes(r.content)
  return {'service':k,'url':u,'status':r.status_code,'bytes':len(r.content),'date':str(datetime.date.today())}
 except Exception as e:return {'service':k,'url':u,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex: results=list(ex.map(lambda kv:get(*kv),queries.items()))
root.joinpath('search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print(json.dumps(results,indent=2))
