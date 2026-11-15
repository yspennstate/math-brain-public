#!/usr/bin/env python3
"""Serial matching simulations. Flush every sample; deterministic per-sample seeds."""
import os,sys,time,csv,json,resource,datetime
from pathlib import Path
from matching import solve,SCALE,np
# This is also a hard guard against inadvertently scaling up the complete graph.
PLAN=[(32,500),(64,500),(128,400),(256,400),(512,320),(1024,240),(2048,200)]
DIMENSIONS=[2,3,4]
MASTER=3100132026
fields=['d','n','sample','seed','length','integer_cost','scale','certificate','seconds','max_rss_bytes','nice','point_sha256']
import hashlib
raw=Path('data/samples.csv')
seen=set()
if raw.exists():
 with raw.open() as f:
  for r in csv.DictReader(f):seen.add((int(r['d']),int(r['n']),int(r['sample'])))
meta={'master_seed':MASTER,'plan':PLAN,'dimensions':DIMENSIONS,'scale':SCALE,'solver':'Blossom V 2.05, complete graph, 64-bit integral costs, exact complementary slackness checker','thread_limits':{k:os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']},'nice':os.getpriority(os.PRIO_PROCESS,0),'started':datetime.datetime.now().astimezone().isoformat(),'platform':sys.platform,'python':sys.version,'numpy':np.__version__,'quantization_cost_error_bound':'n/(2*scale), plus distance-evaluation rounding; these are not symbolic exact square roots'}
Path('data/run_metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
with raw.open('a',buffering=1) as f:
 writer=csv.DictWriter(f,fieldnames=fields)
 if not seen:writer.writeheader()
 for n,reps in PLAN:
  for d in DIMENSIONS:
   t=time.monotonic()
   for sample in range(reps):
    if (d,n,sample) in seen:continue
    # Current compute state is read, never modified. No work beyond this directory.
    if sample%20==0:
     governor=Path.home()/'.claude/compute/compute_state.json'
     if governor.exists():
      st=json.loads(governor.read_text())
      if st.get('status')=='distress':
       print('Paused for compute distress; resume this script after state clears.',flush=True)
       raise SystemExit(75)
    seed=int(np.random.SeedSequence([MASTER,d,n,sample]).generate_state(1,dtype=np.uint64)[0])
    x=np.random.default_rng(seed).random((n,d))
    t0=time.monotonic();length,q,partners=solve(x);seconds=time.monotonic()-t0
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform!='darwin':rss*=1024
    if rss>=3_500_000_000:raise MemoryError('3.5 GB guard')
    writer.writerow({'d':d,'n':n,'sample':sample,'seed':seed,'length':repr(length),'integer_cost':q,'scale':SCALE,'certificate':0,'seconds':seconds,'max_rss_bytes':rss,'nice':os.getpriority(os.PRIO_PROCESS,0),'point_sha256':hashlib.sha256(x.tobytes()).hexdigest()})
    if sample==0:
     np.savez_compressed(f'data/example_d{d}_n{n}.npz',points=x,partners=partners)
   print(json.dumps({'d':d,'n':n,'samples':reps,'wall_seconds':time.monotonic()-t,'max_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
print('COMPLETED',flush=True)
