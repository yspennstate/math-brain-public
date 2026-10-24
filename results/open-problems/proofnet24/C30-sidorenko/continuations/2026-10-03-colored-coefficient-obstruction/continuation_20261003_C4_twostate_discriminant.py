"""Exact generic two-state C4 quartic and paired-term discriminant."""
from pathlib import Path
from collections import Counter,defaultdict
import itertools,json


def multiply(P,Q):
 R=Counter()
 for a,c in P.items():
  for b,d in Q.items():R[tuple(a[i]+b[i] for i in range(3))]+=c*d
 return {a:c for a,c in R.items() if c}

def encode(P):return {','.join(map(str,n)):c for n,c in sorted(P.items()) if c}
def main():
 edges=[(i,5+j) for i in range(5) for j in range(5) if (j-i)%5 in [0,1,4]]
 selected={(0,5),(0,6),(1,5),(1,6)};F=Counter();entry={(0,0):0,(0,1):1,(1,1):2}
 for labels in itertools.product(range(2),repeat=10):
  n=[0]*6
  for i,j in edges:
   u,v=sorted((labels[i],labels[j]));h=entry[u,v]+(3 if (i,j) in selected else 0);n[h]+=1
  F[tuple(n)]+=1
 Q=defaultdict(Counter)
 for n,c in F.items():Q[n[3:]][n[:3]]=c
 c=Q[(2,2,0)];d=Q[(0,2,2)];e=Q[(1,2,1)]
 D=Counter({a:4*v for a,v in multiply(c,d).items()});D.subtract(multiply(e,e));D={a:v for a,v in D.items() if v}
 out={'status':'exact generic two-state colored C4 quartic paired-term test','raw_polynomial':encode(F),
      'quartic_coefficients':{','.join(map(str,n)):encode(P) for n,P in Q.items()},
      'four_cd_minus_e_squared':encode(D),'determinant_negative_coefficients':sum(v<0 for v in D.values()),
      'determinant_terms':len(D),'minimum_exponents':tuple(min(n[i] for n in D) for i in range(3))}
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
 print({k:v for k,v in out.items() if k not in ['raw_polynomial','quartic_coefficients','four_cd_minus_e_squared']})
 print('negative examples',[(n,v) for n,v in D.items() if v<0][:5])
if __name__=='__main__':main()
