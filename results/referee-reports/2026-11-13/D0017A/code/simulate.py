#!/usr/bin/env python3
"""Discretized sheet experiments. Approximate collisions are evidence only.

The sheet is simulated exactly at grid vertices by streaming independent
rectangular white-noise increments. No interpolation is treated as an exact hit.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
if os.getpriority(os.PRIO_PROCESS,0)<10: os.setpriority(os.PRIO_PROCESS,0,10)
import argparse, csv, json, pathlib, resource, time
import numpy as np
from scipy.spatial import cKDTree
p=argparse.ArgumentParser();p.add_argument('--n',type=int,default=2048);p.add_argument('--replicates',type=int,default=4);a=p.parse_args()
assert a.n>=256 and a.n & (a.n-1)==0
root=pathlib.Path(__file__).resolve().parents[1];data=root/'data';data.mkdir(exist_ok=True)
start=time.monotonic();all_curves=[];summaries=[]
# h>=8/n is used in regressions, to avoid the very last unresolved grid scales.
levels=np.arange(3,int(np.log2(a.n))+1)
scales=2.**(-levels)
coeffs=(.5,1.,2.)
for rep in range(a.replicates):
    seed=170170+rep;rng=np.random.default_rng(seed)
    row=np.zeros((3*a.n+1,5),dtype=np.float64)
    uidx=np.arange(a.n//4,5*a.n//4+1)
    vidx=np.arange(3*a.n//2,5*a.n//2+1)
    slices=[];mins={4:[],5:[]};best={4:None,5:None}
    # Columns are t; each new s-row adds a Brownian motion of covariance ds*min(t,t').
    for si in range(1,2*a.n+1):
        increments=rng.standard_normal((3*a.n,5))/a.n
        row[1:]+=np.cumsum(increments,axis=0)
        if si<a.n: continue
        s=si/a.n;slices.append(s)
        norm=np.sqrt(s)
        for d in (4,5):
            u=row[uidx,:d]/norm;v=row[vidx,:d]/norm
            distances=cKDTree(v).query(u,k=1,workers=1)[0]
            minimum=float(np.min(distances));mins[d].append(minimum)
            if best[d] is None or minimum<best[d]['min_distance']:
                best[d]={'min_distance':minimum,'s':s,'u':u.copy(),'v':v.copy()}
    ss=np.array(slices)
    for d in (4,5):
        mind=np.array(mins[d])
        np.savetxt(data/f'near_distances_d{d}_seed{seed}.csv',np.c_[ss,mind],delimiter=',',header='s,min_distance_after_dividing_B_by_sqrt_s',comments='')
        b=best[d]
        # Selected slice is the sampled slice with the smallest cross-interval distance.
        distances=np.linalg.norm(b['u'][:,None,:]-b['v'][None,:,:],axis=2)
        for coef in coeffs:
            ecounts=[];fcounts=[]
            for level,h in zip(levels,scales):
                radius=coef*np.sqrt(h)
                active=mind<=radius
                sboxes=np.minimum(np.floor((ss[active]-1)/h+1e-10).astype(int),int(round(1/h))-1)
                ec=int(np.unique(sboxes).size)
                pairs=np.argwhere(distances<=radius)
                if len(pairs):
                    uv=np.column_stack((uidx[pairs[:,0]]/a.n,vidx[pairs[:,1]]/a.n))
                    boxes=np.floor((uv-np.array([.25,1.5]))/h+1e-10).astype(np.int64)
                    fc=int(len(np.unique(boxes,axis=0)))
                else: fc=0
                ecounts.append(ec);fcounts.append(fc)
                all_curves.append({'seed':seed,'d':d,'coefficient':coef,'level':int(level),'h':float(h),'radius':float(radius),'exceptional_s_boxes':ec,'selected_fiber_boxes':fc,'selected_s':b['s'],'selected_min_distance':b['min_distance']})
            usable=(scales>=8/a.n)&(scales<=1/16)
            def fit(counts):
                counts=np.array(counts);use=usable&(counts>0)
                if np.sum(use)<3: return None
                x=np.log(1/scales[use]);y=np.log(counts[use]);slope,inter=np.polyfit(x,y,1)
                residual=np.sum((y-(slope*x+inter))**2);total=np.sum((y-y.mean())**2)
                return {'slope':float(slope),'r_squared':float(1-residual/total) if total>0 else None,'scales':scales[use].tolist(),'counts':counts[use].tolist()}
            summaries.append({'seed':seed,'d':d,'coefficient':coef,'selected_s':b['s'],'selected_min_distance':b['min_distance'],'exceptional_s_fit':fit(ecounts),'selected_fiber_fit':fit(fcounts)})
    # Save after every replicate, so interrupted computations still have their evidence.
    with (data/'box_counts.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(all_curves[0]));w.writeheader();w.writerows(all_curves)
    (data/'simulation_summary.json').write_text(json.dumps({'grid_n':a.n,'replicates_completed':rep+1,'domain_s':[1,2],'domain_u':[.25,1.25],'domain_v':[1.5,2.5],'threshold':'coefficient*sqrt(h), after dividing B(s,t) by sqrt(s)','fit_scales':'1/16 >= h >= 8/n','nice':os.getpriority(os.PRIO_PROCESS,0),'threads':1,'max_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'elapsed_seconds':time.monotonic()-start,'fits':summaries},indent=2)+'\n')
    print(f'replicate {rep+1}/{a.replicates} saved; elapsed {time.monotonic()-start:.1f}s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20:.1f} MiB',flush=True)
print('simulation complete',flush=True)
