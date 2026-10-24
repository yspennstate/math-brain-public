"""Read-only, exact logical-id probe of one math-brain population snapshot."""
import json
import sqlite3

path = '~/math-brain-build/local/population/brain.sqlite3'
con = sqlite3.connect('file:' + path + '?mode=ro', uri=True)
names = [
    'finite-gaussian-optimized-exponential-path-response',
    'two-edge-gaussian-path-switching-survives-zero-temperature',
    'p0297-correct-lqg-dimension-parameter-identity',
    'gaussian-optimized-length-response-with-switching',
    'competing-route-correction-to-gaussian-switching-draft',
]
for name in names:
    rows = con.execute('SELECT title,metadata_json FROM nodes WHERE metadata_json LIKE ? LIMIT 5', ('%"logical_id":"math:probability.core:' + name + '"%',)).fetchall()
    print(name, 'found', len(rows))
    for title, raw in rows:
        obj = json.loads(raw)
        print(' ', title, obj.get('logical_id'), obj.get('draft'))
