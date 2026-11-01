import concurrent.futures, json, urllib.request, urllib.parse, datetime
from pathlib import Path
q = urllib.parse.quote
queries = {
 'arxiv': 'http://export.arxiv.org/api/query?search_query='+q('all:"disordered" AND all:"zero-range"')+'&max_results=40',
 'arxiv_https': 'https://export.arxiv.org/api/query?search_query='+q('all:"zero-range" AND all:"convergence"')+'&max_results=40',
 'openalex': 'https://api.openalex.org/works?search='+q('disordered zero range convergence equilibrium')+'&per-page=30',
 'openalex_source': 'https://api.openalex.org/works?search='+q('Recent results and open problems on the hydrodynamics of disordered asymmetric exclusion and zero-range processes')+'&per-page=5',
 'crossref': 'https://api.crossref.org/works?query='+q('disordered zero range convergence equilibrium')+'&rows=30',
 'semantic': 'https://api.semanticscholar.org/graph/v1/paper/search?query='+q('disordered zero range convergence')+'&limit=30&fields=title,authors,year,externalIds,url,abstract',
 'github': 'https://api.github.com/search/repositories?q='+q('disordered zero range')+'&per_page=20',
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'D0024-research/1.0'})
  with urllib.request.urlopen(req,timeout=70) as r: data=r.read(); status=r.status
  Path('search_'+name+'.txt').write_bytes(data)
  return {'service':name,'url':url,'date':'2026-10-11','status':status,'bytes':len(data)}
 except Exception as e:
  return {'service':name,'url':url,'date':'2026-10-11','error':str(e)}
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
  for result in ex.map(fetch,queries.items()):
   with Path('search_log.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps(result)+'\n')
   print(json.dumps(result),flush=True)
