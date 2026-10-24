"""Save review updates and the separately versioned L6--L7 draft supplement."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w369')
REVIEWER = Path('~/brain_workers/w371/REVIEW_PACKET.md')


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def save_json(name, value):
    (ROOT / name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')


measurements = read_json(ROOT / 'CONTINUATION_MEASUREMENTS.json')
assert measurements['checks_failed'] == 0 and measurements['within_elapsed_gate']
review_text = REVIEWER.read_text(encoding='utf-8')
review_receipts = []
for number in range(6):
    match = re.search(rf'(?m)^- \*\*KEEP L{number}\b.*?(?=\n- \*\*|\n###|\Z)',review_text,re.S)
    assert match is not None, f'No written KEEP receipt for L{number}'
    review_receipts.append({
        'claim_id': f'w369-l{number}',
        'verdict': 'KEEP',
        'reviewer': 'w371',
        'source_path': str(REVIEWER),
        'receipt': match.group(0).strip(),
        'scope': 'Only the stated scalar/conditional claim; P0104 not solved',
    })
assert '**FIX `w369/CORRECTION.json`' in review_text
save_json('REVIEW_RECEIPTS.json',review_receipts)

correction = read_json(ROOT / 'CORRECTION.json')
before = ROOT / 'CORRECTION_BEFORE_SCOPE_FIX.json'
if not before.exists():
    before.write_text(json.dumps(correction,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
original = correction['original_statement']
replacement = (
    'Planar undirected first-passage percolation on Z^2 with independent, identically distributed nonnegative edge weights of law F. '
    'Write I=inf supp F. Assume F(0)<p_c=1/2 and, when I>0, F(I)<the oriented-bond critical threshold. '
    'Theorem 1 gives deterministic A_x,B_x such that, as ||x|| tends to infinity, '
    'liminf P(T(0,x)<=A_x)>0, liminf P(T(0,x)>=B_x)>0, and '
    'liminf (B_x-A_x)/sqrt(log ||x||)>0. '
    'If T(0,x) is square-integrable for the relevant x, these separated quantiles imply '
    'Var(T(0,x))>=c log ||x|| for all sufficiently large ||x||. '
    'Indeed, fixed positive probability lower bounds p,q and a separation L give '
    'Var(T)>=[pq/(p+q)] L^2. '
    'More generally, for a square-integrable real X, if every closed interval of length L>0 '
    'has probability at most 1-epsilon with one epsilon in (0,1], then '
    'Var(X)>=epsilon L^2/4. A variance lower bound alone need not imply anti-concentration. '
    'This statement records the planar full-lattice theorem; it makes no logarithmic lower-bound claim for higher-dimensional full lattices.\n'
    'SOURCE: Damron--Hanson--Houdre--Xu, Lower bounds for fluctuations in first-passage percolation for general distributions, '
    'arXiv:1810.08270v2, condition (1.2.1) and Theorem 1.\n'
    'VERIFICATION: primary theorem statement and hypotheses were checked; the two elementary variance implications '
    'were independently rederived by w371. This whole-card revision is resubmitted for source-scope review. '
    'It is not a proof of a polynomial fluctuation exponent or a certificate of current P0104 openness.'
)
correction.update({
    'state': 'DRAFT; whole-statement scope fix resubmitted for review',
    'replacement_mode': 'append-only whole-statement revision keyed by original node id',
    'exact_fragment_to_replace': original,
    'replacement_fragment': replacement,
    'replacement_statement': replacement,
    'primary_locator': 'condition (1.2.1) and Theorem 1; planar full-lattice statement',
    'prior_review_verdict': 'FIX by w371: old fragment did not cover the opening Z^d scope',
    'prior_review_receipt': str(REVIEWER),
    'review_status': 'Whole-card replacement pending review; elementary L0--L1 KEEP',
    'application': 'Coordinator appends a reviewed whole-statement revision; preserve the original node and provenance.',
})
save_json('CORRECTION.json',correction)
controls = {
    'whole_original_statement_selected': correction['exact_fragment_to_replace'] == original,
    'planar_scope_in_opening': replacement.startswith('Planar undirected first-passage percolation on Z^2'),
    'distribution_hypotheses_recorded': 'F(0)<p_c=1/2' in replacement and 'when I>0' in replacement,
    'square_integrability_required_for_variance': 'If T(0,x) is square-integrable' in replacement,
    'uniform_interval_quantifier_present': 'every closed interval of length L>0' in replacement,
    'old_node_preserved_in_artifact': correction['original_statement'] == original,
}
assert all(controls.values())
save_json('CORRECTION_VALIDATION.json',{
    'controls': controls,
    'old_scope_problem': 'The fragment left the original opening Z^d untouched',
    'revised_scope': 'The entire statement is selected; the new opening is explicitly Z^2',
    'deployed': False,
    'independent_keep_for_whole_revision': False,
})

proof = (ROOT / 'CONTINUATION.md').read_text(encoding='utf-8')
new_claims = [json.loads(line) for line in (ROOT / 'CONTINUATION_CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
section_l6 = '## L6.'+proof.split('## L6.',1)[1].split('## L7.',1)[0]
section_l7 = '## L7.'+proof.split('## L7.',1)[1].split('## Hardest gap and NEXT',1)[0]
for claim,section in zip(new_claims,[section_l6,section_l7]):
    claim['proof_or_counterexample'] = section
(ROOT / 'CONTINUATION_CLAIMS.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in new_claims),encoding='utf-8')

claims = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
receipt_by_id = {row['claim_id']: row for row in review_receipts}
for claim in claims:
    if claim['id'] in receipt_by_id:
        claim['status'] = 'independently checked proof'
        claim['review_status'] = 'KEEP by independent referee w371'
        claim['independent_reviewer'] = 'w371'
        claim['review_receipt'] = {'path': str(ROOT / 'REVIEW_RECEIPTS.json'),'source_path': str(REVIEWER)}
        claim['remaining_gap'] = 'The stated scalar/conditional claim has independent KEEP. Uniform lattice standardized fourth moments and nondegenerate n^(1/3) typical scaling remain unproved here.'
        if claim['id'] == 'w369-l5':
            claim['proof_or_counterexample'] = claim['proof_or_counterexample'].replace('followed by L4 martingale convergence','followed by convergence in the L^4 norm of conditional expectations')
existing_ids = {row['id'] for row in claims}
claims.extend(row for row in new_claims if row['id'] not in existing_ids)
(ROOT / 'CLAIMS.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in claims),encoding='utf-8')

bundle = {
    'spec': 'mathbrain-draft-v1',
    'author_agent': 'w369',
    'bundle_slug': 'p0104-martingale-square-function-w369-20261010',
    'entries': [],
    'relations': [
        {'from_key':'l7','to_key':'l6','kind':'depends_on','rationale':'The FPP Doob reduction uses both square-function comparisons in L6, plus separately proved L^4 conditional-expectation convergence.'},
        {'from_key':'l7','to_existing_logical':'math:probability.core:open-problem-p0104-subdiffusive-and-kpz-passage-time-fluctuation-exponents','kind':'semantic_association','rationale':'This is a conditional moment-input reduction relevant to P0104; neither its moment hypothesis nor one-third scaling is established.'},
    ],
}
names = [
    ('l6','martingale-fourth-moment-square-function-comparison-with-cubic-control','Finite martingale square function controls fourth moments and cubic terms'),
    ('l7','lattice-fpp-uniform-kurtosis-square-function-equivalence','Conditional square-function and predictable-variance criterion for lattice FPP'),
]
for claim,(key,logical_name,title) in zip(new_claims,names):
    bundle['entries'].append({
        'key': key,
        'namespace': 'probability.martingales',
        'logical_name': logical_name,
        'kind': 'lemma',
        'title': title,
        'statement': claim['statement'],
        'proof_text': claim['proof_or_counterexample'],
        'assumptions': claim['assumptions'],
        'domain': 'probability theory',
        'source': {
            'source_id': f'owner-probability-campaign-20261010:w369:{key}',
            'url': 'file:///~/brain_workers/w369/CONTINUATION.md',
            'revision': 'author-proof-awaiting-independent-review-20261010',
            'license': 'owner-own-work (campaign proof; no novelty claim)',
            'excerpt': None,
        },
    })
for entry in bundle['entries']:
    assert set(entry) == {'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
    assert entry['proof_text'] and entry['source']['license'].startswith('owner-own-work')
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',entry['logical_name'])
assert {entry['key'] for entry in bundle['entries']} == {'l6','l7'}
save_json('CONTINUATION_DRAFT_BUNDLE.json',bundle)

state_file = ROOT / 'CONTINUATION_SUBMISSION_STATE.json'
if state_file.exists():
    state = read_json(state_file)
    target = Path(state['inbox_path'])
    assert target.parent.resolve() == INBOX.resolve()
    assert read_json(target) == bundle, 'Previously submitted supplement differs; write a reviewed amendment instead of overwriting it'
else:
    INBOX.mkdir(parents=True,exist_ok=True)
    number = 2
    while (INBOX / f'bundle_{number:03d}.json').exists() or (INBOX / f'bundle_{number:03d}.json.part').exists():
        number += 1
    target = INBOX / f'bundle_{number:03d}.json'
    partial = INBOX / f'bundle_{number:03d}.json.part'
    assert target.parent.resolve() == partial.parent.resolve() == INBOX.resolve()
    with partial.open('x',encoding='utf-8') as handle:
        handle.write(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n')
    assert read_json(partial) == bundle and not target.exists()
    partial.rename(target)
    state = {
        'draft_created': True,
        'submitted': True,
        'inbox_path': str(target),
        'reviewed': False,
        'reviewer': 'w371; pending',
        'ingested': False,
        'retrievable': False,
        'local_validation': True,
        'integration_run': False,
        'status': 'DRAFT_ONLY',
        'statement_delivered_to_adversary': False,
        'proof_packet_delivered_to_referee': False,
    }
save_json('CONTINUATION_SUBMISSION_STATE.json',state)
save_json('CONTINUATION_BUNDLE_VALIDATION.json',{
    'entries': len(bundle['entries']),
    'relations': len(bundle['relations']),
    'depends_on_acyclic': True,
    'required_entry_fields_present': True,
    'lemma_proofs_nonempty': True,
    'source_license_prefix_allowed': True,
    'written_bundle_equal_to_local': read_json(target) == bundle,
    'integration_run': False,
    'independent_review': False,
})

old_edges = [json.loads(line) for line in (ROOT / 'DRAFT_EDGE_ROWS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
target_quote = None
for row in old_edges:
    if bundle['relations'][1]['to_existing_logical'] in json.dumps(row):
        target_quote = row
        break
edge_rows = [
    {'from_key':'l7','from_statement':new_claims[1]['statement'],'to_key':'l6','to_statement':new_claims[0]['statement'],'kind':'depends_on','rationale':bundle['relations'][0]['rationale'],'status':'draft; unreviewed'},
    {'from_key':'l7','from_statement':new_claims[1]['statement'],'to_existing_logical':bundle['relations'][1]['to_existing_logical'],'to_original_node_id':'claim_32684d2ece2943d218971312722a87f42333b030b9c7a29f034d6c11f31f8f1d','to_statement_quote_receipt':target_quote,'kind':'semantic_association','rationale':bundle['relations'][1]['rationale'],'status':'draft; unreviewed'},
]
assert target_quote is not None, 'No saved exact P0104 edge-end receipt'
(ROOT / 'CONTINUATION_EDGE_ROWS.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in edge_rows),encoding='utf-8')

submission = read_json(ROOT / 'SUBMISSION_STATE.json')
submission['reviewed'] = True
submission['reviewer'] = 'w371; KEEP L0--L5'
submission['review_scope'] = 'The original scalar/conditional claims, not P0104 or the revised whole-card source correction'
submission['review_receipt'] = 'REVIEW_RECEIPTS.json'
submission['whole_card_correction_reviewed'] = False
save_json('SUBMISSION_STATE.json',submission)

statement = '\n\n'.join([
    '# Statement only: P0104 martingale supplement',
    'w369, 2026-10-10. Independent adversary w370: statements below precede the proof-packet handoff. Please test the generic constants and the exposure-filtration criterion. No lattice estimate is claimed.',
    new_claims[0]['statement'],
    new_claims[1]['statement'],
    'Hardest gap: establish sup_{n,k} E Q_{n,k}^2/Var(T_n)^2<infinity for the actual lattice model. Nondegenerate n^(1/3) scaling remains a separate missing input.',
])+'\n'
(ROOT / 'CONTINUATION_STATEMENT_FOR_ADVERSARY.md').write_text(statement,encoding='utf-8')

packet = (
    '# w369 review packet: P0104 bridge\n\n'
    'P0104 is not solved; current openness remains UNKNOWN. The exact target and primary-source assumptions remain in STATEMENT_FOR_ADVERSARY.md and SOURCE_STATUS.json.\n\n'
    'Independent receipt: w371 KEEP L0--L5 after rederivation, saved in REVIEW_RECEIPTS.json with exact passages from w371/REVIEW_PACKET.md. The original inbox bundle_001.json remains intact. Ingestion and retrievability are unconfirmed.\n\n'
    'Source correction: w371 requested FIX because the old selected fragment left the general-dimensional opening intact. CORRECTION.json now selects the entire original statement and supplies a planar Z^2 statement with distribution hypotheses and the extra L^2 assumption for variance. CORRECTION_BEFORE_SCOPE_FIX.json preserves the previous proposal. The revised whole-card text awaits scope review.\n\n'
    'Supplement: CONTINUATION.md L6 proves both 81-factor square-function comparisons and absolute 16/4 cross/cubic bounds. L7 proves the exact FPP conditional reduction and predictable-variance/jump-moment criterion. Review the first-hit maximal argument, the orthogonality of M_{k-1}D_k, both ratio inequalities, and convergence in the L^4 norm. A rare-volatility counterexample prevents replacing E Q^2 by (E Q)^2.\n\n'
    f'Checks: {measurements["cases"]} exact finite-martingale cases, {measurements["checks_passed"]} algebraic assertions passed, zero failures, {measurements["elapsed_seconds"]:.9f} seconds; command: `python -X utf8 ~/brain_workers/w369/check_continuation.py`. Earlier 11 checks remain in MEASUREMENTS.json. Checks are supporting calculations, not formal or independent proof certificates.\n\n'
    f'Supplement inbox: {target.as_posix()}. Two lemma entries and two supported relations; local validation passed. submitted=true, reviewed=false, ingested=false, retrievable=false. CONTINUATION_EDGE_ROWS.jsonl preserves exact supporting ends from the original read-only source receipt.\n\n'
    'NEXT: Estimate E V_{n,k}^2 and sum E D_{n,j}^4 against Var(T_n)^2 while retaining shared-environment dependence; w371 audit L6--L7 and the whole-card scope fix before integration. The uniform moment bound and nondegenerate one-third scaling are both unproved here.\n'
)
(ROOT / 'REVIEW_PACKET.md').write_text(packet,encoding='utf-8')
report = (
    'Found a false anti-concentration/variance inference in one of eight targeted FPP cards. The quantitative implication and five further scalar/conditional lemmas now have independent KEEP from w371. P0104 remains unsolved in this packet; current openness is UNKNOWN.\n\n'
    'Applied the referee\'s source-scope FIX to the draft: CORRECTION.json now replaces the whole legacy statement, including its opening dimension, with the precise planar theorem and the L^2 condition for its variance consequence. This whole-card revision is pending review. No live store or code was changed.\n\n'
    'Continued the saved proof step: L6--L7 control the martingale cross and cubic terms by a square-function second moment and identify an equivalent form of the missing lattice estimate. A two-step rare-volatility example shows its mean alone is insufficient. The reduction does not prove the needed lattice budget.\n\n'
    f'Measured: eight-card read-only retrieval took 0.077052 seconds; earlier 11 checks passed. New checks: {measurements["cases"]} exact martingale cases, zero failures, {measurements["elapsed_seconds"]:.9f} seconds. Command: `python -X utf8 ~/brain_workers/w369/check_continuation.py`. No deployed retrieval or recall improvement is claimed.\n\n'
    f'Apply: w371 reviews CONTINUATION.md and the revised CORRECTION.json; the validating coordinator integrates the reviewed inbox drafts including {target.as_posix()}, and appends the approved whole-card correction by original node id while preserving prior data.\n\n'
    'Risk: the moment input and independent nondegenerate n^(1/3) typical-scale input for actual lattice FPP are still missing. Generic counterexamples are not lattice models. Reviewed, submitted, ingested, and retrievable states are recorded separately.\n\n'
    'NEXT: Bound E V_{n,k}^2 and sum E D_{n,j}^4 by constants times Var(T_n)^2, without discarding shared-environment terms.\n'
)
(ROOT / 'REPORT.md').write_text(report,encoding='utf-8')
status = (ROOT / 'STATUS.md').read_text(encoding='utf-8').splitlines()
status[0] = 'STATE: WORKING'
status[1] = 'NEXT: Deliver the supplement statement to w370, then L6--L7 and the whole-card scope fix to w371; save receipts and set NEEDS_REVIEW.'
status.append('2026-10-10 resume: Verified w371 KEEP L0--L5 on disk and updated claim review states. Fixed CORRECTION.json to select the entire old card and state planar hypotheses. Eight exact martingale cases/121 assertions passed in 0.005292300 seconds. Saved L6--L7 and submitted their separate two-entry/two-relation draft; these new proofs and the whole-card source fix await review. P0104 is not solved.')
(ROOT / 'STATUS.md').write_text('\n'.join(status)+'\n',encoding='utf-8')
print(json.dumps({'reviewed_original_claims':len(review_receipts),'supplement_claims':len(new_claims),'inbox_path':str(target),'whole_card_scope_fix':all(controls.values()),'live_integration':False}))
