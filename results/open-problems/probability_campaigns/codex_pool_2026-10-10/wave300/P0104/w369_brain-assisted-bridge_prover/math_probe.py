"""Read only named FPP nodes; no corpus export, store mutation, or model load."""
import json
import sqlite3
import time
from pathlib import Path

root=Path(__file__).resolve().parent
database=Path('~/math-brain-build/local/population/brain.sqlite3')
started=time.monotonic()
with sqlite3.connect(f'file:{database.as_posix()}?mode=ro',uri=True,timeout=8) as connection:
    connection.execute('PRAGMA query_only=ON')
    connection.execute('PRAGMA busy_timeout=8000')
    rows=connection.execute('''SELECT id,title,body,metadata_json FROM nodes
      WHERE (lower(title) LIKE '%passage%' OR lower(title) LIKE '%fpp%')
      AND (lower(title) LIKE '%concentrat%' OR lower(title) LIKE '%fluctuation%')
      ORDER BY CASE WHEN lower(title) LIKE '%subdiffusive%' THEN 0
                    WHEN lower(body) LIKE '%standard deviation%' THEN 1 ELSE 2 END,
               title LIMIT 8''').fetchall()
payload={'database':str(database),'mode':'read-only; query_only=ON',
         'query':'FPP passage-time concentration; full hypotheses and scale',
         'seconds':time.monotonic()-started,
         'nodes':[{'id':i,'title':t,'statement':b,'metadata':json.loads(m)} for i,t,b,m in rows]}
(root/'math_retrieval.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False),encoding='utf-8')
for node in payload['nodes']:
    print(json.dumps({'id':node['id'],'title':node['title'],'statement':node['statement'],
                      'logical_id':node['metadata'].get('logical_id'),
                      'source_id':node['metadata'].get('source_id')},ensure_ascii=False))
print('SECONDS',payload['seconds'])
