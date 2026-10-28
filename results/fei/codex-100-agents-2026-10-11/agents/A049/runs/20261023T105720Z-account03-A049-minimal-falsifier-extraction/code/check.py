"""Exact truth-table replay; no numerical logarithms or external libraries."""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json,time,hashlib,sys
RUN=Path(__file__).resolve().parents[1]
START=time.perf_counter();checks=0
def ck(v):
 global checks
 assert v
 checks+=1
 if time.perf_counter()-START>55:raise TimeoutError('55 second cap')
def spectrum(t):
 n=len(t)
 a=[F(sum(t[x]*(-1)**((x&s).bit_count()) for x in range(n)),n) for s in range(n)]
 return {s:x*x for s,x in enumerate(a) if x}
def restrict(t,j,b):
 return tuple(t[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(t)//2))
def freshcore(t,a):
 p=spectrum(t);ess=sum(1<<j for j in range(len(t).bit_length()-1) if restrict(t,j,0)!=restrict(t,j,1))
 if len(p)==1:return p.copy()
 q={s:((1-a)*v if s else v) for s,v in p.items()}
 q[ess]=q.get(ess,F())+a*(1-p.get(0,F()))
 ck(sum(q.values())==1);return q
def activate(t,s):return tuple(s if x%2==0 else t[x//2] for x in range(2*len(t)))
def lift(t,s,a):
 p=spectrum(activate(t,s));q={u:v for u,v in p.items() if u<2}
 for u,v in freshcore(t,a).items():
  if u:q[2*u]=q[2*u+1]=v/4
 ck(sum(q.values())==1);return q
def transport(t,q,j):
 p=spectrum(t);pe=defaultdict(F);qe=defaultdict(F)
 erase=lambda u:(u&((1<<j)-1))|((u>>(j+1))<<j)
 for u,v in p.items():pe[erase(u)]+=v
 for u,v in q.items():qe[erase(u)]+=v
 children=[];zs=[]
 for b in (0,1):
  tb=restrict(t,j,b);pb=spectrum(tb)
  w={u:v*(pb.get(u,F())/(2*pe[u]) if pe[u] else F(1,2)) for u,v in qe.items()}
  z=sum(w.values());ck(z>0);qb={u:v/z for u,v in w.items() if v}
  ck(sum(qb.values())==1);ck(all(qb.get(u,0)>0 for u in pb))
  children.append((tb,qb));zs.append(z)
 ck(sum(zs)==1);return children,zs
def exact_power_price(children,fresh):
 # 32 times paired new-minus-old KL is an integer-weighted log.
 # Evaluate its exponential as a rational; sign is a single integer comparison.
 k=F(1)
 for (t,old),new in zip(children,fresh):
  p=spectrum(t)
  for u,v in p.items():
   power=16*v;ck(power.denominator==1)
   k*=(old[u]/new[u])**int(power)
 return k
def formula(a):
 return (1-a/26)**13*(1-a/10)**5*(1+a/2)**10/((1+2*a)**2*(1-(14*a/65)**2)**16)
def encodeq(q):return {str(k):str(v) for k,v in q.items()}
g=(1,-1,-1,1,-1,1,1,1)
ck(spectrum(g)=={0:F(1,16),1:F(1,16),2:F(1,16),3:F(1,16),4:F(1,16),5:F(1,16),6:F(1,16),7:F(9,16)})
domain=[F(1,6)] if '--pilot' in sys.argv else sorted(set([F(j,100) for j in range(1,100)]+[F(1,6)]))
rows=[];witness=[]
for a in domain:
 # Pointwise checks supplement the analytic interval proof, never replace it.
 d1=10/(2+a)-4/(1+2*a)-13/(26-a)-5/(10-a)
 ck(d1==a*((11-2*a)/((2+a)*(1+2*a))-F(1,2)*(1/(26-a)+1/(10-a))))
 ck(d1>=F(208,225)*a)
 derivative=d1+6272*a/(4225-196*a*a)
 ck(derivative>=F(208,225)*a)
 for sign in (1,-1):
  t=activate(g,sign);q=lift(g,sign,a)
  children,zs=transport(t,q,1)
  fs=[lift(restrict(g,0,b),sign,a) for b in (0,1)]
  k=exact_power_price(children,fs)
  ck(k==formula(a));ck(k>1)
  ck(set(q)==set(spectrum(t)))
  for (tb,old),new in zip(children,fs):ck(set(old)==set(new)==set(spectrum(tb)))
  rows.append({'alpha':str(a),'sign':sign,'K_gt_1':True})
  if a==F(1,6):witness.append({'alpha':str(a),'sign':sign,'truth_table':list(t),'old_reference':encodeq(q),'reference_outcomes':[str(z) for z in zs],'children':[{'truth_table':list(tb),'inherited_reference':encodeq(old),'fresh_reference':encodeq(new)} for (tb,old),new in zip(children,fs)],'K_numerator':str(k.numerator),'K_denominator':str(k.denominator)})
result={'status':'PASS','checks':checks,'cases':len(rows),'seconds':time.perf_counter()-START,'arithmetic':'Fraction; exact rational exponential of 32*sigma','rows':rows,'witness':witness,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
name='PILOT.json' if '--pilot' in sys.argv else 'CHECK.json'
(RUN/'out'/name).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','checks','cases','seconds']}))
