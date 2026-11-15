from pathlib import Path
from fractions import Fraction as F
from datetime import datetime
import json,hashlib,subprocess,time,itertools
H=Path(__file__).resolve().parent;W=Path('~/brain_workers/w682')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert not (H/'T067_DEGREE6_INDEPENDENT_NUMERIC_RECEIPT.json').exists()
build=json.loads((H/'T067_INDEPENDENT_FUSION_BUILD_RECEIPT.json').read_bytes());assert sha(H/'t067_independent_fusion.cpp')==build['source_sha256'] and sha(H/'t067_independent_fusion.exe')==build['exe_sha256']
def native(N,steps):
 p=H/f'T067_INDEPENDENT_FUSION_N{N}.jsonl';assert not p.exists(),'Inspect existing output before replay'
 start=time.monotonic()
 with p.open('wb') as out:r=subprocess.run([str(H/'t067_independent_fusion.exe'),str(N),str(steps)],cwd=H,stdout=out,stderr=subprocess.STDOUT,timeout=180,creationflags=subprocess.CREATE_NO_WINDOW|subprocess.BELOW_NORMAL_PRIORITY_CLASS)
 assert r.returncode==0,f'Native failure; inspect {p}'
 rows=[json.loads(x) for x in p.read_bytes().splitlines()];assert len(rows)==steps+1
 print('Native completed',N,steps,'seconds',round(time.monotonic()-start,3),flush=True)
 return rows
def keys(N):return [(a,b,N-a-b) for a in range(N+1) for b in range(N-a+1) if a>=b>=N-a-b]
small=native(6,4);N=6;ks=keys(N);S=2**32;pure=tuple(sorted((N,0,0)))
def split(p):
 coords=[x*N for x in p];base=[int(x) for x in coords];rem=[x-int(x) for x in coords];deficit=N-sum(base);out=[]
 if deficit==0:return [(tuple(sorted(base)),F(1))]
 assert deficit in [1,2]
 for i in range(3):
  q=base.copy()
  for j in range(3):q[j]+=int(j==i) if deficit==1 else int(j!=i)
  weight=rem[i] if deficit==1 else 1-rem[i]
  if weight:out.append((tuple(sorted(q)),weight))
 return out
def upgrade(raw):
 assert sum(raw.values())==1
 out={k:int(v*S) for k,v in raw.items()};out[pure]=out.get(pure,0)+S-sum(out.values());return out
def edge(m):
 raw={}
 for k,v in m.items():
  p=[F(1,3)+F(89,218)*(F(x,N)-F(1,3)) for x in k]
  for q,w in split(p):raw[q]=raw.get(q,F(0))+F(v,S)*w
 return upgrade(raw)
def fuse(x,y):
 raw={}
 # Average BOTH independently permuted inputs; unlike native's fixed left.
 for k,mass in x.items():
  pp=set(itertools.permutations(k))
  for h,mass2 in y.items():
   rr=set(itertools.permutations(h))
   for p in pp:
    for r in rr:
     z=[F(p[i]*r[i],N*N) for i in range(3)];dot=sum(z)
     if not dot:continue
     probability=F(mass*mass2,S*S*len(pp)*len(rr))*3*dot
     for q,w in split([a/dot for a in z]):raw[q]=raw.get(q,F(0))+probability*w
 return upgrade(raw)
m={pure:S}
for depth in range(1,5):
 one=edge(m);two=fuse(one,one);four=fuse(two,two);m=fuse(two,four)
 got={tuple(sorted(k)):int(v) for k,v in zip(ks,small[depth]['masses'])}
 assert all(got.get(k,0)==m.get(k,0) for k in set(got)|set(m)),depth
full=native(96,26);subject=W/'checks/balanced_bp_fast_d6_N96_89-218.json'
assert sha(subject)=='2b0976cced31beda5ca04785b1e15ba8b1e6eca2fb2067e559704b7293303f34'
r=json.loads(subject.read_bytes());assert full[0]['orbits']==817 and full[0]['ordered_rows']==667489
for i,row in enumerate(full[1:]):
 assert row['depth']==i+1 and F(row['signal_numerator'],row['signal_denominator'])==F(r['rows'][i]['second_moment_upper']),i+1
 assert sum(row['masses'])==S
got={tuple(sorted(k)):int(v) for k,v in zip(keys(96),full[-1]['masses'])};expected={tuple(k):int(v) for k,v in zip(r['orbit_keys'],r['final_integer_masses'])};assert got==expected
signal=F(full[-1]['signal_numerator'],full[-1]['signal_denominator']);assert signal==F(942948951491,19791209299968)<F(217,4500)
receipt={'at':datetime.now().astimezone().isoformat(),'status':'PASS fresh independent full native26depth replay and4depth all-orientation Fraction control; analytic proof review separate, no admission','signal':str(signal),'radius':str(F(217,4500)),'gap':str(F(217,4500)-signal),'depths_exact':26,'final_masses_exact':817,'ordered_rows_built':667489,'code_sha256':sha(H/'t067_independent_fusion.cpp'),'driver_sha256':sha(Path(__file__)),'native_outputs':{f'T067_INDEPENDENT_FUSION_N{N}.jsonl':sha(H/f'T067_INDEPENDENT_FUSION_N{N}.jsonl') for N in [6,96]},'subject_sha256':sha(subject),'arithmetic':'fresh direct Bayes coefficients, checked 128-bit limbs, exact floor; no imported solver table/cache'}
(H/'T067_DEGREE6_INDEPENDENT_NUMERIC_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(json.dumps(receipt))
