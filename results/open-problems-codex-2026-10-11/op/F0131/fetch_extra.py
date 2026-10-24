import requests,json,concurrent.futures
from pathlib import Path
from pypdf import PdfReader
jobs=[('random','https://arxiv.org/pdf/1909.07849'),('reduction','https://arxiv.org/pdf/2009.05968'),('fr','https://arxiv.org/pdf/math/0702450'),('lp_bounds','https://arxiv.org/pdf/0704.0688'),('openalex_citing','https://api.openalex.org/works?filter=cites:W2145796065&per-page=100'),('arxiv_recent','https://export.arxiv.org/api/query?search_query=all:sandpile+AND+(all:convergence+OR+all:holes+OR+all:polygon)&start=0&max_results=80&sortBy=submittedDate&sortOrder=descending')]
def run(j):
 name,url=j
 try:
  r=requests.get(url,timeout=45);pdf=r.content.startswith(b'%PDF');p=Path('downloads',name+('.pdf' if pdf else '.txt'));p.write_bytes(r.content)
  if pdf:Path('downloads',name+'.txt').write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+x.extract_text() for i,x in enumerate(PdfReader(p).pages)),encoding='utf8')
  return dict(service=name,url=url,date='2026-10-11',status=r.status_code,bytes=len(r.content))
 except Exception as e:return dict(service=name,url=url,date='2026-10-11',error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 for row in pool.map(run,jobs):
  with open('search_log.jsonl','a',encoding='utf8') as f:f.write(json.dumps(row)+'\n')
  print(row)
