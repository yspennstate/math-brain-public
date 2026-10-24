"""Consume scoped referee receipts and prepare a review-only integration handoff.

Writes only this worker directory and its explicitly authorized DRAFT inbox.
No store writes, delegation, numerical experiment, or live promotion.
"""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w505').resolve()
REVIEW_PATH = Path('~/brain_workers/w506/CLAIMS.jsonl')


def read(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8-sig'))


def save(name, data):
    path = (ROOT / name).resolve()
    assert path.parent == ROOT
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def prepare():
    now = datetime.now(timezone.utc).isoformat()
    receipt_map = {
        'w505-C001': 'P0162-REVIEW-W505-C001',
        'w505-C002': 'P0162-REVIEW-W505-C002',
        'w505-C003': 'P0162-REVIEW-W505-004',
        'w505-C004': 'P0162-REVIEW-W505-C004',
        'w505-C005': 'P0162-REVIEW-W505-C005',
        'w505-C006': 'P0162-REVIEW-W505-C006',
    }
    by_id = {}
    for line in REVIEW_PATH.read_text(encoding='utf-8-sig').splitlines():
        row = json.loads(line) if line.strip() else {}
        if row.get('id') in receipt_map.values():
            by_id[row['id']] = row
    assert set(by_id) == set(receipt_map.values())
    assert all(row['verdict'] == 'KEEP' for row in by_id.values())
    save('INDEPENDENT_REVIEW_UPDATE.json', {
        'reviewer': 'w506', 'received_at': now,
        'receipt_path': REVIEW_PATH.as_posix(),
        'receipts': [by_id[receipt_map[key]] for key in receipt_map],
        'scope': 'C001-C005 mathematical proofs checked; C006 conditional induction checked, existence premise NOT proved.',
        'different_model_review_gate': 'UNKNOWN; served model evidence unavailable',
    })
    gaps = {
        'w505-C001': 'No gap in the arbitrary-subset-law result; arbitrary laws need not be Boolean spectra, so this is not FEI.',
        'w505-C002': 'No gap in the exact identity under stated assumptions; a universal suitable-coordinate estimate is still unproved.',
        'w505-C003': 'No gap in this all-coordinate counterexample; full FEI and its suitable-coordinate input remain unproved. No novelty claim.',
        'w505-C004': 'No gap in the named family bound; it does not prove FEI for arbitrary Boolean functions.',
        'w505-C005': 'No gap in the elementary upper bound; its small-influence logarithmic loss remains and no novelty is claimed.',
    }
    claims = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8-sig').splitlines() if line.strip()]
    for row in claims:
        key = row['claim_id']
        if key in receipt_map:
            row['independent_reviewer'] = 'w506; KEEP ' + receipt_map[key]
            row['review_receipt'] = 'INDEPENDENT_REVIEW_UPDATE.json'
            row['served_model_gate'] = 'UNKNOWN, not satisfied by requested settings or agent id'
            if key in gaps:
                row['status'] = 'independently checked proof'
                row['remaining_gap'] = gaps[key]
            else:
                assert row['status'] == 'conjecture'
                row['review_scope'] = 'Conditional induction only; coordinate-existence premise remains unproved.'
        elif key == 'w505-C007':
            row['independent_reviewer'] = 'w506 separately corroborated m=1,2,3 selector values; numerical evidence only'
    assert len({row['claim_id'] for row in claims}) == len(claims)
    (ROOT / 'CLAIMS.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in claims), encoding='utf-8')
    source = read('SOURCE_STATUS.json')
    source['review_received_at'] = now
    source['proof_status'] = 'C001-C005 independently checked by w506; C006 conditional reduction checked, universal suitable-coordinate premise and full FEI unproved.'
    source['review_receipts'] = 'INDEPENDENT_REVIEW_UPDATE.json'
    source['served_model_review_gate'] = 'UNKNOWN'
    save('SOURCE_STATUS.json', source)
    attempt_path = ROOT / 'ATTEMPT.md'
    attempt = attempt_path.read_text(encoding='utf-8')
    old = 'w506 has now independently kept the explicit selector counterexample (P0162-REVIEW-W505-004); the other auxiliary claims retain their recorded review status.'
    new = 'w506 has now independently checked C001-C005 (INDEPENDENT_REVIEW_UPDATE.json). The C006 induction is checked only conditionally: its universal coordinate-selection premise remains unproved. Response-side served model identities are UNKNOWN.'
    assert old in attempt or new in attempt
    attempt_path.write_text(attempt.replace(old, new), encoding='utf-8')
    bundle = read('DRAFT_BUNDLE_REVIEWED.json')
    if not (ROOT / 'DRAFT_BUNDLE_002_SNAPSHOT.json').exists():
        save('DRAFT_BUNDLE_002_SNAPSHOT.json', bundle)
    bundle['bundle_slug'] = 'p0162-restriction-quantifier-obstruction-w505-003'
    for entry in bundle['entries']:
        if entry['key'] == 'restriction-deficit':
            entry['source']['revision'] = '2026-10-10-w506-KEEP-C002-definition-and-identity'
        elif entry['key'] == 'missing-coordinate-input':
            entry['source']['revision'] = '2026-10-10-w506-checked-conditional-reduction-premise-unproved'
        elif entry['key'] == 'coordinate-obstruction':
            addition = ' The same family satisfies I(F_m)=m+(2m+1)/N and H_2(F_m)<=2I(F_m) for every m>=1.'
            if addition not in entry['statement']:
                entry['statement'] += addition
            entry['source']['revision'] = '2026-10-10-w506-KEEP-C002-C003-C004-DRAFT-model-gate-pending'
            proof_addition = ' For the whole-family bound, each of the 2m base coordinate influences is 1/2+1/N: flipping the zero point changes two directed endpoint disagreements in the selector-minus restriction, and averaging the two selector restrictions gives this influence. Along with I_y=1/N this gives I=m+(2m+1)/N. Selector presence in the spectral subset has mass rho=1/N, and either conditional slice has at most N atoms, hence H_2(F_m)<=2m+h_2(rho). Since -(1-rho)ln(1-rho)<=rho, h_2(rho)<=2m rho+rho/ln(2)<=2(2m+1)rho for m>=1, giving H_2(F_m)<=2I(F_m). w506 separately checked C004. These are reviewed mathematical statements in a DRAFT; served-model and different-model promotion gates are not established.'
            if proof_addition not in entry['proof_text']:
                entry['proof_text'] += proof_addition
    save('DRAFT_BUNDLE_REVIEWED.json', bundle)
    final = INBOX / 'bundle_003.json'
    temporary = INBOX / 'bundle_003.part'
    assert final.resolve().parent == INBOX and temporary.resolve().parent == INBOX
    if final.exists():
        assert json.loads(final.read_text(encoding='utf-8-sig')) == bundle, 'Existing draft differs; preserve it.'
    else:
        assert not temporary.exists(), 'Existing partial draft requires inspection; preserve it.'
        with temporary.open('x', encoding='utf-8') as handle:
            handle.write(json.dumps(bundle, ensure_ascii=False, indent=2) + '\n')
        temporary.rename(final)
    state = read('BUNDLE_STATE.json')
    state.update({
        'latest_inbox_path': str(final),
        'supersedes_draft': str(INBOX / 'bundle_002.json'),
        'retained_prior_drafts': ['bundle_001.json', 'bundle_002.json'],
        'instruction': 'Use bundle_003 for validation; retain earlier drafts. Hold live promotion until the corresponding served-model/different-model gates pass.',
        'reviewed': False,
        'review_scope': {'C001-C005': 'independently checked mathematics, w506', 'C006': 'conditional induction only; existence premise unproved', 'full_bundle': 'coordinator validation pending', 'relations': 'proposed, not independently audited'},
        'different_model_review_gate': 'UNKNOWN',
        'promotion_hold': True,
        'live_store_written': False,
    })
    save('BUNDLE_STATE.json', state)
    edges = [json.loads(line) for line in (ROOT / 'EDGE_EVIDENCE.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
    counter = next(entry for entry in bundle['entries'] if entry['key'] == 'coordinate-obstruction')
    for edge in edges:
        edge['from_statement_quote'] = counter['statement']
        edge['state'] = 'submitted bundle_003 DRAFT relation; coordinator relation audit pending'
    (ROOT / 'EDGE_EVIDENCE.jsonl').write_text(''.join(json.dumps(edge, ensure_ascii=False) + '\n' for edge in edges), encoding='utf-8')
    save('MODEL_EVIDENCE.json', {
        'author_agent': 'w505', 'referee_agent': 'w506',
        'author_served_model': 'UNKNOWN', 'referee_served_model': 'UNKNOWN',
        'response_side_evidence': None,
        'requested_model': 'gpt-6.1-sol',
        'requested_settings_are_served_evidence': False,
        'different_model_review_gate': 'UNKNOWN',
        'reason': 'No authorized response-side transcript evidence is supplied in these mathematical artifacts; worker ids and requested settings do not prove served identity.',
        'cost_tokens': None, 'cost_currency': None,
        'measurement_receipt': 'measurements.json',
    })
    audit = read('PEER_AUDIT.json')
    audit['correction_state'] = 'w504 PROOF.md now states phase -2t*(-1)^(indicator z in U); w506 records corrected w504 bundle_003.json. Historical patch retained; do not reapply to corrected text.'
    audit['correction_evidence'] = 'w504/PROOF.md:74; w506/REVIEW_PACKET.md; P0162-REVIEW-SIGN-FIX'
    save('PEER_AUDIT.json', audit)
    (ROOT / 'REVIEW_PACKET.md').write_text('''# w505 P0162 integration review packet

For codex-01a12190. The independent derivation in ATTEMPT.md was saved before reading w504's proof. The all-coordinate bound fails for an exact Boolean family; full FEI and suitable-coordinate selection remain unproved. SOURCE_STATUS.json keeps current global openness UNKNOWN and makes no novelty claim.

w506's exact receipt rows independently check C001-C005: arbitrary-law entropy obstruction, local entropy identity, Boolean selector obstruction, H<=2I for the named family, and the general entropy-deficit upper bound. INDEPENDENT_REVIEW_UPDATE.json contains these receipts. C006 retains status conjecture; its induction was checked conditionally, with its premise assumed rather than proved.

Use ~/math-brain-inbox/w505/bundle_003.json. The four entries and five relations preserve the conjectural input as a concept. The single lemma includes both the diverging selector Delta/I and the bounded full H/I, with complete proofs and separate referee receipts. The two proposed canonical relations quote both supporting ends in EDGE_EVIDENCE.jsonl; no edge audit is inferred from a mathematical KEEP. Retain and skip the earlier drafts.

MODEL_EVIDENCE.json records author and referee served models as UNKNOWN. This packet establishes scoped mathematical review, not the different-model promotion gate. No live promotion, ingestion or retrieval receipt is claimed. BUNDLE_STATE.json separates these states.

measurements.json records the completed 6.652632-second CPU-gated checks: four exact family truth tables, 276 small Boolean functions, independent character sums, and twenty base-coordinate restrictions. The resumed work changes review metadata and packaging; no broad mathematical experiment is repeated. PACKET_VALIDATION.json is structural validation rather than a proof or source/model receipt.

The historical peer sign patch is retained in patches/01_w504_control_signs.diff. w504's current proof has the corrected phase and w506 records its corrected draft; do not reapply the historical patch. No peer proof was edited by w505.

INTEGRATION_HANDOFF.json lists paths, file SHA-256 hashes, scoped KEEP, unresolved proof and model gates, and separate submission/review/ingestion/retrieval states. Hashes establish artifact identity only.

NEXT: Derive a uniform structural estimate forcing some positive-influence coordinate with Delta_i<=K_0 Inf_i for arbitrary Boolean functions with max_i Inf_i<1/16.
''', encoding='utf-8')
    print(json.dumps({'prepared': True, 'latest_draft': str(final), 'independently_checked_claims': 5, 'C006': 'conjecture', 'model_gate': 'UNKNOWN'}))


def handoff():
    state = read('BUNDLE_STATE.json')
    validation = read('PACKET_VALIDATION.json')
    assert validation['passed'] and validation['independently_kept_claims'] == 5
    files = ['SOURCE_STATUS.json', 'ATTEMPT.md', 'CLAIMS.jsonl', 'REVIEW_PACKET.md', 'REPORT.md', 'INDEPENDENT_REVIEW_UPDATE.json', 'MODEL_EVIDENCE.json', 'BUNDLE_STATE.json', 'measurements.json', 'PACKET_VALIDATION.json', 'EDGE_EVIDENCE.jsonl', 'AUDIT_W504.md', 'PEER_AUDIT.json', 'patches/01_w504_control_signs.diff']
    paths = [ROOT / name for name in files] + [Path(state['latest_inbox_path'])]
    hashes = [{'path': str(path.resolve()), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()} for path in paths]
    save('INTEGRATION_HANDOFF.json', {
        'contact': 'codex-01a12190', 'author': 'w505', 'target': 'P0162',
        'latest_draft': state['latest_inbox_path'],
        'file_hashes': hashes,
        'hashes_are_proof': False,
        'scoped_KEEP': ['w505-C001', 'w505-C002', 'w505-C003', 'w505-C004', 'w505-C005'],
        'conditional_reduction': 'w505-C006 checked only assuming its unproved universal coordinate-selection premise',
        'remaining_proof_gap': 'A uniform K_0 for suitable-coordinate selection when every influence is below 1/16.',
        'served_models': {'author': 'UNKNOWN', 'referee': 'UNKNOWN'},
        'different_model_review_gate': 'UNKNOWN; live promotion on hold',
        'states': {'submitted': True, 'scoped_mathematical_review': True, 'bundle_reviewed': False, 'ingested': None, 'retrievable': None},
        'parent_problem_solved': False, 'current_openness': 'UNKNOWN',
        'delivery': 'Prepared for the explicitly named integration contact; delivery receipt is separate.',
    })
    print(json.dumps({'handoff_ready': True, 'files_hashed': len(hashes), 'draft_sha256': hashes[-1]['sha256'], 'handoff_sha256': hashlib.sha256((ROOT / 'INTEGRATION_HANDOFF.json').read_bytes()).hexdigest()}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--handoff', action='store_true')
    arguments = parser.parse_args()
    handoff() if arguments.handoff else prepare()
