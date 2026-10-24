"""Scoped, read-only math-brain retrieval; no full-store or model load."""
import json
from pathlib import Path
import sqlite3
import time

ROOT=Path(__file__).resolve().parent
db=Path('~/math-brain-build/local/population/brain.sqlite3')
start=time.monotonic()
with sqlite3.connect(db.as_uri()+'?mode=ro',uri=True) as conn:
    conn.execute('PRAGMA query_only=ON')
    conn.row_factory=sqlite3.Row
    conn.set_progress_handler(lambda: int(time.monotonic()-start>45),10000)
    hits=conn.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE (title LIKE '%Cardy%' OR (title LIKE '%conformal%' AND title LIKE '%percolation%') OR (title LIKE '%Smirnov%' AND title LIKE '%percolation%') OR body LIKE '%C0017%') ORDER BY CASE WHEN body LIKE '%C0017%' THEN 0 WHEN title LIKE '%Smirnov%' THEN 1 ELSE 2 END, title LIMIT 7").fetchall()
    cards=[]
    for hit in hits:
        card=dict(hit)
        card['metadata']=json.loads(card.pop('metadata_json'))
        cards.append(card)
    ids=[c['id'] for c in cards]
    edges=[]
    if ids:
        marks=','.join('?' for _ in ids)
        edges=[dict(r) for r in conn.execute(f'SELECT source_id,target_id,kind,rationale FROM edges WHERE source_id IN ({marks}) AND target_id IN ({marks}) LIMIT 20',ids+ids)]
result={'method':'bounded SQL lexical retrieval from the current math-brain population store','database':str(db),'read_only':True,'candidate_cap':7,'seconds':time.monotonic()-start,'cards':cards,'edges_among_returned_cards':edges}
(ROOT/'MATH_BRAIN_RETRIEVAL.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
