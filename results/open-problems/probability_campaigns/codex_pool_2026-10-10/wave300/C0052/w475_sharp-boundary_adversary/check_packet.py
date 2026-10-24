"""One final artifact-integrity check; no repeat mathematical computation or integration."""
from pathlib import Path
import hashlib
import json

root=Path(__file__).resolve().parent
packet=json.loads((root/'review_packet.json').read_text(encoding='utf-8'))
for name,expected in packet['artifact_sha256'].items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==expected, name
claims=[json.loads(line) for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
assert len(claims)==5 and len({c['claim_id'] for c in claims})==5
allowed={'conjecture','numerical evidence','sketch','proved special case','independently checked proof'}
assert all(c['status'] in allowed and c['parent_problem_solved'] is False for c in claims)
bundle=json.loads((root/'bundle_001.json').read_text(encoding='utf-8'))
draft=Path(packet['brain_output']['draft'])
assert json.loads(draft.read_text(encoding='utf-8'))==bundle
assert len(bundle['entries'])==2 and all(e['kind']=='concept' and e['proof_text'] is None for e in bundle['entries'])
assert packet['brain_output']['ingested'] is False and packet['brain_output']['retrievable'] is False
assert packet['model_gate']['promotion_allowed'] is False and packet['parent_problem_solved'] is False
assert json.loads((root/'measurements.json').read_text(encoding='utf-8'))['checks_passed']==10
assert json.loads((root/'bridge_measurements.json').read_text(encoding='utf-8'))['checks_passed']==17
assert (root/'patches/01_current_sprinkling_hook.diff').read_text(encoding='utf-8').startswith('--- a/~/primary_directive/hooks1000/proposals/probability-w475.jsonl')
result={'status':'PASS','artifact_hashes_verified':len(packet['artifact_sha256']),
        'claim_rows':5,'audit_rows':3,'math_checks_previously_passed':27,'concept_draft_entries':2,
        'live_store_mutated':False,'parent_problem_solved':False}
(root/'FINAL_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
