"""Inspect only schema and target-matching cards of a read-only math store."""
import json
import pathlib
import sqlite3
import time

root = pathlib.Path(__file__).resolve().parent
db = '~/math-brain-build/local/population/brain.sqlite3'
started = time.perf_counter()
conn = sqlite3.connect('file:'+db+'?mode=ro', uri=True, timeout=5)
conn.execute('PRAGMA query_only=ON')
schemas = [dict(name=name, sql=sql) for name, sql in conn.execute(
    "SELECT name,sql FROM sqlite_master WHERE type='table' AND (name IN ('nodes','claims','sources','edges') OR name LIKE '%fts%')")]
(root/'store_schema.json').write_text(json.dumps(schemas, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(dict(db=db, mode='read-only', elapsed_s=time.perf_counter()-started, schemas=schemas), ensure_ascii=False))
conn.close()
