import json
from pathlib import Path
import sqlite3

base=Path(__file__).resolve().parent
path=Path('~/math-brain-build/local/population/brain.sqlite3')
con=sqlite3.connect('file:'+path.as_posix()+'?mode=ro',uri=True,timeout=5)
con.execute('PRAGMA query_only=ON')
tables=[r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")]
report={'store_path':str(path),'read_only':True,'tables_considered':[], 'matches':[]}
for table in tables:
    if table not in ['cards','entries','nodes','assertions','statements','sources','results']:
        continue
    safe='"'+table.replace('"','""')+'"'
    columns=[r[1] for r in con.execute('PRAGMA table_info('+safe+')')]
    text_cols=[c for c in columns if c in ['title','logical_name','statement','name','content','source_id']]
    if not text_cols:
        continue
    report['tables_considered'].append({'table':table,'columns':columns})
    selected=[c for c in columns if c in ['id','kind','title','logical_name','status','verification','source_id','statement','name']]
    if not selected:
        selected=text_cols[:2]
    escaped=lambda c:'"'+c.replace('"','""')+'"'
    projections=','.join(('substr('+escaped(c)+',1,700)' if c=='statement' else escaped(c))+' AS '+escaped(c) for c in selected)
    where=' OR '.join(escaped(c)+" LIKE '%Anderson%' OR "+escaped(c)+" LIKE '%C0056%'" for c in text_cols)
    for row in con.execute('SELECT '+projections+' FROM '+safe+' WHERE '+where+' LIMIT 15'):
        report['matches'].append({'table':table,**dict(zip(selected,row))})
con.close()
(base/'STORE_C0056_READONLY.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False),flush=True)
