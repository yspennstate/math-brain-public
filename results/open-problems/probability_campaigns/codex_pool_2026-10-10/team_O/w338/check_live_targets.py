"""Optional, scoped current-target check. The SQLite connection is read-only."""
from pathlib import Path
import json
import sqlite3

root = Path(__file__).resolve().parent
quotes = [json.loads(line) for line in (root/'edge_evidence.jsonl').read_text(encoding='utf-8').splitlines()]
targets = sorted(set(q['to_existing_logical'] for q in quotes))
report = dict(connection_mode='ro',targets_requested=len(targets),store_writes=0)
try:
    uri = 'file:~/math-brain-build/local/population/brain.sqlite3?mode=ro'
    with sqlite3.connect(uri,uri=True,timeout=2) as connection:
        columns = {row[1] for row in connection.execute('PRAGMA table_info(nodes)')}
        if not {'metadata_json','body'} <= columns:
            raise RuntimeError('Current node schema differs; defer live resolution to the integrator.')
        placeholders = ','.join('?' for _ in targets)
        rows = list(connection.execute(
            "SELECT json_extract(metadata_json,'$.logical_id'),body FROM nodes "
            f"WHERE json_extract(metadata_json,'$.logical_id') IN ({placeholders})",targets))
        bodies = {}
        for logical,body in rows:bodies.setdefault(logical,[]).append(body)
        missing = [t for t in targets if t not in bodies]
        unmatched = [q['to_existing_logical'] for q in quotes
                     if not any(q['to_quote'] in b for b in bodies.get(q['to_existing_logical'],[]))]
        report.update(status='PASS_READ_ONLY_LIVE_TARGETS' if not missing and not unmatched else 'LIVE_TARGET_REVIEW_REQUIRED',
                      targets_found=len(bodies),missing_targets=missing,unmatched_quote_targets=unmatched)
except (sqlite3.Error,RuntimeError) as exc:
    report.update(status='UNVERIFIED_LIVE_TARGETS',reason=str(exc))
(root/'live_target_validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
