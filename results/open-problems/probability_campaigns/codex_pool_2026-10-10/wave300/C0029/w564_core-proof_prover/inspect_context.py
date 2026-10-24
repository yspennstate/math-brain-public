import json
import sqlite3
from pathlib import Path

state_path = Path('~/.claude/compute/compute_state.json')
state = json.loads(state_path.read_text(encoding='utf-8-sig'))
selected = {k: state[k] for k in ('ts', 'host', 'status', 'reasons', 'cpu_pct',
            'available_mb', 'avail_mb', 'commit_pct', 'commit_used_mb',
            'commit_limit_mb', 'ai_tagged_private_mb') if k in state}
selected['file_mtime'] = state_path.stat().st_mtime
print('LOCAL_COMPUTE', json.dumps(selected, ensure_ascii=False))
db = Path('~/.agents/coordination/agent_mesh.sqlite3')
with sqlite3.connect(db.as_uri() + '?mode=ro', uri=True, timeout=2) as conn:
    print('ACTIVE_PROBABILITY_TEAMS', conn.execute(
        "SELECT campaign_id,name FROM campaigns WHERE status='active' AND "
        "(name LIKE '%probability%' OR name LIKE '%C0029%') LIMIT 25").fetchall())
    print('PEER_COLUMNS', [r[1] for r in conn.execute('PRAGMA table_info(agents)')])
    print('PEER_TEAMS', conn.execute(
        "SELECT a.agent_id,a.campaign_id,c.name FROM agents a LEFT JOIN campaigns c "
        "ON c.campaign_id=a.campaign_id WHERE a.agent_id IN ('w564','w565','w566')").fetchall())
