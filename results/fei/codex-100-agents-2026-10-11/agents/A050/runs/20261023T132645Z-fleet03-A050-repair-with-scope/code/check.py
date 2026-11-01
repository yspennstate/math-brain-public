from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
from itertools import permutations
import json,sys,time,hashlib
R=Path(__file__).resolve().parents[1]
START=time.perf_counter(); C=0; N=0; D=0; P='--pilot' in sys.argv
def ck(x):
 global C
 assert x
 C+=1
 if time.perf_counter()-START>55: raise RuntimeError('frozen 55-second watchdog')
@lru_cache(None)
def spectrum(t,co):
 n=len(t); p={}
 for s in range(n):
  a=sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t))
  if a: p[sum(1<<i for j,i in enumerate(co) if s>>j&1)]=F(a*a,n*n)
 return p
def restrict(t,j,b):
 return tuple(t[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(t)//2))
def marg(p,mask):
 q={}
 for s,w in p.items():q[s&mask]=q.get(s&mask,F(0))+w
 return q
def mixture(p,b,atoms):
 q={s:b*w for s,w in p.items()}
 for s,w in atoms:q[s]=q.get(s,F(0))+w
 return {s:w for s,w in q.items() if w}
def visit(t,co,b,atoms,q,order,pathprob=F(1),refprob=F(1),broot=F(6,7)):
 global N,D
 p=spectrum(t,co); ck(q==mixture(p,b,atoms));ck(sum(q.values())==1)
 ck(b==broot*pathprob/refprob);ck(b>0 and b<=1)
 ck(all(q[s]>=b*w for s,w in p.items()))
 ck(all(p.get(s,F(0))>0 for s,w in atoms if w))
 if not order:return [(pathprob,refprob,b)]
 N+=1;i=order[0];j=co.index(i);cn=tuple(z for z in co if z!=i);mask=sum(1<<z for z in cn)
 pe=marg(p,mask);qe=marg(q,mask)
 tt=[restrict(t,j,k) for k in (0,1)];pp=[spectrum(z,cn) for z in tt]
 ck(all(2*w==pp[0].get(s,F(0))+pp[1].get(s,F(0)) for s,w in pe.items()))
 out=[];rr=[]
 for k in (0,1):
  kernel={s:pp[k].get(s,F(0))/(2*w) for s,w in pe.items()}
  joint={s:w*kernel[s] for s,w in qe.items()};r=sum(joint.values());rr.append(r)
  at=[(s&mask,w*kernel[s&mask]/r) for s,w in atoms if w*kernel[s&mask]]
  bb=b/(2*r);qq={s:w/r for s,w in joint.items() if w}
  ck(r>=b/2);ck(bb+sum(w for s,w in at)==1)
  ck(qq==mixture(pp[k],bb,at));ck(len(at)<=len(atoms))
  out+=visit(tt[k],cn,bb,at,qq,order[1:],pathprob/2,refprob*r,broot)
 ck(sum(rr)==1)
 return out
def run(t,order):
 p=spectrum(t,tuple(range(len(t).bit_length()-1)));a=F(1,7);u=p.get(0,F(0))
 witness=max((s for s in p if s),default=0)
 atoms=[(0,a*u),(witness,a*(1-u))];atoms=[(s,w) for s,w in atoms if w]
 b=1-a;q=mixture(p,b,atoms)
 leaves=visit(t,tuple(range(len(t).bit_length()-1)),b,atoms,q,order,broot=b)
 ck(sum(w for w,_,_ in leaves)==1);ck(sum(r for _,r,_ in leaves)==1)
 return leaves
cases=0
domain=range(8) if P else range(256)
for f in domain:
 t=tuple(1 if f>>x&1 else -1 for x in range(8))
 for order in ((0,1,2),) if P else permutations(range(3)):
  run(t,order);cases+=1
# Independent A047 stable-mask witness, all orders not needed: rare query only.
rare=[]
for r in ((4,) if P else (4,5,6)):
 delta=F(1,1<<r)
 def h(x):return (-1 if x>>1&1 else 1) if not x&1 else (-1 if x>>2&1 else 1)
 t=tuple((-h(x>>1) if (x&1==0 and x>>1==1) or (x&1==1 and x>>1 in (1,4,5)) else h(x>>1)) for x in range(1<<(r+1)))
 co=tuple(range(r+1));p=spectrum(t,co);alpha=F(1,6);u=4*delta*delta
 atoms=[(0,alpha*u),((1<<(r+1))-1,alpha*(1-u))];q=mixture(p,1-alpha,atoms)
 # The transported witness stays the full ORIGINAL residual mask; weights adapt.
 visit(t,co,1-alpha,atoms,q,(0,),broot=1-alpha)
 E=20*delta*delta;c=alpha*(1-u);eta=4*c/5
 pe=marg(p,((1<<(r+1))-1)^1);qe=marg(q,((1<<(r+1))-1)^1)
 rr=[]
 for k in (0,1):
  pk=spectrum(restrict(t,0,k),co[1:]);rout=sum(w*pk.get(s,F(0))/(2*pe[s]) for s,w in qe.items());rr.append(rout)
 ck(rr==[(1-eta)/2,(1+eta)/2]);ck(eta>=F(21,160))
 # -log2(1-eta^2)/2 > eta^2/2 >1/128, using ln2<1.
 ck(eta*eta/2>F(1,128))
 rare.append({'r':r,'outcomes':list(map(str,rr)),'eta':str(eta),'fresh_reset_lower':'>1/128','transport_conversion':'0'})
result={'status':'PASS','function_order_cases':cases,'physical_query_nodes':N,'assertions':C,'rare_witnesses':rare,'runtime_seconds':time.perf_counter()-START,'arithmetic':'Fraction; direct Walsh sums, exact pivots checked separately below','automatic_escalation':False}
(R/'out'/('PILOT.json' if P else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
