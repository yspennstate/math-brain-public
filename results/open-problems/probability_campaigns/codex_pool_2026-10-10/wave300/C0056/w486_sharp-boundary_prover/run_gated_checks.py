"""Check the actual governor immediately before a small, bounded CPU calculation."""
import json
import math
import runpy
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
state_file = Path('~/.claude/compute/compute_state.json')
receipt = {'state_file': str(state_file), 'job': '27 bounded stdlib scalar/cutoff checks',
           'gpu_used': False, 'models_loaded': False, 'subprocesses_started': False}
try:
    state = json.loads(state_file.read_text(encoding='utf-8-sig'))
    age = time.time() - state_file.stat().st_mtime
    receipt.update({
        'age_seconds': age, 'status': state.get('status'), 'mode': state.get('mode'),
        'cpu_pct': state.get('cpu_pct'), 'mem_avail_mb': state.get('mem_avail_mb'),
        'commit_avail_mb': state.get('commit_avail_mb'), 'disk_free_gb': state.get('disk_free_gb'),
        'checked_at_epoch': time.time(),
    })
    valid = all(isinstance(receipt[k], (int, float)) and math.isfinite(receipt[k])
                for k in ('cpu_pct', 'mem_avail_mb', 'commit_avail_mb', 'disk_free_gb'))
    receipt['allowed'] = valid and 0 <= age <= 600 and state.get('status') in ('ok', 'warn')
    receipt['decision'] = 'ALLOW' if receipt['allowed'] else 'HOLD'
except (OSError, ValueError, TypeError) as error:
    receipt.update({'allowed': False, 'decision': 'HOLD', 'error': str(error)})

(ROOT / 'GATE_RECEIPT.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
if receipt['allowed']:
    runpy.run_path(str(ROOT / 'verify_geometry.py'), run_name='__main__')
else:
    held = {'status': 'HELD_BY_FRESH_COMPUTE_GATE', 'numerical_checks_run': 0,
            'gate': receipt,
            'limitation': 'Numerical checks are optional sanity checks of the complete analytic author proof. No numerical or deployed-brain improvement claim is made.'}
    (ROOT / 'MEASUREMENTS.json').write_text(json.dumps(held, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(held))
