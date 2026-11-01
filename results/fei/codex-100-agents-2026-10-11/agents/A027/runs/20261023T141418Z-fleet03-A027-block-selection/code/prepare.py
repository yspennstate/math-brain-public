from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1];P=R.parent/'20261023T120132Z-fleet03-A027-block-selection'
(R/'code/exact.py').write_bytes((P/'code/exact.py').read_bytes())
src=(P/'code/check.py').read_text(encoding='utf-8').split('\ndef P(f):')[0]
with (R/'code/base.py').open('w',encoding='utf-8',newline='') as f:f.write(src+'\n')
(R/'out/PREPARE.json').write_text(json.dumps({'helper_sha256':hashlib.sha256((R/'code/exact.py').read_bytes()).hexdigest(),'base_source':str(P/'code/check.py'),'base_source_sha256':hashlib.sha256((P/'code/check.py').read_bytes()).hexdigest(),'prefix_boundary':'before def P(f)','no_search':True},indent=2)+'\n',encoding='utf-8')
print('Helper and original-account prefix pinned; no search executed')
