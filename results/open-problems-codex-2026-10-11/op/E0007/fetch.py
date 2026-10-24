import requests,concurrent.futures,json,time
from pathlib import Path
P=Path('.')
urls={
'source.pdf':'https://arxiv.org/pdf/0906.2293',
'arxiv.xml':'https://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20all:%22death%20rates%22&max_results=30',
'openalex.json':'https://api.openalex.org/works?search=multitype%20contact%20process%20unequal%20death%20rates&per-page=30',
'crossref.json':'https://api.crossref.org/works?query=multitype%20contact%20process%20unequal%20death%20rates&rows=20',
'semantic.json':'https://api.semanticscholar.org/graph/v1/paper/search?query=multitype%20contact%20process%20unequal%20death%20rates&limit=20&fields=title,year,authors,url,abstract',
'github.json':'https://api.github.com/search/repositories?q=multitype+contact+process',
'openalex_source.json':'https://api.openalex.org/works/https://doi.org/10.1214/09-PS139'}
def fetch(k,u):
 try:
  r=requests.get(u,timeout=45);P.joinpath(k).write_bytes(r.content)
  return {'file':k,'url':u,'status':r.status_code,'bytes':len(r.content),'date':'2026-10-12'}
 except Exception as e:return {'file':k,'url':u,'error':str(e),'date':'2026-10-12'}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
 for a in ex.map(lambda kv:fetch(*kv),urls.items()):
  with P.joinpath('search_log.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(a)+'\n')
  print(a,flush=True)
try:
 import pymupdf
 doc=pymupdf.open('source.pdf');P.joinpath('source.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+page.get_text() for i,page in enumerate(doc)),encoding='utf8')
 print(P.joinpath('source.txt').read_text(encoding='utf8')[:16000])
except Exception as e:print(e)
