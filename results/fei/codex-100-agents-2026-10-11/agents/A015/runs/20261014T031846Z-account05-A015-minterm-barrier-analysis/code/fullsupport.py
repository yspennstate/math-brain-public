from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import factorial
import json,time
BASE=Path(__file__).resolve().parents[1]
old=BASE.parents[0]/'20261014T001450Z-account05-A015-minterm-barrier-analysis/code/check.py'
helper={'__file__':str(old),'__name__':'a015_prior_readonly'}
exec(compile(old.read_text(encoding='utf-8'),str(old),'exec'),helper)
start=time.perf_counter(); checks=0; rows=[]
def ck(v):
 global checks
 checks+=1
 assert v,checks
def compositions(s,k):
 if k==1: yield(s,)
 else:
  for j in range(1,s-k+2):
   for rest in compositions(s-j,k-1): yield(j,)+rest
def rising(s,d):
 v=1
 for j in range(d): v*=s+j
 return v
for m in [1,2,3]:
 N=1<<(m-1); pi=F(1,1<<m)
 for s in range(1,m+1):
  raw={}; count=0
  for assignment in product(range(N),repeat=s):
   owned=[set() for _ in range(N)]
   for j,l in enumerate(assignment): owned[l].add(j)
   k=sum(bool(a) for a in owned)
   trace,can,moment=helper['review']([set(range(m)) for _ in range(N)],owned,[pi]*N)
   ck(moment==pi*rising(s,k-1))
   sizes=tuple(len(a) for a in owned if a)
   base=F(1)
   for size in sizes: base*=F(size,s)**size
   # Common rank/pi cancel; key retains congestion base to power gamma.
   key=(k,base); raw[key]=raw.get(key,F(0))+moment/pi/F(N)**k
   count+=1
  formula={}
  for k in range(1,min(N,s)+1):
   choose=factorial(N)//(factorial(k)*factorial(N-k))
   for sizes in compositions(s,k):
    multi=factorial(s); base=F(1)
    for size in sizes: multi//=factorial(size); base*=F(size,s)**size
    key=(k,base)
    formula[key]=formula.get(key,F(0))+F(choose*multi*rising(s,k-1),N**k)
  ck(raw==formula)
  rows.append({'m':m,'N':N,'s':s,'assignments':count,'symbolic_weights':[{'k':k,'congestion_base':str(base),'coefficient':str(v)} for (k,base),v in sorted(raw.items())]})
  (BASE/'out/FULLSUPPORT_CHECKPOINT.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
ck(sum(x['assignments'] for x in rows)==91)
out={'status':'PASS','own_helper_assertions':helper['CHECKS'],'new_assertions':checks,'assertions':checks+helper['CHECKS'],'cases':6,'assignments':91,'seconds':time.perf_counter()-start,'rows':rows}
(BASE/'out/FULLSUPPORT_CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','assertions','assignments','seconds']}))
