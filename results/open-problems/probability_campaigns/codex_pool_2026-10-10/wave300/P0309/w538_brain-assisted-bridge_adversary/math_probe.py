import json,pathlib,sqlite3,time
w=pathlib.Path('~/brain_workers/w538')
p=pathlib.Path('~/math-brain-build/local/population/brain.sqlite3')
c=sqlite3.connect(p.as_uri()+'?mode=ro',uri=True,timeout=5)
c.execute('PRAGMA query_only=ON')
c.set_progress_handler(lambda: 1 if time.monotonic()-started>20 else 0, 20000)
started=time.monotonic()
queries={'target':"lower(title) LIKE '%crystall%riesz%' OR lower(body) LIKE '%p0309%'",'variance':"lower(title) LIKE '%brascamp%'",'gas':"lower(title) LIKE '%riesz%gas%'",'gaussian':"lower(title) LIKE '%gaussian%free%field%'"}
result={}
for name,where in queries.items():
 rows=c.execute('SELECT id,kind,title,body,metadata_json FROM nodes WHERE '+where+' LIMIT 5').fetchall()
 result[name]=[{'id':r[0],'kind':r[1],'title':r[2],'body':r[3],'metadata':json.loads(r[4])} for r in rows]
c.close()
result['seconds']=time.monotonic()-started
(w/'math_brain_probe.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False)[:28000])
