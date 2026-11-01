"""Prepare a local draft from the saved mathematical packet; never ingest a store."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def dump(name, value):
    (ROOT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


rows = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
claims = {r['id'].rsplit('-', 1)[-1]: r for r in rows}
attempt = (ROOT / 'ATTEMPT.md').read_text(encoding='utf-8')
sections = re.split(r'(?m)^## ', attempt)[1:]


def proof(label):
    return next(s for s in sections if re.search(r'\b' + label + r'\b', s.splitlines()[0]))


nn = 'Let E={+/-e_i:1<=i<=d}. The environment omega has probability rows omega(x,e), e in E, on Z^d, is sampled once, and the quenched walk has X_0=0 and transition P_omega(X_{n+1}=x+e|X_n=x)=omega(x,e). '
qdef = 'For fixed nonzero l in R^d put A_l={lim_n X_n dot l=+infinity}, q_l(omega)=P_omega^0(A_l), theta_x omega(y,e)=omega(x+y,e), and Kg(omega)=sum_e omega(0,e)g(theta_e omega). '
statements = {
    'L1': nn + qdef + 'If the annealed union law P_0(A_l union A_-l) belongs to {0,1}, then the directional law P_0(A_l) in {0,1} is equivalent to excluding simultaneous positivity of P_0(A_l) and P_0(A_-l). Event disjointness by itself does not establish this exclusion.',
    'L2': nn + qdef + 'Suppose the environment law P is shift-ergodic and strictly elliptic, and there is a K-invariant probability Q equivalent to P. Then the annealed probability P_0(A_l) is zero or one.',
    'L3': nn + 'Suppose P is shift-invariant, shift-ergodic, and strictly elliptic. Let theta_x omega(y,e)=omega(x+y,e) and Kg=sum_e omega(0,e)g(theta_e omega). Every K-invariant probability Q absolutely continuous with respect to P is equivalent to P.',
    'L4': nn + 'Suppose P is shift-invariant, shift-ergodic, and strictly elliptic. Define f_n(omega)=sum_{x in Z^d}P_omega^x(X_n=0) and H_N=(1/N)sum_{n=0}^{N-1}f_n. If the family H_N is uniformly integrable in L1(P), then there is an absolutely continuous stationary probability for the environment viewed from the particle, and P_0(lim_n X_n dot l=+infinity) is zero or one for every fixed nonzero l in R^d.',
    'L5': nn + qdef + 'Suppose P is shift-invariant. Put f_n(omega)=sum_x P_omega^x(X_n=0), H_N=(1/N)sum_{n<N}f_n, and D_l(omega)=sum_e omega(0,e)[q_l(theta_e omega)-q_l(omega)]^2. Then sum_{n>=0} integral f_n D_l dP = integral q_l(1-q_l)dP, and integral H_N D_l dP <= 1/(4N) for every N>=1. This does not assert that integral D_l dP is zero.',
    'L6': nn + qdef + 'Suppose P has iid strictly elliptic rows. Set s(omega)=sum_e omega(-e,e) and D_l(omega)=sum_e omega(0,e)[q_l(theta_e omega)-q_l(omega)]^2. Then Cov_P(s,q_l^2)=integral D_l dP>=0, and P_0(A_l) in {0,1} is equivalent to Cov_P(s,q_l^2)=0.',
    'C1': 'For d=3, take iid Dirichlet rows with positive parameters (1/10,1/50,1/50,1/50,1/50,1/50) ordered (+e1,+e2,+e3,-e1,-e2,-e3). These rows are strictly elliptic but are not uniformly elliptic. Their trap exponent 2 sum_i alpha_i-max_{i<=3}(alpha_i+alpha_{i+3}) is 7/25. Sabot, arXiv:1007.2565v3, Theorem 1(ii), therefore rules out an absolutely continuous invariant probability for the environment viewed from the particle. Consequently the family H_N=(1/N)sum_{n<N}sum_x P_omega^x(X_n=0) is not uniformly integrable in L1(P). This refutes that blanket proof input, not the directional zero-one law.',
    'G1': 'UNPROVED INPUT IN THIS PACKET; current openness UNKNOWN because a recent primary manuscript claims a proof that this packet has not adjudicated. ' + nn + qdef + 'For iid strictly elliptic rows, d>=3, the remaining proposed input is Cov_P(sum_e omega(-e,e),q_l^2)=0. This is equivalent to the fixed-direction zero-one target by the proved covariance reduction. Independence of the rows does not make q_l independent of the incoming rows, because q_l depends on the whole environment.',
}
names = {
    'L1': ('rwre-opposite-escape-exclusion-reduction', 'Opposite-escape exclusion reduction'),
    'L2': ('rwre-stationary-equivalent-law-directional-zero-one', 'Stationary-law conditional directional zero-one proof'),
    'L3': ('rwre-absolutely-continuous-stationary-law-equivalence', 'Equivalence of an absolutely continuous stationary environment law'),
    'L4': ('rwre-cesaro-incoming-mass-uniform-integrability-criterion', 'Incoming-mass uniform-integrability criterion'),
    'L5': ('rwre-directional-harmonic-energy-mass-balance', 'Exact directional harmonic-energy mass balance'),
    'L6': ('rwre-directional-zero-one-flux-covariance-equivalence', 'Directional zero-one flux-covariance equivalence'),
    'C1': ('rwre-dirichlet-trap-obstruction-to-stationary-probability-route', 'Dirichlet trap obstruction to the stationary-probability route'),
    'G1': ('rwre-unproved-directional-flux-covariance-input', 'Unproved directional flux-covariance input'),
}
entries = [{
    'key': 'q-definition', 'namespace': 'probability.randomenvironment',
    'logical_name': 'rwre-quenched-directional-escape-harmonic-function',
    'kind': 'definition', 'title': 'Quenched directional escape harmonic function',
    'statement': nn + qdef, 'proof_text': None, 'assumptions': ['Nearest-neighbor probability rows on Z^d', 'fixed deterministic nonzero l'],
    'domain': 'probability theory',
    'source': {'source_id': 'owner-own-work:w576:C0044:q-definition', 'url': None, 'revision': '2026-10-10-local-author-draft', 'license': 'owner-own-work (author derivation; review pending; no novelty claim)', 'excerpt': None},
}]
for label, (logical, title) in names.items():
    r = claims[label]
    is_gap = label == 'G1'
    entries.append({
        'key': label.lower(), 'namespace': 'probability.randomenvironment', 'logical_name': logical,
        'kind': 'concept' if is_gap else 'lemma', 'title': title,
        'statement': ('AUTHOR PROOF OR SOURCE-BACKED DEDUCTION; INDEPENDENT REVIEW PENDING. ' if not is_gap else '') + statements[label],
        'proof_text': None if is_gap else proof(label), 'assumptions': r['assumptions'], 'domain': 'probability theory',
        'source': {'source_id': 'owner-own-work:w576:C0044:' + label, 'url': r['source'].get('url'), 'revision': '2026-10-10-local-author-draft', 'license': 'owner-own-work (author derivation; source attributed; review pending; no novelty claim)', 'excerpt': None},
    })
relations = [
    {'from_key': 'l2', 'to_key': 'q-definition', 'kind': 'depends_on', 'rationale': 'The conditional proof applies stationarity to the actual quenched escape harmonic function q_l.'},
    {'from_key': 'l3', 'to_key': 'q-definition', 'kind': 'semantic_association', 'rationale': 'Both use the shift convention theta_x omega(y,e)=omega(x+y,e) and environment kernel K.'},
    {'from_key': 'l4', 'to_key': 'l2', 'kind': 'depends_on', 'rationale': 'After constructing an invariant law, the stationary-law conditional proof gives the directional zero-one conclusion.'},
    {'from_key': 'l4', 'to_key': 'l3', 'kind': 'depends_on', 'rationale': 'The constructed law is absolutely continuous; the support argument proves its equivalence to P.'},
    {'from_key': 'l5', 'to_key': 'q-definition', 'kind': 'depends_on', 'rationale': 'Kq_l=q_l and the quenched escape-indicator martingale produce the energy identity.'},
    {'from_key': 'l6', 'to_key': 'l5', 'kind': 'depends_on', 'rationale': 'The harmonic-energy formula D_l=K(q_l^2)-q_l^2 becomes Cov_P(K*1,q_l^2).'},
    {'from_key': 'c1', 'to_key': 'l4', 'kind': 'depends_on', 'rationale': 'Nonexistence of an absolutely continuous invariant probability, by contraposition of the sufficient criterion, implies failure of uniform integrability. The counterexample does not refute L4.'},
    {'from_key': 'g1', 'to_key': 'l6', 'kind': 'depends_on', 'rationale': 'The unproved covariance input is precisely equivalent to the fixed-direction target.'},
    {'from_key': 'l1', 'to_key': 'g1', 'kind': 'semantic_association', 'rationale': 'Both identify the remaining one-sign directional question without claiming to solve it.'},
    {'from_key': 'g1', 'to_existing_logical': 'math:probability.randomenvironment:open-problem-c0044-zero-one-law-for-directional-transience-in-dimensions-d-3', 'kind': 'semantic_association', 'rationale': 'Existing card asks whether P_0(A_l) belongs to {0,1}; this draft asks whether Cov_P(sum_e omega(-e,e),q_l^2)=0. L6 proves equivalence. The 2026-09-07 open label is historical and current openness remains UNKNOWN.'},
]
dump('bundle_001.json', {'spec': 'mathbrain-draft-v1', 'author_agent': 'w576', 'bundle_slug': 'c0044-invariant-energy-author-draft-2026-10-10', 'entries': entries, 'relations': relations})
source = {
    'target_id': 'C0044', 'checked_at': '2026-10-10', 'current_openness': 'UNKNOWN',
    'exact_statement': nn + qdef + 'For iid strictly elliptic rows, d>=3, the target is P_0(A_l) in {0,1}.',
    'primary_statement_source': {'url': 'https://arxiv.org/pdf/1309.2589', 'locator': 'Drewitz-Ramirez, Open question 3.2, PDF page 42 (index 41)', 'assumptions': ['(E)', '(IID)'], 'verified': True},
    'recent_primary_claim': {'title': 'A directional zero-one law under strict ellipticity', 'date': '2026-09-23', 'url': 'https://raw.githubusercontent.com/openai/math/main/preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/paper.pdf', 'local_copy': str(ROOT / 'sources/strict_zero_one_2026.pdf'), 'locator': 'Theorem 1.1; statement and strategy only read', 'adjudicated': False, 'formal_receipt': 'NONE. The linked comparator DirectionalWalk.lean has by sorry at its target theorem; this is not a refutation of a separate implementation or manuscript.'},
    'counterexample_source': {'url': 'https://arxiv.org/pdf/1007.2565v3', 'locator': 'Sabot Theorem 1(ii), PDF page index 3', 'packet_trap_exponent': '7/25', 'refutes': 'Blanket stationary-probability / Cesaro-UI proof input', 'does_not_refute': 'C0044'},
    'prior_attempts': {'original': 'C0044-A001', 'superseding': 'C0044-A002', 'scoped_other_intakes': 'Exact problem_id/attempt_id rg search across all named intake directories returned only the original intake records', 'H_I_attempt_directories': 'No C0044-specific match in targeted searches', 'lean_prior_directory': 'Annotated ranking only; no target proof located'},
    'owner_solved_retired_check': {'status': 'PARTIAL, not a global certification', 'named_population_store': 'Read-only exact-title query returned three historical or unverified target cards', 'canonical_store': 'Scoped canonical-repository README/sqlite filename search did not expose a target store; verification unavailable; no retired/solved claim'},
    'served_model_evidence': {'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max', 'requested_tier': 'Fast', 'response_side_receipt_available': False, 'served_identity': 'UNKNOWN', 'note': 'Requested settings and self-report are not served-model evidence.'},
    'submission_state': 'not submitted', 'review_state': 'pending w578', 'different_model_review_gate': 'pending; served identities unverified', 'ingestion_state': 'not ingested', 'retrieval_state': 'not checked',
    'full_target_proved_in_this_packet': False, 'single_hardest_gap': 'G1: Cov_P(sum_e omega(-e,e),q_l^2)=0. Row independence does not give independence from the global escape function.',
    'handoff_receipts': {'statement_first_to_w577': 'msg-eb0797a19f', 'scope_to_w578': 'msg-5fdec58f53', 'lane_claim': 'clm-be7daca008'},
}
dump('SOURCE_STATUS.json', source)
print(json.dumps({'prepared_entries': len(entries), 'prepared_relations': len(relations), 'claim_rows': len(rows), 'full_target_proved': False}))
