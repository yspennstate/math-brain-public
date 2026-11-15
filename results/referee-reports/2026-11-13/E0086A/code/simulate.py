"""Serial, reproducible SRW evidence; no trajectory or PDF images are retained."""
import os
for name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[name] = '1'
import csv
import json
import math
import pathlib
import resource
import subprocess
import time
import numpy as np
from scipy.ndimage import distance_transform_edt

ROOT = pathlib.Path(__file__).resolve().parents[1]
ALPHAS = (.25, .4, .5, .65, .8)

def measure(local, n, alpha):
    a = n**alpha
    h = min(n, math.ceil(2*a)+2)
    counts = local[n-h:n+h+1, n-h:n+h+1]
    coord = np.arange(-h,h+1,dtype=np.int64)
    r2 = coord[:,None]**2+coord[None,:]**2
    ann = (r2>a*a)&(r2<=4*a*a)
    maximum = int(counts[ann].max(initial=0))
    good = (counts>0)&ann
    # False padding ensures distance to the complement is defined on every side.
    distances = distance_transform_edt(np.pad(good,1))[1:-1,1:-1]
    i = np.unravel_index(np.argmax(distances),distances.shape)
    supremum = float(distances[i])
    radius = max(0, math.ceil(supremum)-1)
    return dict(alpha=alpha,a=a,max_local=maximum,
                local_over_log2=maximum/math.log(n)**2,
                local_prediction=4*alpha**2/math.pi,
                radius_integer=radius,radius_supremum=supremum,
                center_x=int(i[1]-h),center_y=int(i[0]-h),
                radius_log_exponent=math.log(max(radius,1))/math.log(n),
                radius_exponent_prediction=alpha/2,
                radius_over_sqrt_a=radius/math.sqrt(a))

def main():
    assert os.getpriority(os.PRIO_PROCESS,0)>=10, 'Must inherit nice >=10'
    # RSS is additionally checked after each run; largest allocations are <1 GiB.
    resource.setrlimit(resource.RLIMIT_CPU,(600,600))
    binary=ROOT/'code'/'srw'
    subprocess.run(['cc','-O3','-std=c11',str(ROOT/'code'/'srw.c'),'-o',str(binary)],check=True)
    plans=[(128,24),(256,24),(512,24),(1024,20),(2048,16),(4096,12)]
    target=ROOT/'data'/'simulation.csv'
    scratch=ROOT/'data'/'counts_work.bin'
    start=time.monotonic()
    with target.open('w',newline='') as f:
        writer=None
        for n,reps in plans:
            for rep in range(reps):
                seed=86000000+n*1000+rep
                meta=json.loads(subprocess.check_output([str(binary),str(n),str(seed),str(scratch)]))
                assert meta['seed']==seed
                local=np.fromfile(scratch,dtype=np.uint32).reshape(2*n+1,2*n+1)
                assert int(local.sum(dtype=np.uint64))==meta['exit_time']
                assert meta['exit_x']**2+meta['exit_y']**2>n*n
                global_max=int(local.max())
                for alpha in ALPHAS:
                    row=dict(n=n,rep=rep,seed=seed,exit_time=meta['exit_time'],global_max=global_max,
                             global_over_log2=global_max/math.log(n)**2,**measure(local,n,alpha))
                    if writer is None:
                        writer=csv.DictWriter(f,fieldnames=list(row));writer.writeheader()
                    writer.writerow(row)
                f.flush()
                del local
                scratch.unlink()
            print(f'n={n}: {reps} replicates finished, elapsed={time.monotonic()-start:.1f}s',flush=True)
    usage=resource.getrusage(resource.RUSAGE_SELF)
    children=resource.getrusage(resource.RUSAGE_CHILDREN)
    (ROOT/'data'/'resources.json').write_text(json.dumps(dict(
        nice=os.getpriority(os.PRIO_PROCESS,0),threads=1,elapsed_seconds=time.monotonic()-start,
        parent_peak_rss_bytes=usage.ru_maxrss,child_peak_rss_bytes=children.ru_maxrss,
        rss_units='bytes on macOS; parent and child run serially except parent holds its baseline',
        stopping_rule='first step outside closed Euclidean disc; exit site excluded',
        rng='SplitMix64; top two bits choose +/- x, +/- y',plans=plans),indent=2)+'\n')

if __name__=='__main__':main()
