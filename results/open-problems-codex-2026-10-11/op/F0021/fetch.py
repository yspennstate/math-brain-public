import urllib.request, concurrent.futures, json, pathlib, datetime
p=pathlib.Path('.')
queries=[('source','https://arxiv.org/pdf/2401.01757'),('arxiv','https://export.arxiv.org/api/query?search_query=all:heavy-tailed+AND+all:polymer&start=0&max_results=30&sortBy=submittedDate&sortOrder=descending'),('openalex','https://api.openalex.org/works?search=heavy%20tailed%20directed%20polymer&per-page=30'),('crossref','https://api.crossref.org/works?query=heavy%20tailed%20directed%20polymer&rows=20'),('semantic','https://api.semanticscholar.org/graph/v1/paper/ARXIV:2401.01757?fields=title,year,citations.title,citations.year,citations.externalIds'),('github','https://api.github.com/search/repositories?q=heavy+tailed+directed+polymer')]
p.joinpath('LITERATURE.md').write_text('# Literature search\n\nSearch date: 2026-10-12 (machine date).\n'+''.join(f'- {n}: `{u}`\n' for n,u in queries),encoding='utf-8')
def get(item):
 n,u=item
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'ProbabilityResearch/1.0'})
  with urllib.request.urlopen(req,timeout=50) as r: data=r.read()
  p.joinpath(n+('.pdf' if n=='source' else '.json' if n not in ['arxiv'] else '.xml')).write_bytes(data)
  return n,len(data)
 except Exception as e:
  p.joinpath(n+'_error.txt').write_text(str(e),encoding='utf-8');return n,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 for r in ex.map(get,queries): print(r)
