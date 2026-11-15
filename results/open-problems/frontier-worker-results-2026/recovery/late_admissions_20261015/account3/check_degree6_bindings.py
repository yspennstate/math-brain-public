"""Bind all new submission pins and explicitly inherited reviewed premises."""
from pathlib import Path
import hashlib,json
OUT=Path(__file__).resolve().parent;ROOT=Path('~/brain_workers/w682')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
start=json.loads((OUT/'t067_degree6_provenance_start.json').read_text(encoding='utf-8'))
hashes={}
for p,h in start['proof_hashes'].items():assert sha(Path(p))==h;hashes[p]=h
manifest=ROOT/'checks/balanced_degree6_submission.json';data=json.loads(manifest.read_text(encoding='utf-8'))
for relative,h in data['sha256'].items():
    p=ROOT/relative;assert sha(p)==h,(relative,'changed submission pin');hashes[str(p)]=h
hashes[str(manifest)]=sha(manifest)
prior=json.loads((OUT/'d91_review_receipt.json').read_text(encoding='utf-8'))
inherited={}
for name in ['T067-CUBIC-FUSION-001_v1.md','T067-TERNARY-MOMENTS-001_v1.md','T067-UNIFORM-LOCAL-001_v1.md']:
    p=ROOT/'proofs'/name;h=prior['source_hashes'][str(p)];assert sha(p)==h;hashes[str(p)]=h;inherited[str(p)]=h
for name in ['uniform_local_radius_d5_048_raw.json','uniform_local_radius_d5_048_bern1.json','uniform_local_radius_d5_048_bern2.json','uniform_local_radius_d5_048_report.json']:
    p=ROOT/'checks'/name;hashes[str(p)]=sha(p)
local=json.loads((OUT/'degree6_local_checks.json').read_text(encoding='utf-8'))
assert local['raw_sha256']==hashes[str(ROOT/'checks/uniform_local_radius_d5_048_raw.json')]
assert local['source_sha256']==sha(OUT/'check_degree6_local.py')
native=json.loads((OUT/'degree6_exact_replay_checks.json').read_text(encoding='utf-8'))
assert native['source_sha256']==sha(OUT/'check_degree6_exact.cpp') and native['driver_sha256']==sha(OUT/'check_degree6_exact.py')
assert native['masses_sha256']==sha(OUT/'degree6_full.masses.txt')
o=dict(status='PASS',all_submission_pins_checked=len(data['sha256']),source_hashes=hashes,explicit_inherited_premises=inherited,prior_review_receipt_sha256=sha(OUT/'d91_review_receipt.json'),prior_verdicts_sha256=sha(OUT/'d91_inherited_verdicts.tsv'),source_sha256=sha(Path(__file__)))
(OUT/'degree6_binding_checks.json').write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8');print('Exact submission pins and inherited premises matched',len(hashes),flush=True)
