from pathlib import Path
from fractions import Fraction as Q
import json,time
from independent_audit import U,H,du,plus,child,padding,influence
R=Path(__file__).resolve().parents[1];O=R/'out'
spec=dict(helper_version='direct-walsh-tensor-tree-v1',family='two disjoint copies of explicit nonzero-erasure witness, each with its own parity bit',domain=dict(seed_bits=6,lifted_bits=8,blocks=2,query_coordinates=[1,5]),case_count=1,symmetry='none',arithmetic='direct rational Walsh, exact prime-log vectors',memory_estimate_MB=30,max_runtime_seconds=30)
(O/'FROZEN_TENSOR_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
start=time.monotonic();checks=0
def ck(b):
 global checks
 checks+=1;assert b,checks
 assert time.monotonic()-start<30
v=(-1,1,1,-1,-1,1,1,1);F=padding(v,5)
vv=tuple(a*b for b in v for a in v);FF=tuple(a*b for b in F for a in F)
for op in (H,U):
 ck(op(vv)==plus((2,op(v))));ck(op(FF)==plus((2,op(F))))
ck(sum((influence(FF,j) for j in range(8)),Q(0))==2*sum((influence(F,j) for j in range(4)),Q(0)))
ck(du(FF,1)==du(F,1));ck(du(FF,5)==du(F,1))
# Restrict first block, then query second in both complete children.
children=[child(FF,1,b) for b in (0,1)]
leaves=[child(ch,4,b) for ch in children for b in (0,1)]
for ch in children:ck(du(ch,4)==du(F,1))
bill=plus((1,du(FF,1)),(Q(1,2),du(children[0],4)),(Q(1,2),du(children[1],4)))
ck(bill==plus((2,du(F,1))))
ck(U(FF)==plus((1,bill),*[(Q(1,4),U(leaf)) for leaf in leaves]))
# Root discount versus ALL terminal discounts using the parallel seed tree.
seedleaves=[child(child(vv,1,a),3,b) for a in (0,1) for b in (0,1)]
rootd=plus((1,U(vv)),(-1,U(FF)))
terminald=plus(*[(Q(1,4),plus((1,U(s)),(-1,U(t)))) for s,t in zip(seedleaves,leaves)])
c={2:-Q(1,2),3:Q(17,16),5:-Q(1,2)}
ck(plus((1,terminald),(-1,rootd))==plus((2,c)))
result=dict(status='PASS',exact_assertions=checks,runtime_seconds=time.monotonic()-start,full_terminal_leaves=4,physical_query_influence='3/2',scope='fixed two-block exact audit; all-m theorem supplied analytically')
(O/'TENSOR_TREE_AUDIT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
