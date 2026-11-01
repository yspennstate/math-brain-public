"""Actual nonuniform Boolean fixtures for the general projection inequality."""
from pathlib import Path
from fractions import Fraction as F
from math import prod
import sys,json,time
sys.dont_write_bytecode=True
import kernel as k
from check import plus,scale,log,hb,kl_atoms,bkl,C,LOGE_LO,serial
start=time.monotonic();rows=[]
for widths,phase in [([2],0),([3],0),([4],0),([2,3],0),([3,3],0),([3,4],0),([4,4],0),([3],1),([4],1)]:
 n=sum(widths);N=1<<n;truth=[]
 for x in range(N):
  offset=0;bit=0
  for w in widths:bit^=int(((x>>offset)&((1<<w)-1))==0);offset+=w
  truth.append(bit ^ (phase*(x.bit_count()%2)))
 truth=bytes(truth);walsh=k.walsh(truth);p={s:F(v*v,N*N) for s,v in enumerate(walsh)}
 marg=[sum(v for s,v in p.items() if s&(1<<j)) for j in range(n)]
 for j,d in enumerate(marg):
  a,b=k.children(truth,j);k.check(d==F(sum(x!=y for x,y in zip(a,b)),len(a)))
 q={s:prod(d if s&(1<<j) else 1-d for j,d in enumerate(marg)) for s in p}
 k.check(sum(p.values())==sum(q.values())==1 and p[0]>=q[0] and all(0<d<1 for d in marg))
 H=plus(*(scale(log(v),-v) for v in p.values() if v));M=plus(*(hb(d) for d in marg));TC=k.sub(M,H);I=sum(marg)
 for lam in [F(1),F(1,2),F(1,4)]:
  z=sum(lam**s.bit_count()*v for s,v in q.items() if s)
  shape={s:lam**s.bit_count()*v/z for s,v in q.items() if s}
  k.check(sum(shape.values())==1)
  mean=sum(s.bit_count()*v for s,v in shape.items());k.check(mean<=I/(1-p[0]))
  for empty in [q[0],p[0]]:
   R={s:(empty if s==0 else (1-empty)*shape[s]) for s in p};k.check(sum(R.values())==1)
   K=kl_atoms(p,R);T=k.sub(TC,K);bound=bkl(p[0],q[0]);k.check(F(T[1],k.SCALE)<LOGE_LO*I)
   if lam==1 and (empty==p[0] or p[0]==q[0]):
    diff=k.sub(T,bound);k.check(diff[0]<=0<=diff[1]) # diagnostic of proved chain equality
   else:k.check(T[1]<bound[0])
   rows.append({'widths':widths,'parity_shift':phase,'lambda':lam,'empty':empty,'p0':p[0],'q0':q[0],'marginals':marg,'I':I,'K':K,'TC':TC,'T':T,'binary_bound':bound})
 k.check(time.monotonic()-start<55)
out={'rows':rows,'cases':len(rows),'assertions':k.ASSERTIONS,'seconds':time.monotonic()-start,'scope':'general projection only; no post-query common-attenuation claim'}
r=Path(__file__).resolve().parents[1];(r/'out/GENERAL.json').write_text(json.dumps(serial(out),indent=2),encoding='utf-8');print(json.dumps({s:out[s] for s in ['cases','assertions','seconds']}))
