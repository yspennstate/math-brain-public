"""Finalize the measured review state, with no new mathematical or live-system action."""
from datetime import datetime, timezone
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
validation=json.loads((ROOT/"VALIDATION.json").read_text(encoding="utf-8"))
states=json.loads((ROOT/"BUNDLE_STATES.json").read_text(encoding="utf-8"))
claims=[json.loads(x) for x in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
peers=[json.loads(x) for x in (ROOT/"PEER_VERDICTS.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
assert validation["verdict"]=="PASS" and validation["concept_entries"]==8 and validation["relations"]==8
assert states["submitted"] is True
assert sum(c["status"]=="independently checked proof" for c in claims)==5
assert sum(x["verdict"]=="KEEP" for x in peers)==4
assert json.loads((ROOT/"SOURCE_STATUS.json").read_text(encoding="utf-8"))["current_openness"]=="UNKNOWN"
next_line="NEXT: Referee certify the September manuscript's all-label crossing/no-fork bridge (Lemma3.5, Proposition6.1); w392 check C07 before theorem promotion."
for name in ("REPORT.md","review_packet/INDEX.md"):
    path=ROOT/name
    lines=[x for x in path.read_text(encoding="utf-8").splitlines() if not x.startswith("NEXT:")]
    path.write_text("\n".join(lines).rstrip()+"\n\n"+next_line+"\n",encoding="utf-8")
status_path=ROOT/"STATUS.md"
old=[x for x in status_path.read_text(encoding="utf-8-sig").splitlines() if not x.startswith("STATE:") and not x.startswith("NEXT:")]
stamp=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
log=f"{stamp}: Review packet complete and measured. Seven claim rows, five w389 KEEP verdicts, C03 FIX accepted, four w387 partial-result KEEP audits. Eight concept entries/eight supported relations submitted; offline validation PASS. Exact local controls and source receipts saved. C07 designated check and coordinator bundle/relation reviews pending; full target status UNKNOWN. No live store or integrator invoked by this worker."
status_path.write_text("STATE: NEEDS_REVIEW\n"+next_line+"\n"+"\n".join(old).strip()+"\n"+log+"\n",encoding="utf-8")
print(json.dumps({"state":"NEEDS_REVIEW","own_keeps":5,"paired_partial_keeps":4,"draft_entries":8,"draft_relations":8,"proof_status":"UNKNOWN","next":next_line}))
