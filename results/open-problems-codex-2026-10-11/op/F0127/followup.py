import requests,concurrent.futures
from pathlib import Path
from urllib.parse import quote
qs={'oliveira_pdf':'https://arxiv.org/pdf/1109.5684','hermon_pdf':'https://arxiv.org/pdf/1908.08525','bigbang_pdf':'https://arxiv.org/pdf/2105.11585','crossref_hermon':'https://api.crossref.org/works?query.title='+quote('Some inequalities for reversible Markov chains and branching random walks via spectral optimization')+'&rows=3','openalex_retry':'https://api.openalex.org/works?search='+quote('Interacting particle systems as stochastic social dynamics')+'&per_page=3','semantic_source':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1309.6766?fields=title,citations.title,citations.year,citations.externalIds'}
def f(kv):
 k,u=kv
 try:
  r=requests.get(u,timeout=45);Path(k+('.pdf' if k.endswith('pdf') else '.json')).write_bytes(r.content);s=f'HTTP {r.status_code}; {len(r.content)} bytes'
  if k.endswith('pdf') and r.status_code==200:
   import pymupdf
   d=pymupdf.open(k+'.pdf');Path(k+'.txt').write_text('\n'.join(p.get_text() for p in d),encoding='utf-8')
 except Exception as e:s=str(e)
 return k,u,s
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 for k,u,s in ex.map(f,qs.items()):
  print(k,s)
  with open('LITERATURE.md','a',encoding='utf-8') as out:out.write(f'\n- 2026-10-11 | {k} | `{u}` | {s}\n')
