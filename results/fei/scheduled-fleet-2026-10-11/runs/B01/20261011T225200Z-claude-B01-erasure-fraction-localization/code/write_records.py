# Writes CLAIMS.json, PROGRESS.json, PACKET_DELTA.json for this run (machine-readable campaign records).
import json, hashlib, os, datetime
RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RID = os.path.basename(RUN)
A = "2/ln 2"


def sha(statement, hyps):
    return hashlib.sha256(json.dumps({"statement": statement, "hypotheses": hyps}, sort_keys=True,
                                     separators=(",", ":")).encode("utf-8")).hexdigest()


def fsha(p):
    with open(os.path.join(RUN, p), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


BASE_H = ["f: {-1,1}^n -> {-1,1}, n finite, uniform measure", "p(S)=fhat(S)^2, entropies in bits",
          "Inf_i=sum_{S containing i} fhat(S)^2, I=sum_i Inf_i, B_i=H(S_i|S_{-i}), B=sum_i B_i, DTC=H-B",
          "Delta_i=H(f)-(H(f_{i,+})+H(f_{i,-}))/2 for the physical restrictions x_i=+1,-1"]
claims = []


def add(cid, status, stmt, hyps, proof, deps, first_unproved=None, refutes=None, consumers=None, reviews=None):
    claims.append({"claim_id": cid, "version": 1, "exact_statement": stmt, "hypotheses": hyps,
                   "statement_sha256": sha(stmt, hyps), "contributors": ["claude-B01-lead"],
                   "proof_source": proof, "proof_dependencies": deps, "review_records": reviews or [],
                   "status": status, "supersedes": [], "refutes": refutes or [],
                   "first_unproved_line": first_unproved,
                   "next_consumers": consumers or ["A003", "A051", "A031", "A086", "A094"]})


add("B01-COORD-JS-BOUND", "PROVED",
    "For every Boolean f and coordinate i, with f=psi+x_i*phi, JS_i(f) <= (2/ln 2)*sum_{T not containing i} min(psihat(T)^2, phihat(T)^2) <= (2/ln 2)*min(Inf_i(f), 1-Inf_i(f)), where JS_i is the equal-weight Jensen-Shannon divergence in bits of the squared spectra of f_{i,+} and f_{i,-}. The constant 2/ln 2 is sharp as Inf_i -> 0.",
    BASE_H, RID + "/REPORT (blocked; text in StructuredOutput) section 2: per-cell reduction to G(u)<=2u^2 with K(u)=2u^2-G(u), K(0)=K'(0)=0, K''>=0",
    ["C005 per-cell form of JS"])
add("B01-MINIMAL-VIOLATOR-STRUCTURE", "PROVED",
    "Let C*>=0 and let f be Boolean with m>=2 relevant coordinates such that H(f_{i,s}) <= C* I(f_{i,s}) for every relevant i and s in {+1,-1}, and r=H(f)/I(f) > C*. Then for every relevant i: (a) Delta_i(f) >= C* Inf_i(f) + (r-C*) I(f) > r Inf_i(f); (b) B_i(f) > (r-2/ln 2) Inf_i(f) and Inf_i(f) < e^3 2^{-r}; (c) H(f)-B(f) <= (2/ln 2 - (m-1)(r-C*)) I(f) < (2/ln 2) I(f), so (m-1)(r-C*) <= 2/ln 2 and B(f)/H(f) > 1-2/(r ln 2). If some Boolean function violates H <= C* I, a violator with the fewest relevant variables exists and satisfies the hypotheses.",
    BASE_H + ["C* >= 0 fixed in advance"],
    RID + " derivation section 3 (influence recursion, Delta_i=B_i+JS_i, B-JS bound, h2(x)<=x log2(e/x), well-ordering of the number of relevant variables)",
    ["B01-COORD-JS-BOUND v1", "C005 identity Delta_i=B_i+JS_i (re-derived)", "B<=H (chain rule)"])
add("B01-FEI-IFF-LOW-INFLUENCE-ERASURE", "PROVED",
    "FEI holds if and only if there is K>=0 such that B(f) <= K I(f) for every Boolean f with H(f)-B(f) < (2/ln 2) I(f) and max_i Inf_i(f) < e^3 2^{-(K+2/ln 2)}. Forward constant C=K+2/ln 2; conversely FEI(C) gives the condition with K=C.",
    BASE_H, RID + " derivation section 4 (least violator from B01-MINIMAL-VIOLATOR-STRUCTURE)",
    ["B01-MINIMAL-VIOLATOR-STRUCTURE v1"])
add("B01-ERASURE-FRACTION-BRIDGE", "PROVED",
    "If lambda in [0,1), K>=0 and B(f) <= lambda H(f) + K I(f) for every Boolean f with H(f)-B(f) < (2/ln 2) I(f) and all influences below e^3 2^{-C}, where C=(K+2/ln 2)/(1-lambda), then FEI(C). Equivalently DTC(f) >= (1-lambda) H(f) - K I(f) on that class suffices. The same holds inside any class of Boolean functions closed under physical restrictions. FEI(C) gives the hypothesis with lambda=0, K=C.",
    BASE_H, RID + " derivation section 5", ["B01-MINIMAL-VIOLATOR-STRUCTURE v1"])
add("B01-LOW-INFLUENCE-GOOD-COORDINATE", "PROVED",
    "FEI holds iff there are tau in (0,1], lambda in [0,1), K>=0 such that every Boolean f with max_i Inf_i(f) < tau has a relevant coordinate i with B_i(f) <= (lambda H(f)/I(f) + K) Inf_i(f). Forward constant C = max(log2(e/tau) + 2/ln 2, (K+2/ln 2)/(1-lambda)); converse with lambda=0, K=C and any tau.",
    BASE_H, RID + " derivation section 6", ["B01-MINIMAL-VIOLATOR-STRUCTURE v1", "C018 averaging step"])
add("B01-SMALL-N-CALIBRATION", "CERTIFIED",
    "Over all labelled Boolean tables with n=2,3,4 inputs: max H/I = 2, (256-72 log2 3)/48, (1536-392 log2 7)/128; G* = max_f min_{relevant i} B_i/Inf_i = 2, 2.672488984, 2.672488984 (n=4 maximizers are 3-variable point defects); D* = max_f min_i Delta_i/Inf_i = 4, 4.867668747, 4.867668747; max JS_i/min(Inf_i,1-Inf_i) = 2, 2.195179763, 2.398671813 (< 2/ln 2); functions with Delta_i > r Inf_i at every relevant i: 8, 104, 22384; functions with r above every one-step restriction ratio: 8, 40, 880, all satisfying B01-MINIMAL-VIOLATOR-STRUCTURE (a)-(c) with C* the largest restriction ratio, min margins (c) 0.886, 0.518, 0.389. Decimal values to 1e-9.",
    ["exhaustive enumeration of 2^(2^n) tables, n<=4", "float64 screening with error below 1e-12; ties within 1e-9 decided exactly via integer vectors over log2 of primes at 300 bits"],
    RID + "/code/calib.py; out/calib_n1_4.json", ["none (finite computation)"],
    consumers=["A003", "A004", "A001"])
add("B01-LOW-INFLUENCE-DTC-TARGET", "OPEN",
    "There are absolute c>0, K>=0, tau>0 such that every Boolean f with max_i Inf_i(f) <= tau satisfies H(f)-B(f) >= c H(f) - K I(f).",
    BASE_H, "target; FEI-equivalent by B01-ERASURE-FRACTION-BRIDGE (forward) and B<=H (converse)",
    ["B01-ERASURE-FRACTION-BRIDGE v1"],
    first_unproved="No step proved. Product laws of Bernoulli(q) coordinates satisfy DTC=0 with H/I ~ log2(e/q), so any proof must use full signed Booleanity: sum_S fhat(S) fhat(S xor U) = 0 for U nonempty (G-BOOLEANITY).",
    consumers=["A031", "A003", "B07", "B08", "B14"])
add("B01-PRODUCT-LAW-RIGIDITY-SMALL-N", "CERTIFIED",
    "For n=1,2,3,4, the Boolean functions on n inputs whose spectral law is a product measure on {0,1}^n (equivalently DTC=0) number 4, 16, 64, 1120, and every marginal Inf_i of each of them lies in {0, 1/2, 1}; hence each satisfies H(f) <= 2 I(f).",
    ["exhaustive, exact integer test p(S)*N2^(n-1) == prod_i (N2*Inf_i or N2*(1-Inf_i))"],
    RID + "/code/product_laws.py; out/product_laws_n1_4.json", ["none (finite computation)"], consumers=["A031", "A003"])
add("B01-PRODUCT-LAW-RIGIDITY", "OPEN",
    "If the spectral law of a Boolean function is a product measure on {0,1}^n, then every marginal Inf_i(f) lies in {0, 1/2, 1}. Proved necessary condition: for 0<Inf_i<1, (1-Inf_i)/Inf_i is the square of a rational (it equals W(T)^2/W(T+i)^2 for integer Walsh sums).",
    BASE_H, "open; exact case of the near-product exclusion needed by B01-LOW-INFLUENCE-DTC-TARGET",
    ["Booleanity: f=psi+x_i phi with psi*phi=0 and psi^2+phi^2=1 pointwise"],
    first_unproved="Proportional spectral magnitudes |psihat(T)|^2 = ((1-q)/q)|phihat(T)|^2 for all T, with psi, phi ternary of disjoint supports, have not been shown to force q=1/2.",
    consumers=["A031", "A003", "A005"])
reviews = [
    {"reviewed_claim": "A001-FIXED-BOOLEAN-MARGINAL-TENSOR-ADMISSION v1", "reviewer": "claude-B01-lead", "verdict": "CORRECT",
     "note": "Product spectrum of F0(X,Y0)*f^{tensor t} on fresh variables gives H(S_Y|S_X)=c0+tH(f), I=I(F0)+tI(f); upper bound H(S_Y|S_X)<=H<=C_FEI I. Re-derived analytically."},
    {"reviewer": "claude-B01-lead", "reviewed_claim": "A001-UNIVERSAL-QUANTIFIER-AND-GAP-MAP v1 (good-coordinate equivalence part)", "verdict": "CORRECT",
     "note": "E_K => FEI(K+2/ln 2) by averaging and telescoping; FEI(C) => B<=H<=CI. JS constant 2/ln 2 now has a complete proof (B01-COORD-JS-BOUND)."},
    {"reviewer": "claude-B01-lead", "reviewed_claim": "A002-FULL-SUPPORT-ADMISSION v1 (support part)", "verdict": "CORRECT (support); continuity bound not re-derived",
     "note": "Coefficients of a Boolean function of D bits lie in 2^(1-D)Z; after two dummies one flip moves every coefficient by +-2^(-1-D), so no coefficient vanishes."},
    {"reviewer": "claude-B01-lead", "reviewed_claim": "A002 two-cell selector ledger", "verdict": "CORRECT",
     "note": "M=((1+s)/2)u+((1-s)/2)g: H(M)=2+H(g)/2, I(M)=1+I(g)/2; with g=z f^{tensor m}: 4+mH(f)<=C(3+mI(f))."},
    {"reviewer": "claude-B01-lead", "reviewed_claim": "A003 run 20261011T221324Z sections 1-2 (implication diagram, L<=B<=L+I/ln2, Gibbs posterior identity)", "verdict": "CONSISTENT (read, not line-audited)",
     "note": "Edge split B_i = L_i + sum_T p_T log2(1+p_{T+i}/p_T) matches the lead's derivation."}]
with open(os.path.join(RUN, "CLAIMS.json"), "w", encoding="utf-8") as fh:
    json.dump({"protocol_revision": "2026-10-11-execution-v2", "run_id": RID, "stream": "B01", "claims": claims,
               "review_records_for_other_claims": reviews}, fh, indent=1, ensure_ascii=True)
arts = ["code/calib.py", "code/write_records.py", "out/FROZEN_SPEC.json", "out/calib_n1_3.json", "out/calib_n1_4.json", "code/product_laws.py", "out/product_laws_n1_4.json", "CLAIMS.json"]
prog = {"protocol_revision": "2026-10-11-execution-v2", "run_id": RID, "stream": "B01", "packet_id": "A003",
        "gap_id": "G-BOOLEANITY", "attempt_id": "B01-claude-20261011-01",
        "method": "least-violator (well-ordering) analysis of the restriction recursion, complete proof of the JS coordinate bound, exhaustive certified calibration n<=4",
        "mathematical_delta": "Proved that a least violator of FEI(C*) has every influence below e^3 2^{-r}, every coordinate with B_i > (r-2/ln 2) Inf_i, and DTC < (2/ln 2) I; hence FEI <=> B <= K I on {DTC < (2/ln 2) I, max Inf < e^3 2^{-K-2/ln 2}} (C = K + 2/ln 2), with a lambda<1 erasure-fraction bridge and a low-influence localization of the good-coordinate route. Remaining: DTC >= cH - KI for low-influence Boolean f (FEI-equivalent; needs Booleanity).",
        "deliverable_status": "COMPLETE_WITH_SAVE_BLOCKER", "mathematical_status": "REDUCTION_PROVED; FULL_FEI_OPEN",
        "claim_versions_used": ["C005", "C018", "A001-UNIVERSAL-QUANTIFIER-AND-GAP-MAP v1", "A001-FIXED-BOOLEAN-MARGINAL-TENSOR-ADMISSION v1", "A002-FULL-SUPPORT-ADMISSION v1", "A002-EXACT-HARDENING-LEDGER v1"],
        "claims_created_or_changed": [c["claim_id"] + " v1" for c in claims],
        "source_artifacts": [{"path": p, "sha256": fsha(p)} for p in arts],
        "next_consumers": ["A003", "A051", "A031", "A086", "A094", "B07", "B08", "B14"],
        "next_action": "Prove or refute DTC(f) >= c H(f) - K I(f) for Boolean f with all influences <= tau, starting from the U={i} Booleanity identity (psi orthogonal to phi) on near-product spectral laws.",
        "stagnant_substantive_attempts": 0,
        "blockers": ["REPORT.md, LEARNED.md and the STREAM_NOTES.md update were not written: the harness refused the REPORT.md write ('Subagents should return findings as text, not write report files'); STREAM_NOTES.md v1 (22:39Z) predates the refusal and was not updated; the full report, learned notes and agent targets are in this run's StructuredOutput for the coordinator to persist."],
        "packet_ids": ["A003"],
        "written_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
with open(os.path.join(RUN, "PROGRESS.json"), "w", encoding="utf-8") as fh:
    json.dump(prog, fh, indent=1, ensure_ascii=True)
with open(os.path.join(RUN, "PACKET_DELTA.json"), "w", encoding="utf-8") as fh:
    json.dump(prog, fh, indent=1, ensure_ascii=True)
print(json.dumps({c["claim_id"]: c["statement_sha256"] for c in claims}, indent=0))
