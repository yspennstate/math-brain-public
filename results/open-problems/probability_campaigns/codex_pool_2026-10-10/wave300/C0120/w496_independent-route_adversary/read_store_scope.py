import json
import sqlite3
from pathlib import Path

target = Path('~/math-brain-build/local/population/brain.sqlite3')
conn = sqlite3.connect(target.as_uri() + '?mode=ro', uri=True, timeout=5)
rows = conn.execute("SELECT name, sql FROM sqlite_master WHERE type='table' AND name NOT LIKE '%fts%' AND name NOT LIKE '%audit%' AND name NOT LIKE '%test%' ORDER BY name").fetchall()
print(json.dumps(rows, ensure_ascii=False)[:16000])
conn.close()
