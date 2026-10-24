from pathlib import Path
import json
from joint_boundary import parts,admissible,orbit
r=json.loads(Path('joint_R2.json').read_text());rows={tuple(s['tokens']):s['weight'] for s in r['states']}
def canon_plain(labels):
 d={};return tuple(d.setdefault(v,len(d)) for v in labels)
for tok,counts in rows.items():
 labels=tuple(v>>1 for v in tok);flags=tuple(v&1 for v in tok);marked=sorted({labels[i] for i in range(4) if flags[i]});want=set()
 for pa in parts(len(marked)):
  merged={b:('boundary',pa[j]) for j,b in enumerate(marked)}
  p=canon_plain([merged.get(b,('unmarked',b)) for b in labels])
  if orbit(p)!='cross':want.add(p)
 assert want==set(admissible(labels,flags))
 for rot in range(4):
  for sgn in [-1,1]:
   perm=[(rot+sgn*i)%4 for i in range(4)];newlab=canon_plain([labels[i] for i in perm]);newtok=tuple(2*newlab[j]+flags[perm[j]] for j in range(4))
   assert rows[newtok]==counts
report=json.loads(Path('joint_verification.json').read_text());report.update({'admissible_sets_independent_boundary_block_partition_generator':'PASS: all 80 states','finite_joint_law_D4_covariance':'PASS: all 8 permutations of all 80 arrays'});Path('joint_verification.json').write_text(json.dumps(report,indent=2),encoding='utf8');print(report)
# A stationarity/positive-definiteness diagnostic: even a genuine stationary
# random equivalence relation can pass the first comparison and fail the next.
from fractions import Fraction as F
v=[F(3,8)+F(3,8)*int(n%3==0)+F(1,4)*F(1,2)**n for n in [1,2,3]];assert v==[F(1,2),F(7,16),F(25,32)]
Path('bootstrap_obstruction.json').write_text(json.dumps({'tau_1':str(v[0]),'tau_2':str(v[1]),'tau_3':str(v[2]),'model':'Mixture: probability 3/8 one universal equivalence block; 3/8 congruence-mod-3 blocks; 1/4 independent p=1/2 percolation on Z. This is not Z^2 nearest-neighbour percolation.'},indent=2),encoding='utf8')
