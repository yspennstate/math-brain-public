"""Check artifact structure, record receipts and route the existing review packet."""
from __future__ import annotations
import hashlib
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parent
MESH=Path("~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py")


def dump(path,obj):
    path.write_text(json.dumps(obj,indent=2)+"\n",encoding="utf-8")


def send(to,topic,body):
    p=subprocess.run(["python","-X","utf8",str(MESH),"send","--agent","w408","--to",to,"--topic",topic,"--kind","message","--body",body],capture_output=True,text=True,encoding="utf-8",errors="replace",timeout=90)
    try:
        receipt=json.loads(p.stdout)
    except json.JSONDecodeError:
        receipt={"stdout":p.stdout[:700],"stderr":p.stderr[:400]}
    item={"date":"2026-10-10","to":to,"topic":topic,"returncode":p.returncode,"receipt":receipt}
    with (ROOT/"COMMUNICATIONS.jsonl").open("a",encoding="utf-8") as f:
        f.write(json.dumps(item)+"\n")
        f.flush()
    return item


def main():
    required={"statement","assumptions","source","proof_or_counterexample","independent_reviewer","remaining_gap","status"}
    claims=[json.loads(s) for s in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
    assert len(claims)==10 and len({r["id"] for r in claims})==10
    assert all(required<=r.keys() for r in claims)
    assert next(r for r in claims if r["id"]=="w408-S1.9")["status"]=="conjecture"
    bundle=json.loads((ROOT/"drafts/bundle_001.json").read_text(encoding="utf-8"))
    assert len(bundle["entries"])==5 and len(bundle["relations"])==7
    assert all(e["kind"] in {"definition","concept"} and e["proof_text"] is None for e in bundle["entries"])
    state=json.loads((ROOT/"INTEGRATION_STATE.json").read_text(encoding="utf-8"))
    assert not state["full_target_solved"] and state["different_model_review_gate"]=="NOT_PASSED"
    state["reviewed"]["global_revision_review_request"]="msg-f445d719de"
    dump(ROOT/"INTEGRATION_STATE.json",state)
    measurements=json.loads((ROOT/"MEASUREMENTS.json").read_text(encoding="utf-8"))
    assert measurements["status"]=="HELD" and measurements["tested_states"]==0
    dump(ROOT/"PACKET_VALIDATION.json",{
        "scope":"artifact structure only; not a mathematical or numerical proof check",
        "claims":len(claims),"draft_entries":5,"draft_relations":7,
        "unreviewed_theorem_promotions":0,"missing_input_label":"conjecture",
        "arithmetic_states_tested":0,"validation":"PASS",
    })
    names=["ATTEMPT.md","GLOBAL_EXHAUSTION.md","COUNTEREXAMPLES.md","CLAIMS.jsonl","SOURCE_STATUS.json","REPORT.md","MEASUREMENTS.json","REVIEW_PACKET.md","review/w410_verdicts.jsonl"]
    hashes={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in names}
    dump(ROOT/"ARTIFACT_FINGERPRINTS.json",{"purpose":"review artifact byte identity only; not a proof/served-model/store-seal receipt","sha256":hashes})
    summary=("w408 C0017 review-ready: ~/brain_workers/w408/REPORT.md and REVIEW_PACKET.md; "
             "DRAFT ~/math-brain-inbox/w408/bundle_001.json (5 entries/7 relations). "
             "w410 5 scoped KEEP/1 global FIX; fixed construction GLOBAL_EXHAUSTION.md awaits w413 (msg-f445d719de). "
             "Square-bond stopped Cardy input UNPROVED, current openness UNKNOWN, arithmetic HELD/0 states, "
             "author/referee response-served models UNAVAILABLE; no different-model or parent-solved gate. "
             "ATTEMPT.md sha256="+hashes["ATTEMPT.md"]+"; all exact paths/hashes ARTIFACT_FINGERPRINTS.json. "
             "Please route source correction STORE_CORRECTION.md and staged HOOK_PROPOSALS.jsonl/PROGRESS_EVENT.txt.")
    dump(ROOT/"INTEGRATION_HANDOFF.json",{"recipient":"codex-01a12190","body":summary,"scoped_review_receipt":"review/w410_verdicts.jsonl","unresolved_gap":"square-bond stopped Cardy martingale approximation","served_model_evidence":"UNAVAILABLE"})
    print(json.dumps(send("codex-01a12190","probability300-integration",summary)))
    print(json.dumps(send("w410","probability-C0017-global-fix","Applied your global FIX explicitly in ~/brain_workers/w408/GLOBAL_EXHAUSTION.md; independent new-construction review requested from w413. ATTEMPT.md and REVIEW_PACKET.md updated; frozen file bytes in ARTIFACT_FINGERPRINTS.json. The event candidate is now explicit. Local KEEP remains scoped; square-bond Cardy input unproved, arithmetic HELD. No parent or model-gate promotion.")))
    print(json.dumps({"final_packet":"validated","claims":10,"numerical_states_tested":0,"draft_entries":5,"draft_relations":7}))


if __name__=="__main__":
    main()
