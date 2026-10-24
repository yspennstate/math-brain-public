import requests,concurrent.futures,json,pymupdf
from pathlib import Path
jobs={'interface.pdf':'https://arxiv.org/pdf/2602.23149','asymmetric.pdf':'https://arxiv.org/pdf/1803.01533','slow.xml':'https://export.arxiv.org/api/query?search_query=all:%22quasi-neutral%20contact%20process%22&max_results=10','voter.xml':'https://export.arxiv.org/api/query?search_query=ti:%22Voter%20Model%20Perturbations%22&max_results=10','openalex_citing_retry.json':'https://api.openalex.org/works?filter=cites:'+json.loads(Path('openalex_source_retry.json').read_text())['id'].split('/')[-1]+'&per-page=100'}
def f(k,u):
 try:
  r=requests.get(u,timeout=40);Path(k).write_bytes(r.content)
  a={'date':'2026-10-12','url':u,'file':k,'status':r.status_code}
  if k.endswith('.pdf') and r.status_code==200:
   d=pymupdf.open(k);Path(k[:-4]+'.txt').write_text('\n'.join('\nPDF PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
 except Exception as e:a={'date':'2026-10-12','url':u,'error':str(e)}
 with open('search_log.jsonl','a',encoding='utf8') as g:g.write(json.dumps(a)+'\n')
 print(a,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:list(ex.map(lambda kv:f(*kv),jobs.items()))
