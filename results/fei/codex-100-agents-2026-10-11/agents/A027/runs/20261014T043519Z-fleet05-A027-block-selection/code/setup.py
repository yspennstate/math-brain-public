from pathlib import Path
import json,hashlib
run=Path(__file__).resolve().parents[1]
source=run.parents[1]/'runs'/'20261014T015108Z-fleet05-A027-block-selection'/'code'/'exact.py'
data=source.read_bytes(); (run/'code'/'exact.py').write_bytes(data)
(run/'out'/'HELPER_PIN.json').write_text(json.dumps({'source':str(source),'sha256':hashlib.sha256(data).hexdigest(),'scope':'exact helpers only; no enumeration executes'},indent=2)+'\n',encoding='utf-8')
print('Copied pinned exact helpers locally.')
