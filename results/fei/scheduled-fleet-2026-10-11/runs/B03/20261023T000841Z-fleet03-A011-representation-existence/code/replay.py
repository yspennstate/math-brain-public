import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json,time
import shared as logs
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0;cases=0;roots=0
def ck(v):
 global checks
 checks+=1;assert v,checks
def walsh(v):
 N=len(v)
 return [F(sum(val*(-1 if (x&T).bit_count()%2 else 1) for x,val in enumerate(v)),N) for T in range(N)]
def prob(v):return [x*x for x in walsh(v)]
def ce(P,Q):
 agg=defaultdict(F)
 for p,q in zip(P,Q):
  if p:ck(q>0);agg[q]+=p
 a=b=F(0)
 for q,p in agg.items():l,h=logs.log(1/q);a+=p*l;b+=p*h
 return a,b
def debt(P,Q):
 c=ce(P,Q);h=ce(P,P);return c[0]-h[1],c[1]-h[0]
def edgeI(v):
 n=len(v).bit_length()-1
 return F(2*sum(v[x]!=v[x^(1<<i)] for x in range(len(v)) for i in range(n) if x<(x^(1<<i))),len(v))
def pair(g,ref,i):
 N=len(g)//2;s=sum(ref)
 def insert(x,bit):return (x%(2**i))+(x//(2**i))*(2**(i+1))+bit*(2**i)
 gs=[[g[insert(x,bit)] for x in range(N)] for bit in [0,1]];Ps=[prob(x) for x in gs];P=prob(g)
 m=[P[insert(x,0)]+P[insert(x,1)] for x in range(N)];rr=[ref[insert(x,0)]+ref[insert(x,1)] for x in range(N)]
 raw=[[rr[x]*Ps[b][x]/m[x] if m[x] else rr[x] for x in range(N)] for b in [0,1]];Z=[sum(x) for x in raw];ck(sum(Z)==2*s)
 Qs=[[s*z/Z[b] for z in raw[b]] for b in [0,1]]
 for b in [0,1]:
  ck(sum(Qs[b])==s)
  for x in range(N):
   if Ps[b][x]:ck(Ps[b][x]/Qs[b][x]==m[x]/rr[x]*Z[b]/s)
 return gs,Qs
def edited(g,b,ref):
 a=len(g).bit_length()-1;n=a+b;N=2**n;p=F(1,2);t=F(1,N);beta=6*p*t
 v=[g[y%len(g)]-2*g[0]*(x==0 and y==0) for x in range(2) for y in range(N)]
 P=prob(v);q=[P[z]+P[N+z] for z in range(N)]
 rr=[((ref[z] if z<len(ref) else 0)+beta*t)/(1+beta) for z in range(N)]
 Q=[rr[z]*P[u*N+z]/q[z] for u in range(2) for z in range(N)];ck(sum(Q)==(sum(ref)+beta)/(1+beta))
 return P,Q,v
for label in [1,23,105,126]:
 gbase=[1 if label>>x&1 else -1 for x in range(8)]
 for point in range(8):
  g=[gbase[x^point] for x in range(8)];Psrc=prob(g);Hsrc=ce(Psrc,Psrc);Ig=edgeI(g);d=sum(g[0]!=g[1<<i] for i in range(3))
  for mass in [F(1),F(1,3)]:
   ref=[mass*F(T+1,36) for T in range(8)];c=ce(Psrc,ref);D=debt(Psrc,ref);C0=c[1]/Ig;K=4*C0+15
   P,Q,v=edited(g,1,ref);Hr=ce(P,P);Iroot=edgeI(v);p=F(1,2);t=F(1,16);C=2*p*t*(4-d);J=2*p*t;Broot=2*p*t*5
   original=[gbase[y%8]-2*gbase[point]*(x==0 and y==point) for x in range(2) for y in range(16)]
   ck(prob(original)==P);ck(Iroot==edgeI(original));off=F(0);curr=g;Rcur=ref
   for k in range(1,4):
    # Query current highest source bit; no primary transform or inheritance routine imported.
    idx=len(curr).bit_length()-2;children,Rs=pair(curr,Rcur,idx)
    Dother=debt(prob(children[1]),Rs[1]);off+=F(1,2**k)*Dother[1]
    Pe,Qe,ve=edited(children[0],0,Rs[0]);De=debt(Pe,Qe)
    L_hi=Hr[1]+D[1]/2+(off+F(1,2**k)*De[1])/2
    ck(K*Iroot-L_hi>=K*(C+J))
    # Explicit prior booking U=K(C+J)/2 retained, no renewed account.
    U=min((C0+1)*Ig,K*(C+J))/2;ck(K*Iroot-L_hi-U>=U)
    if k==3:ck(sum(Qe)>=(sum(ref)))
    curr=children[0];Rcur=Rs[0];cases+=1
   roots+=1
   if time.monotonic()-start>55:raise RuntimeError('frozen55second cutoff')
for sign in [-1,1]:
 g=[sign,sign];P,Q,v=edited(g,1,[F(1),F(0)])
 ck(edgeI(g)==0);ck(ce(P,P)[0]>0)
 # Ig=0 would make the asserted residual K(C+J) equal the ENTIRE influence bill,
 # while L>=H(F)>0. Thus nonconstant source is essential for this margin.
for q in range(2,65):ck(4*(q+1)<=3*(2**q))
ck(logs.log(F(1,2))[1]<0) # mass2 exact-source reference has negative D: invalid admission.
out={'status':'PASS','root_reference_cases':roots,'source_prefix_reference_cases':cases,'constant_exclusion_cases':2,'superprobability_exclusion_cases':1,'exact_assertions':checks,'seconds':time.monotonic()-start,'independence':'direct character sums and separate physical inheritance; primary checker not imported'}
(R/'out/REPLAY_RESULTS.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
