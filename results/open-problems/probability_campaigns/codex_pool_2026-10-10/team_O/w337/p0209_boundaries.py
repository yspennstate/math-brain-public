from pathlib import Path
import json
from p0209_check import case

ROOT=Path(__file__).resolve().parent
rows=[case(s) for s in (2,3)]
for row in rows:
    assert row['scaled_max_total_jump_rate']<=1
result={'command':'python -X utf8 p0209_boundaries.py','exact_boundary_cases':2,
        'cases':rows,'scope':'Small-parameter standardization and rate checks. A nonpositive raw distance bound is not promoted to a positive estimate.'}
(ROOT/'measurements'/'p0209_boundaries.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'exact_boundary_cases':2,'parameters':[2,3],'algebra_and_rate_checks':'PASS'}))
