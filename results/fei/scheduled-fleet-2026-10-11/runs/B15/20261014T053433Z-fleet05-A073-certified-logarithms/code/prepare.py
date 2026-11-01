from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
source=R.parent/'20261014T023508Z-fleet05-A073-certified-logarithms/code/exact.py'
raw=source.read_bytes();(R/'code/exact.py').write_bytes(raw)
spec={'helper_version':'A073-centered-Jensen/1; own exact helper copied byte-for-byte',
 'helper_sha256':hashlib.sha256(raw).hexdigest(),
 'actual_Boolean_family':'Specified bent core with one-vertex AND2 edit; complete physical laws d=2,4,6 and analytically compressed same family',
 'parameter_domain':{'physical_d':[2,4,6],'compressed_d':[2,4,6,8,32,104,538,1076],
 'negative_control_even_d_range':[2,1080]},'case_count':{'physical':3,'compressed':8,'floating_negative_control':540},
 'pilot_domain':{'physical':[2],'compressed':[2,104],'negative_control':0},
 'symmetry':'No physical symmetry reduction; two amplitude classes compressed by proved bent sign counts',
 'arithmetic':'Integer Walsh/inverse/physical influences; Fraction complete KL; centered x-ln(1+x) series through degree24 with absolute geometric tail, rational ln2 interval at24 terms; floats only reproduce frozen negative control',
 'precision_refinements':0,'memory_estimate_bytes':80000000,'max_runtime_seconds':55,
 'maximum_physical_dimension':8,'stop_rule':'Stop on exact analytic sign or initial fixed24-term rational certificate; never escalate dimensions'}
(R/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
print('Frozen spec saved')
