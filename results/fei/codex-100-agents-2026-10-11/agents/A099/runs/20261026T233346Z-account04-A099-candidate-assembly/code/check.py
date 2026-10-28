from pathlib import Path
from fractions import Fraction as F
import json, sys, time, hashlib
import exact as E
R=Path(__file__).resolve().parents[1]
START=time.monotonic(); count=0; queries=0; ghosts=0; floors=0; trees=0
def ck(x):
 global count
 count+=1
 assert x, count
 assert time.monotonic()-START<55, 'frozen 55 second cap'
def neg(x): return E.sc(-1,x)
def equal(x,y): ck(x==y)
def nonneg(x): ck(not x or E.bounds(x)[0]>=0)
def delete(w,j): return (w&((1<<j)-1))|((w>>(j+1))<<j)
def query(f,q,b,cs,ws,j,mode):
 global queries,ghosts
 p=E.spec(f); rp=E.marg(p,j); rq=E.marg(q,j)
 fs=[E.child(f,j,t) for t in [0,1]]; ps=[E.spec(h) for h in fs]
 equal(tuple((x+y)/2 for x,y in zip(*ps)),rp)
 kernels=[]
 for t in [0,1]:
  kernels.append(tuple(ps[t][u]/(2*x) if x else (F(1,2) if mode==0 else F(t==(u%2))) for u,x in enumerate(rp)))
 for u,x in enumerate(rp):
  equal(kernels[0][u]+kernels[1][u],1)
  if x==0 and rq[u]>0:ghosts+=1
 rs=[sum(x*k for x,k in zip(rq,K)) for K in kernels]
 equal(sum(rs),1)
 out=[]
 for t,K in enumerate(kernels):
  ck(rs[t]>=b/2>0)
  bb=b/(2*rs[t]); cc=tuple(c*K[delete(w,j)]/rs[t] for c,w in zip(cs,ws)); ww=tuple(delete(w,j) for w in ws)
  qq=tuple(x*k/rs[t] for x,k in zip(rq,K))
  equal(sum(qq),1);equal(bb+sum(cc),1)
  equal(qq,tuple(bb*ps[t][u]+sum(c for c,w in zip(cc,ww) if w==u) for u in range(len(rp))))
  out.append((fs[t],qq,bb,cc,ww))
 A=E.kl(p,q); children=E.sc(F(1,2),E.add(*(E.kl(ps[t],out[t][1]) for t in [0,1])))
 de=E.add(A,neg(E.kl(rp,rq))); do=E.kl((F(1,2),F(1,2)),tuple(rs))
 js=E.add(E.ent(rp),E.sc(F(-1,2),E.add(*(E.ent(x) for x in ps))))
 B=E.add(E.ent(p),neg(E.ent(rp)))
 equal(A,E.add(de,do,children))
 for x in [de,do,js,B]: nonneg(x)
 equal(E.add(B,E.sc(F(1,2),E.add(*(E.ce(ps[t],out[t][1]) for t in [0,1]))),neg(E.ce(p,q))),neg(E.add(js,de,do)))
 equal(E.sc(F(-1,2),E.add(*(E.logq(x[2]) for x in out))),E.add(neg(E.logq(b)),neg(do)))
 queries+=1
 return out,B,E.add(js,de,do),E.add(de,do),do
def tree(f,q,b,cs,ws,mode,depth=0):
 p=E.spec(f);n=len(f).bit_length()-1
 if not n or (depth==1 and f[0]<0):return E.ce(p,q),E.kl(p,q),neg(E.logq(b))
 out,B,releases,klrel,do=query(f,q,b,cs,ws,(depth+int(f[0]<0))%n,mode)
 vals=[tree(*child,mode,depth+1) for child in out]
 ce=E.add(B,releases,E.sc(F(1,2),E.add(*(v[0] for v in vals))))
 kl=E.add(klrel,E.sc(F(1,2),E.add(*(v[1] for v in vals))))
 blog=E.add(do,E.sc(F(1,2),E.add(*(v[2] for v in vals))))
 equal(ce,E.ce(p,q));equal(kl,E.kl(p,q));equal(blog,neg(E.logq(b)))
 return ce,kl,blog
def run(pilot):
 global floors,trees
 cap=2 if pilot else 3; tables=0
 for n in range(cap+1):
  N=1<<n
  for table in range(1<<N):
   tables+=1;f=tuple(1 if table&(1<<x) else -1 for x in range(N));p=E.spec(f)
   b=F(1,2);cs=(F(1,8),F(1,8),F(1,4));ws=(0,N-1,N-1)
   q=tuple(b*p[u]+sum(c for c,w in zip(cs,ws) if w==u) for u in range(N))
   for j in range(n):
    for mode in [0,1]:query(f,q,b,cs,ws,j,mode)
   if n<=2:
    for mode in [0,1]:tree(f,q,b,cs,ws,mode);trees+=1
 for den in ([8] if pilot else [8,12]):
  for rr in [F(0),F(1,4)]:
   t=1-rr
   for aa in range(1,den):
    a=F(aa,den)
    if not 0<a<t:continue
    for bi in range(1,den):
     bb=F(bi,den)
     for ei in range(bi+1,den):
      ell=F(ei,den)
      if not bb<ell<t:continue
      # Each cell includes a retained true-zero reference atom.
      p=(rr,a,F(0),t-a,F(0));q=(rr,bb/2,bb/2,(t-bb)/3,2*(t-bb)/3)
      z=max(a,ell);qz=(rr,z/2,z/2,(t-z)/3,2*(t-z)/3)
      delta=E.add(E.sc(a,E.logq(bb/z)),E.sc(t-a,E.logq((t-bb)/(t-z))))
      equal(delta,E.add(E.ce(p,qz),neg(E.ce(p,q))))
      equal(delta,E.sc(t,E.add(E.kl((a/t,1-a/t),(z/t,1-z/t)),neg(E.kl((a/t,1-a/t),(bb/t,1-bb/t))))))
      equal(-a*(t-z)+(t-a)*z,t*(z-a))
      # A finite grid check accompanies, and does not replace, convexity proof.
      for zz in [ell,(ell+t)/2,(ell+3*t)/4]:
       val=E.add(E.sc(a,E.logq(bb/zz)),E.sc(t-a,E.logq((t-bb)/(t-zz))))
       nonneg(E.add(val,neg(delta)))
      floors+=1
 # Explicit AND2 guard against omitted erasure in inherited marginal CE.
 f=(-1,1,1,1);p=E.spec(f);q=E.marg(p,0)
 change=E.add(E.sc(F(1,2),E.add(*(E.ce(E.spec(E.child(f,0,t)),q) for t in [0,1]))),neg(E.ce(p,p)))
 equal(change,{2:F(-1)})
 # Exact signed endpoint laws on an actual Boolean child.
 f=tuple(-1 if x in [0,7] else 1 for x in range(8));p=E.spec(E.child(f,0,0));equal(p,(F(1,4),)*4)
 target=(F(1,4),F(5,24),F(5,24),F(1,3))
 for incoming,ratio in [(p,F(27,25)),((F(1,4),F(5,16),F(5,16),F(1,8)),F(27,32))]:
  equal(E.add(E.ce(p,target),neg(E.ce(p,incoming))),E.sc(F(1,4),E.logq(ratio)))
 result=dict(status='PASS',exact_assertions=count,Boolean_tables=tables,local_queries_including_tree_checks=queries,ghost_row_observations=ghosts,adaptive_trees=trees,floor_profiles=floors,seconds=time.monotonic()-START,arithmetic='Fraction, exact prime-log cancellation and outward rational atanh bounds',scope='bounded checks plus analytic all-dimensional finite-tree proof; no universal initial source price')
 (R/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':run('--pilot' in sys.argv)
