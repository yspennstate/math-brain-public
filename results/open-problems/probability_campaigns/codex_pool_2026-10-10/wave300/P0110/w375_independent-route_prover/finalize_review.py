"""Record received review receipts in this worker folder only."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
outcome = {
    'recorded_at_utc': datetime.now(timezone.utc).isoformat(),
    'parent_problem': 'GAP', 'current_openness': 'UNKNOWN', 'novelty_claim': False,
    'peer_reviews': [
        {'agent': 'w376', 'role': 'adversary', 'verdict': 'scoped KEEP', 'scope': ['L1', 'L2', 'L3', 'L4'],
         'receipt': '~/brain_workers/w376/PEER_AUDIT.md'},
        {'agent': 'w377', 'role': 'designated referee', 'verdict': 'scoped KEEP', 'scope': ['L1', 'L2', 'L3', 'L4', 'w376-C008 raw-coupling consequence'],
         'receipt': '~/brain_workers/w377/REVIEW_PACKET.md',
         'reported_reproduction': '~/brain_workers/w377/review_repro.py',
         'reported_exact_cases': {'two_point_assignments': 256, 'two_point_delta': '1/256', 'linear_gap_lower': '1/1024', 'diagonal_paths_at_k3': 20}},
    ],
    'formal_check_receipt': None, 'two_account_admission_verified': False,
    'local_numerical_checks': 'Held twice by fresh physical/commit pressure; checks_started=false',
    'remaining_gap': 'Matching fluctuation/wandering exponent pairs for an explicit full-plane iid lattice law.',
}
(ROOT / 'REVIEW_OUTCOMES.json').write_text(json.dumps(outcome, indent=2) + '\n', encoding='utf-8')
claim_path = ROOT / 'CLAIMS.jsonl'
claims = [json.loads(line) for line in claim_path.read_text(encoding='utf-8').splitlines() if line.strip()]
for claim in claims:
    if claim['claim_id'] in {f'w375-P0110-L{i}' for i in range(1, 5)}:
        claim['status'] = 'independently checked proof'
        claim['independent_reviewer'] = 'w376 scoped KEEP; designated referee w377 scoped KEEP'
        claim['review_receipts'] = [r['receipt'] for r in outcome['peer_reviews']]
        claim['remaining_gap'] = 'Parent P0110 exponent-existence gap remains; two-account admission and live integration are unconfirmed. Scope is exactly this partial lemma.'
if not any(c['claim_id'] == 'w375-P0110-L2C' for c in claims):
    claims.append({
        'claim_id': 'w375-P0110-L2C',
        'statement': 'Under L2, put c0=delta/(k+1)>0. For any coupling at each n of unrestricted axial passage time U_n and the directed axial sum V_n with their prescribed marginal laws, and every 0<c<c0, P((V_n-U_n)/n>=c) tends to one.',
        'assumptions': ['L2 bounded positive nondegenerate iid law', 'Couplings preserve both marginal passage-time laws', 'Raw costs, not centered fluctuations'],
        'source': {'kind': 'owner-own-work', 'path': 'PROVED_LEMMAS.md', 'section': 'L2 coupling clarification', 'credit': 'w376 C008; independently kept by w377', 'quote': 'No independence between the coupled passage times is needed.'},
        'proof_or_counterexample': 'Choose eta=(c0-c)/2. Bound the complement of the joint marginal drift events by the sum of their probabilities; both tend to zero. On their intersection the raw difference is at least c*n.',
        'independent_reviewer': 'w377 KEEP of w376 C008, REVIEW_PACKET.md; proof conclusion matches the saved L2 clarification',
        'remaining_gap': 'No centered-fluctuation or exponent conclusion; this does not solve P0110.',
        'status': 'independently checked proof',
    })
claim_path.write_text(''.join(json.dumps(c, ensure_ascii=False) + '\n' for c in claims), encoding='utf-8')
for filename in ('SOURCE_STATUS.json', 'DELIVERY_RECEIPT.json'):
    p = ROOT / filename
    d = json.loads(p.read_text(encoding='utf-8'))
    d['workflow_states']['reviewed'] = True
    d['review_receipt'] = str(ROOT / 'REVIEW_OUTCOMES.json')
    d['mathematical_review_scope'] = 'L1-L4 plus the L2 raw-coupling corollary; parent P0110 GAP'
    d['two_account_admission_verified'] = False
    if filename == 'SOURCE_STATUS.json':
        d['peer_review']['designated_referee_status'] = 'scoped KEEP L1-L4 and C008'
        d['conditional_theorem_quantifier_note'] = 'This attempt uses Chatterjee A3-A4 with a large-endpoint cutoff. The later Auffinger-Damron all-nonzero-endpoint lower wandering condition is not silently substituted; see the referee source-quantifier note.'
    else:
        d['mathematical_check'] = 'w376 and designated referee w377 scoped KEEP; no parent solution or formal-check receipt'
    p.write_text(json.dumps(d, indent=2) + '\n', encoding='utf-8')
p = ROOT / 'REVIEW_PACKET.md'
text = p.read_text(encoding='utf-8')
text += '\nFinal received outcome, 2026-10-10: w377 KEEP L1-L4 and w376 C008 within the raw/finite/bounded-law scopes; parent P0110 GAP. Receipt: ~/brain_workers/w377/REVIEW_PACKET.md. Local finite numerical checks were held twice, not passed. The two-entry concept draft is submitted; review is recorded separately from admission, ingestion and retrieval.\n'
p.write_text(text, encoding='utf-8')
p = ROOT / 'PROGRESS_EVENT.json'
d = json.loads(p.read_text(encoding='utf-8'))
d['event'] = 'P0110 independent route: w376 and referee w377 KEEP L1-L4 and raw-coupling consequence; two concept drafts/three relations submitted; parent GAP; local numerics held by resource pressure.'
p.write_text(json.dumps(d, indent=2) + '\n', encoding='utf-8')
required = ('SOURCE_STATUS.json', 'ATTEMPT.md', 'CLAIMS.jsonl', 'REVIEW_PACKET.md', 'REPORT.md', 'DELIVERY_RECEIPT.json', 'REVIEW_OUTCOMES.json', 'CERTIFICATE_RESULTS.json', 'COMPUTE_GATE.json')
assert all((ROOT / filename).is_file() for filename in required)
status_path = ROOT / 'STATUS.md'
lines = status_path.read_text(encoding='utf-8').splitlines()
lines[0] = 'STATE: NEEDS_REVIEW'
for i, line in enumerate(lines):
    if line.startswith('NEXT:'):
        lines[i] = 'NEXT: Coordinator admit the reviewed L2/L3 concept rows; next proof step is a centered growing-width comparison at the actual standard-deviation scale without assuming exponents.'
        break
lines += [
    '2026-10-10: STUCK: numerical certificates were held twice by fresh physical/commit pressure; retained the complete hand proofs and independent referee checks rather than bypassing the resource gate.',
    '2026-10-10: w376 and designated referee w377 KEEP L1-L4; w377 also KEEP C008 raw-coupling consequence. Saved REVIEW_OUTCOMES.json and updated per-claim statuses. These are partial results; P0110 remains GAP and current openness UNKNOWN.',
    '2026-10-10: Submitted two concept entries and three relations atomically as math-brain-inbox/w375/bundle_001.json under narrow lease clm-1d8a4734d1. Local shape check PASS. The overlapping threshold stays local; w378 was notified. Source/delivery receipts separate submitted, reviewed, ingested and retrievable. No live-store or recall-control changes.',
    '2026-10-10: REPORT.md, staged hook diff and local progress event complete. No live brain improvement is claimed or measured; coordinator admission and integration remain pending.',
]
status_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(json.dumps({'state': lines[0], 'claim_rows': len(claims), 'partial_lemmas': 4, 'coupling_corollary': 1,
                  'draft_entries': 2, 'draft_relations': 3, 'submitted': True, 'reviewed': True,
                  'ingested': False, 'retrievable': False, 'local_numerical_pass': False, 'parent': 'GAP'}))
