"""Exact simple quartic SOS test for every host-a coefficient of C4."""
import json
from pathlib import Path
from collections import Counter,defaultdict
from math import comb
from fractions import Fraction


def pack(n):return sum(v<<(4*i) for i,v in enumerate(n))
def unpack(n):return [(n>>(4*i))&15 for i in range(8)]
def butterfly(P,i,j):
 Q=Counter();mask=~((15<<(4*i))|(15<<(4*j)))
 for n,v in P.items():
  a=(n>>(4*i))&15;b=(n>>(4*j))&15;rest=n&mask
  for k in range(a+b+1):
   c=sum(comb(a,l)*comb(b,k-l)*(-1)**(k-l) for l in range(max(0,k-b),min(a,k)+1))
   if c:Q[rest+((a+b-k)<<(4*i))+(k<<(4*j))]+=v*c
 return {n:c for n,c in Q.items() if c}

def main():
 F=json.loads(Path(__file__).with_name('continuation_20261002_cube8_colored_partial_walsh.json').read_text())['records']['4']['polynomial']
 P={pack(tuple(map(int,n.split(',')))):c for n,c in F.items()}
 for i,j in [(1,3),(5,7),(1,5),(3,7)]:P=butterfly(P,i,j)
 assert all(c>0 for c in P.values())
 Q=defaultdict(dict)
 for raw,c in P.items():
  n=tuple(unpack(raw));Q[n[::2]][n[1::2]]=c
 partitions=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
 records=[];failed=[]
 for a,q in Q.items():
  assert all(all(v%2==0 for v in b) or b==(1,1,1,1) for b in q)
  gamma=q.get((1,1,1,1),0);budget=0
  terms=[]
  for pair,other in partitions:
   def exponent(ids):return tuple(2 if i in ids else 0 for i in range(4))
   c=q.get(exponent(pair),0);d=q.get(exponent(other),0)
   budget+=2*min(c,d);terms.append([c,d])
  record={'host_a_exponents':a,'gamma':gamma,'simple_sos_budget':budget,'paired_coefficients':terms}
  records.append(record)
  if gamma>budget:failed.append(record)
 out={'status':'exact simple SOS sufficient test','host_polynomial_terms':len(P),
      'coefficient_quartic_count':len(Q),'failed_count':len(failed),'failed':failed,'records':records,
      'host_polynomial':{','.join(map(str,unpack(n))):c for n,c in sorted(P.items())}}
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
 print(json.dumps({k:v for k,v in out.items() if k not in ['records','host_polynomial']},indent=2))
if __name__=='__main__':main()
