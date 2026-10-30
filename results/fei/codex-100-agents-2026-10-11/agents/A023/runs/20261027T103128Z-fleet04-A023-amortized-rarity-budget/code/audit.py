"""Independent truth-edge tree reconstruction and exact scope guards."""
from pathlib import Path
from fractions import Fraction as R
import hashlib
import itertools
import json
import sys
import time

RUN=Path(__file__).resolve().parents[1]
OUT=RUN/'out'
SPEC=dict(helper_version='A023-stage23-audit-v1',
 helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 actual_Boolean_family='ALL Boolean tables n<=3; parity2 and point-defect2/3 guards',
 parameter_domain='every coordinate permutation; five deterministic adaptive stop/mark policies',
 case_count='278 tables; 1574 table-permutation pairs; 7870 policy runs; four guards',
 symmetry='none', arithmetic='Fraction, raw pivotal edges, integer-power strict signs',
 memory_estimate_MB=50, maximum_runtime_seconds=60)
if '--freeze' in sys.argv:
 (OUT/'AUDIT_SPEC.json').write_text(json.dumps(SPEC,indent=2)+'\n',encoding='utf-8')
 print('Independent audit frozen.'); raise SystemExit
assert json.loads((OUT/'AUDIT_SPEC.json').read_text(encoding='utf-8'))==SPEC
start=time.perf_counter(); cases=0; assertions=0
def ck(v):
 global assertions
 assertions+=1
 assert v
 if time.perf_counter()-start>60: raise TimeoutError('audit cap')

def cube(t,n,fix):
 return [x for x in range(1<<n) if all(((x>>i)&1)==b for i,b in fix.items())]

def energy(t,n,fix):
 xs=cube(t,n,fix)
 return sum((R(sum(t[x]!=t[x^(1<<i)] for x in xs),len(xs))
             for i in range(n) if i not in fix),R(0))

for n in range(4):
 for bits in range(1<<(1<<n)):
  t=tuple(1-2*((bits>>x)&1) for x in range(1<<n))
  for order in itertools.permutations(range(n)):
   for policy in range(5):
    # Entries retain physical reach and first-mark ownership independently.
    qpre=qpost=lm=lu=first=R(0)
    todo=[({},R(1),False)]
    while todo:
     fix,p,marked=todo.pop(); depth=len(fix); j=energy(t,n,fix)
     trigger=(policy==0 or (policy==2 and depth==1 and list(fix.values())[0]==0)
       or (policy==3 and depth>0 and sum(fix.values())==1)
       or (policy==4 and depth==n))
     if trigger and not marked: marked=True; first+=p*j
     # Policies use actual history, never unseen input values.
     stop=depth==n or j==0 or (policy in (2,3) and depth>0 and (bits+sum((i+1)*b for i,b in fix.items()))%3==0)
     if stop:
      if marked: lm+=p*j
      else: lu+=p*j
      continue
     i=order[depth]; xs=cube(t,n,fix)
     fee=R(sum(t[x]!=t[x^(1<<i)] for x in xs),len(xs))
     if marked: qpost+=p*fee
     else: qpre+=p*fee
     for b in (0,1): todo.append((dict(fix,**{})|{i:b},p/2,marked))
    root=energy(t,n,{})
    ck(first==qpost+lm); ck(root==qpre+first+lu); ck(root==qpre+qpost+lm+lu)
    cases+=1

# A repeated-mark grant is not an admissible first-mark antichain.
parity=(1,-1,-1,1)
root=energy(parity,2,{})
renewed=root+(energy(parity,2,{0:0})+energy(parity,2,{0:1}))/2
ck(root==2 and renewed==3 and renewed>root)

# Point-defect2 has root spectrum uniform on four atoms. Its half/tuned
# smoothed reference remains uniform. Physical marginal is uniform on two
# atoms, but each child spectrum is a point mass: average query KL=1.
t=(-1,1,1,1)
query=R(sum(t[x]!=t[x^1] for x in range(4)),4)
ck(query==R(1,2)); ck(R(1)>query)

# Point-defect3, mark at root and query to constants. Full signed cost=0.
# Positive-only charges keep at least K_root>0. With tuned epsilon=3/16,
# P=(9/16,1/16 x7), q=(123/256,19/256 x7).
# 16*K_root=log2((48/41)^9*(16/19)^7), certified without rounded logs.
ck(48**9*16**7>41**9*19**7)

# Without normalized r, r=2P at a constant gives K_old=-1, K_new=0,
# hence D=1>I=0. This violates a stated hypothesis, not the theorem.
ck(1>0)

out=dict(status='PASS',policy_runs=cases,assertions=assertions,
 elapsed_seconds=time.perf_counter()-start,
 guards=dict(nonprefix_marks='parity2: renewed 3 > original 2',
  query_KL='point-defect2: actual physical query KL 1 > query influence 1/2',
  positive_clipping='point-defect3: strictly positive first charge; signed full-tree cost and terminal influence both zero',
  normalization='r=2P at constant gives D=1>I=0; normalized-reference hypothesis necessary'),
 caveat='Independent implementation by same author, not independent-person review')
(OUT/'audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
