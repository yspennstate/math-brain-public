from pathlib import Path
from fractions import Fraction as R
import json,time,hashlib
RUN=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=cases=0
def ck(x):
 global checks
 checks+=1;assert x,(cases,checks)
def fw(a):
 a=list(a);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for i in range(j,j+h):
    x,y=a[i],a[i+h];a[i],a[i+h]=x+y,x-y
  h*=2
 return a
def inf(a):
 N=len(a)
 return [R(sum(a[j]!=a[j^(1<<i)] for j in range(N)),N) for i in range((N-1).bit_length())]
def fac(n):
 r={};p=2
 while p*p<=n:
  while n%p==0:r[p]=r.get(p,0)+1;n//=p
  p+=1
 if n>1:r[n]=r.get(n,0)+1
 return r
def addlog(d,w,q):
 if not w:return
 assert q>0
 for sign,n in ((1,q.numerator),(-1,q.denominator)):
  for p,e in fac(n).items():d[p]=d.get(p,R(0))+w*e*sign
def clean(d):return {k:v for k,v in d.items() if v}
def combine(*terms):
 d={}
 for a,r in terms:
  for p,v in r.items():d[p]=d.get(p,R(0))+a*v
 return clean(d)
cs=[[1],[2],[3],[4,5],[6,7]];ws=[R(1,4),R(1,4),R(1,16),R(7,20),R(7,80)]
def stats(a,RY):
 z=fw(a);N=len(a);k=len(RY).bit_length()-1
 P=[R(v*v,N*N) for v in z]
 alpha=sum(p for j,p in enumerate(P) if j&7)
 RD=[R(0)]*8;RD[0]=1-alpha
 for w,cell in zip(ws,cs):
  for s in cell:RD[s]=alpha*w/len(cell)
 ce={}
 for j,p in enumerate(P):
  if p:addlog(ce,-p,RY[j>>3]*RD[j&7])
 py=[sum(P[s|(t<<3)] for s in range(8)) for t in range(1<<k)]
 pd=[sum(P[s|(t<<3)] for t in range(1<<k)) for s in range(8)]
 return alpha,clean(ce),py,pd
def h2(p):
 d={}
 if p:addlog(d,-p,p)
 if p<1:addlog(d,-(1-p),1-p)
 return clean(d)
RY=[R(i,10) for i in (1,2,3,4)];RYchild=[R(3,10),R(7,10)]
nonzero_signed=0
for j in range(256):
 codes=(j%16,j//16,(5*j+3)%16,(7*j+1)%16)
 hs=[[1 if code>>y&1 else -1 for y in range(4)] for code in codes]
 F=[hs[x&3][x>>3]*(-1 if not(x&1) and not(x&4) else 1) for x in range(32)]
 childs=[[F[(x&7)|((x>>3)<<4)|(b<<3)] for x in range(16)] for b in (0,1)]
 a,C,py,pd=stats(F,RY);ap,Cp,pyp,pdp=stats(childs[0],RYchild);am,Cm,pym,pdm=stats(childs[1],RYchild)
 ck(a==(ap+am)/2);ck(all(pd[s]==(pdp[s]+pdm[s])/2 for s in range(8)))
 ck(all(py[2*t]+py[2*t+1]==(pyp[t]+pym[t])/2 for t in range(2)))
 core={}
 for t,p in enumerate(py):
  ratio=RYchild[t>>1]/RY[t];ck(ratio>=1);addlog(core,p,ratio)
 flag=combine((1,h2(a)),(-R(1,2),h2(ap)),(-R(1,2),h2(am)))
 delta=combine((1,C),(-R(1,2),Cp),(-R(1,2),Cm))
 ck(delta==combine((1,core),(1,flag)))
 i=inf(F);ip=inf(childs[0]);im=inf(childs[1])
 ck(sum(i)==i[3]+(sum(ip)+sum(im))/2)
 # Complete signed K=6 budget identity is checked symbolically; rational
 # terms are separate from logarithmic terms, never inferred nonnegative.
 K=6;parent_r=K*sum(i);child_r=K*(sum(ip)+sum(im))/2
 ck(parent_r==child_r+K*i[3]);ck(combine((-1,C))==combine((-R(1,2),Cp),(-R(1,2),Cm),(-1,delta)))
 if delta:nonzero_signed+=1
 cases+=1
 if time.perf_counter()-start>55:raise RuntimeError('frozen55s history guard')
ck(cases==json.loads((RUN/'FROZEN_HISTORY_SPEC.json').read_text())['case_count'])
result={'status':'PASS','cases':cases,'exact_assertions':checks,'elapsed_seconds':time.perf_counter()-start,'arithmetic':'Fraction and exact prime-log coefficient maps','nonzero_reference_decrements':nonzero_signed,'query':'first physical core coordinate Y0','K_for_signed_identity':6,'positivity_claim':'No claim that K*Inf minus decrement is nonnegative','spec_sha256':hashlib.sha256((RUN/'FROZEN_HISTORY_SPEC.json').read_bytes()).hexdigest()}
(RUN/'out/HISTORY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
