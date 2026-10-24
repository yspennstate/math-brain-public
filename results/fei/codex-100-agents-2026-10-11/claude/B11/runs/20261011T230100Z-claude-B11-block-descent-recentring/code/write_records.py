import json, hashlib, sys, os
RD = sys.argv[1]; RUN = os.path.basename(RD)
def sha(st, hy): return hashlib.sha256(json.dumps({"statement": st, "hypotheses": hy}, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()
C = []
def claim(cid, st, hy, status, src, deps, first, consumers, refutes=None):
    C.append(dict(claim_id=cid, version=1, exact_statement=st, hypotheses=hy, statement_sha256=sha(st, hy),
                  contributors=["claude-B11"], proof_source=src, proof_dependencies=deps,
                  review_records=[], status=status, supersedes=[], refutes=refutes or [],
                  first_unproved_line=first, next_consumers=consumers))
claim("CLAUDE-B11-R1",
 "For every block A and every map e from subsets of C=[n]\A to subsets of A: (ln 2) J_A <= 2 E|S_A symdiff e(S_C)|, J_A = I(X;Y) in bits. With e the conditional majority, (ln 2) J_A <= 2 beta_A where beta_A = sum_{i in A} E min(p_i(S_C), 1-p_i(S_C)), p_i(T) = P(i in S | S_C = T); and 2 beta_A <= sum_{i in A} H(Z_i | S_C).",
 "f:{-1,1}^n->{-1,1}, n>=1, A nonempty subset of [n], S ~ fhat^2, X uniform on {-1,1}^A, Y|X=a ~ (f_a)hat^2, entropies in bits",
 "PROVED", "REPORT.md section 3 (fibrewise Gross log-Sobolev Ent(g^2) <= 2 sum|U| ghat(U)^2 applied to chi_{e(T)} w_T)",
 ["Gross log-Sobolev inequality on the uniform cube (natural log)", "C006 block identity"], None, ["A052", "A051", "C019"])
claim("CLAUDE-B11-R2",
 "If f is a dimension-critical C-witness then for every nonempty proper block A: C I_A + D_C(f) <= H(Z_A|Z_C) + (2/ln2) beta_A. For a singleton i: C Inf_i + D_C(f) <= H(Z_i|Z_-i) + (2/ln2) beta_i, where beta_i is the Bayes error of predicting Z_i from Z_-i, beta_i <= min(Inf_i, 1-Inf_i, eps_u for every u containing i, H(Z_i|Z_-i)/2); hence H(Z_i|Z_-i) >= (C Inf_i + D_C(f))/(1+1/ln2) > 0, so no coordinate's spectral membership is a function of the rest of the spectral sample. This implies A052's rank-one bound C Inf_i + D_C <= h2(eps_u) + (2/ln2) eps_u.",
 "D_C(f) = H(f) - C I(f) > 0 and H(g) <= C I(g) for every Boolean g on fewer than n coordinates; eps_u = (1-|E f(x)f(x xor u)|)/2",
 "PROVED", "REPORT.md section 3", ["CLAUDE-B11-R1", "A051 block inequality (3.1)"], None, ["A052", "A055"])
claim("CLAUDE-B11-R3",
 "Let phi(f) = min over nonempty proper blocks A with I_A>0 of L_A/I_A and K_desc(n) = max over nonconstant f on n bits of phi(f). Then K_desc(2)=4, K_desc(3)=4.433834373377398591729..., K_desc(4)=4.536634068264783227945..., and M_n = max H/I equals 2, 2.955889582251599061152..., 3.402475551198587420958...; for n=2,3,4 both maxima are attained exactly at the 2^(n+1) point defects. Runner-up values at n=4: phi 3.13158, H/I 2.95589.",
 "n in {2,3,4}; all 2^(2^n) tables; bits",
 "CERTIFIED", "out/exhaustive_n2_4.json, out/certify_n2_4.json; exhaustive float64 scan in which weights and influences are exact dyadic rationals and the only inexact operation is log2 (gaps 1.40 and 0.45 exceed any log2 error by >10^9); point-defect values by mpmath interval arithmetic at 120 bits from closed forms",
 [], None, ["A051", "A055"])
claim("CLAUDE-B11-R4",
 "Steepest-ascent search (n=5: 2308 climbs per objective; n=6: 340 and 401 climbs) found no function beating the point defect for either phi or H/I: n=5 phi=4.508799793716, H/I=3.623740399702; n=6 phi=4.319882108878, H/I=3.739764017898. For point defects phi(pd_n) decreases to 4 for n>=5 (4.0032 at n=14) while H/I increases to 4.",
 "n in {5,6}; frozen search spec in code/descent_search.py; float64",
 "EVIDENCE", "out/search_n5_n6.json, out/search_n5_n6.log", [], "Exhaustive or symmetry-reduced certification of K_desc(5).", ["A051"])
claim("CLAUDE-B11-R5",
 "For every n>=2: M_n <= max(M_{n-1}, K_desc(n)); hence M_n <= max_{2<=m<=n} K_desc(m) and C_* = lim M_n <= sup_n K_desc(n). If K_desc(n) <= K for every n then FEI holds with constant K.",
 "M_1 = 0; D_K(f) = (L_A - K I_A) + E_a D_K(f_a) for every proper block (C006 + influence identity)",
 "PROVED", "REPORT.md section 3", ["C006 block identity"], None, ["A051", "C019", "C000"])
claim("CLAUDE-B11-R6",
 "For nonconstant g, h on disjoint coordinate sets, phi(g (x) h) <= min(phi(g), phi(h), H(g)/I(g), H(h)/I(h)) <= H(g (x) h)/I(g (x) h). A tensor product is never a block-descent obstruction at its own ratio.",
 "g, h Boolean, nonconstant, disjoint coordinates",
 "PROVED", "REPORT.md section 3; numerical check out/nine_bit_and_tensor.json (pd3 x pd2: phi = 2.0 = min)", [], None, ["A053", "A055"])
json.dump(C, open(os.path.join(RD, 'CLAIMS.json'), 'w'), indent=1)
prog = dict(protocol_revision="2026-10-11-execution-v2", run_id=RUN, stream="B11", packet_id="A052", gap_id="C019",
  attempt_id=RUN + "-1", method="proof (fibrewise log-Sobolev, descent induction, tensor lemma) + exhaustive n<=4 scan with interval certification + frozen-spec local search n=5,6",
  mathematical_delta="Recentred channel bound (ln2)J_A <= 2 beta_A for every recentring, optimal = conditional majority; critical sources are coordinatewise spectrally unpredictable; one-step block descent is an exact sufficient route (M_n <= max_m K_desc(m)); K_desc = 4, 4.4338, 4.5366 (n=2,3,4 certified, point defects), 4.5088 (n=5 evidence); tensor products never obstruct descent.",
  deliverable_status="complete", mathematical_status="partial: FEI open; one-step descent constant bounded? open",
  claim_versions_used=["C006@registry", "C005@registry", "A051 (3.1) run 20261011T214321Z", "A052 affine-syndrome run 20261011T220243Z"],
  claims_created_or_changed=[c['claim_id'] for c in C], source_artifacts=["REPORT.md", "CLAIMS.json", "code/", "out/"],
  next_consumers=["A051", "A052", "A053", "A054", "A055", "A090", "A094"],
  next_action="Compute phi exactly on iterated point-defect compositions (FEI lower-bound family) at n=6..9 by orbit reduction; decide whether phi/ratio stays bounded.",
  stagnant_substantive_attempts=0, blockers=[], packet_ids=["A052"])
json.dump(prog, open(os.path.join(RD, 'PROGRESS.json'), 'w'), indent=1)
json.dump(prog, open(os.path.join(RD, 'PACKET_DELTA.json'), 'w'), indent=1)
print([ (c['claim_id'], c['status'], c['statement_sha256'][:12]) for c in C])
