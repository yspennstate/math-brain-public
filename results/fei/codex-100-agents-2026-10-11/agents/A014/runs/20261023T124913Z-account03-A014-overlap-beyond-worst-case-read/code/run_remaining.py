from pathlib import Path
import subprocess,sys,json,time,hashlib,os
R=Path(__file__).resolve().parents[1]
assert (R/'out/independent.json').exists(),'Finish independent job before this sequential runner'
old=(R/'code/check_v1.py').read_text(encoding='utf-8');new=(R/'code/check.py').read_text(encoding='utf-8')
frozen=json.loads((R/'FROZEN_REPAIR.json').read_text(encoding='utf-8'))
assert 'def binary_bounds' not in old and 'def binary_bounds' in new
assert hashlib.sha256((R/'code/check_v1.py').read_bytes()).hexdigest()==frozen['prior_sha256']
for source,target in [('checkpoint.json','timeout_checkpoint.json'),('pilot.json','pilot_v1.json')]:
    if not (R/'out'/target).exists():(R/'out'/target).write_bytes((R/'out'/source).read_bytes())
rows=[]
for script,args,label in [('check.py',['--pilot'],'pilot_v2'),('check.py',[],'full_v2'),('history.py',[],'history'),('scalar.py',[],'scalar')]:
    start=time.monotonic();command=[sys.executable,'-X','utf8',str(R/'code'/script)]+args
    flags=(subprocess.CREATE_NO_WINDOW|subprocess.BELOW_NORMAL_PRIORITY_CLASS) if os.name=='nt' else 0
    with (R/f'out/{label}.log').open('w',encoding='utf-8',newline='\n') as out:
        result=subprocess.run(command,stdout=out,stderr=subprocess.STDOUT,creationflags=flags,timeout=300)
    rows.append({'script':script,'args':args,'returncode':result.returncode,'elapsed_seconds':time.monotonic()-start})
    (R/'out/RUNNER.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(rows[-1]),flush=True)
    if result.returncode:raise RuntimeError('Validation failed: '+label+'; inspect its saved log')
