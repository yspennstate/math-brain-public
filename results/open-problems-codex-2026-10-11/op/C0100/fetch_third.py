import requests,pathlib,pymupdf,json,concurrent.futures
jobs={'stability':'https://arxiv.org/pdf/1708.09432','openalex_doi':'https://api.openalex.org/works/https://doi.org/10.1090/bull/1563','openalex_citing':'https://api.openalex.org/works?filter=cites:W2535495547&per_page=100','semantic_bulk':'https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=%22sandpile%22%20%2B%22identity%22&fields=title,year,externalIds','arxiv_fractions':'https://export.arxiv.org/api/query?search_query=all:sandpile+AND+(all:frequency+OR+all:frequencies+OR+all:Pegden)&max_results=70&sortBy=submittedDate&sortOrder=descending'}
def f(k,u):
 try:
  r=requests.get(u,timeout=45);pathlib.Path(k+('.pdf' if k=='stability' else '.xml' if k=='arxiv_fractions' else '.json')).write_bytes(r.content)
  if k=='stability' and r.status_code==200:
   d=pymupdf.open(stream=r.content,filetype='pdf');pathlib.Path(k+'.txt').write_text('\n'.join(f'\nPAGE {i+1}\n'+x.get_text() for i,x in enumerate(d)),encoding='utf8')
  return dict(service=k,url=u,status=r.status_code,bytes=len(r.content),date='2026-10-12')
 except Exception as e:return dict(service=k,url=u,error=str(e),date='2026-10-12')
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:r=list(ex.map(lambda x:f(*x),jobs.items()))
p=pathlib.Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+r,indent=2));print(json.dumps(r,indent=2))
