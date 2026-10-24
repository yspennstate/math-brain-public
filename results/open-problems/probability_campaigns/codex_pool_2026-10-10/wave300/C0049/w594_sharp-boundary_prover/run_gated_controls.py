"""Read the governor immediately before a tiny, sequential CPU check."""
import importlib.util
import json
import sys
import time
from pathlib import Path

root = Path(__file__).resolve().parent
state_path = Path('~/.claude/compute/compute_state.json')
state = json.loads(state_path.read_text(encoding='utf-8-sig'))
age = time.time()-state_path.stat().st_mtime
status = state.get('status')
allowed = status in ('ok','normal','warn') and 0 <= age <= 60
receipt = {'checked_at_epoch': time.time(), 'state_mtime_age_seconds': age,
           'state_timestamp': state.get('ts'), 'state_status': status,
           'allowed': allowed, 'policy': 'Fresh governor; refuse distress, unknown, or stale. Tiny CPU controls only.',
           'bounded_work': '128 FK configurations, 7 step sizes, 32 local cases, 4 paths; one process; no GPU, models or training',
           'cpu_pct': state.get('cpu_pct'), 'mem_avail_mb': state.get('mem_avail_mb'),
           'commit_avail_mb': state.get('commit_avail_mb'), 'disk_free_gb': state.get('disk_free_gb')}
path = root/'COMPUTE_GATE.json'
path.write_text(json.dumps(receipt, indent=2), encoding='utf-8')
print(json.dumps(receipt))
sys.argv = [str(root/'check_endpoint.py'), '--gate-receipt', str(path)]
spec = importlib.util.spec_from_file_location('endpoint_controls', root/'check_endpoint.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
raise SystemExit(module.main())
