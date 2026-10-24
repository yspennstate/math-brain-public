"""Exact colored-cycle partial Walsh polynomial; exploratory signs only."""
from pathlib import Path
from collections import Counter
from math import comb
import json


def pack(n):return sum(v<<(4*i) for i,v in enumerate(n))
def unpack(n):return [(n>>(4*i))&15 for i in range(8)]
def butterfly(P,i,j):
 Q=Counter(); mask=~((15<<(4*i))|(15<<(4*j)))
 for n,v in P.items():
  a=(n>>(4*i))&15;b=(n>>(4*j))&15;rest=n&mask
  for k in range(a+b+1):
   c=sum(comb(a,l)*comb(b,k-l)*(-1)**(k-l) for l in range(max(0,k-b),min(a,k)+1))
   if c:Q[rest+((a+b-k)<<(4*i))+(k<<(4*j))]+=c*v
 return {n:v for n,v in Q.items() if v}

def main():
 F=json.loads(Path(__file__).with_name('continuation_20261002_cube8_flow_and_smoothing.json').read_text())['Fourier_polynomial']
 records={}
 for k in [4,6,8,10]:
  P={pack(tuple(map(int,n.split(',')))):c for n,c in F.items() if sum(tuple(map(int,n.split(',')))[1::2])==k}
  for i,j in [(0,2),(4,6),(0,4),(2,6)]:P=butterfly(P,i,j)
  records[str(k)]={'nonzero_terms':len(P),'negative_terms':sum(v<0 for v in P.values()),
                   'polynomial':{','.join(map(str,unpack(n))):v for n,v in sorted(P.items())}}
  print(k,len(P),records[str(k)]['negative_terms'],flush=True)
 Path(__file__).with_suffix('.json').write_text(json.dumps({'status':'exact partial-Walsh exploratory polynomial, no positivity claim','records':records},indent=2))
if __name__=='__main__':main()
