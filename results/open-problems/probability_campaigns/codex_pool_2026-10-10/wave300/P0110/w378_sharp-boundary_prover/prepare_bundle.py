"""Prepare reviewable drafts locally; --submit writes only the brief's inbox path."""
from __future__ import annotations

import argparse
import difflib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w378")
FINAL = INBOX / "bundle_001.json"
NAMES = {
    "L1": ("sharp-support-width-axial-fpp-geodesic-threshold", "Sharp support-width threshold for axial FPP geodesics"),
    "L2": ("no-law-uniform-strict-fpp-variance-contraction", "No law-uniform strict FPP variance contraction"),
    "L3": ("uniform-weight-fpp-almost-sure-axial-cutoff", "Exact almost-sure axial cutoff for Uniform FPP weights"),
}


def dump(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--submit", action="store_true")
    args = parser.parse_args()
    claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(claims) == 3 and len({c["claim_id"] for c in claims}) == 3
    entries = []
    for claim in claims:
        suffix = claim["claim_id"].rsplit("-", 1)[-1]
        logical, title = NAMES[suffix]
        assert claim["status"] == "proved special case"
        entries.append({
            "key": suffix.lower(), "namespace": "probability.fpp", "logical_name": logical,
            "kind": "lemma", "title": "DRAFT: " + title,
            "statement": "Author-proved special case; independent review pending. " + claim["statement"],
            "proof_text": claim["proof_or_counterexample"], "assumptions": claim["assumptions"],
            "domain": "probability theory",
            "source": {"source_id": "owner-own-work:w378:P0110:" + suffix,
                       "url": "file:///~/brain_workers/w378/BOUNDARY_LEMMA.md",
                       "revision": "2026-10-10 author proof, independent review pending",
                       "license": "owner-own-work", "excerpt": None},
        })
    bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w378", "bundle_slug": "w378-p0110-sharp-support-boundary-001",
              "entries": entries,
              "relations": [
                  {"from_key": "l2", "to_key": "l1", "kind": "depends_on",
                   "rationale": "Apply L1 at n and Mn with epsilon<2/(Mn); both passage times are iid sums and their normalized variance ratio is exactly one."},
                  {"from_key": "l3", "to_key": "l1", "kind": "depends_on",
                   "rationale": "The strict half of the Uniform-law cutoff follows from L1; the explicit endpoint and detour arguments prove equality and sharpness."},
              ]}
    required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
    for entry in entries:
        assert required <= entry.keys() and entry["proof_text"]
        assert entry["source"]["license"].startswith("owner-own-work")
    keys = {entry["key"] for entry in entries}
    for relation in bundle["relations"]:
        assert relation["from_key"] in keys and relation["to_key"] in keys
        assert relation["kind"] == "depends_on" and relation["to_key"] == "l1"
    local = ROOT / "bundle_001.json"
    dump(local, bundle)
    hook = {
        "id": "fpp-boundary-w378-01", "area": "math", "event": "PostToolUse",
        "cue": r"(?is)(FPP|first[- ]passage).*(common threshold|law-independent|uniform over (all )?(iid )?(laws|distributions)).*(variance|contraction|doubling)",
        "fire_when": "FPP common threshold 100: variance contraction for every continuous iid law in [1,2].",
        "silent_when": "FPP variance contraction for fixed Uniform[1,5/4] weights after a threshold N(F) depending on that law.",
        "text": "Check the law quantifier in an FPP variance bootstrap. For Uniform[1,1+epsilon], Mn epsilon<2 forces axial iid sums and V(Mn)/(M V(n))=1. Allow the threshold to depend on the law; this finite boundary does not decide a fixed law's KPZ exponents.",
        "evidence": "w378-P0110-L2; ~/brain_workers/w378/BOUNDARY_LEMMA.md; measurements/boundary_exact.json, exact ratio=1; recall scar fpp_base_case_is_doubling_transfer_principle_2026_08_15",
        "proposer": "w378",
    }
    assert len(hook["text"]) <= 300
    assert re.search(hook["cue"], hook["fire_when"])
    assert not re.search(hook["cue"], hook["silent_when"])
    hook_text = json.dumps(hook, ensure_ascii=False) + "\n"
    (ROOT / "HOOK_PROPOSALS.jsonl").write_text(hook_text, encoding="utf-8")
    patches = ROOT / "patches"
    patches.mkdir(exist_ok=True)
    for number, label, text, destination in [
        (1, "math_w378_hook", hook_text, "~/primary_directive/hooks1000/proposals/math-w378.jsonl"),
        (2, "draft_brain_bundle", local.read_text(encoding="utf-8"), FINAL.as_posix()),
    ]:
        patch = "".join(difflib.unified_diff([], text.splitlines(keepends=True), fromfile="a/" + destination, tofile="b/" + destination))
        (patches / f"{number:02d}_{label}.diff").write_text(patch, encoding="utf-8")
    dump(ROOT / "measurements" / "draft_validation.json", {
        "verdict": "PASS", "bundle_entries": len(entries), "internal_relations": len(bundle["relations"]),
        "dangling_relation_ends": 0, "source_license": "owner-own-work", "independent_review": "pending",
        "hook_text_characters": len(hook["text"]), "hook_fire_controls": "1/1", "hook_silent_controls": "1/1",
        "validation_scope": "Local structural checks and two cue controls; no integrator, store mutation, source seal, manifest, or formal-proof receipt."})
    dump(ROOT / "PROGRESS_EVENT.json", {
        "agent": "w378", "row": "S1.P0110", "state": "staged for reviewer, not posted to global progress page",
        "event": "P0110: 3 sharp support-width boundary claims saved; 8704 exact cases PASS; original exponent-matching gap remains open in this packet.",
        "evidence": (ROOT / "REVIEW_PACKET.md").as_posix()})
    submitted = False
    if args.submit:
        INBOX.mkdir(parents=True, exist_ok=True)
        payload = local.read_bytes()
        if FINAL.exists():
            if FINAL.read_bytes() != payload:
                raise RuntimeError("Inbox draft already exists with different content; preserved it")
        else:
            part = FINAL.with_suffix(".part")
            if part.exists():
                raise RuntimeError("Existing partial draft preserved; choose a new authorized output name")
            part.write_bytes(payload)
            part.rename(FINAL)
        assert FINAL.read_bytes() == payload
        submitted = True
    dump(ROOT / "BRAIN_SUBMISSION.json", {
        "agent": "w378", "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "local_draft": local.as_posix(), "inbox_draft": FINAL.as_posix(),
        "prepared": True, "submitted": submitted, "reviewed": False,
        "ingested": "not claimed", "retrievable": "not claimed", "entry_count": 3,
        "review_packet": (ROOT / "REVIEW_PACKET.md").as_posix(),
        "note": "Only a DRAFT submission. Validating coordinator reviews and integrates; worker does not run the live integrator."})
    status_path = ROOT / "SOURCE_STATUS.json"
    source_status = json.loads(status_path.read_text(encoding="utf-8"))
    source_status["brain_states"].update(prepared=True, submitted=submitted)
    dump(status_path, source_status)
    print(json.dumps({"validation": "PASS", "entries": 3, "relations": 2, "hook_fire": True, "hook_silent": True, "submitted": submitted, "destination": FINAL.as_posix()}))


if __name__ == "__main__":
    main()
