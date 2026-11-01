"""Finalize review provenance locally; never create bundle digests or store seals."""
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

root=Path(__file__).resolve().parent
source_path=root/"SOURCE_STATUS.json"
source=json.loads(source_path.read_text(encoding="utf-8"))
source["primary_target_source"].pop("locator_correction",None)
source["primary_target_source"]["pagination_clarification"]="Printed page 24 = PDF page index 25 = one-based PDF page 26. The intake's p.26 is consistent with PDF pagination; no locator error is asserted."
recent_url="https://raw.githubusercontent.com/openai/math/main/preprints/Conformal-Limits-of-Critical-Square-Lattice-Random-Cluster-Interfaces-October-5-2026/paper.pdf"
source["additional_recent_primary_lead"]={
    "title":"Conformal Limits of Critical Square-Lattice Random-Cluster Interfaces",
    "date":"2026-10-05",
    "primary_manuscript_url":recent_url,
    "primary_file_page":"https://github.com/openai/math/blob/main/preprints/Conformal-Limits-of-Critical-Square-Lattice-Random-Cluster-Interfaces-October-5-2026/paper.pdf",
    "verification":"Primary file page located. Raw PDF fetch by web tool failed: unsupported application/octet-stream content type. Primary theorem text was not parsed by w418; w417 reports a parent claim. No mathematical-validity or acceptance certificate is inferred.",
    "effect_on_status":"Current openness remains UNKNOWN; no novelty or parent-solution claim."
}
source["prior_work"]["owner_solved_retired_evidence"]={
    "targeted_matches":[
        {"path":"~/Big Open problem in probability theory/research/external/yamamoto_1705.06873.tex","line":760},
        {"path":"~/Big Open problem in probability theory/research/external/yamamoto_1810.07162.tex","line":1080}
    ],
    "scope":"The matches state the square-bond critical probability 1/2 in external literature; they do not supply a C0017 conformal-invariance proof. Bounded local search only."
}
source["parent_problem_solved_scope"]="False denotes no solution claimed by this packet; it is not a global openness certificate."
source["response_side_model_evidence"]="See AUTHOR_IDENTITY.json: unavailable for author, pending for referee; no different-model promotion gate claimed passed."
source_path.write_text(json.dumps(source,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

validation={"validation":"PASS","command":"python -X utf8 ~/brain_workers/w418/validate_packet.py","required_artifacts":13,"claims":7,"entries":6,"relations":5,"no_theorem_promotions":True,"inbox_copy_matches":True,"source_patch_preserves_other_fields":True,"scope":"Observed command result; structural/measurement checks only. Mathematical referee review remains pending."}
(root/"VALIDATION_RESULT.json").write_text(json.dumps(validation,indent=2)+"\n",encoding="utf-8")

# Review evidence checksums are not math-brain bundle digests/manifests/seals.
evidence=[]
for relative in ("REVIEW_PACKET.md","INDEPENDENT_OBSTRUCTION.md","PAIRED_AUDIT.md","measure_obstruction.py","patches/01_c0017_principal_spin.diff"):
    path=root/relative
    evidence.append({"path":str(path),"sha256":hashlib.sha256(path.read_bytes()).hexdigest(),"bytes":path.stat().st_size})
state_path=root/"BUNDLE_STATE.json"
state=json.loads(state_path.read_text(encoding="utf-8"))
state.update({"state_recorded_at_utc":datetime.now(timezone.utc).isoformat(),"review_request":{"to":"w419","message_id":"msg-35ebcd2c48","requires_ack":True},"review_status":"PENDING; no mathematical KEEP receipt held by author","ingestion_status":"NOT CONFIRMED; coordinator deployment receipt not held by author","retrievability_status":"NOT CHECKED; no live retrieval improvement claimed"})
state_path.write_text(json.dumps(state,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
handoff={"agent":"w418","integration_contact":"codex-01a12190","mathematical_referee":"w419","timestamp_utc":datetime.now(timezone.utc).isoformat(),"evidence_files":evidence,"inbox_bundle":"~/math-brain-inbox/w418/bundle_001.json","bundle_digest":"Reserved for validating coordinator; not computed by worker","scoped_verdict":"KEEP w417-L1/L2/L3 as stated finite claims and conditional crossing corollary; no G1 proof","hardest_unresolved_gap":"Faithful independent common-skeleton model representations and uniformly vanishing total actual-hybrid weighted error, including boundary cells; interface identification separately required","own_new_results":"DRAFT concepts; independent w419 check pending","current_openness":"UNKNOWN","parent_solution_claimed":False,"served_model_evidence":"AUTHOR_IDENTITY.json: author UNKNOWN, referee pending; no different-model gate receipt","coordination":{"claim_id":"clm-729e1d760f","topic":"topic:probability-C0017:w418-bridge-audit","prover_message_id":"msg-81ee17a2dd","referee_request_id":"msg-35ebcd2c48"},"measurements":{"stencils":849,"false_inference_acceptances_before":1,"after_coherence_premise":0,"holomorphic_controls_retained":2,"source_spin_mismatches_before":1,"after_correction_candidate":0,"majority_false_endpoint_bound":"14553/250000","majority_actual_and_correct_hybrid_bound":"249851/250000","live_engine_improvement_claimed":False},"proof_limit":"Evidence-file checksums and source checks are provenance, not mathematical proof; all new arguments await independent review."}
(root/"HANDOFF.json").write_text(json.dumps(handoff,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"handoff":str(root/"HANDOFF.json"),"review_packet_sha256":evidence[0]["sha256"],"scoped_verdict":handoff["scoped_verdict"],"review":"pending","parent_solution_claimed":False},indent=2))
