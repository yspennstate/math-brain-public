from pathlib import Path
import hashlib,json
run=Path(__file__).resolve().parents[1]
source=run.parents[1]/'runs'/'20261013T221314Z-account05-A027-block-selection'/'code'/'check.py'
raw=source.read_text(encoding='utf-8'); helper=raw.split('\ncontrollers=')[0]
(run/'code'/'exact.py').write_text(helper+'\n',encoding='utf-8')
(run/'out'/'HELPER_PIN.json').write_text(json.dumps({'source':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'copied_prefix_sha256':hashlib.sha256((helper+'\n').encode()).hexdigest(),'scope':'exact rational prime-log/Walsh helpers only; source enumeration not copied or executed'},indent=2)+'\n',encoding='utf-8')
print('Own prior exact helpers copied locally; no search executed.')
