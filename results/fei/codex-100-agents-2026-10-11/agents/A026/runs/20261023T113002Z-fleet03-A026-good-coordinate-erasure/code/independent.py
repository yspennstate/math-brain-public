from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import time,json
R=Path(__file__).resolve().parents[1];start=time.monotonic();count=0
def ck(x):
 global count
 assert x,count;count+=1
 assert time.monotonic()-start<55
@lru_cache(None)
def four(v):
 return tuple(sum(x*(-1 if (s&t).bit_count()%2 else 1) for t,x in enumerate(v))/F(len(v)) for s in range(len(v)))
def sq(v):return tuple(x*x for x in four(tuple(v)))
def ins(x,j,b):return (x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)
def child(v,j,b):return tuple(v[ins(x,j,b)] for x in range(len(v)//2))
def marginal(v,j):return tuple(v[ins(x,j,0)]+v[ins(x,j,1)] for x in range(len(v)//2))
def make(a,g,h):return tuple((g if a[u]==1 else h)[t] for t in range(len(g)) for u in range(len(a)))
def blocks(Q,c):return tuple(Q[c*t] for t in range(len(Q)//c)),tuple(sum(Q[c*t+1:c*t+c]) for t in range(len(Q)//c))
def reset(Q,c,b):
 x,y=blocks(Q,c);return tuple(x[t] if u==0 else y[t]*b[u-1] for t in range(len(x)) for u in range(c))
def physical(v,Q,j,D=None,c=None,A=None):
 P=sq(v);mp=marginal(P,j);mq=marginal(Q,j);out=[];rho=[]
 for z in (0,1):
  pz=sq(child(v,j,z));k=[p/(2*m) if m else F(1,2) for p,m in zip(pz,mp)]
  if A is not None:
   nc=len(A)//2;am=marginal(sq(A),j);ap=sq(child(A,j,z))
   for i in range(len(k)):
    u=i%nc
    if u:
     kval=ap[u]/(2*am[u]) if am[u] else F(1,2)
     if mp[i]:ck(k[i]==kval)
     k[i]=kval
  if D is not None:
   dk=j-(c.bit_length()-1);dm=marginal(sq(D),dk);dp=sq(child(D,dk,z))
   for i in range(len(k)):
    if i%c:
     kval=dp[i//c]/(2*dm[i//c]) if dm[i//c] else F(1,2)
     if mp[i]:ck(k[i]==kval)
     k[i]=kval
  joint=tuple(x*y for x,y in zip(mq,k));r=sum(joint);rho.append(r);out.append(tuple(x/r for x in joint))
 ck(sum(rho)==1);return out,rho
rows=[]
for m in (1,2):
 M=1<<(m+2);ch=((1<<m)-1)<<2
 g=tuple(-1 if (t>>2).bit_count()%2 else 1 for t in range(M))
 h=tuple(g[t]*(1 if t%4==0 else -1) for t in range(M));D=tuple(F(x-y,2) for x,y in zip(g,h))
 aa=tuple(-1 if u<3 else 1 for u in range(8));v=make(aa,g,h);P=sq(v)
 pg,ph=sq(g),sq(h);pi0=sq(aa);pi=tuple(x/(1-pi0[0]) for x in pi0[1:])
 rg=tuple(F(8,5*M-12) if t==ch else F(0) if (t>>2)==(ch>>2) else F(5,5*M-12) for t in range(M))
 rh=(F(1,M),)*M;ck(sum(rg)==sum(rh)==1)
 qt=tuple(F(5,8)*x+F(3,8)*y for x,y in zip(pg,ph));rr=tuple(F(5,8)*x+F(3,8)*y for x,y in zip(rg,rh))
 Q=tuple(rr[t]*(P[8*t+u]/qt[t] if qt[t] else F(u==0)) for t in range(M) for u in range(8));ck(sum(Q)==1)
 for theta in (F(1,8),F(3,16)):
  bt=tuple((1-theta)*x+theta/F(7) for x in pi);qb=reset(Q,8,bt)
  for j in (0,1):
   children,rho=physical(v,qb,j)
   for z in (0,1):
    a=child(aa,j,z);pa=sq(a);pic=tuple(x/(1-pa[0]) for x in pa[1:]);q0,q1=blocks(children[z],4)
    t=next(i for i,x in enumerate(q1) if x);carry=tuple(x/q1[t] for x in children[z][4*t+1:4*t+4]);ck(reset(children[z],4,carry)==children[z])
    if z==0:ck(carry==pic)
    if z==1:ck(pic==(F(1,3),)*3)
    fresh=tuple(F(255,256)*x+F(1,768) for x in pic);qq=reset(children[z],4,fresh);vc=make(a,g,h)
    for k in range(m+2):
     new,rs=physical(vc,qq,2+k,D,4);base,rb=physical(vc,reset(children[z],4,pic),2+k,D,4);ck(rs==rb)
     for b in (0,1):ck(new[b]==reset(base[b],4,fresh))
    for j2 in (0,1):
     second,rr=physical(vc,qq,j2,A=a)
     for b in (0,1):
      x,y=blocks(second[b],2);t=next((t for t,v in enumerate(y) if v),None)
      if t is not None:
       bb=(second[b][2*t+1]/y[t],);ck(bb==(F(1),));ck(reset(second[b],2,bb)==second[b])
    rows.append({'m':m,'theta':str(theta),'controller':j,'outcome':z,'actual_rho':list(map(str,rho))})
ck(16807**144*384**384 < 2**17*15606**144*383**384)
ck(16807**144*2048**1536 < 2**17*15606**144*2047**1536)
ck(F(45,2576)-F(17,1024)==F(143,164864))
out={'status':'PASS','method':'independent direct character sums, analytic source-reference reconstruction; no main/helper imports','assertions':count,'controller_children':len(rows),'seconds':time.monotonic()-start,'rows':rows}
(R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
