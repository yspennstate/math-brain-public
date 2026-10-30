from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
source=root.parents[1]/'runs/20261013T222630Z-fleet05-A003-minimal-target-formulation/code/check.py'
text=source.read_text(encoding='utf-8').split('endpoint=[]')[0]
(root/'code/lib.py').write_text(text,encoding='utf-8')
(root/'out/HELPER_SOURCE.json').write_text(json.dumps({'source':str(source),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'reuse':'Only exact arithmetic definitions before prior endpoint driver; no previous computation executes.'},indent=2)+'\n',encoding='utf-8')
print('Exact own arithmetic helper saved; no search executed.')
