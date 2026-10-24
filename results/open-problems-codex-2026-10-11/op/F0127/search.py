import requests,concurrent.futures,json
from pathlib import Path
from urllib.parse import quote
queries={
'aldous_pdf':'https://arxiv.org/pdf/1309.6766',
'arxiv_api':'http://export.arxiv.org/api/query?search_query='+quote('all:"coalescing random walks" AND all:"mean field"')+'&max_results=15',
'openalex_search':'https://api.openalex.org/works?search='+quote('mean field conditions coalescing random walks')+'&per-page=15',
'openalex_source':'https://api.openalex.org/works/https://doi.org/10.3150/12-BEJSP04',
'crossref':'https://api.crossref.org/works?query='+quote('mean field conditions coalescing random walks')+'&rows=10',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query='+quote('mean field coalescing random walks')+'&limit=10&fields=title,authors,year,externalIds,url,abstract',
'github':'https://api.github.com/search/repositories?q='+quote('coalescing random walks Kingman')
}
def fetch(item):
 k,u=item
 try:
  r=requests.get(u,timeout=65);Path(k+('.pdf' if k.endswith('pdf') else '.json')).write_bytes(r.content)
  msg=f'{k}: HTTP {r.status_code}; {len(r.content)} bytes'
 except Exception as e:msg=f'{k}: {e}'
 return k,u,msg
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
 for k,u,msg in ex.map(fetch,queries.items()):
  print(msg)
  with open('LITERATURE.md','a',encoding='utf-8') as f:f.write(f'\n- 2026-10-11 | {k} | `{u}` | {msg}\n')
try:
 import pymupdf
 doc=pymupdf.open('aldous_pdf.pdf');Path('aldous_source.txt').write_text('\n'.join(p.get_text() for p in doc),encoding='utf-8')
 print('PDF extracted')
except Exception as e:print('PDF extract:',e)
