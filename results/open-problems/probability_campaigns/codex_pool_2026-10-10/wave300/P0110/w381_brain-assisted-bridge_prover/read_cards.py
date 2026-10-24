"""Read a bounded set of task-named math cards from SQLite, strictly read-only."""
import json
import sqlite3
import time
from pathlib import Path

root = Path(__file__).resolve().parent
db = Path(r'~\math-brain-build\local\population\brain.sqlite3')
started = time.perf_counter()
with sqlite3.connect(db.resolve().as_uri()+'?mode=ro', uri=True, timeout=5) as conn:
    conn.execute('PRAGMA query_only=ON')
    names = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('nodes','claims','edges')")]
    print('tables', names)
    columns = {t:[r[1] for r in conn.execute('PRAGMA table_info('+t+')')] for t in names}
    print('columns', json.dumps(columns))
    rows = conn.execute("SELECT id,title,body,metadata_json FROM nodes WHERE title LIKE '%An iid FPP law with proved KPZ exponent relation%' OR title LIKE 'Chatterjee (2013)%' ORDER BY title LIMIT 4").fetchall()
    cards=[]
    for ident,title,body,metadata in rows:
        claim=conn.execute('SELECT payload_json FROM claims WHERE id=?',(ident,)).fetchone()
        cards.append({'id':ident,'title':title,'body':body,'metadata':json.loads(metadata),'claim':json.loads(claim[0]) if claim else None})
    (root/'brain_cards.json').write_text(json.dumps(cards,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps(cards,ensure_ascii=False,indent=2))
receipt={'database':str(db),'access':'mode=ro; PRAGMA query_only=ON','elapsed_seconds':time.perf_counter()-started,'returned_cards':len(cards),'max_cards':4,'filter':'exact target title or Chatterjee (2013) conditional hypothesis card'}
(root/'brain_cards_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt))
