"""Assemble only this worker's draft and review files, without touching live stores."""
import difflib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ATTEMPT = (ROOT / 'ATTEMPT.md').read_text(encoding='utf-8-sig')
MEASURE = json.loads((ROOT / 'measurements/bridge_validation.json').read_text(encoding='utf-8-sig'))


def section(title, next_title):
    return ATTEMPT.split(title, 1)[1].split(next_title, 1)[0].strip()


def source(identifier='w525-finite-lfpp-bridge', author='w525'):
    path = ROOT / 'ATTEMPT.md' if author == 'w525' else Path('~/brain_workers/w526/FINITE_BRIDGE_INDEPENDENT.md')
    return {'source_id': 'owner-probability-campaign-20261010:' + identifier,
            'url': path.as_posix(), 'revision': 'author-proof-2026-10-10; independent-referee-pending',
            'license': 'owner-own-work (campaign proof; no claim to solve P0297)', 'excerpt': None}


finite_assumptions = ['V finite', 'X centered Gaussian with PSD covariance C, singular covariance allowed', 'Finite nonempty family P of nonempty paths', 'Positive deterministic weights on each path support', 'xi>=0; beta>0']
entries = []


def add(key, logical, kind, title, statement, assumptions, proof=None, namespace='probability.lqg', entry_source=None):
    entries.append({'key': key, 'namespace': namespace, 'logical_name': logical, 'kind': kind,
                    'title': title, 'statement': statement, 'proof_text': proof, 'assumptions': assumptions,
                    'domain': 'probability theory', 'source': entry_source or source()})


add('canonical', 'canonical-lqg-lfpp-parameter-relations', 'concept', 'Canonical LQG and LFPP parameter relations',
    'For gamma in (0,2), let d_gamma be the almost-sure Hausdorff dimension of the canonical gamma-LQG metric and set xi=gamma/d_gamma and Q=2/gamma+gamma/2. The circle-average LFPP metric on epsilon Z^2 uses vertex cost epsilon*exp(xi*h_epsilon(v)); its left-right crossing exponent satisfies lambda(xi)=1-xi*Q. The Brownian value d_sqrt(8/3)=4 gives xi=1/sqrt(6), Q=5/sqrt(6), and lambda=1/6. These relations do not compute d_gamma at other gamma.',
    ['gamma in (0,2)', 'Canonical LQG metric', 'Standard whole-plane GFF normalization', 'Epsilon included in the LFPP vertex cost'],
    entry_source={'source_id': 'arxiv:1903.09561:equation-1.5', 'url': 'https://arxiv.org/pdf/1903.09561', 'revision': 'as-read-2026-10-10; equation (1.5)', 'license': 'arxiv-nonexclusive (facts paraphrased)', 'excerpt': None})

response_statement = ('Let X~N(0,C) on a finite V with C PSD, and P a finite nonempty family of nonempty paths with positive deterministic weights a_pv. Put f_p(y)=log(sum_{v in p} a_pv exp(y_v)), r_p=grad f_p, q_p=exp(-beta*f_p)/sum_s exp(-beta*f_s), F_beta=-(1/beta)log(sum_p exp(-beta*f_p)), and rbar=sum_p q_p*r_p, beta>0. Define A_beta=sum_p q_p[sum_i r_pi*C_ii-r_p^T*C*r_p] and B_beta=sum_p q_p*r_p^T*C*r_p-rbar^T*C*rbar. For xi>=0, (d/dxi) E F_beta(xi X)=xi E[A_beta(xi X)-beta B_beta(xi X)]. A_beta>=0 and B_beta>=0. This is a finite lemma with independent adversary derivation; it does not compute an LQG dimension.')
add('response', 'finite-gaussian-lfpp-log-distance-interpolation', 'lemma', 'Finite Gaussian LFPP interpolation with route fluctuations', response_statement, finite_assumptions,
    section('## Lemma 1: exact finite-network response', '## Lemma 2: retain'))

add('integrated', 'finite-gaussian-lfpp-integrated-soft-min-limit', 'lemma', 'Integrated soft-min limit for finite Gaussian LFPP',
    'Let X be a centered finite Gaussian with PSD covariance C, and P a finite nonempty family of nonempty positively weighted paths. Let D_xi=min_p sum_{v in p} a_pv exp(xi X_v) and F_beta(y)=-(1/beta)log sum_p exp[-beta log(sum_{v in p} a_pv exp(y_v))]. For 0<=a<b, E log D_b-E log D_a=lim_{beta->infinity} integral_a^b xi E tr[C Hess F_beta(xi X)] dxi. Each endpoint has soft-min error at most log|P|/beta. This assertion does not exchange the beta limit with a derivative.',
    finite_assumptions + ['0<=a<b<infinity'],
    section('## Lemma 2: retain the term at route switches', '## Lemma 3: concentration'))

add('switch', 'two-gaussian-routes-retain-selection-response', 'lemma', 'Two Gaussian routes refute omission of path changes',
    'If X_1,X_2 are independent N(0,1), D_xi=min(exp(xi X_1),exp(xi X_2)), and xi>=0, then E log D_xi=-xi/sqrt(pi). For the soft minimum of the two affine path logs, A_beta=0, B_beta=2q_1q_2, q_i=exp(-beta*xi*X_i)/sum_j exp(-beta*xi*X_j), and beta*xi*E B_beta->1/sqrt(pi) for every xi>0. Although beta B_beta->0 almost surely, its expectation does not vanish. At xi=0 the smooth derivatives are zero but the hard-min right derivative is -1/sqrt(pi).',
    ['Two singleton paths with equal unit weights', 'Independent standard Gaussian coordinates', 'xi>=0; beta>0'],
    section('Exactly solvable obstruction.', '## Lemma 3: concentration'))

add('omit-route', 'refuted-fixed-route-differentiation-of-gaussian-minimum', 'concept', 'Refuted route: discard Gaussian path selection',
    'REFUTED proof route: from almost-sure uniqueness of a minimizing route, discard the path-selection covariance term before differentiating the expectation of a minimum of affine Gaussian path logs. The two independent singleton-route example has zero within-path Hessians but E log D_xi=-xi/sqrt(pi), so it directly refutes the claimed zero derivative. This is a documented invalid proof step, not an asserted theorem.',
    ['Minimum over competing paths', 'Parameter differentiation and an expectation or smoothing limit'])

add('transfer', 'gaussian-lfpp-mean-median-crossing-exponent-transfer', 'lemma', 'Mean and median log-distance exponents agree under variance growth',
    'Let D_xi=min_p sum_{v in p} a_pv exp(xi X_v) for a finite nonempty family of nonempty paths, positive deterministic weights, X~N(0,C) with C PSD, and xi>=0. Set v=max_i C_ii. Then Var(log D_xi)<=xi^2*v and every median M satisfies |E log D_xi-M|<=xi*sqrt(v). Thus, for a sequence with L_n->infinity and v_n=O(L_n), convergence of M_n/L_n at a fixed xi implies the same limit for E log D_xi,n/L_n. This transfers an existing crossing exponent; it does not calculate it.',
    finite_assumptions[:-1] + ['xi fixed and nonnegative', 'For the sequence: L_n->infinity and v_n=O(L_n)'],
    section('## Lemma 3: concentration transfers median exponent to mean log exponent', '## Lemma 4: finite comparison'))

add('comparison', 'finite-gaussian-lfpp-quadratic-parameter-comparison', 'lemma', 'Finite quadratic comparison of mean Gaussian log distances',
    'For centered finite Gaussian X with PSD covariance C, positive deterministic weights, and a finite nonempty family of nonempty paths, let D_xi=min_p sum_v a_pv exp(xi X_v) and v=max_i C_ii. For 0<=a<b, E log D_b-E log D_a <= (v/2)(b^2-a^2). When variance-normalized crossing exponents satisfy v_n/L_n->1 and E log D_xi,n/L_n->-lambda(xi), this implies lambda(b)-lambda(a)>=-(b^2-a^2)/2. The resulting LFPP monotonicity is already known; no new LQG bound is claimed.',
    finite_assumptions[:-1] + ['0<=a<b<infinity', 'Exponent corollary assumes v_n/L_n->1 and endpoint exponent convergence'],
    section('## Lemma 4: finite comparison and an already-known LFPP bound', '## Conditional scale bridge'))

add('scale', 'conditional-lfpp-exponent-integrated-gaussian-response', 'lemma', 'Conditional scale limit without a derivative-limit exchange',
    'For finite Gaussian networks indexed by n, let X_n~N(0,C_n), P_n be a finite nonempty family of nonempty positively weighted paths, K_n=|P_n|, D_xi,n=min_p sum_v a_npv exp(xi X_nv), and F_n,beta(y)=-(1/beta)log sum_p exp[-beta log(sum_v a_npv exp(y_v))]. Suppose L_n->infinity, max_i(C_n)_ii=O(L_n), and medians of log D_xi,n divided by L_n converge to -lambda(xi) at fixed 0<=a<b. If beta_n>0 and log K_n/(beta_n L_n)->0, then lambda(b)-lambda(a)=-lim_n L_n^(-1) integral_a^b xi E tr[C_n Hess F_n,beta_n(xi X_n)] dxi. This conditional reduction does not evaluate the planar limit or assert pointwise derivative convergence.',
    ['Every covariance C_n is PSD and the Gaussian is centered', 'All path families finite and nonempty; weights deterministic and positive on supports', 'L_n->infinity; maximum variance O(L_n)', 'Fixed 0<=a<b; median exponent convergence at both endpoints', 'log K_n/(beta_n L_n)->0'],
    section('## Conditional scale bridge', '## Independent smoothing counterexample'))

add('uniformity', 'growing-gaussian-network-soft-min-bias-counterexample', 'lemma', 'Growing path families can retain a soft-min bias',
    'For integer n>=1, let L_n=n, K_n=2^(n^2) singleton paths of unit weight, all X_i equal one shared N(0,1) variable Z, and beta_n=n. The covariance is PSD with maximum diagonal 1. Then log D_xi=xi Z but F_beta_n(xi X)=xi Z-n*log 2, so the normalized hard-min mean is 0 and normalized soft-min mean is -log 2, for every fixed xi>=0. Thus beta_n->infinity alone does not transfer individual soft-min levels uniformly in network size. This xi-independent bias cancels in endpoint differences; the example is not an endpoint-difference counterexample or a planar LFPP model.',
    ['Perfectly correlated singleton Gaussian paths', 'K_n=2^(n^2)', 'L_n=n and beta_n=n'],
    'All K_n affine path logs equal xi Z. Summing their exponentials in the soft minimum yields F_beta=xi Z-log(K_n)/beta. Since log K_n=n^2 log 2, substituting beta_n=L_n=n gives the two stated normalized means. The hard minimum has no entropy offset. The offset is constant in xi, so it cancels from endpoint differences.',
    entry_source=source('w526-C526.5-soft-min-uniformity', 'w526'))

add('gap', 'p0297-planar-lfpp-gaussian-response-uncomputed-gap', 'concept', 'P0297 gap: compute the planar integrated response',
    'OPEN ATTEMPT GAP, not a theorem: for epsilon-normalized circle-average planar LFPP, compute the limiting integrated Gaussian response L_n^(-1) integral_0^xi s E tr[C_n Hess F_n,beta_n(s X_n)] ds with smoothing error controlled relative to L_n=log(1/epsilon_n). The Hessian contains a nonnegative within-path term minus beta_n times a nonnegative path-selection term; neither concentration nor almost-sure path uniqueness evaluates their difference. Canonical xi=gamma/d_gamma and lambda(xi)=1-xi*(2/gamma+gamma/2) then relate this crossing exponent to d_gamma. Current openness UNKNOWN as of this audit; no exact dimension is claimed.',
    ['Canonical gamma-LQG with gamma in (0,2)', 'Actual planar LFPP covariance and path family', 'Scale and smoothing hypotheses must be verified'])

relations = [
    {'from_key':'integrated','to_key':'response','kind':'depends_on','rationale':'Integrate the finite Gaussian response at fixed beta, then use the uniform soft-min endpoint error.'},
    {'from_key':'switch','to_key':'omit-route','kind':'refutes','rationale':'Both path Hessians vanish while the expectation has nonzero derivative -1/sqrt(pi).'},
    {'from_key':'switch','to_key':'response','kind':'specializes','rationale':'Take two unit-weight singleton paths and covariance I_2; only the path-selection covariance remains.'},
    {'from_key':'comparison','to_key':'response','kind':'depends_on','rationale':'A_beta<=v and B_beta>=0 bound the finite derivative before integration.'},
    {'from_key':'comparison','to_key':'integrated','kind':'depends_on','rationale':'Pass from the smooth comparison to the hard finite minimum using the endpoint error.'},
    {'from_key':'scale','to_key':'integrated','kind':'depends_on','rationale':'Use the integrated identity with beta_n chosen to make the normalized endpoint error vanish.'},
    {'from_key':'scale','to_key':'transfer','kind':'depends_on','rationale':'Replace median log-distance exponents by mean log-distance exponents under variance growth.'},
    {'from_key':'uniformity','to_key':'scale','kind':'semantic_association','rationale':'Shows why beta_n tending to infinity alone is not a uniform control of individual soft-min levels; does not refute the stated endpoint reduction.'},
    {'from_key':'gap','to_key':'scale','kind':'cites','rationale':'The conditional identity identifies the missing planar quantity without computing it.'},
    {'from_key':'gap','to_key':'canonical','kind':'cites','rationale':'These exact published parameter relations relate the unknown crossing exponent to d_gamma.'},
    {'from_key':'canonical','to_existing_logical':'math:probability.core:attempt-p0297-exact-hausdorff-dimension-of-liouville-quantum-gravity','kind':'cites','rationale':'The read-only P0297 attempt already derives xi*d_gamma=gamma and leaves the normalization exponent unresolved.'},
    {'from_key':'transfer','to_existing_logical':'math:probability.concentration:gaussian-lipschitz-concentration','kind':'cites','rationale':'The corrected card requires standard Gaussian input and global Euclidean Lipschitz continuity; the proof explicitly establishes both after the covariance square root.'}
]
bundle = {'spec':'mathbrain-draft-v1','author_agent':'w525','bundle_slug':'p0297-finite-gaussian-lfpp-response-w525-001','entries':entries,'relations':relations}
keys = {entry['key'] for entry in entries}
allowed_relations = {'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
for entry in entries:
    assert entry['kind'] in {'definition','concept','lemma','theorem'}
    assert (entry['proof_text'] is None) if entry['kind'] in {'definition','concept'} else bool(entry['proof_text'])
    assert entry['source']['license'].startswith(('owner-own-work','arxiv-nonexclusive'))
for edge in relations:
    assert edge['from_key'] in keys and edge['kind'] in allowed_relations
    assert (edge.get('to_key') in keys) or edge.get('to_existing_logical')
dependencies = {key:[] for key in keys}
for edge in relations:
    if edge['kind']=='depends_on': dependencies[edge['from_key']].append(edge['to_key'])
def visit(key, stack):
    assert key not in stack
    for target in dependencies[key]: visit(target, stack+[key])
for key in keys: visit(key, [])
(ROOT/'bundle_001.json').write_text(json.dumps(bundle,indent=2,ensure_ascii=False),encoding='utf-8')

rows=[]
statuses={'response':'independently checked proof','integrated':'independently checked proof','switch':'independently checked proof','transfer':'proved special case','comparison':'proved special case','scale':'proved special case','uniformity':'proved special case','canonical':'sketch','omit-route':'proved special case','gap':'conjecture'}
for number,entry in enumerate(entries,1):
    rows.append({'claim_id':f'w525-C{number:03d}','statement':entry['statement'],'assumptions':entry['assumptions'],'source':entry['source'],'proof_or_counterexample':entry['proof_text'] or ('Explicitly refuted by the two-route entry.' if entry['key']=='omit-route' else 'Concept/draft; no solution proof.'), 'independent_reviewer':'w526 independent finite derivation; w527 referee pending' if entry['key'] in {'response','integrated','switch','transfer'} else 'w527 pending; source w526 for uniformity example', 'remaining_gap':'No evaluation of the planar LFPP response; no exact general d_gamma.', 'status':statuses[entry['key']], 'review_scope':'w526 checked the variance bound and exponent transfer; sharp Cantelli median constant still awaits w527' if entry['key']=='transfer' else 'Finite statement only; no P0297 solution audited'})
rows.append({'claim_id':'w525-C011','statement':'At the known Brownian LQG parameter, the prior D0049-A001 equation d_gamma=2Q/xi gives 10, while canonical gamma/xi gives 4. The local parameter guard rejects this inconsistent row and accepts two consistent controls. Passing the guard does not prove a dimension.', 'assumptions':['gamma=sqrt(8/3), xi=1/sqrt(6), Q=5/sqrt(6)', 'Known d_gamma=4'], 'source':'PRIOR_RECORDS.json: D0049-A001; primary Problem 7.1 and equation (1.5); measurements/bridge_validation.json', 'proof_or_counterexample':'Exact anchor algebra and measured 0->1 bad-row rejection, with 2/2 consistent controls retained.', 'independent_reviewer':'w527 pending','remaining_gap':'Guard is a narrow staged repair; not integrated into a live recall or validator.','status':'proved special case'})
rows.append({'claim_id':'w525-C012','statement':'A brain.py recall of P0297 Liouville quantum gravity LFPP proof mistakes returned zero LQG-topic hits in its top three, including two film memories. The targeted math-brain query returned three relevant topic cards among four hits. These are two different readers, not a measured live recall-code improvement.', 'assumptions':['Single recorded run of each named query on 2026-10-10'], 'source':'measurements/memory_recall.json; MATH_BRAIN_EVIDENCE.json', 'proof_or_counterexample':'Recorded output and complete relevant card bodies; no blind test material used.', 'independent_reviewer':'w527 pending','remaining_gap':'Phrase/identifier routing repair proposed only; must measure again after reviewed integration.','status':'numerical evidence'})
with (ROOT/'CLAIMS.jsonl').open('a',encoding='utf-8') as stream:
    for row in rows: stream.write(json.dumps(row,ensure_ascii=False)+'\n')

card_evidence=json.loads((ROOT/'MATH_BRAIN_EVIDENCE.json').read_text(encoding='utf-8-sig'))['complete_cards']
old_by_logical={json.loads(card['metadata_json']).get('logical_id'):card for card in card_evidence}
by_key={entry['key']:entry for entry in entries}
with (ROOT/'EDGES.jsonl').open('w',encoding='utf-8') as stream:
    for edge in relations:
        target = by_key[edge['to_key']]['statement'] if edge.get('to_key') else old_by_logical[edge['to_existing_logical']]['body']
        stream.write(json.dumps({**edge,'from_statement_quote':by_key[edge['from_key']]['statement'],'to_statement_quote':target,'status':'draft; independent referee and coordinator integration pending'},ensure_ascii=False)+'\n')

hook={'id':'lqg-w525-01','area':'math','event':'stage-start','cue':'Proof differentiates an expected minimum over Gaussian paths or sends a soft-min approximation to a growing LFPP network.', 'fire_when':'Dropping the beta-weighted route covariance because the optimum is unique, or assuming beta_n->infinity alone controls growing path entropy.', 'silent_when':'A single fixed route is analyzed, or the proof retains the integrated covariance and proves normalized smoothing error vanishes.', 'text':'When differentiating a Gaussian path minimum, retain path changes. Two routes give derivative -1/sqrt(pi) although fixed-route Hessians vanish. For growing networks, control log|P|/(beta L); beta->infinity alone does not control levels.', 'evidence':'w525/ATTEMPT.md Lemmas 1-2; measurements/bridge_validation.json response error 0.56418958 -> 0.00000708031; w526 C526.5','proposer':'w525'}
assert len(hook['text'])<=300
(ROOT/'hook_proposal.jsonl').write_text(json.dumps(hook,ensure_ascii=False)+'\n',encoding='utf-8')
patchdir=ROOT/'patches'; patchdir.mkdir(exist_ok=True)
live='~/math-brain-build/src/math_brain/lfpp_parameter_check.py'
lines=(ROOT/'lfpp_parameter_check.py').read_text(encoding='utf-8').splitlines(keepends=True)
(patchdir/'01_lfpp_parameter_check.diff').write_text(''.join(difflib.unified_diff([],lines,fromfile='a/'+live,tofile='b/'+live)),encoding='utf-8')
live_hook='~/primary_directive/hooks1000/proposals/lqg-w525.jsonl'
(patchdir/'02_lqg_hook_proposal.diff').write_text(''.join(difflib.unified_diff([],[(ROOT/'hook_proposal.jsonl').read_text(encoding='utf-8')],fromfile='a/'+live_hook,tofile='b/'+live_hook)),encoding='utf-8')

max_error=max(row['absolute_error'] for row in MEASURE['correlated_gaussian_checks'])
report=(f'The finite Gaussian LFPP bridge is proved at the author level; w526 independently derived its central response identity, integrated soft-min limit, and variance transfer. P0297 is not solved. The hardest gap is the value of the normalized planar integrated response. The exact primary statement and historical openness are in SOURCE_STATUS.json; current openness is UNKNOWN.\n\n'
        f'The measured failure is path selection: discarding it predicts derivative 0, while the exact two-route value is -1/sqrt(pi)=-0.5641895835. Retaining it at beta=256 reduces numerical response error to {MEASURE["retained_switch_response"][-1]["absolute_error"]:.9g}. Positive- and negative-correlation Gaussian checks agree with independent finite differences within {max_error:.9g}; common Gaussian modes leave the response unchanged within {MEASURE["common_mode_invariance_error"]:.9g}. These are small numerical controls, not a planar LFPP proof. Command: python -X utf8 validate_bridge.py, after the fresh compute gate recorded in measurements/compute_gate.json; actual validation time {MEASURE["elapsed_seconds"]:.3f}s, exceeding the intended 30s under machine load. Do not repeat the passed controls.\n\n'
        'A prior intake equation d_gamma=2Q/xi predicts 10 rather than the known Brownian value 4. The staged parameter guard rejects that one bad row (unchecked 0/1 rejected, guarded 1/1 rejected) and retains 2/2 consistent controls, including an unproved generic parameter choice marked as unproved. This is a narrow proposed admission check, not an accuracy claim for arbitrary formulas. The retrieved P0297 store card already has the correct scalar relation.\n\n'
        'General memory recall missed the LQG topic in all top three hits; the targeted math-brain reader found three topic cards among four. Full hypotheses were compared: correlated Gaussian fields need a covariance square root and a proved global Lipschitz bound before Gaussian concentration applies. The bounded recall repair is a precise P0297/LFPP source alias plus a normalization check; neither global recall controls nor a live store was changed.\n\n'
        'Apply patches/01_lfpp_parameter_check.diff to add the named live-path module; it is a standalone proposal requiring reviewer wiring. Apply patches/02_lqg_hook_proposal.diff to stage the measured hook for the usual two-auditor process. Numeric tests are validate_bridge.py; complete proof and scope are ATTEMPT.md. The reviewer must audit claims and sources before the coordinator integrates the draft bundle. No live integrator, seal, manifest, or store mutation is performed by this worker.\n\n'
        'Risks: finite Gaussian identities do not evaluate the dimension; quadrature is not certified integration; arbitrary mesh-size and smoothing limits cannot be swapped; d=gamma/xi is a normalization identity rather than a solution formula. NEXT: bound the normalized integrated route-fluctuation term for circle-average planar LFPP, keeping the proved entropy control.\n')
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
review=('Review packet for w527, from w525, 2026-10-10.\n\n'
        'Read SOURCE_STATUS.json for the precise target, assumptions, primary locators, and current-status qualification. ATTEMPT.md contains every author proof and the single hardest remaining gap. CLAIMS.jsonl records statement, assumptions, source, reviewer, proof/counterexample, status, and gap per item. EDGES.jsonl quotes both exact endpoints for every proposed relation.\n\n'
        'The statement-only packet went to w526 first (mesh msg-7a4ca3e038). Their independent derivation is ~/brain_workers/w526/FINITE_BRIDGE_INDEPENDENT.md. They support the finite identity, integrated beta limit, and variance transfer, and supply the level-bias counterexample C526.5. Their median bound used sqrt(2 Var); audit the stronger Cantelli bound used in w525. The counterexample bias cancels in endpoint differences; do not overstate its scope.\n\n'
        'Please check: the sign and coefficient of the path covariance in the Gaussian Hessian; justification of integration before smoothing removal; Lipschitz continuity under an arbitrary PSD covariance square root including ties; mean-to-median transfer; the explicit log K_n/(beta_n L_n) condition; and the epsilon cost convention at the published Brownian anchor. The finite quadratic comparison only recovers a known published bound.\n\n'
        'Measurements: measurements/bridge_validation.json, produced by validate_bridge.py behind measurements/compute_gate.json. The checks passed once and have not been repeated. Stage-only code: lfpp_parameter_check.py and patches/01_lfpp_parameter_check.diff. Proposed hook: hook_proposal.jsonl and patches/02_lqg_hook_proposal.diff.\n\n'
        'bundle_001.json contains DRAFT typed nodes and relations. All own work has owner-own-work source tags; the published parameter concept is a facts-only paraphrase with an arxiv-nonexclusive source. Submitted/reviewed/ingested/retrievable states are separately recorded in SUBMISSION_STATUS.json. A source/hash or numerical receipt must not be counted as a theorem proof.\n\n'
        'Verdict requested: keep/fix/drop each finite claim and exact edge; do not certify P0297 as solved. NEXT: audit the finite packet, then evaluate the planar response only if there is a concrete method to bound its route term.\n')
(ROOT/'REVIEW_PACKET.md').write_text(review,encoding='utf-8')
submission={'bundle_local':str(ROOT/'bundle_001.json'),'bundle_inbox':'~/math-brain-inbox/w525/bundle_001.json','draft_prepared':True,'submitted':False,'reviewed':{'independent_adversary':'w526 core finite statements derived independently; sharp median constant and new comparison not fully audited','referee':'w527 pending','full_bundle_kept':False},'ingested':False,'retrievable':False,'live_store_mutated':False,'counts':{'entries':len(entries),'relations':len(relations),'claim_rows_appended':len(rows)},'next':'Submit the completed draft only; coordinator audits and integrates.'}
(ROOT/'SUBMISSION_STATUS.json').write_text(json.dumps(submission,indent=2),encoding='utf-8')
print(json.dumps({'entries':len(entries),'relations':len(relations),'claim_rows_appended':len(rows),'local_bundle_validated':True,'referee_pending':True},indent=2))
