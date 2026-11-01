import json
from pathlib import Path
import sqlite3
import time

root = Path(__file__).resolve().parent
peer_receipt = json.loads(Path('~/brain_workers/w471/LOCAL_SOURCE_RECEIPT.json').read_text(encoding='utf-8'))
ids = [row['id'] for row in peer_receipt.get('canonical_matches', [])]
store = '~/math-brain-build/local/population/brain.sqlite3'
receipt = {'store':store,'mode':'ro','id_discovery':'w471 source receipt only; records re-read directly', 'target':'C0052'}
start = time.monotonic()
try:
    conn = sqlite3.connect('file:'+store+'?mode=ro',uri=True,timeout=2)
    conn.execute('PRAGMA query_only=ON')
    conn.set_progress_handler(lambda: int(time.monotonic()-start > 5), 1000)
    rows = []
    for identity in ids:
        row = conn.execute('SELECT id,kind,title,body,metadata_json FROM nodes WHERE id=?',(identity,)).fetchone()
        if row:
            rows.append(dict(zip(('id','kind','title','body','metadata_json'),row)))
    conn.close()
    receipt['matches'] = rows
    receipt['status'] = 'read_only_complete' if ids else 'no_exact_ids_in_peer_receipt'
    receipt['current_openness'] = 'UNKNOWN'
except (OSError, sqlite3.Error) as exc:
    receipt['status'] = 'UNAVAILABLE'
    receipt['reason'] = str(exc)
(root/'READ_ONLY_STORE_RECEIPT.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({**receipt,'matches':[{k:v for k,v in row.items() if k!='body'} for row in receipt.get('matches',[])]},ensure_ascii=False)[:2600])
