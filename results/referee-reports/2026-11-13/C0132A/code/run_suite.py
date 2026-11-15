"""Run both open cases sequentially at nice >=10; record time and measured memory."""
import datetime
import json
import os
from pathlib import Path
import resource
import subprocess
import time

root=Path(__file__).resolve().parents[1]
os.chdir(root)
priority=os.getpriority(os.PRIO_PROCESS,0)
if priority<10:
    os.nice(10-priority)
# Some macOS sandboxes expose RLIMIT_AS with unusable limits. The hash table is
# deterministically 128 MiB; record the measured RSS as the independent check.
try:
    soft,hard=resource.getrlimit(resource.RLIMIT_AS)
    limit=3*1024**3 if hard==resource.RLIM_INFINITY else min(hard,3*1024**3)
    resource.setrlimit(resource.RLIMIT_AS,(limit,hard))
except (ValueError,OSError) as error:
    print('RLIMIT_AS unavailable:',error,flush=True)
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
governor=Path('~/.claude/compute/compute_state.json')
records=[]
for d1 in (1,2):
    state=json.loads(governor.read_text())
    if state.get('status')=='distress':
        raise SystemExit('Compute governor reports distress; simulation not started.')
    start=time.monotonic()
    args=['code/simulate',str(d1),'10000000','128','0',f'data/m{d1}1.csv']
    with open(f'data/m{d1}1.stderr','w') as log:
        subprocess.run(args,stderr=log,check=True)
    # macOS reports ru_maxrss in bytes. Each child runs alone.
    usage=resource.getrusage(resource.RUSAGE_CHILDREN)
    records.append(dict(d1=d1,d2=1,steps_per_seed=10000000,seeds=128,
                        seconds=time.monotonic()-start,peak_child_rss_bytes=usage.ru_maxrss,
                        nice=os.getpriority(os.PRIO_PROCESS,0),
                        governor_at_launch=state,command=args))
    Path('data/resources.json').write_text(json.dumps(records,indent=2)+'\n')
    print(d1,records[-1]['seconds'],records[-1]['peak_child_rss_bytes'],flush=True)
Path('data/completed.txt').write_text(datetime.datetime.now().astimezone().isoformat()+'\n')
