"""Read the existing compute gate without changing it or contacting any machine."""
import json
import time
from pathlib import Path

root = Path(__file__).resolve().parent
path = Path('~/.claude/compute/compute_state.json')
out = {'path': str(path), 'checked_epoch': time.time(), 'new_processes': 0, 'new_threads': 0}
try:
    state = json.loads(path.read_text(encoding='utf-8-sig'))
    out['file_age_seconds'] = time.time() - path.stat().st_mtime
    out['top_level_keys'] = sorted(state)
    for key in ('status', 'overall', 'mode', 'ts', 'timestamp', 'level'):
        if key in state:
            value = state[key]
            if isinstance(value, (str, int, float, bool, type(None))):
                out[key] = value
    # Report field names only; do not report remote-machine data or process details.
    for key in ('local', 'machines', 'hosts', 'boxes'):
        value = state.get(key)
        if isinstance(value, dict):
            out[key + '_keys'] = sorted(value)
except (OSError, ValueError) as exc:
    out['error'] = str(exc)
(root / 'GATE_INSPECTION.json').write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
print(json.dumps(out))
