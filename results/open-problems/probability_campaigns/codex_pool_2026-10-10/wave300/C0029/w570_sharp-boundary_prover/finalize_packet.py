"""Record measured results, source status and review hashes; do not integrate."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
measured = json.loads((ROOT / 'MEASUREMENTS.json').read_text(encoding='utf-8'))
assert measured['all_checks_passed'] and measured['compute_gate']['passed']

sources = {
    'candidate': 'C0029', 'worker': 'w570', 'date': '2026-10-10',
    'current_openness': 'UNKNOWN',
    'openness_scope': 'No complete solution found in the bounded named-record and primary-literature check; absence of a search hit is not certification of openness.',
    'exact_target': 'For iid uniform {-1,1} real n by n B_n, there exists fixed c in (0,1) such that for every n>=1 and epsilon>=0, P(s_min(B_n)<=epsilon/sqrt(n))<=epsilon+c^n.',
    'primary_statement_recovered': True,
    'sources': [
        {'url': 'https://arxiv.org/pdf/math/0212413', 'revision': 'v1, 2002-12-01',
         'authors': 'Daniel A. Spielman; Shang-Hua Teng', 'title': 'Smoothed Analysis of Algorithms',
         'locator': 'Conjecture 2, printed p.605, PDF page 9',
         'statement_checked': 'Inverse operator norm tail; modern least-singular-value form recovered by substitution and epsilon+h continuity from above.',
         'notation_note': 'Extracted original text uses d for dimension and n in exponential remainder; the modern source consistently uses n.',
         'byte_hash_verified': False},
        {'url': 'https://arxiv.org/html/2405.20308v2', 'revision': 'v2, 2025-01-08',
         'authors': 'Ashwin Sah; Julian Sahasrabudhe; Mehtaab Sawhney', 'title': 'On the Spielman-Teng Conjecture',
         'locator': 'Equation (2), Theorems 1.1 and 1.2',
         'statement_checked': 'Target coefficient is exactly one; proved upper bound has 1+O_xi((log n)^(-1/16)) factor for all epsilon>=0.',
         'byte_hash_verified': False},
        {'url': 'https://websites.umich.edu/~rudelson/papers/rv-ICM2010.pdf',
         'title': 'Non-asymptotic theory of random matrices: extreme singular values',
         'locator': 'Gaussian least singular value discussion and equation (3.2)',
         'statement_checked': '1-exp(-epsilon-epsilon^2/2) is under an n->infinity limit; the all-n Gaussian bound <=epsilon is separate.',
         'access_scope': 'Primary-source search extract checked; not a whole-paper read or byte-hash check.'},
        {'url': 'https://arxiv.org/abs/1812.09016', 'authors': 'Konstantin Tikhomirov',
         'title': 'Singularity of random Bernoulli matrices',
         'statement_checked': 'Singularity probability has exponential rate (1/2+o_n(1))^n; this does not establish a collision-dominance prefactor.'}
    ],
    'prior_records': [
        {'path': '~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/RANKING_2026-09-07.csv', 'line': 428},
        {'path': '~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl', 'line': 29,
         'source_id': 'bordenave_chafai_circular_2012', 'source_url': 'https://arxiv.org/pdf/1109.3343',
         'primary_pdf_content_here': 'Not read; statement instead independently recovered from original ST source.',
         'scope': 'All large n and all small t>=0; keep this historical wording distinct from the original all-epsilon statement.'},
        {'path': '~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl', 'line': 23,
         'attempt_id': 'C0029-A001', 'finding': 'Incorrect finite-n exact-Gaussian-law sentence; scoped correction proposed.'}
    ],
    'targeted_prior_searches': {
        'attempts_H_20260912': 'No C0029 or Spielman-Teng match in targeted text files.',
        'attempts_I_20260914': 'No C0029 or Spielman-Teng match in targeted text files.',
        'prob1000_lean_20260908': 'Ranked entry only; no matching proof file found.',
        'Team_O': 'No C0029 row on W0300_O/TEAM_BOARD.md.',
        'owner_solved_retired': 'Relevant recall concerns a different Gaussian-submatrix target; no solved/retired certificate for C0029 recovered.'
    },
    'brain_scars': ['perceptron_proof_open_gaps_fleet_2026_07_12', 'open_problem_least_sv_submatrix_2026_07_06'],
    'served_model_evidence': {'author': 'UNKNOWN: no response-side served-model receipt available',
                              'referee': 'UNKNOWN: no independent audit receipt yet',
                              'requested_settings_are_evidence': False,
                              'different_model_review_gate_met': False},
    'promotion': 'DRAFT ONLY; no parent-problem solved claim; no live store write'
}
(ROOT / 'SOURCE_STATUS.json').write_text(json.dumps(sources, indent=2) + '\n', encoding='utf-8')

claim_path = ROOT / 'CLAIMS.jsonl'
claims = [json.loads(line) for line in claim_path.read_text(encoding='utf-8').splitlines() if line]
for c in claims:
    c['measurement'] = {'path': str(ROOT / 'MEASUREMENTS.json'),
                        'independent_audit': False, 'formal_check': False}
if not any(c['id'] == 'w570-C0029-CORRECTION-01' for c in claims):
    claims.append({'id': 'w570-C0029-CORRECTION-01',
        'statement': 'The formula 1-exp(-t-t^2/2) is not the exact finite-n Gaussian least-singular-value CDF: at n=1 the exact CDF is erf(t/sqrt(2)).',
        'assumptions': 't>=0; real standard-normal 1 by 1 matrix for the finite-size counterexample; the other formula is the n->infinity limit.',
        'source': 'owner-own-work: ATTEMPT.md prior digest; Rudelson-Vershynin ICM 2010 primary survey',
        'prior_source_quote': "For the Gaussian matrix Edelman's exact law gives P(sqrt n s_n <= t) = 1 - e^{-t^2/2 - t}",
        'proof_or_counterexample': 'Integrate the standard-normal density over [-t,t]. At t=0.1 the finite and limiting CDF differ by ' + str(measured['gaussian_finite_law_correction']['absolute_difference']) + '.',
        'independent_reviewer': 'w572; pending', 'remaining_gap': 'Independent review and coordinator correction of the existing concept only.',
        'status': 'proved special case', 'live_store_changed': False})
claim_path.write_text(''.join(json.dumps(c, ensure_ascii=False) + '\n' for c in claims), encoding='utf-8')

bad = [r for r in measured['collision_checks'] if r['incorrect_independence_absolute_error'] != '0']
table = '\n'.join('| {n} | {normalized_matrices} | {collision_probability} | {incorrect_independence_probability} |'.format(**r)
                  for r in measured['collision_checks'])
report = f'''The packet proves four boundary claims as author work: joint projective collision constraints, an exact collision probability, the sharp leading collision atom, and a corank-one counterexample to a two-coordinate witness bridge. It also proposes one correction to the prior Gaussian-law statement. Independent review and served-model evidence are pending; the exact-one parent target is not solved here.

The command `python -X utf8 ~/brain_workers/w570/verify_boundary.py` passed {measured['partition_pair_checks']} joint-partition checks against original matrices of sizes 1-3, exact collision counts over {measured['total_normalized_matrices']:,} normalized matrices of sizes 1-5, and eight rational-rank counterexample checks of sizes 5-12. It used {measured['cpu_seconds']:.3f} CPU seconds and {measured['elapsed_seconds']:.3f} wall seconds after a fresh compute gate. No GPU, model load, process-priority change or live-store write was used.

The incorrect baseline treats the row- and column-collision events as independent. It disagrees with exact enumeration in {len(bad)} of 5 sizes; the exact formula disagrees in 0 of 5. This is a correctness repair, not a claimed speed improvement. At n=2 the baseline gives 3/4 and the exact answer is 1/2. The two-sparse collision event is only a subset of singularity.

| n | Normalized matrices | Exact collision probability | Incorrect independence probability |
|---|---:|---:|---:|
{table}

At n=1,t=0.1 the exact Gaussian CDF is {measured['gaussian_finite_law_correction']['exact_CDF']:.12f}; the limiting law gives {measured['gaussian_finite_law_correction']['limiting_CDF']:.12f}. Calling the limiting law finite-size exact introduces an absolute error {measured['gaussian_finite_law_correction']['absolute_difference']:.12f}.

Reviewer application: apply patches/01_C0029_gaussian_scope.diff to the single C0029-A001 intake row only after checking its old line, then use STORE_CORRECTION.json to revise the named concept through the normal coordinator integration process. The patch preserves historical author text and adds an explicit correction. Do not apply a raw patch to the sqlite store.

Brain draft: ~/math-brain-inbox/w570/bundle_001.json contains 8 entries and 7 relations. Submitted=true, reviewed=false, ingested=false, retrievable=false. A DRAFT submission is not an ingestion or recall receipt. The coordinator alone integrates after the corresponding proof and model-review gates. The hook proposal C0029-w570-01 is in primary_directive/hooks1000/proposals/math-w570.jsonl.

The remaining risk is the collision-free singular/small-singular-value complement. No estimate of its probability is proved, and the exact-one coefficient at intermediate scales remains the single hardest gap. Current openness and novelty are UNKNOWN. Finite checks do not certify an all-n theorem or a formal proof.

NEXT: w572 independently rederives the joint partition count and inclusion-exclusion formula; then examine a coefficient-one small-ball estimate on the complement of the collision event.
'''
(ROOT / 'REPORT.md').write_text(report, encoding='utf-8')

files = ['ATTEMPT.md', 'CLAIMS.jsonl', 'SOURCE_STATUS.json', 'verify_boundary.py',
         'MEASUREMENTS.json', 'COUNTEREXAMPLE_N5.json', 'STORE_CORRECTION.json',
         'RELATION_EVIDENCE.json', 'patches/01_C0029_gaussian_scope.diff', 'REPORT.md']
receipts = [{'path': str(ROOT / name), 'sha256_for_peer_review': hashlib.sha256((ROOT / name).read_bytes()).hexdigest()}
            for name in files]
(ROOT / 'REVIEW_HASHES.json').write_text(json.dumps({'purpose': 'Content identity for peer review, not store cryptographic ceremony',
                                                   'files': receipts}, indent=2) + '\n', encoding='utf-8')
hash_table = '\n'.join('| ' + Path(r['path']).name + ' | ' + r['sha256_for_peer_review'] + ' |' for r in receipts)
packet = f'''# C0029 sharp-boundary review packet: w570 -> w572

Please return KEEP/FIX/DROP separately on P1-P4 and the Gaussian-scope correction. All mathematics is author-checked only. No novelty or solved-parent claim. Adversary statement delivered first to w571 as msg-2709a5e6df.

Read ATTEMPT.md for the complete target, original-source conversion at atoms, prior-attempt digest, proofs and single hardest gap. P1's load-bearing step is the uniform dephased bit matrix with (a-1)(b-1) free block values; P2's is the connected-graph/partition inclusion-exclusion and signed Stirling weights. Independently rederive these instead of relying on the numerical receipt. For P4, verify rank(B)=1+rank(D), support-four kernel and no projective repetitions. P3 refutes only epsilon+K2^-n, never the actual target with c>1/2.

Reproduce: `python -X utf8 ~/brain_workers/w570/verify_boundary.py`. The script checks the fresh live governor state and exits before experiments on distress/throttle/stop/unknown modes. Published owner_present_polite policy allows the existing single-process scope; no resource limits are changed.

MEASUREMENTS.json records {measured['total_normalized_matrices']:,} normalized matrices, {measured['partition_pair_checks']} original-matrix partition checks, eight exact rational counterexamples, and the false finite-Gaussian law boundary. These checks are neither an independent audit nor a formal proof. No Lean receipt or admitted placeholder is claimed.

The proposed store correction targets only claim_cbd6e1bc44ea67c88a3ad2112abab63bbfcf63f991be2eeccb063fdba514f1fa / logical attempt-c0029-spielman-teng-conjecture-on-the-least-singular-value-of-bernoulli-matr. Keep its historical attempted-unsolved status. Do not promote the parent target from these lemmas.

Bundle: ~/math-brain-inbox/w570/bundle_001.json. Review status is in DRAFT_STATUS.json and every edge's two ends are quoted in RELATION_EVIDENCE.json. No integrator was run. The author and referee response-side served-model receipts are absent, so the different-model gate is UNKNOWN / not met. Requested settings and source hashes do not prove either mathematical soundness or served model identity.

| Artifact | SHA256 for peer review |
|---|---|
{hash_table}

NEXT: Independently derive P1/P2 and audit the scoped Gaussian correction; the coefficient-one bound on the collision-free complement remains open in this packet.
'''
(ROOT / 'REVIEW_PACKET.md').write_text(packet, encoding='utf-8')
print(json.dumps({'review_packet': str(ROOT / 'REVIEW_PACKET.md'), 'claims': len(claims),
                  'normalized_matrices_checked': measured['total_normalized_matrices'],
                  'independence_baseline_failures': len(bad), 'formula_failures': 0,
                  'independent_review': 'PENDING', 'live_store_changed': False}))
