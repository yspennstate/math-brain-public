"""Record scoped referee verdicts; preserve every proof/model admission gate."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
referee_path = Path('~/brain_workers/w458/REVIEW_PACKET.md')
if not referee_path.is_file():
    raise SystemExit('appointed referee receipt missing')
# Consume the verdict as evidence, without reviewing the review or claiming model attestation.
review = {'state': 'SCOPED MATHEMATICAL KEEP from w457 and w458; served-model admission gates pending', 'peers': [{'agent': 'w457', 'evidence': '~/brain_workers/w457/AUDIT_w456.md'}, {'agent': 'w458', 'evidence': str(referee_path)}], 'scope': 'finite free zero-field identities, local Legendre/exclusion statements, L5 conditional implication; scalar q=3 constants checked; SP and C0048 excluded', 'served_model_evidence': 'UNKNOWN', 'theorem_promotion': 'not authorized by this packet'}
pipeline_path = root / 'BRAIN_PIPELINE.json'
pipeline = json.loads(pipeline_path.read_text(encoding='utf-8'))
pipeline['reviewed'] = review
pipeline_path.write_text(json.dumps(pipeline, indent=2) + '\n', encoding='utf-8')

claims_path = root / 'CLAIMS.jsonl'
claims = [json.loads(line) for line in claims_path.read_text(encoding='utf-8').splitlines() if line.strip()]
for claim in claims:
    if claim['claim_id'] in ('w456-L1', 'w456-L4', 'w456-L5', 'w456-L2-L3'):
        claim['independent_reviewer'] = review
    elif claim['claim_id'] == 'w456-entropy':
        claim['independent_reviewer'] = {'w457': 'KEEP scalar entropy bounds and constants', 'w458': 'q=3 constants independently checked in REVIEW_PACKET.md', 'served_model_evidence': 'UNKNOWN'}
    elif claim['claim_id'] == 'w456-SP':
        claim['independent_reviewer'] = {'w458': 'retain unproved status; never promote input to parent proof', 'evidence': str(referee_path)}
claims_path.write_text(''.join(json.dumps(claim) + '\n' for claim in claims), encoding='utf-8')

source_path = root / 'SOURCE_STATUS.json'
source = json.loads(source_path.read_text(encoding='utf-8'))
source['review_state'] = review
source['served_model_evidence']['referee'] = 'Unavailable according to w458/REVIEW_PACKET.md; no response-side attestation.'
source['canonical_target_check'] = {'receipt': 'store_target_lookup.json', 'read_only': True, 'nodes': ['claim_38c945c83e6d9f9dc77b20f936b660e811e528c284f76bd513990e6ed06ecc6a', 'claim_9830d2b5c32b82afa88de780611e6b0fe5e81b7d425ff5fabff71dad19cc6930'], 'observed_status': 'both concept/unverified; prior attempt reports no result'}
source_path.write_text(json.dumps(source, indent=2) + '\n', encoding='utf-8')

report_path = root / 'REPORT.md'
report = report_path.read_text(encoding='utf-8')
report = report.replace('w457 independently recorded a scoped KEEP of L1--L5 and the scalar constants, excluding SP and C0048. Appointed referee w458 is pending.', 'w457 and appointed referee w458 independently recorded scoped KEEP verdicts for the finite identities and conditional reduction, with scalar q=3 constants checked. Both exclude SP and C0048.')
report_path.write_text(report, encoding='utf-8')
packet_path = root / 'REVIEW_PACKET.md'
packet_path.write_text(packet_path.read_text(encoding='utf-8') + '\nAppointed referee receipt: ~/brain_workers/w458/REVIEW_PACKET.md. Scoped mathematical KEEP recorded; SP remains unproved and author/referee served-model evidence is unavailable. No theorem admission, ingestion or retrieval is claimed.\n', encoding='utf-8')

receipt_path = root / 'REVIEW_RECEIPT.json'
receipt = json.loads(receipt_path.read_text(encoding='utf-8'))
receipt['peer_review'] = review
receipt['served_model']['referee'] = 'UNKNOWN per actual referee receipt'
receipt['at_utc'] = datetime.now(timezone.utc).isoformat()
for name in receipt['files']:
    data = (root / name).read_bytes()
    receipt['files'][name].update({'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
receipt_path.write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')

status_path = root / 'STATUS.md'
status = status_path.read_text(encoding='utf-8').splitlines()
status[0] = 'STATE: NEEDS_REVIEW'
status[1] = 'NEXT: Obtain the remaining model/admission decision; the next proof step is a volume-uniform C1 lattice-correlation bound for SP(3,3).'
status.extend(['2026-10-10: Completed and measured packet: 8 claim rows, 6 DRAFT brain entries, 4 dependencies, 72/72 exact checks; variance omission failed 40 cases and changed two signs. Scoped KEEP receipts from w457 and w458 recorded; SP and C0048 remain unproved. Current openness UNKNOWN; served-model evidence unavailable; no live ingestion/retrieval claimed.', '2026-10-10: Measured packet delivered to w458 (msg-6491d63de0) and integration contact codex-01a12190 (msg-58fd4249b6); hook proposal submitted under own file, scoped correction under clm-94933f2435 and released. All proof and evidence files saved.'])
status_path.write_text('\n'.join(status) + '\n', encoding='utf-8')
progress = subprocess.run([sys.executable, '-X', 'utf8', '~/primary_directive/pd_progress.py', '--event', 'w456 C0048 NEEDS_REVIEW: 8 claim rows, six draft cards/four dependencies, 72 exact cases pass; w457/w458 scoped KEEP, SP(3,3) unproved and model gates pending.', '--agent', 'w456', '--row', 'S1.C0048', '--evidence', str(report_path)], capture_output=True, text=True, encoding='utf-8', errors='replace')
print(json.dumps({'state': 'NEEDS_REVIEW', 'progress_exit': progress.returncode, 'progress_output': progress.stdout.strip(), 'report': str(report_path), 'parent_problem_proved': False, 'model_gate': 'UNKNOWN'}), flush=True)
messages = subprocess.run([sys.executable, '-X', 'utf8', '~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py', 'read', '--as', 'w456', '--max', '6'], capture_output=True, text=True, encoding='utf-8', errors='replace')
print(messages.stdout[:6000], flush=True)
