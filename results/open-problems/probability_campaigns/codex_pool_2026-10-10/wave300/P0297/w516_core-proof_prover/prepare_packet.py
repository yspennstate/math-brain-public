"""Write the local, reviewable mathematical packet; never ingest or edit live stores."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MEASUREMENTS = json.loads((ROOT / 'measurements.json').read_text(encoding='utf-8'))
assert MEASUREMENTS['assertions_passed']

attempt_path = ROOT / 'ATTEMPT.md'
attempt = attempt_path.read_text(encoding='utf-8')
old = 'Original intake source and local prior-attempt pointers are being recovered separately in SOURCE_STATUS.json.'
replacement = ('Original P0297 source independently recovered: Rhodes-Vargas, Two Decades of Probabilistic Approach '
               'to Liouville Conformal Field Theory, arXiv:2509.21053v1, Section 3, '
               'https://arxiv.org/html/2509.21053v1. The 2026 ICM primary publication '
               'https://epubs.siam.org/doi/10.1137/25M181012X still describes general d_gamma as unknown. '
               'Global current openness remains UNKNOWN beyond this scoped evidence.')
attempt = attempt.replace(old, replacement)
old = ('Exact-ID searches in the named H/I attempts and Lean campaign have not found a P0297 proof. '
       'Title/alias checks are ongoing; absence from these searches does not certify absence of an owner result.')
replacement = ('Exact-ID and title searches in the named H/I attempts and Lean campaign found no target proof. '
               'The independently read intake aliases D0049 and D0052 share dedup_key lqg_hausdorff_dimension_d_gamma. '
               'Their unreviewed attempts are an obstruction digest (with a wrong d_gamma=2Q/xi string that w522 owns correcting) '
               'and exclusion of affine guesses by known bounds. Neither supplies a formula. '
               'Direct read-only population-store SQL retrieved the original P0297 problem and constant-shift attempt; '
               'both are unverified, and the attempt explicitly cannot calculate xi. '
               'PRIOR_ALIAS_ROWS.json and EXISTING_P0297_CARDS.json preserve these exact records. '
               'These scoped negative checks do not certify absence of any owner result.')
attempt = attempt.replace(old, replacement)
section = '''
## L6: the two-route weighted near-tie density

Fix xi>0 and two coefficient vectors in L1. Set Delta=f_1-f_2 and D=(w_1-w_2)^T C(w_1-w_2). Define the weighted gap law nu(E)=E[D 1_{Delta in E}]. Assume that on some neighborhood (-delta,delta), nu has a density r(t) continuous at zero. No independence between D and Delta is assumed. Then

    S(xi)=r(0).                                               (L6)

Proof. With k(u)=e^u/(1+e^u)^2, pi_1 pi_2=k(beta Delta), so beta E B_beta=beta integral k(beta t) nu(dt). The contribution from |t|>=delta is at most beta exp(-beta delta) E D, which tends to zero; E D<=4V. On |t|<delta, change variables u=beta t. Continuity makes r bounded on a smaller neighborhood. Dominated convergence against the integrable k(u), whose integral is one, yields r(0); the intervening compact region away from zero is handled by the same exponential tail estimate. This proves L6. The assumption is a weighted density condition, not merely a density for unweighted path lengths.

For the two single-edge paths of L3, D=sigma^2 is constant and Delta=c_1-c_2+xi Z, so r(0)=sigma phi((c_1-c_2)/(xi sigma))/xi, agreeing with the direct Gaussian calculation.

This provides a precise possible input for H. It does not establish a uniform weighted density for the increasing multi-route LFPP family, screen additional almost-minimal paths, or compute mu. The next concrete proof step is to control the multi-route screening remainder and the weighted gap densities uniformly in n, rather than infer their order from uniqueness of the minimum.
'''
if '## L6:' not in attempt:
    attempt += section
attempt = attempt.replace('The next concrete proof step is a two-route near-tie formula with an explicit remainder that remains uniform as the regularization scale decreases; its required uniform control is still unproved.', 'L6 below supplies a conditional two-route density formula. The next concrete proof step is a multi-route screening and weighted-density remainder estimate uniform in the regularization scale; that uniform control is still unproved.')
attempt_path.write_text(attempt, encoding='utf-8')
(ROOT / 'GAP.md').write_text('P0297 remains unresolved.\n\nHardest remaining lemma H: explicitly evaluate the subcritical measure mu, the weak limit of [xi/T_n][V_n-E A_{n,*}(xi)+S_n(xi)] dxi. The finite Gaussian lemmas and source-dependent measure reduction are author-proved in ATTEMPT.md; independent review is pending. No density or interchange of beta and scale limits is assumed. L6 identifies the two-route switching term with a weighted near-tie density under an explicit continuity assumption, but supplies no scale-uniform multi-route estimate.\n\nNEXT: Bound the multi-route screening remainder and weighted near-tie densities uniformly in the regularization scale, to determine an interval mass of mu.\n', encoding='utf-8')

def claim(identifier, statement, assumptions, proof, status='proved special case', gap='Independent mathematical review pending; this does not solve P0297.'):
    return {'id': 'w516.P0297.' + identifier, 'statement': statement, 'assumptions': assumptions,
            'source': {'kind': 'owner campaign derivation', 'source_id': 'owner-probability-campaign-w516-P0297-20261010:' + identifier,
                       'license': 'owner-own-work', 'artifact': str(attempt_path), 'locator': identifier},
            'proof_or_counterexample': proof, 'independent_reviewer': 'w518 (pending)',
            'remaining_gap': gap, 'status': status, 'artifact_state': 'local draft; author-proved where stated; unreviewed'}

rows = [
    claim('L1', 'For a centered finite Gaussian vector X with covariance C, finite nonnegative nonzero coefficient vectors a_p, xi,beta>0, let f_p=log sum_i a_pi exp(xi X_i), w_pi=a_pi exp(xi X_i)/exp(f_p), pi_p=exp(-beta f_p)/sum_q exp(-beta f_q), bar_w=sum_p pi_p w_p, A=sum_p pi_p[sum_i C_ii w_pi-w_p^T C w_p], and B=sum_p pi_p w_p^T C w_p-bar_w^T C bar_w. Then d/dxi E[-log sum_p exp(-beta f_p)/beta]=xi E[A-beta B], B>=0, and 0<=A<=max_i C_ii.', ['X centered Gaussian; C positive semidefinite', 'Finitely many coefficient vectors, nonnegative and each nonzero', 'xi,beta>0'], 'ATTEMPT.md L1 gives differentiated Gibbs weights, full-covariance Gaussian integration by parts and the exact pair-variance decomposition.'),
    claim('L2', 'Under L1 with positive definite C and distinct coefficient vectors, the minimum of f_p is unique almost surely for each fixed xi>0. With p_* the minimizer, A_*=sum_i C_ii w_{p_*i}-w_{p_*}^T C w_{p_*}, S=lim_beta beta E B exists, is finite and nonnegative, and (E min_p f_p)\'=xi(E A_*-S)<=xi max_i C_ii.', ['L1 assumptions', 'C positive definite', 'Duplicate coefficient vectors removed', 'Fixed xi>0; beta limit taken before any scale limit'], 'ATTEMPT.md L2 proves uniqueness by nonzero analytic zero sets and passes the finite-beta identity with dominated first derivatives; it does not discard beta B.'),
    claim('L3', 'For two parallel edges of base length one and independent standard normal X_1,X_2, F=log min(exp(xi X_1),exp(xi X_2))=xi min(X_1,X_2). Its expected xi derivative is -1/sqrt(pi), the within-path covariance term is zero, and the switching term is S=1/(xi sqrt(pi)). Omitting switching therefore has absolute derivative error 1/sqrt(pi).', ['xi>0', 'Two independent standard normal costs and two single-edge candidate paths'], 'ATTEMPT.md L3 evaluates E|X_1-X_2| exactly. measurements.json independently reproduces the finite-beta approach to this exact limit.'),
    claim('L4', 'For the finite Gaussian minimum log length F of L2 and V=max_i C_ii, Var(F)<=xi^2 V and every median M satisfies |E F-M|<=xi sqrt(2V). For heat-smoothed whole-plane GFF crossings with T=log(1/epsilon), V=T+O(1), and the established median exponent, sufficiently accurate finite polygonal/quadrature approximants F_n have E F_n/T_n -> xi Q(xi)-1 at every fixed xi in a compact interior parameter interval.', ['Finite Gaussian gradient bound and Gaussian Poincare inequality', 'For the LQG extension: smooth regularized GFF with finite L2 supremum, diagonal variance T+O(1), and cited median exponent', 'Finite approximants have uniform-in-xi L2 error <=1/n; tiny auxiliary noise makes their covariances positive definite'], 'ATTEMPT.md L4 proves the median bound and an existential finite-path/quadrature approximation, avoiding an unproved fixed-direction lattice identification.'),
    claim('L5', 'For the approximants in L4, define g_n=E F_n/T_n, Psi_n=(V_n/T_n)xi^2/2-g_n and dmu_n=[xi/T_n][V_n-E A_{n,*}+S_n]dxi. These are nonnegative measures converging weakly on compact interior intervals to dmu=d[xi^2/2-(xi Q(xi)-1)]. From xi_*=1/sqrt(6) and g(xi_*)=-1/6, for xi>xi_* one has g(xi)=-1/6+(xi^2-1/6)/2-mu((xi_*,xi]); for xi<xi_* the corresponding interval mass has the opposite orientation. Computing mu determines Q but mu is not computed here.', ['L1-L4', 'Continuity of cited Q and the Brownian anchor', 'V_n/T_n ->1', 'No absolute continuity or differentiated scale limit is assumed'], 'ATTEMPT.md L5 proves monotonicity and Stieltjes-measure convergence, then integrates interval masses.', gap='The single hard input H is explicit evaluation of the limiting measure; it remains unproved.'),
    claim('L6', 'For two candidate paths at a fixed xi>0 in L1, set Delta=f_1-f_2 and D=(w_1-w_2)^T C(w_1-w_2). If the weighted gap measure nu(E)=E[D 1_{Delta in E}] has a density continuous at zero on a neighborhood of zero, then lim_beta beta E B_beta equals that density at zero.', ['L1 with two paths', 'xi fixed positive', 'Weighted gap density exists near zero and is continuous at zero', 'No independence between Delta and D'], 'ATTEMPT.md L6 proves a logistic approximate-identity limit and controls the far-gap contribution by beta exp(-beta delta) E D.', gap='Weighted density continuity and multi-route screening must still be established uniformly across LFPP scales for use in H.'),
    claim('H', 'Explicit evaluation of the limiting nonnegative response-defect measure mu in L5, including the geodesic covariance and near-tie terms, would compute the subcritical LFPP exponent Q(xi) and hence d_gamma through Q=2/gamma+gamma/2 and d_gamma=gamma/xi. The evaluation is not supplied.', ['Cited LFPP-to-LQG exponent identification', 'L1-L5 finite response/measure reduction'], 'ATTEMPT.md and GAP.md specify the missing scale-uniform near-tie/geodesic-occupation estimate. Only comparison bounds have been obtained.', status='conjecture', gap='Unproved evaluation of mu; no exact generic dimension and no success claim.')
]
claim_path = ROOT / 'CLAIMS.jsonl'
existing = {json.loads(line)['id'] for line in claim_path.read_text(encoding='utf-8').splitlines() if line.strip()}
with claim_path.open('a', encoding='utf-8') as file:
    for row in rows:
        if row['id'] not in existing:
            file.write(json.dumps(row, ensure_ascii=False) + '\n')

result_rows = [{'row': 'S1.P0297.w516.' + r['id'].split('.')[-1], 'verdict': 'AUTHOR_PROVED_PENDING_REVIEW' if r['status'] == 'proved special case' else 'OPEN_GAP',
                'claim_id': r['id'], 'evidence': str(attempt_path), 'reviewer': 'w518', 'parent_problem_solved': False} for r in rows]
(ROOT / 'RESULT_ROWS.jsonl').write_text(''.join(json.dumps(row) + '\n' for row in result_rows), encoding='utf-8')

hook = {'id': 'gaussian-minimum-w516-01', 'area': 'math', 'event': 'stage-start',
        'cue': 'Gaussian integration by parts applied to optimizer or geodesic weights of a minimum log exponential path length',
        'fire_when': 'Differentiate the selected-path weights of a Gaussian minimum and discard the near-tie switching term because the minimum is unique almost surely.',
        'silent_when': 'A single fixed deterministic path is being differentiated, or the finite-beta optimizer covariance is explicitly retained.',
        'text': 'Gaussian integration by parts through a minimum needs the optimizer-switching term. Almost-sure uniqueness does not remove it: two parallel Gaussian edges have a nonzero averaged derivative although every fixed-path term is zero.',
        'evidence': str(ROOT / 'measurements.json') + ': two_edge_cases[-1]; ATTEMPT.md L1-L3; scar perceptron_proof_open_gaps_fleet_2026_07_12',
        'proposer': 'w516'}
assert len(hook['text']) <= 300
hook_line = json.dumps(hook, ensure_ascii=False)
(ROOT / 'HOOK_PROPOSAL.jsonl').write_text(hook_line + '\n', encoding='utf-8')
patch_dir = ROOT / 'patches'
patch_dir.mkdir(exist_ok=True)
live_path = '~/primary_directive/hooks1000/proposals/math-w516.jsonl'
(patch_dir / '01_gaussian_minimum_hook.diff').write_text('--- a/' + live_path + '\n+++ b/' + live_path + '\n@@ -0,0 +1 @@\n+' + hook_line + '\n', encoding='utf-8')

def draft_entry(key, name, title, statement, assumptions, source_id, kind='concept', source_url=None, license_tag='owner-own-work'):
    return {'key': key, 'namespace': 'probability.lqg', 'logical_name': name,
            'kind': kind, 'title': title, 'statement': statement, 'proof_text': None,
            'assumptions': assumptions, 'domain': 'probability theory; Gaussian optimization; LQG',
            'source': {'source_id': source_id, 'url': source_url, 'revision': 'author-draft-2026-10-10-pending-w518',
                       'license': license_tag, 'excerpt': None}}

entries = [draft_entry('finite-model', 'finite-gaussian-exponential-path-response-model', 'Finite Gaussian exponential path response model',
    'Let X be a centered finite Gaussian vector with covariance C, and let a_p be finitely many nonnegative nonzero coefficient vectors. For xi>0 set l_p=sum_i a_pi exp(xi X_i), f_p=log l_p, w_pi=a_pi exp(xi X_i)/l_p. For beta>0 define pi_p=exp(-beta f_p)/sum_q exp(-beta f_q) and F_beta=-log sum_p exp(-beta f_p)/beta. These definitions represent finite candidate path lengths, not an identification with an LQG metric.',
    ['C positive semidefinite; finite path family'], 'owner-probability-campaign-w516-P0297-20261010:model', kind='definition')]
for row in rows:
    identifier = row['id'].split('.')[-1]
    names = {'L1': ('gaussian-optimized-length-response-with-switching', 'Gaussian optimized-length response includes switching'),
             'L2': ('finite-geodesic-switching-zero-temperature-limit', 'Finite zero-temperature switching limit'),
             'L3': ('two-parallel-gaussian-edges-switching-obstruction', 'Two Gaussian edges refute omitted switching'),
             'L4': ('gaussian-minimum-log-length-mean-median-bridge', 'Gaussian minimum log-length mean-median bridge'),
             'L5': ('lqg-response-defect-measure-reduction', 'LQG response-defect measure reduction'),
             'L6': ('two-route-weighted-near-tie-response-density', 'Two-route response from weighted near-tie density'),
             'H': ('lqg-response-defect-measure-open-input', 'Open input: evaluate LQG response-defect measure')}
    name, title = names[identifier]
    prefix = 'OPEN INPUT, not a theorem: ' if identifier == 'H' else 'AUTHOR-PROVED DRAFT; independent mathematical review pending: '
    entries.append(draft_entry(identifier.lower(), name, title, prefix + row['statement'], row['assumptions'], row['source']['source_id']))
self_contained = {
    'l2': 'Let X be a centered finite Gaussian vector with positive definite covariance C, and let a_p be finitely many distinct nonnegative nonzero coefficient vectors. For xi>0 let f_p=log sum_i a_pi exp(xi X_i), w_pi=a_pi exp(xi X_i)/exp(f_p), and pi_p=exp(-beta f_p)/sum_q exp(-beta f_q). Put B_beta=sum_p pi_p w_p^T C w_p-(sum_p pi_p w_p)^T C(sum_p pi_p w_p). At each fixed xi>0 the minimizer p_* is unique almost surely, S=lim_beta beta E B_beta exists, is finite and nonnegative, and d/dxi E min_p f_p=xi(E[sum_i C_ii w_{p_*i}-w_{p_*}^T C w_{p_*}]-S)<=xi max_i C_ii. The beta limit is taken at fixed finite model; no uniform scale limit follows.',
    'l4': 'Let X be a centered finite Gaussian vector with covariance C, a_p finitely many nonnegative nonzero coefficient vectors, xi>0, and F=min_p log sum_i a_pi exp(xi X_i). With V=max_i C_ii one has Var(F)<=xi^2 V and, for every median M of F, |E F-M|<=xi sqrt(2V). For smooth regularized GFF crossing log lengths with T=log(1/epsilon), variance diagonal T+O(1), finite L2 field supremum and the cited median exponent a_epsilon=epsilon^(1-xi Q(xi)+o(1)), finite polygonal-path/quadrature approximants with uniform-on-compact-xi L2 error <=1/n satisfy E F_n/T_n ->xi Q(xi)-1 pointwise. Such finite approximants exist; no identification with a fixed-direction lattice metric is assumed.',
    'l5': 'Let X_n be centered finite Gaussian vectors with positive definite covariances C_n, and let F_n(xi)=min_p log sum_i a_{n,pi} exp(xi X_{n,i}) for finite nonnegative nonzero coefficient vectors. Put V_n=max_i C_{n,ii}. Suppose T_n->infinity, V_n/T_n->1, and E F_n(xi)/T_n converges pointwise on an interval to the continuous function g(xi)=xi Q(xi)-1. Then Psi_n=(V_n/T_n)xi^2/2-E F_n/T_n are nondecreasing; their nonnegative Stieltjes measures converge weakly on compact interior intervals to mu=d[xi^2/2-g(xi)]. If xi_*=1/sqrt(6) is in the interval and g(xi_*)=-1/6, then for xi>xi_* one has g(xi)=-1/6+(xi^2-1/6)/2-mu((xi_*,xi]); for xi<xi_* add mu((xi,xi_*]) instead. This identity does not compute mu or Q and does not assume a density.',
    'l6': 'Let X be a centered finite Gaussian vector with covariance C, a_1,a_2 two nonnegative nonzero coefficient vectors, and xi>0 fixed. Set f_p=log sum_i a_pi exp(xi X_i), w_pi=a_pi exp(xi X_i)/exp(f_p), pi_p=exp(-beta f_p)/sum_{q=1,2} exp(-beta f_q), Delta=f_1-f_2, and D=(w_1-w_2)^T C(w_1-w_2). If nu(E)=E[D 1_{Delta in E}] has a density r continuous at zero on a neighborhood of zero, then lim_beta beta E[pi_1 pi_2 D]=r(0). No independence between D and Delta is assumed. This is a conditional finite-model statement; the weighted density assumption is not established uniformly for LFPP.',
    'h': 'OPEN INPUT, not a theorem: For subcritical LFPP, let Q be the continuum crossing-median exponent a_epsilon=epsilon^(1-xi Q(xi)+o(1)) and let mu=d[xi^2/2-(xi Q(xi)-1)], a nonnegative Stieltjes measure furnished by the Gaussian response reduction. Explicitly evaluating mu interval masses from finite-scale geodesic covariance and near-tie statistics would determine Q and then d_gamma=gamma/xi through Q=2/gamma+gamma/2. No such evaluation, absolute continuity, exact generic dimension formula or scale-uniform near-tie estimate is supplied.'
}
for entry in entries:
    if entry['key'] in self_contained:
        prefix = '' if entry['key'] == 'h' else 'AUTHOR-PROVED DRAFT; independent mathematical review pending: '
        entry['statement'] = prefix + self_contained[entry['key']]
    if entry['source']['url'] is None:
        entry['source']['url'] = 'file:///~/brain_workers/w516/ATTEMPT.md'
relations = [
    {'from_key': 'l1', 'to_key': 'finite-model', 'kind': 'depends_on', 'rationale': 'The response identity differentiates exactly the finite-model log lengths and Gibbs weights stated at the target end.'},
    {'from_key': 'l2', 'to_key': 'l1', 'kind': 'depends_on', 'rationale': 'The zero-temperature existence proof rearranges the exact finite-beta identity before taking beta to infinity.'},
    {'from_key': 'l3', 'to_key': 'l1', 'kind': 'specializes', 'rationale': 'With two single-edge paths and identity covariance, the within-path term vanishes and switching supplies the whole response.'},
    {'from_key': 'l6', 'to_key': 'l1', 'kind': 'specializes', 'rationale': 'For two routes, the path covariance equals a logistic near-tie kernel times their squared covariance distance.'},
    {'from_key': 'l5', 'to_key': 'l2', 'kind': 'depends_on', 'rationale': 'The finite-scale measure density is the response inequality integrated against xi; the scale bridge is proved separately in ATTEMPT.md L4.'},
    {'from_key': 'l5', 'to_key': 'l4', 'kind': 'depends_on', 'rationale': 'The mean-median and finite approximation bridge supplies the scale-normalized pointwise convergence required by the Stieltjes-measure reduction.'},
    {'from_key': 'h', 'to_key': 'l5', 'kind': 'depends_on', 'rationale': 'The unresolved input is precisely evaluation of the interval masses in the proved measure reduction.'}
]
bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w516', 'bundle_slug': 'lqg-gaussian-minimum-response-w516-001',
          'entries': entries, 'relations': relations}
(ROOT / 'bundle_local_001.json').write_text(json.dumps(bundle, indent=2) + '\n', encoding='utf-8')

counter = MEASUREMENTS['two_edge_cases'][-1]
report = f'''Saved six author proofs/conditional reductions L1-L6 and one explicit remaining gap H in ATTEMPT.md. P0297 is unresolved; independent review is pending. Primary sources give the exact metric-dimension target and exponent relation; scoped source status is in SOURCE_STATUS.json.

The concrete reasoning repair retains the Gaussian optimizer-switching term. On the exact two-edge counterexample, omitting it gives derivative error {counter['baseline_absolute_error']:.12g}; bounded quadrature with it reduces the error to {counter['corrected_absolute_error']:.12g}. Four finite-beta Gaussian checks have maximum integration-by-parts error {MEASUREMENTS['maximum_ibp_absolute_error']:.3g}. Command: python -X utf8 ./measure_response.py. The gate-003 reproduction is repeatable from scratch; the prior timeout and completed receipts are preserved. These numbers measure finite-model correction, not LQG accuracy or global recall improvement.

Review/PROOF_PACKET.md points to the exact assumptions and the scale-limit gap. The seven-entry draft bundle uses definitions/concepts only until reviewed. The validating coordinator integrates; w516 does not run integration or mutate a store. Submission, review, ingestion and retrieval remain separate states.

Apply patches/01_gaussian_minimum_hook.diff by adding its proposed row at the named live proposal path after the proposal audit. The hook is staged locally because the worker file restriction permits the named brain inbox but not that shared hook directory. No live hook was edited.

Risk: uniqueness of the finite minimizer does not control near-tie density; passing beta to infinity inside an increasing graph or differentiating the scale limit needs a proof. The response-defect measure is not evaluated and need not be absolutely continuous. L6 assumes weighted density continuity; it does not prove scale-uniform multi-route control.

NEXT: w518 checks L1-L6; the next proof step is a uniform multi-route screening and weighted near-tie-density estimate that determines an interval mass of mu.
'''
report = report.replace('gate-003', 'gate-004').replace('seven-entry draft bundle', 'eight-entry draft bundle')
(ROOT / 'REPORT.md').write_text(report, encoding='utf-8')
review = f'''# Review packet for w518

Target P0297; author w516; original problem unresolved. Independent referee of any NEW result contributed by w518 is w521.

Statement-first packet: review/STATEMENT_ONLY.md, delivered to w517 by direct mesh message msg-70fcd954e8 after the team route failed. The statement file predates ATTEMPT.md; no independent verdict is claimed.

Read ATTEMPT.md L1-L6 and GAP.md. Highest-priority checks: the sign and factor beta in the Gaussian response; the zero-temperature argument at a fixed xi; the finite polygonal/quadrature approximation and Poincare mean-median bound; weak convergence of nonnegative Stieltjes measures without differentiating a limit; and the precise weighted-density assumption in L6. CLAIMS.jsonl records statements, assumptions, source, proof, reviewer, gap and status for each row.

Reproduce with `python -X utf8 ~/brain_workers/w516/measure_response.py`. Four finite-beta cases, five two-edge beta values and two covariance controls are checked under a fresh 120-second gate with at most 6,561 grid points per case. Maximum Gaussian identity residual: {MEASUREMENTS['maximum_ibp_absolute_error']:.3g}. Two-edge derivative error: {counter['baseline_absolute_error']:.12g} without the switching term versus {counter['corrected_absolute_error']:.12g} with it at beta=1250. Numerical checks support but do not replace the proofs.

Single hard input H: compute the limiting response-defect measure mu. The proved reduction does not compute Q(xi), prove an exact dimension formula, or establish that mu has a density. The critical comparison bound is not claimed novel.

bundle_local_001.json contains eight DRAFT definition/concept entries and seven exact internal relations, all derived work tagged owner-own-work. No lemma/theorem entry is promoted before independent review. BRAIN_STATES.json will record the submission receipt separately from review, ingestion and retrievability. The reviewer or validating coordinator handles integration. Source evidence: SOURCE_STATUS.json, PRIOR_ALIAS_ROWS.json and exact-ID, read-only EXISTING_P0297_CARDS.json. The requested proof-gap scar is named in ATTEMPT.md.

Please issue KEEP/FIX/DROP per claim in your own folder. A KEEP on any lemma does not solve P0297. REVIEW_REQUEST.json records the handoff rather than manufacturing an audit.

NEXT: Check L1's covariance calculation and independently rederive the exact two-edge limit; then audit the source-dependent scale bridge L4-L5.
'''
review_dir = ROOT / 'review'
review_dir.mkdir(exist_ok=True)
(review_dir / 'PROOF_PACKET.md').write_text(review, encoding='utf-8')
(ROOT / 'PROGRESS_EVENT.json').write_text(json.dumps({'agent':'w516','row':'S1.P0297.w516.L3','event':'P0297: finite Gaussian response repaired; exact switching counterexample and L1-L6 proof packet saved; hardest scale-response input H open.','evidence':str(attempt_path),'state':'STAGED_FOR_REVIEWER_POST','reason':'Shared progress-page writes are outside the named worker/inbox write scope.'},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'claims_added':len(rows),'draft_entries':len(entries),'relations':len(relations),
                  'baseline_error':counter['baseline_absolute_error'],'corrected_error':counter['corrected_absolute_error'],
                  'remaining_gap':'H: evaluation of limiting response-defect measure','reviewer':'w518'}))
