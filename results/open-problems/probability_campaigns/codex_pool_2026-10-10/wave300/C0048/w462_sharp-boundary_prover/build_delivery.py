"""Build this worker's review files and authorized concept-only DRAFT inbox bundle."""
from pathlib import Path
import difflib
import json

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w462')


def write_json(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    results = json.loads((ROOT / 'CHECK_RESULTS.json').read_text(encoding='utf-8'))
    assert results['status'] == 'PASS' and results['formal_check'] is False
    rows = [json.loads(x) for x in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if x]
    by_id = {x['claim_id']: x for x in rows}
    by_id['w462-C0048-L1']['assumptions'].append('locally finite infinite graph for the infinite-cluster corollary') if 'locally finite infinite graph for the infinite-cluster corollary' not in by_id['w462-C0048-L1']['assumptions'] else None
    own_source = {'source_id': 'owner:C0048:w462:boundary-packet:2026-10-10',
                  'license': 'owner-own-work', 'path': str(ROOT / 'ATTEMPT.md')}
    additions = [
        {
            'claim_id': 'w462-C0048-W1', 'status': 'proved special case',
            'kind': 'exact_finite_counterexample_pending_review',
            'statement': 'On the free FK width-two three-layer ladder with q=3,p=1/2, let A and B mean that the two respective longitudinal two-edge cuts contain an open edge. P(A)=P(B)=409/925, P(A intersection B)=181/925, and P(A intersection B)-P(A)P(B)=144/855625>0. The disjoint cuts are dependent, so multiplying their marginal probabilities does not give an upper bound.',
            'assumptions': ['free boundary', 'q=3', 'p=1/2', 'six vertices and seven edges listed in check_cutsets.py', 'cut crossing means nonempty cut, not actual point connectivity'],
            'source': own_source,
            'proof_or_counterexample': 'ATTEMPT.md derives Z(3)=5550, weight(A complement)=3096 and weight(A complement intersection B complement)=1728 using isolated-edge and four-cycle partition polynomials. Inclusion-exclusion gives weight(A)=2454 and weight(A intersection B)=1086. CHECK_RESULTS.json independently corroborates those ratios by exact enumeration.',
            'independent_reviewer': 'w464 (pending)',
            'remaining_gap': 'Independent check of partition-polynomial counts; no claim about the original target.',
        },
        {
            'claim_id': 'w462-C0048-Q1', 'status': 'proved special case',
            'kind': 'logical_scope_warning_pending_review',
            'statement': 'If q_c is a threshold over real cluster weights, discontinuity for every integer q>=3 together with continuity at q=2 does not logically imply q_c=2. The monotone predicate D(q) iff q>5/2 satisfies these integer assertions while its real threshold is 5/2. The intake parenthetical equivalence needs this quantifier distinction and a definition of q_c.',
            'assumptions': ['q_c is interpreted over real q', 'this is a logical countermodel, not a random-cluster model', 'source-context correction remains conditional until reviewed'],
            'source': {**own_source, 'record_path': '~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl', 'record_line': 48, 'quote': '(equivalently q_c(d) = 2 for all d >= 3)'},
            'proof_or_counterexample': 'Every integer n>=3 exceeds 5/2, but real q=9/4 does not; the real onset threshold of D is 5/2. STORE_PRIOR_CHECK.json shows the parenthetical also occurs in the live source-scope card. No physical phase diagram is constructed.',
            'independent_reviewer': 'w464 (pending)',
            'remaining_gap': 'Check the cited ICM definition of q_c before treating this warning as a source correction.',
        },
    ]
    for row in additions:
        row['created'] = '2026-10-10'
        if row['claim_id'] not in by_id:
            rows.append(row)
            by_id[row['claim_id']] = row
    (ROOT / 'CLAIMS.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in rows), encoding='utf-8')

    entries = []
    catalog = [
        ('target-scope', 'potts-discontinuity-critical-magnetization-conjecture-scope', 'C0048: exact critical magnetization target',
         'CONJECTURE; CURRENT OPENNESS UNKNOWN. For every integer q>=3,d>=3, the zero-field nearest-neighbor unit-coupling Potts model on Z^d is conjectured to satisfy m(beta_c)>0, where its weight is exp(beta sum 1{equal neighboring spins}), m(beta)=(q mu^1_beta(sigma_0=1)-1)/(q-1), and beta_c=inf{beta:m(beta)>0}. Equivalently theta^w(p_c,q)>0 for ordinary FK open connectivity and p=1-exp(-beta). The 2017 primary Conjecture 2 and the 2026-09-07 ranking are dated evidence, not a current openness certificate.', ['integer q>=3', 'integer d>=3', 'zero field', 'nearest-neighbor unit ferromagnetic couplings']),
        ('conditional-cuts', 'fk-conditioned-disjoint-cut-bound', 'FK: sharp conditional product bound for disjoint edge sets', by_id['w462-C0048-L1']['statement'], by_id['w462-C0048-L1']['assumptions']),
        ('finite-strip', 'finite-strip-potts-no-finite-temperature-magnetization', 'Finite-width FK strips: no finite-temperature Potts order', by_id['w462-C0048-L2']['statement'], by_id['w462-C0048-L2']['assumptions']),
        ('degree-six', 'six-regular-amenable-strip-obstruction-potts-ordering', 'Six-regular amenable strip obstructs a degree-only ordering bridge', by_id['w462-C0048-L3']['statement'], by_id['w462-C0048-L3']['assumptions']),
        ('dependent-cuts', 'random-cluster-ladder-disjoint-cut-dependence', 'Exact q=3 ladder witness against marginal-product upper bounds', by_id['w462-C0048-W1']['statement'], by_id['w462-C0048-W1']['assumptions']),
        ('real-q-scope', 'potts-integer-versus-real-cluster-weight-quantifier-warning', 'Integer Potts states do not determine a real-q phase threshold', by_id['w462-C0048-Q1']['statement'], by_id['w462-C0048-Q1']['assumptions']),
    ]
    for key, logical, title, statement, assumptions in catalog:
        if key != 'target-scope':
            statement = 'DRAFT AUTHOR PROOF; INDEPENDENT REVIEW PENDING; NO NOVELTY CLAIM. ' + statement
        entries.append({
            'key': key, 'namespace': 'probability.randomcluster', 'logical_name': logical,
            'kind': 'concept', 'title': title, 'statement': statement, 'proof_text': None,
            'assumptions': assumptions, 'domain': 'probability theory and statistical mechanics',
            'source': {'source_id': own_source['source_id'] + ':' + key,
                       'url': (ROOT / 'ATTEMPT.md').as_uri(), 'revision': 'author-draft-2026-10-10-review-pending',
                       'license': 'owner-own-work', 'excerpt': None},
        })
    relations = [
        {'from_key': 'finite-strip', 'to_key': 'conditional-cuts', 'kind': 'depends_on',
         'rationale': 'From "H is finite connected with m vertices" and to "disjoint nonempty edge sets C_i": the m longitudinal edges in each layer boundary form such disjoint cuts, giving the strip bound.'},
        {'from_key': 'degree-six', 'to_key': 'finite-strip', 'kind': 'depends_on',
         'rationale': 'From "Z Cartesian-product K5" and to "H is finite connected with m vertices": taking H=K5 gives zero finite-temperature magnetization on the six-regular graph.'},
        {'from_key': 'dependent-cuts', 'to_key': 'conditional-cuts', 'kind': 'semantic_association',
         'rationale': 'From "The disjoint cuts are dependent" and to "P(each C_i contains an open edge)<=product_i(1-(1-p)^|C_i|)": the witness explains the conditional chain required by the upper bound.'},
        {'from_key': 'real-q-scope', 'to_key': 'target-scope', 'kind': 'semantic_association',
         'rationale': 'From "threshold over real cluster weights" and to "For every integer q>=3,d>=3": the latter quantifier does not settle the former threshold.'},
    ]
    bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w462',
              'bundle_slug': 'c0048-conditional-cutsets-boundary-w462-20261010',
              'entries': entries, 'relations': relations}
    required = {'key', 'namespace', 'logical_name', 'kind', 'title', 'statement', 'proof_text', 'assumptions', 'domain', 'source'}
    keys = {e['key'] for e in entries}
    assert len(keys) == len(entries) <= 200
    for e in entries:
        assert required <= e.keys() and e['kind'] == 'concept' and e['proof_text'] is None
        assert all(isinstance(e['source'][x], str) and e['source'][x] for x in ['source_id', 'url', 'revision', 'license'])
        assert e['source']['license'].startswith('owner-own-work')
    for rel in relations:
        assert rel['from_key'] in keys and rel['to_key'] in keys
        assert rel['kind'] in {'depends_on', 'semantic_association'}
    # The only dependency chain is degree-six -> finite-strip -> conditional-cuts.
    write_json(ROOT / 'DRAFT_BUNDLE.json', bundle)
    INBOX.mkdir(parents=True, exist_ok=True)
    number = 1
    while (INBOX / f'bundle_{number:03d}.json').exists() or (INBOX / f'bundle_{number:03d}.part').exists():
        number += 1
    final = INBOX / f'bundle_{number:03d}.json'
    part = final.with_suffix('.part')
    write_json(part, bundle)
    part.rename(final)
    assert json.loads(final.read_text(encoding='utf-8')) == bundle
    receipt = {'status': 'PASS', 'command': 'python -X utf8 ~/brain_workers/w462/build_delivery.py',
               'entries': len(entries), 'relations': len(relations), 'all_entry_kinds': ['concept'],
               'official_integrator_run': False, 'no_store_mutation_performed': True, 'draft_path': str(final)}
    write_json(ROOT / 'BUNDLE_VALIDATION.json', receipt)
    source_status = {
        'candidate': 'C0048', 'worker': 'w462', 'current_openness': 'UNKNOWN', 'target_solved': False,
        'exact_target': catalog[0][3],
        'primary_source': {'title': 'Lectures on the Ising and Potts models on the hypercubic lattice',
                           'author': 'Hugo Duminil-Copin', 'url': 'https://arxiv.org/abs/1707.00520',
                           'locator': 'Conjecture 2, printed p. 93; definitions p. 5; FK conversion equation (1.4), p. 8'},
        'prior_attempt': {'id': 'C0048-A001', 'path': '~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl', 'line': 38, 'result': 'No result; contour entropy and 3D transfer obstacles'},
        'prior_searches': ['Exact C0048 in H/I attempt directories and Lean ranking: no additional exact proof found', 'Owner probability project notes/paper/research Potts search: no matching retirement found', 'Read-only canonical-store target and attempt cards saved in STORE_PRIOR_CHECK.json'],
        'recent_primary_evidence': ['https://arxiv.org/abs/2309.06489 (renormalization-group approximation)', 'https://arxiv.org/abs/2501.14320 (finite-size fuzzy-sphere study)', 'https://doi.org/10.1016/j.nuclphysb.2025.116801 (RG study; not full lattice proof)'],
        'source_status_limit': 'Targeted searches cannot certify current openness or a complete owner retirement check.',
        'brain_recall': {'timeout_seconds': 60, 'result': 'timeout', 'fallback_slug': 'perceptron_proof_open_gaps_fleet_2026_07_12'},
        'hardest_gap': 'theta^w(p_c,3)>0 on nearest-neighbor Z^3; no valid critical lower bound established',
        'requested_model': 'gpt-6.1-sol, reasoning max, Fast service tier', 'served_model_evidence': 'UNKNOWN; requested settings are not observed served settings',
        'states': {'submitted': {'state': 'staged DRAFT', 'path': str(final)},
                   'reviewed': {'state': 'pending', 'referee': 'w464'},
                   'ingested': {'state': 'not observed'}, 'retrievable': {'state': 'not checked'}},
    }
    write_json(ROOT / 'SOURCE_STATUS.json', source_status)
    (ROOT / 'REVIEW_PACKET.md').write_text('''# C0048 review packet for w464

Author result: three elementary boundary lemmas, an exact dependent-cut witness, and a conditional integer/real-q warning. No proof of C0048 and no novelty claim. Current openness is UNKNOWN.

Read ATTEMPT.md for complete statements and proofs; CLAIMS.jsonl for six claim rows and their assumptions; CHECK_RESULTS.json for the exact arithmetic receipt; SOURCE_STATUS.json for source status; STORE_PRIOR_CHECK.json for the scoped live-card retrieval. STATEMENT_TO_ADVERSARY.md was sent first to w463 via mesh message msg-a71e0f50ca, before this full packet was sent to the referee. w463 already had an independent minimax lane saved; this cutset lane is disjoint.

Please record KEEP/FIX/DROP per L1, L2, L3, W1 and Q1 in your own folder. Check that partial conditioning and disjointness justify every product; locally finite graphs justify the infinite-path corollary; ordinary connectivity is kept separate from boundary identifications; the Potts parameter normalization and zero-field hypotheses are explicit; the ladder partition counts are correct; and the real-q warning stays conditional on the meaning of q_c. If you introduce new mathematics in the review, w467 is your independent referee.

The exact finite check covered 3456 configurations, 12096 edge conditionals, 1728 full-cut conditionals and 81 history conditionals. Marginal-product bounds failed 18/27 cases; conditional product bounds passed 27/27. All nine q=1 cases attained equality. This is a regression receipt, not a formal-check receipt; there is no Lean theorem or axiom declaration claimed.

The hardest remaining gap is theta^w(p_c,3)>0 on the actual nearest-neighbor lattice Z^3. Z Cartesian-product K5 has linear growth and p_c=1, so its counterexample does not refute C0048 or a bridge requiring p_c<1. The real-q predicate witness is logical and does not construct a physical phase diagram.

All six bundle entries are concepts with explicit draft/review labels. Independent review, ingestion and retrieval remain separate states. The coordinator must handle store integration and any required cross-account audit; do not infer a theorem admission from file or source validation. Actual served-model evidence is unavailable.

NEXT: w464 audits the five result rows and records verdicts; preserve the unresolved Z^3 critical lower bound.
''', encoding='utf-8')
    (ROOT / 'REPORT.md').write_text(f'''C0048 remains unresolved; current openness is UNKNOWN. The reviewable result is a sharp conditional-cut bound, a no-ordering theorem for finite-width strips, a six-regular amenable counterexample to a degree-only bridge, and an exact dependent-cut witness. The live intake also needs care with its integer/real-q parenthetical; that source warning is conditional until the referee checks q_c's definition.

The invalid marginal-product upper bound failed 18 of 27 exact cases. The corrected conditional bound passed 27 of 27, with 12096 edge conditionals, 1728 full-cut conditionals and 81 history conditionals checked over 3456 configurations. Runtime: {results['elapsed_seconds']:.6f} seconds. Command: python -X utf8 ~/brain_workers/w462/check_cutsets.py. General proofs are in ATTEMPT.md; finite computation does not certify the general theorem.

Six concept drafts and four supporting relations are staged at {final}. Bundle validation command: python -X utf8 ~/brain_workers/w462/build_delivery.py. Independent mathematical review is pending; ingestion and retrieval have not been observed. No recall improvement or theorem admission is claimed.

Archive patch application after review: from ~/<private-repo>, run git apply ~/brain_workers/w462/patches/01_C0048_boundary_packet.diff. This adds one research packet under 06_math_research/probability_1000_boundary_w462_20261010/. The validating coordinator handles draft ingestion and source manifests.

Risk: confusing auxiliary wiring with ordinary paths, treating a one-dimensional strip as Z^3, or promoting a pure quantifier witness to a physical phase diagram. The original hardest gap is a positive critical wired order parameter on Z^3 at q=3. A narrow hook proposal, based on the exact dependent-cut witness, is saved locally for review; no global hook was changed.

NEXT: w464 independently reviews L1-L3, W1 and Q1; integration coordinator lands only the reviewed scope.
''', encoding='utf-8')
    patch_dir = ROOT / 'patches'
    patch_dir.mkdir(exist_ok=True)
    relative = '06_math_research/probability_1000_boundary_w462_20261010/C0048_boundary_packet.md'
    diff = ''.join(difflib.unified_diff([], (ROOT / 'ATTEMPT.md').read_text(encoding='utf-8').splitlines(keepends=True),
                                     fromfile='/dev/null', tofile='b/' + relative))
    (patch_dir / '01_C0048_boundary_packet.diff').write_text(
        'diff --git a/' + relative + ' b/' + relative + '\nnew file mode 100644\n' + diff, encoding='utf-8')
    hooks = ROOT / 'hook_proposals'
    hooks.mkdir(exist_ok=True)
    hook = {'id': 'cutset-w462-01', 'area': 'math', 'event': 'PreToolUse',
            'cue': 'A proof proposes an upper bound by multiplying marginal crossing probabilities of FK cutsets with q>1',
            'fire_when': 'q=3,p=1/2 ladder cut marginals 409/925 are multiplied as an upper bound although the joint is 181/925',
            'silent_when': 'q=1 with independent edge sets, or a uniform bound is proved conditional on all previously exposed events',
            'text': 'Disjoint FK cuts need not be independent. Before multiplying upper bounds, prove the bound under the full previous-event history; the q=3 ladder has joint excess 144/855625 over its marginal product.',
            'evidence': '~/brain_workers/w462/CHECK_RESULTS.json witness; 18/27 marginal-product bounds fail',
            'proposer': 'w462'}
    assert len(hook['text']) <= 300
    (hooks / 'cutset-w462.jsonl').write_text(json.dumps(hook) + '\n', encoding='utf-8')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
