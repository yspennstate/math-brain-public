from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
previous=R.parent/'20261026T211700Z-account04-A019-orthogonality-extensions'
paths=list(dict.fromkeys(x['path'] for x in json.loads((previous/'out/SOURCE_RECEIPTS.json').read_text(encoding='utf-8'))))
paths += [str(previous/'REPORT.md'),str(previous/'CLAIMS.json'),'agents/A018/runs/20261027T101247Z-account04-A018-shared-data-collision-law/REPORT.md','agents/A016/runs/20261027T031122Z-account04-A016-addressing-benchmark/REPORT.md']
rows=[]
for name in paths:
    p=Path(name);raw=p.read_bytes()
    try:txt=raw.decode('utf-8-sig');enc='utf-8-sig'
    except UnicodeDecodeError:txt=raw.decode('cp1252');enc='cp1252'
    rows.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'encoding':enc})
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(rows,indent=2),encoding='utf-8',newline='\n')
print(json.dumps({'sources_read':len(rows),'bytes':sum(x['bytes'] for x in rows),'status':'PASS'}))
