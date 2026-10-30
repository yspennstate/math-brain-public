from fractions import Fraction as F
from pathlib import Path
import sys,json,time
import exact as E
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(v):
 global checks
 checks+=1;assert v,checks
 assert time.perf_counter()-start<55
def KL(p,q):return E.kl(p,[E.iv(x) for x in q])
def point(w):return [1]*((1<<w)-1)+[-1]
def qfactor(t,alpha):
 p=E.law(t)
 if len(t)<=2 or abs(sum(t))==len(t):return p
 q=[p[0]]+[(1-alpha)*x for x in p[1:]];q[-1]+=alpha*(1-p[0]);ck(sum(q)==1);return q
def tensor(a,b):return [x*y for y in b for x in a]
def lift(v,u,epsilon,qv,qu):
 g=[a*b for b in u for a in v];t=[epsilon if not z&1 else g[z>>1] for z in range(2*len(g))]
 p=E.law(t);q=[F(0)]*len(t);q[0:2]=p[0:2];core=tensor(qv,qu)
 for s in range(1,len(core)):q[2*s]=q[2*s+1]=core[s]/4
 ck(sum(q)==1);ck(all((pp==0)==(qq==0) for pp,qq in zip(p,q)))
 return t,q
def step(t,q,i):
 p=E.law(t);ts=[E.restrict(t,i,y) for y in [0,1]];ps=[E.law(z) for z in ts]
 pp=[p[k]+p[k|(1<<i)] for k in range(len(p)) if not k>>i&1]
 qq=[q[k]+q[k|(1<<i)] for k in range(len(q)) if not k>>i&1]
 ck(pp==[(a+b)/2 for a,b in zip(*ps)])
 joint=[[qq[k]*(ps[y][k]/(2*pp[k]) if pp[k] else F(1,2)) for k in range(len(pp))] for y in [0,1]]
 outs=[sum(a) for a in joint];ck(sum(outs)==1);child=[[a/outs[y] for a in joint[y]] for y in [0,1]]
 ck(all(sum(a)==1 for a in child))
 loss=E.sub(KL(p,q),KL(pp,qq));out=KL([F(1,2)]*2,outs)
 old=E.scale(F(1,2),E.total(KL(a,b) for a,b in zip(ps,child)))
 ck(E.overlaps(KL(p,q),E.add(loss,E.add(out,old))))
 return ts,ps,child,outs,loss,out

