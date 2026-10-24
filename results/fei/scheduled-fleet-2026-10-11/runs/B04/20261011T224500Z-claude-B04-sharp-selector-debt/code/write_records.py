# Writes CLAIMS.json, PROGRESS.json, PACKET_DELTA.json for the B04 lead run (statement_sha256 per protocol).
import json, hashlib, os
RUN = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
RID = os.path.basename(RUN)
def sha(st, hy):
    return hashlib.sha256(json.dumps({"statement": st, "hypotheses": hy}, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()
H0 = ["F(x,y)=g_x(y) with x a fresh uniform selector block of a>=0 bits independent of uniform data y in {0,1}^m",
      "g_b arbitrary Boolean (+-1) functions on the common data cube; no balance, orthogonality or disjointness",
      "entropy H(f)=sum_S fhat(S)^2 log2(1/fhat(S)^2); influence = physical edge disagreement probability; h2 binary entropy in bits"]
claims = []
def add(cid, st, hy, status, proof, deps, reviews, first, consumers):
    claims.append(dict(claim_id=cid, version=1, exact_statement=st, hypotheses=hy, statement_sha256=sha(st, hy),
                       contributors=["claude-B04-lead"], proof_source=proof, proof_dependencies=deps, review_records=reviews,
                       status=status, supersedes=None, refutes=[], first_unproved_line=first, next_consumers=consumers))
S1 = ("For every multiplexer F(x,y)=g_x(y) with a selector bits, Delta:=H(F)-2^{-a} sum_b H(g_b) satisfies Delta=M_W+B_W with "
      "0<=M_W<=min(a,(2/ln2) I_sel(F)) and 0<=B_W<=a*h2(I_sel(F)/a) (h2(0)=0; for a=0 both sides vanish). Hence "
      "Delta<=min(a,(2/ln2) I_sel)+a*h2(I_sel/a)<=I_sel*log2(e^3 a/I_sel). Here M_W=a-sum_T R_T H(r_T), B_W=sum_T R_T H(nu_T)=H(S_sel|S_data) "
      "as in threshold paper Prop. 8.6 eq. (75).")
add("B04-SEL-LOG-SHARP", S1, H0, "PROVED_AUTHOR_INDEPENDENT_REVIEW_PENDING",
    "REPORT.md sec. 3.1 (identity = threshold Prop 8.6 (75); M_W via hypercube log-Sobolev; B_W via subadditivity + concavity of h2); out/verify_results.json P1-P3",
    ["threshold_paper_38pp Prop 8.6 eq (75),(79)", "Gross/Bonami log-Sobolev on {0,1}^a (independently re-proved from the two-point inequality in A018 REPORT sec. 2)"],
    [{"reviewer": "A018", "scope": "part M_W<=(2/ln2)I_sel only", "verdict": "independent derivation by a different route agrees", "independent": True},
     {"reviewer": "claude-B04-lead", "verdict": "exhaustive exact-Walsh checks a=1 m<=3, a=2 m<=2 (131,600 multiplexers), 0 violations", "independent": False}],
    None, ["A018", "A020", "A090", "A091", "B06", "C019"])
S2 = ("For even m>=2 let g_0(y)=(-1)^{y1y2+...+y_{m-1}y_m} and g_1=g_0 with the value at y=0 flipped; F(x,y)=g_x(y) (a=1). With u=2^{-m/2}: "
      "I_sel=2^{-m}=u^2 exactly and Delta=m u^2+A+B where A=-2 sum_{e=+-1} w_e (1-e u)^2 log2(1-e u), B=sum_e w_e (1-2eu)^2 log2|1-2eu|, w_e=(1+eu)/2. "
      "Consequently Delta=I_sel(m+3/ln2)-(19/(6 ln2)) I_sel^2+O(I_sel^3) and [(2/ln2)I_sel+h2(I_sel)]-Delta=(8/(3 ln2)) I_sel^2+O(I_sel^3)>0. "
      "For the t-fold tensor power (a=t selector bits, tm data bits) Delta, I_sel and the B04-SEL-LOG-SHARP bound are t times the one-bit values. "
      "Hence for every eps>0 no function psi with psi(s,a)<=(2/ln2)s+a h2(s/a)-eps s bounds Delta over all multiplexers.")
add("B04-BENT-SPLICE-SHARP", S2, H0 + ["m even, inner-product bent core, one flipped point"], "PROVED_AUTHOR_INDEPENDENT_REVIEW_PENDING",
    "REPORT.md sec. 3.2 closed form; out/verify_results.json P4 (certified mpmath intervals m=2..12, tensor squares m=2,4) and P4_symbolic (sympy series)",
    ["B04-SEL-LOG-SHARP"], [{"reviewer": "claude-B04-lead", "verdict": "closed form inside certified enclosure at m=2,4,6,8,10,12; series coefficients exact", "independent": False}],
    None, ["A016", "A017", "A019", "A020", "B05"])
S3 = ("If I_sel(F)>=c*a for some 0<c<=1 and H(g_b)<=C*I(g_b) for every b, then H(F)<=max(C,K_c)*I(F) with K_c=min(1/c,2/ln2)+h2(c)/c. "
      "K_c<=2/c for all c in (0,1] with equality only at c=1/2, and K_c=log2(1/c)+3/ln2+o(1) as c->0.")
add("B04-LOWSEL-LOG-CLOSURE", S3, H0, "PROVED_AUTHOR_INDEPENDENT_REVIEW_PENDING",
    "REPORT.md sec. 3.3 (B04-SEL-LOG-SHARP + I_data(F)=avg I(g_b), threshold eq. (77))", ["B04-SEL-LOG-SHARP"],
    [], None, ["A019", "A020", "A090"])
S4 = ("For every Boolean f on n>=1 coordinates and every coordinate i, with D_i=(f|_{x_i=0}-f|_{x_i=1})/2 on the other n-1 coordinates: "
      "Delta_i H:=H(f)-(H(f|_{x_i=0})+H(f|_{x_i=1}))/2 <= (3/ln2) Inf_i(f) + 2 I(D_i), where I(D_i)=sum_{S contains i}(|S|-1) fhat(S)^2. "
      "The bound is first-order sharp: on the bent splice of B04-BENT-SPLICE-SHARP, Delta/bound -> 1.")
add("B04-NODE-BOUNDARY", S4, ["f Boolean +-1 on the uniform cube", "entropy in bits; physical influence"], "PROVED_AUTHOR_INDEPENDENT_REVIEW_PENDING",
    "REPORT.md sec. 3.4 (a=1 case of B04-SEL-LOG-SHARP, h2(d)<=d log2(e/d), edge-isoperimetric inequality of Harper/Hart on the disagreement set); out/verify2_results.json",
    ["B04-SEL-LOG-SHARP", "edge-isoperimetric inequality: e(S)<=(1/2)|S|log2|S| on the m-cube"],
    [{"reviewer": "claude-B04-lead", "verdict": "all 65,836 Boolean f on n<=4 and every i: 0 violations; bent splice ratio 0.99999982 at m=20", "independent": False}],
    None, ["A019", "A020", "B06", "C019"])
S5 = ("For every Boolean f: H(f) <= sum_S (|S|^2+(3/ln2-1)|S|) fhat(S)^2. Equivalently, summing B04-NODE-BOUNDARY along any fixed coordinate order, "
      "the expected node charges sum exactly to 2 sum_S C(|S|,2) fhat(S)^2.")
add("B04-SECOND-MOMENT-PRICE", S5, ["f Boolean +-1 on the uniform cube"], "PROVED_AUTHOR_NO_NOVELTY_CLAIM",
    "REPORT.md sec. 3.5", ["B04-NODE-BOUNDARY"], [{"reviewer": "claude-B04-lead", "verdict": "all Boolean f on n<=4: 0 violations", "independent": False}],
    None, ["B06", "C019", "A020"])
json.dump({"claims": claims}, open(os.path.join(RUN, 'CLAIMS.json'), 'w', encoding='utf8'), indent=1)
prog = {
 "protocol_revision": "2026-10-11-execution-v2", "run_id": RID, "stream": "B04", "packet_id": "A019", "gap_id": "G-LOWSEL-COLLISION",
 "attempt_id": "claude-B04-lead-1", "method": "spectral decomposition Delta=M_W+B_W (threshold Prop 8.6); log-Sobolev; max-entropy; exact bent-splice asymptotics; edge-isoperimetry; exact Walsh enumeration and certified intervals",
 "mathematical_delta": ("Selector-only collision debt priced exactly: Delta<=min(a,(2/ln2)I_sel)+a h2(I_sel/a)<=I_sel log2(e^3 a/I_sel) for every shared-data multiplexer, "
                        "first-order sharp including the constant 3/ln2 (tensor bent splices). Closure under I_sel>=ca improves from max(2/c,C) to max(C,log2(1/c)+O(1)). "
                        "One-bit node lemma Delta_i<=(3/ln2)Inf_i+2I(D_i) converts the log into a linear charge on the influence of the derivative, also first-order sharp; "
                        "along any fixed order those charges sum to the second moment. A018 and A019 claims checked."),
 "deliverable_status": "COMPLETE", "mathematical_status": "PROVED_AT_STATED_SCOPE_INDEPENDENT_REVIEW_PENDING; FEI OPEN",
 "claim_versions_used": ["A018-COLLISION-BLOCK-INTERFACE v1", "A019-RARE-TRANSLATION-COLLISION v1", "A017-QUADRATIC-REUSED-ADDRESSING-LEDGER v1", "A016-ADDRESSING-BASELINE-COST-LEDGER v1"],
 "claims_created_or_changed": [c["claim_id"] + " v1" for c in claims],
 "source_artifacts": ["REPORT.md", "CLAIMS.json", "code/verify.py", "code/verify2.py", "out/FROZEN_SPEC.json", "out/verify_results.json", "out/verify2_results.json"],
 "next_consumers": ["A016", "A017", "A018", "A019", "A020", "A090", "A091", "B06"],
 "next_action": ("Adaptive stopping-tree amortization: find a tree rule under which sum over nodes of pi_v * 2 I(D_v), counted only at nodes where the exact B_W exceeds K*I_W, "
                 "is <=K'*I(f); first test case majority/threshold restrictions where the h2 bound loses but exact B_W is small (reviewer A018/A090)."),
 "stagnant_substantive_attempts": 0, "blockers": [], "packet_ids": ["A019"]}
json.dump(prog, open(os.path.join(RUN, 'PROGRESS.json'), 'w', encoding='utf8'), indent=1)
pd = dict(prog); pd["packet_ids"] = ["A016", "A017", "A018", "A019", "A020"]
json.dump(pd, open(os.path.join(RUN, 'PACKET_DELTA.json'), 'w', encoding='utf8'), indent=1)
for c in claims: print(c["claim_id"], c["statement_sha256"])
