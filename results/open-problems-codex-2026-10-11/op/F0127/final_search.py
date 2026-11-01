import requests,json,concurrent.futures
from urllib.parse import quote
from pathlib import Path
qs={
'arxiv_later':'http://export.arxiv.org/api/query?search_query='+quote('all:"coalescing" AND (all:"Kingman" OR all:"mean field") AND submittedDate:[201310010000 TO 202610112359]')+'&max_results=40',
'openalex_citing_source':'https://api.openalex.org/works?filter=cites:'+quote('https://doi.org/10.3150/12-BEJSP04',safe='')+'&per-page=50',
'openalex_hermon':'https://api.openalex.org/works/https://doi.org/10.1214/21-AIHP1208',
'semantic_hermon':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1908.08525?fields=title,year,authors,externalIds,citations.title,citations.year',
'github_broad':'https://api.github.com/search/repositories?q='+quote('coalescing random walks'),
'crossref_exact_oliveira':'https://api.crossref.org/works/10.1214/12-AOP813',
'crossref_exact_bigbang':'https://api.crossref.org/works/10.1214/22-AOP1571'}
def f(kv):
 k,u=kv
 try:
  r=requests.get(u,timeout=40);Path(k+'.json').write_bytes(r.content);msg=f'HTTP {r.status_code}; {len(r.content)} bytes'
 except Exception as e:msg=str(e)
 return k,u,msg
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
 for k,u,msg in ex.map(f,qs.items()):
  print(k,msg)
  with open('LITERATURE.md','a',encoding='utf-8') as out:out.write(f'\n- 2026-10-11 | {k} | `{u}` | {msg}\n')
