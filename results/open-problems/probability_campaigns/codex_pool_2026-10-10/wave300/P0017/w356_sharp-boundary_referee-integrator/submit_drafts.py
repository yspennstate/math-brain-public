"""Submit only the task/contract-named draft and hook proposal; no ingestion."""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w356")
HOOK = Path("~/primary_directive/hooks1000/proposals/math-w356.jsonl")


def main():
    schema = json.loads((ROOT / "INTEGRATOR_SCHEMA_RECEIPT.json").read_text(encoding="utf-8"))
    assert schema["result"] == "PASS" and schema["entries"] == 8
    assert INBOX.resolve().as_posix().lower() == "~/math-brain-inbox/w356"
    assert HOOK.resolve().as_posix().lower() == "~/primary_directive/hooks1000/proposals/math-w356.jsonl"
    INBOX.mkdir(exist_ok=True)
    data = (ROOT / "drafts/bundle_001.json").read_bytes()
    destination = INBOX / "bundle_001.json"
    if destination.exists():
        assert destination.read_bytes() == data, "existing destination differs; preserve it"
    else:
        partial = INBOX / "bundle_001.part"
        with partial.open("xb") as out:
            out.write(data)
            out.flush()
            os.fsync(out.fileno())
        partial.rename(destination)
    assert destination.read_bytes() == data
    line = (ROOT / "HOOK_PROPOSALS.jsonl").read_text(encoding="utf-8").strip()
    proposed = json.loads(line)
    existing = [json.loads(row) for row in HOOK.read_text(encoding="utf-8-sig").splitlines() if row.strip()] if HOOK.exists() else []
    matches = [row for row in existing if row["id"] == proposed["id"]]
    if matches:
        assert matches == [proposed], "existing hook with this ID differs; preserve it"
    else:
        with HOOK.open("a", encoding="utf-8") as stream:
            stream.write(line + "\n")
    state = json.loads((ROOT / "SUBMISSION_STATE.json").read_text(encoding="utf-8"))
    state.update({"submitted": True, "destination": str(destination), "hook_proposal": str(HOOK),
                  "review_request_sent": True, "review_request_message": "msg-fe6e0a7a93",
                  "reviewed": False, "ingested": False, "retrievable": False})
    (ROOT / "SUBMISSION_STATE.json").write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    source = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
    source["brain_states"].update({"submitted": True, "reviewed": False, "ingested": False, "retrievable": False})
    (ROOT / "SOURCE_STATUS.json").write_text(json.dumps(source, indent=2) + "\n", encoding="utf-8")
    claims = [json.loads(row) for row in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()]
    for claim in claims:
        claim["independent_reviewer"] = "w359; review request msg-fe6e0a7a93 delivered; verdict pending"
        if claim["id"] == "w356-P0017-C01":
            claim["source"] = {"license": "owner-own-work", "artifact": "ATTEMPT.md", "parent_source": "SOURCE_STATUS.json (verified statement; full proof unaudited)"}
        claim["measurement"] = "MEASUREMENTS.json"
    (ROOT / "CLAIMS.jsonl").write_text("".join(json.dumps(row) + "\n" for row in claims), encoding="utf-8")
    print(json.dumps(state, indent=2))


if __name__ == "__main__":
    main()
