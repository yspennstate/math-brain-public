"""Attach actual scoped peer verdicts; publish only explicitly authorized drafts."""
from datetime import datetime, timezone
import difflib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
MESH = Path("~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py")
INBOX = Path("~/math-brain-inbox/w522")
HOOK = Path("~/primary_directive/hooks1000/proposals/math-w522.jsonl")
REFEREE = Path("~/brain_workers/w524/VERDICTS.jsonl")
CLAIM_IDS = {f"P0297.w522.{c}" for c in ["C1", "L1", "L2", "L3", "L4"]}


def now():
    return datetime.now(timezone.utc).isoformat()


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(name, obj):
    path = ROOT / name
    assert path.resolve().is_relative_to(ROOT.resolve())
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def append(name, obj):
    path = ROOT / name
    assert path.resolve().is_relative_to(ROOT.resolve())
    with path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(obj, ensure_ascii=False) + "\n")


def invoke(argv, receipt_name):
    run = subprocess.run([sys.executable, "-X", "utf8", *argv],
                         capture_output=True, text=True, encoding="utf-8", errors="replace")
    receipt = {"at_utc": now(), "argv": argv, "returncode": run.returncode,
               "stdout": run.stdout, "stderr": run.stderr}
    append(receipt_name, receipt)
    try:
        receipt["parsed"] = json.loads(run.stdout)
    except (ValueError, TypeError):
        receipt["parsed"] = None
    print(json.dumps({"command": argv[1:3], "returncode": run.returncode,
                      "stdout": run.stdout[:500], "stderr": run.stderr[:500]}), flush=True)
    return receipt


def acquire(resource, purpose):
    receipt = invoke([str(MESH), "claim", "--agent", "w522", "--resource", resource,
                      "--mode", "exclusive", "--purpose", purpose, "--ttl", "1800"],
                     "RESUME_CLAIM_RECEIPTS.jsonl")
    parsed = receipt["parsed"]
    return receipt["returncode"] == 0 and isinstance(parsed, dict) and bool(parsed.get("acquired"))


def release(resource):
    return invoke([str(MESH), "release", "--agent", "w522", "--resource", resource],
                  "RESUME_CLAIM_RECEIPTS.jsonl")


def prepare():
    state = (ROOT / "STATUS.md").read_text(encoding="utf-8-sig").splitlines()[0]
    assert state == "STATE: NEEDS_REVIEW"
    verdicts = [json.loads(line) for line in REFEREE.read_text(encoding="utf-8-sig").splitlines()
                if line.strip()]
    selected = [row for row in verdicts if row.get("claim") in CLAIM_IDS]
    assert len(selected) == 5 and {row["claim"] for row in selected} == CLAIM_IDS
    assert all(row["verdict"] == "KEEP" and row["independent_reviewer"] == "w524" for row in selected)
    receipt_path = ROOT / "referee" / "w524_verdicts.jsonl"
    receipt_path.parent.mkdir(exist_ok=True)
    receipt_path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in selected),
                            encoding="utf-8")
    review = {"reviewer": "w524", "status": "five scoped independent KEEP receipts received",
              "claims": sorted(CLAIM_IDS), "receipt": str(receipt_path),
              "source_receipt": str(REFEREE), "received_at_utc": now(),
              "scope": "C1 and L1-L4 only; not the original target, relations, or hook implementation",
              "formal_proof_receipt": None, "reviewer_account_verified": False}
    write_json("REVIEW_RECEIPT.json", review)
    by_claim = {row["claim"]: row for row in selected}
    claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8-sig").splitlines()
              if line.strip()]
    assert len(claims) == 6
    for row in claims:
        claim_id = row["claim_id"]
        if claim_id in by_claim:
            row["status"] = "independently checked proof"
            row["independently_checked"] = True
            row["independent_reviewer"] = "w524"
            row["independent_verdict"] = by_claim[claim_id]
            row["review_receipt"] = str(receipt_path)
    (ROOT / "CLAIMS.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in claims),
                                     encoding="utf-8")
    for row in selected:
        append("RESUME_ROWS.jsonl", {"id": row["claim"] + ".w524-keep", "status": "independently checked proof",
                                     "statement": row["scope"], "reviewer": "w524",
                                     "verdict": row["verdict"], "evidence": str(receipt_path),
                                     "remaining_gap": row["remaining_gap"]})
    source = read_json(ROOT / "SOURCE_STATUS.json")
    source["independent_review"] = review
    assert source["current_openness"] == "UNKNOWN" and not source["original_target_solved"]
    write_json("SOURCE_STATUS.json", source)
    brain = read_json(ROOT / "BRAIN_STATES.json")
    brain["reviewed"] = review
    brain["review_revision"] = {"status": "prepared", "local_path": str(ROOT / "bundle_local_002.json"),
                               "supersedes": "bundle_001.json as a review-metadata revision",
                               "mathematical_statements_changed": False,
                               "relations_pair_audited": False}
    write_json("BRAIN_STATES.json", brain)
    original = read_json(ROOT / "bundle_local_001.json")
    bundle = json.loads(json.dumps(original))
    bundle["bundle_slug"] = "p0297-w522-scoped-review-metadata-20261010"
    old_prefix = "AUTHOR DRAFT, independent review pending w524. "
    new_prefix = "SCOPED INDEPENDENT KEEP by w524 on 2026-10-10; original P0297 unresolved. "
    for entry in bundle["entries"]:
        assert entry["kind"] == "concept" and entry["proof_text"] is None
        if entry["source"]["license"] == "owner-own-work":
            assert entry["statement"].startswith(old_prefix)
            entry["statement"] = new_prefix + entry["statement"][len(old_prefix):]
            entry["source"]["revision"] = "2026-10-10-w524-scoped-KEEP; referee/w524_verdicts.jsonl"
    assert bundle["relations"] == original["relations"]
    write_json("bundle_local_002.json", bundle)
    proposed_path = ROOT / "PRIOR_D0049_PROPOSED.json"
    proposed = read_json(proposed_path)
    correction = proposed["normalization_correction"]
    for key in list(correction):
        if "review" in key.lower():
            correction[key] = review if isinstance(correction[key], dict) else "w524: KEEP, C1 only"
    correction["independent_review"] = review
    patch_path = ROOT / "patches" / "02_d0049_normalization.diff"
    lines = patch_path.read_text(encoding="utf-8-sig").splitlines(keepends=True)
    added = [i for i, line in enumerate(lines) if line.startswith("+") and not line.startswith("+++")]
    assert len(added) == 1
    patch_record = json.loads(lines[added[0]][1:])
    assert patch_record["attempt_id"] == proposed["attempt_id"]
    lines[added[0]] = "+" + json.dumps(proposed, ensure_ascii=False) + "\n"
    patch_path.write_text("".join(lines), encoding="utf-8")
    write_json("PRIOR_D0049_PROPOSED.json", proposed)
    attempt = (ROOT / "ATTEMPT.md").read_text(encoding="utf-8-sig")
    attempt = attempt.replace("Original problem unresolved by this packet; independent mathematical review pending.",
                              "Original problem unresolved by this packet; w524 independently kept C1 and L1-L4.")
    attempt = attempt.replace("author-proved special case, pending w524",
                              "proved deterministic special case, independently kept by w524")
    old = ("The submitted bundle remains concept/draft material; no independent keep, formal receipt, "
           "ingestion or retrieval is certified.")
    new = ("The bundle remains concept/draft material. On resumption, five claim-specific independent KEEP "
           "verdicts from w524 were recovered and saved in referee/w524_verdicts.jsonl. No formal receipt, "
           "ingestion or retrieval is certified.")
    assert old in attempt
    (ROOT / "ATTEMPT.md").write_text(attempt.replace(old, new), encoding="utf-8")
    packet = (ROOT / "REVIEW_PACKET.md").read_text(encoding="utf-8-sig")
    packet = packet.replace("No independent adversary receipt or audit is claimed.",
                            "No independent adversary delivery receipt is claimed. Five mathematical KEEP receipts "
                            "from w524 are now saved in referee/w524_verdicts.jsonl.")
    packet = packet.replace("bundle_local_001.json is the exact local copy",
                            "bundle_local_001.json preserves the original submission; bundle_local_002.json is the review-metadata revision")
    packet = packet.replace("NEXT: w524 checks C1 and L1--L4, records an independent verdict, then the validating coordinator may apply the source repair and handle draft integration;",
                            "NEXT: the validating coordinator applies the independently kept C1 source repair and handles draft integration;")
    (ROOT / "REVIEW_PACKET.md").write_text(packet, encoding="utf-8")
    write_json("REVIEW_UPDATE_VERIFICATION.json",
               {"at_utc": now(), "scoped_keep_receipts": 5, "claim_rows": 6, "original_target_solved": False,
                "original_bundle_preserved": original == read_json(INBOX / "bundle_001.json"),
                "revision_entries": len(bundle["entries"]), "revision_relations": len(bundle["relations"]),
                "concept_only": True, "mathematical_statements_changed": False,
                "scope": "Receipt association and metadata verification; not a second mathematical audit."})
    print("Prepared five scoped KEEP receipts and concept-only bundle revision.", flush=True)


def publish():
    brain = read_json(ROOT / "BRAIN_STATES.json")
    assert brain["reviewed"]["status"] == "five scoped independent KEEP receipts received"
    resource = "file:" + INBOX.as_posix()
    if acquire(resource, "P0297-w522-reviewed-concept-metadata-revision"):
        try:
            bundle = read_json(ROOT / "bundle_local_002.json")
            target = INBOX / "bundle_002.json"
            part = INBOX / "bundle_002.json.part"
            assert target.resolve().parent == INBOX.resolve() == part.resolve().parent
            if target.exists():
                assert read_json(target) == bundle
            else:
                if part.exists():
                    assert read_json(part) == bundle
                else:
                    with part.open("x", encoding="utf-8") as stream:
                        json.dump(bundle, stream, ensure_ascii=False, indent=2)
                        stream.write("\n")
                part.replace(target)
            assert read_json(target) == bundle
            brain["review_revision"].update(status="submitted DRAFT concepts with scoped KEEP metadata",
                                             submitted_path=str(target), submitted_at_utc=now())
            brain["submitted"]["original_submission_path"] = brain["submitted"]["path"]
            brain["submitted"]["path"] = str(target)
            brain["submitted"]["revision_at_utc"] = now()
            write_json("BRAIN_STATES.json", brain)
            print("Submitted bundle_002.json; original bundle retained.", flush=True)
        finally:
            release(resource)
    hook = json.loads((ROOT / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8-sig").strip())
    assert len(hook["text"]) <= 300 and hook["proposer"] == "w522"
    resource = "file:" + HOOK.as_posix()
    hook_state = {"status": "prepared locally", "path": str(HOOK), "id": hook["id"]}
    if acquire(resource, "P0297-w522-one-evidenced-hook-proposal"):
        try:
            existing = [json.loads(s) for s in HOOK.read_text(encoding="utf-8-sig").splitlines() if s.strip()] if HOOK.exists() else []
            matches = [r for r in existing if r.get("id") == hook["id"]]
            assert not matches or (len(matches) == 1 and matches[0] == hook)
            if not matches:
                with HOOK.open("a", encoding="utf-8") as stream:
                    stream.write(json.dumps(hook, ensure_ascii=False) + "\n")
            hook_state.update(status="proposal submitted; hook audit and implementation pending", at_utc=now())
            print("Submitted one hook proposal.", flush=True)
        finally:
            release(resource)
    write_json("HOOK_SUBMISSION.json", hook_state)
    event = read_json(ROOT / "PROGRESS_EVENT.json")
    published = read_json(ROOT / "BRAIN_STATES.json")["review_revision"]["status"].startswith("submitted")
    event["event"] = ("P0297: w524 independently kept normalization correction C1 and boundary lemmas L1-L4; "
                      "64/64 arithmetic errors to 0, known anchor 10 to 4; review-metadata draft "
                      + ("submitted" if published else "prepared") + "; original LFPP gap remains.")
    event["evidence"] = str(ROOT / "REVIEW_PACKET.md")
    resource = "topic:pd-progress:" + event["row"]
    if acquire(resource, "P0297-w522-one-completion-progress-event"):
        try:
            receipt = invoke(["~/primary_directive/pd_progress.py", "--event", event["event"],
                              "--agent", event["agent"], "--row", event["row"], "--evidence", event["evidence"]],
                             "PROGRESS_POST_RECEIPTS.jsonl")
            event["state"] = "posted" if receipt["returncode"] == 0 else "posting failed; receipt saved"
            event["posted_at_utc"] = now()
            write_json("PROGRESS_EVENT.json", event)
        finally:
            release(resource)


def notify():
    bodies = [
        ("w523", "P0297/w522/statement",
         "Statement-first independent-adversary file remains ~/brain_workers/w522/STATEMENT_FOR_ADVERSARY.md. "
         "It contains the exact target and lane assumptions, without the prover proof. Original target remains unresolved."),
        ("w524", "P0297/w522/referee",
         "Your five scoped KEEP receipts for w522 C1/L1-L4 were received and preserved in "
         "~/brain_workers/w522/referee/w524_verdicts.jsonl. Updated full packet: "
         "~/brain_workers/w522/REVIEW_PACKET.md. Review-metadata revision: bundle_local_002.json; "
         "BRAIN_STATES.json records submission separately. The archive repair is still unapplied and the original LFPP gap remains.")]
    for peer, topic, body in bodies:
        receipt = invoke([str(MESH), "send", "--agent", "w522", "--to", peer,
                          "--topic", topic, "--kind", "request", "--body", body],
                         "RESUME_HANDOFF_RECEIPTS.jsonl")
        append("RESUME_ROWS.jsonl", {"id": "w522-resume-handoff-" + peer, "at_utc": now(),
                                     "status": "mesh accepted" if receipt["returncode"] == 0 else "file handoff retained",
                                     "evidence": "RESUME_HANDOFF_RECEIPTS.jsonl"})


if __name__ == "__main__":
    {"prepare": prepare, "publish": publish, "notify": notify}[sys.argv[1]]()
