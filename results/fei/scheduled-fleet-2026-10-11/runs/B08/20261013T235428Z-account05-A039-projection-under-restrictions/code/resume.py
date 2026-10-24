from pathlib import Path
import json,hashlib
run=Path(__file__).resolve().parents[1]
old=run.parent/'20261012T040116Z-account05-A039-projection-under-restrictions'
receipts=[]
for name in ['TREE_TARGET.md','code/optimal_tree.py','out/OPTIMUM_K2.json','out/OPTIMALITY_CERTIFICATE_K2.json']:
    src=old/name; dst=run/name; dst.parent.mkdir(parents=True,exist_ok=True)
    data=src.read_bytes(); dst.write_bytes(data)
    receipts.append({'source':str(src),'destination':str(dst),'sha256':hashlib.sha256(data).hexdigest(),'use':'resumed proof/code or adopted completed pilot; no prior-run mutation'})
(run/'out/RESUME_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
print(json.dumps({'status':'RESUMED','prior_partial_stage_preserved':True,'copies':len(receipts)}))
