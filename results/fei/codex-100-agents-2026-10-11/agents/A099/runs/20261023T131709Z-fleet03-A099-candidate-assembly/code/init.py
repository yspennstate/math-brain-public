from pathlib import Path
import json, hashlib
R=Path(__file__).resolve().parents[1]; ROOT=R.parents[2]
BASE=R.parent/'20261023T110044Z-fleet03-A099-candidate-assembly'
for d in ['out','code']: (R/d).mkdir(exist_ok=True)
def put(n,x): (R/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
(R/'code/prior_exact.py').write_bytes((BASE/'code/prior_exact.py').read_bytes())
sources={
'A085':ROOT/'A085/runs/20261023T112613Z-fleet03-A085-certificate-adversary',
'A096':ROOT/'A096/runs/20261023T115236Z-fleet03-A096-live-gap-ledger',
'A003':ROOT/'A003/runs/20261023T121547Z-fleet03-A003-minimal-target-formulation',
'A097':ROOT/'A097/runs/20261023T121505Z-fleet03-A097-cross-route-transfer'}
records=[]
for who,p in sources.items():
 for f in ['CLAIMS.json','REPORT.md','PROOF.md' if who in ['A085','A097'] else 'DERIVATION.md']:
  q=p/f
  text=q.read_text(encoding='utf-8')
  (R/'out'/f'{who}_{f}').write_text(text,encoding='utf-8')
  records.append(dict(path=str(q),sha256=sha(q),bytes=q.stat().st_size))
put('out/SOURCE_RECEIPTS.json',records)
put('out/FROZEN_SPEC.json',dict(helper_version='A099 v10 check.py and byte-identical v9 prior_exact.py',
 helper_sha256=sha(R/'code/prior_exact.py'),checker_sha256=sha(R/'code/check.py'),
 family='All labelled Boolean cores dimension0..3 lifted to disjoint parity blocks; explicit three-bit phase-null core in both signed four-bit-controller wrappers',
 domain='L2 for all278 cores; L3 for all22 cores dimension0..2; complete legal block-unwrapping trees. Geometric targets on22 dimension0..2 L3 lifts,3 target recipes,stopping reaches1/2,1/4,1/4 when>=2 physical coordinates. Explicit floor-family L1,2,3 and both signs.',
 case_count=dict(lifted_trees=300,geometric_target_transactions=66,floor_wrappers=6),
 symmetry='None on truth tables, coordinates or outcomes; one deterministic complete legal tree per core. Adaptive and all-dimensional extension is analytic, not enumerated.',
 arithmetic='Fraction spectra, direct physical edges, exact prime-log expressions; rational fourth-power geometric pullback removes irrational roots; integer-power normalizer certificate. No floating sign test.',
 memory_estimate_MB=150,peak_memory='UNMEASURED',pilot_max_seconds=55,main_max_seconds=180,
 pilot='all22 labelled dimension0..2 cores L2, geometric transactions and6 explicit wrappers',
 version='1',automatic_dimension_escalation=False,heavy_job=False))
print('Source copies and frozen specification saved; no search executed.')
