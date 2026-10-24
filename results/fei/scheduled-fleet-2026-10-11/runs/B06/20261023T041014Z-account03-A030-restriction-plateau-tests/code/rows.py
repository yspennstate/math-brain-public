from itertools import product
from pathlib import Path
import time,json,hashlib
RUN=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=cases=offtrue=0
def ck(v):
 global checks
 checks+=1;assert v,checks
def direct(t):
 return tuple(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(len(t)))
groups=[]
for L,D in ((2,4),(3,2)):
 functions=list(product((-1,1),repeat=D));ws=[direct(f) for f in functions];count=0
 for label in product(range(L),repeat=4):
  cw=[direct(tuple(int(l==j) for l in label)) for j in range(L)]
  for ids in product(range(len(functions)),repeat=L):
   bs=[ws[i] for i in ids];truth=tuple(functions[ids[label[y]]][x] for x in range(D) for y in range(4));actual=direct(truth)
   predicted=tuple(sum(cw[j][u]*bs[j][t] for j in range(L)) for t in range(D) for u in range(4))
   ck(actual==predicted)
   p=tuple(a*a for a in actual)
   q=tuple(sum(cw[j][u]**2*bs[j][t]**2 for j in range(L)) for t in range(D) for u in range(4))
   ck(sum(p)==sum(q)==(4*D)**2)
   for t in range(D):
    ck(sum(p[4*t:4*t+4])==sum(q[4*t:4*t+4]))
    overlap=sum(bs[j][t]!=0 for j in range(L))
    for u in range(4):ck(p[4*t+u]<=overlap*q[4*t+u])
   if any(a==0 and b>0 for a,b in zip(p,q)):offtrue+=1
   cases+=1;count+=1
   assert time.perf_counter()-start<55,'frozen runtime'
 groups.append({'labels':L,'shared_data_points':D,'cases':count})
ck(cases==9280);ck(offtrue>0)
out={'status':'PASS','cases':cases,'checks':checks,'groups':groups,'cases_with_required_off_true_reference_mass':offtrue,'arithmetic':'integer character sums, no numerical logs','elapsed_seconds':time.perf_counter()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'finite certificate of algebra/dominance only; universal KL conclusion supplied by PROOF.md'}
(RUN/'out/ROWS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
