"""Refresh the unchanged resource gate and run bounded exact diagnostics only if allowed."""
from pathlib import Path
import json
import runpy
import time

root = Path(__file__).resolve().parent
state_path = Path(r'~\.claude\compute\compute_state.json')
state = json.loads(state_path.read_text(encoding='utf-8-sig'))
age = time.time()-state_path.stat().st_mtime
stale = 120
with Path(r'~\.claude\dreaming\compute_sense.py').open(encoding='utf-8') as src:
    for k,line in enumerate(src):
        if line.startswith('STALE_SEC'):
            stale = min(stale,int(line.split('=',1)[1].split('#',1)[0].strip()))
            break
        if k >= 30:
            break
allow = state.get('status','unknown') in ('ok','warning') and 0 <= age <= stale
gate = {'worker':'w400','checked_unix':time.time(),'allow':allow,
        'governor_status':state.get('status'),'governor_age_seconds':age,
        'max_governor_age_seconds':stale,'max_vertices':10,'max_paths':1000,
        'max_process_cpu_seconds':2,'max_math_wall_seconds':10,
        'gpu':False,'training':False,'network':False,'store_writes':False,
        'scope':'exact Fraction diagnostics only'}
(root/'COMPUTE_GATE.json').write_text(json.dumps(gate,indent=2)+'\n',encoding='utf-8')
print(json.dumps(gate))
if allow:
    runpy.run_path(str(root/'check_obstructions.py'),run_name='__main__')
else:
    print('GATE_DENIED; no experiment executed')
