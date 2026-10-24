"""Apply received mathematical feedback and source receipts to the local packet."""
from datetime import datetime, timezone
from pathlib import Path
import difflib
import json

ROOT = Path(__file__).resolve().parent
now = datetime.now(timezone.utc).isoformat()
def save(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

status = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
status["checked_at"] = now
status["original_p0043_store_records"] = {
    "readonly_store": "~/math-brain-build/local/population/brain.sqlite3",
    "statement_node": "claim_c84438aaebd3352ec231b6a011882233b933b517484f1aceb0e487376b263099",
    "attempt_node": "claim_9850a15b06f23b6e38459dc61373db77c0b50e6ff9678c5a92e051af94f90dc4",
    "original_source": "Lyons--Peres, Probability on Trees and Networks, paperback electronic version 19 August 2026, Conjecture 8.15, printed p.285",
    "recorded_statement": "If G is quasi-transitive and p_c(G)<1, is there almost surely no infinite Bernoulli cluster at p_c(G)?",
    "prior_method": "Critical branching-process extinction for a regular tree, with no justified loop-dependent transfer",
    "book_locator_independently_rechecked": False,
    "stuck": "STUCK: two targeted public-book PDF searches did not return Conjecture 8.15. Keep the stored locator and use the opened Hutchcroft primary bond formulation. Do not infer current openness."
}
status["targeted_history_receipt"] = {
    "file": "LOCAL_SOURCE_RECEIPTS.json", "named_intake_ledgers_checked": 10,
    "matching_cross_reference_rows": 1,
    "cross_reference": "H0016, intake H problems.jsonl line 16, not_attempted, duplicate_of G0001/P0043",
    "model_limit": "This is a site-percolation lattice problem, not a verified equivalence to the general quasi-transitive bond target"
}
status["recent_site_partial_result"] = {
    "url": "https://arxiv.org/abs/2608.23661", "author": "Raphael Cerf", "date": "2026-08-24",
    "checked": "primary abstract only", "model": "Bernoulli site percolation on Z^d, d>=3",
    "result": "At criticality either no infinite cluster exists or the finite-cluster distribution has no stretched-exponential tail",
    "full_target_certificate": False, "bond_transfer_verified": False
}
status["independent_review_status"] = "designated referee w437 pending; adversary w436 kept L1-L4"
status["adversary_review"] = {
    "reviewer": "w436", "file": "~/brain_workers/w436/AUDIT_w435.md",
    "verdicts": {"L1": "KEEP", "L2": "KEEP", "L3": "KEEP", "L4": "KEEP", "G1": "FIX, accepted as missing completion premise"},
    "full_target": "UNPROVED BY THIS ROUTE", "different_account_verified": False
}
save("SOURCE_STATUS.json", status)

claims_file = ROOT / "CLAIMS.jsonl"
old_claims = claims_file.read_text(encoding="utf-8")
snapshot = ROOT / "CLAIMS_BEFORE_ADVERSARY.jsonl"
if not snapshot.exists():
    snapshot.write_text(old_claims, encoding="utf-8")
claims = [json.loads(s) for s in old_claims.splitlines() if s.strip()]
for c in claims:
    if c["id"] in {"w435-L1", "w435-L2", "w435-L3", "w435-L4"}:
        c["independent_reviewer"] = "w436 KEEP, designated referee w437 pending"
        c["review_state"] = "adversary-kept; designated-referee-pending"
        c["review_evidence"] = "~/brain_workers/w436/AUDIT_w435.md"
    if c["id"] == "w435-G1":
        c["statement"] = "Missing completion premise: in an applicable graph class, derive from the full quasi-transitive hypotheses and hypothetical critical survival a ray measure inside a surviving critical component with finite I_r for some r<1. This premise has not been proved."
        c["status"] = "sketch"
        c["kind"] = "unproved method gap"
        c["independent_reviewer"] = "w436 FIX accepted, designated referee w437 pending"
        c["review_state"] = "FIX accepted; remains unproved"
        c["proof_or_counterexample"] = "L1 and L2 imply that any actually surviving critical component has no such finite-energy measure. A host-graph measure does not transfer automatically. The non-quasi-transitive controls do not refute the desired implication with the full P0043 hypotheses, but no derivation is supplied."
        c["review_evidence"] = "~/brain_workers/w436/AUDIT_w435.md"
if not any(c["id"] == "w435-S1" for c in claims):
    claims.append({"id": "w435-S1", "kind": "source-status correction",
        "statement": "The exact stored P0043 statement includes p_c<1 and cites Lyons--Peres Conjecture 8.15. The opened Hutchcroft primary paper independently verifies the connected locally finite quasi-transitive bond formulation. Current openness remains UNKNOWN; no full-target proof receipt was obtained.",
        "assumptions": ["Historical P0043 record and dated ranking", "Primary statement check, not mathematical proof verification"],
        "source": "STORE_SOURCE_ROWS.json; SOURCE_STATUS.json; https://arxiv.org/html/1605.05301",
        "proof_or_counterexample": "The statement card explicitly says 'If G is quasi-transitive and p_c(G)<1'; the 2016 primary bond formulation agrees. The public comparator has an admitted placeholder and no actual solution receipt was checked.",
        "independent_reviewer": "w437 pending", "remaining_gap": "Actual recent full-proof verification unavailable; current openness UNKNOWN.",
        "status": "sketch", "novelty_claim": False})
claims_file.write_text("".join(json.dumps(c, ensure_ascii=False)+"\n" for c in claims), encoding="utf-8")

attempt_file = ROOT / "ATTEMPT.md"
attempt = attempt_file.read_text(encoding="utf-8")
attempt = attempt.replace("No matching P0043/C0084 result was returned from targeted ID searches of the supplied H/I attempt directories or their intake ledgers.",
    "Ten named intake ledgers yielded one cross reference: H0016, a not-attempted site-percolation lattice conjecture tagged duplicate_of G0001/P0043. Cerf's primary abstract, arXiv:2608.23661, confirms a site partial result and supplies neither general critical extinction nor a site-to-bond transfer. The targeted H/I attempt search returned no target proof.")
if "Original P0043 record recovered" not in attempt:
    attempt += "\nOriginal P0043 record recovered. STORE_SOURCE_ROWS.json preserves the exact statement and regular-tree attempt from the read-only population store. The statement cites Lyons--Peres, Conjecture 8.15, printed p.285, electronic version 19 August 2026. Its prior proof is the valid regular-tree branching fixed point, with loop dependence explicitly left open. This packet reuses critical regular-tree extinction only as a classical fact in the susceptibility correction; the independent route is L1--L3. The book locator itself was not recovered in two public-PDF searches; the precise bond statement is independently checked in Hutchcroft's primary paper. Current peer boundaries: w432 uses finite-radius pivotal concentration; w438 uses a polynomial tree threshold. The square-generation control here uses a different profile and is not a novelty claim.\n\nAdversary feedback accepted. w436 independently kept L1--L4 in AUDIT_w435.md and marked G1 FIX. G1 is now recorded as an unproved completion premise, not a proposed proved lemma. This agrees with the explicit hardest gap: derive critical-cluster robustness from quasi-transitivity in an applicable class. The full target remains unproved. Assigned referee w437 has the original packet; its audit is still pending.\n"
attempt_file.write_text(attempt, encoding="utf-8")

statement_file = ROOT / "STATEMENT.md"
statement = statement_file.read_text(encoding="utf-8")
if "Original campaign source recovered" not in statement:
    statement += "\nOriginal campaign source recovered from the read-only statement card: Lyons--Peres, Probability on Trees and Networks, electronic version 19 August 2026, Conjecture 8.15, printed p.285. The cited book locator was not independently recovered online; the equivalent precise bond statement was checked in the Hutchcroft primary paper.\n"
statement_file.write_text(statement, encoding="utf-8")

bundle_file = ROOT / "draft_bundle_001.json"
bundle = json.loads(bundle_file.read_text(encoding="utf-8"))
for e in bundle["entries"]:
    e["statement"] = e["statement"].replace("awaiting independent review", "awaiting designated referee review")
assert len(bundle["entries"]) == 8 and len(bundle["relations"]) == 7
assert all(e["kind"] in {"concept", "definition"} and e["proof_text"] is None for e in bundle["entries"])
assert all(e["source"]["license"].startswith("owner-own-work") for e in bundle["entries"])
save("draft_bundle_001.json", bundle)
text = bundle_file.read_text(encoding="utf-8")
diff = "".join(difflib.unified_diff([], text.splitlines(keepends=True),
    fromfile="a/math-brain-inbox/w435/bundle_001.json", tofile="b/math-brain-inbox/w435/bundle_001.json"))
(ROOT / "patches/01_p0043_draft_bundle.diff").write_text(diff, encoding="utf-8")
validation = json.loads((ROOT / "VALIDATION.json").read_text(encoding="utf-8"))
validation.update({"checked_at": now, "claim_rows": len(claims), "adversary_keep_count": 4,
                   "assigned_referee_audit_complete": False, "full_target_proved": False})
save("VALIDATION.json", validation)

state = json.loads((ROOT / "SUBMISSION.json").read_text(encoding="utf-8"))
state["reviewed"].update({"adversary": "w436", "auxiliary_keeps": ["L1", "L2", "L3", "L4"],
    "gap_fix_accepted": "G1", "assigned_referee_audit_complete": False,
    "meaning": "full designated review not confirmed"})
save("SUBMISSION.json", state)
for name in ("REPORT.md", "REVIEW_PACKET.md"):
    p = ROOT / name
    text = p.read_text(encoding="utf-8")
    if "Adversary audit receipt" not in text:
        text += "\nAdversary audit receipt: w436 kept L1--L4 and marked G1 FIX; the missing completion premise remains unproved. The designated referee w437 received packet message msg-38f8f7abba; its audit is pending. The original P0043 regular-tree attempt and book citation are saved in STORE_SOURCE_ROWS.json. Local output changed from zero claim rows/draft entries at session start to eight claim rows, eight definition/concept entries, and seven relations; live brain gain is not yet measured. Reproduce local packaging with build_packet.py followed by finalize_packet.py.\n"
    p.write_text(text, encoding="utf-8")
print(json.dumps({"status": "PASS", "claim_rows": len(claims), "draft_entries": 8,
                  "relations": 7, "adversary_keeps": 4, "G1": "unproved premise", "referee": "pending"}))
