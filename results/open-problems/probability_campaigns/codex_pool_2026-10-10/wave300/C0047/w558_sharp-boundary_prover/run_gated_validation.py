"""Fresh local compute admission, then one tiny foreground arithmetic check."""
import ctypes
import datetime
import json
import os
import runpy
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
state_path = Path('~/.claude/compute/compute_state.json')
checked = datetime.datetime.now(datetime.timezone.utc).isoformat()
state = json.loads(state_path.read_text(encoding='utf-8-sig'))
age = max(0.0, time.time() - state_path.stat().st_mtime)
keys = ('ts', 'status', 'mode', 'cpu_pct', 'mem_avail_mb', 'mem_load_pct',
        'commit_eff_avail_mb', 'commit_eff_used_pct', 'disk_free_gb')
snapshot = {k: state.get(k) for k in keys}
admitted = state.get('status') in {'ok', 'warn'} and age <= 60
admitted = admitted and float(state.get('mem_avail_mb', 0)) >= 256
admitted = admitted and float(state.get('disk_free_gb', 0)) >= 1
if state.get('mode') in {'distress', 'throttle'}:
    admitted = False

# This is the current foreground command only; no existing service or peer job is changed.
priority_set = False
if admitted and os.name == 'nt':
    k32 = ctypes.WinDLL('kernel32', use_last_error=True)
    k32.GetCurrentProcess.restype = ctypes.c_void_p
    k32.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_ulong]
    priority_set = bool(k32.SetPriorityClass(k32.GetCurrentProcess(), 0x4000))
    admitted = admitted and priority_set
gate = json.loads((ROOT / 'COMPUTE_GATE.json').read_text(encoding='utf-8'))
gate.update({'checked_at_utc': checked, 'governor_state_path': str(state_path),
             'governor_state_age_seconds': age, 'governor_snapshot': snapshot,
             'foreground_priority': 'BelowNormal' if priority_set else 'not set',
             'status': 'ADMITTED' if admitted else 'DENIED'})
(ROOT / 'COMPUTE_GATE.json').write_text(json.dumps(gate, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'gate': gate['status'], 'snapshot': snapshot, 'age_seconds': age}))
if not admitted:
    raise SystemExit(3)
runpy.run_path(str(ROOT / 'validate_boundary.py'), run_name='__main__')
