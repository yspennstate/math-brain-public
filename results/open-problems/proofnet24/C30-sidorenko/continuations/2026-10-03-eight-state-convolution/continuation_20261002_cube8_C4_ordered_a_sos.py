"""Exact sufficient SOS certificate for C4 after ordering quotient a."""
from pathlib import Path
import json
from collections import Counter,defaultdict
from math import comb
from fractions import Fraction


def pack(n):return sum(v<<(4*i) for i,v in enumerate(n))
def unpack(n):return [(n>>(4*i))&15 for i in range(8)]
def shear(P,i,j):
 Q=Counter()
 for n,c in P.items():
  a=(n>>(4*i))&15
  for k in range(a+1):Q[n-(k<<(4*i))+(k<<(4*j))]+=c*comb(a,k)
 return {n:c for n,c in Q.items() if c}

def main():
 F=json.loads(Path(__file__).with_name('continuation_20261002_cube8_C4_host_sos.json').read_text())['host_polynomial']
 P={pack(tuple(map(int,n.split(',')))):c for n,c in F.items()}
 for i,j in [(0,2),(2,4),(4,6)]:P=shear(P,i,j)
 Q=defaultdict(dict)
 for raw,c in P.items():
  n=tuple(unpack(raw));Q[n[::2]][n[1::2]]=c
 partitions=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
 failed=[];records=[]
 for a,q in Q.items():
  gamma=q.get((1,1,1,1),0);budget=0;terms=[]
  for pair,other in partitions:
   exponent=lambda ids:tuple(2 if i in ids else 0 for i in range(4))
   c=q.get(exponent(pair),0);d=q.get(exponent(other),0)
   budget+=2*min(c,d);terms.append([c,d])
  rec={'a_diff_exponents':a,'gamma':gamma,'simple_sos_budget':budget,'paired_coefficients':terms}
  records.append(rec)
  if gamma>budget:failed.append(rec)
 out={'status':'exact ordered-a simple SOS test, no positivity assertion if failed',
      'quartic_coefficient_count':len(Q),'failed_count':len(failed),'failed':failed,'records':records,
      'polynomial':{','.join(map(str,unpack(n))):c for n,c in sorted(P.items())}}
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
 print({'quartics':len(Q),'failed_count':len(failed),'first_failures':failed[:5]})
if __name__=='__main__':main()
