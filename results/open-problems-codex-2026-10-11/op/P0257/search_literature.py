import concurrent.futures, json, urllib.request, urllib.parse, datetime
from pathlib import Path

queries = {
 'arxiv': 'http://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"nearest unvisited"','max_results':30}),
 'arxiv_https': 'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"nearest unvisited"','max_results':30}),
 'openalex': 'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'The Nearest Unvisited Vertex Walk','per-page':30}),
 'crossref': 'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'nearest unvisited vertex walk','rows':30}),
 'semantic': 'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1912.13175?fields=title,year,authors,citationCount,citations.title,citations.year,citations.externalIds',
 'github': 'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'"nearest unvisited"'}),
 'openalex_greedy': 'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'greedy walk random points nearest neighbor limit','per-page':30}),
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'probability-research/1.0'})
  with urllib.request.urlopen(req,timeout=35) as r: data=r.read()
  Path('search_'+name+'.txt').write_bytes(data)
  return {'service':name,'url':url,'date':'2026-10-12','ok':True,'bytes':len(data)}
 except Exception as e: return {'service':name,'url':url,'date':'2026-10-12','ok':False,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 results=list(pool.map(fetch,queries.items()))
Path('search_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
for r in results: print(r)
for name in ['openalex','openalex_greedy','crossref','semantic','github']:
 p=Path('search_'+name+'.txt')
 if not p.exists(): continue
 d=json.loads(p.read_text(encoding='utf-8')); print('\nRESULTS',name)
 if name.startswith('openalex'):
  for x in d.get('results',[]): print(x['id'],x.get('publication_year'),x.get('title'),x.get('doi'))
 elif name=='crossref':
  for x in d['message']['items']: print(x.get('title'),x.get('DOI'))
 else: print(json.dumps(d)[:12000])
