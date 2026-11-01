"""Inspect only the local governor gate; no writes or remote queries."""
import json
from pathlib import Path
import time

path=Path('~/.claude/compute/compute_state.json')
if not path.is_file():
    print('NO_GOVERNOR_STATE')
else:
    data=json.loads(path.read_text(encoding='utf-8-sig'))
    print('age_seconds',round(time.time()-path.stat().st_mtime,2))
    for name in ('status','mode','cpu_pct','mem_avail_mb','commit_avail_mb','disk_free_gb'):
        if name in data:
            print(name,json.dumps(data[name],ensure_ascii=False)[:1500])
    print('hung_window_count',len(data.get('hung_windows') or []))
