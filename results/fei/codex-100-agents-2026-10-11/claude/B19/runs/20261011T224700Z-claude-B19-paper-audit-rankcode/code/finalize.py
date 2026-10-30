import json, hashlib, os
RUN_ID = "20261011T224700Z-claude-B19-paper-audit-rankcode"
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPER_SHA = "de36fcdab064333565b2f311db861df57b50955245d747ae7c03653d5e9bf28e"


def sha(st, hyp):
    return hashlib.sha256(json.dumps({"statement": st, "hypotheses": hyp}, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


claims = []


def add(cid, st, hyp, status, src, deps, reviews, first_unproved, consumers, refutes=None):
    claims.append({"claim_id": cid, "version": 1, "exact_statement": st, "hypotheses": hyp,
                   "statement_sha256": sha(st, hyp), "contributors": ["claude-B19-lead"],
                   "proof_source": src, "proof_dependencies": deps, "review_records": reviews,
                   "status": status, "supersedes": [], "refutes": refutes or [],
                   "first_unproved_line": first_unproved, "next_consumers": consumers})


add("B19-THRESHOLD-PAPER-CREG-AUDIT",
    "In main.tex with sha256 " + PAPER_SHA + ", the proof of Theorem A (every regular Boolean f satisfies H(f) <= C_reg D(f), C_reg = log2(4+e) + 2 log2(e pi)) has no gap in Lemma levelentropy, Lemma centering, Lemma pivotal-antichain, Lemma antichain-density, Lemma antichain-noise, Lemma ranktail, the Euler reference Q_k(S) = ((2k+1)!/pi^(2k)) prod_{i in S} i^(-2), and the final display l.594-633; the Theorem B Frullani step l.499-504 gives 2 ln m + gamma + 2 exactly.",
    ["entropy in bits", "uniform measure on {-1,1}^n", "regular = unate with a desirability order (l.89-93)"],
    "INDEPENDENT_REVIEW_HOLDS_AT_SCOPE", "PAPER_AUDIT_38pp.md sections 1-2 (hand re-derivation of each step)",
    ["main.tex l.99-117, 252-541, 557-649"], ["claude-B19-lead 2026-10-11, line-by-line"],
    None, ["B20", "A093", "A095"])
add("B19-THRESHOLD-PAPER-CONSTANTS-CERTIFIED",
    "8.9364 < C_reg < 8.9366 (so 4 < C_reg < 8.937); the m-independent constant of eq:ordinaryexact at a = 6/5, C_lev + (1 + ln 6 + (6/5)(2+gamma))/ln 2, lies in [11.2375133696, 11.2375133697]; C_multi = C_lev + (1 + ln 7 + (6/5)(2+gamma))/ln 2 < 11.460; (2(1+ln2) + ln(pi^2/4))/ln2 = 2 log2(e pi); 80 + 460/ln2 < 744.",
    ["C_lev = log2(4+e)", "gamma = Euler's constant"],
    "CERTIFIED", "code/cert_constants.py: exact rational comparison ((4+e_hi)e_hi^2 pi_hi^2)^1000 < 2^8937 with certified rational brackets; mpmath interval arithmetic with Euler-Maclaurin gamma bracket; agrees with A091 out/constants.json",
    [], ["claude-B19-lead exact certificate", "A091 independent rational enclosure (agrees to 18 digits)"],
    None, ["B20"])
add("B19-SHARED-DATA-MULTIPLEXER-REVIEW",
    "Proposition shared-data-collision (main.tex l.2224-2255), Corollary orthogonal-multiplexers (l.2281-2301), Corollary recursive-multiplexers (l.2303-2323) and the Maj3 example (l.2324-2332: two atoms 1/4, eight atoms 1/16, H(F)=3, I(F)=2) hold as stated. The proposition imposes no hypothesis on F: for every Boolean F and every split of its coordinates into a block x of size a and the rest y it is the block-restriction identity with g_b = F|_{x=b}; the substantive hypotheses are I_sel(F) >= c a and FEI for every restriction.",
    ["uniform measure", "x and y disjoint coordinate blocks", "N = 2^a"],
    "INDEPENDENT_REVIEW_HOLDS_AT_SCOPE", "PAPER_AUDIT_38pp.md section 3; code/exact_checks.py sections A-B (216 multiplexers with exact coefficients, all 6 identities pass; 65,536 3-bit pairs for orthogonality <=> disagreement 1/2)",
    ["main.tex l.2212-2333", "Theorem A (for the recursive corollary)"], ["claude-B19-lead 2026-10-11"],
    None, ["A091", "A095", "B20"])
add("B19-RANKCODE-REDUCTION",
    "For every Boolean f on n coordinates and every order pi of [n]: H(f) <= [log2(4+e) + log2(pi^2/4)] I(f) + (2/ln 2) R_pi(f), where R_pi(f) = E_{S ~ fhat^2} sum_{j=1}^{|S|} ln(i_j/j) and i_1 < ... < i_|S| are the pi-positions of the elements of S.",
    ["uniform measure", "entropy in bits", "I = total influence"],
    "PROVED", "Gibbs on the level law with reference P(0)=1-v, P(k)=v(1-rho)rho^(k-1), rho=4/(4+e), plus Lemma levelentropy (valid for every Boolean f by edge-isoperimetry); Gibbs on each level with Q_k of main.tex l.524 and (2k+1)! >= 4^k (k!)^2. Validated on 3,240 (f, order) pairs, n=3,4, proved intervals.",
    ["main.tex Lemma levelentropy l.252-291", "main.tex l.507-541"], ["claude-B19-lead"],
    None, ["A095", "B20"])
add("B19-RANKCODE-GLOBAL-ORDER-NOGO",
    "For integers L >= 2, m >= 1 let f = prod_{b=1}^m AND_L(x_b) on disjoint blocks (+-1 valued). For every order pi of the mL coordinates, R_pi(f) >= 2^(1-L) sum_{p=1}^{mL} max{0, ln p - ln((L+1)/2 + (p-1) 2^(1-L))}; I(f) = mL 2^(1-L); H(f)/I(f) = H(AND_L)/I(AND_L) < 4; and liminf_{m -> infinity} min_pi R_pi(f)/I(f) >= (L-1) ln 2. Hence the right side of B19-RANKCODE-REDUCTION is at least (2(L-1) - o(1)) I(f) for every order while H(f) < 4 I(f): no single-order rank code proves FEI with a constant uniform over all Boolean functions.",
    ["uniform measure", "R_pi as in B19-RANKCODE-REDUCTION"],
    "PROVED", "Per coordinate c at position p: ln(p/N_p) >= 0 with N_p = |S intersect pi^{-1}[1,p]|; Jensen gives E[1{c in S} ln(p/N_p)] >= P(c in S) max{0, ln p - ln E[N_p | c in S]}; P(c in S) = 2^(1-L); given c in S its block's other members are in S independently with prob 1/2 and other blocks are independent, so E[N_p | c in S] <= (L+1)/2 + (p-1) 2^(1-L). H(AND_L)/I(AND_L) <= 4 - [4 + 2(L-1)eps - 2(1-eps)/ln2]/L < 4 with eps = 2^(1-L). The liminf follows from the increasing integrand phi(t) = ln t - ln(c - q + q t). Checks: exhaustive over all orders for (m,L) = (2,2),(3,2),(2,3); certified rows L=4..32 (e.g. L=8, mL=1e9: rank term >= 13.99997 I vs H <= 3.8428 I).",
    ["B19-RANKCODE-REDUCTION (only for the consequence)"], ["claude-B19-lead; independent reviewer requested: A094"],
    None, ["A094", "A095", "B20"], refutes=["any universal-FEI route that uses Theorem A's single-order rank code unchanged"])
add("B19-A056-COMPOSITION-RECHECK",
    "Independent numerical re-check of the A056 disjoint composition identity accepted by A091: for uniform physical inputs and nonconstant, possibly unbalanced children f_i on disjoint blocks, with nu the induced product law of child outputs, Fhat(S)^2 = ghat_nu(A)^2 prod_{i in A} fhat_i(T_i)^2/v_i exactly, H(F) = H_nu(g) + sum_i a_i [H(f_i) - h2(v_i)], I(F) = sum_i a_i I(f_i), Var(F) = Var_nu(g), 0 <= a_i <= 1, a_i = I_i^nu(g)/v_i.",
    ["uniform physical inputs", "disjoint blocks", "children nonconstant"],
    "CHECKED_EVIDENCE", "code/exact_checks.py section C: 110 random compositions (k=2,3; block sizes 1-3), exact rationals plus interval entropies; all five identities pass. The proof is A056/A091's; this is evidence, not a new proof.",
    ["A056 v1", "A091 run 20261011T214848Z"], ["claude-B19-lead"], None, ["B20"])

progress = {
    "protocol_revision": "2026-10-11-execution-v2", "run_id": RUN_ID, "stream": "B19", "packet_id": "A091",
    "gap_id": "B19-threshold-paper-creg-and-shared-data-audit", "attempt_id": RUN_ID + "-1",
    "method": "line-by-line hand audit of main.tex Theorem A and Section 8 shared data; exact rational and interval certificates; exhaustive/random exact checks; Jensen lower bound for the rank code",
    "mathematical_delta": "Theorem A's proof and constants independently confirmed (C_reg in (8.9364, 8.9366)); shared-data proposition shown to be the general block-restriction identity, corollaries hold; new proved boundary: the single-order rank code costs >= 2(L-1) I on XOR of AND_L blocks while H < 4 I, so universal FEI needs a block-adaptive reference.",
    "deliverable_status": "COMPLETE_LOCAL", "mathematical_status": "AUDIT_HOLDS_PLUS_METHOD_NOGO; full FEI OPEN",
    "claim_versions_used": ["C018 v1", "C035 v1", "A056 v1", "B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO v1"],
    "claims_created_or_changed": [c["claim_id"] + " v1" for c in claims],
    "source_artifacts": ["~/fourier-entropy-threshold-functions/paper/main.tex sha256 " + PAPER_SHA,
                         "agents/A091/runs/20261011T214848Z-fleet05-A091-composition-referee/REPORT.md, out/constants.json"],
    "next_consumers": ["A094", "A095", "A091", "B20"],
    "next_action": "A094 to referee B19-RANKCODE-GLOBAL-ORDER-NOGO; A095 to state the largest class with R_pi <= K I and a block-adaptive reference that removes the 2(L-1) cost on XOR-of-AND blocks; A091 to review the B09 core uncertainty lemma (unchanged stream next_action).",
    "stagnant_substantive_attempts": 0,
    "blockers": ["REPORT.md could not be saved: the harness refused the write ('Subagents should return findings as text, not write report files'); its full content is in the lead's StructuredOutput (fields mathematical_delta, claims, codex_checks) and PAPER_AUDIT_38pp.md", "B09 core lemma review (stream next_action) not started by the lead in this run; delegated to A091", "no external persistence: write scope is local only"],
    "packet_ids": ["A091"]}
json.dump(claims, open(os.path.join(HERE, "CLAIMS.json"), "w", encoding="utf-8"), indent=1)
json.dump(progress, open(os.path.join(HERE, "PROGRESS.json"), "w", encoding="utf-8"), indent=1)
pd = dict(progress)
pd["packet_ids"] = ["A091"]
json.dump(pd, open(os.path.join(HERE, "PACKET_DELTA.json"), "w", encoding="utf-8"), indent=1)
for c in claims:
    print(c["claim_id"], c["statement_sha256"][:16], c["status"])
