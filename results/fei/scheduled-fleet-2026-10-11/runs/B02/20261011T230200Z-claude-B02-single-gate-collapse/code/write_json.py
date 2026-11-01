import json, hashlib, sys, os
R = sys.argv[1]
run = os.path.basename(R)
def sha(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()
L1 = ("For every nonconstant f:{-1,1}^n->{-1,1} with relevant support R and every cover of R by M>=1 ordered subsets R_t "
      "(ranks r_t, strict predecessor sets U_j^t): H(f) <= h2(Var f) + (K_ref + log2 M) I(f) + (6/(5 ln 2)) sum_A fhat(A)^2 "
      "sum_{j in A} min_{t: j in R_t} ln( r_t(j)/(|A cap U_j^t|+1) ), K_ref = 3+2log2(3)+log2(6e).")
L2 = ("For one order (M=1) the rank term equals sum_j Inf_j(f) ln r(j) - E_{P_f} ln|A|!, minimized by ordering coordinates by "
      "decreasing influence; hence H(f) <= h2(Var f) + K_ref I(f) + (6/(5 ln 2))[sum_i Inf_(i) ln i - E_{P_f} ln|A|!].")
O1 = ("For tribes T_{m,w} (OR of m disjoint ANDs of width w, q=1-2^-w) and every single-gate table (any M, any ordered M-cover), "
      "the right side of L1 is >= h2(v) + K_ref I + (1 - (6/5) q^{m-1}) I log2 M + (6/5) q^{m-1} I log2(m/e). At m=2^w the ratio to I "
      "tends to infinity (about K_ref + 0.44(w-1.44)) while H/I tends to 4, so no single-gate table certifies FEI with an absolute constant; "
      "the one-gate-per-block forest has bound/I <= 13.40 in the limit (13.34 at w=60).")
RA6 = ("A006 partial review: sunflower spectrum P(empty)=4^-m, P({0})=(1-2^-m)^2, P(T)=P({0} u T)=4^-m and I=1+(m-1)2^-m (m<=10 exact); "
       "max_m 2^-m[m^2+11m/5+4/5]=23/10; m^2+9m+5<=(15/2)2^m; D_m in [1/4, e^(1/4)-1]. Forest enumeration and R_m<=(43/10)I not reproduced.")
RA7 = ("A007 partial review: for D = prod_l(1+x_l)-1, a = sum_l x_l, x_l>=0: 0 <= log2 D - log2 a <= a log2 e. p^2 suppression and petal identity not reproduced.")
PIJ = ("PI-J: with gates = all prime implicants of f^{-1}(true), one fixed fractional lambda and the posterior over partition forests, "
       "is the conditioned residual of eq:posteriorforest <= K I(f) for every Boolean f with an absolute K?")
def claim(cid, st, hyp, src, deps, status, first, nxt, refutes=None):
    return {"claim_id": cid, "version": 1, "exact_statement": st, "hypotheses": hyp, "statement_sha256": sha(st),
            "contributors": ["claude-B02-lead"], "proof_source": src, "proof_dependencies": deps, "review_records": [],
            "status": status, "supersedes": [], "refutes": refutes or [], "first_unproved_line": first, "next_consumers": nxt}
claims = [
 claim("B02-L1-single-gate-collapse", L1, ["f nonconstant", "ordered cover of the relevant support", "logs base 2 except ln"],
       "REPORT.md section L1 (specialization N=1, h_1=f, lambda_1=1 of thm:posteriorforest)", ["forests.tex thm:posteriorforest eq:minforest"],
       "PROVED", None, ["C020", "A086", "A094"]),
 claim("B02-L2-one-order-closed-form", L2, ["M=1"], "REPORT.md section L2", ["B02-L1-single-gate-collapse"], "PROVED", None, ["C020", "A006"]),
 claim("B02-O1-tribes-single-gate-obstruction", O1, ["tribes spectrum, true=-1", "m>=2 for the M-term sign"], "REPORT.md section O1; out/check_single_gate.txt",
       ["B02-L1-single-gate-collapse"], "PROVED", None, ["C020", "A008", "A010"]),
 claim("B02-R-A006-partial", RA6, ["sunflower f_m = x0 AND OR(x1..xm)"], "out/review_a006_a007.txt", ["A006 run 20261011T210855Z"], "CERTIFIED",
       "A006 forest enumeration (stars, run counts) and the assembly R_m <= (43/10) I were not independently reproduced", ["A006", "A086"]),
 claim("B02-R-A007-partial", RA7, ["x_l >= 0"], "REPORT.md reviews; out/review_a006_a007.txt", ["A007 run 20261011T215236Z"], "PROVED",
       "p^2 suppression and petal identity not reproduced", ["A007", "A094"]),
 claim("B02-T-PIJ", PIJ, ["prime-implicant table"], "STREAM_NOTES.md", ["B02-L1-single-gate-collapse"], "OPEN",
       "no bound on sum_{l used}[L_l + s_l log M_l] when the read of a coordinate grows with n", ["A006", "A009", "A010"]),
]
json.dump({"run_id": run, "claims": claims}, open(os.path.join(R, "CLAIMS.json"), "w", encoding="utf-8"), indent=1)
prog = {"protocol_revision": "2026-10-11-execution-v2", "run_id": run, "stream": "B02", "packet_id": "A006",
 "gap_id": "C020-whole-set-witness-cost", "attempt_id": "claude-B02-1",
 "method": "specialize thm:posteriorforest to one gate; exact spectra by integer FWHT; closed forms for tribes; partial independent review of A006/A007",
 "mathematical_delta": "Single-gate collapse (root costs cancel exactly) and its one-order closed form; proof that every single-gate table fails on tribes by log m while the block forest stays bounded (13.40 limit).",
 "deliverable_status": "complete", "mathematical_status": "PROVED (L1, L2, O1); partial reviews CERTIFIED; PI-J OPEN",
 "claim_versions_used": ["C020", "C018"], "claims_created_or_changed": [c["claim_id"] for c in claims],
 "source_artifacts": ["forests.tex lines 1-135", "agents/A006,A007,A008 run reports"], "next_consumers": ["A006", "A007", "A008", "A009", "A010", "A086", "A094"],
 "next_action": "Independent review of L1/L2/O1 by A086 or A094; PI-J on Majority_n (A006); block-forest positive side for read-once DNF (A008).",
 "stagnant_substantive_attempts": 0, "blockers": ["review cap exceeded in B02 (A006, A007, A008 unreviewed as wholes)"], "packet_ids": ["A006"]}
json.dump(prog, open(os.path.join(R, "PROGRESS.json"), "w", encoding="utf-8"), indent=1)
json.dump(prog, open(os.path.join(R, "PACKET_DELTA.json"), "w", encoding="utf-8"), indent=1)
print("ok", [c["statement_sha256"][:12] for c in claims])
