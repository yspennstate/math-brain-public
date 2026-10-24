"""One fresh read-only pressure check, then a single tiny exact CPU control batch."""
from pathlib import Path
from datetime import datetime
import json
import math
import runpy

ROOT = Path(__file__).resolve().parent
state_path = Path('~/.claude/compute/compute_state.json')
state = json.loads(state_path.read_text(encoding='utf-8'))
stamp = datetime.fromisoformat(state['ts'])
age = (datetime.now() - stamp).total_seconds()  # governor ts is laptop local time
keys = ['ts', 'status', 'mode', 'reasons', 'cpu_pct', 'mem_avail_mb',
        'commit_avail_mb', 'commit_used_pct', 'commit_eff_avail_mb',
        'commit_eff_used_pct', 'disk_queue', 'disk_free_gb', 'hung_windows']
receipt = {key: state.get(key) for key in keys}
receipt.update({
    'checked_at_local': datetime.now().isoformat(), 'age_seconds': age,
    'policy': 'compute_governor/COMPUTE_DOCTRINE.md: fresh pressure check; owner_present_polite continues scoped work; throttle/distress holds this batch; memory warning floors retained.',
    'work': 'one foreground standard-library CPU batch: 256 exact square assignments, 12 geometry controls; no models, GPU, parallel workers, or sampling',
})
holds = []
if not 0 <= age <= 60:
    holds.append('fresh local telemetry unavailable')
if state.get('status') in ['distress', 'critical', 'stop'] or state.get('mode') in ['throttle', 'stop']:
    holds.append('published pressure holds new batch')
for key in ['cpu_pct', 'mem_avail_mb', 'commit_avail_mb', 'commit_used_pct', 'disk_queue', 'disk_free_gb']:
    value = state.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        holds.append('missing finite telemetry: ' + key)
if state.get('mem_avail_mb', 0) <= 8192 or state.get('commit_avail_mb', 0) <= 16384 or state.get('commit_used_pct', 100) >= 85:
    holds.append('physical/commit memory pressure floor')
if state.get('commit_eff_avail_mb', state.get('commit_avail_mb', 0)) <= 16384 or state.get('commit_eff_used_pct', state.get('commit_used_pct', 100)) >= 85:
    holds.append('effective commit pressure floor')
if state.get('hung_windows'):
    holds.append('hung-window signal')
if any(str(reason).lower() in ['stop', 'explicit_stop'] or 'critical' in str(reason).lower() for reason in state.get('reasons', [])):
    holds.append('explicit/critical reason')
receipt['decision'] = 'HOLD' if holds else 'ALLOW_ONE_TINY_BATCH'
receipt['holds'] = holds
history = ROOT / 'COMPUTE_GATES.jsonl'
if not history.exists() and (ROOT / 'COMPUTE_GATE.json').exists():
    previous = json.loads((ROOT / 'COMPUTE_GATE.json').read_text(encoding='utf-8'))
    history.write_text(json.dumps(previous) + '\n', encoding='utf-8')
with history.open('a', encoding='utf-8') as handle:
    handle.write(json.dumps(receipt) + '\n')
    handle.flush()
(ROOT / 'COMPUTE_GATE.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps(receipt, indent=2))
if holds:
    raise SystemExit(3)
runpy.run_path(str(ROOT / 'tests' / 'verify_shortcut_controls.py'), run_name='__main__')
