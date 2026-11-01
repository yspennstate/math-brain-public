"""Tiny artifact check only; no numerical experiment or live-store mutation."""
from pathlib import Path
import datetime as dt
import json

root=Path(__file__).resolve().parent
expected=("STATUS.md","SOURCE_STATUS.json","ATTEMPT.md","INDEPENDENT.md","NEAR_TIE_LEMMA.md","CLAIMS.jsonl","AUDIT.jsonl","PAIR_AUDIT.md","REVIEW_PACKET.md","REPORT.md","VALIDATION.json","SUBMISSION.json","bundle_001.json","HOOK_PROPOSAL.jsonl","patches/01_competing_path_hook.diff")
assert all((root/p).is_file() for p in expected)
claims=[json.loads(s) for s in (root/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()]
audits=[json.loads(s) for s in (root/"AUDIT.jsonl").read_text(encoding="utf-8").splitlines()]
hook=json.loads((root/"HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8"))
submission=json.loads((root/"SUBMISSION.json").read_text(encoding="utf-8"))
validation=json.loads((root/"VALIDATION.json").read_text(encoding="utf-8"))
assert len(claims)==6 and len(audits)==6
assert [a["verdict"] for a in audits].count("KEEP")==5 and audits[-1]["verdict"]=="OPEN"
assert len(hook["text"])<=300 and hook["fire_when"] and hook["silent_when"]
assert submission["submitted"] and not submission["reviewed"]
assert Path(submission["path"]).read_bytes()==(root/"bundle_001.json").read_bytes()
assert validation["structural"]["integrator_parse_errors"]==[]
result={"checked_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"files_present":len(expected),"claims":len(claims),"qualified_author_step_keeps":5,"open_full_target_gap":1,"hook_rows":1,"inbox_delivery_matches":True,"formal_proof_check":False,"numeric_controls":validation["numerical_status"],"independent_mathematical_review":"pending w518","ingestion_and_retrieval":"not confirmed by this worker"}
(root/"FINAL_CHECK.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result))
