import pathlib,urllib.request,urllib.parse,concurrent.futures
p=pathlib.Path('.')
qs=[('improved','https://arxiv.org/pdf/2509.21453'),('lindeberg','https://arxiv.org/pdf/2304.04871'),('crossref_source','https://api.crossref.org/works?query.title='+urllib.parse.quote('Directed polymers in a random environment a review of the phase transitions')+'&rows=3'),('semantic_citations','https://api.semanticscholar.org/graph/v1/paper/ARXIV:2401.01757/citations?fields=title,year,externalIds&limit=100'),('openalex_citations','https://api.openalex.org/works?filter=cites:https%3A%2F%2Farxiv.org%2Fabs%2F2401.01757&per_page=100')]
with p.joinpath('LITERATURE.md').open('a',encoding='utf-8') as f:
 for n,u in qs:f.write(f'- {n}: `{u}` (2026-10-12).\n')
def get(z):
 n,u=z
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'math-research'}),timeout=45) as r:data=r.read()
  p.joinpath(n+('.pdf' if n in ['improved','lindeberg'] else '.json')).write_bytes(data);return n,len(data)
 except Exception as e:p.joinpath(n+'_error.txt').write_text(str(e));return n,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 for r in ex.map(get,qs):print(r)
