from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
old=R.parents[0]/'20261014T021710Z-fleet05-A013-representation-stability/code/check.py'
helper=old.read_text().split('patterns=')[0]
(R/'code/arithmetic.py').write_text(helper,encoding='utf-8')
pilot=json.loads((R/'out/PILOT_RESULTS.json').read_text())
spec={'helper_version':'A013-two-row-continuum-v1','actual_family':'G=c(s), H=c(s)(1-2[1_(s=w0) E0(V)+1_(s=w1) E1(V)]); distinct shared points on three bits; arbitrary events on same independent private cube; fresh selector','domain':'All real p,q in [0,1]; exact Boolean applications have dyadic event probabilities. Fixed eight grouped phase profiles; seed16x16 boxes, at most4 bisection levels in both axes.','maximum_leaf_box_count':8*256**2,'phase_classification':'All256 phases via character-orbit representatives; affine maps distinct point pair to0,1. Analytic B,d invariant only; original physical influence retained.','arithmetic':'Rational monotone Phi bounds; integer Walsh classification; exact 20-term atanh log intervals rounded outward to2^-48','memory_estimate_MB':100,'maximum_runtime_seconds_per_profile':50,'profile_jobs':8,'automatic_escalation':False,'failure_policy':'Save unresolved boxes at fixed depth or runtime; do not claim continuum unless all boxes close','proof_bridge':'Analytic rare/moderate domains already closed; on middle-band boxes bound k=(p+sign*q)/8, A=(a-k)^2,B=k^2 by rational endpoint maxima, use componentwise monotonicity of Phi and lower-bound2d+2delta.'}
(R/'out/FROZEN_CONTINUUM.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
print('continuum helper and spec frozen')
