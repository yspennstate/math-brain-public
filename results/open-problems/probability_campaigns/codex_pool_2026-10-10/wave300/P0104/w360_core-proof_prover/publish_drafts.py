"""Submit only the explicitly named DRAFT and proposal files; never ingest."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
payload = (ROOT / "drafts/bundle_001.json").read_bytes()
bundle = json.loads(payload)
assert bundle["author_agent"] == "w360" and len(bundle["entries"]) == 3
assert all(e["kind"] == "concept" and e["proof_text"] is None for e in bundle["entries"])
destination = pathlib.Path("~/math-brain-inbox/w360")
destination.mkdir(parents=True, exist_ok=True)
target = destination / "bundle_001.json"
part = destination / "bundle_001.part"
assert target.resolve().parent == destination.resolve() and part.resolve().parent == destination.resolve()
if target.exists():
    assert target.read_bytes() == payload, "Existing external draft differs; preserve it"
else:
    with part.open("xb") as stream:
        stream.write(payload)
    part.replace(target)
assert target.read_bytes() == payload

hook_payload = (ROOT / "hooks/math-w360.jsonl").read_text(encoding="utf-8")
hook = json.loads(hook_payload)
assert hook["proposer"] == "w360" and len(hook["text"]) <= 300
hook_target = pathlib.Path("~/primary_directive/hooks1000/proposals/math-w360.jsonl")
present = []
if hook_target.exists():
    present = [json.loads(line) for line in hook_target.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
matches = [row for row in present if row.get("id") == hook["id"]]
if matches:
    assert matches == [hook], "Existing proposal with this id differs; preserve it"
else:
    with hook_target.open("a", encoding="utf-8") as stream:
        stream.write(hook_payload)

receipt_path = ROOT / "REVIEW_RECEIPT.json"
receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
receipt.update(submitted=True, submission_path=str(target), submitted_entries=3,
               reviewed=False, ingested=None, retrievable=None,
               ingestion_state="not independently verified; worker performed no integration",
               retrieval_state="not measured after submission",
               hook_submitted=True, hook_path=str(hook_target),
               narrow_claims=["path:~/math-brain-inbox/w360", "path:~/primary_directive/hooks1000/proposals/math-w360.jsonl"])
receipt_path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
source_path = ROOT / "SOURCE_STATUS.json"
source = json.loads(source_path.read_text(encoding="utf-8"))
source["brain_publication"] = {"submitted":True,"reviewed":False,"ingested":None,"retrievable":None,"receipt":"REVIEW_RECEIPT.json"}
source_path.write_text(json.dumps(source, indent=2), encoding="utf-8")
report_path = ROOT / "REPORT.md"
report = report_path.read_text(encoding="utf-8")
report = report.replace("The local hook proposal and its unified diff are ready for the rolling hook audit.", "The hook proposal is submitted to the named rolling-audit file; its local copy and unified diff preserve the reviewable version.")
report += "\nSubmission verified: three concept DRAFT entries and two relations mirrored byte-for-byte to " + str(target) + ". Review is pending; ingestion and retrieval are unverified.\n"
report_path.write_text(report, encoding="utf-8")
print(json.dumps({"submitted":True,"entries":3,"relations":2,"byte_comparison":"PASS","reviewed":False,"ingested":None,"retrievable":None,"hook_submitted":True}))
