"""Independent direct character sums and physical pivots, not FWHT."""
from fractions import Fraction as F
from pathlib import Path
import exact as E
import json,time,sys
R=Path(__file__).resolve().parents[1];start=time.perf_counter();count=0
def ck(x):
 global count
 assert x;count+=1
 assert time.perf_counter()-start<55
def ge(v):ck(not v or E.bounds(v)[0]>=0)
def calc(t):
 n=len(t).bit_length()-1;N=len(t);p={}
 for s in range(N):
  z=sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t))
  if z:p[s]=F(z*z,N*N)
 ck(sum(p.values())==1)
 ip=F(sum(sum(t[x]!=t[x^(1<<j)] for x in range(N)) for j in range(n)),N)
 iw=sum((s.bit_count()*w for s,w in p.items()),F(0));ck(ip==iw)
 return E.ent(p.values()),iw
def s4(t):
 h,i=calc(t);return E.add({2:4*i},E.scale(h,-1))
def cut(t,j,b):
 out=[]
 for x in range(len(t)):
  if (x>>j)&1==b:out.append(t[x])
 return tuple(out)
def leaves(t,sign,mode):
 # Each is a complete cylinder partition; policies differ with sign.
 if mode==0:return [(F(1,2),cut(t,sign,0)),(F(1,2),cut(t,sign,1))]
 if mode==1:
  if sign:return [(F(1),t)]
  return [(F(1,len(t)),(v,)) for v in t]
 j=2 if sign else 0
 a=cut(t,j,0);b=cut(t,j,1)
 return [(F(1,2),a),(F(1,4),cut(b,0,0)),(F(1,4),cut(b,0,1))]
pilot='--pilot' in sys.argv;tables=range(16) if pilot else range(256)
pairs=0;terminal=0
for mask in tables:
 t=tuple(1-2*((mask>>x)&1) for x in range(8));mu=F(sum(t),8)
 for mode in range(3):
  whole={};rhs={}
  for bit,s in [(0,1),(1,-1)]:
   ls=leaves(t,bit,mode);ck(sum(w for w,g in ls)==1)
   ck(sum((w*F(sum(g),len(g)) for w,g in ls),F(0))==mu)
   for w,g in ls:
    activation=tuple(s if not(x&1) else g[x>>1] for x in range(2*len(g)))
    sg=s4(g);sj=s4(activation);mg=F(sum(g),len(g));ge(sg)
    ge(E.add(sj,{2:2*s*mg},E.scale(sg,F(-1,2))))
    whole=E.add(whole,E.scale(sj,w/2));rhs=E.add(rhs,E.scale(sg,w/4));terminal+=1
  ge(E.add(whole,E.scale(rhs,-1)));ge(whole);pairs+=1
result=dict(status='PASS',Boolean_cores=len(tables),divergent_paired_policies=pairs,actual_terminals=terminal,direct_character_and_pivot_assertions=count,primitive_assertions=E.COUNT,runtime_seconds=time.perf_counter()-start,scope='Independent finite direct-character reconstruction of A049 paired-mean lemma; unbounded scope proved analytically')
(R/'out'/('PAIR_PILOT.json' if pilot else 'PAIR_AUDIT.json')).write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
