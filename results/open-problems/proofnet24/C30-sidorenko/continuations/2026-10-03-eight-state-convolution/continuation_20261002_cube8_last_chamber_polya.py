"""Exact Pólya multiplier exploration of the cube8 exceptional chamber."""
from pathlib import Path
from collections import Counter
import json


def unpack(n):return [(n>>(6*i))&63 for i in range(8)]
def main():
 source=json.loads(Path(__file__).with_name('continuation_20261002_cube8_last_chamber.json').read_text())
 P={sum(v<<(6*i) for i,v in enumerate(map(int,n.split(',')))):c for n,c in source['gap_coefficients'].items()}
 out={'status':'exact multiplier exploration, audit pending','multiplier':'d0+d1+d2+d3+d4+d5+d6','steps':[]}
 for step in range(1,9):
  Q=Counter()
  for n,c in P.items():
   for i in range(7):Q[n+(1<<(6*i))]+=c
  P={n:c for n,c in Q.items() if c}
  negatives=[(n,c) for n,c in P.items() if c<0]
  rec={'power':step,'terms':len(P),'negative_terms':len(negatives),
       'negative_examples':[(unpack(n),c) for n,c in negatives[:10]]}
  out['steps'].append(rec);print(step,len(P),len(negatives),flush=True)
  if not negatives:
   out['certificate_coefficients']={','.join(map(str,unpack(n))):c for n,c in sorted(P.items())};break
  Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
if __name__=='__main__':main()
