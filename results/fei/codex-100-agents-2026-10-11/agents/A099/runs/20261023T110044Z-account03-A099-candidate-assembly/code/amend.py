from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]
(R/'out/PILOT_V1.json').write_bytes((R/'out/PILOT.json').read_bytes())
s=json.loads((R/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
s.update(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),helper_version='A099-v9.1 '+hashlib.sha256((R/'code/check.py').read_bytes()).hexdigest(),main_max_seconds=600)
s['case_count']='pilot128 grid transactions plus2 explicit controls=130; primary3072 grid plus2 controls=3074;81 controller faces each'
s['amendment']='Before ANY primary evaluation: measured pilot10.368s motivates explicit primary cap600s (<30min), replacing180s. Add A003 exact coarse-vector and refund assertions; family, dimensions, references and policies unchanged. Preserve v1 pilot; rerun revised pilot before main. Counts explicitly include two previously listed witness/boundary fixtures.'
(R/'out/FROZEN_SPEC_V2.json').write_text(json.dumps(s,indent=2)+'\n',encoding='utf-8')
print('V2_FROZEN_BEFORE_PRIMARY')
