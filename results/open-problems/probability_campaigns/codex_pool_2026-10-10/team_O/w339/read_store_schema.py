import sqlite3
from pathlib import Path

p = Path('~/math-brain-build/local/population/brain.sqlite3')
with sqlite3.connect(p.as_uri() + '?mode=ro', uri=True, timeout=3) as db:
    rows = db.execute("SELECT name, sql FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'").fetchall()
text = '\n\n'.join(f'{name}\n{sql}' for name, sql in rows)
Path(__file__).with_name('store_schema.txt').write_text(text, encoding='utf-8')
print(text[:15000])
