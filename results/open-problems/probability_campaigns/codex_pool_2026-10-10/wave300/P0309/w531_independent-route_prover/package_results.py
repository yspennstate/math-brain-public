"""Build local review artifacts; this never writes the live store or shared inbox."""
import difflib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
latest_results = json.loads((ROOT / 'control_results.json').read_text(encoding='utf-8'))
if latest_results.get('status') == 'PASS':
    results = latest_results
elif latest_results.get('status') == 'GATED':
    results = json.loads((ROOT / 'verification_initial/control_results.json').read_text(encoding='utf-8'))
else:
    raise SystemExit('A failed control run must be resolved before packaging.')
if results.get('status') != 'PASS':
    raise SystemExit('No archived passing measurement is available.')
source = {'source_id': 'owner-own-work:w531:P0309:2026-10-10',
          'url': 'urn:math-research:w531:p0309:pressure-route:2026-10-10',
          'revision': 'draft-author-proof-pending-independent-review-20261010',
          'license': 'owner-own-work', 'excerpt': None}


def claim(cid, statement, assumptions, locator, proof, gap, status='proved special case'):
    return {'id': cid, 'target': 'P0309', 'statement': statement, 'assumptions': assumptions,
            'source': dict(source, path=str(ROOT / ('HARMONIC_LEMMAS.md' if locator.startswith('L') else 'PRESSURE_ROUTE.md')), locator=locator),
            'proof_or_counterexample': proof, 'independent_reviewer': 'w533 (review pending)',
            'remaining_gap': gap, 'status': status, 'independently_checked': False, 'formal_check': None}


rows = [
    claim('w531-P0309-STATEMENT-002',
          'The P0309 intake requests low-positive-temperature crystalline Gibbs phases in three-dimensional Coulomb/Riesz regimes predicted by Lewin Section VI; the retrieved intake gives no universally quantified exponent range. The working specialization is a short-range s>3 grand-canonical DLR law periodic under a full-rank lattice and breaking continuous translations.',
          ['This is a specialization, not a universal restatement of the underspecified intake.', 'Current openness UNKNOWN.', 'A renormalized long-range specification is required before claiming Coulomb or s<=3 results.'],
          'Source recovery: STATEMENT_FOR_ADVERSARY.md and prior_target_entries.json',
          'Recovered op-p0309 and at-p0309 exact entries; read Lewin Section VI. Conjecture 38 itself is zero-temperature. Historical status and a limited search are not current-status certificates.',
          'Original crystallization question unproved; exact universal scope is not supplied by the intake.', 'conjecture'),
    json.loads((ROOT / 'claim_002.json').read_text(encoding='utf-8')),
    claim('w531-P0309-L2',
          'For the 3D nearest-neighbor Gaussian displacement field with beta,kappa>0 and reciprocal K!=0, volume before quadratic-pinning removal gives E exp(-iK.u_0)=exp[-|K|^2 G_3/(2 beta kappa)]>0. The shifted-lattice point process is simple, locally finite, lattice-periodic, and has a nonzero intensity Fourier coefficient. Its normalized Fourier average converges in L2 to that amplitude.',
          ['Labelled harmonic reference field with covariance C(r)=(beta kappa)^(-1) integral exp(ikr)/omega(k) dk/(2pi)^3.', 'Lambda=A Z^3, A invertible, A^T K in 2pi Z^3.', 'No Riesz Gibbs membership is asserted.'],
          'L2', 'Gaussian characteristic function, finite covariance, Riemann-Lebesgue, pair Cesaro averaging, and fundamental-cell tiling/Tonelli.',
          'No gap in the reference-model proof; transferring it to the nonlinear unlabelled Riesz gas is unproved.'),
    claim('w531-P0309-L3',
          'For a stationary matched/defect decomposition nu=sum_x J_x delta_(Ax+t+u_x)+eta with J in {0,1}, q_m=1-EJ_0, q_b=Eeta(F), delta=E[J_0 |u_0|^2], v=|det A| and reciprocal K, Re[exp(iK.t)v lambda_hat(K)]>=1-q_m-q_b-|K|^2 delta/2. A positive right side witnesses broken translations; a Gibbs conclusion additionally requires membership in a translation-covariant specification.',
          ['Joint stationarity under integer label shifts; no independence.', 'eta is Lambda-periodic in law.', 'Finite q_b and delta.', 'lambda_hat(K)=v^(-1) integral_F exp(-iK.x) E nu(dx).'],
          'L3', 'Exact tiling formula for the matched coefficient; absolute extra-mass bound q_b; cos z>=1-z^2/2.',
          'No gap in this conditional criterion; a Riesz matching/defect estimate and Gibbs membership are not supplied.'),
    claim('w531-P0309-P1',
          'The unlabelled short-range Riesz torus pressure with bounded source Psi=sum_{j=1}^3 cos(K_j.x) is even, real analytic at finite volume and convex, with p_N prime=E Q/(N^3 v), p_N double-prime=beta Var Q/(N^3 v), and factorial densities bounded by exp[k beta(mu+3|h|)].',
          ['Finite s>3; beta>0; mu,h real; integer N>=1.', 'Lambda=A Z^3 and K_j=2pi A^(-T)e_j.', 'Nonnegative periodized Riesz pair energy.', 'The source is coupled as +beta h Q.'],
          'P1', 'Poisson exponential domination, differentiated partition series, half-cell translation, and insertion bounds after deleting nonnegative interaction terms.',
          'No gap in the finite-volume lemma; it does not establish any thermodynamic pressure cusp.'),
    claim('w531-P0309-P2',
          'Assume P1, the equal-diagonal/equal-off-diagonal positive Gram condition on A, finite limiting pressure p near 0 and m=p right-prime(0)>0. Along a volume-first diagonal with pressure approximation error <=h_l/l, every selected local limit has three real equal intensity Fourier coefficients c_j>=m/3 and intensity translation-period group exactly A Z^3. If that limit is a zero-field Riesz DLR law, it is a periodic Gibbs law breaking continuous translations.',
          ['s>3, beta>0 and finite mu.', 'A^T A has diagonal a, off-diagonal b, a-b>0 and a+2b>0.', 'p_N(h) converges to finite p(h) near zero.', 'm=p right-prime(0)>0.', 'Gibbs conclusion explicitly assumes zero-field DLR membership of the selected limit.'],
          'P2', 'Convex secant bound plus diagonal selection; local moment and boundary-nullness controls pass cell expectations; inversion and basis permutations make three coefficients equal and real; nonzero reciprocal basis coefficients characterize the lattice period group.',
          'Application to P0309 needs a positive zero-source slope for the full gas and verification of zero-field DLR membership. No such slope has been proved.'),
    claim('w531-P0309-P3',
          'Positive response at nonzero pinning does not imply spontaneous order: V independent signs have pressure beta^(-1)log(2cosh(beta h)) and positive response at h>0 but zero right slope at 0. Conversely a collective two-state pressure (beta V)^(-1)log(2cosh(beta V h)) tends to |h| although every finite-volume slope at 0 is zero, and an arbitrary pinning diagonal can still destroy the selected response.',
          ['Exact toy partition functions, not Riesz gases.', 'beta>0 and integer V>=1.'],
          'P3', 'Differentiate both explicit pressures; use h_V=1/(beta V^2) versus h_V=1/sqrt(V).',
          'None for these exact counterexamples; no implication about existence of a Riesz cusp.'),
    claim('w531-P0309-P4',
          'For a trial T on the same unlabelled space with finite D(T||G_N,0) and E_T|Q|, p_N(h)-p_N(0)>=h E_TQ/V_N-D/(beta V_N). Under finite pressure convergence, trial families with liminf_N E_TQ/V_N>=q>0 and limsup_N D/(beta V_N h)<=epsilon(h) tending to zero give p right-prime(0)>=q. A sector Q>=qV_N of probability exp[-o(V_N)] is a sufficient special case.',
          ['P1 zero-source law G_N,0 and source Q.', 'T absolutely continuous with finite relative entropy and finite E_T|Q|.', 'Limiting order and entropy-cost estimates are application hypotheses, not obtained estimates.', 'A deterministic lattice-position law is singular and inadmissible.'],
          'P4', 'Expand D(T||G_N,h)>=0 with the exact source density; conditioning on a sector has entropy -log its probability.',
          'An ordered trial with entropy cost o(h) per volume has not been constructed for the full Riesz gas.'),
    claim('w531-P0309-M2',
          f"Small fresh-gated deterministic controls passed {results['passed']} checks with no failures; elapsed CPU {results['elapsed_cpu_seconds']} seconds and wall {results['elapsed_wall_seconds']} seconds. These are numerical controls of saved formulas, not a proof certificate or independent audit.",
          ['One process, one thread, no GPU or model load.', 'Current governor and direct CPU/RAM/commit/disk probe admitted the bounded run.'],
          'Verification: check_controls.py and control_results.json',
          'Command: python -X utf8 ~/brain_workers/w531/check_controls.py. Complete result and compute gate receipt saved.',
          'No full Riesz phase theorem was tested or proved.', 'numerical evidence')
]
if latest_results['status'] == 'GATED':
    rows[-1]['statement'] = 'The additional entropy-control run was held by the fresh governor gate (throttle/distress); zero mathematical controls ran in that attempt. The initial 295/295 passing controls, source and gate receipt remain archived under verification_initial. No extra entropy numerical validation or proof certificate is claimed.'
    rows[-1]['source']['path'] = str(ROOT / 'compute_gate_receipt.json')
    rows[-1]['proof_or_counterexample'] = 'Latest control_results.json records GATED, passed 0; compute_gate_receipt.json records a fresh throttle/distress governor state with disk_low and process_critical. Archived verification_initial/control_results.json records the earlier passing run.'
    rows[-1]['remaining_gap'] = 'Extra numerical entropy controls have not run; P4 is a symbolic author proof awaiting independent review. No Riesz phase theorem was checked.'
ledger = ROOT / 'CLAIMS.jsonl'
seen = {json.loads(line)['id'] for line in ledger.read_text(encoding='utf-8').splitlines() if line.strip()}
with ledger.open('a', encoding='utf-8', newline='\n') as f:
    for row in rows:
        if row['id'] not in seen:
            f.write(json.dumps(row, ensure_ascii=False) + '\n')
            f.flush()
            seen.add(row['id'])


def entry(key, logical, kind, title, statement, assumptions):
    return {'key': key, 'namespace': 'probability.statisticalmechanics', 'logical_name': logical,
            'kind': kind, 'title': title, 'statement': statement, 'proof_text': None,
            'assumptions': assumptions, 'domain': 'probability and statistical mechanics', 'source': dict(source)}


bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w531', 'bundle_slug': 'riesz-three-mode-pressure-route-w531-001',
          'entries': [
    entry('pressure-definition', 'riesz-three-mode-periodic-source-pressure', 'definition', 'Three-mode periodic source pressure for the short-range Riesz gas',
          'For finite s>3, beta>0, mu,h real, an invertible A and integer N>=1, let Lambda=A Z^3, v=|det A|, K_j=2pi A^(-T)e_j, W_N(r)=sum_{m in Z^3}|r+NAm|^(-s), E_N=sum_{i<j}W_N(x_i-x_j), Psi(x)=sum_{j=1}^3 cos(K_j.x), and Q=sum_i Psi(x_i). Define Z_N(h)=sum_{n>=0}(1/n!) integral_(R^3/NLambda)^n exp[beta mu n-beta E_N+beta h Q] dx and p_N(h)=log Z_N(h)/(beta N^3 v). This is a bounded external source in the full unlabelled gas, distinct from a quadratic displacement pinning on fixed labels.',
          ['s>3', 'beta>0', 'A invertible', 'N positive integer']),
    entry('pressure-cusp-reduction', 'draft-riesz-three-mode-pressure-cusp-period-group-reduction', 'concept', 'Draft: pressure cusp and exact lattice period group',
          'Author-proved conditional reduction; independent audit pending, not a proof of Riesz crystallization. In the defined three-mode pressure, assume A^T A has diagonal a and off-diagonal b with a-b>0 and a+2b>0; p_N converges to finite p near zero; and m=p right-prime(0)>0. Choose h_l down to zero and N_l up to infinity with |p_N_l(h_l)-p(h_l)|+|p_N_l(0)-p(0)|<=h_l/l (a volume-first diagonal). Any selected local limit has real equal intensity Fourier coefficients c_j=(1/v) integral_F exp(-iK_j.x) E eta(dx)>=m/3. Its intensity translation-period group is exactly Lambda. If this limit is a zero-field Riesz DLR law, it is a lattice-periodic Gibbs law breaking continuous translations. The positive slope and zero-field DLR membership have not been established for P0309; no Coulomb, optimal-lattice or all-extreme-phases conclusion follows.',
          rows[5]['assumptions']),
    entry('pinned-response-obstruction', 'draft-positive-pinned-response-does-not-imply-zero-field-order', 'concept', 'Draft: positive pinned response is insufficient for spontaneous order',
          'Author-proved exact counterexample, independent audit pending. V independent fair signs have Z_V(h)=(2cosh(beta h))^V and limiting pressure beta^(-1)log(2cosh(beta h)); the response tanh(beta h) is positive at each h>0 but the zero-source right slope is zero. A collective two-state model instead has Z_V(h)=2cosh(beta Vh), pressure tending to |h|, and finite-volume zero-field derivative zero. For that model h_V=1/(beta V^2) gives response tending to zero while h_V=1/sqrt(V) gives response tending to one. These exact toy models show that neither fixed positive pinning nor an arbitrary diagonal proves spontaneous order; they are not Riesz phase results.',
          ['beta>0', 'V positive integer', 'Exact toy systems only']),
    entry('entropy-witness', 'draft-riesz-periodic-source-relative-entropy-cusp-witness', 'concept', 'Draft: relative-entropy witness for a Riesz pressure cusp',
          'Author-proved conditional criterion, independent audit pending. For the defined pressure with V_N=N^3 v and zero-source law G_N,0, any trial T absolutely continuous with finite relative entropy and finite E_T|Q| satisfies p_N(h)-p_N(0)>=h E_TQ/V_N-D(T||G_N,0)/(beta V_N). With finite pressure convergence, trials satisfying liminf_N E_T_N,h Q/V_N>=q>0 and limsup_N D/(beta V_N h)<=epsilon(h) tending to zero give p right-prime(0)>=q. A sector Q>=qV_N of probability exp[-o(V_N)] supplies a sufficient trial by conditioning. Deterministic lattice positions are singular; a fixed positive entropy cost per volume does not control field removal. No such trial estimate has been obtained for P0309. A phase conclusion still requires the geometry and zero-field Gibbs-limit condition of the cusp reduction.',
          ['Same full unlabelled configuration space as G_N,0', 'Finite relative entropy and E_T|Q|', 'Order and vanishing entropy-cost estimates remain explicit application hypotheses'])
], 'relations': [
    {'from_key': 'pressure-cusp-reduction', 'to_key': 'pressure-definition', 'kind': 'depends_on',
     'rationale': 'The conditional criterion uses precisely the defined p_N(h), bounded three-mode source, and full unlabelled short-range torus law.'},
    {'from_key': 'pinned-response-obstruction', 'to_key': 'pressure-cusp-reduction', 'kind': 'semantic_association',
     'rationale': 'The counterexample states positive response at each h>0 but zero right slope; the criterion explicitly requires m=p right-prime(0)>0 and a volume-first diagonal.'},
    {'from_key': 'entropy-witness', 'to_key': 'pressure-definition', 'kind': 'depends_on',
     'rationale': 'The entropy inequality compares the exact zero-source and source laws for the defined pressure and Q.'},
    {'from_key': 'entropy-witness', 'to_key': 'pressure-cusp-reduction', 'kind': 'semantic_association',
     'rationale': 'The entropy witness concludes p right-prime(0)>=q>0; the periodicity reduction assumes m=p right-prime(0)>0. Geometry and the Gibbs-limit condition remain explicit.'}
]}
required = {'key', 'namespace', 'logical_name', 'kind', 'title', 'statement', 'proof_text', 'assumptions', 'domain', 'source'}
keys = {e['key'] for e in bundle['entries']}
for e in bundle['entries']:
    assert required <= set(e) and e['kind'] in {'definition', 'concept'} and e['proof_text'] is None
    assert e['source']['license'].startswith('owner-own-work')
for r in bundle['relations']:
    assert r['from_key'] in keys and r['to_key'] in keys
draft = ROOT / 'drafts'
draft.mkdir(exist_ok=True)
serialized = json.dumps(bundle, ensure_ascii=False, indent=2) + '\n'
(draft / 'bundle_001.json').write_text(serialized, encoding='utf-8')
(ROOT / 'BRAIN_SUBMISSION.json').write_text(json.dumps({
    'prepared': {'state': 'COMPLETE', 'path': str(draft / 'bundle_001.json'), 'entries': 4, 'relations': 4},
    'submitted': {'state': 'PENDING', 'destination': '~/math-brain-inbox/w531/bundle_001.json'},
    'reviewed': {'state': 'PENDING', 'reviewer': 'w533'},
    'ingested': {'state': 'NOT_VERIFIED'}, 'retrievable': {'state': 'NOT_VERIFIED'},
    'no_unreviewed_theorem_promotion': True, 'all_mathematical_drafts_are_concepts': True
}, indent=2), encoding='utf-8')
patch_dir = ROOT / 'patches'
patch_dir.mkdir(exist_ok=True)
live = '~/math-brain-inbox/w531/bundle_001.json'
patch = ''.join(difflib.unified_diff([], serialized.splitlines(keepends=True), fromfile='a/' + live, tofile='b/' + live))
(patch_dir / '01_pressure_route_draft.diff').write_text(patch, encoding='utf-8')
hook_dir = ROOT / 'hooks'
hook_dir.mkdir(exist_ok=True)
hook = {'id': 'pressure-cusp-w531-01', 'area': 'math', 'event': 'stage-start',
        'cue': 'A proof treats positive response at a nonzero periodic field as sufficient for a zero-field crystalline phase.',
        'fire_when': 'The independent-sign pressure has tanh(beta*h)>0 at h>0 and a proof calls this spontaneous order.',
        'silent_when': 'A strictly positive zero-source one-sided pressure slope is proved with the volume-first selection and the correct Gibbs-limit condition, or the pinning conclusion remains explicitly conditional.',
        'text': 'Positive response under a nonzero field does not prove zero-field order. Show the one-sided pressure slope survives field removal, fix the volume/field limit order, and verify the actual Gibbs specification.',
        'evidence': '~/brain_workers/w531/PRESSURE_ROUTE.md P3; control_results.json false_pinned_response_controls (4 exact toy-model cases); proof_steps_need_derived_joint_structure_2026_09_09',
        'proposer': 'w531'}
assert len(hook['text']) <= 300
(hook_dir / 'math-w531.jsonl').write_text(json.dumps(hook) + '\n', encoding='utf-8')
review = ROOT / 'review_packet'
review.mkdir(exist_ok=True)
first_errors = [r['first_error'] for r in results['measurements']['pressure_derivative_errors']]
second_errors = [r['second_error'] for r in results['measurements']['pressure_derivative_errors']]
report = f'''P0309 is unproved here; current openness is UNKNOWN. The retrieved intake is underspecified about exponent scope. The precise working specialization is the short-range s>3 grand-canonical DLR gas.

The historical attempt already used phonons. The independent contribution is PRESSURE_ROUTE.md: bounded three-mode source pressure, a conditional cusp-to-periodicity reduction, and a relative-entropy witness sufficient for the cusp if its order/cost hypotheses can be proved. A positive zero-source right slope plus the stated Gibbs-limit condition would give a law whose mean-intensity period group is exactly the chosen lattice. The original phase theorem is not claimed. Harmonic and matching lemmas are supporting reference results.

Measured command: python -X utf8 ~/brain_workers/w531/check_controls.py. Result: {results['passed']} checks passed, 0 failed, {results['elapsed_cpu_seconds']:.6f} CPU seconds and {results['elapsed_wall_seconds']:.6f} wall seconds. The fresh governor/direct resource gate is in compute_gate_receipt.json. The 256-state discrete repulsive toy preserves the source symmetry; maximum first/second pressure derivative errors were {max(first_errors):.3g} and {max(second_errors):.3g}. Direct Hessian inverse versus Fourier covariance error was {results['measurements']['direct_inverse_max_abs_error']:.3g}. At N=4 the exact zero-mode term grows from 1.5625 to 15625 when h goes from 0.01 to 0.000001. Four independent-sign controls have positive pinned response but zero zero-source slope. These controls do not certify continuum crystallization.

Verification chronology: the initial 295-check PASS, its exact code and admission receipt are archived under verification_initial. The later entropy-extension attempt is {latest_results['status']}; its fresh gate reported throttle/distress and ran zero mathematical controls. P4 has a complete symbolic author proof; no extra numerical validation is claimed. The current root control_results.json and compute_gate_receipt.json describe that held attempt, not the earlier PASS.

Risks and gap: no positive zero-source slope has been proved for the unrestricted Riesz gas. The sufficient entropy estimate needs positive order and cost o(h) per volume; a fixed positive free-energy error is insufficient. Zero-field DLR membership is a separate condition. No Coulomb renormalization, lattice optimality, phase classification, independent audit or Lean certificate is supplied.

Apply: after mathematical review, the validating coordinator can use drafts/bundle_001.json (or patches/01_pressure_route_draft.diff) as a mathbrain-draft-v1 bundle under ~/math-brain-inbox/w531. All unreviewed result entries are concepts. Review, ingestion and retrieval are separate states in BRAIN_SUBMISSION.json; the coordinator owns integration. The one hook is local under hooks/math-w531.jsonl for review because of this worker's folder write restriction.

NEXT: w533 audit PRESSURE_ROUTE.md P1-P4 against CLAIMS.jsonl; the next mathematical step is an ordered absolutely continuous trial with entropy cost o(h) per volume.
'''
(ROOT / 'REPORT.md').write_text(report, encoding='utf-8')
(review / 'README.md').write_text('''Review packet for w533, 2026-10-10.

Claimed result: complete conditional reductions and exact obstructions; P0309 remains unproved. Independent audit has not occurred.

Start with ../STATEMENT_FOR_ADVERSARY.md and ../SOURCE_STATUS.json. The main independent proof is ../PRESSURE_ROUTE.md P1-P4. Check source sign/normalization, volume-first selection, primitive-basis symmetry, cell expectations, the exact period group, and the entropy identity/error scale. Zero-field DLR membership is explicit and the positive slope has not been proved. The stronger conjecture about all extreme phases is not a conclusion. Initial 295-check controls and their code are archived in ../verification_initial; the latest result includes the entropy extension.

The complete claim ledger is ../CLAIMS.jsonl. Reference proofs are ../HARMONIC_LEMMAS.md L1-L3; they are not the new independent mechanism. Provenance and targeted prior work are ../PRIOR_ATTEMPTS.md and ../prior_target_entries.json. Current openness remains UNKNOWN. Read-only store query returned zero matching target IDs; this is not an absence certificate for other stores.

Run python -X utf8 ~/brain_workers/w531/check_controls.py. It performs a fresh resource gate before the small controls; existing receipts are ../compute_gate_receipt.json and ../control_results.json. No formal checker, theorem/axiom receipt, admitted placeholder, independent reviewer keep, live-store change or source-hash-as-proof is claimed.

The review-only math-brain draft is ../drafts/bundle_001.json. Every unreviewed mathematical result is a concept with the owner-own-work source tag. Submission state is separately tracked in ../BRAIN_SUBMISSION.json. Please write your independent verdict in your own worker folder and send its path; this packet does not ask you to modify the store.

Control chronology: ../verification_initial contains the exact 295-check passing code, result, and admitting gate receipt. The root control_results.json records the later GATED entropy-extension attempt. That attempt ran no mathematical controls. P4 is a symbolic author proof awaiting independent audit; no extra entropy numerical pass is claimed.
''', encoding='utf-8')
st = json.loads((ROOT / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))
st['brain_states']['prepared'] = True
st['measurements'] = {'checks_passed': results['passed'], 'checks_failed': len(results['failures']), 'cpu_seconds': results['elapsed_cpu_seconds'], 'wall_seconds': results['elapsed_wall_seconds'], 'certificate': False, 'passing_receipt': 'verification_initial/control_results.json', 'latest_entropy_extension_status': latest_results['status']}
(ROOT / 'SOURCE_STATUS.json').write_text(json.dumps(st, indent=2), encoding='utf-8')
print(json.dumps({'claims': len(seen), 'draft_entries': 4, 'relations': 4, 'control_checks': results['passed'], 'max_first_derivative_error': max(first_errors), 'max_second_derivative_error': max(second_errors), 'inverse_error': results['measurements']['direct_inverse_max_abs_error'], 'entropy_extension_status': latest_results['status'], 'entropy_identity_error': results['measurements'].get('relative_entropy_max_identity_error')}))
