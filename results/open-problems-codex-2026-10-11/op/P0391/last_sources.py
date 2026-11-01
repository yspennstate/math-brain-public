import pathlib,urllib.request,concurrent.futures,subprocess,json
root=pathlib.Path(__file__).resolve().parent
urls={'citing_stable':'https://arxiv.org/pdf/2105.02349','citing_fairness':'https://arxiv.org/pdf/1411.4841','fralix_page':'https://doi.org/10.1007/s11134-010-9202-1'}
def get(pair):
 name,url=pair
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Research-check/1.0'}),timeout=40) as f: data=f.read()
  path=root/(name+('.pdf' if name.startswith('citing') else '.html'));path.write_bytes(data)
  if name.startswith('citing'):
   import pymupdf
   d=pymupdf.open(path);tx='\n'.join(p.get_text() for p in d)
   (root/(name+'.txt')).write_text(tx,encoding='utf-8')
   lines=tx.splitlines();hits=[]
   for i,line in enumerate(lines):
    if any(s in line.lower() for s in ['symmetric queue','conjecture','brownian','zwart']):hits.append('\n'.join(lines[max(0,i-2):i+3]))
   print(name,tx[:1200], '\nHITS\n','\n'.join(hits)[:6500],flush=True)
  return dict(service=name,query=url,date='2026-10-11',result='saved',bytes=len(data))
 except Exception as e:return dict(service=name,query=url,date='2026-10-11',result=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex: res=list(ex.map(get,urls.items()))
(root/'last_sources_log.json').write_text(json.dumps(res,indent=2),encoding='utf-8'); print(json.dumps(res,indent=2),flush=True)
p=subprocess.run(['git','-C','~/math-open-problems','grep','-n','-m','2','-F','P0391','origin/master','--','probability_1000'],capture_output=True,text=True,encoding='utf-8',timeout=120)
(root/'prior_git_hits.txt').write_text(p.stdout,encoding='utf-8')
print('GIT P0391 HITS', '\n'.join(line[:2200] for line in p.stdout.splitlines()[:12]))
