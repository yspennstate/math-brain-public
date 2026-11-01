"""Finalize local review receipts even if shared-inbox lease operations are busy."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
gate = {'author': {'agent': 'w531', 'served_model_status': 'UNKNOWN',
                   'response_side_evidence': None, 'requested_model': 'gpt-6.1-sol',
                   'requested_reasoning': 'max', 'requested_service_tier': 'Fast',
                   'requested_settings_are_not_served_model_evidence': True},
        'referee': {'agent': 'w533', 'served_model_status': 'UNKNOWN',
                    'response_side_evidence': None, 'verdict': 'PENDING'},
        'scoped_keeps': [], 'parent_problem_solved_claim': False,
        'current_openness': 'UNKNOWN', 'promotion': 'DRAFT concepts only', 'formal_check': None}
(root / 'review_packet/REVIEW_GATES.json').write_text(json.dumps(gate, indent=2), encoding='utf-8')
rows = [json.loads(s) for s in (root / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
for row in rows:
    if row['id'] == 'w531-P0309-M1':
        row['source']['path'] = str(root / 'verification_initial/control_results.json')
        row['proof_or_counterexample'] = 'Initial command: python -X utf8 ~/brain_workers/w531/check_controls.py; exact code, 295-check PASS and admission receipt archived in verification_initial. Root control_results.json is the separate GATED entropy-extension attempt.'
(root / 'CLAIMS.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
report = (root / 'REPORT.md').read_text(encoding='utf-8')
report = report.replace('Measured command:', 'Measured initial command:').replace(
    'The fresh governor/direct resource gate is in compute_gate_receipt.json.',
    'The passing fresh resource gate is archived in verification_initial/compute_gate_receipt.json.')
report += '\nSubmission checkpoint: local 4-entry/4-relation DRAFT is complete at drafts/bundle_001.json. The first shared-inbox lease/assert attempt hit a mesh database lock before writing; submission is PENDING in BRAIN_SUBMISSION.json and is being retried once. Review pending; no scoped KEEP or response-side served-model evidence is available.\n'
(root / 'REPORT.md').write_text(report, encoding='utf-8')
readme = (root / 'review_packet/README.md').read_text(encoding='utf-8')
readme += '\nREVIEW_GATES.json records no scoped KEEP and UNKNOWN author/referee served identity. Requested settings are not served evidence. The local draft is complete; consult BRAIN_SUBMISSION.json for actual shared-inbox submission status, which is separate from independent review, ingestion and retrieval.\n'
(root / 'review_packet/README.md').write_text(readme, encoding='utf-8')
identities = {'meaning': 'Review-file identity only, not mathematical proof or a store manifest', 'files': []}
for name in ['PRESSURE_ROUTE.md', 'CLAIMS.jsonl', 'review_packet/README.md', 'verification_initial/control_results.json']:
    p = root / name
    identities['files'].append({'path': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
(root / 'review_packet/REVIEW_FILE_IDENTITIES.json').write_text(json.dumps(identities, indent=2), encoding='utf-8')
with (root / 'HANDOFF_LOG.jsonl').open('a', encoding='utf-8') as f:
    f.write(json.dumps({'date': '2026-10-10', 'kind': 'draft-submission', 'state': 'PENDING',
                        'reason': 'Mesh database locked during lease assertion/reacquisition before inbox mutation',
                        'local_draft': str(root / 'drafts/bundle_001.json')}) + '\n')
print(json.dumps({'local_review_complete': True, 'claims': len(rows), 'pressure_route_sha256': identities['files'][0]['sha256']}))
