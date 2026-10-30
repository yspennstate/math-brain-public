import sys
sys.dont_write_bytecode=True
import exact as e
from fractions import Fraction as Q
from pathlib import Path
import itertools,time,json
R=Path(__file__).resolve().parents[1]
def main(pilot):
 start=time.perf_counter();cases=live=0
 ids=[1,3,5,6] if pilot else range(16)
 for i,j in itertools.product(ids,repeat=2):
  A=tuple((i>>x)&1 for x in range(4));B=tuple((j>>x)&1 for x in range(4))
  p=Q(sum(A),4);q=Q(sum(B),4);mass=(1-p)*(1-q)
  for m,n in itertools.product([-1,0,1],repeat=2):
   cases+=1
   if not mass:continue
   live+=1
   E=e.walsh(tuple((1-A[a])*(1-B[b]) for b in range(4) for a in range(4)))
   K=e.walsh(tuple(m*A[a]+n*(1-A[a])*B[b] for b in range(4) for a in range(4)))
   moment={};law=[Q(0)]*3
   for t,(x,y) in enumerate(zip(E,K)):
    if not x:continue
    last=2 if t>>2 else 1 if t&3 else 0
    tail=[mass,1-q,Q(1)][last];w=x*x/mass;law[last]+=w
    for M in [-1,0,1]:e.ok(abs(y/x+M)<=3/tail,'arbitrary private prefix ratio')
    moment=e.add(moment,e.cost(tail),w/tail)
   e.ok(law==[mass,p*(1-q),q],'last-frequency distribution, arbitrary events')
   e.leconst(moment,1-mass,'universal log-tail moment')
 out={'status':'PASS','cases':cases,'positive_guard_cases':live,'assertions':e.checks,'elapsed_seconds':time.perf_counter()-start,'pilot':pilot}
 (R/'out'/('guard_pilot.json' if pilot else 'guard_validation.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main('--pilot' in sys.argv)
