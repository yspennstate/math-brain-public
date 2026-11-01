import subprocess,pathlib,json,concurrent.futures,urllib.request
p=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True)
paths=[s for s in p.stdout.splitlines() if 'p0336' in s.lower()]
print('repo matching paths',paths)
for i,s in enumerate(paths):
 t=subprocess.run(['git','-C','~/math-open-problems','show','origin/master:'+s],capture_output=True,text=True,encoding='utf8')
 pathlib.Path(f'repo_P0336_{i}.txt').write_text(t.stdout,encoding='utf8');print(t.stdout[:3000])
for d in pathlib.Path('~/<private-repo>/06_math_research').glob('probability_1000_intake_*'):
 for name in ['problems.jsonl','attempts.jsonl','sources.jsonl']:
  f=d/name
  if f.exists():
   for line in f.open(encoding='utf8'):
    if 'P0336' in line: print('LEDGER',str(f),line[:6500])
ids=['2609.22240','2608.29565','2607.18191','2610.10257','2609.13587','2609.05062','2607.16881']
def get(id):
 u='https://arxiv.org/pdf/'+id
 try:
  with urllib.request.urlopen(u,timeout=40) as r:b=r.read()
  pathlib.Path('lead_'+id+'.pdf').write_bytes(b)
  import pymupdf
  d=pymupdf.open(stream=b,filetype='pdf');s='\n'.join(f'PDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(d));pathlib.Path('lead_'+id+'.txt').write_text(s,encoding='utf8')
  return {'service':'arxiv_pdf_lead','url':u,'date':'2026-10-12','status':'ok','pages':len(d),'opening':s[:1000]}
 except Exception as e:return {'service':'arxiv_pdf_lead','url':u,'date':'2026-10-12','status':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:r=list(ex.map(get,ids))
pathlib.Path('search_log3.json').write_text(json.dumps(r,indent=2),encoding='utf8');print(json.dumps(r,indent=2))
