"""Independent direct DFT. No production imports or prime-log expression code."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]; checks=0
def ck(x):
 global checks
 checks+=1; assert x,checks
@lru_cache(None)
def log(x):
 k=x.numerator.bit_length()-x.denominator.bit_length(); y=x/F(2)**k
 if y<1: y*=2; k-=1
 def ln(y):
  z=(y-1)/(y+1); term=z; s=F(0)
  for j in range(48): s+=2*term/(2*j+1); term*=z*z
  return s,s+2*term/(97*(1-z*z))
 a,b=ln(y); c,d=ln(F(2)); return k+a/d,k+b/c
def sp(f):
 n=len(f); a=[sum(v*(-1 if (j&s).bit_count()%2 else 1) for j,v in enumerate(f)) for s in range(n)]
 return [F(v*v,n*n) for v in a]
def CE(P,Q):
 l=u=F(0)
 for p,q in zip(P,Q):
  if p:
   ck(q>0); a,b=log(1/q); l+=p*a; u+=p*b
 return l,u
def inf(f,i): return F(sum(v!=f[j^(1<<i)] for j,v in enumerate(f)),len(f))
def run():
 start=time.perf_counter(); rows=[]
 for v in (0,1,3,63):
  for A in ((0,0,0,1),(1,1,1,1)):
   alpha=F(sum(A),4); f=[]
   for z in range(4):
    for x in range(64):
     seed=(-1 if x%8==0 else 1)*(-1 if x//8==0 else 1)
     f.append(seed*(-1 if x==v and A[z] else 1))
   P=sp(f); R=[sum(P[z*64:(z+1)*64]) for z in range(4)]
   q=[F(9 if s%8==0 else 1,16)*F(9 if s//8==0 else 1,16) for s in range(64)]
   C0=CE(P,[q[s]*R[z] for z in range(4) for s in range(64)])
   cs=[]; fs=[]
   for b in (0,1):
    ff=[a for j,a in enumerate(f) if j%2==b]; fs.append(ff)
    qb=[(F(1,4) if b==0 else F(13 if s%4==0 else 1,16))*F(9 if s//4==0 else 1,16) for s in range(32)]
    ck(sum(qb)==1)
    cs.append(CE(sp(ff),[qb[s]*R[z] for z in range(4) for s in range(32)]))
   C1=((cs[0][0]+cs[1][0])/2,(cs[0][1]+cs[1][1])/2)
   drop=(C0[0]-C1[1],C0[1]-C1[0]); d=inf(f,0)
   ck(4*d-drop[0]<F(1,8))
   Id=sum((inf(f,i) for i in range(6)),F(0))
   Ic=sum((sum((inf(ff,i) for i in range(5)),F(0)) for ff in fs),F(0))/2
   ck(Ic==Id-d)
   Ha=CE(sp([1-2*a for a in A]),sp([1-2*a for a in A]))
   Llo=Ha[0]/64
   ck(4*Ic+Llo-C1[1]-F(2,64)>=F(22,64))
   rows.append({'v':v,'alpha':str(alpha),'query_d':str(d),'reference_loss_upper':str(4*d-drop[0])})
   if time.perf_counter()-start>59: raise RuntimeError('frozen60-second cap')
 obj={'status':'PASS','cases':len(rows),'assertions':checks,'seconds':time.perf_counter()-start,'rows':rows}
 (ROOT/'out/REPLAY.json').write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8',newline='')
 print(json.dumps({k:v for k,v in obj.items() if k!='rows'}))
if __name__=='__main__': run()
