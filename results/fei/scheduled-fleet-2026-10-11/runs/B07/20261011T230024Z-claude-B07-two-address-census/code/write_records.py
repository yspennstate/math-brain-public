#!/usr/bin/env python
"""Writes CLAIMS.json, PROGRESS.json, PACKET_DELTA.json for the run (statement_sha256 per protocol convention)."""
import json, hashlib, os, sys
RUN = sys.argv[1]
RID = os.path.basename(RUN.rstrip('/\\'))


def sha(stmt, hyp):
    return hashlib.sha256(json.dumps({"statement": stmt, "hypotheses": hyp}, sort_keys=True,
                                     separators=(",", ":")).encode('utf-8')).hexdigest()


def fsha(p):
    with open(os.path.join(RUN, p), 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


H_CLASS = ["Uniform measure on {-1,1}^N", "f Boolean", "Entropy in bits, I = sum |S| fhat(S)^2",
           "Two-address class: a set A of two coordinates such that for every positive-probability value of S_A the "
           "conditional law of S_(A^c) is a product law (ONE_BIT_ENDPOINT.md section 3; alternative_strategy.md Route C)"]
claims = []

s1 = ("The three-variable one-point defect f = 1 - 2*1{x = x0}, with address set A equal to two of its variables and with "
      "any number of dummy variables added, lies in the two-address conditional-product class and has "
      "H(f)/I(f) = 16/3 - (3/2) log2 3 = 2.955889... > 40/17. Hence any constant C_2 with H <= C_2 I on the class satisfies "
      "C_2 >= 16/3 - (3/2) log2 3. More generally C_k >= M_(k+1), the largest H/I over (k+1)-variable Boolean functions.")
p1 = ("fhat(empty) = 3/4 and fhat(S) = -chi_S(x0)/4 for S nonempty, so H = (9/16)log2(16/9) + 7/4 and I = 12/16. With "
      "A = {1,2}, A^c = {3}; every law on one bit is product, and dummy coordinates are deterministic in every conditional "
      "law. For k addresses the condition is vacuous on k+1 variables.")
claims.append({"claim_id": "B07L-TWO-ADDRESS-POINT-DEFECT", "version": 1, "exact_statement": s1, "hypotheses": H_CLASS,
               "statement_sha256": sha(s1, H_CLASS), "contributors": ["claude-B07-lead"],
               "proof_source": {"text": p1, "check": "out/P4_census.json, out/P4_certificate_cstar.json"},
               "proof_dependencies": [], "review_records": [], "status": "PROVED", "supersedes": [],
               "refutes": ["C016 and X008 as the best recorded two-address obstruction (40/17); not refuted as a counterexample to constant two"],
               "first_unproved_line": None, "next_consumers": ["A034", "A032", "F12", "A088", "A094"]})

s2 = ("For every Boolean F on N <= 5 uniform variables and every pair A of coordinates for which F is in the two-address "
      "conditional-product class, H(F) <= (16/3 - (3/2) log2 3) I(F). For a fixed address pair, equality holds for exactly "
      "32 functions at N = 4 and 48 at N = 5, each an embedded three-variable one-point defect containing both addresses.")
p2 = ("Exhaustive enumeration through the partial Walsh slices g_J in {0,+-1/2,+-1} (pure/mixed pointwise pattern lemma), "
      "exact integer product test per slice, Booleanity re-checked per function; the inequality decided per function by the "
      "integer comparison Ztot^(6 Ztot) 3^(9K) <= 2^(32K) prod C^(6C). N = 4 count (10,560) confirmed by brute force over all "
      "65,536 truth tables. N = 5 count 1,564,928.")
claims.append({"claim_id": "B07L-TWO-ADDRESS-CENSUS-N5", "version": 1, "exact_statement": s2, "hypotheses": H_CLASS + ["N <= 5"],
               "statement_sha256": sha(s2, H_CLASS + ["N <= 5"]), "contributors": ["claude-B07-lead"],
               "proof_source": {"text": p2, "code": ["code/b07_lead_checks.py", "code/certify_max.py", "code/bruteforce_n4.py"],
                                "certificate": "out/P4_certificate_cstar.json", "certificate_sha256": fsha("out/P4_certificate_cstar.json")},
               "proof_dependencies": ["B07L-TWO-ADDRESS-POINT-DEFECT"], "review_records": [], "status": "CERTIFIED",
               "supersedes": [], "refutes": [], "first_unproved_line": None, "next_consumers": ["A034", "A032", "F12", "A088"]})

H3 = ["p a probability law on a finite set", "largest atom p_max < 1", "ell = log2(1/p) on the support", "entropy in bits"]
s3 = ("p_max (H(p) - H_inf(p))^2 <= (1 - p_max) Var_p(ell). Equality holds when ell takes exactly two values and the smaller "
      "value has mass p_max; in particular for the spectral law of every n-bit one-point defect. So the point-defect "
      "calibration (H - H_inf)/I -> 4 of the A031 anchor inequality is reproduced, with equality, without Booleanity.")
p3 = ("X = ell - H_inf >= 0, q = P(X = 0) >= p_max, mu = E X. Cauchy-Schwarz on {X > 0}: E X^2 >= mu^2/(1-q), so "
      "Var X >= mu^2 q/(1-q) >= mu^2 p_max/(1-p_max).")
claims.append({"claim_id": "B07L-GENERIC-MINENTROPY-CALIBRATION", "version": 1, "exact_statement": s3, "hypotheses": H3,
               "statement_sha256": sha(s3, H3), "contributors": ["claude-B07-lead"],
               "proof_source": {"text": p3, "illustration": "out/P3_generic_minentropy.json"},
               "proof_dependencies": [], "review_records": [], "status": "PROVED", "supersedes": [], "refutes": [],
               "first_unproved_line": None, "next_consumers": ["A031", "A035", "A088"]})

H4 = ["n = 4", "magnitude vector m = (8,8,4,4,4,4,4,4,4,4,0,0,0,0,0,0)/16 indexed by subsets of [4] in binary order"]
s4 = ("m passes every separate XOR pair-partition test and, for each nonzero U, some common sign vector cancels the U-th "
      "signed autoconvolution, but none of the 1024 sign vectors cancels all fifteen; no 4-bit Boolean function has |fhat| = m; "
      "840 of the 360,360 labelled placements of the multiset {8,8,4^8,0^6} are Boolean-realizable; there are 2261 distinct "
      "4-bit Boolean spectral laws.")
claims.append({"claim_id": "B07L-REVIEW-A032-TEN-ATOM", "version": 1, "exact_statement": s4, "hypotheses": H4,
               "statement_sha256": sha(s4, H4), "contributors": ["claude-B07-lead (independent re-derivation of A032)"],
               "proof_source": {"code": "code/b07_lead_checks.py P1", "certificate": "out/P1_ten_atom.json",
                                "certificate_sha256": fsha("out/P1_ten_atom.json")},
               "proof_dependencies": [], "review_records": [{"reviews": "A032-EXACT-PHASE-ADMISSION v1 (sha de3e9399...)",
                                                             "verdict": "ACCEPT ten-atom obstruction, n=4 counts, even-rank admission at n<=4; general-n support<=4 classification not re-proved"}],
               "status": "CERTIFIED", "supersedes": [], "refutes": [], "first_unproved_line": None,
               "next_consumers": ["A032", "A088"]})

with open(os.path.join(RUN, 'CLAIMS.json'), 'w', encoding='utf-8') as fh:
    json.dump(claims, fh, indent=1)

progress = {"protocol_revision": "2026-10-11-execution-v2", "run_id": RID, "stream": "B07", "packet_id": "A034",
            "gap_id": "G-PHASE-COND", "attempt_id": RID + "-1",
            "method": "exact exhaustive census of two-address conditional-product Boolean functions (N<=5) with integer certificate; generic probability inequality; independent re-derivation of A031/A032 results",
            "mathematical_delta": "Best known lower bound on the two-address constant raised from 40/17 to 16/3-(3/2)log2 3 = 2.9559 (three-variable point defect, vacuous one-coordinate conditionals); exact maximum for N<=5 certified; A031 point-defect calibration shown generic; A032 ten-atom obstruction and n=4 counts confirmed.",
            "deliverable_status": "COMPLETE_WITH_SAVE_BLOCKER", "mathematical_status": "PARTIAL: lower bound and small-N exact maximum; finiteness of C_2 OPEN",
            "claim_versions_used": ["A031-SIGNED-ENTROPY-ANCHOR v1", "A031-ANCHOR-POSITIVE-PAYMENT-NOGO v1", "A032-EXACT-PHASE-ADMISSION v1", "C016", "C031", "X008"],
            "claims_created_or_changed": [c["claim_id"] + " v1" for c in claims],
            "source_artifacts": ["out/P1_ten_atom.json", "out/P2_affine_even.json", "out/P3_generic_minentropy.json",
                                 "out/P4_census.json", "out/P4_certificate_cstar.json", "out/P4_bruteforce_n4.json"],
            "next_consumers": ["A034", "A032", "A031", "A035", "F12", "A088", "A094"],
            "next_action": "Search N=6 two-address functions for H/I > 16/3-(3/2)log2 3, beginning with pure configurations (four {0,+-1} slices with disjoint supports and product spectra).",
            "stagnant_substantive_attempts": 0,
            "blockers": ["REPORT.md not written: the subagent harness refused the write (Write tool: 'Subagents should return findings as text, not write report files'). The full report (seven protocol fields and the Universal bridge) is in the final StructuredOutput and the proofs are in CLAIMS.json.",
                         "Process deviation: P3 float illustration built dense Hadamard matrices up to 16384x16384 (several GB, about three minutes), above the 1 GB per-job limit."],
            "packet_ids": ["A034"]}
with open(os.path.join(RUN, 'PROGRESS.json'), 'w', encoding='utf-8') as fh:
    json.dump(progress, fh, indent=1)

delta = {"run_id": RID, "stream": "B07", "packet_ids": ["A034"], "gap_id": "G-PHASE-COND",
         "changed_downstream": ["C016/C031/X008: two-address lower bound now 16/3-(3/2)log2 3 (three variables); F12 tracked metric starts here",
                                "A031 anchor: accepted at stated scope; point-defect calibration is generic (equality in a Booleanity-free inequality)",
                                "A032 admission: ten-atom obstruction and n=4 counts independently confirmed"],
         "claims": [{"claim_id": c["claim_id"], "version": 1, "status": c["status"], "statement_sha256": c["statement_sha256"]} for c in claims],
         "review_requested": ["A088", "A094"]}
with open(os.path.join(RUN, 'PACKET_DELTA.json'), 'w', encoding='utf-8') as fh:
    json.dump(delta, fh, indent=1)
print(json.dumps([(c["claim_id"], c["statement_sha256"][:12]) for c in claims]))
