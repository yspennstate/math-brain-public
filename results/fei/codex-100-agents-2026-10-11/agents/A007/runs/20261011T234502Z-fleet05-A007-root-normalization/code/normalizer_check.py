"""Exact finite support for the all-weight retained-normalizer proof."""
from pathlib import Path
from fractions import Fraction as F
import json,sys,time
run=Path(__file__).resolve().parents[1]
spec=dict(helper_version='A007-affine-normalizer-v1',family='affine-plane DNF analytic certificate inputs',
 parameter_domain='q=16..128, five positive total-weight scales per q: q,q/2,1,1/2,2^-q',
 case_count=565,symmetry='none; scalar rational bounds only, no additional truth tables',
 arithmetic='Fraction; analytic log sign and Jensen proofs are in REPORT.md A2',
 memory_estimate_bytes=5_000_000,max_runtime_seconds=60)
if '--freeze' in sys.argv:
 (run/'NORMALIZER_FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf8');print(json.dumps(spec));raise SystemExit
assert json.loads((run/'NORMALIZER_FROZEN_SPEC.json').read_text())==spec
t=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1;assert x,checks
for q in range(16,129):
 rho=F(1,2**q);eps=q*(q+1)*rho*2
 v_bound=F(2,q*(1-eps))
 ck(eps<F(1,2));ck(v_bound<=F(4,q));ck(v_bound<F(11,5));ck(rho*q<=1)
 for u in [F(q),F(q,2),F(1),F(1,2),rho]:
  ck(0<u<=q)
  ck(rho*u/(1+rho*u)>=rho*u/(1+rho*q))
  # In the exact lower bound, the coefficient of log u is negative.
  ck(v_bound-F(11,5)<0)
  ck(q*v_bound+v_bound<=5)
result=dict(helper_version=spec['helper_version'],assertions_passed=checks,cases=565,elapsed_seconds=time.perf_counter()-t,
            scope='exact rational premises; all-weight logarithmic conclusion supplied by REPORT.md A2')
(run/'out'/'NORMALIZER_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps(result))
