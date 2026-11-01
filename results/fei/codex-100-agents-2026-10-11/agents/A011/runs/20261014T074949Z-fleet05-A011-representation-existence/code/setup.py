from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
source=(R/'code/check.py').read_text(encoding='utf-8')
helper=source.split('cases=[];tensor_checks=0')[0]
(R/'code/shared.py').write_text(helper,encoding='utf-8')
(R/'out/HELPER_PROVENANCE.json').write_text(json.dumps({'source':'own code/check.py v1.1','source_sha256':hashlib.sha256(source.encode()).hexdigest(),'helper_sha256':hashlib.sha256(helper.encode()).hexdigest(),'search_executed_by_setup':False},indent=2),encoding='utf-8')
print('own arithmetic helper saved; no search')
