import concurrent.futures, json, pathlib, urllib.request, urllib.parse, datetime
P=pathlib.Path(__file__).parent
q=urllib.parse.quote
jobs={
 'aim_https': 'https://aimath.org/pastworkshops/roadtokpzrep.pdf',
 'aim_http': 'http://aimath.org/pastworkshops/roadtokpzrep.pdf',
 'arxiv_http': 'http://export.arxiv.org/api/query?search_query='+q('all:TASEP AND (all:killing OR all:annihilation OR all:defect)')+'&max_results=40',
 'arxiv_https': 'https://export.arxiv.org/api/query?search_query='+q('all:TASEP AND (all:killing OR all:annihilation OR all:defect)')+'&max_results=40',
 'openalex_killing':'https://api.openalex.org/works?search='+q('TASEP killing')+'&per-page=30',
 'openalex_source':'https://api.openalex.org/works?search='+q('all roads to KPZ')+'&per-page=10',
 'crossref':'https://api.crossref.org/works?query='+q('TASEP killing invariant measures')+'&rows=30',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query='+q('TASEP killing')+'&limit=30&fields=title,authors,year,abstract,url,externalIds',
 'github':'https://api.github.com/search/repositories?q='+q('TASEP killing')+'&per_page=30',
 'openalex_invariant':'https://api.openalex.org/works?search='+q('TASEP invariant measures local particle removal')+'&per-page=30',
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (mathematical literature research)','Accept':'*/*'})
  with urllib.request.urlopen(req,timeout=40) as r: data=r.read(); code=r.status
  file=name+('.pdf' if data.startswith(b'%PDF') else '.json' if data.lstrip().startswith(b'{') else '.txt')
  (P/file).write_bytes(data)
  result={'service':name,'url':url,'date':'2026-10-12','status':code,'file':file,'bytes':len(data)}
 except Exception as e: result={'service':name,'url':url,'date':'2026-10-12','error':str(e)}
 print(json.dumps(result),flush=True)
 return result
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: out=list(ex.map(fetch,jobs.items()))
(P/'search_log.json').write_text(json.dumps(out,indent=2),encoding='utf8')
