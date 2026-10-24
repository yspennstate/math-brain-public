"""Validate local draft artifacts and save exact source/workflow state."""
import json
import pathlib

root = pathlib.Path(__file__).resolve().parent
bundle = json.loads((root/"bundle_001.json").read_text(encoding="utf-8"))
allowed = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
assert bundle["spec"] == "mathbrain-draft-v1" and bundle["author_agent"] == "w550"
assert len(bundle["entries"]) == 6 and len(bundle["relations"]) == 7
keys = {e["key"] for e in bundle["entries"]}
assert len(keys) == len(bundle["entries"])
required = {"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
for e in bundle["entries"]:
    assert required.issubset(e)
    assert e["kind"] == "concept" and e["proof_text"] is None
    assert e["statement"].startswith("DRAFT CONCEPT") and e["assumptions"]
    assert e["source"]["license"].startswith("owner-own-work")
    assert {"source_id","url","revision","license"}.issubset(e["source"])
initial = json.loads((root/"store_lookup_initial.json").read_text(encoding="utf-8"))
old_nodes = [r for q in initial["queries"] for r in q["rows"]]
logical = {json.loads(r["metadata_json"])["logical_id"] for r in old_nodes}
for r in bundle["relations"]:
    assert r["from_key"] in keys and r["kind"] in allowed and r["rationale"].strip()
    if "to_key" in r:
        assert r["to_key"] in keys
    else:
        assert r["to_existing_logical"] in logical
assert not any(r["kind"]=="depends_on" for r in bundle["relations"])
validation = {"spec":"mathbrain-draft-v1", "entries":6, "relations":7, "all_new_nodes_concepts":True,
              "required_fields_valid":True, "allowed_relation_kinds":True,
              "cross_bundle_ends_found_read_only":2, "depends_on_acyclic":True,
              "mathematical_proof_certified_by_this_validation":False, "integrator_run":False}
(root/"bundle_validation.json").write_text(json.dumps(validation, indent=2), encoding="utf-8")

reviews = [
 {"claim_id":"w550-S1.2", "verdict":"KEEP", "reviewer":"w551", "path":"~/brain_workers/w551/CLAIMS.jsonl", "line":7,
  "status":"independently checked proof", "remaining_gap":"Abstract stationary fields only; not a microscopic Riesz Gibbs construction."},
 {"claim_id":"w550-S1.3", "verdict":"KEEP", "reviewer":"w551", "path":"~/brain_workers/w551/CLAIMS.jsonl", "line":8,
  "status":"independently checked proof", "remaining_gap":"No scale-relative comparison for the actual microscopic Riesz observable is established."}
]
source_status = {
 "target":"P0321", "title":"Existence of a hexatic phase for two-dimensional Riesz gases", "as_of":"2026-10-10",
 "current_openness":"UNKNOWN", "novelty_claim":False, "original_phase_problem_solved_by_this_work":False,
 "ranking":{"path":"~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/RANKING_2026-09-07.csv", "line":556, "tier":5, "dated_status":"unsolved", "date":"2026-09-07"},
 "primary_source":{"author":"Mathieu Lewin", "title":"Coulomb and Riesz gases: The known and the unknown", "arxiv":"2202.09240v2", "doi":"10.1063/5.0086835", "url":"https://arxiv.org/html/2202.09240v2", "revision_date_from_abstract":"2022-04-30", "locator":"VI.2, dimension-two discussion (intake: VI.B, PDF66-67)", "fully_quantified_existence_theorem_present":False},
 "recovered_source_question":"Prove or refute an intermediate two-dimensional repulsive Riesz-gas phase with rapid positional and slow sixfold orientational correlations. The source discusses s>2 and jellium s=0,1 as physical scenarios; it does not fix one exponent, Gibbs specification, observable, correlation rate or interval.",
 "working_formulation_is_our_strengthening":True,
 "source_theorem_hypothesis_comparison":{"theorem":"Lewin Theorem 47", "hypotheses":["d in {1,2}","s>d","real chemical potential","finite positive inverse temperature"], "conclusion":"Equilibrium states are translation invariant", "additional_1d_result":"Uniqueness and real analyticity for d=1,s>2 only", "missing_for_target":["Long-range d=2,s=0,1 are outside the theorem", "No geometric sixfold lower bound", "No process alpha-mixing estimate", "No nonempty common phase interval"]},
 "brain_source_records":[{"id":r["id"], "logical_id":json.loads(r["metadata_json"])["logical_id"], "claim_kind":json.loads(r["metadata_json"])["claim_kind"], "truth_status":json.loads(r["metadata_json"])["truth_status"], "statement_fidelity_reviewed":json.loads(r["metadata_json"])["statement_fidelity_reviewed"]} for r in old_nodes],
 "prior_work":{"source_card_path":"~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/brain_bundle_C006a05.json", "key":"at-p0321", "line":2338, "kind":"concept", "independent_review":"No independent review (as in original card)", "use":"One-point rotation averaging does not remove two-point order; toy angle fields do not identify a Riesz Gibbs law."},
 "bounded_literature_check":{"primary_pages":["https://arxiv.org/abs/2202.09240", "https://arxiv.org/html/2202.09240v2"], "queries":["hexatic Riesz gas rigorous proof 2025 2026 (arxiv)","two dimensional Coulomb gas hexatic phase rigorous (arxiv)"], "result":"No verified current existence theorem recovered. A bounded search does not prove openness; no solved/retired certificate is claimed."},
 "scar":{"slug":"perceptron_proof_open_gaps_fleet_2026_07_12", "use":"Keep the hardest unchecked proof piece explicit; finite successful checks are not a proof certificate."},
 "independent_derivation_saved_before_paired_proof":True, "independent_derivation":"INDEPENDENT_DERIVATION.md", "paired_proof":"~/brain_workers/w549/BRIDGE_PROOF.md", "paired_audit":"AUDIT_W549.md",
 "independent_review_receipts":reviews, "remaining_review":["Cox counterexample S1.4", "optional ergodic Gaussian-sign extension"], "reviewer_account_provenance":"not independently verified", "formal_check":"not run; no formal theorem/axiom receipt claimed"
}
(root/"SOURCE_STATUS.json").write_text(json.dumps(source_status, ensure_ascii=False, indent=2), encoding="utf-8")
workflow = {"author":"w550", "bundle_slug":bundle["bundle_slug"],
            "submitted":{"state":"prepared_locally", "local_path":str(root/"bundle_001.json"), "destination":"~/math-brain-inbox/w550/bundle_001.json"},
            "reviewed":{"state":"partial", "received":reviews, "pending":["w550-S1.4", "optional ergodic extension"]},
            "ingested":{"state":"not_ingested", "integrator_run":False},
            "retrievable":{"state":"not_measured_for_new_draft", "existing_context_receipt":"store_lookup_initial.json"},
            "helper":{"state":"measured_proposal", "patch":"patches/01_target_source_fallback.diff", "live_applied":False},
            "hook":{"state":"staged_locally", "path":"hook_proposals/math-w550.jsonl", "global_submitted":False}}
(root/"WORKFLOW_STATE.json").write_text(json.dumps(workflow, indent=2), encoding="utf-8")
for e in reviews:
    row = {"id":e["claim_id"]+"-referee-receipt", "claim_id":e["claim_id"], "kind":"independent_review_receipt",
           "statement":"The original abstract claim is independently kept; this does not solve P0321.",
           "assumptions":"Original claim assumptions preserved, including the model/observable/limit scope.",
           "source": {"path":e["path"],"line":e["line"]}, "proof_or_counterexample":"Independent referee reconstructed the original proof; see the exact verdict row.",
           "independent_reviewer":"w551", "remaining_gap":e["remaining_gap"], "status":e["status"], "workflow_state":"reviewed"}
    with (root/"CLAIMS.jsonl").open("a",encoding="utf-8") as out:
        out.write(json.dumps(row,ensure_ascii=False)+"\n")
print(json.dumps({"validation":validation, "independent_KEEP_receipts":2, "Cox_review":"pending"}))
