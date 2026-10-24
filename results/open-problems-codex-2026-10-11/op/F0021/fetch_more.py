import urllib.request,urllib.parse,concurrent.futures,pathlib,json
p=pathlib.Path('.')
base='https://export.arxiv.org/api/query?'
qs=[('arxiv_kpz',base+urllib.parse.urlencode({'search_query':'all:"directed polymer" AND (all:universality OR all:heavy) AND submittedDate:[20240101 TO 20261012]','max_results':70,'sortBy':'submittedDate','sortOrder':'descending'})),('arxiv_fixed',base+urllib.parse.urlencode({'search_query':'all:"polymer" AND all:"fixed temperature"','max_results':30})),('openalex_retry','https://api.openalex.org/works?search=directed%20polymer%20heavy%20tail&per_page=20'),('openalex_source','https://api.openalex.org/works?filter=title.search:Directed%20polymers%20in%20a%20random%20environment&per_page=10'),('semantic_retry','https://api.semanticscholar.org/graph/v1/paper/search?query=heavy%20tailed%20directed%20polymer&limit=20&fields=title,year,externalIds'),('crossref_kpz','https://api.crossref.org/works?query.bibliographic=directed%20polymer%20KPZ%20universality&filter=from-pub-date:2024-01-01&rows=25'),('newchaos','https://arxiv.org/pdf/2602.04429'),('physics','https://arxiv.org/pdf/1411.1242')]
with p.joinpath('LITERATURE.md').open('a',encoding='utf-8') as f:
 for n,u in qs:f.write(f'- {n}: `{u}` (2026-10-12).\n')
def get(z):
 n,u=z
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'research-math/1.0'}),timeout=45) as r:data=r.read()
  ext='.pdf' if n in ['newchaos','physics'] else '.xml' if n.startswith('arxiv') else '.json'
  p.joinpath(n+ext).write_bytes(data);return n,len(data)
 except Exception as e:p.joinpath(n+'_error.txt').write_text(str(e));return n,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 for r in ex.map(get,qs):print(r)
