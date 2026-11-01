from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
(R/'out').mkdir(exist_ok=True)
old=R.parents[0]/'20261012T011208Z-fleet05-A028-stopping-tree-payment'/'code'/'check.py'
text=old.read_text(encoding='utf-8').split('count=0\nslack_min=None')[0]
(R/'code'/'exact.py').write_text(text,encoding='utf-8')
spec={'helper':'A028-point-selector-v1','family':'Point-selector disjoint Boolean branches; shared-bit same-orientation priority pair',
'domain':{'pilot':'all branches dimensions 0..1, selector r=1..2; priority r=s=1',
'full':'all branches dimensions 0..2, selector r=1..3; priority branches 0..1, r,s=1..2'},
'case_count':{'pilot':108,'full':1596},'symmetry':'none; labeled truth tables include constants, signs and all biases',
'arithmetic':'integer Walsh, Fraction, canonical prime-log equality; outward rational atanh24 intervals',
'memory_estimate_MB':128,'maximum_runtime_seconds':{'pilot':60,'full':600},'max_dimension':7,
'heavy_job':False,'automatic_dimension_escalation':False}
(R/'out'/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
print('Exact helper and frozen specification saved.')
