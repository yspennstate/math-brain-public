import urllib.request, urllib.parse, json, pathlib, concurrent.futures, datetime
ROOT=pathlib.Path(__file__).resolve().parent
queries={
 'source_html':'https://arxiv.org/html/2609.07621',
 'source_abs':'https://arxiv.org/abs/2609.07621',
 'arxiv_rotation':'https://export.arxiv.org/api/query?search_query=all:oriented%20AND%20all:rotation&max_results=20',
 'openalex':'https://api.openalex.org/works?search='+urllib.parse.quote('random walks oriented lattices irrational rotation')+'&per-page=20',
 'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote('random walks oriented lattices irrational rotation')+'&rows=20',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('random walks oriented lattices rotation')+'&limit=20&fields=title,authors,year,externalIds,abstract',
 'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('random walk oriented lattice rotation'),
 'openalex_source':'https://api.openalex.org/works?filter=locations.source.id:s4306400194&search=2609.07621&per-page=5',
}
def fetch(k,u):
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'MathematicalResearch/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  (ROOT/(k+'.txt')).write_bytes(data)
  return {'service_query':k,'url':u,'date':'2026-10-12','bytes':len(data),'status':'ok'}
 except Exception as e: return {'service_query':k,'url':u,'date':'2026-10-12','status':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 results=list(pool.map(lambda kv:fetch(*kv),queries.items()))
(ROOT/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for r in results: print(json.dumps(r))
