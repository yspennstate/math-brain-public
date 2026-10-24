from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parent
now = datetime.now(timezone.utc).isoformat()
referee = Path('~/brain_workers/w509')
receipt = json.loads((root / 'REVIEW_RECEIPT.json').read_text(encoding='utf-8'))
all_rows = [json.loads(line) for line in (referee / 'REVIEW_VERDICTS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
rows = [row for row in all_rows if row.get('claim', '').startswith('w507.P0162.')]
expected = {
    'w507.P0162.L1',
    'w507.P0162.bent-min-split-obstruction',
    'w507.P0162.all-bent-splices',
    'w507.P0162.bent-splice-influence-range',
    'w507.P0162.bent-splice-constant-two-fails',
    'w507.P0162.parity-translation-identity',
}
assert expected <= {row['claim'] for row in rows}
assert all(row['verdict'] == 'KEEP' for row in rows)
(root / 'REFEREE_VERDICTS_SNAPSHOT.jsonl').write_text(
    ''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows), encoding='utf-8')

# Record the review received; this does not perform a new mathematical audit.
receipt.update({'checked_utc': now, 'verdict_rows': rows,
    'snapshot': str(root / 'REFEREE_VERDICTS_SNAPSHOT.jsonl'),
    'review_kind': 'independent analytical proof check by a distinct named peer; served-model provenance unverified',
    'bundle_002_relation': 'w509 KEEP the scoped semantic_association to P0162, not a proves edge',
    'packaging_gate': 'Coordinator review and deduplication still pending'})
(root / 'REVIEW_RECEIPT.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')

mapping = {
    'w507.P0162.restriction-ledger': 'w507.P0162.L1',
    'w507.P0162.bent-min-split-obstruction': 'w507.P0162.bent-min-split-obstruction',
    'w507.P0162.all-bent-splices': 'w507.P0162.all-bent-splices',
    'w507.P0162.bent-splice-influence-range': 'w507.P0162.bent-splice-influence-range',
    'w507.P0162.bent-splice-constant-two-fails': 'w507.P0162.bent-splice-constant-two-fails',
    'w507.P0162.parity-translation-identity': 'w507.P0162.parity-translation-identity',
}
claims = [json.loads(line) for line in (root / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
for claim in claims:
    cid = claim['id']
    if cid in mapping or cid == 'w507.P0162.canonical-global-bound':
        claim['status'] = 'independently checked proof'
        claim['independent_reviewer'] = 'w509; analytical KEEP, response-side model evidence UNKNOWN'
        claim['review_evidence'] = {
            'verdict_file': str(referee / 'REVIEW_VERDICTS.jsonl'),
            'proof_check': str(referee / 'REVIEW_PACKET.md'),
            'snapshot': str(root / 'REFEREE_VERDICTS_SNAPSHOT.jsonl'),
            'verdict_claim': mapping.get(cid),
            'scope': 'L1-L7 only; global FEI and novelty are not certified',
        }
        if cid == 'w507.P0162.canonical-global-bound':
            claim['review_evidence']['scope'] = 'L3 in w509 Verdict 2 and explicit L3, including m=2, in w508 CORE_PROOF_AUDIT.md'
            claim['review_evidence']['additional_check'] = '~/brain_workers/w508/CORE_PROOF_AUDIT.md'
        claim['different_model_gate'] = 'UNVERIFIED'
        claim['remaining_gap'] = {
            'w507.P0162.bent-splice-influence-range': 'Only the bent-splice class is optimized; global FEI and novelty remain unverified.',
            'w507.P0162.bent-splice-constant-two-fails': 'Only C=2 for the broader bent-splice class is refuted; canonical C=2 and general FEI are untouched.',
            'w507.P0162.parity-translation-identity': 'This identity alone gives no global FEI constant.',
            'w507.P0162.restriction-ledger': 'No dimension-free universal local entropy charge follows from the identity.',
        }.get(cid, 'The scoped special-case proof was kept; no global FEI proof or universal good-coordinate argument is supplied.')
    else:
        claim['independent_reviewer'] = 'w509; related context only, not a KEEP of the conjecture or this numerical run'
(root / 'CLAIMS.jsonl').write_text(''.join(json.dumps(c, ensure_ascii=False) + '\n' for c in claims), encoding='utf-8')

source = json.loads((root / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source['mathematical_review'] = {'state': 'KEEP', 'scope': 'ATTEMPT.md L1-L7 only', 'reviewer': 'w509',
    'evidence': str(root / 'REVIEW_RECEIPT.json'), 'checked_utc': now,
    'author_served_model': 'UNKNOWN', 'referee_served_model': 'UNKNOWN', 'different_model_gate': 'UNVERIFIED'}
source['formal_verification']['reason'] = 'Integer and numerical checks are diagnostics, not a formal theorem. Separate analytical KEEP verdicts are recorded in REVIEW_RECEIPT.json.'
(root / 'SOURCE_STATUS.json').write_text(json.dumps(source, indent=2) + '\n', encoding='utf-8')

submission = json.loads((root / 'BRAIN_SUBMISSION.json').read_text(encoding='utf-8'))
submission['mathematically_reviewed'] = True
submission['mathematical_review'] = source['mathematical_review']
submission['reviewed'] = False
submission['reviewed_meaning'] = 'All integration gates; analytical KEEP is recorded separately and does not establish model provenance or complete packaging review.'
submission['ingestion_confirmation'] = 'UNVERIFIED'
submission['retrieval_confirmation'] = 'UNVERIFIED'
submission['review_checked_utc'] = now
submission['promotion_approved'] = False
submission['bundle_review_scopes'] = {
    'bundle_001.json': 'L1-L4 analytical KEEP; definition and unproved good-coordinate concept stay draft; ledger dedupe pending',
    'bundle_002.json': 'L5-L7 analytical KEEP and scoped semantic_association KEEP; concept stays draft pending integration gates',
}
(root / 'BRAIN_SUBMISSION.json').write_text(json.dumps(submission, indent=2) + '\n', encoding='utf-8')

report = '''The distinct result is the exact influence range for every single-point splice of a Boolean bent base, with a fixed spectral entropy and an explicit class extremizer. A five-bit parity twist has I=29/16 and H>469/128>2I; therefore a constant-2 bound cannot transfer to this larger class merely because entropy is unchanged. Every splice in the stated class satisfies H<=3I. The canonical witness and restriction ledger overlap established or peer work and are reproduction only. Global FEI remains unproved; current openness is UNKNOWN and no novelty claim is made.

The completed runs passed 278 Boolean functions, 1,100 ledger checks, 256 initial phase/vertex controls and 240 extension-only cases. Commands: python -X utf8 verify_obstruction.py; python -X utf8 verify_extension.py. Runtime was 0.532 s and 0.100 s, with maximum ledger residual 1.11e-15. In the 11-bit canonical control, the minimum-influence split cost was 14.323620862 versus 3.978237963 for the best observed split. Exact logarithm comparisons, rather than floating-point entropy, prove the five-bit constant-2 counterexample. These completed experiments were not rerun during handoff recovery.

w509 independently kept L1-L7; w508 also kept L1-L3. REVIEW_RECEIPT.json and REFEREE_VERDICTS_SNAPSHOT.jsonl preserve the exact scope. Seven entries and nine relations are submitted in two inbox drafts. The drafts remain concept/definition material; author and referee response-side model evidence is UNKNOWN, and different-model, packaging, ingestion and retrieval gates remain unverified. The single hardest mathematical gap is a universal good-coordinate or aggregate entropy charge throughout restrictions. None of the KEEP verdicts closes that gap.

Apply: codex-01a12190 verifies the remaining integration gates, deduplicates the restriction-ledger material, and integrates only the scoped KEEP material from the two files listed with hashes in INTEGRATION_HANDOFF.json. Existing inbox draft bytes are preserved; their pending labels are superseded only by the attached scoped review receipt, not by a theorem promotion. Communication and progress receipts are recorded separately after the handoff attempt.

NEXT: Obtain integration receipt and model-provenance gate decision from codex-01a12190, then verify retrieval of the accepted exact-range card.
'''
(root / 'REPORT.md').write_text(report, encoding='utf-8')

packet = '''P0162 review packet: independent-route bent-splice analysis, w507, 2026-10-10.

Exact target: for every finite uniform cube and Boolean f taking values -1,+1, find one universal finite C with H_2(f)=sum_S hat(f)(S)^2 log_2(1/hat(f)(S)^2)<=C sum_S |S|hat(f)(S)^2. Zero entropy terms vanish. The parent statement is not proved; current openness is UNKNOWN and novelty is not claimed. Primary-source and prior-attempt records are in SOURCE_STATUS.json.

ATTEMPT.md contains the unchanged complete mathematical derivation. L1 is the established restriction entropy/influence ledger. L2-L3 reproduce the canonical bent-selector obstruction: the selector is uniquely least influential and its entropy charge/influence is unbounded, although the family satisfies H<=3I. L4 extends the exact entropy law and obstruction to every bent base and flipped vertex, for even base dimension m>=4. L5 proves I(F)=m/2+(m+1-2s_g(a))/2^m, attains every s=0,...,m by character twists, and identifies the exact fixed-dimension class maximum of H/I. L6 gives the explicit five-bit counterexample to C=2 for the broader class, with I=29/16 and H>469/128>2I. L7 is the standard character-translation identity, rederived; it is not claimed new.

w509 KEEP L1-L7 is recorded in REVIEW_RECEIPT.json, with exact referee verdict rows in REFEREE_VERDICTS_SNAPSHOT.jsonl. w508 additionally KEEP L1-L3 in its CORE_PROOF_AUDIT.md. These are analytical checks of the supplied claims, not proof of P0162. Author/referee response-side served-model evidence remains UNKNOWN, so the different-model integration gate has not passed.

The bounded measurements and reproduction commands are in MEASUREMENTS.json and EXTENSION_MEASUREMENTS.json, with scripts verify_obstruction.py and verify_extension.py. Integer Walsh and edge comparisons provide independent diagnostic controls; floating-point checks are not a formal theorem receipt. The exact entropy lower bound in L6 is analytic.

Single hardest gap: prove a dimension-free good-coordinate selection or aggregate entropy-charge argument for every Boolean function along a complete restriction tree. The all-coordinate and least-influence rules fail for the displayed family; that failure does not refute the existential good-coordinate principle or global FEI.

Two complete inbox drafts contain seven concept/definition entries and nine relations. The bundle_002 semantic_association to the existing P0162 card was kept with its stated scope; it is not a proves edge. The integration contact is codex-01a12190. INTEGRATION_HANDOFF.json supplies exact file paths, artifact hashes, review evidence, dedupe notes and the remaining gates. No live store or global recall controls were changed by this proof task.

NEXT: codex-01a12190 verifies provenance and packaging gates, deduplicates the ledger, and returns ingestion and retrieval receipts for the scoped draft material.
'''
(root / 'REVIEW_PACKET.md').write_text(packet, encoding='utf-8')

artifact_paths = [root / name for name in (
    'ATTEMPT.md', 'APPROACH_PRECOMMIT.md', 'CLAIMS.jsonl', 'SOURCE_STATUS.json',
    'REVIEW_PACKET.md', 'REVIEW_RECEIPT.json', 'REFEREE_VERDICTS_SNAPSHOT.jsonl',
    'REPORT.md', 'MEASUREMENTS.json', 'EXTENSION_MEASUREMENTS.json',
    'verify_obstruction.py', 'verify_extension.py', 'PACKET_VALIDATION.json',
    'BRAIN_SUBMISSION.json', 'proposals/math-w507.jsonl')]
artifact_paths += [Path(p) for p in submission['bundles']]
artifact_paths += [referee / 'REVIEW_VERDICTS.jsonl', referee / 'REVIEW_PACKET.md',
    Path('~/brain_workers/w508/CORE_PROOF_AUDIT.md')]
artifacts = [{'path': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'bytes': p.stat().st_size} for p in artifact_paths]
assert sum(len(json.loads(Path(p).read_text(encoding='utf-8'))['entries']) for p in submission['bundles']) == 7
assert sum(len(json.loads(Path(p).read_text(encoding='utf-8'))['relations']) for p in submission['bundles']) == 9
assert len(claims) == 10

handoff = {
    'utc': now, 'author_agent': 'w507', 'integration_contact': 'codex-01a12190',
    'target': 'P0162', 'state': 'SCOPED_MATHEMATICAL_KEEP; INTEGRATION_GATES_PENDING',
    'review_scope': 'w509 KEEP L1-L7; w508 KEEP L1-L3; bundle_002 scoped semantic_association KEEP',
    'parent_problem_solved': False, 'current_openness': 'UNKNOWN', 'novelty_claim': False,
    'mathematically_reviewed': True, 'submitted': True, 'ingested': 'UNVERIFIED', 'retrievable': 'UNVERIFIED',
    'served_model_evidence': {'author': 'UNKNOWN', 'referee': 'UNKNOWN',
        'reason': 'No response-side model receipt was supplied in the worker deliverables or referee packet; requested settings and distinct agent IDs do not prove served identities.',
        'different_model_gate': 'UNVERIFIED'},
    'bundles': [{'path': p, 'sha256': next(a['sha256'] for a in artifacts if a['path'] == str(Path(p)))} for p in submission['bundles']],
    'hash_scope': 'Ordinary artifact identity only; not a mathematical proof or integrator source-sealing manifest.',
    'artifacts': artifacts,
    'dedupe': ['Restriction ledger overlaps established 2606.00246v2 and peer drafts; select one canonical representation.',
        'Canonical bent-selector witness overlaps w505; label reproduction. Preserve the arbitrary-bent exact-range and parity counterexample scope.'],
    'remaining_gates': ['Response-side model provenance and different-model review decision',
        'Coordinator packaging/source/relation validation and deduplication', 'Ingestion receipt', 'Actual retrieval receipt'],
    'hardest_remaining_mathematical_gap': receipt['hardest_remaining_gap'],
    'hook': {'state': 'LOCAL_PROPOSAL; NOT AUDITED OR DEPLOYED', 'path': str(root / 'proposals/math-w507.jsonl')},
    'peer_relay': {'w508_packet': '~/brain_workers/w508/REVIEW_PACKET.md',
        'state': 'w509 has independently reviewed w508-MATH-001/002/003 in its own verdict file; no review-of-review performed here'},
    'next': 'Integration contact validates the pending gates and returns an ingestion and retrieval receipt for the scoped exact-range draft.',
}
(root / 'INTEGRATION_HANDOFF.json').write_text(json.dumps(handoff, indent=2) + '\n', encoding='utf-8')
text = '''w507 -> codex-01a12190: scoped P0162 integration handoff.

w509 KEEP L1-L7; w508 KEEP L1-L3. The distinct deliverable is the arbitrary-bent point-splice exact influence range and fixed-dimension H/I extremizer, including the five-bit H>469/128>2I=29/8 example. General FEI remains unproved; the hardest gap is universal good-coordinate selection or an aggregate restriction-tree charge. Current openness is UNKNOWN; novelty is not claimed.

The two inbox files below contain seven concept/definition entries and nine relations. Preserve their draft kinds until the integration gates pass. Existing pending labels are accompanied by REVIEW_RECEIPT.json and the scoped referee snapshot; this packet does not promote the cards to theorems. Deduplicate the established restriction ledger and the canonical witness shared with peers. Author/referee served-model evidence is UNKNOWN; requested models and agent IDs are not response-side evidence. Different-model, packaging, ingestion and retrieval gates are unverified.

'''
text += '\n'.join(f"{b['path']}\nSHA256 {b['sha256']}\n" for b in handoff['bundles'])
text += '\nAll artifact paths/hashes and exact review scope: INTEGRATION_HANDOFF.json. Proof: ATTEMPT.md. Kept verdicts: REVIEW_RECEIPT.json and REFEREE_VERDICTS_SNAPSHOT.jsonl. Ordinary file hashes identify artifacts; they are not proof receipts or integrator source manifests.\n\nNEXT: Verify provenance and packaging, ingest the scoped material, and return the ingestion and retrieval receipt.\n'
(root / 'INTEGRATION_HANDOFF.md').write_text(text, encoding='utf-8')
with (root / 'RESUME_RESULTS.jsonl').open('a', encoding='utf-8') as out:
    out.write(json.dumps({'utc': now, 'result': 'review-scoped integration packet prepared',
        'path': str(root / 'INTEGRATION_HANDOFF.json'), 'kept_lemmas': 'L1-L7',
        'claim_rows': 10, 'draft_entries': 7, 'draft_relations': 9,
        'served_model_gate': 'UNVERIFIED', 'ingestion': 'UNVERIFIED'}) + '\n')
print(json.dumps({'prepared': 'INTEGRATION_HANDOFF.json', 'kept_lemmas': 'L1-L7',
    'draft_entries': 7, 'draft_relations': 9, 'checks': 'review rows and submitted draft counts verified; existing mathematical runs preserved'}))
