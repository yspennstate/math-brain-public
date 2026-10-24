"""Read-only local governor gate for a tiny single-core numerical check."""
import datetime
import json
import time
from pathlib import Path

STATE = Path('~/.claude/compute/compute_state.json')

def check():
    result = {'checked_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'state_path': str(STATE), 'proposed_job': 'single-core auxiliary quadrature, no GPU, no training'}
    try:
        age = time.time() - STATE.stat().st_mtime
        state = json.loads(STATE.read_text(encoding='utf-8-sig'))
        result['age_seconds'] = age
        result['state_keys'] = list(state)
        result['selected_scalars'] = {k: v for k, v in state.items()
            if isinstance(v, (str, float, int, bool, type(None)))
            and any(term in k.lower() for term in ('utc', 'time', 'distress', 'status', 'level', 'commit', 'ram', 'disk', 'freeze', 'hung'))}
        required=('status','mode','cpu_pct','mem_avail_mb','commit_used_pct','commit_avail_mb','disk_free_gb','hung_windows')
        result['selected_scalars'].update({k:state.get(k) for k in required})
        result['reasons']=state.get('reasons')
        missing=[k for k in required if k not in state]
        numeric=('cpu_pct','mem_avail_mb','commit_used_pct','commit_avail_mb','disk_free_gb','hung_windows')
        valid=not missing and all(isinstance(state[k],(int,float)) for k in numeric)
        result['allowed']=(valid and 0<=age<=120 and state['status'] not in ('distress','critical')
            and state['mode']!='throttle' and state['cpu_pct']<95 and state['mem_avail_mb']>8192
            and state['commit_used_pct']<85 and state['commit_avail_mb']>16384
            and state['disk_free_gb']>3 and state['hung_windows']==0)
        result['reason']='fresh governor and conservative single-core headroom check passed' if result['allowed'] else 'numerical work withheld: stale/missing telemetry or governor/physical/commit/CPU/UI pressure'
    except Exception as exc:
        result['allowed'] = False
        result['reason'] = str(exc)
    Path('compute_gate_latest.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))
    return result

if __name__ == '__main__':
    check()
