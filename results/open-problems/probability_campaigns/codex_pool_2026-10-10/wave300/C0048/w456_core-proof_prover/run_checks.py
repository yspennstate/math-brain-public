"""Fresh read-only governor gate, followed immediately by one bounded CPU check."""
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import time

root = Path(__file__).resolve().parent
state_path = Path('~/.claude/compute/compute_state.json')
receipt_path = root / 'compute_gate.json'
now = time.time()
receipt = {
    'checked_at_utc': datetime.now(timezone.utc).isoformat(),
    'source': str(state_path),
    'doctrine': '~/<private-repo>/12_cognitive_architecture/compute_governor/COMPUTE_DOCTRINE.md',
    'allowed': False,
    'job': {'processes': 1, 'gpu': False, 'model_load': False, 'max_vertices': 4, 'max_edges': 6, 'max_cases': 72, 'max_cpu_seconds': 5},
    'priority': 'inherited; no promotion or governor modification',
}
try:
    state = json.loads(state_path.read_text(encoding='utf-8-sig'))
    age = now - state_path.stat().st_mtime
    status = state.get('status')
    reasons = state.get('reasons') or []
    if isinstance(reasons, str):
        reasons = [reasons]
    danger = any(any(term in str(reason).lower() for term in ('distress', 'critical', 'hung', 'explicit_stop')) for reason in reasons)
    receipt.update({'source_age_seconds': age, 'status': status, 'mode': state.get('mode'), 'reasons': reasons})
    # Only local scalar telemetry is retained. No remote, trading or process details are copied.
    keys = ('cpu_pct', 'cpu_percent', 'ram_free_mb', 'free_ram_mb', 'commit_free_mb', 'commit_headroom_mb', 'disk_free_gb', 'physical_available_mb', 'commit_used_pct')
    receipt['local_metrics'] = {key: state[key] for key in keys if isinstance(state.get(key), (int, float))}
    receipt['allowed'] = status in ('ok', 'warn') and 0 <= age <= 300 and not danger
    receipt['decision'] = 'permitted bounded short CPU arithmetic' if receipt['allowed'] else 'held by status, freshness or explicit pressure reason'
except (OSError, ValueError) as exc:
    receipt['decision'] = 'held: unavailable governor telemetry'
    receipt['error'] = type(exc).__name__
receipt_path.write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps(receipt), flush=True)
if not receipt['allowed']:
    raise SystemExit(75)
import verify_cumulants
sys.argv = [str(root / 'verify_cumulants.py'), '--gate-receipt', str(receipt_path)]
raise SystemExit(verify_cumulants.main())
