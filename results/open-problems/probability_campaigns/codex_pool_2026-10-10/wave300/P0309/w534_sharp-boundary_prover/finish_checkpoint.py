"""Save final measurements/status without changing the proved mathematics."""
import json
from datetime import datetime, timezone
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR
from pathlib import Path

root = Path(__file__).resolve().parent
verification = json.loads((root / "VERIFICATION.json").read_text(encoding="utf-8"))
delivery = json.loads((root / "DELIVERY_STATUS.json").read_text(encoding="utf-8"))
validation = json.loads((root / "DRAFT_VALIDATION.json").read_text(encoding="utf-8"))
assert verification["outcome"] == "passed" and validation["passed"]
assert delivery["submitted"]["state"] and not delivery["ingested"] and not delivery["retrievable"]
now = datetime.now(timezone.utc).isoformat()
hessian = next(row for row in verification["rows"] if row.get("s") == 6 and row["kind"] == "rational_hessian_enclosure")
quad = next(row for row in verification["rows"] if row.get("s") == 6 and row["kind"] == "independent_heat_quadrature")


def short_bounds(bounds):
    return [str(Decimal(bounds[0]).quantize(Decimal("0.000001"), rounding=ROUND_FLOOR)),
            str(Decimal(bounds[1]).quantize(Decimal("0.000001"), rounding=ROUND_CEILING))]


period = short_bounds(hessian["periodic_curvature"])
finite = short_bounds(hessian["finite_K_L_per_volume"]["8"])
measurement = {
    "id": "S1.w534.C5", "target_id": "P0309", "utc": now,
    "statement": f"At s=6 the raw periodic curvature lies in {period}; the finitely supported odd-plane displacement on Q_8 has K_8/|Q_8| in {finite}<0. Independent heat quadrature gives D_6(1/4)=-0.0952208176437464. Twelve numeric groups passed.",
    "assumptions": ["The exact A1/B2 energies and displacement are used", "N=8 max-norm cutoff with an analytic shell tail", "Outward-rounded stdlib Decimal integer rational sums; heat quadrature is floating-point"],
    "source": {"path": str(root / "VERIFICATION.json"), "command": "python -B -X utf8 verify_boundary.py"},
    "proof_or_counterexample": "Signed rational enclosures plus independent Gaussian heat quadrature; the universal analytical proof is separately in ATTEMPT.md.",
    "independent_reviewer": {"assigned": "w536", "status": "analytical C2-C4 checked; this numeric implementation has not been independently audited"},
    "remaining_gap": "No formal-check theorem receipt and no P0309 phase construction; do not substitute numeric evidence for the analytical proof.",
    "status": "numerical evidence"
}
with (root / "CLAIMS.jsonl").open("a", encoding="utf-8") as stream:
    stream.write(json.dumps(measurement, ensure_ascii=False) + "\n")

source_status = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
source_status["canonical_math_research_brain_locator"] = {
    "repository": "~/math-research-brain", "status": "not located within the bounded path/code search",
    "method": "README store references, store.py constructor, CLI/config path references, and filename-only sqlite/db discovery excluding banks/audits/evaluations",
    "conclusion": "No complete canonical solved/retired check was possible from that locator; current openness remains UNKNOWN. The named population store was checked read-only."
}
(root / "SOURCE_STATUS.json").write_text(json.dumps(source_status, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

report = f"""P0309 boundary result: for every s>3, simple cubic is force balanced but has arbitrarily small finite-support Riesz energy-lowering perturbations. Alternating-plane slides have strictly lower periodic energy at every nonintegral slide, with equality exactly at integral slides. This refutes the auxiliary bridge from force balance to a stable harmonic crystal.

The recovered prior attempt only checked a conditional infrared integral. ATTEMPT.md now contains three boundary lemmas. Referee w536 kept C2/C3 and kept C4 solely as the displayed relative heat integral; that scope correction is applied. Evidence: REVIEW_RECEIPT.json and w536/REVIEW_w534.md. Current openness and novelty are UNKNOWN; P0309 is unresolved by this packet.

Measured with `python -B -X utf8 verify_boundary.py`: 12 groups passed in {verification['cpu_seconds']:.5f} CPU seconds ({verification['wall_seconds']:.3f}s calculation wall time). At s=6, the curvature is in [{period[0]}, {period[1]}] and K_8/|Q_8| in [{finite[0]}, {finite[1]}]; both are negative. Separate heat quadrature gives Delta_6(1/4)={quad['D_s_a']:.12g}. Exact interval receipts, analytic tail bounds, other exponents and fresh governor gates are in VERIFICATION.json. The initial rejected mode-label receipt is preserved; it was corrected against the compute doctrine before the passing run.

The submitted DRAFT at `~/math-brain-inbox/w534/bundle_001.json` has five entries and six relations. `python -B -X utf8 build_delivery.py` passed schema, owner-own-work, dependency, round-trip and two hook-control checks. DELIVERY_STATUS.json separates submitted and reviewed from ingested=false and retrievable=false. A cross-login admission gate is not certified here.

Apply: the validating coordinator checks/adopts the DRAFT and integrates it; append `hooks/math-w534.jsonl` to the proposal path in `patches/01_riesz_stability_hook.diff`. PROGRESS_EVENT.json stages the progress-page row because unrelated external writes are forbidden in this brief. Named-peer handoffs used the authorized mesh.

The scope limit is substantive: simple-cubic instability says nothing about BCC/FCC stability or existence of a crystalline Gibbs law, and C4 is not a long-range DLR energy identification. The hardest P0309 gap is uniform nonlinear free-energy/order control of a stable phase, its defects and competitors through the thermodynamic limit.

NEXT: Coordinator checks the DRAFT/admission gate and integrates the reviewed boundary cards; subsequent proof work needs a stable-phase nonlinear excess-free-energy estimate.
"""
(root / "REPORT.md").write_text(report, encoding="utf-8")
files = ["SOURCE_STATUS.json", "ATTEMPT.md", "CLAIMS.jsonl", "REVIEW_PACKET.md", "REVIEW_RECEIPT.json", "VERIFICATION.json", "REPORT.md", "DELIVERY_STATUS.json", "DRAFT_VALIDATION.json"]
for name in files:
    assert (root / name).stat().st_size > 0
claims = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()]
assert len({row["id"] for row in claims}) == len(claims)
assert json.loads((root / "drafts/bundle_001.json").read_text(encoding="utf-8")) == json.loads(Path(delivery["submitted"]["path"]).read_text(encoding="utf-8"))
status = (root / "STATUS.md").read_text(encoding="utf-8").splitlines()
status[0] = "STATE: NEEDS_REVIEW"
status[1] = "NEXT: Coordinator reviews DRAFT/admission and staged hook/progress row, then integrates the scoped C2-C4 boundary cards; mathematical KEEP evidence is in REVIEW_RECEIPT.json."
status.append(f"{now}: Finished and measured: 12 scalar groups passed; C2/C3 KEEP and C4 KEEP_SCOPED by w536; five-entry/six-relation DRAFT submitted. Final local artifact checks passed. Live-store ingestion and retrieval remain unverified and separate.")
(root / "STATUS.md").write_text("\n".join(status) + "\n", encoding="utf-8")
print(json.dumps({"state": "NEEDS_REVIEW", "passed_numeric_groups": 12,
                  "periodic_curvature_s6": period, "finite_K8_per_volume_s6": finite,
                  "claims_and_review_events": len(claims), "files_checked": len(files),
                  "bundle_round_trip": True, "ingested": False, "retrievable": False}, indent=2))
