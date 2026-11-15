import os, sys, csv, json, time, statistics, resource
from pathlib import Path
from perimeter import run_path
assert os.getpriority(os.PRIO_PROCESS,0)>=10, 'Requires nice >=10'
# macOS sandbox rejects setting RLIMIT_AS; bounded arrays enforce the budget.
try:
    soft, hard=resource.getrlimit(resource.RLIMIT_AS)
    cap=min(3*1024**3,hard) if hard>=0 else 3*1024**3
    resource.setrlimit(resource.RLIMIT_AS,(cap,hard))
except (ValueError,OSError):
    pass
models=['quadrangulation','octangulation','dyadic_beta_080','dyadic_beta_035']
reps=int(sys.argv[1]) if len(sys.argv)>1 else 80
start=time.monotonic(); rows=[]
for j,model in enumerate(models):
    for i in range(reps): rows.append(run_path(570000+j*10000+i,model))
    print(model,'finished',reps,'paths',flush=True)
with Path('data/paths.csv').open('w') as f:
    cw=csv.DictWriter(f,fieldnames=list(rows[0])); cw.writeheader(); cw.writerows(rows)
summaries=[]
for model in models:
    a=[r for r in rows if r['model']==model]
    completed=[r['neighbourhood_time'] for r in a if r['neighbourhood_time'] is not None]
    summaries.append(dict(model=model,paths=len(a),root_swallowed=sum(r['root_corner_time'] is not None for r in a),
       neighbourhood_swallowed=len(completed),edge_censored=sum(r['censor']=='edge_cap' for r in a),
       time_censored=sum(r['censor']=='time_cap' for r in a),
       median_completed_only=statistics.median(completed) if completed else None,
       max_completed_time=max(completed) if completed else None))
out=dict(summary=summaries,seconds=time.monotonic()-start,nice=os.getpriority(os.PRIO_PROCESS,0),
    max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,max_steps=2000,max_edges=20000,
    p0=8,seed_scheme='570000 + model_index*10000 + replicate',native_threads=1)
Path('data/simulation_summary.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
