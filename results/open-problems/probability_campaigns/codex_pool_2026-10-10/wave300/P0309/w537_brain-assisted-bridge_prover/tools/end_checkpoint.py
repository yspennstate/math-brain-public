"""End this authorized task with a measured, reviewable checkpoint."""
from datetime import datetime, timezone
import json
from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
required=["STATUS.md","SOURCE_STATUS.json","ATTEMPT.md","CLAIMS.jsonl","REPORT.md","review/REVIEW_PACKET.md","review/FINAL_HANDOFF.md","review/SCOPED_KEEP_RECEIPTS.jsonl","draft_bundle/bundle_001.json","BUNDLE_STATUS.json","patches/01_p0309_target_lookup.diff","evidence/retrieval_metrics.json","evidence/bundle_validation.json","evidence/helper_validation.json","HOOK_PROPOSALS.jsonl"]
assert all((root/name).is_file() for name in required)
state=json.loads((root/"BUNDLE_STATUS.json").read_text(encoding="utf-8"))
assert state["submitted"] and state["reviewed"] and not state["ingested"] and not state["retrievable"]
claims=[json.loads(line) for line in (root/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
assert len(claims)==5 and all(row["status"]=="independently checked proof" for row in claims)
status=(root/"STATUS.md").read_text(encoding="utf-8-sig")
assert status.startswith("STATE: WORKING")
status=status.replace("STATE: WORKING","STATE: NEEDS_REVIEW",1)
next_step="NEXT: For s=1, prove o(N) probability cost of a nonzero Fourier-response sector under the unrestricted neutral periodic Coulomb law at fixed finite beta."
status=re.sub(r"^NEXT:.*$",next_step,status,count=1,flags=re.M)
status+="\n2026-10-10: Final checkpoint: w539 scoped KEEP C1-C5 registered; w538 also kept the conditional reductions. Submitted seven concept-only draft entries with eight exact supported relations. No parent P0309 proof, live recall change, ingestion or new-node retrievability claimed.\n2026-10-10: Reviewable optional helper/diff returns 2/2 exact cards in 0.068 s on one replay; general recall was 0/3 in 51.943 s; rejected metadata scan took 133.529 s. Scopes differ. Schema/identity checks passed; numerical surrogate checks denied by a fresh process_critical gate. Different-model/source/edge integration gates and reviewer deployment remain pending.\n"
(root/"STATUS.md").write_text(status,encoding="utf-8")
receipt={"state":"NEEDS_REVIEW","at_utc":datetime.now(timezone.utc).isoformat(),"mandatory_files":required,"claims_independently_kept":5,"draft_submitted":True,"mathematical_claim_review_completed":True,"bundle_edge_and_model_gates_completed":False,"live_store_modified":False,"parent_proved":False,"next":next_step}
(root/"evidence/final_receipt.json").write_text(json.dumps(receipt,indent=2),encoding="utf-8")
print(json.dumps(receipt))
