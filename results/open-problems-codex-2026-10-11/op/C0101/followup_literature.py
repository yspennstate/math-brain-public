import requests,json,concurrent.futures,xml.etree.ElementTree as ET
from pathlib import Path
R=Path(__file__).parent
jobs=[
('crossref_source','https://api.crossref.org/works',{'query.title':'Laplacian growth sandpiles and scaling limits','rows':3}),
('openalex_retry','https://api.openalex.org/works',{'search':'"integer superharmonic"','per_page':25}),
('openalex_source','https://api.openalex.org/works/https://doi.org/10.1090/bull/1553',{}),
('semantic_bulk','https://api.semanticscholar.org/graph/v1/paper/search/bulk',{'query':'"integer superharmonic"','fields':'title,year,authors,externalIds,abstract'}),
('semantic_source','https://api.semanticscholar.org/graph/v1/paper/ARXIV:1611.00411/citations',{'limit':100,'fields':'title,year,authors,externalIds,abstract'}),
('arxiv_higher','https://export.arxiv.org/api/query',{'search_query':'all:sandpile AND (all:"higher dimensions" OR all:"maximal matrices")','max_results':60}),
('f_lattice','https://arxiv.org/pdf/2110.07556',{}),
('solitons','https://arxiv.org/pdf/2212.03717',{})]
def fetch(job):
 name,url,params=job
 rec={'date':'2026-10-12','service':name,'url':url,'query':params}
 try:
  res=requests.get(url,params=params,timeout=45,headers={'User-Agent':'C0101-math-research'})
  rec['status']=res.status_code
  rec['request_url']=res.url
  if name in ('f_lattice','solitons') and res.status_code==200:
   import pymupdf
   (R/(name+'.pdf')).write_bytes(res.content)
   doc=pymupdf.open(stream=res.content,filetype='pdf')
   (R/(name+'.txt')).write_text('\n'.join('PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
  else: (R/(name+'.json')).write_text(res.text,encoding='utf-8')
  print(name,res.status_code,flush=True)
 except Exception as e: rec['error']=str(e)
 return rec
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p: results=list(p.map(fetch,jobs))
(R/'followup_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
with (R/'LITERATURE.md').open('a',encoding='utf-8') as f:
 f.write('\n## Follow-up searches and fetches, 2026-10-12\n')
 for r in results: f.write('- '+json.dumps(r)+'\n')
