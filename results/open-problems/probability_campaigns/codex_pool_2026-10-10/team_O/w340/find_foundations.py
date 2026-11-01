"""Read a few directly used theorem cards, never an export or a test bank."""
import json
import sqlite3
from pathlib import Path
ROOT=Path(__file__).resolve().parent
terms={'holder':['%Hölder%inequality%','%Holder%inequality%'],'markov':['%Markov%inequality%'],'hoeffding':['%Hoeffding%inequality%'],'little':['%Little%law%'],'renewal':['%renewal%reward%'],'flow':['%finite%energy%flow%','%Thomson%principle%'],'gaussian':['%Gaussian%maximum%'],'slutsky':['%Slutsky%']}
results={}
with sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True,timeout=5) as c:
    for topic,patterns in terms.items():
        values=[]
        seen=set()
        for pattern in patterns:
            for row in c.execute('SELECT id,title,body,metadata_json FROM nodes WHERE kind=? AND title LIKE ? LIMIT 3',('claim',pattern)):
                if row[0] in seen: continue
                seen.add(row[0])
                values.append(dict(zip(['id','title','body','metadata_json'],row)))
        results[topic]=values[:3]
(ROOT/'FOUNDATION_REPORT.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
for topic,values in results.items():
    for value in values:
        metadata=json.loads(value['metadata_json'])
        print(json.dumps({'topic':topic,'title':value['title'],'body':value['body'],'logical_id':metadata.get('logical_id'),'truth_status':metadata.get('truth_status')},ensure_ascii=False))
