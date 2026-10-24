"""Assemble review metadata and a proposal-only patch; no integration."""
from pathlib import Path
import difflib
import json

root = Path(__file__).resolve().parent
bundle = json.loads((root / "bundle_001.json").read_text(encoding="utf-8"))
failure = json.loads((root / "RETRIEVAL_FAILURE.json").read_text(encoding="utf-8"))
metrics = json.loads((root / "MEASUREMENTS.json").read_text(encoding="utf-8"))
source = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
source["primary_sources"].append({
    "url": "https://arxiv.org/pdf/1712.04651", "authors": "Hugo Duminil-Copin",
    "locator": "Conjecture 1, page 3; model definition pages 1-2",
    "verified_scope": "Primary historical bond conjecture theta(p_c)=0 on Z^d for d>=3. Exact nearest-neighbour product model read; not a current openness certificate."})
source["primary_sources"].append({
    "url": "https://arxiv.org/html/2304.12110", "authors": "Hugo Vanneuville",
    "locator": "Theorem 2, magnetization and volume-tail definitions; Theorem 1",
    "verified_scope": "Comparison at q=p(1-m_h(p)), p in (0,1), h>0; exact changed parameter and green-mark definitions read. It does not directly supply a critical tail bound."})
source["math_brain_card_evidence"] = {
    "file": str(root / "MATH_BRAIN_CARDS.json"), "returned_claims": failure["claim_hit_count"],
    "empty_structured_assumptions": failure["claims_with_empty_structured_assumptions"],
    "without_fidelity_review": failure["claims_without_fidelity_review"],
    "note": "Theorem 1 has an existing statement-fidelity repair. This worker neither reviewed that review nor overwrote it; only the current statement was used."}
source["solved_register_check"] = {"path": "~/Open problem project/solved_register.md",
                                   "result": "Targeted percolation/C0023/critical search returned no match. No whole-register read; absence of a match is not a proof of openness."}
(root / "SOURCE_STATUS.json").write_text(json.dumps(source, indent=2, ensure_ascii=False), encoding="utf-8")

hook_lines = (root / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8").splitlines(keepends=True)
hooks = [json.loads(line) for line in hook_lines]
assert all(len(hook["text"])<=300 for hook in hooks)
patchdir = root / "patches"
patchdir.mkdir(exist_ok=True)
live = "~/primary_directive/hooks1000/proposals/math-w430.jsonl"
patch = "".join(difflib.unified_diff([], hook_lines, fromfile="a/"+live, tofile="b/"+live))
(patchdir / "01_math_endpoint_hook.diff").write_text(patch, encoding="utf-8")

receipt = {"claims_jsonl_rows": 4, "edge_rows": len(bundle["relations"]), "draft_entries": len(bundle["entries"]),
           "all_entries_concepts": all(e["kind"]=="concept" and e["proof_text"] is None for e in bundle["entries"]),
           "all_entries_review_pending": all(e["statement"].startswith("DRAFT;") for e in bundle["entries"]),
           "schema": "Locally checked against BUNDLE_SPEC.md; integrator not run",
           "hook_text_chars": len(hooks[0]["text"]), "hook_patch_header_live_path": live,
           "arithmetic_checks": "passed", "tile_distance_checks": metrics["tile_distance_checks"],
           "referee_receipt": None, "formal_theorem_receipt": None,
           "command": "python -X utf8 ~/brain_workers/w430/finalize_packet.py"}
assert receipt["all_entries_concepts"] and receipt["all_entries_review_pending"]
assert len((root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines())==4
(root / "VALIDATION.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))
