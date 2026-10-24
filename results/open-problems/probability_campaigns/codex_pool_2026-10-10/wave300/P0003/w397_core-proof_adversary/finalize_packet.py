"""Save the completed mathematical audit and its length-preserving draft addendum."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
source_status = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
snapshot = json.loads((root / "review_packet/w396_snapshot_receipt.json").read_text(encoding="utf-8"))
source_status["hardest_missing_input"] = "H_disk: at the explicitly chosen scale s_n=n^(-3/4), limsup_n of the uniform exact-length-n probability of avoiding a fixed disk but entering its epsilon collar is at most C(z,r)*epsilon^alpha. This remains unproved."
source_status["other_unproved_inputs"] = ["H_len: SLE identification from length-resolved continuation kernels", "Ordered-curve tightness and simplicity", "Scale, continuum geometry and stopping conventions", "Related chordal H_5/8 asymptotics and ensemble transfer", "Genuine observable regularity suppressing circulation modes"]
source_status["independence"]["paired_full_proof_audit"] = {"verdict": "KEEP finite/conditional L0,L0prime,L1,L2,L3 under(C), and first-entrance injection(U); full P0003 unproved", "artifact": "REVIEW_w396_proof.md", "snapshot_receipt": "review_packet/w396_snapshot_receipt.json", "snapshot_sha256": snapshot["sha256"]}

rows = [
    {"id": "w397.P0003.002.audit", "target": "P0003", "statement": "The corrected paired packet's L0/L0prime/L1/L2 are valid finite path-law statements, L3 is valid under clearance condition(C), and(U) is a valid first-entrance counting upper bound.", "assumptions": ["Positive inherited finite simple-path weights", "Exact remaining length for the fixed-length ensemble", "Nested obstacle events and terminal-aware filtration", "For L3: compact trace weak convergence, positive limiting avoidance mass and the stated collar-ratio condition(C)"], "source": {"kind": "owner-own-work", "originator": "w396", "artifact": "review_packet/w396_ATTEMPT_snapshot.md", "source_snapshot_receipt": "review_packet/w396_snapshot_receipt.json"}, "proof_or_counterexample": "Independent mathematical checks in REVIEW_w396_proof.md; length-preserving completion bijection, bounded stopping, nested-event total variation, continuous-clearance cutoffs and first-entrance injection.", "independent_reviewer": "w397; w398 independently kept L0-L3 in REVIEW_w396.md. Referee check of the newest L0prime/(U) packet remains separate.", "remaining_gap": "H_disk, H_len, ordered-curve tightness, scale/continuum conventions and related H_5/8 are unproved. LSW uniqueness citation needs Lemma3.2 plus Theorem6.1.", "status": "proved special case", "claim_type": "mathematical_audit", "landing_state": "draft"},
    {"id": "w397.P0003.005", "target": "P0003", "statement": "A small absolute avoidance-martingale difference does not imply small relative error without a lower bound on the conditioning probability.", "assumptions": ["Three simple paths a-u-k-b,a-u-c-b,a-v-b have weights epsilon,1-epsilon,1", "0<epsilon<1", "A={c},B={c,k}"], "source": {"kind": "owner-own-work", "artifact": "REVIEW_w396_proof.md"}, "proof_or_counterexample": "D_0=epsilon/2. Prefix(a,u) has probability1/2 and gives M^A=epsilon,M^B=0, so D/M^A=1. Thus localization away from M^A=0 is a missing premise for a relative-error extension.", "independent_reviewer": "w398 requested; pending", "remaining_gap": "Independent check. The paired packet makes only the valid absolute bound and is not refuted by this example.", "status": "proved special case", "claim_type": "boundary_counterexample", "landing_state": "draft"}
]
with (root / "CLAIMS.jsonl").open("a", encoding="utf-8") as handle:
    for row in rows:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")

def make_entry(key, name, title, statement, assumptions, kind="concept"):
    return {"key": key, "namespace": "probability.saw", "logical_name": name,
            "kind": kind, "title": title, "statement": statement, "proof_text": None,
            "assumptions": assumptions, "domain": "probability theory",
            "source": {"source_id": "owner-probability-w397-p0003-length-audit-20261010:" + key,
                       "url": None, "revision": "2026-10-10-draft-independent-audit",
                       "license": "owner-own-work",
                       "excerpt": "w396 proposed the length-preserving kernels and first-entrance bound; w397 independently audited them in REVIEW_w396_proof.md. The static estimate remains unproved."}}

entries = [
    make_entry("length-kernel", "saw-length-resolved-continuation-kernel", "Length-resolved SAW continuation kernel", "For a finite graph G with inherited positive edge weights, C_m(G;v) is the sum of product weights over simple paths of exactly m edges starting at v, with a free terminal vertex; C_0(G;v)=1 for a retained v. In a uniform n-step origin-started SAW law, a realized k-edge prefix eta has a suffix law on G_eta with exact remaining length n-k, where G_eta deletes earlier prefix vertices and retains its tip. Obstacle avoidance therefore uses C_(n-k)(G_eta minus A;tip)/C_(n-k)(G_eta;tip), multiplied by the prefix-avoidance indicator. An all-length partition sum defines a different conditional law.", ["Finite graph containing all n-step origin walks", "Simple paths", "Positive-probability prefix", "Exact n-step ensemble"], "definition"),
    make_entry("entrance-bound", "fixed-length-saw-first-collar-entrance-bound-draft", "Draft first-collar-entrance counting bound", "DRAFT checked counting reduction; integration referee for the newest fixed-length packet is pending. For nested forbidden edge sets A subset B, every length-n path avoiding A but using B has a unique first B edge(v,w), after k edges. Its prefix avoids B and its suffix avoids A with length n-k-1. Consequently its total count is at most sum over k=0,...,n-1 and oriented(v,w) in B minus A of c_k^B(0,v)*C_(n-k-1)^A(w). Unit edge weights are assumed; include the first-edge weight for a weighted version. Dropping mutual prefix/suffix avoidance increases the count and supplies no scale-uniform collar decay.", ["Finite graph", "Unit weights for the displayed counts", "Nested forbidden edge sets", "Exact length n", "C_0=1"]),
    make_entry("hdisk-gap", "uniform-fixed-length-saw-disk-collar-estimate-open-input", "Unproved fixed-length SAW disk-collar estimate", "UNPROVED INPUT for an explicitly chosen version of P0003. Take a uniform n-step origin-started honeycomb SAW and scale its trace by s_n=n^(-3/4). For a fixed closed disk A centered at z of radius r<|z| and its concentric radius(1+epsilon)r disk B_epsilon, let Delta_n(epsilon)=P(the scaled trace avoids A but intersects B_epsilon). The requested bound is limsup_(n to infinity)Delta_n(epsilon)<=C(z,r)*epsilon^alpha for some alpha>0, finite C(z,r), and all sufficiently small epsilon. The n limit comes first. This modulus is not proved by the finite continuation identity, a Doob inequality, or the first-entrance counting bound. Even proving it would still leave SLE identification, ordered-curve tightness, and the scale/continuum conventions open.", ["Uniform exact-length-n honeycomb walks", "Operational conjectured scale n^(-3/4)", "Fixed z,r with r<|z|", "epsilon small enough that the enlarged disk avoids the origin"])
]
relations = [
    {"from_key": "entrance-bound", "to_key": "length-kernel", "kind": "depends_on", "rationale": "The injection uses the exact remaining-length suffix count defined by C_m, including m=0."},
    {"from_key": "hdisk-gap", "to_key": "entrance-bound", "kind": "semantic_association", "rationale": "The bound gives an upper count for the H_disk collar event but lacks the quantitative mutually avoiding mass estimate needed to make that count small."}
]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w397", "bundle_slug": "p0003-fixed-length-audit-addendum-20261010", "entries": entries, "relations": relations}
local = root / "DRAFT_BUNDLE_002.json"
data = json.dumps(bundle, ensure_ascii=False, indent=2) + "\n"
local.write_text(data, encoding="utf-8")
target = Path("~/math-brain-inbox/w397/bundle_002.json")
part = target.with_suffix(".part")
assert not target.exists() and not part.exists()
part.write_text(data, encoding="utf-8")
part.rename(target)

receipt = json.loads((root / "SUBMISSION_RECEIPT.json").read_text(encoding="utf-8"))
receipt["addendum"] = {"path": str(target), "entries": len(entries), "relations": len(relations)}
receipt["total_entries"] = 9
receipt["total_relations"] = 6
receipt["reviewed"] = False
receipt["reviewed_parts"]["w396.L0-L3"] = "w397 mathematical audit; separate w398 KEEP for finite/conditional L0-L3"
(root / "SUBMISSION_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
source_status["landing_states"] = {"prepared": True, "submitted": True, "reviewed": False, "ingested": False, "retrievable": False}
(root / "SOURCE_STATUS.json").write_text(json.dumps(source_status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

packet_path = root / "review_packet/PACKET.json"
packet = json.loads(packet_path.read_text(encoding="utf-8"))
packet["artifacts"] += ["REVIEW_w396_proof.md", "DRAFT_BUNDLE_002.json", "review_packet/w396_snapshot_receipt.json"]
packet["check_needed"] = ["Latest fixed-length L0prime and first-entrance injection(U)", "Boundary-attached capped-notch and relative-error examples", "Draft concepts, allowed relations and primary source scope", "LSW uniqueness citation correction"]
packet["hardest_gap"] = source_status["hardest_missing_input"]
packet_path.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
(root / "PROGRESS_EVENT.txt").write_text("w397 S1.P0003: w398-kept finite circulation witness;96 exact configurations/576 equations; corrected fixed-length paired packet audited;9 draft entries submitted; H_disk/H_len remain unproved. Evidence:~/brain_workers/w397/REPORT.md\n", encoding="utf-8")
print(json.dumps({"submitted_addendum": str(target), "total_entries": 9, "total_relations": 6,
                  "paired_proof_snapshot": snapshot["sha256"], "ingested": False, "retrievable": False}, indent=2))
