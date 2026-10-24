from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import hashlib,json,time,sys

RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; OUT.mkdir(exist_ok=True)
START=time.perf_counter(); checks=0
def save(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def ck(v):
 global checks
 checks+=1
 assert v,checks
 if time.perf_counter()-START>55: raise TimeoutError('55-second frozen compute cap')
def ln_series(q):
 z=(q-1)/(q+1); term=z; val=F(0)
 for k in range(22): val+=2*term/(2*k+1);term*=z*z
 return val,val+2*term/(45*(1-z*z))
L2=ln_series(F(2))
@lru_cache(None)
def log(q):
 q=F(q);assert q>0
 k=q.numerator.bit_length()-q.denominator.bit_length();z=q/F(2)**k
 if z<1:k-=1;z*=2
 assert 1<=z<2
 lo,hi=ln_series(z);return lo/L2[1]+k,hi/L2[0]+k
def add(*xs):return sum((x[0] for x in xs),F(0)),sum((x[1] for x in xs),F(0))
def mul(a,x):return (a*x[0],a*x[1]) if a>=0 else (a*x[1],a*x[0])
def sub(x,y):return add(x,mul(-1,y))
def CE(P,Q):
 assert len(P)==len(Q)
 return add(*(mul(-p,log(q)) for p,q in zip(P,Q) if p))
def spec(v):
 # Direct character sums, deliberately not the source's butterfly transform.
 N=len(v)
 return [F(sum(y*(-1 if (x&T).bit_count()%2 else 1) for x,y in enumerate(v)),N)**2 for T in range(N)]
def vals(a,b,r):return [1-2*int(x&((1<<a)-1)==0)+2*int(x==0) for x in range(1<<(a+b+r))]
def src(a,b):return [1-2*int(x&((1<<a)-1)==0) for x in range(1<<(a+b))]
def marginal(P,j):
 Q=[F(0)]*(len(P)//2)
 for x,p in enumerate(P):Q[(x&((1<<j)-1))|((x>>(j+1))<<j)]+=p
 return Q
def child(v,j,t):return [v[(x&((1<<j)-1))|((x>>j)<<(j+1))|(t<<j)] for x in range(len(v)//2)]
def cal(R,P):
 if P[0]==1:return [F(1)]+[F(0)]*(len(P)-1)
 return [P[0]]+[(1-P[0])*x/(1-R[0]) for x in R[1:]]
def floor(a,b,r,R):
 n=a+b;s=F(1,1<<a);t=F(1,1<<n);e=F(2,1<<(n+r));mu=1-2*s
 v=vals(a,b,r);P=spec(v);M=[sum(P[T+(U<<n)] for U in range(1<<r)) for T in range(1<<n)]
 V=[(1-e/s)*q+(e/s)*mu*int(T==0)+2*e*t for T,q in enumerate(R)]
 Q=[V[x%len(R)]*p/M[x%len(R)] for x,p in enumerate(P)]
 ck(sum(P)==sum(Q)==1);ck(all(q>=0 for q in Q));ck(V[0]==M[0])
 return v,P,Q
def B(P,j):return sub(CE(P,P),CE(marginal(P,j),marginal(P,j)))
def influence(v):
 n=(len(v)-1).bit_length()
 return sum(F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v)) for j in range(n))
def W(a,b,r,R):
 e=F(2,1<<(a+b+r));return add(CE(spec(src(a,b)),R),(10*e*(a+b+r),)*2)
def active(a,b,r,R):
 v,P,Q=floor(a,b,r,R);old=marginal(Q,0);on=child(v,0,0);off=child(v,0,1)
 ck(all(x==1 for x in off));costoff=mul(-1,log(old[0]));debit=B(P,0)
 if a==1:
  pn=spec(on);ck(sum(pn)==1)
  return None,debit,costoff,CE(pn,pn)
 Rn=cal(marginal(R,0),spec(src(a-1,b)))
 vn,pn,qn=floor(a-1,b,r,Rn);ck(vn==on)
 e=F(2,1<<(a+b+r))
 local=add(debit,mul(F(1,2),W(a-1,b,r,Rn)),mul(F(1,2),costoff))
 ck(local[1]<=W(a,b,r,R)[0]-e)
 return Rn,debit,costoff,CE(pn,qn)
def history(a,b,r,R,prefix,suffix):
 a0=a;e0=F(2,1<<(a+b+r));Ig=F(2*a,1<<a);c=CE(spec(src(a,b)),R)
 K=2*c[1]/Ig+10;v,P,Q=floor(a,b,r,R);quota=K*influence(v)
 ck(quota-W(a,b,r,R)[1]>=20*a*e0)
 debit=(F(0),F(0));term=(F(0),F(0));reach=F(1)
 for _ in range(prefix):
  Rn,d,k,_=active(a,b,r,R);ck(Rn is not None)
  debit=add(debit,mul(reach,d));term=add(term,mul(reach/2,k));reach/=2;a-=1;R=Rn
 v,P,Q=floor(a,b,r,R);j=a+b;e=F(2,1<<(a+b+r));s=F(1,1<<a);t=F(1,1<<(a+b))
 old=marginal(Q,j);off=child(v,j,1);on=child(v,j,0)
 ck(off==src(a,b)*(1<<(r-1)));vn,pn,qn=floor(a,b,r-1,R);ck(on==vn)
 d=B(P,j);coff=CE(spec(off),old);c=CE(spec(src(a,b)),R)
 ck(d[1]<12*e);ck(sub(coff,c)[1]<11*e)
 loc=add(d,mul(F(1,2),coff),mul(F(1,2),W(a,b,r-1,R)))
 ck(loc[1]<W(a,b,r,R)[0]+8*e)
 # Exact data-normalizer and overlap bounds used in the analytic proof.
 h=e/s;kappa=((2*s-e)**2+e*e)/(4*s*s-4*s*e+2*t*e)
 ck(0<h<=F(1,2));ck(1/kappa<=1+h/2)
 Pg=spec(src(a,b))
 for T,pT in enumerate(Pg):
  if pT and T:ck(old[T]>=R[T]*(1-h)*kappa)
 ck(old[0]>=R[0]);ck(reach*e==e0)
 debit=add(debit,mul(reach,d));term=add(term,mul(reach/2,coff));reach/=2;r-=1
 for _ in range(suffix):
  Rn,d,k,last=active(a,b,r,R)
  debit=add(debit,mul(reach,d));term=add(term,mul(reach/2,k));reach/=2
  if a==1:
   full=add(debit,term,mul(reach,last));ck(full[1]<=quota-12*e0)
   return full[1]
  R=Rn;a-=1
 v,P,Q=floor(a,b,r,R);full=add(debit,term,mul(reach,CE(P,Q)))
 ck(full[1]<=quota-12*e0)
 return full[1]

def main():
 pilot='--pilot' in sys.argv
 # Freeze before any family evaluation; no automated dimension escalation.
 save('FROZEN_SPEC_PILOT.json' if pilot else 'FROZEN_SPEC.json',{'helper':'check_transfer.py v1/direct character sums','family':'1-2A_a+2A_(a+b+r)','domain':{'a':[1,2] if pilot else [1,2,3],'b':[0] if pilot else [0,1],'r':[2] if pilot else [2,3],'references':['matching','uniform','increasing','singleton-spiked']},'cases':16 if pilot else 48,'histories':'every prefix length 0..a-1 then one control then each suffix length 0..a-prefix; fixed labelled active order, no symmetry claim','arithmetic':'Fraction spectra, rational log intervals (22 terms plus exact tail)','memory_estimate_mb':80,'max_runtime_seconds':55,'search_type':'bounded exact validation, not exhaustive over references'})
 roots=0;hist=0;minratio=None
 for a in ([1,2] if pilot else [1,2,3]):
  for b in ([0] if pilot else [0,1]):
   for r in ([2] if pilot else [2,3]):
    Pg=spec(src(a,b));N=len(Pg)
    raws=[Pg,[F(1,N)]*N,[F(2*(i+1),N*(N+1)) for i in range(N)],[F(1000 if i==1 else 1,1000+N-1) for i in range(N)]]
    for raw in raws:
     R=cal(raw,Pg);roots+=1
     for p in range(a):
      for q in range(a-p+1):history(a,b,r,R,p,q);hist+=1
 # Boundary guard: r=1 fails h<=1/2 when b=0, so excluded from new query.
 ck(F(2,1<<(2+1))/F(1,1<<2)==1)
 result={'status':'PASS','roots':roots,'histories':hist,'checks':checks,'runtime_seconds':time.perf_counter()-START,'r1_boundary':'excluded: h=1 is possible','claimed_scope':'one control exposure after active prefix, then active resets or no-reset continuations; not arbitrary mixed histories'}
 save('PILOT.json' if pilot else 'VALIDATION.json',result);print(json.dumps(result))
if __name__=='__main__':main()
