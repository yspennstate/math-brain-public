import json
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parent
db = sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro', uri=True)
tables = list(db.execute("select name,sql from sqlite_master where type='table' and name not like '%fts%'"))
if __import__('sys').argv[-1] == '--schema':
    for name, sql in tables:
        print(name, sql)
else:
    terms = ['P0289','C0035','P0001','P0133','C0002','C0059','C0083','C0128','P0015','P0044']
    records = []
    for term in terms:
        rows = list(db.execute("select id,kind,title,body,metadata_json from nodes where lower(json_extract(metadata_json, '$.logical_id')) like ? or lower(json_extract(metadata_json, '$.logical_id')) like ? limit 4", ('%:open-problem-'+term.lower()+'-%', '%:attempt-'+term.lower()+'-%')))
        for node_id, kind, title, body, metadata in rows:
            record = {'query': term, 'id': node_id, 'kind': kind, 'title': title, 'body': body, 'metadata': json.loads(metadata)}
            records.append(record)
            print(json.dumps({'problem_id':term,'logical_id':record['metadata'].get('logical_id'),'title':title,'body':body}, ensure_ascii=False))
    (ROOT/'store_cards.json').write_text(json.dumps(records, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
