from pathlib import Path
import json,hashlib
root=Path(__file__).parent
status=(root/'STATUS.md').read_text(encoding='utf-8')
assert status.splitlines()[0]=='STATE: DONE'
assert 'VERDICT: PARTIAL' in status.splitlines()
manifest=json.loads((root/'final_manifest.json').read_text(encoding='utf-8'))
for name,digest in manifest['sha256'].items():
 assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
claims=[json.loads(line) for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
for r in claims:
 assert set(['problem_id','claim','status','proof_location','remaining_gap','checks'])<=set(r)
 assert r['problem_id']=='P0170'
 assert r['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture']
 assert (root/r['proof_location'].split(',')[0].split(' and ')[0]).exists()
print('STATE: DONE; VERDICT: PARTIAL.',flush=True)
print('All recorded artifact hashes and',len(claims),'claim schemas verified.',flush=True)
print('Lean completed at closure:',manifest['lean_completed_at_closure'],flush=True)
