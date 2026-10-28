from pathlib import Path
from collections import Counter
from math import gcd
import itertools,json,time,hashlib,sys
R=Path(__file__).resolve().parents[1]
E={0,1,2,4};free=[x for x in range(16) if x not in E]
def walsh(a):
 a=list(a);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):u,v=a[k],a[k+h];a[k],a[k+h]=u+v,u-v
  h*=2
 return a
def ratio(hist):
 p=q=1
 for t,u,c in hist:
  if not t or not u:continue
  p*=pow(t+u,(t+u)*c);q*=pow(t,t*c)*pow(u,u*c)
 return p,q
start=time.perf_counter();pilot='--pilot' in sys.argv
orbits=json.loads((R/'out/orbits.json').read_text(encoding='utf-8'))['orbits']
d=[v//2 for v in walsh([int(x in E) for x in range(16)])]
assert sum(x*x for x in d)*2==32
cache={};count=checks=bad=0;best=None;first=None;summary=[];digest=hashlib.sha256()
for orbit in orbits:
 rep=orbit['representative'];outside=[1-2*(rep>>x&1) for x in range(16)];wo=[x//2 for x in walsh(outside)];localbad=0;localbest=None
 for code in range(32 if pilot else 4096):
  inside=[1]*16
  for j,x in enumerate(free):inside[x]=1-2*(code>>j&1)
  wi=[x//2 for x in walsh(inside)]
  pairs=[(wi[k]-d[k]+sign*wo[k],d[k]) for k in range(16) for sign in [-1,1]]
  assert sum(a*a for a,b in pairs)==224;checks+=1
  hist=tuple((t,u,c) for (t,u),c in sorted(Counter((a*a,b*b) for a,b in pairs if a and b).items()))
  if hist not in cache:
   p,q=ratio(hist);cache[hist]=(p,q,p<=q<<128)
  p,q,ok=cache[hist]
  if not ok:
   bad+=1;localbad+=1
   if first is None:first={'outside_mask':rep,'inside_code':code,'inside':inside,'outside':outside,'P':str(p),'Q':str(q),'pairs':pairs}
  if best is None or p*best[1]>best[0]*q:best=(p,q,rep,code,hist)
  if localbest is None or p*localbest[1]>localbest[0]*q:localbest=(p,q,code)
  digest.update(rep.to_bytes(2,'little')+code.to_bytes(2,'little')+bytes([ok]));count+=1
 summary.append({'representative':rep,'orbit_size':orbit['size'],'cases':32 if pilot else 4096,'bad':localbad,'max_inside_code':localbest[2],'P':str(localbest[0]),'Q':str(localbest[1])})
res={'status':'PASS' if not bad else 'ACTUAL_BOOLEAN_OBSTRUCTION','pilot':pilot,'cases':count,'assertions':checks,'histogram_classes':len(cache),'bad':bad,'summary':summary,'first_bad':first,'maximum':{'P':str(best[0]),'Q':str(best[1]),'outside_mask':best[2],'inside_code':best[3],'histogram':best[4]},'coverage_sha256':digest.hexdigest(),'elapsed_seconds':time.perf_counter()-start}
(R/'out'/('tetra_pilot.json' if pilot else 'tetra_certificate.json')).write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in res.items() if k not in ['maximum','first_bad','summary']}))
