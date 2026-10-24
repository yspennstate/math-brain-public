import urllib.request,urllib.parse,json,concurrent.futures,xml.etree.ElementTree as E
from pathlib import Path
qs={
'arxiv_poisson':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"polymer" AND all:"Poisson"','max_results':60,'sortBy':'submittedDate','sortOrder':'descending'}),
'arxiv_local':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"polymer" AND (all:"local limit" OR all:"weak disorder")','max_results':50,'sortBy':'submittedDate','sortOrder':'descending'}),
'oa_retry':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Brownian Polymers in Poissonian Environment a survey','per_page':10}),
's2_source':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1805.10899?fields=title,authors,year,externalIds,citations.title,citations.year,citations.externalIds',
'crossref_local':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query.bibliographic':'directed polymers local limit theorem weak disorder','rows':25})}
def get(k,u):
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Research-E0112'}),timeout=45);b=r.read();Path('search_'+k+'.txt').write_bytes(b);return k,u,r.status,len(b),None
 except Exception as e:return k,u,None,0,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:out=list(ex.map(lambda a:get(*a),qs.items()))
with Path('LITERATURE.md').open('a',encoding='utf-8') as f:
 for k,u,s,n,e in out:f.write(f'- 2026-10-11 {k}: `{u}`; HTTP {s}, bytes {n}, error {e}.\n')
for row in out: print(row)
ns={'a':'http://www.w3.org/2005/Atom'}
for k in ['arxiv_poisson','arxiv_local']:
 p=Path('search_'+k+'.txt')
 if p.exists():
  for e in E.fromstring(p.read_bytes()).findall('a:entry',ns):
   print(k,e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns));print(e.findtext('a:summary',namespaces=ns))
for k in ['oa_retry','s2_source']:
 p=Path('search_'+k+'.txt')
 if p.exists():print(k,p.read_text()[:22000])
