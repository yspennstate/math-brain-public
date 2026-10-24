"""One targeted live read-only measurement; no test bank or store mutation."""
from pathlib import Path
import json
import sqlite3
import time
from candidate_alias_ro import resolve_candidate

ROOT = Path(__file__).resolve().parent
database = Path('~/math-brain-build/local/population/brain.sqlite3')
started = time.monotonic()
with sqlite3.connect(database.as_uri()+'?mode=ro', uri=True, timeout=3) as connection:
    before = connection.execute('SELECT COUNT(*) FROM nodes WHERE title LIKE ? OR body LIKE ?', ('%C0041%','%C0041%')).fetchone()[0]
after = resolve_candidate(database, 'C0041')
invalid_rejected = 0
for invalid in ('C0041 OR 1=1', 'C00410', 'C004', '%', 'C0041;DROP'):
    try:
        resolve_candidate(database, invalid)
    except ValueError:
        invalid_rejected += 1
unknown = resolve_candidate(database, 'C9999')
lowercase = resolve_candidate(database, 'c0041')
assert before == 0, 'Baseline changed: recompute conclusions before reporting'
assert len(after) == 1, 'Expected unique exact C0041 problem card'
assert after[0]['id'] == lowercase[0]['id']
assert not unknown and invalid_rejected == 5
record = {'command':'python -B -X utf8 ~/brain_workers/w454/measure_alias.py', 'scope':'Exact candidate-ID lookup only; title/body SQL baseline, not a full recall benchmark', 'before_title_body_matches':before, 'after_exact_metadata_alias_matches':len(after), 'retrieved_id':after[0]['id'], 'retrieved_logical_id':json.loads(after[0]['metadata_json'])['logical_id'], 'unknown_id_matches':len(unknown), 'invalid_queries_rejected':invalid_rejected, 'case_equivalence':True, 'elapsed_seconds':time.monotonic()-started, 'deployed':False}
(ROOT/'alias_measurement.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps(record,indent=2))
