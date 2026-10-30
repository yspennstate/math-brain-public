from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
ar=R.parents[2]/'A029'
files=sorted((ar/'runs').glob('20261023*/*A028*'))
out=[]
for p in files:
    if p.is_file() and p.suffix.lower() in ('.md','.json'):
        s=p.read_text(encoding='utf-8-sig')
        if 'v8' in s or 'version8' in s or 'version 8' in s:
            out.append(dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),text=s))
(R/'out/new_review_receipts.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
for x in out: print(x['path']+'\n'+x['text'][:2200])
if not out: print('No explicitly named v8 A028 review found; do not infer independent acceptance from a board receipt.')
