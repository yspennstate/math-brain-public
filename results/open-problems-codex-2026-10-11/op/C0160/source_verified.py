import pathlib, requests, pymupdf, json, subprocess
R=pathlib.Path(__file__).parent
url='https://arxiv.org/pdf/math/0612812v1'
r=requests.get(url,timeout=40)
print('survey',r.status_code,len(r.content),flush=True)
(R/'survey.pdf').write_bytes(r.content)
if r.content.startswith(b'%PDF'):
 d=pymupdf.open(R/'survey.pdf')
 (R/'survey.txt').write_text('\n'.join(p.get_text() for p in d),encoding='utf-8')
 for i,p in enumerate(d):
  t=p.get_text()
  if any(w in t.lower() for w in ['monotonicity','quasi-transitive','nonunimodular','harris','kesten','theorem 3.1']): print('PDF PAGE',i+1,'\n'+t,flush=True)
paths=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True,encoding='utf-8',timeout=120).stdout.splitlines()
relevant=[p for p in paths if 'C0160' in p]
print('git paths',relevant,flush=True)
for p in relevant[:5]:
 rr=subprocess.run(['git','-C','~/math-open-problems','show','origin/master:'+p],capture_output=True,text=True,encoding='utf-8',timeout=60)
 print('git show',p,rr.stdout[:15000],flush=True)
 (R/('prior_git_'+str(relevant.index(p))+'.txt')).write_text(rr.stdout,encoding='utf-8')
