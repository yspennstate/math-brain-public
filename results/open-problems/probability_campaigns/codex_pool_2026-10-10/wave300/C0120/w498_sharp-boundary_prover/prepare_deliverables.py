"""Prepare scoped proposals; never change a live source record or a store."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w498").resolve()
INTAKE = Path("~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl")
PRIMARY = "https://arxiv.org/pdf/0810.4221v2"
now = datetime.now(timezone.utc).isoformat()


def save(name, value):
    (ROOT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def source(source_id, url=None):
    return {"source_id": source_id, "url": url, "revision": "author-proof-w498-2026-10-10-v1",
            "license": "owner-own-work (campaign comparison and proofs; independent audit pending)",
            "excerpt": None}


def entry(key, namespace, logical_name, title, statement, assumptions, reference):
    return {"key": key, "namespace": namespace, "logical_name": logical_name,
            "kind": "concept", "title": title,
            "statement": statement, "proof_text": None,
            "assumptions": assumptions, "domain": "probability theory", "source": reference}


def main():
    measurements = json.loads((ROOT / "MEASUREMENTS.json").read_text(encoding="utf-8"))
    if measurements["checks_passed"] != 12:
        raise ValueError("Expected all 12 bounded checks to pass")
    old_line = None
    with INTAKE.open(encoding="utf-8") as file:
        for line_number, line in enumerate(file, 1):
            if '"problem_id": "C0120"' in line:
                old_line = line.rstrip("\r\n")
                old_row = json.loads(old_line)
                break
    if old_line is None:
        raise ValueError("No C0120 source row; do not construct a blind patch")
    new_row = dict(old_row)
    new_row["statement"] = (
        "For iid N(0,1) vertex weights g_v on Z^2, let P_n be every up/right path of n visited vertices, "
        "starting at (0,0), including the origin, with free endpoint. Set M_n=max_{p in P_n} sum_{v in p} g_v. "
        "Improve the source's Var(M_n)<=C n/log n estimate to a power variance bound: find epsilon>0 and C'<infinity, "
        "independent of n, such that Var(M_n)<=C' n^(1-epsilon) for n>=2. The source asks to improve the fluctuation "
        "exponent; the inequality is the campaign's concrete formulation of that question."
    )
    new_row["status_search"] = (
        "Source-scope correction proposed 2026-10-10 by w498; current openness UNKNOWN. arXiv:0810.4221v2 "
        "Sections 1 and 8 concern a planar Gaussian ground-state maximum, not finite-temperature log Z_n or "
        "general disorder/dimension. Those broader extensions require separate sources. No solved/retired claim."
    )
    new_row["scope_correction"] = {"proposer": "w498", "review_state": "PENDING_W500",
                                   "primary_url": PRIMARY, "artifact": str(ROOT / "STATEMENT.md")}
    save("SOURCE_ROW_BEFORE.json", old_row)
    save("SOURCE_ROW_AFTER.json", new_row)
    new_line = json.dumps(new_row, ensure_ascii=False, sort_keys=True)
    patches = ROOT / "patches"
    patches.mkdir(exist_ok=True)
    live_path = INTAKE.as_posix()
    patch = (f"--- a/{live_path}\n+++ b/{live_path}\n"
             f"@@ -{line_number},1 +{line_number},1 @@\n-{old_line}\n+{new_line}\n")
    (patches / "01_c0120_source_scope.diff").write_text(patch, encoding="utf-8")
    # The proposed diff changes one row only; test against the scoped copy.
    removed = next(line[1:] for line in patch.splitlines() if line.startswith("-") and not line.startswith("---"))
    added = next(line[1:] for line in patch.splitlines() if line.startswith("+") and not line.startswith("+++"))
    assert json.loads(removed) == old_row
    assert json.loads(added) == new_row
    unchanged_fields = set(old_row) - {"statement", "status_search"}
    assert all(new_row[key] == old_row[key] for key in unchanged_fields)
    assert new_row["current_status"] == "unverified" and new_row["verification"] == "unreviewed"

    existing_logical = "math:probability.gaussian:open-problem-c0120-fluctuation-exponent-of-directed-polymers-beyond-the-logarithmic-impro"
    correction = {
        "state": "PROPOSED_NOT_APPLIED", "operation": "correct_source_scope_after_independent_KEEP",
        "existing_node_id": "claim_2b6b7c1da300a8ed1c28367cabd584f2c02769a03a64ed519cf081b1af04693d",
        "existing_node_digest": "sha256:578853e3b2073e0e1a4e864c29ebf3c5a2b0fa5b2a359fdbc9cc0d700aae250d",
        "existing_logical_id": existing_logical,
        "existing_statement_quote": old_row["statement"],
        "proposed_statement_quote": new_row["statement"],
        "source": {"url": PRIMARY, "locators": "Sections 1, 8, 12(3)",
                   "quote": "Improve the fluctuation exponent in directed polymers."},
        "reviewer": "w500", "mathematical_review": "PENDING",
        "guard": "Preserve current-status unverified; do not claim solved, general weights/dimension, or finite temperature without a separate source."
    }
    save("STORE_CORRECTION.json", correction)

    entries = [
        entry("c0120-scope", "probability.gaussian", "c0120-primary-ground-state-source-scope",
              "DRAFT: C0120 primary-source scope correction",
              "SOURCE CORRECTION, independent review pending. The cited Chatterjee 0810.4221v2 model has iid N(0,1) "
              "vertex weights on Z^2 and every up/right path of n visited vertices starting at the origin, with free "
              "endpoint. M_n is the maximum sum of those weights. Theorem 8.1 bounds Var(M_n) by C n/log n; Section "
              "12(3) asks to improve the fluctuation exponent. A concrete campaign objective is Var(M_n)<=C' n^(1-epsilon) "
              "for fixed epsilon>0 and all n>=2. The intake's finite-temperature log Z_n/general weights/general dimension "
              "wording is broader than this primary source. Current openness UNKNOWN; no solution claimed.",
              ["Historical source: 0810.4221v2, 2008-12-16; Sections 1, 8, 12(3)",
               "n counts vertices including the origin; endpoint free"],
              source("owner-campaign-w498:C0120-source-scope", PRIMARY)),
        entry("layer-average", "probability.gaussian", "layer-average-variance-decomposition-for-gaussian-path-functionals",
              "DRAFT author proof: Gaussian layer-average variance decomposition",
              "AUTHOR PROOF, independent review pending. Let a finite deterministic nonempty path family visit one site "
              "of each layer t, containing m_t independent N(0,sigma_t^2) variables, with independent layers. Set A_t to "
              "the layer average and R[t,x]=g[t,x]-A_t. For M=max_p sum_t g[t,p_t], "
              "Var(M)=sum_t sigma_t^2/m_t+Var(M(R)). For F_beta=log(sum_p a_p exp(beta sum_t g[t,p_t])), "
              "where a_p>0 are deterministic and beta is finite, Var(F_beta)=beta^2 sum_t sigma_t^2/m_t+Var(F_beta(R)). "
              "In the unrestricted planar n-vertex unit-Gaussian model, Var(M_n)>=H_n=sum_{j=1}^n 1/j. Proof packet: "
              "ATTEMPT.md L1; novelty unverified. No residual-variance upper bound is asserted.",
              ["Finite deterministic path family and finite layer sets", "One visited site per layer per path",
               "Independent centered Gaussian variables; variance constant within each layer", "Deterministic positive a_p for F_beta"],
              source("owner-campaign-w498:C0120-layer-average")),
        entry("strip-variance", "probability.polymers", "exact-ground-state-variance-in-width-one-gaussian-diagonal-strip",
              "DRAFT author proof: exact Gaussian strip variance",
              "AUTHOR PROOF, independent review pending. For r>=1, iid N(0,1) vertex weights and all up/right paths "
              "from (0,0) to (r,r) restricted to |x-y|<=1, counting N=2r+1 vertices including both endpoints, "
              "M_r^strip=sum_{k=0}^r G_k+sum_{k=0}^{r-1} max(X_k,Y_k), with all G_k,X_k,Y_k independent standard "
              "normals. E M_r^strip=r/sqrt(pi), Var(M_r^strip)=(2-1/pi)r+1, and the variance per visited vertex "
              "tends to 1-1/(2pi)>0. The r+1 G_k are the forced diagonal junction weights. This restricted, fixed-endpoint "
              "model does not decide the unrestricted, free-endpoint C0120 target. Proof packet: ATTEMPT.md L2; novelty unverified.",
              ["r>=1 integer; width-one strip and endpoint (r,r)", "iid standard Gaussian vertex weights",
               "All allowed nearest-neighbor up/right paths; both endpoints counted"],
              source("owner-campaign-w498:C0120-strip-variance")),
        entry("noise-separation", "probability.polymers", "gaussian-strip-path-instability-with-asymptotically-full-overlap",
              "DRAFT author proof: path instability with overlap near one",
              "AUTHOR PROOF, independent review pending. In the width-one Gaussian strip from (0,0) to (r,r), "
              "perturb weights by g^s=e^(-s)g+sqrt(1-e^(-2s))g', with independent iid standard Gaussian g'. "
              "The number B_r(s) of different diamond choices is Binomial(r,q(s)), where q(s)=arccos(e^(-s))/pi. "
              "P(P_r(g)=P_r(g^s))=(1-q(s))^r and E|P_r(g) intersect P_r(g^s)|/(2r+1)=1-rq(s)/(2r+1). "
              "For s=r^(-alpha), 0<alpha<2, identical-path probability tends to zero, while normalized expected overlap "
              "tends to one and Var(M_r^strip)=(2-1/pi)r+1 stays linear. Block independence is unconditional because "
              "the vertex sets are disjoint. This is a restricted-model boundary example, not a refutation of C0120. "
              "Proof packet: ATTEMPT.md L3; novelty unverified.",
              ["Width-one strip with fixed endpoint (r,r), r>=1", "Original and copied environments iid standard Gaussian",
               "All N=2r+1 vertices, including endpoints", "0<alpha<2 for the asymptotic assertion"],
              source("owner-campaign-w498:C0120-noise-separation")),
        entry("bad-bridge", "probability.polymers", "refuted-path-change-alone-implies-power-variance-bridge",
              "DRAFT route warning: maximizer change alone does not give a power variance bound",
              "REFUTED AUXILIARY BRIDGE, author proof pending independent review: for all deterministic Gaussian "
              "nearest-neighbor layered path families with N vertices per path, the premise that a unique maximizing "
              "path changes with probability tending to one under polynomially small OU noise would, by itself, imply "
              "Var(M_N)<=C N^(1-epsilon) for some fixed epsilon>0. The width-one diagonal strip disproves this proposed "
              "implication: path equality tends to zero but its maximum has linear variance. A hypothesis on normalized "
              "common-vertex overlap is different. No counterexample is asserted for a bridge with an additional O(N/log N) "
              "variance premise, for the correctly quantified overlap-chaos implication, or for unrestricted C0120.",
              ["The refuted implication uses path change alone", "No additional logarithmic variance baseline premise"],
              source("owner-campaign-w498:C0120-refuted-weak-bridge")),
        entry("residual-gap", "probability.polymers", "c0120-unrestricted-planar-residual-variance-gap",
              "DRAFT attempt gap: unrestricted planar residual variance",
              "UNRESOLVED GAP. In the unrestricted planar iid standard Gaussian n-vertex ground-state model, remove "
              "the independent average on each diagonal layer to obtain R. The layer-average identity gives "
              "Var(M_n)=H_n+Var(M_n(R)). The current packet supplies no power upper bound on Var(M_n(R)) and no "
              "polynomial upper bound on expected common-vertex overlap under small OU noise. Either would require "
              "a new argument beyond the exact strip counterexample. Current openness UNKNOWN; the parent target is not solved.",
              ["Unrestricted up/right planar paths starting at the origin", "n vertices including origin; endpoint free",
               "iid N(0,1) weights; R subtracts each diagonal layer average"],
              source("owner-campaign-w498:C0120-residual-gap")),
    ]
    relations = [
        {"from_key": "c0120-scope", "to_existing_logical": existing_logical, "kind": "cites",
         "rationale": "Exact existing card is the subject of the proposed source-scope correction; its log Z_n wording is not promoted to a primary-source theorem."},
        {"from_key": "strip-variance", "to_key": "layer-average", "kind": "specializes",
         "rationale": "Strip has r+1 one-site layers and r two-site layers. The layer-average contribution is 3r/2+1; its residual variance is r(1/2-1/pi), summing to (2-1/pi)r+1."},
        {"from_key": "noise-separation", "to_key": "strip-variance", "kind": "depends_on",
         "rationale": "Uses the same r independent diamond choices and r+1 forced junctions, and the exact linear variance from the strip result."},
        {"from_key": "noise-separation", "to_key": "bad-bridge", "kind": "refutes",
         "rationale": "P(same path)=(1-q)^r tends to zero for polynomial OU noise, but the exact variance is (2-1/pi)r+1. This disproves the universally quantified path-change-alone implication."},
        {"from_key": "residual-gap", "to_key": "layer-average", "kind": "depends_on",
         "rationale": "The explicit decomposition identifies H_n plus residual variance; it provides no upper bound on that residual."},
        {"from_key": "noise-separation", "to_key": "c0120-scope", "kind": "analogous_to",
         "rationale": "Shares Gaussian up/right geometry and OU noise but restricts width and endpoint; these distinctions prevent claiming a refutation of the original target."},
    ]
    bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w498", "bundle_slug": "c0120-sharp-boundary-w498-001",
              "entries": entries, "relations": relations}
    save("bundle_001.json", bundle)
    # All concepts, no theorem/lemma promotion and no integration call.
    allowed = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
    keys = {item["key"] for item in entries}
    assert len(keys) == len(entries) == 6
    assert all(item["kind"] == "concept" and item["proof_text"] is None for item in entries)
    assert all(item["source"]["license"].startswith("owner-own-work") for item in entries)
    assert all(rel["from_key"] in keys and rel["kind"] in allowed and
               (rel.get("to_key") in keys or rel.get("to_existing_logical") == existing_logical) for rel in relations)
    INBOX.mkdir(parents=True, exist_ok=True)
    final = INBOX / "bundle_001.json"
    part = INBOX / "bundle_001.json.part"
    assert final.resolve().parent == INBOX and part.resolve().parent == INBOX
    bundle_text = (ROOT / "bundle_001.json").read_text(encoding="utf-8")
    if final.exists():
        if final.read_text(encoding="utf-8") != bundle_text:
            raise FileExistsError("Preserve existing inbox artifact; create a new bundle revision instead")
    else:
        part.write_text(bundle_text, encoding="utf-8")
        assert json.loads(part.read_text(encoding="utf-8")) == bundle
        part.rename(final)

    hook = {"id": "math-w498-01", "area": "math", "event": "stage-start",
            "cue": "A polymer argument treats a change of maximizer alone as sufficient for overlap chaos or a power variance gain",
            "fire_when": "An argument infers a polynomial variance gain solely because the maximizing Gaussian path changes under polynomially small noise",
            "silent_when": "The argument bounds normalized expected common-vertex overlap, or reports path change without claiming a variance gain",
            "text": "Check common-vertex overlap at the claimed noise scale. In the width-one Gaussian strip, paths change with high probability under polynomially small noise while overlap tends to one and variance stays linear. Path change alone cannot supply the chaos input.",
            "evidence": str(ROOT / "ATTEMPT.md") + " L2-L3; " + str(ROOT / "MEASUREMENTS.json"), "proposer": "w498"}
    assert len(hook["text"]) <= 300
    save("HOOK_PROPOSAL.json", hook)
    hook_path = Path("~/primary_directive/hooks1000/proposals/math-w498.jsonl")
    existing_ids = set()
    if hook_path.exists():
        for line in hook_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                existing_ids.add(json.loads(line)["id"])
    if hook["id"] not in existing_ids:
        with hook_path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(hook, ensure_ascii=False) + "\n")

    delivery = {"prepared": {"at": now, "file": str(ROOT / "bundle_001.json")},
                "submitted": {"at": now, "file": str(final), "entries": 6, "relations": len(relations)},
                "reviewed": {"state": "PENDING", "reviewer": "w500", "response_side_model_evidence": None},
                "ingested": {"state": "NOT_PERFORMED"}, "retrievable": {"state": "NOT_VERIFIED"},
                "promotion_guard": "All entries are DRAFT concepts; no parent solved claim, no live store writes, no global recall change, no integrator invocation."}
    save("BRAIN_DELIVERY.json", delivery)
    status = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
    status["store_export_check"] = {
        "path": "~/math-brain-build/export/population/nodes.jsonl",
        "target_rows": [1592, 4324],
        "finding": "Existing unverified C0120 problem and author-only attempt repeat the broad log Z_n wording; no solved status is present in these exact records.",
        "scope": "Targeted records only, not a whole-store audit"}
    status["statement_sent_first"] = {"to": "w499", "mesh_message_id": "msg-f8dabe53c9"}
    status["proof_packet_requested_review"] = {"to": "w500", "mesh_message_id": "msg-3d53002dcf"}
    status["draft_bundle"] = str(final)
    save("SOURCE_STATUS.json", status)

    row = measurements["formula_rows"][1]
    report = (
        "C0120's cited paper concerns a planar Gaussian ground-state maximum; the stored intake broadened it to log Z_n, "
        "general weights and general dimension. The proposed one-row correction and STORE_CORRECTION.json restore the source scope "
        "without changing unverified/open-status fields.\n\n"
        "Proved special cases, awaiting w500: exact layer-average variance decomposition, exact width-one strip variance, "
        "and a counterexample to a path-change-alone variance bridge. In a strip of r diamonds, Var(M)=(2-1/pi)r+1. "
        "At OU time r^(-alpha), 0<alpha<2, paths change with probability tending to one while normalized overlap tends to one. "
        "The unrestricted parent problem remains unresolved, and current openness/novelty are unverified.\n\n"
        f"Measured with run_bounded_verification.py: {measurements['checks_passed']} deterministic checks passed; "
        f"maximum geometry error {measurements['maximum_geometry_error']:.3g}; independent overlap-integral/moment variance discrepancy "
        f"{measurements['overlap_integral_variance_error']:.3g}. For r=10000 and OU time 0.0001, identical-path probability is "
        f"{row['identical_path_probability']:.6g}, normalized expected overlap {row['expected_normalized_overlap']:.9f}, "
        f"and variance {row['exact_variance']:.9f}. These evaluate proved formulas; they are not independent proof audits.\n\n"
        "Before: one C0120 store concept has an unsupported source scope and a qualitative decorrelation bridge. "
        "Prepared after: one correction patch, five scoped claim rows, six DRAFT concept entries and six justified relations. "
        "Submitted is separate from reviewed, ingested and retrievable; no live change or theorem promotion occurred. "
        "The hook proposal math-w498-01 has a specific fire and silent case.\n\n"
        "Apply after independent KEEP: apply patches/01_c0120_source_scope.diff to the live problems.jsonl path named in its header, "
        "or replace only its C0120 row with SOURCE_ROW_AFTER.json; the validating integrator handles STORE_CORRECTION.json and the draft.\n\n"
        "Risks: strip and endpoint restrictions cannot be transferred to the unrestricted model by variance monotonicity; "
        "a bridge that additionally assumes O(N/log N) variance is not refuted. Requested models do not prove served identity. "
        "No Lean/formal-check receipt is claimed.\n\n"
        "NEXT: w500 checks L1-L3 and source scope; the next proof step is a polynomial upper bound on the unrestricted centered maximum's variance, "
        "with H_n retained as its exact independent layer-average contribution.\n"
    )
    (ROOT / "REPORT.md").write_text(report, encoding="utf-8")
    artifacts = ["STATEMENT.md", "ATTEMPT.md", "CLAIMS.jsonl", "SOURCE_STATUS.json", "REVIEW_REQUEST.md",
                 "MEASUREMENTS.json", "COMPUTE_GATE.json", "STORE_CORRECTION.json", "bundle_001.json",
                 "BRAIN_DELIVERY.json", "REPORT.md", "patches/01_c0120_source_scope.diff"]
    hashes = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in artifacts}
    save("REVIEW_PACKET.json", {"packet_id": "w498-C0120-boundary-v1", "frozen_at": now,
                                "artifact_sha256": hashes,
                                "mathematical_claims": ["w498-C0120-L1", "w498-C0120-S0", "w498-C0120-L1M", "w498-C0120-L2", "w498-C0120-L3"],
                                "author_review_status": "AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW",
                                "author_response_side_served_model_evidence": None,
                                "independent_reviewer": "w500", "independent_review_of_referee_new_results": "w503",
                                "hardest_gap": "Polynomial upper bound on Var(M_n(R)) in unrestricted planar Gaussian model",
                                "parent_problem_solved": False, "novelty": "UNVERIFIED",
                                "numerical_or_source_hash_checks_are_not_proofs": True,
                                "formal_check_receipt": None})
    print(json.dumps({"inbox_file": str(final), "entries": len(entries), "relations": len(relations),
                      "claims": 5, "source_row": line_number, "hook_file": str(hook_path),
                      "attempt_sha256": hashes["ATTEMPT.md"], "bundle_sha256": hashes["bundle_001.json"],
                      "review_packet": str(ROOT / "REVIEW_PACKET.json")}, indent=2))


if __name__ == "__main__":
    main()
