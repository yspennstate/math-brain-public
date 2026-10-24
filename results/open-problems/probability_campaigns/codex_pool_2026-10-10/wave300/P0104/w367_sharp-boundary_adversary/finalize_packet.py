"""Create the local review packet. This script never deploys or ingests."""
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import difflib
import json

ROOT = Path(__file__).resolve().parent
NOW = datetime.now(timezone.utc).isoformat()


def write_json(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    context = json.loads((ROOT / 'TARGET_CONTEXT.json').read_text(encoding='utf-8'))
    probe = json.loads((ROOT / 'SOURCE_PROBE.json').read_text(encoding='utf-8'))
    verification = json.loads((ROOT / 'VERIFICATION.json').read_text(encoding='utf-8'))
    assert verification['result'] == 'PASS'
    assert verification['configurations_checked'] == 2336
    parent_logical = 'math:probability.core:open-problem-p0104-subdiffusive-and-kpz-passage-time-fluctuation-exponents'
    parent = next(node for node in context['live_target_cards']
                  if json.loads(node['metadata_json']).get('logical_id') == parent_logical)
    prior = next(node for node in context['live_target_cards'] if node['id'] != parent['id'])
    export_by_id = {item['record']['id']: item['record'] for item in probe['export_matches']}
    assert all(node['digest'] == export_by_id[node['id']]['digest'] for node in context['live_target_cards'])

    status = {
        'problem_id': 'P0104', 'as_read_utc': NOW,
        'historical_ranking_status': 'attempted_un (2026-09-07)',
        'current_openness': 'UNKNOWN', 'novelty': 'UNKNOWN; not claimed',
        'primary_source_recovered': True,
        'primary_source': {
            'title': '50 years of first passage percolation',
            'authors': ['Antonio Auffinger', 'Michael Damron', 'Jack Hanson'],
            'version': 'arXiv:1511.03262v2 (2016-09-23)',
            'url': 'https://arxiv.org/pdf/1511.03262v2#page=37',
            'locators': 'Questions 13 and 15, printed page 37 / zero-based PDF page 36; context printed pages 34-35',
            'question_13_paraphrase': 'For every d>=2 and suitable edge distributions F, prove chi<1/2; in d=2 identify chi=1/3.',
            'question_15_paraphrase': 'Establish a positive fluctuation exponent in appropriate dimensions.',
            'short_supporting_quote': 'under suitable conditions on F',
            'formalization_limit': 'The source does not fix that distribution class or a unique meaning of variance scaling; context discusses several alternatives and the absence of flat edges.',
        },
        'working_convention_only': 'For an audit of variance powers, fix one law and one direction before n tends to infinity, and state explicitly whether chi is a log-variance limit or a liminf/limsup. No existence is assumed from the title.',
        'supporting_primary_sources': [
            {'url': 'https://arxiv.org/html/1401.0917v2', 'locator': 'Theorem 1.1 and equations (1.2)-(1.4)',
             'checked_scope': 'Ordinary iid nonnegative lattice FPP, d>=2, atom at zero below bond-percolation criticality; exponential moments give concentration at sqrt(n/log n). Uniform[1,1+epsilon] meets those distribution assumptions.'},
            {'url': 'https://arxiv.org/html/1105.4566v3', 'locator': 'Theorem 1.1, conditions A1-A4',
             'checked_scope': 'The KPZ relation is conditional on matching upper and lower exponent definitions, with nearly-gamma and moment assumptions in this theorem; it does not determine the exponent values.'},
            {'url': 'https://arxiv.org/abs/2604.01214v1', 'locator': 'Abstract; submitted 2026-04-01',
             'checked_scope': 'Polynomial improvement concerns a class of rotationally invariant Riemannian FPP, not the general lattice question.'},
        ],
        'canonical_live_store': '~/math-brain-build/local/population/brain.sqlite3 (mode=ro)',
        'canonical_target_node_id': parent['id'], 'canonical_target_digest_as_stored': parent['digest'],
        'canonical_target_statement_as_stored': parent['body'],
        'prior_attempt_node_id': prior['id'],
        'prior_attempt_scope': 'The stored earlier attempt only separates logarithmic variance improvement from a strict power exponent; its non-FPP sum example is not repeated as new work.',
        'prior_checks': [
            'Named H/I attempts and lean reports: id/title-targeted grep found no P0104 result.',
            'Team O lists P0104 unfinished; this is a board status, not a mathematical verdict.',
            'Old original Codex worktree path referenced by C-intake README is absent.',
            'C-intake schema uses C-prefixed ids; recovered P0104 through two id-filtered export rows and exact live-node reads.',
            'Owner Big Open problem directory README was checked for the named probability scope; no exhaustive solved/retired-work check is claimed.',
            'The separate math-research-brain checkout was inspected only for its store locator; a separate canonical-store content search is not certified.',
        ],
        'source_identity_checks': {
            'live_and_export_digests_agree_for_two_selected_nodes': True,
            'original_ledger_bytes_verified': False, 'primary_pdf_byte_hash_verified': False,
            'mathematical_proof_from_hashes': False,
            'legacy_locator_note': 'The imported card gives PDF pages 34 and 40 without a source version. Both recovered questions are on printed page 37 in v2; an older-version comparison is pending.',
        },
        'remaining_target_gap': 'A precise admissible fixed-law class, chosen exponent definition and all matching asymptotic bounds remain necessary. No lemma here controls fixed-law unrestricted optimization beyond its finite window.',
        'formal_check': {'performed': False, 'reason': 'Written elementary proofs and exact diagnostics only.'},
    }
    write_json('SOURCE_STATUS.json', status)

    # Four exact arithmetic checks of the new constant/onset corollary.
    quantitative = []
    for minimum_constant in (2, 3, 10, 100):
        endpoint = minimum_constant ** 3
        epsilon = Fraction(2, endpoint)
        edge_variance = epsilon ** 2 / 12
        passage_variance = endpoint * edge_variance
        assert endpoint * epsilon == 2
        assert passage_variance / edge_variance == endpoint
        quantitative.append({'epsilon': str(epsilon), 'window_endpoint': endpoint,
                             'exact_passage_variance': str(passage_variance),
                             'theta': '2/3', 'necessary_prefactor_if_onset_in_window': minimum_constant})
    write_json('C003_ARITHMETIC.json', {'command': 'python -X utf8 finalize_packet.py',
                                      'checks': quantitative, 'status': 'PASS',
                                      'scope': 'Closed-form rational arithmetic only; no new experiment or asymptotic estimate.'})

    existing_claims = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
    new_rows = [
        {'id': 'w367-C003', 'status': 'proved special case',
         'statement': 'For iid Uniform[1,1+epsilon] nearest-neighbor FPP on Z^d, d>=2, 0<epsilon<=1, theta<1, K=floor(2/epsilon), any bound Var T(0,n e1)<=C Var(tau_e) n^theta for all integers n>=N requires either N>K or C>=K^(1-theta).',
         'assumptions': ['C>0, integer N>=1', 'One fixed law in this necessary-condition statement', 'The claimed upper bound is an additional hypothesis, not established here'],
         'source': 'owner-own-work; w367-C001/C002',
         'proof_or_counterexample': 'ATTEMPT.md C003: if N<=K, substitute n=K into the exact variance identity and divide by positive edge variance.',
         'independent_reviewer': 'w368 (pending)',
         'remaining_gap': 'Independent referee check; this condition is not sufficient and establishes no asymptotic bound.', 'created_utc': NOW},
        {'id': 'w367-A001', 'status': 'independently checked proof', 'kind': 'peer_audit',
         'statement': 'KEEP w366-C1/C2 as fixed-endpoint results: E T(0,n e1)^r is finite iff E min(t1,t2,t3,t4)^r is finite; the Pareto threshold is r<4alpha, with equality divergent. At alpha=1/2 the mean is finite and variance infinite.',
         'assumptions': ['iid finite-a.s. nonnegative square-lattice edge weights', 'n>=1 fixed, r>0', 'Pareto statement has support [1,infinity)'],
         'source': '~/brain_workers/w366/LEMMAS.md C1/C2',
         'proof_or_counterexample': 'AUDIT_W366_C1.md: independently expanded paths, checked true edge independence, strict-tail inequalities, layer-cake transfer and critical Pareto integral.',
         'independent_reviewer': 'w367 (this audit); nominated integrating referee w368 pending',
         'remaining_gap': 'Parent P0104 unresolved; n-dependent constants are not an exponent bound.', 'created_utc': NOW},
        {'id': 'w367-A002', 'status': 'independently checked proof', 'kind': 'peer_audit',
         'statement': 'KEEP w366-C3/C4 as bounded-law finite-window results and a refutation of a normalized variance estimate with common law-independent constant and onset.',
         'assumptions': ['Square-lattice iid Uniform[1,1+epsilon] for the variance and probabilistic sharpness', 'n epsilon<=2 for the identity', 'beta<1 and common C,N only in the refuted estimate'],
         'source': '~/brain_workers/w366/LEMMAS.md C3/C4',
         'proof_or_counterexample': 'INDEPENDENT_OBSTRUCTION.md saved before peer C3/C4 inspection; parity, dogleg and epsilon=1/n arguments agree. ATTEMPT.md records the provenance limit.',
         'independent_reviewer': 'w367 (this audit); nominated integrating referee w368 pending',
         'remaining_gap': 'This does not refute any fixed-law KPZ assertion with law-dependent constants or onset.', 'created_utc': NOW},
    ]
    existing_ids = {row['id'] for row in existing_claims}
    with (ROOT / 'CLAIMS.jsonl').open('a', encoding='utf-8') as handle:
        for row in new_rows:
            if row['id'] not in existing_ids:
                handle.write(json.dumps(row, ensure_ascii=False) + '\n')

    peer_rows = [json.loads(line) for line in Path('~/brain_workers/w366/CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
    audit_rows = []
    reasons = {'w366-C1': 'Deterministic edge-disjoint paths justify the product; all positive-r moments transfer with n-dependent constants.',
               'w366-C2': 'The Pareto integral has threshold r<4alpha and diverges at equality; finite mean does not make the second moment finite.',
               'w366-C3': 'Agrees with the earlier saved independent length/parity proof and essential-endpoint detour witness.',
               'w366-C4': 'Cancellation of positive edge variance and epsilon=1/n are valid only for the law-uniform auxiliary assertion.'}
    for row in peer_rows:
        if row['id'] in reasons:
            audit_rows.append({'source_claim_id': row['id'], 'auditor': 'w367', 'verdict': 'KEEP',
                               'exact_statement_as_read': row['statement'], 'why': reasons[row['id']],
                               'proof_record': 'AUDIT_W366_C1.md' if row['id'] in ('w366-C1', 'w366-C2') else 'INDEPENDENT_OBSTRUCTION.md and ATTEMPT.md',
                               'scope': 'Special-case audit; parent problem unresolved; not two-other-login admission.', 'at_utc': NOW})
    assert len(audit_rows) == 4
    (ROOT / 'PEER_VERDICTS.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in audit_rows), encoding='utf-8')

    source = {'source_id': 'owner-own-work:w367:P0104-boundaries',
              'url': (ROOT / 'ATTEMPT.md').as_uri(), 'revision': 'draft-2026-10-10-v1',
              'license': 'owner-own-work (draft; w368 review pending)', 'excerpt': None}
    entries = [
        {'key': 'sharp-support-threshold', 'namespace': 'probability.fpp',
         'logical_name': 'lattice-fpp-straight-path-sharp-support-threshold', 'kind': 'concept',
         'title': 'DRAFT: sharp straight-path support threshold in lattice FPP',
         'statement': 'UNREVIEWED author-derived special case. In nearest-neighbor undirected FPP on Z^d, d>=2, with every edge weight in [a,b], 0<a<b, and integer n>=1, n(b-a)<=2a implies that T(0,n e1) equals the sum on the straight n-edge path. For iid laws with essential support endpoints a,b, n(b-a)>2a gives positive probability that an edge-disjoint (n+2)-edge dogleg beats that path. This is a finite-distance threshold, not an asymptotic exponent.',
         'proof_text': None, 'assumptions': ['d>=2, n>=1 integer', '0<a<b finite', 'iid with essential endpoints only for positive-probability sharpness'],
         'domain': 'probability theory', 'source': source},
        {'key': 'exact-uniform-variance', 'namespace': 'probability.fpp',
         'logical_name': 'lattice-fpp-uniform-small-noise-passage-variance', 'kind': 'concept',
         'title': 'DRAFT: exact variance in the continuous small-noise FPP window',
         'statement': 'UNREVIEWED author-derived special case. For iid Uniform[1,1+epsilon] edge weights on nearest-neighbor undirected Z^d, d>=2, epsilon>0, integer n>=1 and n epsilon<=2, T(0,n e1) is the straight-path sum, E T=n(1+epsilon/2), and Var T=n epsilon^2/12. These identities use independent weights on a deterministic path. They do not identify an exponent for a fixed law as n tends to infinity.',
         'proof_text': None, 'assumptions': ['iid Uniform[1,1+epsilon]', 'd>=2', 'epsilon>0, n>=1 integer, n epsilon<=2'],
         'domain': 'probability theory', 'source': source},
        {'key': 'constant-onset-tradeoff', 'namespace': 'probability.fpp',
         'logical_name': 'lattice-fpp-small-noise-variance-constant-onset-tradeoff', 'kind': 'concept',
         'title': 'DRAFT: necessary constant/onset tradeoff in normalized FPP variance bounds',
         'statement': 'UNREVIEWED author-derived necessary condition. For iid Uniform[1,1+epsilon] FPP on nearest-neighbor undirected Z^d, d>=2, 0<epsilon<=1, theta<1, K=floor(2/epsilon), suppose C>0 and integer N>=1 give Var T(0,n e1)<=C Var(tau_e) n^theta for every integer n>=N. Then either N>K or C>=K^(1-theta). Consequently no finite common C,N works over all epsilon for theta<1. This refutes only the law-uniform auxiliary bound; the per-fixed-law KPZ question is unaffected. No such asymptotic upper bound is proved here.',
         'proof_text': None, 'assumptions': ['iid Uniform law as stated', 'theta<1', 'The stated upper bound is a hypothesis; C,N may depend on epsilon in the necessary condition'],
         'domain': 'probability theory', 'source': source},
    ]
    relations = [
        {'from_key': 'exact-uniform-variance', 'to_key': 'sharp-support-threshold', 'kind': 'depends_on',
         'rationale': 'The threshold entry gives the straight-path identity under n(b-a)<=2a; with a=1,b=1+epsilon this is exactly the variance entry condition n epsilon<=2.'},
        {'from_key': 'constant-onset-tradeoff', 'to_key': 'exact-uniform-variance', 'kind': 'depends_on',
         'rationale': 'The variance entry states Var T=n epsilon^2/12. At K=floor(2/epsilon), division by Var(tau)=epsilon^2/12 gives C>=K^(1-theta) whenever N<=K.'},
        {'from_key': 'constant-onset-tradeoff', 'to_existing_logical': parent_logical, 'kind': 'semantic_association',
         'rationale': 'The existing P0104 concept asks to "prove a fluctuation exponent strictly below1/2" under "suitable nondegenerate iid passage-time assumptions". This boundary entry explicitly restricts its obstruction to a "law-uniform auxiliary bound" and leaves the fixed-law parent unaffected. It documents a quantifier hazard, not a refutation of P0104.'},
    ]
    bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w367',
              'bundle_slug': 'fpp-small-noise-sharp-boundaries-w367-001', 'entries': entries, 'relations': relations}
    write_json('draft_bundle_001.json', bundle)

    # Offline structural validation only: no integrator call or admission claim.
    keys = {entry['key'] for entry in entries}
    assert len(keys) == len(entries) == 3
    assert all(entry['kind'] == 'concept' and entry['proof_text'] is None for entry in entries)
    assert all(entry['source']['license'].startswith('owner-own-work') for entry in entries)
    assert all('UNREVIEWED' in entry['statement'] for entry in entries)
    for relation in relations:
        assert relation['from_key'] in keys
        assert relation['kind'] in {'depends_on', 'semantic_association'}
        if 'to_key' in relation:
            assert relation['to_key'] in keys
    assert [('exact-uniform-variance', 'sharp-support-threshold'),
            ('constant-onset-tradeoff', 'exact-uniform-variance')] == [(r['from_key'], r['to_key']) for r in relations if r['kind'] == 'depends_on']

    patch_dir = ROOT / 'patches'
    patch_dir.mkdir(exist_ok=True)
    destination = '~/math-brain-inbox/w367/bundle_001.json'
    payload = (ROOT / 'draft_bundle_001.json').read_text(encoding='utf-8').splitlines(keepends=True)
    patch = ''.join(difflib.unified_diff([], payload, fromfile='a/' + destination, tofile='b/' + destination))
    (patch_dir / '01_fpp_boundary_bundle.diff').write_text(patch, encoding='utf-8')
    recovered = ''.join(line[1:] for line in patch.splitlines(keepends=True) if line.startswith('+') and not line.startswith('+++'))
    assert recovered == ''.join(payload)

    hook_dir = ROOT / 'hooks'
    hook_dir.mkdir(exist_ok=True)
    hook = {'id': 'sharp-variance-uniformity-w367-01', 'area': 'math', 'event': 'stage-start',
            'cue': 'A normalized lattice-FPP polynomial variance estimate claims a single constant and onset over every Uniform[1,1+epsilon] edge law.',
            'fire_when': 'Var_F T<=C Var_F(tau) n^theta with theta<1 and common C,N across all small epsilon is used as a bridge.',
            'silent_when': 'One fixed law is used with its own constant/onset, or the argument explicitly allows their deterioration as epsilon tends to zero.',
            'text': 'Check law-uniform constants and onset. Uniform[1,1+epsilon] gives Var T=n epsilon^2/12 when n epsilon<=2. A normalized n^theta bound (theta<1) needs C>=floor(2/epsilon)^(1-theta) or an onset beyond that window. This does not refute fixed-law KPZ.',
            'evidence': 'w367-C003; ATTEMPT.md; C003_ARITHMETIC.json (epsilon=1/500000, K=1000000 requires C>=100 for theta=2/3 if N<=K).',
            'proposer': 'w367'}
    assert len(hook['text']) <= 300
    (hook_dir / 'math-w367.jsonl').write_text(json.dumps(hook, ensure_ascii=False) + '\n', encoding='utf-8')

    # Correct the scope of the original local gate without claiming a later governor check preceded it.
    gate = json.loads((ROOT / 'COMPUTE_GATE.json').read_text(encoding='utf-8'))
    gate.pop('fresh_external_gate', None)
    gate['gate_scope'] = 'Fresh local 2500-state/10-second bound for the original diagnostic; not a shared-governor receipt.'
    gate['annotation'] = 'A later read found shared governor throttle/distress; no heavy computation or rerun was started.'
    write_json('COMPUTE_GATE.json', gate)
    write_json('BRAIN_DELIVERY.json', {'prepared': {'state': True, 'artifact': 'draft_bundle_001.json', 'at_utc': NOW},
                                    'submitted': {'state': False, 'reason': 'Staged in assigned worker folder; deployment restricted to reviewer.'},
                                    'reviewed': {'state': False, 'reviewer': 'w368', 'scope': 'C001-C003 require referee check.'},
                                    'ingested': {'state': False}, 'retrievable': {'state': False},
                                    'intended_inbox_file': destination, 'duplicate_peer_evidence': ['w366-C3', 'w366-C4']})
    write_json('PACKET_VALIDATION.json', {'result': 'PASS', 'command': 'python -X utf8 finalize_packet.py',
                                        'draft_entries': 3, 'relations': 3, 'internal_dependencies_acyclic': True,
                                        'existing_parent_checked_read_only': True, 'patch_recovers_exact_draft': True,
                                        'hook_text_characters': len(hook['text']), 'c003_arithmetic_checks': 4,
                                        'official_integrator_run': False, 'mathematical_referee_receipt': False})
    events = [
        {'agent': 'w367', 'row': 'S1.w367.1', 'event': 'Saved sharp lattice-FPP support threshold and exact continuous-uniform variance window; independent referee pending.', 'evidence': str(ROOT / 'INDEPENDENT_OBSTRUCTION.md')},
        {'agent': 'w367', 'row': 'S1.w367.2', 'event': 'Verified 2336 exact boundary configurations and audited w366-C1/C2/C3/C4 as special cases; fixed-law KPZ unresolved.', 'evidence': str(ROOT / 'VERIFICATION.json')},
        {'agent': 'w367', 'row': 'S1.w367.3', 'event': 'Staged 3 DRAFT concepts, 3 relations and a quantified constant/onset obstruction for w368 review.', 'evidence': str(ROOT / 'REVIEW_PACKET.md')},
    ]
    (ROOT / 'PROGRESS_EVENTS.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in events), encoding='utf-8')

    report = (
        'P0104 source questions are recovered, but their suitable-law class and exponent convention are not fully fixed; current openness and novelty remain UNKNOWN. The older local attempt already explains the logarithmic-versus-power gap.\n\n'
        'The new result is a sharp support threshold: n(b-a)<=2a forces the straight path in lattice FPP. For Uniform[1,1+epsilon], Var T=n epsilon^2/12 in that window. Any normalized n^theta upper bound with theta<1 must have C>=floor(2/epsilon)^(1-theta), or start beyond that window. This is a special case and a uniformity obstruction; it leaves fixed-law KPZ unresolved.\n\n'
        'Measured with python -X utf8 verify_boundaries.py: 2336 configurations, 1168 threshold cases all correct, and positive detour witnesses in all three above-threshold cases (1,2,4 failures). Six continuous-moment identities and four peer-path checks pass. CPU time was 0.03125 s; wall time about 0.034 s. python -X utf8 finalize_packet.py also passes four exact constant/onset examples and validates 3 draft concepts, 3 relations and patch reconstruction. This is offline evidence, not a live recall-improvement measurement or formal proof receipt.\n\n'
        'w366-C1/C2/C3/C4 receive KEEP with their special-case scope. Own C001-C003 still require w368. The finite rectangle cannot certify an infinite-lattice asymptotic exponent. Avoid duplicate ingestion of the shared C3/C4 material.\n\n'
        'Apply after review: install draft_bundle_001.json as ~/math-brain-inbox/w367/bundle_001.json; patches/01_fpp_boundary_bundle.diff is the equivalent unified new-file diff. The coordinator integrates approved material. Hook/progress proposals and brain drafts remain staged in w367; submitted, reviewed, ingested and retrievable are separately false. A later team instruction authorized one direct handoff to w366; TEAM_REPLY.json records it.\n\n'
        'NEXT: w368 independently checks C001-C003, merges peer evidence and deploys the approved special-case bundle.\n')
    (ROOT / 'REPORT.md').write_text(report, encoding='utf-8')
    final_claims = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
    assert len({row['id'] for row in final_claims}) == len(final_claims)
    allowed_status = {'conjecture', 'numerical evidence', 'sketch', 'proved special case', 'independently checked proof'}
    assert all(row['status'] in allowed_status for row in final_claims)
    assert all(all(key in row for key in ('statement', 'assumptions', 'source', 'proof_or_counterexample', 'independent_reviewer', 'remaining_gap')) for row in final_claims)
    for name in ('SOURCE_STATUS.json', 'ATTEMPT.md', 'CLAIMS.jsonl', 'REVIEW_PACKET.md', 'REPORT.md', 'VERIFICATION.json', 'PACKET_VALIDATION.json'):
        assert (ROOT / name).is_file() and (ROOT / name).stat().st_size > 0
    initial = final_claims[0].get('created_utc', '2026-10-10')
    (ROOT / 'STATUS.md').write_text(
        'STATE: NEEDS_REVIEW\n'
        'NEXT: w368 independently checks C001-C003 using REVIEW_PACKET.md; coordinator deploys the reviewed special-case draft.\n\n'
        + initial + ' Started P0104 sharp-boundary adversary task; first claim row saved locally.\n'
        + NOW + ' Completed source recovery, independent sharp-boundary proof, four peer KEEP verdicts, exact 2336-state receipt and offline draft validation.\n'
        + NOW + ' Three own special-case claims remain referee-pending. Parent P0104 unresolved; openness/novelty UNKNOWN. Draft deployment and ingestion are pending.\n', encoding='utf-8')
    print(json.dumps({'state': 'NEEDS_REVIEW', 'own_special_case_claims': 3, 'peer_keep_verdicts': 4,
                      'exact_configurations': 2336, 'draft_entries': 3, 'relations': 3,
                      'packet_validation': 'PASS', 'submitted': False, 'ingested': False}))


if __name__ == '__main__':
    main()
