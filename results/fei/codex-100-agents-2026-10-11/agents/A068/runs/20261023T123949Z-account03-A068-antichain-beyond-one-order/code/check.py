import sys,json,time,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
R=Path(__file__).resolve().parents[1]
START=time.monotonic(); N=0
def ck(v,msg):
 global N
 N+=1
 if not v: raise AssertionError(msg)
 if time.monotonic()-START>55: raise TimeoutError('frozen 55 second limit')
@lru_cache(None)
def factors(v):
 d=2; out={}
 while d*d<=v:
  while v%d==0: out[d]=out.get(d,0)+1; v//=d
  d+=1
 if v>1: out[v]=out.get(v,0)+1
 return out
def add(*terms):
 z={}
 for c,e in terms:
  for p,v in e.items(): z[p]=z.get(p,F(0))+c*v
 return {p:v for p,v in z.items() if v}
def lg(v):
 v=F(v); assert v>0
 return add((1,factors(v.numerator)),(-1,factors(v.denominator)))
def ce(p,q):
 z={}
 for a,b in zip(p,q):
  if a:
   ck(b>0,'complete support'); z=add((1,z),(-a,lg(b)))
 return z
def kl(p,q): return add((1,ce(p,q)),(-1,ce(p,p)))
def fwht(truth):
 a=list(truth); h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for i in range(j,j+h):
    x,y=a[i],a[i+h]; a[i],a[i+h]=x+y,x-y
  h*=2
 return [F(x,len(a)) for x in a]
def spectrum(truth): return [v*v for v in fwht(truth)]
def infl(p): return sum((v*s.bit_count() for s,v in enumerate(p)),F(0))
def edge(truth,n):
 return sum((F(sum(truth[x]!=truth[x^(1<<i)] for x in range(len(truth))),len(truth)) for i in range(n)),F(0))
def groups(n,blocks,erased=0):
 masks=[]; pos=0
 for b in blocks: masks.append(((1<<b)-1)<<pos); pos+=b
 d={}
 for s in range(1<<n):
  if s&erased: continue
  key=tuple(bool(s&m) for m in masks)
  d.setdefault(key,[]).append(s)
 return list(d.values())
def average(q,oo):
 z=[F(0)]*len(q)
 for o in oo:
  mass=sum((q[s] for s in o),F(0))
  for s in o:z[s]=mass/len(o)
 return z
def marginal(q,e):
 z=[F(0)]*len(q)
 for s,v in enumerate(q):z[s&~e]+=v
 return z
def main(pilot):
 counts={'invoice_cases':0,'physical_marginals':0,'character_guards':0,'paid_roots':0,'paid_terminals':0}
 for code in range(4 if pilot else 256):
  truth=[1 if code>>x&1 else -1 for x in range(8)]; p=spectrum(truth)
  ck(infl(p)==edge(truth,3),'independent physical influence')
  qs=[[ (v+F(1,8))/2 for v in p],[(v+(s==0))/2 for s,v in enumerate(p)],[F(s+1,36) for s in range(8)]]
  for q in qs:
   ck(sum(q)==1,'source normalized')
   for blocks in [[1,1,1],[2,1],[3]]:
    oo=groups(3,blocks); qb=average(q,oo); phi={}; mismatch={}; rankbill=F(0)
    ck(sum(qb)==1,'averaged source normalized')
    for o in oo:
     a=sum((p[s] for s in o),F(0)); b=sum((q[s] for s in o),F(0))
     ck(sum((qb[s] for s in o),F(0))==b,'original orbit mass retained')
     minrank=min(s.bit_count() for s in o)
     ck(len(o)<=2**(max(blocks)*minrank),'rank orbit cardinal bound')
     rankbill+=a*max(blocks)*minrank
     if a:
      pc=[p[s]/a for s in o]; qc=[q[s]/b for s in o]; u=[F(1,len(o))]*len(o)
      phi=add((1,phi),(a,kl(pc,u))); mismatch=add((1,mismatch),(a,kl(pc,qc)))
    ck(rankbill<=max(blocks)*infl(p),'rank bill paid by influence')
    ck(add((1,ce(p,qb)),(-1,ce(p,q)),(-1,phi),(1,mismatch))=={},'exact noninvariant conversion invoice')
    for e in range(8):
     qm=marginal(qb,e); residual=groups(3,blocks,e)
     ck(average(qm,residual)==qm,'all residual physical source shapes invariant')
     ck(sum(qm)==1,'full marginal normalized')
     counts['physical_marginals']+=1
    counts['invoice_cases']+=1
 for n in range(1,9):
  p=[F(0)]*(1<<n); p[1]=1; q=p[:]; qb=average(q,groups(n,[n])); M=(1<<n)-1
  ck(ce(p,qb)==lg(M),'sharp actual dictator guard')
  ck(infl(p)==1 and ce(p,q)=={},'guard original complete source cost zero')
  if n>=2:ck(M>2**(n-1),'unbounded orbit tariff guard')
  counts['character_guards']+=1
 h=[1 if sum(1 if not x>>i&1 else -1 for i in range(5))>0 else -1 for x in range(32)]
 ph=spectrum(h)
 ck(sum(v==F(9,64) for v in ph)==6 and sum(v==F(1,64) for v in ph)==10,'actual Maj5 full spectrum')
 ck(ph[0]==0 and infl(ph)==F(15,8),'Maj5 balance/influence')
 ck(ph[1]>0 and ph[3]==0,'actual GL noninvariance')
 for code in ([0,1] if pilot else range(16)):
  gt=[1 if code>>x&1 else -1 for x in range(4)]; pg=spectrum(gt); ig=infl(pg); cg=ce(pg,pg)
  truth=[(-1 if a&1 else 1)*(-1 if a&2 else 1)*h[(a>>2)&31]*gt[a>>7] for a in range(512)]
  pf=spectrum(truth)
  ck(infl(pf)==edge(truth,9)==ig+F(31,8),'full actual root influence via edges')
  expected=[F(0)]*512
  for s in range(32):
   for z in range(4):expected[3+(s<<2)+(z<<7)]=ph[s]*pg[z]
  ck(pf==expected,'full physical product spectrum')
  for K in [4,5,8]:
   eps=F(1,2**(3*K)); q=[F(0)]+[eps]*31; q[1]=1-30*eps; qb=average(q,groups(5,[5]))
   ck(qb==[F(0)]+[F(1,31)]*31,'actual original source orbit return')
   c=ce(ph,q)
   ck(c==add((F(165*K,64),lg(2)),(-F(9,64),lg(1-30*eps))),'exact old full cost')
   ck(ce(ph,qb)==lg(31),'NONINVARIANT target cost retains entropy deficit')
   ck(F(1,2)<q[1]<1,'rational source-cost bound premise')
   ck(F(165*K,64)>F(15*K,8)-F(1,4),'literal old account strictly insolvent lower bound')
   ck(F(19*K-25,64)>=F(51,64),'real prefix already paid upper bound')
   ck(31<32 and F(15*K,8)-F(21,4)>=F(9,4),'same original final reserve >9/4')
   A=K*(ig+F(31,8)); tau=add((K*ig+F(1,4),lg(2)),(-1,cg)); final=add((F(15*K,8)-F(1,4),lg(2)),(-1,lg(31)))
   ck(add((A-2*K,lg(2)),(-1,cg),(-1,lg(31)),(-1,tau),(-1,final))=={},'same owner, old tau, both complete terminal bills')
   for t in [-1,1]:
    child=[t*(-1 if a&1 else 1)*h[(a>>1)&31]*gt[a>>6] for a in range(256)]
    pc=spectrum(child)
    ck(infl(pc)==edge(child,8)==ig+F(23,8),'actual prefix child')
    for x in [-1,1]:
     term=[t*x*h[a&31]*gt[a>>5] for a in range(128)]; pt=spectrum(term)
     ck(infl(pt)==edge(term,7)==ig+F(15,8),'actual BOTH terminal influences')
     old=[q[s]*pg[z] for z in range(4) for s in range(32)]
     new=[qb[s]*pg[z] for z in range(4) for s in range(32)]
     ck(ce(pt,old)==add((1,cg),(1,c)),'both FULL original terminal costs')
     ck(ce(pt,new)==add((1,cg),(1,lg(31))),'both FULL returned terminal costs')
     ck(pt[0]==0,'no hidden vacuum credit')
     counts['paid_terminals']+=1
   counts['paid_roots']+=1
 out={'status':'PASS','pilot':pilot,'assertions':N,'counts':counts,'seconds':time.monotonic()-START,'arithmetic':'Fraction and exact prime-log coefficients; signs by proved rational bounds','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (R/'out').mkdir(exist_ok=True)
 (R/'out'/('pilot.json' if pilot else 'check.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(out))
if __name__=='__main__':main('--pilot' in sys.argv)
