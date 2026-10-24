from pathlib import Path
import numpy as np,json,time,math
from fractions import Fraction
P=Path(__file__).parent;rng=np.random.default_rng(85002);start=time.perf_counter()
a=3.0;M=1;h=0.2
axis=np.arange(-4.9,5.0,h); xx,yy=np.meshgrid(axis,axis);sites=np.column_stack([xx.ravel(),yy.ravel()])
qa=np.linspace(-1.5,1.5,31);xx,yy=np.meshgrid(qa,qa);query=np.column_stack([xx.ravel(),yy.ravel()]);net_radius=math.sqrt(2)*0.05
delta=Fraction(71,1000);delta2=delta*delta
qfrac=[Fraction(float(t)) for t in qa];qpoints=[(x,y) for y in qfrac for x in qfrac]
gap=max(y-x for x,y in zip(qfrac,qfrac[1:]));assert gap*gap<=2*delta2
assert qfrac[0]==Fraction(-3,2) and qfrac[-1]==Fraction(3,2)
allrows=[]
with (P/'round2_samples.jsonl').open('w',encoding='utf8',buffering=1) as f:
 for sample in range(24):
  if time.perf_counter()-start>120:break
  k=int(rng.poisson(36))
  if k>128 or k==0:
   row=dict(sample=sample,centres=k,skipped=True);f.write(json.dumps(row)+'\n');allrows.append(row);continue
  centres=rng.uniform(-3,3,size=(k,2));ds=((sites[:,None,:]-centres[None,:,:])**2).sum(axis=2);order=np.argsort(ds,axis=None);dq=np.sqrt(((query[:,None,:]-centres[None,:,:])**2).sum(axis=2))
  previous=None
  for quota in [23,24,25]:
   assignment=np.full(len(sites),-1,dtype=np.int32);loads=np.zeros(k,dtype=np.int32);r2=np.zeros(k);total=0
   for idx in order:
    si=int(idx)//k;ci=int(idx)%k
    if assignment[si]<0 and loads[ci]<quota:
     assignment[si]=ci;loads[ci]+=1;r2[ci]=max(r2[ci],float(ds[si,ci]));total+=1
     if total==quota*k:break
   own=np.full(len(sites),np.inf);claimed=assignment>=0;own[claimed]=ds[np.flatnonzero(claimed),assignment[claimed]]
   instability=int(np.count_nonzero((ds<own[:,None])&((ds<r2[None,:])|(loads[None,:]<quota))))
   margins=np.max(np.sqrt(r2)[None,:]-dq,axis=1);margin=float(margins.min())
   cfrac=[(Fraction(float(x)),Fraction(float(y))) for x,y in centres];rfrac=[Fraction(float(x)) for x in r2]
   exact_cover=False;exact_hole=False
   if margin>float(delta):
    best=np.argmax(np.sqrt(r2)[None,:]-dq,axis=1);exact_cover=True
    for qi,(x,y) in enumerate(qpoints):
     ci=int(best[qi]);cx,cy=cfrac[ci];d2=(x-cx)**2+(y-cy)**2;b=rfrac[ci]-d2-delta2
     if not (b>0 and b*b>4*d2*delta2):exact_cover=False;break
   elif margin<=0:
    x,y=qpoints[int(np.argmin(margins))]
    exact_hole=all((x-cx)**2+(y-cy)**2>=rfrac[ci] for ci,(cx,cy) in enumerate(cfrac))
   row=dict(sample=sample,centres=k,appetite=quota*h*h,quota=quota,all_sated=bool(np.all(loads==quota)),unstable_pairs=instability,min_query_margin=margin,surrogate_ball_cover='certified_by_net' if exact_cover else 'uncovered_witness' if exact_hole else 'inconclusive',radius_monotonicity_violations=0 if previous is None else int(np.count_nonzero(r2+1e-12<previous[0])),site_distance_monotonicity_violations=0 if previous is None else int(np.count_nonzero(own>previous[1]+1e-12)))
   f.write(json.dumps(row)+'\n');allrows.append(row);previous=(r2.copy(),own.copy())
summary=dict(seed=85002,model='Finite equal-mass lattice sites, continuous Poisson centres, greedy distance matching; NOT the continuum allocation',block_side=a,buffer_half_side=a*M,site_mesh=h,query_net_radius=net_radius,exact_net_radius='71/1000',geometry_check='Exact Fraction inequalities for cover margins and uncovered witnesses, for the floating squared radii interpreted as rationals',domain=[-5,5],elapsed_seconds=time.perf_counter()-start,peierls_threshold=1/(4096*9),rows=len(allrows),cases={})
for quota in [23,24,25]:
 rows=[r for r in allrows if r.get('quota')==quota]
 summary['cases'][str(quota)]=dict(samples=len(rows),all_sated=sum(r['all_sated'] for r in rows),uncovered_witnesses=sum(r['surrogate_ball_cover']=='uncovered_witness' for r in rows),certified_surrogate_covers=sum(r['surrogate_ball_cover']=='certified_by_net' for r in rows),unstable_pairs=sum(r['unstable_pairs'] for r in rows),radius_order_violations=sum(r['radius_monotonicity_violations'] for r in rows),site_distance_order_violations=sum(r['site_distance_monotonicity_violations'] for r in rows))
(P/'round2_experiment_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf8');print(json.dumps(summary,indent=2))
