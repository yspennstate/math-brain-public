import requests,concurrent.futures,json
from pathlib import Path
urls={
'openalex_source_retry.json':'https://api.openalex.org/works/doi:10.1214/08-AAP590',
'openalex_retry.json':'https://api.openalex.org/works?search=competing%20contact%20process&per_page=50',
'crossref_target.json':'https://api.crossref.org/works?query=%22contact%20process%22%20%22unequal%22&rows=30',
'semantic_retry.json':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:0906.2293/citations?limit=100&fields=title,year,authors,abstract',
'arxiv_target.xml':'https://export.arxiv.org/api/query?search_query=all:%22multitype%20contact%22&max_results=50'}
def f(k,u):
 try:
  r=requests.get(u,timeout=35);Path(k).write_bytes(r.content);a={'file':k,'url':u,'status':r.status_code,'date':'2026-10-12'}
  if k=='openalex_source_retry.json' and r.status_code==200:
   obj=r.json();url='https://api.openalex.org/works?filter=cites:'+obj['id'].split('/')[-1]+'&per_page=100';s=requests.get(url,timeout=35);Path('openalex_citing.json').write_bytes(s.content)
   with open('search_log.jsonl','a',encoding='utf8') as g:g.write(json.dumps({'url':url,'status':s.status_code,'date':'2026-10-12','file':'openalex_citing.json'})+'\n')
 except Exception as e:a={'url':u,'error':str(e),'date':'2026-10-12'}
 with open('search_log.jsonl','a',encoding='utf8') as g:g.write(json.dumps(a)+'\n')
 print(a,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:list(ex.map(lambda kv:f(*kv),urls.items()))
