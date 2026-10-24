from pathlib import Path
import urllib.request, urllib.parse, concurrent.futures,json,subprocess
urls={'arxiv_broad.xml':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"log-concavity" AND (all:exclusion OR all:TASEP OR all:"Schur process")')+'&max_results=40','bkm.pdf':'https://arxiv.org/pdf/2412.15116','petrov_page.html':'https://lpetrov.cc/2025/03/AIM-KPZ/','openalex_retry.json':'https://api.openalex.org/works?search=TASEP%20log-concavity&per_page=10','semantic_retry.json':'https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=TASEP%20log-concavity&fields=title,year,authors,url'}
def fetch(item):
 k,u=item
 try:
  r=urllib.request.urlopen(u,timeout=40);b=r.read();Path(k).write_bytes(b);return[k,u,r.status,len(b)]
 except Exception as e:return[k,u,str(e)]
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=5).map(fetch,urls.items()));Path('search_log_2.json').write_text(json.dumps(r,indent=2));print(r)
import pymupdf
if Path('bkm.pdf').exists():
 d=pymupdf.open('bkm.pdf');s='\n'.join(f'PAGE {i+1}\n'+p.get_text() for i,p in enumerate(d));Path('bkm.txt').write_text(s,encoding='utf8')
 for line in s.splitlines():
  if any(w in line.lower() for w in ['tasep','prékopa','prekopa','schur','midpoint','lehec','klartag']):print(line)
for root in Path('~/<private-repo>/06_math_research').glob('probability_1000_intake_*'):
 for name in ['problems.jsonl','attempts.jsonl','sources.jsonl']:
  p=root/name
  if p.exists():
   for line in p.open(encoding='utf8'):
    if 'P0281' in line: print(str(p),line[:9000])
r=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True,encoding='utf8');paths=[x for x in r.stdout.splitlines() if 'P0281' in x or 'p0281' in x];Path('prior_repo_paths.txt').write_text('\n'.join(paths));print('repo paths',paths[:30])
