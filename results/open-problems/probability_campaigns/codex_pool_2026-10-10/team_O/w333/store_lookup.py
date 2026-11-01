import json, sqlite3
from pathlib import Path

root = Path(__file__).resolve().parent
path = Path('~/math-brain-build/local/population/brain.sqlite3')
conn = sqlite3.connect('file:' + path.as_posix() + '?mode=ro', uri=True)
conn.execute('PRAGMA query_only=ON')
queries = {
    'P0189': ['%Brown%measure%converg%', '%irrational%rotation%'],
    'P0390': ['%Hyperuniformity transition%wake%'],
    'C0100': ['%sandpile%scaling%', '%Pegden%Smart%'],
    'P0031': ['%forward%Brownian%', '%first%passage%Brownian%'],
    'P0242': ['%lumping%', '%stationary%stopping%'],
    'C0011': ['%local%time%level%', '%Ray%Knight%'],
    'C0070': ['%Discrete duality principle%hypercube%'],
    'C0105': ['%Multiscale decomposition%zeta%'],
    'C0153': ['%Local limits%random%cluster%', '%Local Weak Convergence and the Objective Method%'],
    'P0025': ['%synchronous%reflection%', '%reflected%Brownian%'],
}
all_rows = {}
for pid, patterns in queries.items():
    rows = []
    for pattern in patterns:
        hits = conn.execute('SELECT id, kind, title, body, metadata_json FROM nodes WHERE title LIKE ? LIMIT 3', (pattern,)).fetchall()
        for node_id, kind, title, body, metadata in hits:
            if node_id not in {r['id'] for r in rows}:
                rows.append({'id': node_id, 'kind': kind, 'title': title, 'body': body, 'metadata': json.loads(metadata)})
    all_rows[pid] = rows
    print(pid, json.dumps([{'id': r['id'], 'title': r['title'], 'quote': r['body'][:500], 'metadata_keys': list(r['metadata'])} for r in rows], ensure_ascii=False))
(root / 'evidence' / 'store_cards.json').write_text(json.dumps(all_rows, indent=2, ensure_ascii=False), encoding='utf-8')
