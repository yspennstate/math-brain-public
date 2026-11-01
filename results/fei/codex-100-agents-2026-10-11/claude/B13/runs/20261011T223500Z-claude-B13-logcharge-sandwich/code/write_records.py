# Writes CLAIMS.json, PROGRESS.json, PACKET_DELTA.json and RECEIPTS.json for this run (data files for the campaign tools).
import hashlib, json, os

RUN = "20261011T223500Z-claude-B13-logcharge-sandwich"
H = ("f: {-1,1}^n -> {-1,1}, uniform measure, any n; p(S)=fhat(S)^2; entropies in bits; for coordinate i and T subset of [n] minus i: "
     "a_T=fhat(T), b_T=fhat(T+i), q_i(T)=a_T^2+b_T^2, theta_T=b_T^2/q_i(T), d_i=Inf_i=sum_T b_T^2; D_i=H(f)-(H(f_+)+H(f_-))/2; "
     "B_i=H(S_i|S_-i); J_i=JS(p_+,p_-); lambda_i=sum over S containing i of p(S) log2(1+p(S minus i)/p(S))")
TREE = ("restriction tree = finite fair adaptive tree fixing one fresh coordinate per node by a fair coin, coordinate chosen from the "
        "history (independent randomization allowed); a stopping tree may stop anywhere; a complete tree stops only at constants")


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


claims = [
    dict(claim_id="B13-LOGCHARGE-KL-FORM", status="AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW",
         exact_statement="For every f and coordinate i with d_i>0, with nu_i(T)=b_T^2/d_i: lambda_i = d_i[log2(1/d_i) - KL(nu_i||q_i)], and lambda_i <= B_i <= lambda_i + d_i/ln 2.",
         hypotheses=H,
         proof_source="elementary: split log2(q/b^2)=log2(1/d)-log2(nu/q); h2(t)-t log2(1/t)=(1-t)log2(1/(1-t)) lies in [0, t/ln 2]",
         proof_dependencies=[], first_unproved_line=None, next_consumers=["A061", "A064", "A087"]),
    dict(claim_id="B13-J-LE-B-UNCERTAINTY", status="AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW",
         exact_statement="For every f and coordinate i: J_i <= B_i, hence D_i <= 2 B_i; for every finite fair adaptive stopping tree E sum_t J_t <= [H(f) - E H(g_tau)]/2 <= E sum_t B_t; pointwise min_i D_i/d_i <= 2 H(f)/I(f), with equality for AND2.",
         hypotheses=H + "; " + TREE,
         proof_source="per T the real unit vector (a_T,b_T)/sqrt(q_i(T)) has computational-basis law (1-theta_T,theta_T) and Hadamard-basis law (u_T,1-u_T), u_T=(a_T+b_T)^2/(2q_i(T)); Maassen-Uffink (PRL 60 (1988) 1103) for two mutually unbiased qubit bases gives h2(theta_T)+h2(u_T)>=1; J_i=sum_T q_i(T)(1-h2(u_T)) and B_i=sum_T q_i(T)h2(theta_T)",
         proof_dependencies=["Maassen-Uffink entropic uncertainty relation (external, cited from memory)"], first_unproved_line=None,
         next_consumers=["A063", "A087", "A094"]),
    dict(claim_id="B13-LOGCHARGE-SANDWICH", status="AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW",
         exact_statement="For every f and every finite fair adaptive stopping tree with stopped function g_tau: H(f)-E H(g_tau)-(3/ln 2)[I(f)-E I(g_tau)] <= E sum_{t<tau} lambda_t <= H(f)-E H(g_tau). For complete trees H(f)-(3/ln 2)I(f) <= E sum lambda_t <= H(f). Consequently FEI holds iff some (equivalently every) complete tree has E sum lambda_t <= K I(f) for an absolute K, with constants differing by at most 3/ln 2.",
         hypotheses=H + "; " + TREE,
         proof_source="telescoping E sum D_t = H(f)-E H(g_tau); fresh-coordinate influence conservation E sum d_t = I(f)-E I(g_tau); node-wise lambda_t <= B_t <= D_t and D_t <= lambda_t + 3 d_t/ln 2",
         proof_dependencies=["B13-LOGCHARGE-KL-FORM v1", "A061-LOG-COMPENSATION v1 (J<=2d/ln2, re-derived)", "A062-INFLUENCE-STOPPING-INTERFACE v1 (re-derived)"],
         first_unproved_line=None, next_consumers=["A061", "A064", "A065", "A087"]),
    dict(claim_id="B13-ONE-COORDINATE-CERTIFICATE", status="AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW",
         exact_statement="Let C* be the best FEI constant (possibly infinite), K* = sup over nonconstant g of min_{i: d_i>0} D_i/d_i, and K*_lambda the same with lambda_i. Then C* <= K* <= C* + min(2/ln 2, C*) and C* - 3/ln 2 <= K*_lambda <= C*. Pointwise for nonconstant g: min_i D_i/d_i <= H/I + min(2/ln 2, H/I) and min_i lambda_i/d_i <= (sum_i B_i)/I <= H/I. Equivalently, FEI holds iff there is an absolute K such that every f has a coordinate i with KL(nu_i||q_i) >= log2(1/Inf_i(f)) - K.",
         hypotheses=H,
         proof_source="min ratio <= ratio of sums; sum_i H(S_i|S_-i) <= H(S) by the chain rule; sum_i J_i <= min((2/ln 2) I, sum_i B_i); greedy argmin tree plus telescoping for the lower bounds",
         proof_dependencies=["B13-J-LE-B-UNCERTAINTY v1", "B13-LOGCHARGE-SANDWICH v1", "A061-LOG-COMPENSATION v1"],
         first_unproved_line="Every Boolean function has a coordinate i with D_i <= K Inf_i for an absolute K (equivalently KL(nu_i||q_i) >= log2(1/Inf_i) - K). This is FEI itself up to 2/ln 2 and is unproved.",
         next_consumers=["A064", "A065", "B05", "A087"]),
    dict(claim_id="B13-DEBT-FALSIFICATION-PRINCIPLE", status="AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW",
         exact_statement="For every complete tree and every coordinate rule, E sum_t (D_t - C d_t) = H(f) - C I(f); for a stopping tree it equals (H(f)-C I(f)) - E[H(g_tau) - C I(g_tau)]. The minimal nonnegative potential Q*_v = max(0, D_v - C d_v + avg Q*_children) (Q*=0 at leaves) satisfies D_t <= C d_t + Q_t - E[Q_{t+1}|F_t], is dominated by every nonnegative potential with that property, and gives H(f) <= C I(f) + Q*_root; Q*_root = 0 under the greedy D/d rule whenever C >= K*. Hence positive expected whole-path debt on a complete tree is exactly a counterexample to H <= C I, independent of the rule, and stopping-rule falsifiers can only target Q*.",
         hypotheses=H + "; " + TREE,
         proof_source="telescoping and conservation; induction from the leaves for minimality",
         proof_dependencies=["A062-INFLUENCE-STOPPING-INTERFACE v1 (re-derived)"], first_unproved_line=None, next_consumers=["A065", "A064"]),
    dict(claim_id="B13-N4-CONSTANTS", status="EXHAUSTIVE_FLOAT64_WITH_CLOSED_FORM_MAXIMA",
         exact_statement="Over all Boolean functions on n<=4 variables: max H/I = 2, 16/3-(3/2)log2 3, 12-(49/16)log2 7 for n=2,3,4; max_g min_i D_i/d_i = 4, 12-(9/2)log2 3, 12-(9/2)log2 3; max_g min_i lambda_i/d_i = 1, (3+log2 10)/4, (3+log2 10)/4; max_g (min_i D_i/d_i - H/I) = 2 (AND2 and embeddings); J_i <= B_i everywhere with max J/B = 1; the sandwich holds on complete trees of rules minInf, maxInf, greedyD, greedyL, lex with (H - E sum lambda)/I <= 2.3622 at n=4 and rule spread <= 0.156 I; Q*_root = 0 at C >= 6.5218 for those rules.",
         hypotheses="n<=4; all 2^(2^n) truth tables; float64 with log2 of integers from mpmath (40 digits); maximizer values enclosed by mpmath intervals",
         proof_source="code/sandwich_all.py, code/certify_n4.py, code/check_JB.py; out/*.json",
         proof_dependencies=[],
         first_unproved_line="Argmax identification rests on float64 evaluation (error far below the float gaps 0.447, 0.125, 0.236); no exact rational-interval sweep over all 65,536 functions was run.",
         next_consumers=["A087", "A065"]),
    dict(claim_id="B13-B05-LOCAL-POTENTIAL", status="NUMERICAL_EVIDENCE_FLOAT64",
         exact_statement="For the B05 sparse bent point-defect family (selector y, k data bits, 2k control bits): at the root H/I = 3.7084 (k=4), 3.7381 (k=6); selector D/d = 8.3001, 10.3507 with B/d - k = 1.488, 1.481 and J/d = 2.812, 2.870; min_i D_i/d_i = 3.3819, 3.8704, attained at data coordinates. For k=4 complete trees under seven rules the sandwich holds, and the minimal nonnegative potential Q*_root/I at C = 6.5218 is 0.0126 for selector_first and minInf and 0 for control_first, control_selector, data_first, greedyD, maxInf; at C = 8 it is at most 0.0021.",
         hypotheses="B05 family as defined in runs/B05/20261011T193057Z-fleet01-B05-rare-restrictions (k even); float64; k=4 full trees with memo, k=6 root only",
         proof_source="code/b05_trees.py; out/b05_trees_results.json",
         proof_dependencies=["B05 family definition (commit 80cc2e50)"],
         first_unproved_line="No proof for general k; the decay of selector-first Q*_root/I like k 2^-k is an extrapolation from (8.30-C) d_y and d_y/I = 2^-k/(2.2k) at k=4.",
         next_consumers=["A065", "A064", "B05"]),
]
order = ["claim_id", "version", "exact_statement", "hypotheses", "statement_sha256", "contributors", "proof_source",
         "proof_dependencies", "review_records", "status", "supersedes", "refutes", "first_unproved_line", "next_consumers"]
for c in claims:
    c["version"] = 1
    c["statement_sha256"] = sha(c["exact_statement"])
    c["contributors"] = ["claude-B13 (Claude lead, stream B13)"]
    c["review_records"] = []
    c["supersedes"] = []
    c["refutes"] = []
claims = [{k: c[k] for k in order} for c in claims]
with open("CLAIMS.json", "w", encoding="utf-8") as fh:
    json.dump({"protocol_revision": "2026-10-11-execution-v2", "run_id": RUN, "stream": "B13", "claims": claims}, fh, indent=1)

blocker = ("REPORT.md, LEARNED.md entry and .final not written: the Claude subagent harness refused report-file writes "
           "(Subagents should return findings as text). The complete report (seven protocol fields and the Universal bridge "
           "paragraph) is in this run's StructuredOutput to the coordinator claude-2d8060eb; .final is withheld so no consumer "
           "treats the run as having a REPORT.md.")
progress = {
    "protocol_revision": "2026-10-11-execution-v2", "run_id": RUN, "stream": "B13", "packet_id": "A061", "gap_id": "G-R-MISMATCH",
    "attempt_id": "B13-lead-logcharge-sandwich-1",
    "method": ("Exact ledger algebra for one fair query (D=B+J, lambda KL form), Maassen-Uffink per Fourier pair, telescoping and "
               "influence conservation on adaptive trees; exhaustive float64 n<=4 sweep with closed-form maxima under mpmath "
               "intervals; B05 k=4 complete trees with the minimal nonnegative potential per rule"),
    "mathematical_delta": ("Log charge lambda_i=d_i[log2(1/d_i)-KL(nu_i||q_i)]; J_i<=B_i (so D_i<=2B_i, half-entropy barrier in "
                           "ledger form); sandwich H-(3/ln2)I<=E sum lambda<=H on every complete tree; K* in [C*, C*+min(2/ln2,C*)] "
                           "so FEI is a one-coordinate certificate; whole-path expected debt is rule-independent, so falsifiers must "
                           "target the minimal potential Q*; B05 k=4: Q*_root/I<=0.0126 at C=6.5218 for every rule tested, 0 for "
                           "five of seven."),
    "deliverable_status": "MATHEMATICS_COMPLETE_REPORT_MD_SAVE_BLOCKED",
    "mathematical_status": "FIVE_LEMMAS_AUTHOR_PROVED; N4_CONSTANTS_EXHAUSTIVE_FLOAT64; B05_POTENTIAL_EVIDENCE; FULL_FEI_OPEN; G-R-MISMATCH_OPEN",
    "claim_versions_used": [
        {"claim_id": "A061-FAIR-TREE-PROCESS", "version": 1, "use": "re-derived; holds"},
        {"claim_id": "A061-LOG-COMPENSATION", "version": 1, "use": "re-derived; holds; J<=2d/ln2 used in the sandwich"},
        {"claim_id": "A062-INFLUENCE-STOPPING-INTERFACE", "version": 1, "use": "re-derived; holds; conservation used in the sandwich"},
        {"claim_id": "A062-BOOLEAN-DIMENSION-LIMIT-OBSTRUCTION", "version": 1, "use": "recomputed I(F_k) and terminal expectations; holds; not a dependency"},
        {"claim_id": "A063-QUERY-COARSENING-REFUND-AND-HALF-ENTROPY-BARRIER", "version": 1, "use": "singleton consequence J<=B and the ledger half-entropy barrier proved independently; block refund and order witness not checked"},
        {"claim_id": "B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO", "version": 1, "use": "family definition for the potential test; scope obstruction only"},
    ],
    "claims_created_or_changed": [{"claim_id": c["claim_id"], "version": 1} for c in claims],
    "source_artifacts": ["CLAIMS.json", "FROZEN_SPEC.json", "code/sandwich_all.py", "code/certify_n4.py", "code/check_JB.py",
                         "code/b05_trees.py", "code/write_records.py", "out/sandwich_all_results.json", "out/sandwich_all_stdout.txt",
                         "out/certify_n4.json", "out/check_JB.json", "out/b05_trees_results.json", "out/b05_trees_stdout.txt",
                         "code/break_JB.py", "out/break_JB.json", "RECEIPTS.json"],
    "next_consumers": ["A064", "A065", "A063", "A087", "A094", "B05", "B20"],
    "next_action": ("Compute min_i D_i/d_i in closed form for point functions, AND-of-bent splices and the B05 family as k grows, and "
                    "either prove min_i D_i/d_i <= 5 on all of them or exhibit growth; reviewer A087 (A094 second)."),
    "stagnant_substantive_attempts": 0,
    "blockers": [blocker, "One-coordinate certificate (FEI up to 2/ln 2) unproved beyond n=4."],
    "packet_ids": ["A061", "A063", "A064", "A065"],
}
with open("PROGRESS.json", "w", encoding="utf-8") as fh:
    json.dump(progress, fh, indent=1)
delta = dict(progress)
delta["packet_ids"] = ["A061"]
with open("PACKET_DELTA.json", "w", encoding="utf-8") as fh:
    json.dump(delta, fh, indent=1)
rec = {}
for root, _, files in os.walk("."):
    for fn in sorted(files):
        p = os.path.join(root, fn).replace(os.sep, "/")
        if p.endswith("RECEIPTS.json") or "__pycache__" in p:
            continue
        with open(p, "rb") as fh:
            b = fh.read()
        rec[p] = {"bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}
with open("RECEIPTS.json", "w", encoding="utf-8") as fh:
    json.dump({"run_id": RUN, "files": rec, "save_blocker": blocker}, fh, indent=1)
for p, v in rec.items():
    print(p, v["bytes"], v["sha256"][:16])
