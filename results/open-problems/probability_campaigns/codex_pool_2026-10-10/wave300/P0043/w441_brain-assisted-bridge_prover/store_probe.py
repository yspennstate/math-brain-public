"""Read schemas or retrieve bounded relevant mathematics; never write to SQLite."""
from pathlib import Path
import json, sqlite3, sys, time

ROOT=Path(__file__).resolve().parent
DB=Path(r'~\math-brain-build\local\population\brain.sqlite3')

def schema():
    con=sqlite3.connect(DB.as_uri()+'?mode=ro',uri=True,timeout=10)
    con.execute('PRAGMA query_only=ON')
    rows=con.execute("SELECT name,sql FROM sqlite_master WHERE type='table' AND name NOT LIKE '%_data' AND name NOT LIKE '%_idx' AND name NOT LIKE '%_docsize' AND name NOT LIKE '%_config' AND name NOT LIKE 'sqlite_%' ORDER BY name").fetchall()
    con.close()
    (ROOT/'STORE_SCHEMA.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(rows,ensure_ascii=False,indent=2)[:16500])

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='retrieve':
        start=time.perf_counter()
        con=sqlite3.connect(DB.as_uri()+'?mode=ro',uri=True,timeout=10)
        con.execute('PRAGMA query_only=ON')
        con.set_progress_handler(lambda: int(time.perf_counter()-start>15),10000)
        rows=con.execute("SELECT n.id,n.kind,n.title,n.body,n.metadata_json,c.payload_json FROM nodes n LEFT JOIN claims c ON c.id=n.id WHERE (lower(n.title) LIKE '%critical%percolation%' OR lower(n.title) LIKE '%percolation%critical%' OR lower(n.title) LIKE '%percolation%exponential%' OR n.title LIKE '%P0043%') AND n.kind='claim' ORDER BY n.title LIMIT 12").fetchall()
        con.close()
        data={'store':str(DB),'mode':'read-only','query_seconds':time.perf_counter()-start,'rows':[dict(zip(('id','kind','title','body','metadata_json','claim_payload'),row)) for row in rows]}
        (ROOT/'BRAIN_THEOREM_RETRIEVAL.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
        print(json.dumps(data,ensure_ascii=False,indent=2)[:24000])
    else:
        schema()
