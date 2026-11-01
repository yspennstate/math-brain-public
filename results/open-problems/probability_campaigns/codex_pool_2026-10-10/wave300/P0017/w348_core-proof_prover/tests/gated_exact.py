"""Read current governor state, honor the live GPU gate, run one tiny CPU check.

No governor settings, process priorities, services or shared files are changed.
"""
from pathlib import Path
import datetime as dt
import importlib.util
import json
import runpy
import sys
import time

sys.dont_write_bytecode = True
base = Path(__file__).resolve().parents[1]
state_path = Path('~/.claude/compute/compute_state.json')
hook_path = Path('~/.claude/dreaming/compute_sense.py')
test_path = base/'tests'/'check_exact.py'
receipt_path = base/'checks'/'compute_gate.json'
receipt_path.parent.mkdir(exist_ok=True)

state = json.loads(state_path.read_text(encoding='utf-8-sig'))
age = time.time()-state_path.stat().st_mtime
spec = importlib.util.spec_from_file_location('w348_readonly_compute_hook', hook_path)
hook = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hook)
command = 'python -B -X utf8 ~/brain_workers/w348/tests/check_exact.py'
denial = hook._local_gpu_deny({
    'hook_event_name':'PreToolUse','tool_name':'PowerShell',
    'cwd':str(base),'tool_input':{'command':command}})
allowed = denial is None and 0 <= age <= 120
receipt = {
    'checked_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
    'state_file':str(state_path),'state_age_seconds':age,
    'governor_status':state.get('status'),'governor_mode':state.get('mode'),
    'reasons':state.get('reasons'),'cpu_pct':state.get('cpu_pct'),
    'mem_avail_mb':state.get('mem_avail_mb'),'proc_count':state.get('proc_count'),
    'live_gpu_gate_file':str(hook_path),'live_gpu_gate_denial':denial,
    'command':command,'decision':'ALLOW_BOUNDED_EXACT_CPU_CHECK' if allowed else 'DEFER',
    'scope':'One finite standard-library exact-arithmetic check; no random search, GPU, model, child workers, or ongoing process.',
    'policy':'Current compute_sense instruction: carry on with short local work; do not launch anything large during distress.',
    'shared_policy_changed':False}
receipt_path.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
if not allowed:
    print(json.dumps({'decision':'DEFER','state_age_seconds':age,'gate_denial':denial}))
    raise SystemExit(3)
print(json.dumps({'decision':receipt['decision'],'state_age_seconds':age,
                  'governor_status':state.get('status'),'receipt':str(receipt_path)}))
runpy.run_path(str(test_path),run_name='__main__')
