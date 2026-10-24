import json,sys,runpy,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[1]
pilot='--pilot' in sys.argv
spec=json.loads((root/'out'/'FROZEN_SPEC_V2.json').read_text())
spec.update(helper_version='A079-quadratic-collision-v3-cached',helper_sha256=hashlib.sha256((root/'code'/'check_collision.py').read_bytes()).hexdigest(),maximum_runtime_seconds=60 if pilot else 600)
if pilot:
    spec.update(parameter_domain='All quadratic pairs on n=0,1,2 modulo simultaneous sign; four n=4 rank endpoints.',case_count=142)
(root/'out'/('FROZEN_PILOT_V3.json' if pilot else 'FROZEN_FULL_V3.json')).write_text(json.dumps(spec,indent=2)+'\n')
runpy.run_path(str(root/'code'/'check_collision.py'),run_name='__main__')
