from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]
old=(R/'out/PILOT.json').read_bytes();(R/'out/PILOT_ORIGINAL.json').write_bytes(old)
spec=json.loads((R/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
spec.update(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),helper_version='A099-v8.1 '+hashlib.sha256((R/'code/check.py').read_bytes()).hexdigest())
spec['parameter_domain']=spec['parameter_domain'].replace('uniform residual nonempty mass','residual mass on the true conditional nonempty spectrum')
spec['amendment']='After initial pilot (6879 checks), before ANY primary evaluation: replace only residual Q profile by true conditional nonempty law to force positive first resets; n, case count, policies, caps unchanged. Original pilot retained separately. Revised pilot required.'
(R/'out/FROZEN_SPEC_V2.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
print('AMENDED_BEFORE_PRIMARY')
