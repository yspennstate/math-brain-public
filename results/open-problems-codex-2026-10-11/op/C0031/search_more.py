import pathlib,urllib.request,urllib.parse,json,concurrent.futures
R=pathlib.Path(__file__).parent
qs=[('cr_invertibility','https://api.crossref.org/works?',{'query':'smallest singular value heavy tailed no moment assumptions','rows':25}),('cr_almostsure','https://api.crossref.org/works?',{'query':'almost sure heavy tailed circular law','rows':25}),('arxiv_invertibility','https://export.arxiv.org/api/query?',{'search_query':'all:"smallest singular" AND (all:"heavy" OR all:"moment assumptions")','max_results':50,'sortBy':'submittedDate','sortOrder':'descending'})]
def go(x):
 name,base,p=x;url=base+urllib.parse.urlencode(p)
 try:
  with urllib.request.urlopen(url,timeout=45) as f:b=f.read()
  (R/(name+('.xml' if name.startswith('arxiv') else '.json'))).write_bytes(b);status=f'OK {len(b)}'
 except Exception as e:status=f'FAILED {e}'
 print(name,status,flush=True);return {'file':name,'url':url,'date':'2026-10-11','status':status}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:out=list(e.map(go,qs))
(R/'search_more_log.json').write_text(json.dumps(out,indent=2),encoding='utf8')
# Read-only lookup in specifically authorized roots.
base=pathlib.Path('~/<private-repo>/06_math_research')
for d in base.glob('probability_1000_intake_*'):
 for name in ['problems.jsonl','attempts.jsonl','sources.jsonl']:
  p=d/name
  if p.exists():
   for i,line in enumerate(p.read_text(encoding='utf8').splitlines(),1):
    if 'C0031' in line:print('LEDGER',str(p),i,line,flush=True)
import subprocess
p=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True,encoding='utf8',timeout=60)
for name in p.stdout.splitlines():
 if 'c0031' in name.lower() or 'heavy_tailed_circular' in name.lower():
  print('PUBLISHED_PATH',name,flush=True)
  q=subprocess.run(['git','-C','~/math-open-problems','show','origin/master:'+name],capture_output=True,text=True,encoding='utf8',timeout=60)
  print(q.stdout[:25000],flush=True)
