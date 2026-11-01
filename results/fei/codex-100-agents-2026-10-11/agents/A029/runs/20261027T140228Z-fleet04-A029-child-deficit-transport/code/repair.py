from pathlib import Path
from fractions import Fraction as R
from functools import lru_cache
import json,time
r=Path(__file__).resolve().parents[1];start=time.monotonic();checks=nodes=calibs=0
def ck(b):
 global checks
 checks+=1
 if not b:raise AssertionError(checks)
 if time.monotonic()-start>55:raise TimeoutError('frozen cap')
@lru_cache(maxsize=4096)
def spectrum(t):
 a=list(t);j=1
 while j<len(a):
  for k in range(0,len(a),2*j):
   for z in range(j):x,y=a[k+z],a[k+z+j];a[k+z],a[k+z+j]=x+y,x-y
  j*=2
 return tuple(R(x*x,len(a)**2) for x in a)
def restrict(t,i,b):return tuple(v for x,v in enumerate(t) if (x>>i)&1==b)
def erase(p,i):
 q=[R(0)]*(len(p)//2)
 for x,v in enumerate(p):q[(x&((1<<i)-1))|((x>>(i+1))<<i)]+=v
 return q
def walk(t,q,policy,depth=0):
 global nodes,calibs
 nodes+=1;p=spectrum(t);V={0}|{i for i in range(1,len(p)) if p[i]}
 ck(sum(p)==sum(q)==1);ck(all(x>=0 for x in q));ck(all(q[i]>0 for i,x in enumerate(p) if x))
 ck(all(a^b in V for a in V for b in V))
 ck(all(q[i]==0 for i in range(len(q)) if i not in V))
 vals={q[i] for i in V if i};ck(len(vals)<=1)
 if len(V)==1:ck(q[0]==1)
 if (policy==1 and depth==1) or (policy==2 and depth>=2 and depth%2==0):
  rho=p[0]
  new=[R(1)]+[R(0)]*(len(q)-1) if rho==1 else [rho]+[(1-rho)*a/(1-q[0]) for a in q[1:]]
  ck(tuple(new)==p);q=new;calibs+=1
 if len(t)==1:return
 n=len(t).bit_length()-1;i=0 if policy==0 else n-1 if policy==1 else abs(sum(t))%n
 mp=erase(p,i);mq=erase(q,i);children=[]
 for b in [0,1]:
  tc=restrict(t,i,b);pc=spectrum(tc)
  raw=[mq[j]*pc[j]/(2*mp[j]) if mp[j] else mq[j]/2 for j in range(len(mp))]
  z=sum(raw);ck(z>0);qc=[a/z for a in raw]
  ck(sum(qc)==1)
  for j in range(len(mp)):
   if mp[j]:ck(mp[j]*(pc[j]/(2*mp[j]))==pc[j]/2)
  children.append((tc,qc,z))
 ck(children[0][2]+children[1][2]==1)
 for tc,qc,z in children:walk(tc,qc,policy,depth+1)
trees=0
for m in [2,3,4]:
 L=2**m;N=L*L;t=tuple(-1 if x%(2**m)==x//(2**m) else 1 for x in range(N))
 A=R((L-2)**2,(L-2)**2+1);D=A+R(4*(L-1),5);q=[R(0)]*N
 for s in range(L):q[s+L*s]=A/D if s==0 else R(4,5)/D
 lam=R(4*L,5)/D;c=(A-R(4,5))/D
 ck(lam+c==1);ck(all(q[i]==(lam/L if i%(L+1)==0 else 0)+(c if i==0 else 0) for i in range(N)))
 for policy in range(3):walk(t,q,policy);trees+=1
out={'status':'PASS','complete_G_subtrees':trees,'nodes':nodes,'vacuum_calibrations':calibs,'exact_assertions':checks,'seconds':time.monotonic()-start,'scope':'H sibling held as full inherited terminal; no main helper imports'}
(r/'out/repair.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
