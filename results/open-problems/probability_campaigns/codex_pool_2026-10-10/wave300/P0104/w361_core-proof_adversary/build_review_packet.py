"""Build worker-owned review artifacts; publish only the explicitly named draft inbox."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def own_source(key):
    return {"source_id": "owner-own-work:w361:P0104:" + key,
            "url": "urn:owner-own-work:w361:p0104:" + key,
            "revision": "2026-10-10-draft-v1",
            "license": "owner-own-work (campaign proof audit; concept-only draft)",
            "excerpt": None}


def main():
    receipt = json.loads((ROOT / "COUNTEREXAMPLE_RECEIPT.json").read_text(encoding="utf-8"))
    kernel = json.loads((ROOT / "KERNEL_RECEIPT.json").read_text(encoding="utf-8"))
    assert receipt["conditional_covariance"] == "-5/121"
    assert kernel["missing_retention_factor_large_time_floor"] == "1/4"
    source_status = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
    source_status["intake_evidence"]["exact_primary_question_check"] = "VERIFIED in Section 3.1: Questions 13 and 15 are printed page 37 / PDF zero-based page 36 in the fetched November 8, 2015 version. The intake page 34/40 locators do not locate those questions in this version."
    source_status["intake_evidence"]["short_primary_quotes"] = ["If d = 2, show that chi = 1/3.", "For suitable d, show that chi > 0."]
    source_status["intake_evidence"]["quote_note"] = "chi transliterates the source's Greek symbol; these are short excerpts, not a complete hypothesis package"
    source_status["primary_sources_checked"][2]["checked"] = "Model definition, Section 3.1 equation (3.1), variance-scaling interpretations, and exact Questions 13/15"
    source_status["prior_searches"] = {"H_and_I_attempt_directories": "Targeted P0104 search in math/document files returned no match; no whole logs read",
                                         "owner_percolation_notes_and_research": "Targeted named-ID search returned no match; width-three solved memory was checked separately",
                                         "lean_ranked_list": "P0104 retains attempted_un; no formal theorem receipt was found or claimed"}
    source_status["new_draft_publication"] = {"submitted": False, "reviewed": False, "ingested": False, "retrievable": False}
    claims_path = ROOT / "CLAIMS.jsonl"
    claims = [json.loads(line) for line in claims_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    first = next(row for row in claims if row["id"] == "w361-C001")
    first["source"]["kind"] = "owner-own-work"
    first["independent_reviewer"] = "w362"
    first["review_state"] = "KEEP: w362-R001 in ~/brain_workers/w362/PEER_REVIEWS.jsonl"
    first["remaining_gap"] = "No infinite-lattice variance exponent follows; the discrete claim has an independent arithmetic check."
    first["status"] = "independently checked proof"
    additions = [
      {"id": "w361-C002", "statement": "On a square with four iid Exp(1) edges, the two upper-path edge costs have covariance -1/64 conditional on that path being strictly faster. The selected path is unique almost surely.", "assumptions": ["Four independent Exp(1) edge costs", "Two simple square paths between opposite corners"], "source": {"kind": "owner-own-work", "path": "INDEPENDENT_OBSTRUCTION.md, Tie-free control"}, "proof_or_counterexample": "Conditional joint density 2 exp(-2(x+y))(1+x+y); means 5/8 and product moment 3/8 give covariance -1/64.", "independent_reviewer": "w362; explicit verdict pending", "remaining_gap": "Independent check of the continuous control; no asymptotic conclusion.", "status": "proved special case"},
      {"id": "w361-C003", "statement": "For finite-graph iid Uniform[1,2] FPP, the clipped off-edge threshold a_e gives centered coordinate response h_a(U)=min(U,a)-a+a^2/2. For 0<=a<=b<=1, its covariance kernel is K(a,b)=a^2[b(2-b)/4-a/6]. With independent rate-one coordinate refresh, Var(T)=integral exp(-t) sum_e E K(a_e(eta),a_e(eta^t)) dt.", "assumptions": ["Finite connected graph and distinct fixed terminals", "Independent Uniform[1,2] edge weights", "Simple terminal paths", "Off-edge and edge refresh flags are independent; retention probability exp(-t)"], "source": {"kind": "owner-own-work", "path": "ATTEMPT.md, independent kernel and normalization derivations"}, "proof_or_counterexample": "Piecewise polynomial integral for K; conditional retained-edge coupling; finite orthogonal Hoeffding decomposition for the variance integral. KERNEL_RECEIPT.json verifies 81 rational threshold pairs and 5 independent binary-square coupling controls.", "independent_reviewer": "w362: INDEPENDENT_KERNEL_AUDIT.md independently reproduces kernel and retention factor; claim-specific verdict pending", "remaining_gap": "No quantitative lattice crossover bound is proved. Explicit claim-specific referee acceptance remains pending.", "status": "proved special case"},
      {"id": "w361-C004", "statement": "For the kernel in C003, H(t)=sum_e E K(a_e(eta),a_e(eta^t)) has a persistent first-order limit L=sum_e ||T_{e}||_2^2, and H(t)-L=sum_{|S|>=2}|S| exp(-(|S|-1)t)||T_S||_2^2. A full-kernel upper bound H(t)<=C n F(n^(1/3)t) for all t>=0 with integrable nonnegative F is impossible when L>0.", "assumptions": ["Same finite-product setting as C003", "Hoeffding projections T_S with averaging over each independent coordinate", "For the impossible-bound assertion, fixed n,C>0 and L>0"], "source": {"kind": "owner-own-work", "path": "ATTEMPT.md, first-order-corrected crossover"}, "proof_or_counterexample": "The finite spectral sum separates |S|=1 exactly. H>=L forces F(s)>=L/(Cn) for all s, contradicting integrability. Exact binary-square check has L=1/4, H(t)=1/4+(3/16)exp(-t)+(1/16)exp(-3t).", "independent_reviewer": "w362; requested review-update", "remaining_gap": "Referee check of the plateau correction and its use in the sufficient route; full exponent untouched.", "status": "proved special case"},
      {"id": "w361-C005", "statement": "In the Uniform[1,2] planar slice, the sufficient crossover inputs L_n<=C n^(2/3), H_n(t)-L_n<=C n F(n^(1/3)t) with integrable nonnegative F, and H_n(t)>=c n for 0<=t<=c' n^(-1/3), uniformly in n, would imply Var(T_n) is bounded above and below by positive constants times n^(2/3).", "assumptions": ["C003 variance identity", "All three quantitative crossover inputs hold with n-independent constants", "Integer n>=1"], "source": {"kind": "owner-own-work", "path": "ATTEMPT.md, correctly stated sufficient stronger route"}, "proof_or_counterexample": "Upper integral bound by substitution s=n^(1/3)t and separate L_n; lower bound c c' exp(-c') n^(2/3) on the persistence interval.", "independent_reviewer": "w362; pending", "remaining_gap": "All quantitative crossover inputs remain unproved; this is a conditional route, not a proof of those inputs.", "status": "sketch"}
    ]
    existing = {row["id"] for row in claims}
    claims += [row for row in additions if row["id"] not in existing]
    claims_path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in claims), encoding="utf-8")
    audit = {"review_id": "w361-A001", "author": "w360", "claim_id": "w360-C1", "verdict": "KEEP", "statement": "Exact finite-box reduction for edge weights in [1,2], all integer n>=1", "reason": "A direct path costs <=2n; leaving the box needs >=2n+1 edges each costing >=1; loops strictly increase cost; finite simple minimum exists.", "scope": "The supplied C1 proof only; no variance-exponent conclusion", "reviewer": "w361", "remaining_gap": "Later resampling proof and quantitative scaling inputs"}
    (ROOT / "AUDIT_VERDICTS.jsonl").write_text(json.dumps(audit) + "\n", encoding="utf-8")
    entries = [
      {"key": "selected-square", "namespace": "probability.first-passage-percolation", "logical_name": "selected-geodesic-costs-are-dependent-square-counterexample", "kind": "concept", "title": "Selected geodesic costs can be dependent", "statement": "INDEPENDENTLY CHECKED FINITE COUNTEREXAMPLE (w362-R001). On a square with four independent edge weights uniform on {1,2}, select the cheaper path between opposite corners, breaking ties toward the upper path. Conditional on upper selection, its two costs have covariance -5/121: the probability both equal 2 is 1/11, but the product of marginal probabilities is 16/121. The unconditional two selected costs have covariance -9/256. Their sum has variance 23/64; dropping covariance terms gives 55/128. Disjoint raw inputs therefore do not ensure independent costs after path selection. This is a finite obstruction, not a claim about planar fluctuation exponents.", "proof_text": None, "assumptions": ["Finite square graph with two two-edge terminal paths", "Four independent uniform {1,2} weights", "Upper path wins ties"], "domain": "probability theory", "source": own_source("selected-square")},
      {"key": "threshold-floor", "namespace": "probability.first-passage-percolation", "logical_name": "replacement-threshold-kernel-retention-factor-and-first-order-floor", "kind": "concept", "title": "Retention factor and persistent threshold covariance", "statement": "AUTHOR-DERIVED FINITE IDENTITY, explicit referee acceptance pending. On a finite connected graph with iid Uniform[1,2] edge weights and fixed terminals, define clipped off-edge thresholds a_e in [0,1] so that centered coordinate costs are min(U,a_e)-a_e+a_e^2/2 for U uniform on [0,1]. For a<=b, K(a,b)=a^2[b(2-b)/4-a/6], and K is symmetric. Under independent rate-one coordinate refresh, Var(T)=integral_0^infinity exp(-t)H(t)dt, where H(t)=sum_e E K(a_e(eta),a_e(eta^t)) and only off-edge coordinates are coupled inside H. Its limit is the first-order Hoeffding energy L, not generally zero. H(t)-L is the sum over |S|>=2 of |S|exp(-(|S|-1)t)||T_S||_2^2. A full-kernel integrable decay envelope for all t is impossible when L>0. No lattice exponent estimate is asserted.", "proof_text": None, "assumptions": ["Finite connected graph and distinct fixed terminals", "Simple paths and positive weights", "Independent Uniform[1,2] coordinates and independent refresh flags", "T_S denotes the orthogonal Hoeffding projection on coordinate set S"], "domain": "probability theory", "source": own_source("threshold-floor")},
      {"key": "open-crossover", "namespace": "probability.first-passage-percolation", "logical_name": "planar-fpp-first-order-separated-two-sided-noise-crossover-draft", "kind": "concept", "title": "Unproved crossover input for planar FPP", "statement": "UNPROVED SUFFICIENT INPUT, not a theorem about FPP. For iid Uniform[1,2] undirected nearest-neighbour Z^2 passage times from 0 to n e1, restrict to the exact finite box [-2n,2n]^2. Let H_n and L_n be the threshold kernel and its first-order floor from the finite-product identity. A sufficient route to variance of order n^(2/3) would prove, uniformly in integer n>=1: L_n<=C n^(2/3); H_n(t)-L_n<=C n F(n^(1/3)t) for all t>=0 with nonnegative integrable F; and H_n(t)>=c n for 0<=t<=c' n^(-1/3), for positive constants independent of n. Upper and lower integral bounds then follow by substitution and persistence. All quantitative inputs remain unproved. A qualitative chaos statement, a kernel value only at t=0, or an assumed variance-growth ratio does not supply them. Current full-target openness is UNKNOWN as of this draft.", "proof_text": None, "assumptions": ["Exact finite-box reduction for positive bounded edge weights", "The named normalized variance identity", "Quantitative inputs are a proposed proof obligation, not established hypotheses of the actual model"], "domain": "probability theory", "source": own_source("open-crossover")}
    ]
    bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w361", "bundle_slug": "p0104-adversary-selection-threshold-floor-20261010", "entries": entries,
              "relations": [{"from_key": "open-crossover", "to_key": "threshold-floor", "kind": "depends_on", "rationale": "The sufficient crossover bounds require the correctly normalized variance integral and separation of its persistent first-order floor."},
                            {"from_key": "selected-square", "to_key": "threshold-floor", "kind": "semantic_association", "rationale": "The finite selection counterexample prevents substituting independent selected segments for the derived joint refresh coupling in the threshold identity."}]}
    write_json(ROOT / "drafts" / "bundle_001.json", bundle)
    inbox = Path("~/math-brain-inbox/w361/bundle_001.json")
    inbox.parent.mkdir(parents=True, exist_ok=True)
    if inbox.exists():
        assert json.loads(inbox.read_text(encoding="utf-8")) == bundle, "Existing bundle differs; do not overwrite another artifact."
    else:
        part = inbox.with_suffix(".json.part")
        assert not part.exists(), "Existing partial bundle requires manual inspection."
        write_json(part, bundle)
        part.rename(inbox)
    source_status["new_draft_publication"]["submitted"] = True
    source_status["new_draft_publication"]["path"] = str(inbox)
    source_status["new_draft_publication"]["entry_reviews"] = {"selected-square": "KEEP w362-R001", "threshold-floor": "pending explicit referee acceptance", "open-crossover": "unproved input; pending route review"}
    write_json(ROOT / "SOURCE_STATUS.json", source_status)
    hooks = [
      {"id": "p0104-w361-01", "area": "math", "event": "stage-start", "cue": "A proof factors selected geodesic segment costs solely because their raw edge sets are disjoint", "fire_when": "The square's selected-cost product 16/121 is substituted for the actual joint probability 1/11", "silent_when": "The path is fixed independently of weights, or the selected conditional law is explicitly shown to factor", "text": "State the selection conditioning before factoring geodesic costs. Disjoint iid inputs can become dependent after minimization; verify a joint factorization or use the actual covariance/filtration argument.", "evidence": "INDEPENDENT_OBSTRUCTION.md; COUNTEREXAMPLE_RECEIPT.json; w362-R001; memory proof_steps_need_derived_joint_structure_2026_09_09", "proposer": "w361"},
      {"id": "p0104-w361-02", "area": "math", "event": "stage-start", "cue": "A refresh proof integrates the off-edge threshold covariance over infinite time or assumes its complete-resampling limit is zero", "fire_when": "H(t) is integrated without exp(-t), or an integrable envelope is imposed on full H with a positive first-order floor", "silent_when": "The integral uses resampling-probability dp, or exp(-t) is present and the first-order floor is separately handled", "text": "Check the retained-coordinate factor and first-order floor. In continuous refresh time Var(T)=integral exp(-t)H(t)dt; full H can stay positive after all other coordinates are refreshed. Subtract its first-order term before claiming decay.", "evidence": "ATTEMPT.md; KERNEL_RECEIPT.json (square floor 1/4, variance 23/64)", "proposer": "w361"}
    ]
    lines = [json.dumps(h, ensure_ascii=False) for h in hooks]
    assert all(len(h["text"]) <= 300 for h in hooks)
    proposal = ROOT / "hooks" / "math-w361.jsonl"
    proposal.parent.mkdir(parents=True, exist_ok=True)
    proposal.write_text("\n".join(lines) + "\n", encoding="utf-8")
    patch_path = ROOT / "patches" / "01_math_selection_threshold_hooks.diff"
    patch_path.parent.mkdir(parents=True, exist_ok=True)
    live = "primary_directive/hooks1000/proposals/math-w361.jsonl"
    patch_path.write_text("--- a/" + live + "\n+++ b/" + live + "\n@@ -0,0 +1,2 @@\n" + "".join("+" + line + "\n" for line in lines), encoding="utf-8")
    write_json(ROOT / "PROGRESS_EVENT.json", {"event": "P0104 w361: independent square obstruction KEEP; retention and first-order floor audit verified; three concept drafts submitted; exponent gap preserved", "agent": "w361", "row": "S1.5", "evidence": str(ROOT / "REPORT.md"), "state": "staged for reviewer; external progress-page writes excluded by worker-folder rule"})
    write_json(ROOT / "REVIEW_RECEIPT.json", {"counterexample": "independently checked: w362-R001", "kernel": "independent w362 derivation matches K and exp(-t); explicit claim acceptance pending", "first_order_floor": "author exact checks; referee verdict pending", "submitted": True, "reviewed": False, "ingested": False, "retrievable": False, "bundle": str(inbox), "formal_check": None, "full_target_proved": False})
    print(json.dumps({"claims": len(claims), "concept_entries_submitted": len(entries), "hooks_staged": len(hooks), "bundle": str(inbox), "full_target_proved": False}, indent=2))


if __name__ == "__main__":
    main()
