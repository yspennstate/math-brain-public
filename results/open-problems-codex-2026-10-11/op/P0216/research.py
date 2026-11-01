import urllib.request, urllib.parse, json, pathlib, concurrent.futures
ROOT=pathlib.Path(__file__).resolve().parent
queries={
 'aldous_page':'https://www.stat.berkeley.edu/~aldous/Research/OP/substructures.html',
 'arxiv':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"common" AND all:"partial orders"')+'&max_results=30',
 'openalex':'https://api.openalex.org/works?search='+urllib.parse.quote('largest common random substructures')+'&per-page=20',
 'openalex_posets':'https://api.openalex.org/works?search='+urllib.parse.quote('common random two dimensional partial orders')+'&per-page=20',
 'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote('largest common random substructures')+'&rows=20',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('largest common random substructures')+'&limit=20&fields=title,authors,year,url,abstract,externalIds',
 'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('common random partial orders'),
}
def get(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'MathematicsResearch/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  (ROOT/(name+'.raw')).write_bytes(data)
  return {'service':name,'url':url,'bytes':len(data),'status':'ok'}
 except Exception as e: return {'service':name,'url':url,'status':str(e)}
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
  results=list(pool.map(get,queries.items()))
 (ROOT/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
 for x in results: print(json.dumps(x))
