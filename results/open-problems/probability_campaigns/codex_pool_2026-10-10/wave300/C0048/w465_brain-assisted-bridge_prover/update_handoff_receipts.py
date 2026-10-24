import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
state=json.loads((ROOT/"SUBMISSION_STATE.json").read_text(encoding="utf-8"))
pilot=json.loads((ROOT/"evidence/draft_recall_pilot.json").read_text(encoding="utf-8"))
state["local_ranking_pilot"]={"receipt":"evidence/draft_recall_pilot.json","before_conditional_bridge_hits_at_5":pilot["before"]["conditional_bridge_hits_at_5"],"after_conditional_bridge_hits_at_5":pilot["after"]["conditional_bridge_hits_at_5"],"scope":pilot["scope"],"elapsed_seconds":pilot["elapsed_seconds"]}
(ROOT/"SUBMISSION_STATE.json").write_text(json.dumps(state,indent=2)+"\n",encoding="utf-8")
failure=json.loads((ROOT/"RETRIEVAL_FAILURE.json").read_text(encoding="utf-8"))
failure["bounded_repair_measurement"]=state["local_ranking_pilot"]
(ROOT/"RETRIEVAL_FAILURE.json").write_text(json.dumps(failure,indent=2)+"\n",encoding="utf-8")
hook=json.loads((ROOT/"HOOK_PROPOSALS.jsonl").read_text(encoding="utf-8"))
assert len(hook["text"])<=300
print(json.dumps({"status":"NEEDS_REVIEW","draft_submission":state["submitted"],"reviewed":state["reviewed"],"ingested":state["ingested"],"live_retrievable":state["retrievable"],"local_bridge_hits_before":pilot["before"]["conditional_bridge_hits_at_5"],"local_bridge_hits_after":pilot["after"]["conditional_bridge_hits_at_5"],"hook_text_length":len(hook["text"]),"parent_problem_proved":False}))
