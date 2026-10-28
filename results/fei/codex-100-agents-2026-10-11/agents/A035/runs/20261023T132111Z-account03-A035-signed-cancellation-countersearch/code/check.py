from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time,hashlib,sys
R=Path(__file__).resolve().parents[1];(R/'out').mkdir(exist_ok=True);N=0
def ck(x):
 global N
 assert x;N+=1
def fw(v):
 v=v[:];s=1
 while s<len(v):
  for b in range(0,len(v),2*s):
   for j in range(s):a,c=v[b+j],v[b+j+s];v[b+j]=a+c;v[b+j+s]=a-c
  s*=2
 return v
def parts(n):
 if n==0:yield [];return
 for p in parts(n-1):
  yield p+[[n-1]]
  for j in range(len(p)):yield p[:j]+[p[j]+[n-1]]+p[j+1:]
def criterion(ps,m,blocks,rs):
 for B in blocks:
  a=[sum(ps[t][i] for i in B) for t in [0,1]];r=[sum(rs[t][i] for i in B) for t in [0,1]]
  if a[0] and a[1]:
   if any(r[0]*ps[0][i]/a[0]+r[1]*ps[1][i]/a[1]!=2*m[i] for i in B):return False
  elif any(a):
   t=0 if a[0] else 1
   if any(r[t]*ps[t][i]/a[t]>2*m[i] for i in B):return False
 return True
def reconstruct(ps,m,blocks,rs):
 q=[[F(0)]*4 for _ in [0,1]]
 for B in blocks:
  a=[sum(ps[t][i] for i in B) for t in [0,1]];r=[sum(rs[t][i] for i in B) for t in [0,1]]
  if a[0] and a[1]:
   for t in [0,1]:
    for i in B:q[t][i]=r[t]*ps[t][i]/a[t]
  elif any(a):
   t=0 if a[0] else 1
   for i in B:q[t][i]=r[t]*ps[t][i]/a[t];q[1-t][i]=2*m[i]-q[t][i]
  else:
   mass=sum(m[i] for i in B)
   for i in B:q[0][i]=r[0]*m[i]/mass;q[1][i]=2*m[i]-q[0][i]
 return all(v>=0 for row in q for v in row) and all(q[0][i]+q[1][i]==2*m[i] for i in range(4)) and all(sum(q[t][i] for i in B)==sum(rs[t][i] for i in B) for t in [0,1] for B in blocks)
def main():
 start=time.monotonic();pilot='--pilot' in sys.argv;domain=range(16) if pilot else range(256)
 spec=dict(helper='A035-mismatched-mean-v1',sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),family='ALL actual Boolean3-bit truth tables as physical splits',domain=[0,15] if pilot else [0,255],case_count=(16 if pilot else 256)*15*3*2,symmetry='None; labelled tables, all15 partitions',arithmetic='Integer FWHT/direct characters, exact Fractions; rational KKT and integer power log signs',memory_estimate_MB=60,max_runtime_seconds=55)
 (R/'out'/('PILOT_SPEC.json' if pilot else 'FROZEN_SPEC.json')).write_text(json.dumps(spec,indent=2),encoding='utf-8')
 yes=no=cases=0
 for table in domain:
  truth=[1 if table>>i&1 else -1 for i in range(8)];a=fw(truth)
  direct=[sum(v*(-1)**((S&i).bit_count()) for i,v in enumerate(truth)) for S in range(8)];ck(a==direct)
  for U in range(8):ck(sum(a[S]*a[S^U] for S in range(8))==64*int(U==0))
  amp=[fw([truth[2*y+t] for y in range(4)]) for t in [0,1]];ps=[[F(v*v,16) for v in row] for row in amp]
  for S in range(4):ck((F(a[2*S],8)+F(a[2*S+1],8))==F(amp[0][S],4));ck((F(a[2*S],8)-F(a[2*S+1],8))==F(amp[1][S],4))
  mid=[(ps[0][i]+ps[1][i])/2 for i in range(4)]
  for lam in [F(0),F(1,2),F(3,4)]:
   m=[lam*mid[i]+(1-lam)/4 for i in range(4)]
   for shift in [False,True]:
    plus=m[:]
    if shift:eps=min(m[0],m[1])/2;plus[0]+=eps;plus[1]-=eps
    rs=[plus,[2*m[i]-plus[i] for i in range(4)]]
    for B in parts(4):
     # Explicit feasible positive full target and independently assembled equality candidate.
     q=[[F(0)]*4 for _ in [0,1]]
     for block in B:
      mass=sum(m[i] for i in block)
      for t in [0,1]:
       r=sum(rs[t][i] for i in block)
       for i in block:q[t][i]=r*m[i]/mass
     ck(all(q[t][i]>0 for t in [0,1] for i in range(4)));ck(all(q[0][i]+q[1][i]==2*m[i] for i in range(4)))
     v=criterion(ps,m,B,rs);ck(v==reconstruct(ps,m,B,rs));yes+=v;no+=not v;cases+=1
  ck(time.monotonic()-start<55)
 # Actual Boolean witness and exact globally supporting gradient.
 p=[[F(1,4)]*4,[F(0),F(1),F(0),F(0)]];m=[F(1,4)]*4;blocks=[[0,1],[2,3]]
 opt=[[F(5,12),F(1,12),F(1,4),F(1,4)],[F(1,12),F(5,12),F(1,4),F(1,4)]]
 ck(all(sum(row)==1 for row in opt));ck(all(opt[0][i]+opt[1][i]==2*m[i] for i in range(4)))
 for row in opt:ck([sum(row[i] for i in B) for B in blocks]==[F(1,2),F(1,2)])
 grad=[-p[0][i]/opt[0][i]+p[1][i]/opt[1][i] for i in range(4)];ck(grad==[F(-3,5),F(-3,5),F(-1),F(-1)])
 ck(186624>16*3125);ck(186624<256*3125)
 witness=dict(actual_child_p=[[str(x) for x in row] for row in p],inherited_m=[str(x) for x in m],optimizer=[[str(x) for x in row] for row in opt],gradient=[str(x) for x in grad],coarse_KL='1/2',fine_minimum='log2(186624/3125)/8',strict_fine_gap='186624>16*3125',complete_transaction='fine_minimum - JS - D(actual_midpoint||m) = fine_minimum-1 <0',net_sign='186624<256*3125',scope='Old actual-midpoint criterion would pass no coarse-shift test here, but its stated hypothesis fails; A033 not refuted')
 (R/'out/WITNESS.json').write_text(json.dumps(witness,indent=2),encoding='utf-8')
 ans=dict(cases=cases,attainable=yes,strict_fine_gap=no,checks=N,seconds=time.monotonic()-start)
 (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(ans,indent=2),encoding='utf-8');print(json.dumps(ans))
if __name__=='__main__':main()
