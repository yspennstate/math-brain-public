from pathlib import Path
import hashlib,json
run=Path(__file__).resolve().parents[1]
old=run.parent/'20261014T013711Z-fleet05-A086-joint-code-referee/code/arithmetic.py'
(run/'code/arithmetic.py').write_bytes(old.read_bytes())
(run/'out/HELPER_PROVENANCE.json').write_text(json.dumps({'source':str(old),'sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'external_author_code_imported':False})+'\n',encoding='utf8')
