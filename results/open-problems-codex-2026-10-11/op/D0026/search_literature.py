import concurrent.futures, datetime, json, pathlib, urllib.request, urllib.parse
ROOT = pathlib.Path(__file__).resolve().parent
queries = [
 ('arxiv', 'all:"FA-1f"', 'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"FA-1f"')+'&sortBy=submittedDate&sortOrder=descending&max_results=40'),
 ('arxiv_title', 'Long time behaviour of one facilitated', 'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('ti:"Long time behaviour" AND all:"facilitated"')+'&max_results=10'),
 ('openalex', 'FA-1f convergence equilibrium', 'https://api.openalex.org/works?search='+urllib.parse.quote('FA-1f convergence equilibrium')+'&per-page=40'),
 ('openalex_source', 'Long time behaviour of one facilitated kinetically constrained models', 'https://api.openalex.org/works?search='+urllib.parse.quote('Long time behaviour of one facilitated kinetically constrained models')+'&per-page=10'),
 ('crossref', 'FA-1f convergence equilibrium', 'https://api.crossref.org/works?query='+urllib.parse.quote('FA-1f convergence equilibrium')+'&rows=30'),
 ('semantic', 'FA-1f convergence equilibrium', 'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('FA-1f convergence equilibrium')+'&limit=30&fields=title,authors,year,externalIds,abstract,url'),
 ('semantic_citations', 'ARXIV:2510.20461 citations', 'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2510.20461/citations?fields=title,authors,year,externalIds,abstract,url&limit=100'),
 ('github', 'FA-1f', 'https://api.github.com/search/repositories?q='+urllib.parse.quote('FA-1f')+'&per_page=30'),
 ('github_fredrickson', 'Fredrickson Andersen', 'https://api.github.com/search/repositories?q='+urllib.parse.quote('Fredrickson Andersen')+'&per_page=30'),
]
def fetch(item):
 name, query, url = item
 record={'service':name,'query':query,'url':url,'date':datetime.datetime.now().isoformat()}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'ProbabilityResearch/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read();record['http_status']=r.status
  (ROOT/(name+'.response')).write_bytes(data)
  record['saved']=name+'.response'
  print(name, len(data), flush=True)
 except Exception as e:
  record['error']=repr(e); print(name,repr(e),flush=True)
 return record
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 results=list(ex.map(fetch,queries))
(ROOT/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
try:
 data=json.loads((ROOT/'openalex_source.response').read_text(encoding='utf-8'))
 for work in data.get('results',[]):
  if 'one facilitated' in work['title'].lower():
   wid=work['id'].rsplit('/',1)[-1]
   result=fetch(('openalex_citations', 'cites:'+wid,'https://api.openalex.org/works?filter=cites:'+wid+'&per-page=100'))
   results.append(result)
except Exception as e: print('citation lookup:',repr(e),flush=True)
(ROOT/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
