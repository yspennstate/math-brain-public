from pathlib import Path
import shutil,json,hashlib
R=Path(__file__).resolve().parents[1];old=R.parent/'20261023T063447Z-fleet03-A028-stopping-tree-payment'
for src,dst in [('check.py','prior8.py'),('base.py','base.py'),('exact_helper.py','exact_helper.py'),('independent_base.py','independent_base.py')]:shutil.copyfile(old/'code'/src,R/'code'/dst)
paths=list((R.parents[3]/'agents/A029/runs').glob('*/REVIEW_A028.md'))
pins=[]
for p in sorted(paths)[-2:]:
    text=p.read_text(encoding='utf-8');pins.append(dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
    print(str(p)+'\n'+text[:450])
(R/'out/review_source_pins.json').write_text(json.dumps(pins,indent=2)+'\n',encoding='utf-8',newline='')
print('v8 helpers copied and pinned')
