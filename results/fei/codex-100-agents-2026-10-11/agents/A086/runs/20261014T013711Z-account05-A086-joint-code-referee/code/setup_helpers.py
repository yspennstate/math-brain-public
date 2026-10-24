from pathlib import Path
import hashlib
run=Path(__file__).resolve().parents[1]
old=run.parent/'20261013T220217Z-account05-A086-joint-code-referee/code/check.py'
s=old.read_text(encoding='utf8').split('def activation():')[0]
(run/'code/arithmetic.py').write_text(s,encoding='utf8')
(run/'out/HELPER_PROVENANCE.json').write_text('{"source":"own A086 v3 pre-activation arithmetic utilities","source_sha256":"'+hashlib.sha256(old.read_bytes()).hexdigest()+'"}\n',encoding='utf8')
