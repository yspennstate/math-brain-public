"""Bounded C0029 retrieval; the live SQLite store is always opened read-only."""
import dataclasses
import json
import sqlite3
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, '~/math-brain-build/src')
from math_brain.retrieval import retrieve
from math_brain.store import ResearchStore

store_path = Path('~/math-brain-build/local/population/brain.sqlite3')
started = time.monotonic()
with sqlite3.connect(store_path.as_uri() + '?mode=ro', uri=True) as con:
    con.execute('PRAGMA query_only=ON')
    candidates = con.execute(
        "SELECT id,title,length(body) FROM nodes WHERE lower(title) LIKE ? "
        "OR lower(title) LIKE ? OR lower(title) LIKE ? OR lower(title) LIKE ? "
        "ORDER BY id LIMIT 60",
        ('%spielman%', '%singular value%', '%gaussian%small%', '%small%ball%')
    ).fetchall()
    print(json.dumps({'candidate_count': len(candidates), 'candidates': candidates}, ensure_ascii=False))
    ids = [row[0] for row in candidates]
    # No full-store node or edge iteration, no background recall or signal-cache writes.
with ResearchStore.open_read_only(store_path) as store:
    nodes = tuple(store.get_nodes(ids).values())
queries = [
    'C0029 Spielman Teng exact constant one least singular value Bernoulli Gaussian rescaling',
    'Gaussian independent random radius small ball probability rescaling third moment spectral cutoff',
]
records = []
for query in queries:
    t = time.monotonic()
    result = retrieve(query, nodes=nodes, edges=(), limit=5, graph_depth=0)
    records.append({'query': query, 'elapsed_seconds': time.monotonic()-t,
                    'decision': dataclasses.asdict(result)})
payload = {'read_only': True, 'scope': 'At most 60 title-matching C0029-related nodes; no global-recall estimate',
           'store': str(store_path), 'candidates': candidates,
           'elapsed_seconds': time.monotonic()-started, 'results': records}
Path('math_recall.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2, default=str), encoding='utf-8')
for row in records:
    decision = row['decision']
    print(json.dumps({'query': row['query'], 'elapsed_seconds': row['elapsed_seconds'],
                      'abstained': decision.get('abstained'),
                      'hits': decision.get('hits')}, ensure_ascii=False, default=str)[:15000])
