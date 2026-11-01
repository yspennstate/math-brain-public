# Writes CLAIMS.json, PROGRESS.json and PACKET_DELTA.json for this run with protocol hashes.
import hashlib, json, os, sys
RUN = sys.argv[1]
RUN_ID = os.path.basename(RUN.rstrip('/'))
SRC = 'B06 lead StructuredOutput for run ' + RUN_ID + ' (REPORT.md save refused by the subagent harness; text returned to coordinator claude-2d8060eb)'


def sha(statement, hyps):
    return hashlib.sha256(json.dumps({'statement': statement, 'hypotheses': hyps}, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()


claims = []


def add(cid, statement, hyps, deps, status, src, first_unproved=None, consumers=None):
    claims.append({'claim_id': cid, 'version': 1, 'exact_statement': statement, 'hypotheses': hyps,
                   'statement_sha256': sha(statement, hyps), 'contributors': ['claude-B06-lead'], 'proof_source': src,
                   'proof_dependencies': deps, 'review_records': [], 'status': status, 'supersedes': [], 'refutes': [],
                   'first_unproved_line': first_unproved, 'next_consumers': consumers or ['A087', 'A094', 'B20']})


H_BOOL = ['f: {-1,1}^n -> {-1,1} under the uniform measure; S has law Pr[S=T]=fhat(T)^2; S_i=1[i in S]; entropies in bits',
          'B_i=H(S_i|S_{-i}); Inf_i=Pr[f(x)!=f(x^i)]; I=sum_i Inf_i; I_A=sum_{i in A} Inf_i; Delta_i H=H(f)-avg_b H(f_{i=b})']
add('B06-LEAD-R1-BLOCK-TO-SINGLETON',
    'For every probability law on subsets of [n] and every A subset of [n], H(S_A|S_{A^c}) >= sum_{i in A} H(S_i|S_{-i}). '
    'Consequently, for Boolean f with I_A(f)>0 and K>=0: if H(S_A|S_{A^c}) <= K I_A(f) then some i in A with Inf_i(f)>0 has '
    'B_i(f) <= K Inf_i(f); and if Delta_A H(f)=H(f)-E_X H(f_X) <= K I_A(f) then some i in A with Inf_i(f)>0 has '
    'Delta_i H(f) <= (K+2/ln 2) Inf_i(f).',
    H_BOOL + ['C005: Delta_i H=B_i+JS_i with JS_i <= (2/ln 2) min(Inf_i,1-Inf_i)', 'C006: Delta_A H=H(S_A|S_{A^c})+I(X;Y)'],
    ['C005', 'C006'], 'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW', SRC + ', section R1', None, ['A026', 'A027', 'A028', 'A087', 'B20'])
add('B06-LEAD-R2-LEAF-PARTITION-INVARIANCE',
    'For every Boolean f on n uniform bits and every adaptive decision tree T (internal node v of weight w_v=2^{-depth(v)}, restriction '
    'f_v, queried coordinate i_v free at v; leaves rho of weight w_rho): sum_v w_v Delta_{i_v}H(f_v) = H(f)-sum_rho w_rho H(f_rho) =: Pi_H; '
    'sum_v w_v Inf_{i_v}(f_v) = I(f)-sum_rho w_rho I(f_rho) =: Pi_I = E_x #{v on the root-leaf path of x : f(x)!=f(x^{i_v})}; and for every '
    'real K, K I(f)-H(f) = sum_rho w_rho (K I(f_rho)-H(f_rho)) + K Pi_I - Pi_H. Hence for every complete tree sum_v w_v B_{i_v}(f_v) >= '
    'H(f)-(2/ln 2) I(f), and if every leaf satisfies H <= C_T I and Pi_H <= K Pi_I then H(f) <= max(K,C_T) I(f).',
    H_BOOL + ['C005 entropy-decrement identity and influence identity I=Inf_i+avg_b I(f_{i=b})'],
    ['C005'], 'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW', SRC + ', section R2', None, ['A028', 'A029', 'A064', 'A087', 'A094', 'B20'])
add('B06-LEAD-R3-RESTRICTION-CLOSED-EQUIVALENCE',
    '(a) Every Boolean f satisfies sum_i B_i(f) <= H(f); hence H(f) <= C I(f) implies a coordinate i with Inf_i(f)>0 and '
    'B_i(f) <= C Inf_i(f). (b) If a class of Boolean functions is closed under fixing coordinates and every nonconstant member has a '
    'coordinate i with Inf_i>0 and B_i <= K Inf_i, then every member satisfies H <= (K+2/ln 2) I. (c) If the nonzero Fourier support '
    'of f lies in an affine subspace of F_2^n of dimension d, then H(f) <= d and, for nonconstant f, I(f) >= 4^{1-d}; hence every '
    'nonconstant function of affine Fourier dimension at most 4, and every disjoint product of such functions, satisfies H <= 256 I.',
    H_BOOL + ['C005', 'disjoint products: H and I are additive over disjoint variable sets'],
    ['C005'], 'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW', SRC + ', section R3', None, ['A026', 'B20', 'A094'])
add('B06-LEAD-SMALLN-TRUE-ERASURE-CONSTANTS',
    'Let kappa_n = max over nonconstant Boolean f on n uniform bits of min over i with Inf_i(f)>0 of B_i(f)/Inf_i(f). Then kappa_1=0, '
    'kappa_2=2, kappa_3=(5/2) h2(1/10)+3/2=2.67248898397..., attained exactly by the three-variable functions with one or seven values '
    '-1 (point defects and their negations; every other spectrum class is strictly below by the exact screen); kappa_4 = kappa_3 exactly, attained exactly by three-variable point defects and their negations with one dummy variable; every '
    'other four-variable class has min_i B_i/Inf_i < 267/100 (the next largest is the four-variable point defect, 2.63400339...). The amplitude proxy max_f min_i A_i/Inf_i, A_i=2 sum_T |fhat(T) fhat(T+i)|, equals '
    '0, 2, 3, 7/2 for n=1..4, and max_f sum_i B_i / I at n=4 lies in [2.7041532056284, 2.7041532056305].',
    ['exhaustive enumeration of all 2^(2^n) truth tables for n<=4 with integer Walsh sums',
     'certified by mpmath interval logarithms (40 digits, outward margin 1e-12) on the maximiser and on every class not excluded by '
     'the exact rational screen min_i A_i/Inf_i <= certified lower bound (valid since B_i <= A_i)',
     'strict n=4 separation: code/kappa4_strict.py, 2255 classes below 267/100 by the exact proxy, 1 by interval, 4 dummy extensions'],
    [], 'CERTIFIED_FINITE_COMPUTATION_PENDING_INDEPENDENT_REVIEW', 'code/b06_checks.py; out/b06_checks.json; ' + SRC + ', section R4',
    None,
    ['A026', 'A029', 'B15', 'B17', 'A092'])
reviews = [
    {'target_claim': 'A026-AFFINE4-GOOD-COORDINATE', 'version': 1, 'verdict': 'LOGIC_CHECKED_FINITE_PART_REPRODUCED',
     'evidence': 'own integer census, all 65536 four-variable tables (2261 distinct spectra): proxy maxima 0,2,3,7/2; leverage limited by R3(c)'},
    {'target_claim': 'A026-AMPLITUDE-K4-THRESHOLD-NOGO', 'version': 1, 'verdict': 'REPRODUCED_EXACTLY',
     'evidence': 'Fraction Krawtchouk sums: ratio 2220940451/536870912; true B_i/Inf_i=1.8154 (float), so proxy-only'},
    {'target_claim': 'A027-CORE-BLOCK-HARDNESS', 'version': 1, 'verdict': 'IDENTITY_REDERIVED_AND_REPRODUCED',
     'evidence': 'own Fourier derivation; 828 cores m,r in {1,2,3}, both mean signs, max error 6.66e-16 (R0=0 as zero mass)'},
    {'target_claim': 'A027-DATA-FIRST-PROPER-BLOCK', 'version': 1, 'verdict': 'BOUND_AND_INFLUENCES_REPRODUCED_SCOPE_NOTE',
     'evidence': 'B_W <= p(2dm+2) on all 828 cases (max ratio 0.708); I_W=pI(u), terminal rpd exact; I(u)>=eta m makes the core FEI with 1/eta'},
]
with open(os.path.join(RUN, 'CLAIMS.json'), 'w', encoding='utf-8') as fh:
    json.dump({'protocol_revision': '2026-10-11-execution-v2', 'run_id': RUN_ID, 'stream': 'B06', 'claims': claims,
               'review_records_of_other_claims': reviews}, fh, indent=1)
progress = {
    'protocol_revision': '2026-10-11-execution-v2', 'run_id': RUN_ID, 'stream': 'B06', 'packet_id': 'A027', 'gap_id': 'G-R-SELECT',
    'attempt_id': RUN_ID + '-1', 'method': 'proof (chain rule, telescoping) plus exhaustive exact census with interval certification',
    'mathematical_delta': 'R1 block->singleton at the same node (rate K -> K+2/ln2); R2 every restriction-tree payment is a function of the '
                          'leaf partition, Pi_I = expected queried pivotal count, complete trees have cumulative erasure >= H-(2/ln2)I; '
                          'R3 good-coordinate selection on restriction-closed classes = FEI on the class, A026 class already has H<=256I; '
                          'R4 kappa_3=kappa_4=(5/2)h2(1/10)+3/2=2.6725 exactly (point defect on 3 bits, dummy for n=4), proxy maxima 0,2,3,7/2.',
    'deliverable_status': 'LOCAL_JSON_SAVED_REPORT_MD_BLOCKED',
    'mathematical_status': 'REDUCTIONS_PROVED_LOCALLY; SMALL_N_CERTIFIED; UNIVERSAL_G-R-SELECT_OPEN; FULL_FEI_OPEN',
    'claim_versions_used': ['C005 v-current', 'C006 v-current', 'A026-AFFINE4-GOOD-COORDINATE v1', 'A026-AMPLITUDE-K4-THRESHOLD-NOGO v1',
                            'A027-CORE-BLOCK-HARDNESS v1', 'A027-DATA-FIRST-PROPER-BLOCK v1'],
    'claims_created_or_changed': [c['claim_id'] + ' v1' for c in claims],
    'source_artifacts': ['code/b06_checks.py', 'code/kappa4_exact.py', 'code/kappa4_strict.py', 'code/make_claims.py', 'out/b06_checks.json', 'out/b06_checks.stdout.txt', 'out/kappa4_exact.json', 'out/kappa4_strict.json'],
    'next_consumers': ['A027', 'A028', 'A029', 'A030', 'A064', 'A087', 'A094', 'B20'],
    'next_action': 'Prove Pi_H <= K Pi_I (R2 root inequality) for low-density activated cores when a proper subset of the core is revealed '
                   'before the controls, with point-defect and C001-regular terminals, or give the parameterized family where every such '
                   'partition fails; reviewer A087.',
    'stagnant_substantive_attempts': 0,
    'blockers': ['REPORT.md not saved: the subagent harness refused report-file writes ("Subagents should return findings as text"); '
                 'the full report is in this run\'s StructuredOutput to coordinator claude-2d8060eb. .final is withheld until REPORT.md exists.'],
    'packet_ids': ['A027'],
}
for name in ('PROGRESS.json', 'PACKET_DELTA.json'):
    with open(os.path.join(RUN, name), 'w', encoding='utf-8') as fh:
        json.dump(progress, fh, indent=1)
print('wrote', [c['claim_id'] for c in claims])
for c in claims:
    print(c['claim_id'], c['statement_sha256'])
