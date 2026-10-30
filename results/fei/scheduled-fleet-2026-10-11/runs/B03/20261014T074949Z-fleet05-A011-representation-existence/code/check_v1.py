from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
def fw(v):
 a=list(v);step=1
 while step<len(a):
  for i in range(0,len(a),2*step):
   for j in range(i,i+step):a[j],a[j+step]=a[j]+a[j+step],a[j]-a[j+step]
  step*=2
 return [F(z,len(a)) for z in a]
def insert(W,j,b):return (W&((1<<j)-1))|((W>>j)<<(j+1))|(b<<j)
def inf(v):return [F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v)) for j in range(len(v).bit_length()-1)]
@lru_cache(None)
def log(x):
 x=F(x);k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def ln(z):
  w=(z-1)/(z+1);lo=2*sum((w**(2*i+1)/F(2*i+1) for i in range(32)),F(0))
  return lo,lo+2*w**65/(65*(1-w*w))
 a,b=ln(x);c,d=ln(F(2));return F(k)+a/d,F(k)+b/c
def ce(P,Q):
 lo=hi=F(0)
 for p,q in zip(P,Q):
  if p:
   ck(q>0);a,b=log(1/q);lo+=p*a;hi+=p*b
 return lo,hi
def entropy(P):return ce(P,P)
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def avg(a,b):return (a[0]+b[0])/2,(a[1]+b[1])/2
def display(x):return [str(x[0]),str(x[1])]
cases=[];tensor_checks=0
for k in [2,4,6]:
 n=k+4;N=2**n;t=F(1,N);j=k+3;zstar=(1<<(k//2))-1
 def core(W):
  z=W&((1<<k)-1);y=(W>>k)&7
  bend=(-1)**sum(((z>>(2*i))&1)*((z>>(2*i+1))&1) for i in range(k//2))
  return bend*(-1 if y==0 else 1)
 v=[core(W)*(-1 if W==zstar else 1) for W in range(2*N)]
 g=[core(W) for W in range(N)]
 a=fw(v);P=[x*x for x in a];aq=[P[T]+P[N+T] for T in range(N)]
 Q=[t*P[U*N+T]/aq[T] for U in range(2) for T in range(N)]
 ck(sum(Q)==1);ck(all(x>0 for x in Q))
 for U in range(2):
  for T in range(N):ck(Q[U*N+T]*aq[T]==t*P[U*N+T])
 Ig=sum(inf(g));iv=inf(v);If=sum(iv)
 ck(Ig==F(k,2)+F(3,4));ck(If==Ig-t);ck(iv[j]==t);ck(iv[n]==t)
 old=sum(g[zstar]!=g[zstar^(1<<i)] for i in range(n));ck(old==k//2+3)
 vals=[[v[insert(W,j,b)] for W in range(N)] for b in range(2)]
 ac=[fw(vals[b]) for b in range(2)];Pc=[[x*x for x in ac[b]] for b in range(2)]
 ck(sum(inf(vals[0]))==Ig-4*t);ck(sum(inf(vals[1]))==Ig)
 ck(all(len(set(vals[b]))==2 for b in range(2)))
 m=[(Pc[0][W]+Pc[1][W])/2 for W in range(N)]
 rr=[Q[insert(W,j,0)]+Q[insert(W,j,1)] for W in range(N)]
 Rt=[[rr[W]*Pc[b][W]/m[W] for W in range(N)] for b in range(2)]
 Z=[sum(Rt[b]) for b in range(2)];Rb=[[x/Z[b] for x in Rt[b]] for b in range(2)]
 ck(Z[0]+Z[1]==2);ck(Z[0]>0 and Z[1]>0);ck(Z[0]*Z[1]<=1)
 for W in range(N):
  i0=insert(W,j,0);i1=insert(W,j,1)
  ck(P[i0]+P[i1]==m[W])
  ck(ac[0][W]==a[i0]+a[i1]);ck(ac[1][W]==a[i0]-a[i1])
  for b in range(2):
   ck(Rb[b][W]*m[W]*Z[b]==rr[W]*Pc[b][W])
 Hp=entropy(P);Hc=[entropy(Pc[b]) for b in range(2)];Dlt=sub(Hp,avg(*Hc))
 cp=ce(P,Q);cc=[ce(Pc[b],Rb[b]) for b in range(2)];Tcost=sub(cp,avg(*cc))
 B=sub(Hp,entropy(aq));ck(B[1]<=(k+8)*t)
 ck(cp[1]<4*If);ck(Dlt[0]>(F(k,2)+5)*t);ck(Tcost[0]>(F(k,2)+5)*t)
 # Every signed row also checks the exact scalar second-difference coefficients.
 for W in range(N):
  z=a[insert(W,j,1)];oldcoef=ac[1][W]
  ck(abs(z)==t)
  if oldcoef:ck(abs(oldcoef/z) in [12*2**(k//2),4*2**(k//2)])
 # Incoming conditional likelihood disintegration, with exact argument factors.
 Llo=Lhi=F(0)
 for W in range(N):
  for b in range(2):
   ii=insert(W,j,b)
   prob=P[ii]/m[W];ref=Q[ii]/rr[W]
   ratio=prob/ref
   ck(P[ii]/Q[ii]==(m[W]/rr[W])*ratio)
   x,y=log(ratio);Llo+=P[ii]*x;Lhi+=P[ii]*y
 zn=log(Z[0]*Z[1]);release=(Llo-zn[1]/2,Lhi-zn[0]/2)
 ck(release[0]>=0)
 # The exact factor identities above prove the CE ledger; intervals independently check its sign.
 ledger=sub(Tcost,(Dlt[0]+release[0],Dlt[1]+release[1]));ck(ledger[0]<=0<=ledger[1])
 bank=sub((4*If,4*If),cp);lower=F(k-1)-(k+12)*t
 ck(lower>0);ck(bank[0]>=lower)
 ck(4*If-(F(k+4)+(k+8)*t)==lower)
 cases.append({'k':k,'I_query':str(t),'I_root':str(If),'normalizers':[str(z) for z in Z],'entropy_decrement_over_query':display((Dlt[0]/t,Dlt[1]/t)),'complete_query_cost_over_query':display((Tcost[0]/t,Tcost[1]/t)),'root_bank':display(bank),'proved_root_bank_lower':str(lower),'CE_parent':display(cp),'child_costs':[display(x) for x in cc]})
 (R/'out/CHECKPOINT.json').write_text(json.dumps({'status':'PARTIAL','completed':cases,'assertions':checks},indent=2),encoding='utf-8')
 if k==2:
  # Complete off-true-support terminal reference mass is retained by product-compatible zero-fiber choices.
  for bits in range(16):
   hv=[1 if bits>>x&1 else -1 for x in range(4)];hc=fw(hv);Ph=[x*x for x in hc]
   full=[hv[x]*v[W] for x in range(4) for W in range(2*N)];fcoef=fw(full)
   for x in range(4):
    for W in range(2*N):ck(fcoef[x*2*N+W]==hc[x]*a[W])
   ck(sum(inf(full))==sum(inf(hv))+If)
   for Rh in [Ph,[F(1,4)]*4]:
    for b in range(2):
     prod=[Rh[x]*Rb[b][W] for x in range(4) for W in range(N)]
     ck(sum(prod)==1)
     for x in range(4):
      for W in range(N):
       if Ph[x]*Pc[b][W]:ck(Ph[x]*Pc[b][W]/prod[x*N+W]==(Ph[x]/Rh[x])*(Pc[b][W]/Rb[b][W]))
    tensor_checks+=1
 if time.monotonic()-start>55:raise RuntimeError('frozen cutoff')
out={'status':'PASS','assertions':checks,'actual_queries':len(cases),'tensor_reference_cases':tensor_checks,'seconds':time.monotonic()-start,'cases':cases,'arithmetic':'Fraction, integer Walsh, exact atom likelihood factors, outward rational log signs','max_dimension':11}
(R/'out/EXACT_RESULTS.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({key:value for key,value in out.items() if key!='cases'}))
