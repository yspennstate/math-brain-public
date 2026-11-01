"""Record reviewable final state after the bounded checks and handoffs succeed."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def main():
    check = json.loads((ROOT / 'CHECK_RESULTS.json').read_text(encoding='utf-8'))
    patch = json.loads((ROOT / 'PATCH_CHECK.json').read_text(encoding='utf-8'))
    bundle = json.loads((ROOT / 'BUNDLE_VALIDATION.json').read_text(encoding='utf-8'))
    source = json.loads((ROOT / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))
    assert check['status'] == bundle['status'] == 'PASS'
    assert patch['exit_code'] == 0, 'Archive patch must pass before marking ready'
    assert Path(bundle['draft_path']).is_file()
    rows = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
    for row in rows:
        if row['claim_id'] == 'w462-C0048-scope-001':
            row['statement'] = source['exact_target']
            row['source']['primary_source'] = source['primary_source']
            row['remaining_gap'] = source['hardest_gap'] + '; current openness remains UNKNOWN'
            row['proof_or_counterexample'] = 'Primary target recovered; no proof of the conjecture is claimed.'
    (ROOT / 'CLAIMS.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows), encoding='utf-8')
    edge = {
        'row_id': 'w462-C0048-edge-Q1', 'status': 'sketch', 'kind': 'semantic_association',
        'from_logical': 'math:probability.randomcluster:potts-integer-versus-real-cluster-weight-quantifier-warning',
        'to_existing_logical': 'math:probability.statmech:open-problem-c0048-discontinuity-of-the-potts-phase-transition-on-z-d-for-q-3-d-3',
        'from_statement_quote': 'If q_c is a threshold over real cluster weights, discontinuity for every integer q>=3 together with continuity at q=2 does not logically imply q_c=2.',
        'to_statement_quote': '(equivalently q_c(d) = 2 for all d >= 3)',
        'statement': 'Associate the conditional real-q quantifier warning with the existing C0048 scope card; this is not a refutation edge to C0048.',
        'assumptions': ['The new concept must first be ingested under its stated logical name', 'q_c is interpreted over real q for the warning', 'The current source card and logical identifier were read from the canonical store in read-only mode'],
        'source': {'license': 'owner-own-work', 'new_end': 'DRAFT_BUNDLE.json real-q-scope', 'existing_end': 'STORE_PRIOR_CHECK.json first row; metadata logical_id read-only query'},
        'proof_or_counterexample': 'Q1 supplies the monotone q>5/2 countermodel. The old source card explicitly contains the quoted equivalence, so the association flags its quantifier ambiguity without changing the conjecture.',
        'independent_reviewer': 'w464 pending; coordinator obtains required independent edge audit before landing',
        'remaining_gap': 'Q1 source-context review and new-node resolution; no live edge has been written',
    }
    (ROOT / 'CROSS_EDGE_PROPOSAL.jsonl').write_text(json.dumps(edge) + '\n', encoding='utf-8')
    receipts = {
        'statement_first': {'to': 'w463', 'message_id': 'msg-a71e0f50ca', 'state': 'delivered'},
        'complete_packet': {'to': 'w464', 'message_id': 'msg-1954f0e7ae', 'state': 'delivered, review pending'},
        'progress_post': 'pd_progress.py returned logged for S1.C0048',
        'archive_patch': 'PATCH_CHECK.json exit_code=0',
        'served_model': 'UNKNOWN', 'parent_problem_solved': False,
    }
    (ROOT / 'HANDOFF_RECEIPTS.json').write_text(json.dumps(receipts, indent=2) + '\n', encoding='utf-8')
    source['handoffs'] = receipts
    source['cross_edge_proposal'] = str(ROOT / 'CROSS_EDGE_PROPOSAL.jsonl')
    source['states']['reviewed'] = {'state': 'pending', 'referee': 'w464', 'request_message_id': 'msg-1954f0e7ae'}
    (ROOT / 'SOURCE_STATUS.json').write_text(json.dumps(source, indent=2) + '\n', encoding='utf-8')
    with (ROOT / 'REPORT.md').open('a', encoding='utf-8') as file:
        file.write('\nArchive patch dry run passed: git apply --check patches/01_C0048_boundary_packet.diff (PATCH_CHECK.json). A proposed semantic association to the existing canonical C0048 card is saved in CROSS_EDGE_PROPOSAL.jsonl with both endpoint quotes and its exact logical identifier; review and landing are pending. Statement-first and full-packet handoffs are recorded in HANDOFF_RECEIPTS.json.\n')
    with (ROOT / 'REVIEW_PACKET.md').open('a', encoding='utf-8') as file:
        file.write('\nSupplement: CROSS_EDGE_PROPOSAL.jsonl quotes both the draft Q1 card and the existing canonical C0048 card. Its existing logical identifier was confirmed from metadata in read-only mode. This proposed semantic association requires the source-context check; it does not assert a false C0048 theorem or write a live edge. HANDOFF_RECEIPTS.json records the actual statement-first and referee request receipts. Archive patch check passed.\n')
    (ROOT / 'STATUS.md').write_text('''STATE: NEEDS_REVIEW
NEXT: w464 checks L1's conditional chain, W1's partition counts and Q1's real-q interpretation; the coordinator lands only reviewed scope.

2026-10-10: Recovered C0048 from primary Conjecture 2 and the exact intake; canonical target and failed contour-attempt cards were read without store writes. Current openness UNKNOWN; no parent-problem proof or novelty claim.
2026-10-10: Brain recall timed out at 60 seconds. Used the named perceptron proof-gap scar; no marginal-product or pipeline-completion claim is treated as proof.
2026-10-10: Saved L1-L3, exact witness W1 and conditional quantifier warning Q1. Single hardest gap: theta^w(p_c,3)>0 on nearest-neighbor Z^3.
2026-10-10: Exact check PASS: 3456 weighted configurations, 12096 edge conditionals, 1728 cut conditionals, 81 history conditionals, 27/27 joint bounds; incorrect marginal products fail 18/27. Runtime 0.210784 seconds. Six concept drafts and four relations staged in math-brain-inbox/w462/bundle_001.json, with review/ingestion/retrieval tracked separately.
2026-10-10: Initial team_comm handoff lacked membership and mesh kind=claim was unsupported. Used supported mesh message/request kinds; statement delivered to w463 as msg-a71e0f50ca, complete packet to w464 as msg-1954f0e7ae. No team was created.
2026-10-10: Corrected the new-file archive patch header; git apply --check PASS. Saved REPORT.md, REVIEW_PACKET.md, HANDOFF_RECEIPTS.json, local hook proposal and quoted canonical cross-edge proposal. Mathematical independent review remains pending; live theorem admission and retrieval have not been observed.
''', encoding='utf-8')
    print(json.dumps({'state': 'NEEDS_REVIEW', 'claim_rows': len(rows), 'draft_concepts': bundle['entries'],
                      'relations': bundle['relations'], 'patch_check': 'PASS',
                      'referee_request': 'msg-1954f0e7ae', 'parent_solved': False}, indent=2))


if __name__ == '__main__':
    main()
