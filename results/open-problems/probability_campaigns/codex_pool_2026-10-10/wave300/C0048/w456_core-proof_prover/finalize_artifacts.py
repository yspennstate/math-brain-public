"""Package author-checked mathematics as draft concepts, without live ingestion."""
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w456')
HOOK_PATH = Path('~/primary_directive/hooks1000/proposals/math-w456.jsonl')
NOW = datetime.now(timezone.utc).isoformat()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


measurement = json.loads((ROOT / 'measurements.json').read_text(encoding='utf-8'))
assert measurement['cases'] == 72 and measurement['corrected_identity_failures'] == 0
examples = []
for row in measurement['records']:
    full = Fraction(row['pressure_derivatives'][2])
    omitted = full - Fraction(row['omission_residual_order4'])
    if (full > 0) != (omitted > 0):
        examples.append({'graph': row['graph'], 'q': row['q'], 'exp_beta': row['exp_beta'], 'full': str(full), 'omitted': str(omitted)})

lines = [
    '# Exact finite-volume measurement receipt', '',
    'Command: python -X utf8 ~/brain_workers/w456/run_checks.py', '',
    f"Fresh governor age {measurement['gate_age_seconds']:.4f} seconds at checker launch; compute_gate.json records the governor decision and inherited priority. No GPU, model load or live-store write.", '',
    f"Independent exact enumerations: {measurement['spin_configurations']} spin configurations and {measurement['fk_configurations']} FK configurations across {measurement['cases']} cases (six graphs, q=2,3,4,5 and exp(beta)=1,2,4).",
    f"Complete cumulant identities: {measurement['corrected_identity_failures']} failures. Diagnostic formula omitting 3 a2^2 Var(S2): {measurement['incomplete_formula_failures']} failures, including {measurement['quartic_sign_differences']} wrong quartic signs. The incomplete formula is not a deployed baseline.",
    f"Checker CPU: {measurement['cpu_seconds']:.5f} seconds; checker wall time: {measurement['wall_seconds']:.6f} seconds. Every residual uses exact fractions.", '',
    '| graph | q | exp(beta) | complete P fourth derivative | omitted-variance formula |',
    '|---|---:|---:|---:|---:|',
]
for item in examples:
    lines.append(f"| {item['graph']} | {item['q']} | {item['exp_beta']} | {item['full']} | {item['omitted']} |")
lines += ['', 'Scope: a finite algebra check plus the written L1 proof. It proves no infinite-volume limit, critical uniformity, model novelty, Lean theorem or C0048 solution.', '', 'NEXT: Review the exact finite identities and the uniform-potential obstruction; SP(q,d) remains the missing lattice input.']
(ROOT / 'MEASUREMENTS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

source = json.loads((ROOT / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source['primary_statement'].update({'locator': 'Conjecture 2, printed p.93 / PDF index 92', 'checked_directly': True, 'normalization_locator': 'Proposition 1.3 and Corollary 1.4, pp.9-10', 'short_quote': 'with d >= 3) is discontinuous for any q >= 3.'})
source['recall']['fallback_read_pending'] = False
source['recall']['fallback_used'] = 'perceptron_proof_open_gaps_fleet_2026_07_12'
source['reason'] = 'Historical primary conjecture confirmed. Bounded literature/owner-record searches found no certified complete proof; absence of a found proof does not establish current openness.'
source['bounded_recent_primary_checks'] = [
    {'url': 'https://arxiv.org/abs/math/0207242', 'scope': 'sufficiently high dimensions or sufficiently strong mean-field first-order transition'},
    {'url': 'https://arxiv.org/abs/2501.14320', 'scope': 'quantum fuzzy-sphere finite-size study; not a proof of the nearest-neighbour classical target'},
    {'url': 'https://arxiv.org/abs/1611.09877', 'scope': 'planar q>4 discontinuity'},
    {'url': 'https://arxiv.org/abs/1505.04159', 'scope': 'planar q=2,3,4 continuity; control against a bare cubic-sign argument'},
]
source['owner_prior_lookup'] = {'scope': 'Targeted C0048/Potts queries in the named intakes, H/I attempts, Lean annotations, Team O board and owner notes/research; no complete C0048 proof receipt found. Quantitative historical assertions remain unaudited.', 'canonical_store_receipt': 'store_target_lookup.json', 'limitations': 'Not an exhaustive owner-work or literature review; openness UNKNOWN.'}
source['review_state'] = 'Author proof packet sent to w458; independent receipt and served-model attestation pending.'
write_json(ROOT / 'SOURCE_STATUS.json', source)

claims_path = ROOT / 'CLAIMS.jsonl'
claims = [json.loads(line) for line in claims_path.read_text(encoding='utf-8').splitlines() if line.strip()]
for row in claims:
    if row['claim_id'] == 'w456-C0048-target-001':
        row['statement'] = 'For every integer q,d>=3, the zero-field unit-coupling nearest-neighbour ferromagnetic Potts model on Z^d has M(beta_c)>0, where M(beta)=(q mu_beta^1(sigma_0=1)-1)/(q-1), beta_c=inf{beta>=0:M(beta)>0}, and mu_beta^1 is the monochromatic colour-1 boundary limit. Equivalently the wired FK law at p_c with p=1-exp(-beta) has positive origin infinite-cluster probability.'
        row['source'] = {'url': 'https://arxiv.org/pdf/1707.00520', 'locator': 'Conjecture 2, printed p.93; normalization pp.9-10', 'local_record': 'STATEMENT.md'}
        row['remaining_gap'] = 'The lattice uniform-potential input SP(q,d) in ATTEMPT.md is unproved; no solution claim.'
extra = [
    {'claim_id': 'w456-L2-L3', 'status': 'proved special case', 'statement': 'For finite free-boundary Potts pressure with A=P second derivative at 0>0 and B=P third derivative, I(m)=m^2/(2A)-B m^3/(6A^3)+O(m^4) locally. E[S3]/N >= (E[S2]/N)^2. If I(m)<=m^2/(2A)-b m^3+C m^4 on [0,r0], with b,C>0 and r0>=b/(2C), then A<=2C/b^2.', 'assumptions': ['finite nonempty graph', 'integer q>=2', 'free boundary and zero field', 'beta finite and >=0', 'the stated uniform remainder bound is an additional hypothesis'], 'source': 'ATTEMPT.md L2--L3', 'proof_or_counterexample': 'Invert the analytic pressure derivative; Cauchy--Schwarz and Jensen give the cluster moment inequality; nonnegative Legendre transform at m=b/(2C) gives the susceptibility bound.', 'independent_reviewer': 'w458 pending', 'remaining_gap': 'No uniform critical remainder or positive uniform cubic coefficient for Z^d is established.'},
    {'claim_id': 'w456-entropy', 'status': 'proved special case', 'statement': 'For scalar independent-colour entropy J_q(m) along x1=(1+(q-1)m)/q and xother=(1-m)/q, q integer>=3 and 0<r0<1, the potential J_q(m)-lambda m^2 obeys L4 with b=(q-1)(q-2)/6 and C=(q-1)*((q-1)^3+(1-r0)^(-3))/(12q). For q=3,r0=1/2, no stationary point with potential <= its zero value lies in (0,1/16).', 'assumptions': ['scalar mean-field entropy potential only', 'arbitrary real lambda', 'stationarity and potential comparison'], 'source': 'ATTEMPT.md final section', 'proof_or_counterexample': 'The fourth entropy derivative is bounded by K; Taylor integral remainders give C=K/24 and |R prime|<=4C m^3; apply L4.', 'independent_reviewer': 'w458 pending', 'remaining_gap': 'No identification of this scalar potential with the spatially correlated lattice potential.'},
    {'claim_id': 'w456-exact-enumeration', 'status': 'numerical evidence', 'statement': 'Exact rational enumeration checked all L1 pressure derivatives of orders 2,3,4 and partition-function agreement in 72 finite graph/q/temperature cases; complete identities had 0 failures, the deliberately incomplete fourth formula had 40 failures and 2 wrong signs.', 'assumptions': ['six named graphs with <=4 vertices and <=6 edges', 'q in {2,3,4,5}', 'exp(beta) in {1,2,4}', 'free boundary and zero field'], 'source': 'measurements.json, MEASUREMENTS.md, verify_cumulants.py, compute_gate.json', 'proof_or_counterexample': {'method': 'Independent integer-weight spin enumeration versus FK edge enumeration and exact Fraction arithmetic.', 'sign_counterexamples': examples}, 'independent_reviewer': 'w458 pending', 'remaining_gap': 'Finite computation is not an infinite-volume proof or formal theorem check.'},
]
known = {row['claim_id'] for row in claims}
claims.extend(row for row in extra if row['claim_id'] not in known)
claims_path.write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in claims), encoding='utf-8')

def entry(key, name, title, statement, assumptions, kind='concept'):
    return {'key': key, 'namespace': 'probability.potts', 'logical_name': name, 'kind': kind, 'title': title, 'statement': statement, 'proof_text': None, 'assumptions': assumptions, 'domain': 'probability and statistical mechanics', 'source': {'source_id': 'owner-own-work:w456:C0048-campaign', 'url': 'file:///~/brain_workers/w456/ATTEMPT.md', 'revision': 'author-checkpoint-2026-10-10', 'license': 'owner-own-work', 'excerpt': None}, 'review_status': 'DRAFT; independent and served-model gates pending', 'parent_problem_status': 'C0048 UNSOLVED by this packet; current openness UNKNOWN'}

entries = [
    entry('powers', 'free-fk-cluster-power-sums', 'Free FK cluster power sums', 'For a finite graph G with N vertices and an FK edge configuration omega, let S_j(omega)=sum_C |C|^j over every open cluster C, including isolated vertices. Thus S_1=N. Cluster sizes are random under the FK law; independent cluster colouring does not make the sizes independent.', ['finite graph', 'open connected components including isolated vertices'], 'definition'),
    entry('cumulants', 'draft-free-potts-field-cumulants-through-four', 'DRAFT: exact free Potts field cumulants', 'AUTHOR-DERIVED FINITE IDENTITY, pending independent proof admission. For a nonempty finite graph, integer q>=2, finite beta>=0, free-boundary zero-field Potts weights exp(beta sum_e 1{same colour}), let X=sum_x(1{sigma_x=1}-1/q), P(h)=N^(-1)log E[exp(hX)], and S_j=sum_C |C|^j under free FK with p=1-exp(-beta). With a2=(q-1)/q^2, a3=(q-1)(q-2)/q^3, a4=(q-1)(q^2-6q+6)/q^4, P second and third derivatives at zero are a2 E[S2]/N and a3 E[S3]/N. The fourth is (a4 E[S4]+3 a2^2 Var(S2))/N. No uniform thermodynamic remainder follows.', ['all hypotheses in the statement', 'free FK expectations at zero field']),
    entry('omission', 'draft-potts-fourth-cumulant-variance-omission-obstruction', 'DRAFT: obstruction to averaging conditional fourth cumulants', 'FINITE DIAGNOSTIC, pending independent proof admission. Under the free, zero-field finite Potts hypotheses of the exact cumulant identity, averaging conditional fourth cumulants misses 3 a2^2 Var(S2)/N, a nonnegative term. Exact spin/FK enumeration on six graphs with q=2,3,4,5 and exp(beta)=1,2,4 found 40 failures in 72 cases when this term was dropped, including two wrong quartic signs. The complete identity had zero failures. This does not prove a critical transition.', ['random FK cluster sizes', 'conditionally independent uniform cluster colours', 'measurement scope explicitly finite']),
    entry('exclusion', 'draft-quantitative-cubic-stationary-minimum-exclusion', 'DRAFT: quantitative cubic stationary-minimum exclusion', 'AUTHOR-DERIVED CONDITIONAL LEMMA, pending independent proof admission. Let r0,b>0,C>=0 and differentiable F(m)=a m^2-b_t m^3+R(m) on [0,r0], with b_t>=b, |R(m)|<=C m^4 and |R prime(m)|<=4C m^3. No interior stationary point with F(m)<=F(0)=0 can have 0<m<min(r0,b/(6C)) when C>0; when C=0 no such interior point exists. Substituting stationarity yields F(m)>=b m^3/2-3C m^4.', ['all bounds on a common interval', 'stationarity', 'potential comparison']),
    entry('sp', 'unproved-uniform-potts-scalar-potential-input', 'UNPROVED: uniform Potts scalar-potential input', 'MISSING INPUT, not asserted true. Fix integer q,d>=3, zero-field unit-coupling nearest-neighbour Potts on Z^d, and M(beta)=(q mu_beta^1(sigma_0=1)-1)/(q-1), beta_c=inf{beta:M(beta)>0}. Seek delta,r0,b>0,C>=0, independent of beta and volume, so every beta_c<beta<beta_c+delta with 0<M(beta)<r0 admits a differentiable F_beta(m)=a_beta m^2-b_beta m^3+R_beta(m), b_beta>=b, |R_beta|<=C m^4, |R_beta prime|<=4C m^3 on [0,r0], with F_beta prime(M(beta))=0 and F_beta(M(beta))<=F_beta(0)=0. Only the scalar mean-field entropy special case is established. The lattice input, particularly q=d=3, remains unproved.', ['unproved proposed input for the actual lattice model', 'uniform constants and physical stationarity/minimum link']),
    entry('bridge', 'draft-uniform-cubic-potential-implies-critical-potts-order', 'DRAFT: uniform cubic potential implies critical Potts ordering', 'CONDITIONAL REDUCTION ONLY, pending independent proof admission. For integer q,d>=3 and normalized monochromatic-boundary magnetization M(beta), assume the entire uniform-potential input stated in this bundle on (beta_c,beta_c+delta). The exclusion lemma gives M(beta)>=eta=min(r0,b/(6C)) for C>0, or eta=r0 for C=0. Finite-box magnetizations are continuous in beta and decrease with box size; their infimum M is upper semicontinuous and nondecreasing. Hence M is right-continuous at beta_c and M(beta_c)>=eta>0. The uniform-potential input is not proved, so C0048 is not solved.', ['all uniform-potential hypotheses', 'standard FK domain and parameter comparison', 'no conclusion without the unproved input']),
]
relations = [
    {'from_key': 'cumulants', 'to_key': 'powers', 'kind': 'depends_on', 'rationale': 'The cumulant identity uses the explicitly defined cluster power sums S2,S3,S4.'},
    {'from_key': 'omission', 'to_key': 'cumulants', 'kind': 'depends_on', 'rationale': 'The diagnostic omission is exactly the variance contribution in the complete fourth-cumulant identity.'},
    {'from_key': 'bridge', 'to_key': 'exclusion', 'kind': 'depends_on', 'rationale': 'The uniform supercritical lower bound uses the stationary-minimum exclusion inequality.'},
    {'from_key': 'bridge', 'to_key': 'sp', 'kind': 'depends_on', 'rationale': 'The critical-order reduction assumes this entire explicitly unproved lattice input.'},
]
bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w456', 'bundle_slug': 'potts-c0048-cumulants-gap-001', 'entries': entries, 'relations': relations}
assert len(entries) <= 200
keys = {item['key'] for item in entries}
for item in entries:
    assert item['kind'] in ('definition', 'concept') and item['proof_text'] is None
    assert item['source']['license'].startswith('owner-own-work')
for relation in relations:
    assert relation['from_key'] in keys and relation['to_key'] in keys and relation['kind'] == 'depends_on'
adjacency = {key: [] for key in keys}
for relation in relations:
    adjacency[relation['from_key']].append(relation['to_key'])
def walk(key, visiting):
    assert key not in visiting, 'cycle in draft dependencies'
    for child in adjacency[key]:
        walk(child, visiting | {key})
for key in keys:
    walk(key, set())
write_json(ROOT / 'DRAFT_bundle_001.json', bundle)
INBOX.mkdir(parents=True, exist_ok=True)
number = 1
while (INBOX / f'bundle_{number:03d}.json').exists():
    number += 1
target = INBOX / f'bundle_{number:03d}.json'
part = target.with_suffix('.part')
write_json(part, bundle)
part.rename(target)

hook = {'id': 'potts-cumulants-w456-01', 'area': 'math', 'event': 'stage-start', 'cue': 'fourth (cumulant|pressure derivative).*(FK|random.cluster|cluster.colour)|averag.*conditional fourth cumulant', 'fire_when': 'Computing the unconditional fourth cumulant of a centred Potts field from conditional FK cluster colouring, with random cluster sizes.', 'silent_when': 'Computing only a second or third cumulant, or computing a conditional fourth cumulant with fixed cluster sizes.', 'text': 'Average conditional moments before forming the unconditional fourth cumulant. Random conditional variance adds 3 times its variance; independent cluster colours do not make cluster sizes independent.', 'evidence': '~/brain_workers/w456/MEASUREMENTS.md: omitted variance failed 40/72 exact cases and changed two signs; full identity passed 72/72.', 'proposer': 'w456'}
write_json(ROOT / 'PROPOSED_HOOK.json', hook)
HOOK_PATH.parent.mkdir(parents=True, exist_ok=True)
if not HOOK_PATH.exists() or hook['id'] not in HOOK_PATH.read_text(encoding='utf-8'):
    with HOOK_PATH.open('a', encoding='utf-8') as handle:
        handle.write(json.dumps(hook) + '\n')

pipeline = {'worker': 'w456', 'bundle': str(target), 'submitted': {'state': 'yes', 'at_utc': NOW, 'evidence': 'complete .part renamed to .json'}, 'reviewed': {'state': 'pending independent receipt and served-model evidence', 'referee': 'w458'}, 'ingested': {'state': 'NOT OBSERVED; not attempted by this worker'}, 'retrievable': {'state': 'NOT OBSERVED; no post-ingestion retrieval claimed'}, 'schema_validation': {'state': 'local structural validation passed', 'entries': len(entries), 'relations': len(relations), 'proof_promotion': 'none; definition/concept only', 'ingestor_validation': 'not run: live-store writes reserved for coordinator'}, 'hook': str(HOOK_PATH)}
write_json(ROOT / 'BRAIN_PIPELINE.json', pipeline)

report = f'''C0048 remains unsolved by this packet; current openness is UNKNOWN. The exact historical target and interaction normalization are recovered from Duminil-Copin's primary lectures, Conjecture 2, p.93. The old contour route had no proved q=3,d=3 input.

The substantive result is an exact finite free-FK cumulant identity, including the fourth-order variance term, plus a quantitative cubic exclusion lemma and a proved conditional bridge to critical magnetization. The independent-colour entropy special case gives the explicit q=3 exclusion threshold 1/16. The single remaining lattice input is SP(q,d): a physical scalar potential with a positive uniform cubic coefficient and a uniform C1 quartic remainder. It is unproved.

Measured with `python -X utf8 ~/brain_workers/w456/run_checks.py`: {measurement['cases']} exact cases, {measurement['spin_configurations']} spin and {measurement['fk_configurations']} FK configurations; complete identities 0 failures, deliberately omitted variance {measurement['incomplete_formula_failures']} failures and {measurement['quartic_sign_differences']} wrong signs. Checker CPU {measurement['cpu_seconds']:.5f} seconds, wall {measurement['wall_seconds']:.6f} seconds. Evidence: MEASUREMENTS.md and measurements.json. This measures mathematical diagnostics, not deployed recall quality.

Risk: L1 assumes free boundary and zero field; fixed or wired cluster colours alter the formulas. Finite analyticity supplies no uniform critical remainder. The mean-field potential cannot be substituted for the convex thermodynamic Legendre potential. A source/hash check or exact finite enumeration is not a proof of the parent problem. Served author/referee model identity is unverified.

How to apply: independently review REVIEW_PACKET.md, then let the validating coordinator process {target.as_posix()} under the proof/model gates. It contains six DRAFT definition/concept entries and four explicit dependencies; no theorem promotion or live-store/code edit was made. Submission, review, ingestion and retrieval are recorded separately in BRAIN_PIPELINE.json. The measured hook proposal is {HOOK_PATH.as_posix()}.

NEXT: Review L1--L5 and the exact counterexamples; then control or refute SP(q,d)'s lattice correlation correction for q=d=3.
'''
(ROOT / 'REPORT.md').write_text(report, encoding='utf-8')
review = ROOT / 'REVIEW_PACKET.md'
review.write_text(review.read_text(encoding='utf-8') + '\nMeasurement receipt is now complete: MEASUREMENTS.md and measurements.json; 72 exact cases, zero complete-identity failures, 40 omission failures and two wrong signs. Brain submission: BRAIN_PIPELINE.json.\n', encoding='utf-8')
file_evidence = {}
for name in ('STATEMENT.md', 'ATTEMPT.md', 'CLAIMS.jsonl', 'SOURCE_STATUS.json', 'MEASUREMENTS.md', 'measurements.json', 'verify_cumulants.py', 'REPORT.md', 'REVIEW_PACKET.md'):
    data = (ROOT / name).read_bytes()
    file_evidence[name] = {'path': str(ROOT / name), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
write_json(ROOT / 'REVIEW_RECEIPT.json', {'at_utc': NOW, 'scope': 'Proof-packet byte snapshot only; not integrator cryptographic ceremony or mathematical verification', 'files': file_evidence, 'served_model': {'author': 'UNKNOWN', 'referee': 'pending actual response-side evidence'}, 'bundle': str(target)})
print(json.dumps({'bundle': str(target), 'entries': len(entries), 'relations': len(relations), 'hook': str(HOOK_PATH), 'sign_examples': examples, 'claim_rows': len(claims), 'receipt': str(ROOT / 'REVIEW_RECEIPT.json')}))
