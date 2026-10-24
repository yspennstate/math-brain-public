import concurrent.futures, datetime, json, pathlib, urllib.request, urllib.parse
ROOT=pathlib.Path(__file__).parent
queries={
'source_pdf':'https://arxiv.org/pdf/2303.11486',
'source_html':'https://arxiv.org/html/2303.11486',
'arxiv_http':'http://export.arxiv.org/api/query?search_query=all:Riesz+AND+all:rigidity&start=0&max_results=40',
'arxiv_https':'https://export.arxiv.org/api/query?search_query=all:Riesz+AND+all:rigidity&start=0&max_results=40',
'openalex_search':'https://api.openalex.org/works?search=Riesz%20number%20rigidity&per-page=50',
'openalex_source':'https://api.openalex.org/works?search=Non-rigidity%20Properties%20of%20the%20Coulomb%20Gas&per-page=5',
'crossref':'https://api.crossref.org/works?query=Riesz%20number%20rigidity&rows=30',
'semantic_source':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2303.11486?fields=title,authors,year,externalIds,citations.title,citations.year,citations.externalIds',
'semantic_search':'https://api.semanticscholar.org/graph/v1/paper/search?query=Riesz%20number%20rigidity&limit=30&fields=title,authors,year,externalIds',
'github':'https://api.github.com/search/repositories?q=Riesz+rigidity&per_page=30'}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'MathematicalResearch/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  (ROOT/(name+('.pdf' if name.endswith('pdf') else '.txt'))).write_bytes(data)
  outcome=f'OK {len(data)} bytes'
 except Exception as e: outcome=str(e)
 with (ROOT/'LITERATURE.md').open('a',encoding='utf8') as f: f.write(f'\n- {datetime.date.today()} | {name} | {url} | {outcome}\n')
 return name,outcome
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  for item in pool.map(fetch,queries.items()): print(*item,flush=True)
