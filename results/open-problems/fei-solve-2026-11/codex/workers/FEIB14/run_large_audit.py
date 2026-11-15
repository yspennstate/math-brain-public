import os,subprocess,json,time
from pathlib import Path
from experiments import KEYS
if os.getpriority(os.PRIO_PROCESS,0)<10:os.nice(10-os.getpriority(os.PRIO_PROCESS,0))
subprocess.run(['cc','-O3','audit_large.c','-o','audit_large'],check=True)
z=json.loads(Path('samples.json').read_text());f=json.loads(Path('families.json').read_text());chosen={z['maxima'][k]['tt'] for k in ['both','countN','union','size']};chosen.update(f['maxima'][k]['tt'] for k in ['both','countN','union','size']);rows=[];start=time.time()
for tt in sorted(chosen):
    r=next(r for r in z['rows']+f['rows'] if r['tt']==tt);p=subprocess.run(['./audit_large',str(r['n']),tt],capture_output=True,text=True,check=True);a=json.loads(p.stdout);err=max(abs(a['ratios'][j]-r[k]/r['I']) for j,k in enumerate(KEYS[1:]));assert err<1e-10
    a.update(tt=tt,tag=r['tag'],maximum_ratio_residual=err);rows.append(a);Path('large_audit.json').write_text(json.dumps(dict(rows=rows,elapsed_seconds=time.time()-start),indent=2)+'\n');print('PASS',r['tag'],err,flush=True)
