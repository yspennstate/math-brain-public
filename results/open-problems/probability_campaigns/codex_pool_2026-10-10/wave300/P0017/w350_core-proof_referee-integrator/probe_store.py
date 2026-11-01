from pathlib import Path
import json
import sqlite3

ROOT=Path(__file__).resolve().parent
p=Path('~/math-brain-build/local/population/brain.sqlite3')
c=sqlite3.connect('file:'+p.as_posix()+'?mode=ro',uri=True)
c.execute('PRAGMA query_only=ON')
tables=c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'fts%' LIMIT 12").fetchall()
result={'path':str(p),'mode':'ro','tables':[r[0] for r in tables]}
for table in ['nodes','claims','sources']:
    if table not in result['tables']: continue
    cols=[r[1] for r in c.execute('PRAGMA table_info("'+table+'")')]
    result[table+'_columns']=cols
    print(table,cols,flush=True)
    if table!='nodes': continue
    textual=[x for x in ['title','logical_id','metadata_json','payload_json','attrs_json','data_json','content'] if x in cols]
    if not textual: continue
    probes=['%P0017%','%posterior%variance%','%gaussian%retention%','%block%symmetr%recovery%']
    found=[]
    for probe in probes:
        conditions=' OR '.join('CAST("'+x+'" AS TEXT) LIKE ?' for x in textual)
        select=[x for x in ['id','node_id','title','logical_id'] if x in cols]
        if not select: select=textual[:1]
        rows=c.execute('SELECT '+','.join('"'+x+'"' for x in select)+' FROM "nodes" WHERE ('+conditions+') LIMIT 15',[probe]*len(textual)).fetchall()
        found.append({'probe':probe,'fields':select,'matches':rows})
    result['distinctive_word_probes']=found
c.close()
(ROOT/'context'/'store_probe.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False),flush=True)
