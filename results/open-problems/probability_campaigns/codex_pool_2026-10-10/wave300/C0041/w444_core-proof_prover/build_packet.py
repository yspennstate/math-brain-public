"""Prepare only this worker's review artifacts and its explicitly authorized DRAFT inbox."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w444').resolve()
assert str(INBOX).replace('\\', '/').lower() == '~/math-brain-inbox/w444'

def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

source = {
    'source_id': 'owner-probability300-w444-c0041-20261010',
    'url': 'urn:owner-probability300:w444:c0041:2026-10-10',
    'revision': 'draft-unreviewed-2026-10-10',
    'license': 'owner-own-work (campaign calculations; independent review pending)',
    'excerpt': None,
}

definitions = (
    'B(x,r)=x+[-r,r]^d intersect Z^d, r an integer >=1; '
    'L=2r+1; n_r=r(2r+1)^(d-1); b_1(y)=omega(y,+e_1)-omega(y,-e_1). '
    'For delta>0, I_delta(x,r) counts rows in B with y_1<x_1 and b_1(y)>=delta, '
    'plus rows with y_1>x_1 and b_1(y)<=-delta. The plane y_1=x_1 is ignored. '
    'A_delta,theta(x,r)={I_delta(x,r)>=2 theta n_r}, theta in (1/2,1]. '
    'D(theta||1/2)=theta log(2theta)+(1-theta)log(2(1-theta)), with 0 log 0=0.'
)

records = [
    {
        'key': 'target', 'claim_id': 'w444-C0041-TARGET',
        'logical_name': 'c0041-directional-transience-ballisticity-target-w444',
        'title': 'C0041 exact target and uncertain current openness',
        'statement': 'For a nearest-neighbor RWRE on Z^d, d>=2, sample once and retain an iid field of transition rows. Assume every allowed transition is at least a fixed kappa>0 almost surely. For a fixed unit direction ell, P_0(X_n dot ell -> +infinity)=1 is conjectured to imply P_0(liminf_n (X_n dot ell)/n>0)=1. Current openness UNKNOWN: a September 2026 primary repository claims a solution; this packet does not verify that claim and does not solve the target.',
        'assumptions': ['d>=2', 'sampled-once iid nearest-neighbor environment', 'uniform ellipticity', 'fixed unit direction', 'annealed almost-sure directional transience'],
        'status': 'conjecture',
        'proof': 'Exact original intake record: problems.jsonl line 41, source drewitz_ramirez_rwre_2014, Open question 2.20 p.24. Independently recovered formulation: Campos-Ramirez arXiv:1212.4020v3 Conjecture 1.1, with definitions immediately before it.',
        'gap': 'The full target is not proved here; current claimed external resolution is not audited.',
    },
    {
        'key': 'box-pattern', 'claim_id': 'w444-C0041-PATTERN',
        'logical_name': 'inward-row-density-box-pattern-w444',
        'title': 'Balanced inward-row density pattern for finite boxes',
        'statement': definitions,
        'assumptions': ['nearest-neighbor environment on Z^d', 'r>=1 integer', 'delta>0', 'theta in (1/2,1]'],
        'status': 'sketch', 'proof': 'Definition only. Each half-box has exactly n_r sites.',
        'gap': 'This pattern is not an exhaustive classification of traps.',
    },
    {
        'key': 'exit-moments', 'claim_id': 'w444-C0041-L1',
        'logical_name': 'uniform-elliptic-finite-box-exit-moments-w444',
        'title': 'Draft finite-box exit moment bound under uniform ellipticity',
        'statement': 'UNREVIEWED SPECIAL-CASE CLAIM. In any nearest-neighbor environment on Z^d with every transition at least kappa>0, iid is unnecessary. Let B=x+[-r,r]^d intersect Z^d, r>=1 integer, L=2r+1, p=kappa^L, and T_B be first exit. Uniformly over z in B, P_{z,omega}(T_B>mL)<=(1-p)^m, E_{z,omega}T_B<=L/p, and E_{z,omega}(T_B^s)<=M_r(s)=2^s s! L^s kappa^(-sL) for every integer s>=1.',
        'assumptions': ['fixed nearest-neighbor Markov kernel', 'all transitions >=kappa>0', 'integer r>=1', 'integer s>=1', 'start inside B'],
        'status': 'proved special case',
        'proof': 'ATTEMPT.md L1. Consecutive +e_1 steps exit in at most L moves with probability >=kappa^L from every current site. Iterated Markov conditional bounds imply geometric domination; summing yields the mean bound, and G<=_st 1+Exp(p) yields the stated s-moment bound. No block independence is assumed.',
        'gap': 'Independent mathematical review pending; a finite-box exit bound is not a regeneration-time moment bound.',
    },
    {
        'key': 'inward-entropy', 'claim_id': 'w444-C0041-L2',
        'logical_name': 'inward-row-density-iid-entropy-bound-w444',
        'title': 'Draft entropy bound for inward-oriented row density',
        'statement': 'UNREVIEWED SPECIAL-CASE CLAIM. ' + definitions + ' If environment rows are iid, P_env(A_delta,theta(x,r))<=exp(-2n_r D(theta||1/2)). At theta=1 this is at most 4^(-n_r). Combining this with uniform ellipticity, for each fixed theta>1/2, kappa>0 and integer s>=1, sum_{r>=1} 2^s s! (2r+1)^s kappa^(-s(2r+1)) exp(-2n_r D(theta||1/2)) is finite for d>=2.',
        'assumptions': ['iid site transition rows', 'delta>0', 'theta in (1/2,1]', 'for the weighted series only: d>=2, uniform ellipticity and s>=1 integer'],
        'status': 'proved special case',
        'proof': 'ATTEMPT.md L2/L2b. The two possible inward sign events at a single site are disjoint, so p_++p_-<=1. Across distinct sites independence gives the generating function [(1+a p_+)(1+a p_-)]^n_r, a=exp(lambda)-1>=0. AM-GM bounds it by [(1+exp(lambda))/2]^(2n_r). Chernoff optimization gives the entropy rate; the negative order-r^d exponent beats the exit-cost linear exponent for d>=2.',
        'gap': 'Independent review pending; irregular slow regions and general excursions are not certified by this inward-row pattern.',
    },
    {
        'key': 'adaptive-moments', 'claim_id': 'w444-C0041-L3',
        'logical_name': 'adaptive-inward-box-selection-moment-bound-w444',
        'title': 'Draft adaptive-center trap bound without false independence',
        'statement': 'UNREVIEWED SPECIAL-CASE CLAIM. Let the nearest-neighbor environment on Z^d have iid rows and every allowed transition at least kappa>0. ' + definitions + ' For integer s>=1 put M_r(s)=2^s s! (2r+1)^s kappa^(-s(2r+1)). Let H be a genuine stopping time for the walk filtration enlarged by its entire fixed environment. Let C be an F_H-measurable integer center, with |C|_infinity<=N and X_H in B(C,r) on H<=N, for deterministic integer N>=0. Set Y equal to the exit time from that box measured after H and Y=0 on H>N. Then E_0[1_{H<=N}1_{A_delta,theta(C,r)}Y^s]<=M_r(s) min(1,(2N+1)^d exp(-2n_r D(theta||1/2))). Under Q=P_0(.|D^ell=infinity), q=P_0(D^ell=infinity)>0, where D^ell is first strict backtracking below the initial ell projection, this nonnegative moment is at most the same bound divided by q. Regeneration times cannot replace H because they depend on the future.',
        'assumptions': ['iid uniformly elliptic nearest-neighbor environment', 'H a stopping time with full environment included', 'C measurable at H', 'deterministic bounded center set', 'integer s>=1', 'delta>0, theta>1/2', 'q>0 only for the conditional-law extension'],
        'status': 'proved special case',
        'proof': 'ATTEMPT.md L3. Quenched strong Markov bounds the conditional moment after H uniformly in all centers and sites. Average, then union-bound the deterministic (2N+1)^d possible centers using L2b. For Q, use 1_{D=infinity}<=1 and divide by q; no Markov or fresh-row assertion is used under Q.',
        'gap': 'Independent review pending. This bound grows with N and controls one exit, not all delay before regeneration.',
    },
    {
        'key': 'renewal-reduction', 'claim_id': 'w444-C0041-R1',
        'logical_name': 'integrable-iid-cycle-positive-velocity-reduction-w444',
        'title': 'Draft conditional renewal reduction to positive speed',
        'statement': 'UNREVIEWED CONDITIONAL REDUCTION. Suppose a nearest-neighbor walk is divided after a finite initial time into actual iid cycles, with integer durations S_i>=1 and displacements Z_i, satisfying |Z_i|_1<=S_i. If E[S_1]<infinity and E[Z_1 dot ell]>0, then X_n/n -> E[Z_1]/E[S_1] almost surely, with positive ell projection. The actual iid cycle law and its finite duration mean are explicit inputs, not consequences proved from C0041 in this packet.',
        'assumptions': ['nearest-neighbor path', 'finite initial cycle boundary', 'actual iid subsequent cycles', 'E S_1 finite', 'E(Z_1 dot ell)>0'],
        'status': 'proved special case',
        'proof': 'ATTEMPT.md R1. Strong laws at cycle boundaries give the ratio. Finite first moment implies sum_k P(S_k>epsilon k)<infinity, so Borel-Cantelli gives S_k/k->0. The remaining partial cycle has displacement bounded by its duration and vanishes after dividing by n.',
        'gap': 'Independent review pending; this does not establish regeneration integrability under directional transience.',
    },
    {
        'key': 'remaining-gap', 'claim_id': 'w444-C0041-GAP',
        'logical_name': 'c0041-regeneration-integrability-missing-input-w444',
        'title': 'C0041 hardest remaining input in the finite-trap route',
        'statement': 'UNPROVED INPUT. Under only iid, uniformly elliptic nearest-neighbor RWRE on Z^d, d>=2, and annealed almost-sure transience in a fixed unit direction ell, show E_Q[tau_1]<infinity for Q=P_0(.|D^ell=infinity), D^ell first strict backtracking below the initial projection, and the standard time-valued directional regeneration tau_1=S_K at the first successful fresh-record attempt K. This is equivalent to summability of Q(tau_1>m). The present inward-box bounds do not classify arbitrary slow regions, excursions or repeated entries and cannot supply this input.',
        'assumptions': ['exact full C0041 hypotheses', 'standard time-valued regeneration construction', 'q=P_0(D^ell=infinity)>0'],
        'status': 'conjecture', 'proof': 'No proof. ATTEMPT.md states the exact attempted bridge and why the proved special-case bounds do not imply it.',
        'gap': 'The integrated tail of a genuine regeneration duration remains uncontrolled under only the target hypotheses.',
    },
]

claims_path = ROOT / 'CLAIMS.jsonl'
existing = [json.loads(line) for line in claims_path.read_text(encoding='utf-8').splitlines() if line.strip()]
ids = {item['claim_id'] for item in existing}
with claims_path.open('a', encoding='utf-8', newline='\n') as handle:
    for item in records:
        if item['claim_id'] in ids:
            continue
        claim = {
            'claim_id': item['claim_id'], 'candidate': 'C0041', 'statement': item['statement'],
            'assumptions': item['assumptions'], 'source': dict(source, supporting_file=str(ROOT / 'ATTEMPT.md')),
            'proof_or_counterexample': item['proof'], 'independent_reviewer': 'w446 (pending)',
            'remaining_gap': item['gap'], 'status': item['status'], 'independent_review_status': 'NOT_YET_REVIEWED',
            'parent_problem_solved': False,
        }
        handle.write(json.dumps(claim, ensure_ascii=False) + '\n')

entries = [{
    'key': item['key'], 'namespace': 'probability.randomenvironment',
    'logical_name': item['logical_name'], 'kind': 'concept', 'title': item['title'],
    'statement': item['statement'], 'proof_text': None, 'assumptions': item['assumptions'],
    'domain': 'probability, random walks in random environments', 'source': source,
} for item in records]

tail_entry = {
    'key': 'radius-tail', 'namespace': 'probability.randomenvironment',
    'logical_name': 'future-dependent-time-radius-to-duration-tail-bound-w444',
    'kind': 'concept', 'title': 'Draft radius-to-duration tail reduction without a stopping-time assumption',
    'statement': 'UNREVIEWED CONDITIONAL REDUCTION. For a UE nearest-neighbor walk started at 0, any almost surely finite positive integer-valued time tau (not necessarily a stopping time), and Q=P_0(.|E) with q=P_0(E)>0, put R=max_{0<=j<=tau}|X_j|_infinity. Then for integer r>=1,t>=0, Q(tau>t)<=Q(R>r)+q^(-1)(1-kappa^(2r+1))^floor(t/(2r+1)). If Q(R>r)<=C exp(-a r) for a>2log(1/kappa), then E_Q[tau]<infinity. This is an additional sufficient radius assumption, not a conclusion proved from directional transience.',
    'proof_text': None,
    'assumptions': ['uniform ellipticity with 0<kappa<1', 'walk starts at 0', 'tau finite integer-valued Q-almost surely', 'q>0', 'extra exponential radius tail only for the integrability conclusion'],
    'domain': 'probability, random walks in random environments', 'source': source,
}
entries.append(tail_entry)
if 'w444-C0041-T1' not in ids:
    with claims_path.open('a', encoding='utf-8', newline='\n') as handle:
        handle.write(json.dumps({
            'claim_id': 'w444-C0041-T1', 'candidate': 'C0041',
            'statement': tail_entry['statement'], 'assumptions': tail_entry['assumptions'], 'source': source,
            'proof_or_counterexample': 'ATTEMPT.md T1: {tau>t,R<=r} implies exit from fixed B(0,r) occurs after t. Remove the conditioning event at cost 1/q, apply L1, and optimize r=floor(beta log(t+1)), 1/a<beta<1/(2log(1/kappa)). Both tails are summable under the extra radius assumption.',
            'independent_reviewer': 'w446 (pending)', 'remaining_gap': 'Independent review pending; the extra exponential radius tail has not been derived from the C0041 hypotheses.',
            'status': 'proved special case', 'independent_review_status': 'NOT_YET_REVIEWED', 'parent_problem_solved': False,
        }, ensure_ascii=False) + '\n')

relations = [
    {'from_key': 'inward-entropy', 'to_key': 'box-pattern', 'kind': 'depends_on', 'rationale': 'The entropy calculation uses exactly the balanced row-density pattern defined here.'},
    {'from_key': 'inward-entropy', 'to_key': 'exit-moments', 'kind': 'depends_on', 'rationale': 'Only the weighted-moment series part uses the finite-box exit moment bound.'},
    {'from_key': 'adaptive-moments', 'to_key': 'inward-entropy', 'kind': 'depends_on', 'rationale': 'The deterministic-center union bound uses the precise inward-row entropy estimate.'},
    {'from_key': 'adaptive-moments', 'to_key': 'exit-moments', 'kind': 'depends_on', 'rationale': 'The quenched stopping-time step uses the uniform finite-box moment estimate.'},
    {'from_key': 'remaining-gap', 'to_key': 'renewal-reduction', 'kind': 'semantic_association', 'rationale': 'The missing finite cycle-duration mean is an explicit premise in this conditional positive-speed reduction.'},
    {'from_key': 'remaining-gap', 'to_key': 'target', 'kind': 'semantic_association', 'rationale': 'This is an unproved sufficient input in the proposed route to the target; it is not a proof of the target.'},
    {'from_key': 'adaptive-moments', 'to_key': 'remaining-gap', 'kind': 'semantic_association', 'rationale': 'The bounded-horizon adaptive estimate identifies why the passage to full regeneration integrability is still missing.'},
    {'from_key': 'radius-tail', 'to_key': 'exit-moments', 'kind': 'depends_on', 'rationale': 'The fixed-box exit tail bound controls the time tail on the event of bounded path radius.'},
    {'from_key': 'radius-tail', 'to_key': 'remaining-gap', 'kind': 'semantic_association', 'rationale': 'This is a proved conditional route to the missing duration mean; its radius premise is unproved from the target.'},
    {'from_key': 'remaining-gap', 'to_existing_logical': 'math:probability.randomenvironment:open-problem-c0041-transience-in-a-direction-implies-ballisticity-for-uniformly-elliptic', 'kind': 'semantic_association', 'rationale': 'The existing dated C0041 card states exactly the UE iid directional-transience question; this draft records the still-unproved cycle-duration input for that same target.'},
]
bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w444', 'bundle_slug': 'probability-c0041-inward-traps-w444-20261010', 'entries': entries, 'relations': relations}
write_json(ROOT / 'bundle_001.json', bundle)
write_json(ROOT / 'AUTHOR_MODEL_EVIDENCE.json', {
    'author_agent': 'w444', 'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max',
    'requested_service_tier': 'Fast', 'served_model': 'UNKNOWN',
    'response_side_served_model_evidence': None,
    'explanation': 'No response-side served-model metadata is exposed to this worker. Requested settings and turn_context are not treated as served-model evidence.',
    'referee_agent': 'w446', 'referee_response_side_evidence': 'PENDING',
    'different_model_review_gate': 'NOT_ESTABLISHED',
})

hook = {
    'id': 'math-w444-01', 'area': 'math', 'event': 'PostToolUse',
    'cue': 'A scope/readme announcement or placeholder comparator is being used as a formal proof receipt',
    'fire_when': 'A claim says the theorem is formalized, but the inspected comparator theorem ends in sorry and the actual compiled proof/axioms have not been identified.',
    'silent_when': 'An actual theorem receipt names the exact assumptions, checked proof source and trusted axioms; or only a mathematical statement is being recovered.',
    'text': 'Before calling a theorem formally proved, identify the actual compiled theorem, assumptions and trusted axioms. A comparator ending in sorry gives no proof receipt; it also does not refute a separate proof.',
    'evidence': 'perceptron_proof_open_gaps_fleet_2026_07_12; https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/DirectionalBallisticity.lean lines 87-88 as read 2026-10-10',
    'proposer': 'w444',
}
(ROOT / 'math-w444.jsonl').write_text(json.dumps(hook, ensure_ascii=False) + '\n', encoding='utf-8')

INBOX.mkdir(parents=True, exist_ok=True)
destination = INBOX / 'bundle_001.json'
if destination.exists():
    previous = json.loads(destination.read_text(encoding='utf-8'))
    assert previous['author_agent'] == 'w444' and all(e['kind'] == 'concept' for e in previous['entries'])
    if previous != bundle:
        assert json.loads((ROOT / 'SUBMISSION_STATUS.json').read_text(encoding='utf-8'))['reviewed'] is False
        part = INBOX / 'bundle_001.part'
        write_json(part, bundle)
        part.replace(destination)
else:
    part = INBOX / 'bundle_001.part'
    write_json(part, bundle)
    part.rename(destination)

write_json(ROOT / 'SUBMISSION_STATUS.json', {
    'prepared': True, 'submitted': True, 'reviewed': False, 'ingested': False,
    'retrievable': False, 'draft_path': str(destination), 'promotion': 'NONE; all entries are concepts',
    'new_mathematical_claims': 'Five conditional or special-case hand proofs awaiting w446 review',
    'parent_problem_solved': False,
})
print(json.dumps({'claim_rows': len([line for line in claims_path.read_text(encoding='utf-8').splitlines() if line.strip()]),
                  'draft_entries': len(entries), 'relations': len(relations), 'draft_path': str(destination),
                  'mathematical_review': 'PENDING', 'store_writes': 0}))
