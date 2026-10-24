import urllib.request,urllib.parse,json,concurrent.futures,pathlib
p=pathlib.Path('.')
queries={
'arxiv':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"ideal" AND all:"Voronoi"')+'&start=0&max_results=40',
'openalex':'https://api.openalex.org/works?search='+urllib.parse.quote('Ideal Poisson Voronoi tessellations')+'&per-page=30',
'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote('Ideal Poisson Voronoi tessellations')+'&rows=20',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2303.16831/citations?fields=title,authors,year,externalIds&limit=100',
'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('ideal Voronoi'),
}
def fetch(k,u):
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'P0409-research/1.0'})
  with urllib.request.urlopen(req,timeout=50) as r: s=r.read().decode()
  p.joinpath('search_'+k+'.txt').write_text(s,encoding='utf-8')
  return k,u,'OK'
 except Exception as e:return k,u,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: out=list(ex.map(lambda x:fetch(*x),queries.items()))
p.joinpath('LITERATURE.md').write_text('# Literature search\n\nDate: 2026-10-12. Source: D’Achille, Curien, Enriquez, Lyons and Ünel, Ideal Poisson–Voronoi tessellations on hyperbolic spaces, arXiv:2303.16831.\n\n'+ '\n'.join(f'- {k}: `{u}` — {s}' for k,u,s in out)+'\n',encoding='utf-8')
print(out)
import pymupdf
pdf=pymupdf.open('source.pdf')
for i in [26,27,28,47]:
 print('\nPAGE',i+1,'\n',pdf[i].get_text())
