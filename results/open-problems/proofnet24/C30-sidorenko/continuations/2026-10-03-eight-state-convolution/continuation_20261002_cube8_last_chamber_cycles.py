"""Exact cycle-surplus exploration for the remaining cube8 order chamber."""
from collections import Counter
from pathlib import Path
from fractions import Fraction
import json


def pack(n):return sum(v<<(4*i) for i,v in enumerate(n))
def unpack(n):return [(n>>(4*i))&15 for i in range(8)]
def multiply(P,Q):
 R=Counter()
 for a,u in P.items():
  for b,v in Q.items():R[a+b]+=u*v
 return {a:v for a,v in R.items() if v}
def power(P,n):
 R={0:1}
 for i in range(n):R=multiply(R,P)
 return R

def main():
 source=json.loads(Path(__file__).with_name('continuation_20261002_cube8_last_chamber.json').read_text())
 order=source['descending_order']
 gap={pack(tuple(map(int,n.split(',')))):c for n,c in source['gap_coefficients'].items()}
 mean={1<<(4*i):i+1 for i in range(8)}
 means={n:power(mean,n) for n in [9,11]}
 modes=[]
 for chi in range(1,8):
  sign=[(-1)**((chi&g).bit_count()) for g in order]
  coeff=[sum(sign[:i+1]) for i in range(8)]
  assert coeff[7]==0
  modes.append({1<<(4*i):c for i,c in enumerate(coeff) if c})
 E4=Counter();E6=Counter()
 for i,r in enumerate(modes):
  E4.update(power(r,4));E6.update(power(r,6))
 E4={a:c for a,c in E4.items() if c};E6={a:c for a,c in E6.items() if c}
 print('cycle terms',len(E4),len(E6),flush=True)
 V4=multiply(means[11],E4);V6=multiply(means[9],E6)
 g4=Counter(gap);g4.subtract({a:5*c for a,c in V4.items()})
 g4={a:c for a,c in g4.items() if c}
 g14=Counter(g4);g14.subtract({a:14*c for a,c in V6.items()})
 g14={a:c for a,c in g14.items() if c}
 out={'status':'exact cube8 last-chamber cycle exploration; audit pending',
      'fourth_gap_terms':len(g4),'fourth_gap_negative_terms':sum(c<0 for c in g4.values()),
      'fourteen_gap_terms':len(g14),'fourteen_gap_negative_terms':sum(c<0 for c in g14.values()),
      'E4_negative_terms':sum(c<0 for c in E4.values()),'E6_negative_terms':sum(c<0 for c in E6.values()),
      'fourth_negative_examples':[(unpack(a),c) for a,c in g4.items() if c<0][:30],
      'fourteen_negative_examples':[(unpack(a),c) for a,c in g14.items() if c<0][:30],
      'fourth_gap_coefficients':{','.join(map(str,unpack(a))):c for a,c in sorted(g4.items())},
      'fourteen_gap_coefficients':{','.join(map(str,unpack(a))):c for a,c in sorted(g14.items())}}
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
 print(json.dumps({k:v for k,v in out.items() if not k.endswith('coefficients')},indent=2))
if __name__=='__main__':main()
