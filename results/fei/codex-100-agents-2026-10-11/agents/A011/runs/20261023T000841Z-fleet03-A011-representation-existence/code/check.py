import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
from collections import defaultdict
import json,time
import shared as s
R=Path(__file__).resolve().parents[1];start=time.monotonic();mode=sys.argv[1]
cores=roots=prefixes=finals=constant_siblings=both_nonconstant=zero_fibers=0
minimum=None;eps=F(1,2**75)
def ck(v):s.ck(v)
def add(A,B):return A[0]+B[0],A[1]+B[1]
def mul(w,A):return w*A[0],w*A[1]
def ce(P,Q):
 masses=defaultdict(F)
 for p,q in zip(P,Q):
  if p:ck(q>0);masses[q]+=p
 low=high=F(0)
 for q,p in masses.items():
  a,b=s.log(1/q);low+=p*a;high+=p*b
 return low,high
def spectral(g):return [z*z for z in s.fw(g)]
def floor(g,b,r,ref):
 a=len(g).bit_length()-1;n=a+b;N=2**n;p=F(1,2**r);t=F(1,N);beta=6*p*t
 v=[g[y%len(g)]-2*g[0]*(x==0 and y==0) for x in range(2**r) for y in range(N)]
 P=spectral(v);q=[sum(P[u*N+T] for u in range(2**r)) for T in range(N)]
 dataref=[((ref[T] if T<len(ref) else 0)+beta*t)/(1+beta) for T in range(N)]
 Q=[dataref[T]*P[u*N+T]/q[T] for u in range(2**r) for T in range(N)]
 mass=(sum(ref)+beta)/(1+beta);ck(sum(P)==1);ck(sum(Q)==mass)
 H=ce(P,P);c=ce(P,Q)
 return {'v':v,'P':P,'Q':Q,'H':H,'c':c,'D':s.sub(c,H),'M':mass}
def inherit(g,ref,i):
 global zero_fibers
 Pc=[];gs=[];P=spectral(g);M=sum(ref);N=len(g)//2
 for bit in [0,1]:
  child=[g[s.insert(W,i,bit)] for W in range(N)];gs.append(child);Pc.append(spectral(child))
 marg=[P[s.insert(W,i,0)]+P[s.insert(W,i,1)] for W in range(N)]
 rr=[ref[s.insert(W,i,0)]+ref[s.insert(W,i,1)] for W in range(N)]
 for W in range(N):ck(marg[W]==(Pc[0][W]+Pc[1][W])/2)
 pi=[[Pc[j][W]/(2*marg[W]) if marg[W] else F(1,2) for W in range(N)] for j in [0,1]]
 raw=[[2*rr[W]*pi[j][W] for W in range(N)] for j in [0,1]];Z=[sum(z) for z in raw]
 ck(Z[0]+Z[1]==2*M);ck(Z[0]*Z[1]<=M*M)
 refs=[];Ds=[]
 for bit in [0,1]:
  ck(Z[bit]>0);qb=[M*z/Z[bit] for z in raw[bit]];refs.append(qb);ck(sum(qb)==M)
  for W in range(N):
   if Pc[bit][W]:ck(Pc[bit][W]/qb[W]==marg[W]/rr[W]*Z[bit]/M)
  Ds.append(s.sub(ce(Pc[bit],qb),ce(Pc[bit],Pc[bit])))
 zero_fibers+=sum(marg[W]==0 and rr[W]>0 for W in range(N))
 D=s.sub(ce(P,ref),ce(P,P));ck((Ds[0][0]+Ds[1][0])/2<=D[1]+eps)
 return gs,refs,Ds
if mode=='pilot':domain=[(a,j) for a in [1,2] for j in range(1,2**(2**a)-1)]
else:
 batch=int(mode);domain=[(3,j) for j in range(1+32*batch,min(255,1+32*(batch+1)))]
for a,label in domain:
 g=[1 if label>>y&1 else -1 for y in range(2**a)];Pg=spectral(g);H=ce(Pg,Pg);Ig=sum(s.inf(g));ck(Ig>=F(2*a,2**a))
 orders=[tuple(range(a))] if mode=='pilot' else list(permutations(range(a)))
 for b in [1,2]:
  for r in [1,2]:
   w=F(1,2**b);p=F(1,2**r);t=F(1,2**(a+b));d=sum(g[0]!=g[1<<i] for i in range(a))
   C=2*p*t*(a+b-d);E=2*p*t*d;J=2*r*p*t;Broot=2*p*t*(a+b+r)
   for name,ref in [('P',Pg),('halfP',[z/2 for z in Pg]),('U',[F(1,2**a)]*len(g)),('eighthP',[z/8 for z in Pg])]:
    c=ce(Pg,ref);D=s.sub(c,H);root=floor(g,b,r,ref);Iroot=sum(s.inf(root['v']));C0=c[1]/Ig;K=4*C0+15
    ck(Iroot==Ig+C-E+J);ck(E<=Ig/4);ck(root['H'][1]<=2*H[0]+15*Broot)
    ck(root['c'][1]<=2*c[1]+15*Broot)
    for order in orders:
     currg=g;currr=ref;live=list(range(a));current=floor(g,0,r,ref);stopD=(F(0),F(0))
     Lpad=add(root['H'],add(mul(1-w,D),mul(w,current['D'])))
     reset=s.sub(Lpad,root['c']);Lprev=Lpad
     for k,originalbit in enumerate(order,1):
      idx=live.index(originalbit);gs,refs,Ds=inherit(currg,currr,idx);child=floor(gs[0],0,r,refs[0]);reach=F(1,2**k)
      stopD=add(stopD,mul(reach,Ds[1]));srcD=add(stopD,mul(reach,Ds[0]));ck(srcD[0]<=D[1]+eps)
      Hh=ce(spectral(gs[0]),spectral(gs[0]));ck(reach*Hh[0]<=H[1]+eps);ck(reach*Ds[0][0]<=D[1]+eps)
      totalD=add(mul(1-w,D),mul(w,add(stopD,mul(reach,child['D']))));L=add(root['H'],totalD)
      lam=s.sub(s.avg(child['D'],Ds[1]),current['D']);reset=add(reset,mul(w*2*reach,lam))
      reconstructed=add(root['c'],reset)
      ck(abs(reconstructed[0]-L[0])<eps);ck(abs(reconstructed[1]-L[1])<eps)
      # Both physical source-query children checked directly against actual truth tables.
      for bit,expected in [(0,child['v']),(1,[gs[1][x%len(gs[1])] for x in range(len(child['v']))])]:
       actual=[current['v'][s.insert(x,idx,bit)] for x in range(len(expected))];ck(actual==expected)
      if len(set(gs[1]))==1:constant_siblings+=1
      if len(set(gs[1]))==2 and len(set(child['v']))==2:both_nonconstant+=1
      if k<a:
       m=a-k;Bh=2*p*F(1,2**m)*(m+r)
       ck(child['c'][1]<=2*ce(spectral(gs[0]),refs[0])[1]+15*Bh)
       local=Broot+w*reach*Bh
       ck(local<=F(3,4)*Ig)
       ck(L[1]<=2*(1+w)*c[1]+15*local)
       ck(K*Iroot-L[1]>=K*(C+J))
      else:
       ck(len(refs[0])==1 and refs[0][0]==sum(ref))
       ck(child['M']==(sum(ref)+6*p)/(1+6*p));ck(child['M']>=sum(ref))
       ck(child['D'][0]<=s.log(1/sum(ref))[1]+eps)
       ck(L[1]<=2*c[1]+15*Broot)
       ck(K*Iroot-L[1]>=C0*Ig+K*(C+J));finals+=1
      slack=K*Iroot-L[1]-K*(C+J);minimum=slack if minimum is None else min(minimum,slack)
      prefixes+=1;currg=gs[0];currr=refs[0];live.remove(originalbit);current=child;Lprev=L
      if time.monotonic()-start>55:
       (R/f'out/INCOMPLETE_{mode}.json').write_text(json.dumps({'prefixes_done':prefixes,'reason':'frozen55second cutoff'}),encoding='utf-8');raise RuntimeError('frozen cutoff')
    roots+=1
 cores+=1
out={'status':'PASS','mode':mode,'labelled_cores':cores,'root_reference_cases':roots,'source_order_prefix_reference_cases':prefixes,'final_source_cases':finals,'constant_unedited_siblings':constant_siblings,'both_nonconstant_children':both_nonconstant,'zero_true_source_fibers_with_positive_reference':zero_fibers,'exact_assertions':s.checks,'minimum_certified_extra_margin':str(minimum),'seconds':time.monotonic()-start}
(R/f'out/CHECK_{mode}.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
