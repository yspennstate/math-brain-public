"""Writes CLAIMS.json, PROGRESS.json, PACKET_DELTA.json and out/MANIFEST.json for this run (data records)."""
import json, hashlib

RUN = "20261011T225600Z-claude-B16-retained-kl-sandwich"


def sha_stmt(statement, hypotheses):
    s = json.dumps({"statement": statement, "hypotheses": hypotheses}, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


S1 = ("For every Boolean f:{-1,1}^n->{-1,1} and every stopping restriction tree T for f (adaptive single-coordinate "
      "queries, arbitrary leaves, node weight w_v=2^-depth), with u_T=fhat_v(T), v_T=fhat_v(T+i_v) for T not containing i_v, "
      "q_T=u_T^2+v_T^2, m_T=min(u_T^2,v_T^2), M_v=sum_T m_T, Q_v=sum_{T:m_T>0} m_T log2(q_T/m_T): "
      "sum_v w_v Q_v + E[H(leaf)] <= H(f) <= sum_v w_v Q_v + E[H(leaf)] + (3/ln2) sum_v w_v M_v, and "
      "sum_v w_v M_v <= I(f) - E[I(leaf)]. Consequently for complete trees H(f)-(3/ln2)I(f) <= sum_v w_v Q_v <= H(f): "
      "the retained-KL tree target sum_v w_v M_v[log2(1/M_v)-D_2(nu_v||q_v)]=O(I) (ISOSPECTRAL (8.1)) holds for one complete "
      "tree iff it holds for every tree iff FEI holds, with constants shifted by at most 3/ln2.")
H1 = ("uniform measure on {-1,1}^n; entropy in bits; H(f)=-sum fhat(S)^2 log2 fhat(S)^2; I(f)=sum |S| fhat(S)^2; "
      "Q_v=M_v=0 at nodes with M_v=0; E is over the uniform random leaf; no independence or symmetry assumption")
P1 = ("Node: for theta=m_T/q_T in [0,1/2], q_T h2(theta)=m_T log2(q_T/m_T)+(q_T-m_T)log2(q_T/(q_T-m_T)); the second term lies in "
      "[0,m_T/ln2] since -(1-r)ln(1-r)<=r. Summing, Q_v<=B_v<=Q_v+M_v/ln2. With Delta_v=B_v+JS_v (ISOSPECTRAL 2.8), 0<=JS_v<=2M_v/ln2 "
      "(ISOSPECTRAL 3.3): Q_v<=Delta_v<=Q_v+3M_v/ln2; M_v<=j_v<=Inf_v (ISOSPECTRAL 3.1). Tree: H(f_v)=Delta_v+mean H(children) and "
      "I(f_v)=Inf_v+mean I(children) (C005) telescope to H(f)=sum w_v Delta_v+E H(leaf), I(f)=sum w_v Inf_v+E I(leaf). Insert node bounds. QED. "
      "Validation: code/b16_sandwich.py Part 1, all 65,536+256+16+4 Boolean functions on n<=4, every node of every complete tree "
      "(covers every node of every adaptive tree on n<=4): exact integer identities true, all inequality violations 0.0 in float64.")
S2 = ("For odd n in {5,9,17,33,65,129,257,513}, every complete coordinate tree of Maj_n (all orders give the same node multiset) has "
      "Lambda_T/I(Maj_n) >= 0.385, 0.655, 0.981, 1.355, 1.766, 2.199, 2.651, 3.115 respectively, where "
      "Lambda_T=sum_internal w_v j_v log2(1+kappa_min,v/(2 j_v)) (LOG_ALLOCATION section 5); with the exact isospectral splits "
      "(partial sum s=0, the only isospectral nodes) skipped the values are 0.133, 0.364, 0.678, 1.063, 1.499, 1.965, 2.451, 2.949; "
      "on the same range H(Maj_n)/I(Maj_n) <= 2.826. Conjecture: Lambda_T/I=(1/2)log2 n - c + o(1) with or without the skip, while H/I stays bounded.")
H2 = ("kappa lower bound per child c: kappa(c) >= 1-max(chat(empty)^2, max_j Inf_j(c)) (rigorous: chat(S)^2<=Inf_j(c) for j in S); "
      "node data exact rationals; logarithms float64 (evidence, not a certificate); exact kappa checked by Krawtchouk for n<=33 (808 child checks, "
      "maximum always at level<=1); Lambda_v=0 when j_v=0")
P2 = ("code/b16_sandwich.py Part 4; out/b16_sandwich_results.json part4_majority_Lambda. Asymptotic proof sketch: on good nodes d<=n/2, |s|<=sqrt(n-d), "
      "j_v<=(1+o(1))sqrt(2/(pi m)) and kappa_min>=c'>0, so each good node pays >= w_v j_v((1/2)log2 n - O(1)).")

claims = [
    {"claim_id": "B16-RETAINED-KL-SANDWICH", "version": 1, "exact_statement": S1, "hypotheses": H1,
     "statement_sha256": sha_stmt(S1, H1), "contributors": ["claude-B16-lead"], "proof_source": P1,
     "proof_dependencies": ["ISOSPECTRAL_SPLICING_CURATED eq.2.8", "ISOSPECTRAL_SPLICING_CURATED Thm 3.1",
                            "ISOSPECTRAL_SPLICING_CURATED Thm 3.3", "C005"],
     "review_records": [{"reviewer": "claude-B16-lead (self)", "kind": "exhaustive exact/float validation n<=4", "result": "PASS"},
                        {"reviewer": "A092 (requested)", "kind": "independent proof review", "result": "PENDING"}],
     "status": "PROVED", "supersedes": [], "refutes": [],
     "first_unproved_line": None,
     "next_consumers": ["A077", "A080", "A092", "ISOSPECTRAL route (8.1)/section 9", "C019"]},
    {"claim_id": "B16-MAJORITY-LAMBDA-DIVERGENCE", "version": 1, "exact_statement": S2, "hypotheses": H2,
     "statement_sha256": sha_stmt(S2, H2), "contributors": ["claude-B16-lead"], "proof_source": P2,
     "proof_dependencies": ["LOG_ALLOCATION_CURATED section 5 (Lambda_T definition)", "monotone threshold Fourier facts"],
     "review_records": [{"reviewer": "claude-B16-lead (self)", "kind": "exact rational node data + Krawtchouk kappa check n<=33", "result": "PASS"},
                        {"reviewer": "A076 (requested)", "kind": "independent threshold code", "result": "PENDING"}],
     "status": "EVIDENCE", "supersedes": [], "refutes": [],
     "first_unproved_line": ("explicit-constant local limit bound: sum over good nodes {d<=n/2,|s|<=sqrt(n-d)} of w_v j_v >= c I(Maj_n) "
                             "with kappa_min>=c'>0 there"),
     "next_consumers": ["A076", "A077", "LOG_ALLOCATION route (8)", "C019"]},
]
with open("CLAIMS.json", "w", encoding="utf-8") as fh:
    json.dump({"run_id": RUN, "stream": "B16", "claims": claims}, fh, indent=1)

progress = {
    "protocol_revision": "2026-10-11-execution-v2", "run_id": RUN, "stream": "B16", "packet_id": "B16-claude-lead",
    "gap_id": "G-R-MISMATCH", "attempt_id": "B16-lead-1",
    "method": ("exact node-level sandwich of the retained-KL charge + tree telescoping; exhaustive n<=4 validation; "
               "exact rational majority node data with a rigorous kappa lower bound"),
    "mathematical_delta": ("Retained-KL tree charge Q_T is the entropy drop up to (3/ln2) of consumed influence for every tree, so ISOSPECTRAL (8.1) "
                           "is FEI-equivalent and tree-independent; Maj_n is a scalable bounded-H/I family on which the child-kappa charge Lambda_T/I "
                           "grows like (1/2)log2 n (evidence to n=513), also after skipping exact isospectral splits; A076 tribes spectrum and "
                           "A077 point-defect ledger confirmed."),
    "deliverable_status": ("PARTIAL: REPORT.md not saved because the subagent harness refused the write (tool error: subagents should return "
                           "findings as text, not write report files); the report content is in the coordinator's StructuredOutput and in "
                           "CLAIMS.json proof_source"),
    "mathematical_status": "B16-RETAINED-KL-SANDWICH@1 PROVED (author, review pending A092); B16-MAJORITY-LAMBDA-DIVERGENCE@1 EVIDENCE",
    "claim_versions_used": ["C005", "C018", "C019", "A076-STRUCTURED-SPECTRA@1", "A076-TRIBES-PAYMENT-DISCRIMINATION@1",
                            "A077-MULTISCALE-MINORITY-KL-LEDGER@1"],
    "claims_created_or_changed": ["B16-RETAINED-KL-SANDWICH@1", "B16-MAJORITY-LAMBDA-DIVERGENCE@1"],
    "source_artifacts": ["code/b16_sandwich.py", "code/write_records.py", "out/b16_sandwich_results.json", "out/stdout.txt", "out/MANIFEST.json"],
    "next_consumers": ["A076", "A077", "A078", "A079", "A080", "A092", "A090"],
    "next_action": ("f=Maj(x_1..x_{n-1},Tribes_{w,t}(y)): Lambda_T plus outside leaf certificates against I(f) over y-first, x-first and "
                    "interleaved orders, all influence included"),
    "stagnant_substantive_attempts": 0,
    "blockers": ["REPORT.md write refused by the subagent harness"],
    "packet_ids": ["B16-claude-lead"],
}
with open("PROGRESS.json", "w", encoding="utf-8") as fh:
    json.dump(progress, fh, indent=1)
pd = dict(progress)
pd["packet_ids"] = ["A076", "A077", "A078", "A079", "A080"]
with open("PACKET_DELTA.json", "w", encoding="utf-8") as fh:
    json.dump(pd, fh, indent=1)
man = {}
for p in ["CLAIMS.json", "PROGRESS.json", "PACKET_DELTA.json", "code/b16_sandwich.py", "code/write_records.py",
          "out/b16_sandwich_results.json", "out/stdout.txt", "out/stderr.txt"]:
    with open(p, "rb") as fh:
        b = fh.read()
    man[p] = {"bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}
with open("out/MANIFEST.json", "w", encoding="utf-8") as fh:
    json.dump(man, fh, indent=1)
for c in claims:
    print(c["claim_id"], c["statement_sha256"])
print(json.dumps(man, indent=0))
