"""Honor a fresh live pressure gate before the tiny exact-arithmetic check."""
import json
import pathlib
import sys
import time

sys.dont_write_bytecode=True
ROOT=pathlib.Path(__file__).resolve().parent
path=pathlib.Path("~/.claude/compute/compute_state.json")
start=time.time()
state=json.loads(path.read_text(encoding="utf-8-sig"))
age=max(0,start-path.stat().st_mtime)
fields=["ts","status","mode","reasons","cpu_pct","mem_avail_mb","commit_eff_avail_mb","commit_eff_used_pct","disk_queue","hung_windows","proc_count"]
receipt={"checked_at_epoch":start,"state_age_seconds":age,"source":str(path),"scope":"single exact-fraction hexagon check; twelve meshes; no GPU/model/process creation","state":{key:state.get(key) for key in fields}}
issues=[]
if age>60: issues.append("state older than 60 seconds")
if state.get("status") not in ("ok","warn"): issues.append("live pressure status is not ok/warn")
if state.get("mode") not in ("full","normal","idle_full","owner_present_polite","throttle","polite","owner_active","steady"): issues.append("unknown or paused gate mode")
if state.get("hung_windows") is None or state["hung_windows"]: issues.append("UI telemetry missing or reports a hung window")
for key,minimum in (("mem_avail_mb",4096),("commit_eff_avail_mb",4096)):
    value=state.get(key)
    if not isinstance(value,(int,float)) or value<minimum: issues.append(key+" lacks required headroom")
value=state.get("cpu_pct")
if not isinstance(value,(int,float)) or value>=90: issues.append("CPU saturated or telemetry missing")
receipt["permitted"]=not issues
receipt["issues"]=issues
(ROOT/"compute_gate_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
if issues:
    print(json.dumps({"checker_status":"not run","gate":receipt}))
    raise SystemExit(2)
import verify_cycle_modes
verify_cycle_modes.main()
receipt["checker_status"]="passed"
(ROOT/"compute_gate_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
