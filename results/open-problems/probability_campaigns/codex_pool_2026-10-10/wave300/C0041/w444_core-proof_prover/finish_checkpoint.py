import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
validation = json.loads((ROOT / 'VALIDATION.json').read_text(encoding='utf-8'))
assert validation['structure'] == 'PASS'
assert validation['after_worker_claim_rows'] == 9
assert validation['after_worker_draft_entries'] == 8 and validation['relations'] == 10
assert validation['theorem_promotions'] == 0
hashes = json.loads((ROOT / 'REVIEW_HASHES.json').read_text(encoding='utf-8'))
for item in hashes['files']:
    assert hashlib.sha256(Path(item['path']).read_bytes()).hexdigest() == item['sha256']
receipts = [json.loads(line) for line in (ROOT / 'COMMUNICATION_RECEIPTS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
for recipient in ['w445', 'w446', 'codex-01a12190']:
    item = next(row for row in receipts if row['recipient'] == recipient)
    assert item['returncode'] == 0 and json.loads(item['stdout'])['inserted'] == 1
old = (ROOT / 'STATUS.md').read_text(encoding='utf-8').splitlines()
old[0] = 'STATE: NEEDS_REVIEW'
old[1] = 'NEXT: w446 audits R1/L1/L2-L2b/L3/T1; next proof step is a rare certificate for arbitrary low-escape regions, keeping E_Q[tau_1] integrability unproved.'
now = datetime.now(timezone.utc).isoformat()
old.append(now + ': Deliverables complete and measured at packet scope. All three handoffs delivered; artifact hashes match. Eight concept drafts submitted, review/ingestion/retrieval pending. Full C0041 target remains unproved by this packet; current openness UNKNOWN.')
(ROOT / 'STATUS.md').write_text('\n'.join(old) + '\n', encoding='utf-8')
(ROOT / 'FINISH_RECEIPT.json').write_text(json.dumps({
    'time': now, 'state': 'NEEDS_REVIEW', 'artifact_identity_check': 'MATCH',
    'handoffs': ['w445', 'w446', 'codex-01a12190'],
    'source_openness': 'UNKNOWN', 'mathematical_review': 'PENDING',
    'parent_problem_solved': False,
    'next_proof_step': 'Quantify certificates for arbitrary low-escape regions without coherent inward-row assumptions',
}, indent=2) + '\n', encoding='utf-8')
print('STATE: NEEDS_REVIEW; 9 rows, 8 concepts, 10 relations; all handoffs delivered; mathematical review PENDING; C0041 not proved here.')
