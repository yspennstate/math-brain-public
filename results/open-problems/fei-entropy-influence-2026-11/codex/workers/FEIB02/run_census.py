import subprocess,json,time,os
from pathlib import Path
print('inherited_nice',os.getpriority(os.PRIO_PROCESS,0),flush=True)
for n in range(1,25):
    path=Path(f'census_{n:02d}.json')
    if path.exists(): continue
    data=subprocess.check_output(['./census',str(n)],text=True)
    row=json.loads(data)
    path.write_text(data)
    print(n,row['cpu_seconds'],{k:v['value'] for k,v in row['maxima'].items()},flush=True)
    Path('STATUS.md').write_text(f'# FEIB02 status\nExhaustive integer census completed through n={n}.\nNEXT: finish census through n=24; independently verify extrema and derive uniform bounds.\n')
