# write_records.py - builds CLAIMS.json, PROGRESS.json, PACKET_DELTA.json and .final for this run.
import json, hashlib, os, sys
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
RUN = '20261011T225000Z-claude-B09-sharp-uniform-endpoint-tax'
stmt = ("Let 0<p<=1/2 (relabel X for p>1/2), theta=arcsin sqrt(p), k(d)=h2(sin^2 d). For every {-1,1}-valued f on any finite "
        "product space with interior biases, revealing one coordinate X with P(X=1)=p, with M=H(S_A|S_B), J=I(Z;T) the two terms "
        "of the B09 identity L_A=M_A+J_A (bits): (i) J-M <= tau*(p) := h2(p)-m(p), m(p)=min_{0<=d<=theta}[k(d)+k(theta-d)]; "
        "(ii) for p<=p0=sin^2(d0)=0.0832217..., d0=0.2926408... the root of cos(2d)ln cot d=1, m(p)=2h2((1-sqrt(1-p))/2) and the "
        "two-bit AND 1-2XY with P(Y=1)=q*=1/(2(1+sqrt(1-p))) has J-M=(1-4pq*(1-q*))tau*(p)>=(1-p)tau*(p); "
        "(iii) for 0<p<=e^-3, tau*(p)<=(p/2)log2(1/p)+(log2 e-1)p, and tau*(p)=(p/2)log2(1/p)-(1-log2(e)/2)p+O(p^2 log(1/p)). "
        "Hence the optimal coefficient of p log2(1/p) in a dimension-free one-bit tax is exactly 1/2.")
proof = ("Step 1: f^(T)=(1-p)g^+p h^, f^(T+X)=sqrt(p(1-p))(h^-g^), q_T=(1-p)g^2+p h^2, sum q_T=1 (Boolean children have unit norm); "
         "a_T=(sqrt(1-p)g^,sqrt(p)h^)/sqrt(q_T)=(cos phi_T,sin phi_T); P(Z=1|T)=sin^2 phi_T and, with U the rotation by theta, "
         "P(X in S|S_B=T)=sin^2(phi_T-theta); so J-M=h2(p)-sum_T q_T[h2(sin^2 phi_T)+h2(sin^2(phi_T-theta))]. "
         "Step 2: h2(sin^2 phi)=k(dist(phi,(pi/2)Z)), k increasing on [0,pi/4]; d1+d2>=theta (same nearest lattice point: triangle "
         "inequality; different: >=pi/2-theta>=theta); lowering to d1'+d2'=theta lowers both terms; phi=d in [0,theta] attains; gives (i). "
         "Step 3: k''(d)=(4/ln2)(cos2d ln cot d-1), the bracket strictly decreasing, zero at d0; for theta<=d0 k is convex on [0,theta], "
         "so the symmetric convex function k(d)+k(theta-d) is minimal at theta/2. Step 4: AND fibers T={} with (1,1-2q), mass 1-4pq(1-q), "
         "and T={Y} with angle -pi/2 and bracket h2(p); at q* tan phi_{}=tan(theta/2); (1) gives J-M=q_{} tau*. Step 5: u_i=sin d_i, "
         "u1+u2>=sqrt(p); if some u_i>=sqrt(p): bracket>=h2(p)>=(p/2)log2(1/p)+p (p<=1/4); if both<sqrt(p)<=e^-3/2: h2(x)>=x log2(1/x), "
         "Psi(u)=u^2 log2(1/u^2) convex (u<=e^-3/2) and increasing (u<=e^-1/2), Jensen gives >=2Psi(sqrt(p)/2)=(p/2)log2(1/p)+p; "
         "h2(p)<=p log2(1/p)+p log2 e. Expanding h2(p)-2h2(p/4+p^2/16+O(p^3)) gives the second-order term.")
claim = dict(
    claim_id='B09-CLAUDE-SHARP-ONE-BIT-TAX', version=1, exact_statement=stmt,
    hypotheses=['f takes values in {-1,1}', 'finitely many independent coordinates with interior biases',
                'one revealed coordinate at a time (no multi-bit block claim)', 'entropies in bits'],
    statement_sha256=hashlib.sha256(stmt.encode('utf-8')).hexdigest(),
    contributors=['Claude B09 lead (proof, Steps 1-5)', 'A041 (AND lower bound, coefficient 1/2 at q=1/4)',
                  'A047/B10 (fixed-child coefficient 1/2; named the missing finite-p line)', 'earlier B09 run (identity L=M+J)'],
    proof_source='Run ' + RUN + ': this field and the run StructuredOutput (REPORT.md write was refused by the subagent harness). ' + proof,
    proof_dependencies=['B09 identity L_A=M_A+J_A and its definitions (runs/B09/20261011T195500Z-account01-B09-biased-restriction-uncertainty, interval-repaired)',
                        'orthonormal product-biased Fourier analysis', 'elementary calculus'],
    review_records=[dict(reviewer='A045',
                         record='A045-BIASED-REALIZABILITY-REFEREE v1 (run 20261011T225924Z-account05-A045-biased-realizability-referee)',
                         verdict='holds at scope for (i) and the e^-3 envelope in (iii), reconstructed from STREAM_NOTES v1; (ii), Step 3 and the second-order term were added later and are unreviewed',
                         independent='scoped referee inside B09, not the designated independent reviewer (A091)')],
    status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW', supersedes=[],
    refutes=['any dimension-free one-bit tax with coefficient below 1/2 or of order O(p) (with the A041 AND)'],
    first_unproved_line=None,
    next_consumers=['A091', 'A090', 'A041', 'A042', 'A043', 'A044', 'A045', 'A047', 'B20'])
reviews = [
    dict(target='A041-BOOLEAN-ONE-BIT-ENDPOINT-TAX-LOWER-BOUND', version=1, verdict='HOLDS',
         basis='independent analytic re-derivation: J-M=2h2(pv)-H(P)-p h2(v)=4q(1-2q) p log2(1/p)+O(p), maximal 1/2 at q=1/4; 60-digit check A3 (coefficient 0.49536 at p=2^-60, remainder/p -> -0.278652)'),
    dict(target='A041-BIASED-WEIGHT-BAND-MULTISCALE-RANK', version=1,
         verdict='PARTIAL: singleton lemma re-derived (holds); refresh inequality numerical evidence only (1836 checks, 0 violations); rank/tail/prior proof NOT reviewed',
         basis='code/check_tax.py part C; hand derivation sum_i P({i}) ln(v_i/P({i})) = 2 sum_i v_i rho_i^2 ln(1/rho_i) <= 4 Delta'),
    dict(target='A043-DISJOINT-PRIME-ENDPOINT', version=1,
         verdict='PARTIAL: composition identity holds (hand derivation from the factorised spectral law plus 6 unequal-bias compositions, error <= 8.9e-16); census and decomposition termination NOT reviewed',
         basis='code/check_tax.py part B'),
]
json.dump(dict(protocol_revision='2026-10-11-execution-v2', run_id=RUN, stream='B09', claims=[claim], review_records_issued=reviews),
          open('CLAIMS.json', 'w', encoding='utf-8'), indent=1)
prog = dict(
    protocol_revision='2026-10-11-execution-v2', run_id=RUN, stream='B09', packet_id='A041', gap_id='G-BIASED-LTF',
    attempt_id='B09-LEAD-SHARP-ONE-BIT-TAX-01',
    method='fiber rotation identity, one-dimensional reduction, convexity of h2(sin^2 d), Jensen; exhaustive and 60-digit checks',
    mathematical_delta=('Proved the sharp dimension-free one-bit endpoint tax J-M<=tau*(p)=h2(p)-m(p), attained up to (1-p) by an AND at q*(p) '
                        'for p<=0.0832; tau*=(p/2)log2(1/p)-(1-log2(e)/2)p+O(p^2 log), explicit envelope (p/2)log2(1/p)+(log2 e-1)p for p<=e^-3. '
                        'Closes the A041 endpoint gap [1/2,1] and the A047 first unsupported line; halves the Maassen-Uffink tax in L<=2M+tax.'),
    deliverable_status='COMPLETE_LOCAL_REVIEW_PENDING; REPORT.md BLOCKED (subagent harness refused report-file writes; content in StructuredOutput)',
    mathematical_status='ONE_BIT_TAX_SOLVED_UP_TO_FACTOR_1_MINUS_P; WEIGHTED_FEIPLUS_AND_FULL_FEI_OPEN',
    claim_versions_used=[dict(claim_id='A041-BOOLEAN-ONE-BIT-ENDPOINT-TAX-LOWER-BOUND', version=1, use='lower bound, re-derived'),
                         dict(claim_id='A043-DISJOINT-PRIME-ENDPOINT', version=1, use='composition identity checked'),
                         dict(claim_id='A045-BIASED-REALIZABILITY-REFEREE', version=1, use='review record')],
    claims_created_or_changed=[dict(claim_id='B09-CLAUDE-SHARP-ONE-BIT-TAX', version=1)],
    source_artifacts=['CLAIMS.json', 'code/check_tax.py', 'code/FROZEN_SPEC.json', 'code/write_records.py', 'out/check_tax_output.json'],
    next_consumers=['A091', 'A090', 'A041', 'A042', 'A043', 'A044', 'A045', 'B20'],
    next_action=('Reveal the inputs of a prime gate one at a time at induced biases and test sum_i tau*(eta_i) <= K delta_eta(g) uniformly in arity '
                 'on A044 address gates and symmetric thresholds (exact small cases first); A091 reviews Steps 1-5.'),
    stagnant_substantive_attempts=0,
    blockers=['REPORT.md write refused by the subagent harness ("Subagents should return findings as text, not write report files"); coordinator to materialise it from the StructuredOutput',
              'Full FEI open; charging the taxes and M to the biased deficit on primes is unproved'],
    code_sha256='1a71f98c0dbc2c357eb42374c1eab588db446f9c9ba107e439c5a7faaf4bc50b',
    output_sha256='e83b32b0ece94f275cc8c443219f1984a26ce6d2416425c797e556135b2a295d',
    packet_ids=['A041'])
json.dump(prog, open('PROGRESS.json', 'w', encoding='utf-8'), indent=1)
json.dump(prog, open('PACKET_DELTA.json', 'w', encoding='utf-8'), indent=1)
open('.final', 'w').close()
print('written', claim['statement_sha256'])
