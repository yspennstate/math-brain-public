from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests, fitz, urllib.parse, xml.etree.ElementTree as ET
root=Path.cwd()
jobs={
 'source.pdf':'https://www.imo.universite-paris-saclay.fr/~nicolas.curien/cours/peccot.pdf',
 'budd.pdf':'https://arxiv.org/pdf/1506.01590',
 'conditioned.pdf':'https://arxiv.org/pdf/math/0602306',
 'arxiv.xml':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"peeling" AND (all:"critical" OR all:"exhaustion")','max_results':40,'sortBy':'submittedDate','sortOrder':'descending'}),
 'openalex.json':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'filled peeling critical Boltzmann map','per-page':15})}
def fetch(item):
 name,url=item
 try:
  r=requests.get(url,timeout=55); (root/(name+'.http.txt')).write_text(f'{url}\nHTTP {r.status_code}\n',encoding='utf8'); r.raise_for_status(); (root/name).write_bytes(r.content)
  if name.endswith('.pdf'):
   doc=fitz.open(stream=r.content,filetype='pdf'); (root/(name+'.txt')).write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
  return name,r.status_code,len(r.content)
 except Exception as e:return name,str(e)
with ThreadPoolExecutor(max_workers=5) as pool:
 for out in pool.map(fetch,jobs.items()):print(out)
