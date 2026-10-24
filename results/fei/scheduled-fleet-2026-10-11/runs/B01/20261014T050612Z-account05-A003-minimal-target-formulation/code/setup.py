from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
source=root.parents[1]/'runs/20261014T021415Z-account05-A003-minimal-target-formulation/code/lib.py'
(root/'code/lib.py').write_bytes(source.read_bytes())
(root/'out/HELPER_SOURCE.json').write_text(json.dumps({'source':str(source),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'scope':'Own pure exact arithmetic definitions only; no previous search executes.'},indent=2)+'\n',encoding='utf-8')
print('Own exact arithmetic helper saved.')
