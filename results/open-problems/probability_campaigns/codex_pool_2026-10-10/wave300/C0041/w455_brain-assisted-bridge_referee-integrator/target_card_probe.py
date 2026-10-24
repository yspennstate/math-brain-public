import json
import sqlite3
from pathlib import Path

db = Path('~/math-brain-build/local/population/brain.sqlite3')
conn = sqlite3.connect('file:' + db.as_posix() + '?mode=ro', uri=True, timeout=8)
conn.execute('PRAGMA query_only=ON')
patterns = ['%C0041%', '%directional transience%', '%ballisticity%', '%regeneration time%']
counts = {}
for p in patterns:
    counts[p] = conn.execute('SELECT count(*) FROM nodes WHERE lower(title) LIKE lower(?) OR lower(body) LIKE lower(?)', (p,p)).fetchone()[0]
selected = conn.execute("SELECT id,title,body,metadata_json FROM nodes WHERE title LIKE 'Open problem: Transience in a direction implies ballisticity%' LIMIT 2").fetchall()
cards=[]
for id_, title, body, raw in selected:
    meta=json.loads(raw)
    cards.append({'id':id_, 'title':title, 'body':body, 'logical_id':meta.get('logical_id'), 'conditions':meta.get('conditions'), 'source_id':meta.get('source_id'), 'truth_status':meta.get('truth_status'), 'has_exact_id_in_searchable_text':'C0041' in title+body})
conn.close()
receipt={'store':str(db), 'sql_mode':'read-only', 'query':'count title/body term matches plus exact C0041 open-problem title, no store mutation', 'counts':counts, 'cards':cards}
Path(__file__).with_name('target_card_receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
