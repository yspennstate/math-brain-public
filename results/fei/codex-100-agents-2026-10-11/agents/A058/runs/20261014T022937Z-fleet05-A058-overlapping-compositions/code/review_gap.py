import sys
sys.dont_write_bytecode=True
import arithmetic as a
from itertools import product,combinations
from fractions import Fraction as Q
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1];checks=0
def ck(v):
 global checks
 checks+=1
 assert v,checks
def main():
 start=time.perf_counter();n=3 if sys.argv[1]=='pilot' else 4
 monomials=[0]+[1<<i for i in range(n)]+[(1<<i)|(1<<j) for i,j in combinations(range(n),2)]
 roots=visits=0
 for code in range(1<<len(monomials)):
  v=tuple((-1)**(sum(bool(code&1<<j) and t&m==m for j,m in enumerate(monomials))%2) for t in range(1<<n))
  for assignment in product((-1,0,1),repeat=n):
   w=v
   for i in range(n-1,-1,-1):
    if assignment[i]>=0:w=a.restrict(w,i,assignment[i])
   visits+=1
   for i in range(len(w).bit_length()-1):
    d=a.inf(w,i);ck(d==0 or d>=Q(1,2))
  roots+=1
 # Point-defect suffix bound, verified with its exact displayed spectrum.
 for r in range(1,13):
  d=Q(1,1<<(r-1));e=() if r==1 else a.add(a.Phi((1-d)**2,d*d),((2,2*d*(1-d)),))
  ck(a.absle(e,3*d))
 out={'mode':sys.argv[1],'quadratic_roots':roots,'restricted_slices':visits,'exact_assertions':checks,'seconds':time.perf_counter()-start,'failures':0,'arithmetic':'integer truth values and exact Fraction influence; prime-log point-suffix certificates','scope':'A076 v4 stage4 derivative gap, not earlier bundled claims'}
 (ROOT/'out'/('review_'+sys.argv[1]+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
