"""Writes CLAIMS.json, PROGRESS.json and PACKET_DELTA.json (byte-identical to PROGRESS.json) for the B18 lead run.
statement_sha256 = SHA256 of the exact_statement UTF-8 text."""
import json, hashlib, os, sys
RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN_ID = os.path.basename(RUN)
def sha(s): return hashlib.sha256(s.encode('utf-8')).hexdigest()
KS = "Kstar=4+(5/2)log2(5)-(9/2)log2(3)=2.672488983973203"
claims_src = [
 ("B18-AFFINE-SUPPORT-JUNTA-REDUCTION", "PROVED",
  "Let f be a Boolean sign on a finite uniform cube whose nonzero Fourier support lies in c+V, dim_F2 V<=d. If e_i is not in V then B_i(f)=H(S_i|S_-i)=0. If every relevant i has e_i in V then f depends on at most d coordinates. The class of such f (support condition imposed per disjoint factor) is closed under coordinate restriction and disjoint products, and B_i, Inf_i are factor-local. Hence if every nonconstant Boolean function of at most d variables has a relevant i with B_i<=K Inf_i, every nonconstant member of the class has one, and H(f)<=(K+2/ln 2)I(f) for every member (C005 erasure induction).",
  ["Boolean sign", "uniform finite cube", "entropy in bits", "C005: Delta_i H=B_i+JS_i, JS_i<=(2/ln2)Inf_i"],
  "REPORT text Section 4.1 (returned in StructuredOutput; REPORT.md write refused by harness)", ["C005"],
  "none", ["B18 Codex A090", "C018 consumers", "A082", "A026"]),
 ("B18-N4-GOOD-COORDINATE-CERTIFICATE", "CERTIFIED",
  "Over all 65,536 Boolean sign tables on 4 uniform bits, the maximum over nonconstant f of min over relevant i of B_i/Inf_i equals " + KS + ", attained by exactly 64 tables (the 3-bit point defects: 4 variable triples x 8 positions x 2 signs, each verified exactly as the rational combination {2:4, 5:5/2, 3:-9/2} of log2 primes); the next largest value is 2.634003391 (4-bit point defect); no table exceeds Kstar+1e-8.",
  ["n=4 exhaustive", "float64 with error budget (all p_S in {0} or >=1/64) plus exact rational-log recheck of extremals", "bits"],
  "code/exhaust_n4.py, out/exhaust_n4.json", [], "none", ["A082", "A026", "C018"]),
 ("B18-N5-LEX-EXCEEDS-KSTAR", "CERTIFIED",
  "For f=-1 exactly when x_0+2x_1+4x_2+8x_3+16x_4<3 on 5 uniform bits, every relevant coordinate satisfies B_i/Inf_i>=16/3+(89/24)log2(89)-(169/24)log2(13)-(3/8)log2(3)=2.695887520153101 (attained at i=2,3,4; i=0,1 give 3.604845372685615), which exceeds Kstar by 0.0233985. The lexicographic threshold t=13 on 7 bits gives 2.697237222508217. Hence the optimal n<=4 good-coordinate constant Kstar is not a good-coordinate constant for all Boolean functions; this does not contradict A082-FINITE-TRUE-ERASURE or A082-AFFINE4-ERASURE-BRIDGE (f has five relevant coordinates).",
  ["exact rational Walsh coefficients", "log arguments factored into primes", "mpmath 40 digits", "bits"],
  "code/exact_lex5.py, out/exact_lex5.json; hand derivation REPORT Section 4.2", [], "none", ["C018 consumers", "A089", "A090"]),
 ("B18-A057-B-PART-RECONSTRUCTION", "PROVED",
  "For a disjoint composition F=g(h_1,...,h_m) with balanced Boolean h_j, g=a+y_j b, q=Inf_j(g), x=hhat_j({i})^2 (nats): B_i(F)=q B_i(h_j)+L_j(x) with L_j=sum_T(a_T^2+x b_T^2)h_nat(x b_T^2/(a_T^2+x b_T^2)); 0<=L_j<=x B_j(g)+q x ln(1/x) (termwise convexity of (1+t)ln(1+t)); and B(F)<=sum_j q_j B(h_j)+sum_j W_1(h_j)B_j(g)+(2/e)I(F), using |hhat({i})|<=Inf_i(h) for Boolean h.",
  ["balanced Boolean inner functions on disjoint uniform blocks", "nats"],
  "REPORT Section 4.3; code/check_a057.py, out/check_a057.json (3,216 cases)", [], "the D_i identity and 0<=J_j<=2qx of A057 were not re-derived", ["A057", "B05", "B19"]),
 ("B18-A087-LAMBDA-RECONSTRUCTION", "PROVED",
  "For balanced Boolean g and k fresh fair point controls, F=1+A_k(g-1), on the control-first tree the A061 one-sided charge at an active node with s controls left is lambda_s=u-u^2+u^2 log2((1-2u+2u^2)/u^2), u=2^-s; the reach-weighted sum is q(k+A_k) with A_k<=3, hence <=4kq; the queried cost is kq and terminal influence and entropy are qI(g), qH(g).",
  ["balanced Boolean core", "fresh fair controls", "bits"],
  "REPORT Section 4.4; code/checks2.py (exact agreement, cores dictator/Maj3/Mux3, s=1..4)", ["A061 charge definition"], "identification of lambda_s with A087's magnitude-mismatch KL residual not reconstructed", ["A087", "A090", "C019"]),
 ("B18-A096-FALSIFICATION-SEARCH", "EVIDENCE",
  "No violation of J_X-M_X<=h2(r)-h2(1-sqrt(1-r)) in 40,000 random cases (residual 1-3 bits, random Boolean children, random interior residual biases, p in (0.0005,0.9995) and 2^-1..2^-14); max(E-bound)=-3.054e-5. The expansion h2(r)-h2(delta)=(r/2)log2(1/r)+((log2 e-1)/2)r+O(r^2 log(1/r)) holds analytically.",
  ["float64", "random search, not a proof"], "code/checks2.py, out/checks2.json", [], "universal inequality of A096 unproved by B18", ["A090", "A096"]),
 ("B18-LEX-FAMILY-PLATEAU", "EVIDENCE",
  "On lexicographic thresholds f_t=-1 iff sum x_i 2^i<t, the maximum over t of min over relevant i of B_i/Inf_i is 2.0 (n=2), 2.672489 (n=3,4), 2.695888 (n=5,6), 2.697237 (n=7,8), 2.697376 (n=9..12, all t) and 2.697371 on the n=13,14 grids, with maximizing t near 2^n/10; H/I on this family is at most 3.9623 (n<=12).",
  ["float64", "n<=12 all t, n=13,14 on 1,032 t"], "code/lex_check.py, out/lex_check.json", [], "exact values beyond n=7 not rechecked", ["C018 consumers"]),
 ("B18-GOOD-COORDINATE-CONSTANT-LOWER-BOUND-FROM-FEI-LOWER-BOUND", "CONDITIONAL",
  "If some Boolean family has H(f)/I(f) approaching C0, then sup over all nonconstant Boolean f of min over relevant i of B_i/Inf_i is at least C0-2/ln 2, because otherwise the C005 erasure induction proves FEI with a constant below C0. With the literature value C0=6.278944 (recalled, not verified in this stage) the bound is 3.3935.",
  ["C005", "literature lower bound for the FEI constant, unverified here"], "REPORT Section 6", ["C005"], "the value 6.278944 and its normalization were not verified", ["C018 consumers", "A089"]),
]
claims = []
for cid, st, stmt, hyp, src, deps, fu, cons in claims_src:
    claims.append({"claim_id": cid, "version": 1, "exact_statement": stmt, "hypotheses": hyp, "statement_sha256": sha(stmt),
                   "contributors": ["claude-B18-lead"], "proof_source": src, "proof_dependencies": deps,
                   "review_records": [], "status": st, "supersedes": [], "refutes": [], "first_unproved_line": fu,
                   "next_consumers": cons})
verdicts = [
 ("A082-FINITE-TRUE-ERASURE", "HOLDS", "exhaustive n=4 with exact extremals (B18-N4-GOOD-COORDINATE-CERTIFICATE)"),
 ("A082-AFFINE4-ERASURE-BRIDGE", "HOLDS", "B18-AFFINE-SUPPORT-JUNTA-REDUCTION with d=4, K=Kstar"),
 ("A026-AFFINE4-GOOD-COORDINATE", "HOLDS", "implied by the two lines above; 0 n=4 tables above 7/2"),
 ("A061-LOG-COMPENSATION", "HOLDS", "B_i<=lambda+log2(e)Inf_i plus JS<=(2/ln2)Inf_i; 0 violations on n=4"),
 ("A061-FAIR-TREE-PROCESS", "HOLDS", "C005 martingale identities"),
 ("A031-SIGNED-ENTROPY-ANCHOR", "HOLDS", "Fourier transform of f*phi, Parseval with f^2=1, weighted Cauchy-Schwarz; 0 violations on n=4"),
 ("A067-LOCAL-BOOLEAN-GRANULARITY", "HOLDS", "Moebius integrality and coincident maximal sets; fails only at S=empty for constants, excluded by the statement"),
 ("A032-EXACT-PHASE-ADMISSION", "HOLDS (first sentence only)", "n=4 catalogue 32 singletons + 1120 affine 2-flats, 0 others; later sentences not re-derived"),
 ("A057-COHERENT-ERASURE-SPLIT", "HOLDS (B-part); D/J-part unaudited", "B18-A057-B-PART-RECONSTRUCTION"),
 ("A087-CONTROL-TREE-LAMBDA-KL-IDENTITY", "HOLDS except KL-residual naming", "B18-A087-LAMBDA-RECONSTRUCTION"),
 ("A021-UNIFORM-RARE-CORE-EXPANSION", "HOLDS (spot check)", "exact agreement of H and I formulas, 3 cores x t in {1,2} x k in {1,2,3}"),
 ("A096-UNIFORM-SINGLETON-HALF-TAX", "NOT REFUTED; expansion line HOLDS", "B18-A096-FALSIFICATION-SEARCH"),
 ("A092-AND-EXPLICIT-ENDPOINT-LOWER-BOUND", "NOT REFUTED", "50-digit check at p=2^-k, k=1..60"),
 ("A041-BOOLEAN-ONE-BIT-ENDPOINT-TAX-LOWER-BOUND", "CONSISTENT", "ratio 0.4954 at p=2^-60, approaching 1/2"),
 ("A036-POINT-DEFECT-TENSOR-NORMALIZED-PAYMENT-RECOVERY", "EVIDENCE CONSISTENT", "float check, 18 tensor configurations"),
]
out = {"protocol_revision": "2026-10-11-execution-v2", "run_id": RUN_ID, "stream": "B18", "claims": claims,
       "review_verdicts": [{"claim_id": a, "verdict": v, "basis": b, "reviewer": "claude-B18-lead", "run_id": RUN_ID} for a, v, b in verdicts]}
json.dump(out, open(os.path.join(RUN, 'CLAIMS.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
prog = {
 "protocol_revision": "2026-10-11-execution-v2", "run_id": RUN_ID, "stream": "B18", "packet_id": "A087", "gap_id": "G-R-MISMATCH",
 "attempt_id": "B18-lead-proof-audit-1",
 "method": "Independent analytic re-derivation of claimed proofs; exhaustive exact n=4 certificate; exact rational-log recheck; float falsification searches reported as evidence only",
 "mathematical_delta": "C018 holds with the exact optimal constant Kstar=2.6725 (FEI constant 5.558) on Boolean functions with affine Fourier support of dimension <=4 per factor; the constant is exceeded at n=5 by the lexicographic threshold t=3 (2.6958875, exact), so the good-coordinate route needs a larger constant beyond dimension 4.",
 "deliverable_status": "COMPLETE_EXCEPT_REPORT_MD: harness refused the REPORT.md write from this subagent; full report text returned in StructuredOutput",
 "mathematical_status": "AUDIT_VERDICTS_ISSUED; NO_ERROR_FOUND; FULL_FEI_OPEN",
 "claim_versions_used": ["A082-FINITE-TRUE-ERASURE v1", "A082-AFFINE4-ERASURE-BRIDGE v1", "A026-AFFINE4-GOOD-COORDINATE v1", "A061-LOG-COMPENSATION v1", "A061-FAIR-TREE-PROCESS v1", "A031-SIGNED-ENTROPY-ANCHOR v1", "A067-LOCAL-BOOLEAN-GRANULARITY v1", "A032-EXACT-PHASE-ADMISSION v1", "A057-COHERENT-ERASURE-SPLIT v1", "A087-CONTROL-TREE-LAMBDA-KL-IDENTITY v1", "A021-UNIFORM-RARE-CORE-EXPANSION v1", "A096-UNIFORM-SINGLETON-HALF-TAX v1", "A092-AND-EXPLICIT-ENDPOINT-LOWER-BOUND v1", "A041-BOOLEAN-ONE-BIT-ENDPOINT-TAX-LOWER-BOUND v1", "A036-POINT-DEFECT-TENSOR-NORMALIZED-PAYMENT-RECOVERY v1"],
 "claims_created_or_changed": [c["claim_id"] + " v1 " + c["status"] for c in claims],
 "source_artifacts": ["agents/*/runs/*/CLAIMS.json (80 claims; out/all_agent_claims.txt)", "agents/A086/runs/20261011T214823Z-fleet05-A086-joint-code-referee/REPORT.md", "agents/A087/runs/20261011T221055Z-fleet05-A087-restriction-referee/REPORT.md", "agents/A088/runs/20261011T223053Z-fleet05-A088-booleanity-referee/REPORT.md", "code/exhaust_n4.py", "code/checks2.py", "code/check_a057.py", "code/lex_check.py", "code/exact_lex5.py"],
 "next_consumers": ["A090", "A087", "A089", "C018 consumers", "B05", "B19"],
 "next_action": "Exact K*(5): max over nonconstant 5-variable Boolean f of min over relevant i of B_i/Inf_i over the 616,126 NPN classes with exact rational-log recheck of the top values (reviewer A090; A087 checks the symmetry reduction).",
 "stagnant_substantive_attempts": 0,
 "blockers": ["REPORT.md could not be written: the harness refuses report .md files from subagents; the report text is in this run's StructuredOutput return", "Literature FEI lower bound 6.278944 used in a CONDITIONAL claim was not verified (no source read)", "Supervisor adoption and mirroring outside this folder are not B18's to perform (no git/mesh/brain by instruction)"],
 "packet_ids": ["A087"],
}
s = json.dumps(prog, indent=1, ensure_ascii=False)
for name in ('PROGRESS.json', 'PACKET_DELTA.json'):
    open(os.path.join(RUN, name), 'w', encoding='utf-8', newline='\n').write(s)
print('wrote', len(claims), 'claims,', len(verdicts), 'verdicts; sha PROGRESS', sha(s)[:16])
