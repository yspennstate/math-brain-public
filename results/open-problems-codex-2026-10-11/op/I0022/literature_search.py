import urllib.request, urllib.parse, json, pathlib, datetime, concurrent.futures
ROOT=pathlib.Path(__file__).parent
queries={
 'janson_source':'https://arxiv.org/pdf/1112.0510',
 'arxiv_condensation':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:condensation AND (all:trees OR all:Galton)')+'&max_results=30',
 'openalex_scaling':'https://api.openalex.org/works?search='+urllib.parse.quote('condensation trees scaling limit')+'&per-page=30',
 'openalex_source':'https://api.openalex.org/works/https://doi.org/10.1214/11-PS188',
 'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote('condensation Galton Watson scaling limits')+'&rows=20',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('condensation trees scaling limit')+'&limit=20&fields=title,authors,year,externalIds,url,abstract',
 'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('condensation trees scaling'),
}
def get(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'ProbabilityResearch/1.0'})
  with urllib.request.urlopen(req,timeout=55) as r: data=r.read()
  (ROOT/(name+('.pdf' if name=='janson_source' else '.txt'))).write_bytes(data)
  result=f'{name}: OK {len(data)} bytes'
 except Exception as e: result=f'{name}: ERROR {e}'
 with (ROOT/'LITERATURE.md').open('a',encoding='utf-8') as f: f.write(f'\n- 2026-10-11 | {name} | {url} | {result}\n')
 return result
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
  for result in pool.map(get,queries.items()): print(result,flush=True)
