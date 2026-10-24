from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
import json,sys,time,hashlib
R=Path(__file__).resolve().parents[1]
checks=0
def ck(test,label):
 global checks
 checks+=1
 if not test: raise AssertionError(label)
Z=(F(0),F(0)); ONE=(F(1),F(1))
DEN=1<<140
def bound(lo,hi):
 return F((lo*DEN).__floor__(),DEN),F((hi*DEN).__ceil__(),DEN)
def iv(x): return (F(x),F(x))
def add(a,b):return bound(a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 vals=[x*y for x in a for y in b];return bound(min(vals),max(vals))
def div(a,b):
 ck(not b[0]<=0<=b[1],"nonzero interval denominator")
 return mul(a,(1/b[1],1/b[0]))
def scale(x,a):return mul(iv(x),a)
def isum(v):
 s=Z
 for x in v:s=add(s,x)
 return s
def encode(a):return [str(x) for x in a]
def lnseries(x,N=24):
 t=(x-1)/(x+1);ck(0<=t<=F(1,3),"atanh range")
 lo=2*sum((t**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
 tail=2*t**(2*N+1)/(F(2*N+1)*(1-t*t))
 return lo,lo+tail
LN2=lnseries(F(2))
@lru_cache(None)
def log2(x):
 ck(x>0,"positive log")
 k=x.numerator.bit_length()-x.denominator.bit_length()
 u=x/(F(2)**k)
 while u<1:u*=2;k-=1
 while u>=2:u/=2;k+=1
 ul,uh=bound(u,u)
 low=lnseries(ul)[0];high=lnseries(uh)[1]
 v=add(iv(k),div((low,high),LN2))
 den=1<<110
 return F((v[0]*den).__floor__(),den),F((v[1]*den).__ceil__(),den)
def logiv(x):return log2(x[0])[0],log2(x[1])[1]
def h2(x):
 if x in (0,1):return Z
 return neg(add(scale(x,log2(x)),scale(1-x,log2(1-x))))
def factors(x):
 out={};p=2
 while p*p<=x:
  while x%p==0:out[p]=out.get(p,0)+1;x//=p
  p+=1
 if x>1:out[x]=out.get(x,0)+1
 return out
def formal_sum(*terms):
 out={}
 for c,v in terms:
  for p,x in v.items():out[p]=out.get(p,F(0))+c*x
 return {p:x for p,x in out.items() if x}
def flog(q):
 return formal_sum((1,factors(q.numerator)),(-1,factors(q.denominator)))
def fent(p):return formal_sum(*[(-q,flog(q)) for q in p if q])
def feval(v):return isum(scale(c,log2(F(p))) for p,c in v.items())
def law(t):
 a=list(t);N=len(a);h=1
 while h<N:
  for i in range(0,N,2*h):
   for j in range(i,i+h):u,v=a[j],a[j+h];a[j]=u+v;a[j+h]=u-v
  h*=2
 return [F(x*x,N*N) for x in a]
def restrict(t,i,y):
 return [t[(j&((1<<i)-1))|((j>>i)<<(i+1))|(y<<i)] for j in range(len(t)//2)]
def info(t):
 p=law(t);n=len(t).bit_length()-1
 ck(sum(p)==1,"Parseval")
 d=[sum((q for s,q in enumerate(p) if s>>j&1),F(0)) for j in range(n)]
 for j,x in enumerate(d):
  ck(x==F(sum(t[u]!=t[u^(1<<j)] for u in range(len(t))),len(t)),"physical influence")
 return p,d,fent(p)
def table(n):
 return [-1 if not(t&1) and t&2 else (-1 if not(t>>3) else 1) if t&1 and t&4 else 1 for t in range(1<<(n+3))]
def pd(d):return [-1]+[1]*((1<<d)-1)
def canonical(p,d):
 v=1-p[0];rs=[x/v for x in d]
 ck(v>0 and all(0<x<1 for x in rs) and sum(rs)>1,"canonical interior")
 def g(c):
  q=F(1)
  for x in rs:q*=1-c*x
  return 1-c-q
 lo,hi=F(0),F(1)
 for _ in range(50):
  mid=(lo+hi)/2
  if g(mid)>0:lo=mid
  else:hi=mid
 ck(lo>0 and g(lo)>0>g(hi),"positive canonical bracket")
 c=(lo,hi);theta=[scale(x,c) for x in rs]
 hm=neg(add(scale(p[0],log2(p[0])),scale(v,logiv(div(iv(v),c)))))
 for x,t in zip(d,theta):
  hm=sub(hm,add(scale(x,logiv(t)),scale(v-x,logiv(sub(ONE,t)))))
 Q=[]
 for mask in range(len(p)):
  if not mask:Q.append(iv(p[0]));continue
  q=div(iv(v),c)
  for j,t in enumerate(theta):q=mul(q,t if mask>>j&1 else sub(ONE,t))
  Q.append(q)
 ck(isum(Q)[0]<=1<=isum(Q)[1],"M normalized")
 for j,x in enumerate(d):
  a=isum(q for mask,q in enumerate(Q) if mask>>j&1)
  ck(a[0]<=x<=a[1],"M matched marginal")
 return Q,hm,c
def kl(p,q):
 return isum(scale(x,logiv(div(iv(x),y))) for x,y in zip(p,q) if x)
def erase(q,i):
 return [add(q[s],q[s|(1<<i)]) for s in range(len(q)) if not s>>i&1]
def step(t,Q,i):
 p=law(t);ts=[restrict(t,i,y) for y in (0,1)];ps=[law(t) for t in ts]
 fused=[p[s]+p[s|(1<<i)] for s in range(len(p)) if not s>>i&1]
 ck(fused==[(x+y)/2 for x,y in zip(*ps)],"coherent squared-child interference")
 qr=erase(Q,i)
 ks=[[ps[y][s]/(2*fused[s]) if fused[s] else F(1,2) for s in range(len(fused))] for y in (0,1)]
 out=[isum(scale(k,q) for k,q in zip(ks[y],qr)) for y in (0,1)]
 qc=[[div(scale(k,q),out[y]) for k,q in zip(ks[y],qr)] for y in (0,1)]
 E=sub(kl(p,Q),kl(fused,qr));O=kl([F(1,2)]*2,out)
 child=scale(F(1,2),isum(kl(p,q) for p,q in zip(ps,qc)))
 rhs=add(E,add(O,child));lhs=kl(p,Q)
 ck(rhs[0]<=lhs[1] and lhs[0]<=rhs[1],"KL telescope enclosure check only")
 ck(E[1]>=0 and O[1]>=0,"nonnegative charges")
 return ts,qc,E,O,sum(x==0 for x in fused)
def inherited(n,Q):
 ts,qs,E,O,rows=step(table(n),Q,1);front=[(t,q,F(1,2)) for t,q in zip(ts,qs)]
 for _ in range(n):
  nxt=[]
  for t,q,w in front:
   cs,cq,e,o,rr=step(t,q,2);E=add(E,scale(w,e));O=add(O,scale(w,o));rows+=rr
   nxt.extend((ct,cqq,w/2) for ct,cqq in zip(cs,cq))
  front=nxt
 K=isum(scale(w,kl(law(t),q)) for t,q,w in front)
 A=kl(law(table(n)),Q);end=add(E,add(O,K))
 ck(end[0]<=A[1] and A[0]<=end[1],"complete all-data account")
 ck(rows>0,"source-zero reference rows actually retained")
 return {"E":encode(E),"O":encode(O),"terminal_KL":encode(K),"root_A_direct":encode(A),"source_zero_rows":rows,"terminals":len(front)}
def run(n,pilot=False):
 e=F(1,1<<n);m=1-e;t=table(n);p,d,h0=info(t);I0=sum(d)
 ck(d==[F(1,2),F(1,2)]+[e/2]*(n+1),"root moments")
 pred=formal_sum((2+n*e*(2-e),flog(F(2))),(-m*m,flog(m)))
 ck(h0==pred,"root entropy exact prime-log identity")
 Q,hm,c=canonical(p,d);H0=feval(h0);A=sub(hm,H0);Sroot=sub(iv(4*I0),H0)
 ck(H0[0]>2,"root H lower")
 ck(Sroot[0]>2,"root S eligibility")
 states={}
 for a in (0,1):
  for k in range(n+1):
   tabs=[restrict(t,1,a)]
   for _ in range(n-k):tabs=[restrict(u,2,y) for u in tabs for y in (0,1)]
   facts=[info(u) for u in tabs];w=F(1,len(tabs))
   If=sum((w*sum(f[1]) for f in facts),F(0));hf=formal_sum(*[(w,f[2]) for f in facts])
   J=fent(law(pd(k+2)))
   ck(hf==formal_sum((e*(1<<k),J)),"adaptive branch entropy exact")
   expected=(k+2)*e/2 if not a else 1+k*e/2
   ck(If==expected,"adaptive branch influence exact")
   states[a,k]=(If,hf)
 out=[]
 for k0 in range(n+1):
  for k1 in range(n+1):
   If=(states[0,k0][0]+states[1,k1][0])/2
   hf=formal_sum((F(1,2),states[0,k0][1]),(F(1,2),states[1,k1][1]))
   ck(If==F(1,2)+e*(k0+k1+2)/4,"history mean I")
   Hf=feval(hf);S=sub(iv(4*If),Hf);D=sub(H0,Hf);RR=I0-If
   debit=sub(D,iv(4*RR));L=add(A,(max(F(0),debit[0]),max(F(0),debit[1])))
   margin=sub(S,L);identity=(min(sub(S,A)[0],sub(Sroot,A)[0]),min(sub(S,A)[1],sub(Sroot,A)[1]))
   ck(margin[0]<=identity[1] and identity[0]<=margin[1],"min identity enclosure only")
   ck(S[0]>2-F(3,2)*e,"all-history bank lower")
   if n>=3:ck(margin[0]>F(7,16),"complete source and old booking paid")
   out.append({"k":[k0,k1],"S":encode(S),"liability":encode(L),"margin":encode(margin),"If":str(If),"Hf":encode(Hf)})
 guardS=2*e;guard=sub(iv(guardS),A)
 # Construct all actual terminals after a,data,x, keeping b; no terminal omitted.
 It=F(0);ht={}
 for a in (0,1):
  for z in range(1<<n):
   for x in (0,1):
    terminal=[-1 if not x and a else (-1 if z==0 else 1) if x and b else 1 for b in (0,1)]
    _,dd,hh=info(terminal);weight=F(1,4*(1<<n));It+=weight*sum(dd);ht=formal_sum((1,ht),(weight,hh))
 ck(It==e/2 and not ht,"mixed-controller full terminal bank")
 ck(Sroot[0]>2*e,"no new positive decrement liability after x")
 if n>=3:ck(guard[1]<0,"mixed controller extension refuted exactly")
 result={"n":n,"c":encode(c),"A":encode(A),"H0":encode(H0),"root_surplus":encode(Sroot),"histories":out,"mixed_x_bank":str(guardS),"mixed_x_margin":encode(guard)}
 if n in ((3,) if pilot else (3,4)):result["inherited_full_history"]=inherited(n,Q)
 return result
def scalar_checks():
 out=[]
 for n in [16,17,24,32,64]:
  e=F(1,1<<n);L=n+1;z=1-e/2;t=(1-e)**2/(4*z**L)
  ck(0<t<F(1,2),"competitor positivity")
  ck(t*z**L==(1-e)**2/4,"competitor exact empty mass")
  ck(abs(t-F(1,4))<=L*e/2,"competitor correlation bound")
  ck(8*L*L*e<1,"all-n tail anchor")
  hcomp=add(add(iv(1),h2(2*t)),scale(L,h2(e/2)))
  H0=add(iv(2+n*e*(2-e)),scale(-(1-e)**2,log2(1-e)))
  lower=sub(hcomp,H0);bound=(F(n*n,2)-n-2)*e
  ck(lower[0]>bound,"competitor A lower bound")
  ck(bound>2*e,"mixed all-n obstruction sign")
  out.append({"n":n,"competitor_A_lower":encode(lower),"analytic_bound":str(bound)})
 ck(8*17**2<2**16,"tail anchor integer")
 ck(16*16+F(3,2)*16-2>0,"envelope ratio boundary")
 ck(2-F(3,2)*F(1,8)-F(11,8)==F(7,16),"uniform margin exact")
 return out
def main():
 start=time.perf_counter();pilot="--pilot" in sys.argv
 results=[]
 for n in ([3] if pilot else [1,2,3,4,5,6]):
  results.append(run(n,pilot))
  (R/"out"/"CHECKPOINT.json").write_text(json.dumps({"last_n":n,"checks":checks,"runtime_seconds":time.perf_counter()-start}),encoding="utf-8")
  ck(time.perf_counter()-start<(60 if pilot else 55),"frozen runtime")
 scalar=scalar_checks()
 ck(time.perf_counter()-start<(60 if pilot else 55),"total frozen runtime including scalar checks")
 summary={"status":"PASS","checks":checks,"runtime_seconds":time.perf_counter()-start,"admitted_history_pairs":sum(len(x["histories"]) for x in results if x["n"]>=3),"boundary_pairs":sum(len(x["histories"]) for x in results if x["n"]<3),"minimum_margin":encode(min((tuple(F(v) for v in p["margin"]) for x in results if x["n"]>=3 for p in x["histories"]),key=lambda z:z[0]))}
 result={"summary":summary,"results":results,"scalar":scalar,"script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (R/"out").mkdir(exist_ok=True)
 (R/"out"/("PILOT.json" if pilot else "CHECK.json")).write_text(json.dumps(result,indent=2),encoding="utf-8")
 print(json.dumps(summary))
if __name__=="__main__":main()
