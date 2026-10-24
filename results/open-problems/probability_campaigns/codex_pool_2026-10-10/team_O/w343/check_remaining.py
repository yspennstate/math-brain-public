"""Short mathematical checks for the assigned pass; all output is local."""
import itertools
import json
import math
import os
import time
from collections import deque
from fractions import Fraction
from pathlib import Path

os.environ['OPENBLAS_NUM_THREADS'] = '1'
import numpy as np
from scipy.integrate import quad

root = Path(__file__).resolve().parent
started = time.perf_counter()
all_results = {}

def emit(pid, data):
    data['command'] = 'python -X utf8 ~/brain_workers/w343/check_remaining.py'
    data['audit_status'] = 'pending-w347'
    all_results[pid] = data
    root.joinpath('measurement_'+pid.lower()+'.json').write_text(json.dumps(data, indent=2), encoding='utf-8')
    print(pid, json.dumps(data, ensure_ascii=False), flush=True)

# C0036: enumerate every increasing event, including rank-deficient endpoints.
upsets = [set(s for s in range(4) if mask & (1<<s)) for mask in range(16)
          if all(not(mask & (1<<s)) or all(mask & (1<<t) for t in range(4) if s&t==s)
                 for s in range(4))]
assert len(upsets) == 6
kernels = comparisons = 0
for ai in range(17):
    for bi in range(min(ai,16-ai)+1):
        a, b = ai/16, bi/16
        d = a*a-b*b
        mu = [1-2*a+d, a-d, a-d, d]
        p, q = math.sqrt(max(0,d)), 1-math.sqrt(max(0,(1-a)**2-b*b))
        product = lambda z: [(1-z)**2, z*(1-z), z*(1-z), z*z]
        lo, hi = product(p), product(q)
        for event in upsets:
            value = sum(mu[s] for s in event)
            assert sum(lo[s] for s in event) <= value+1e-12
            assert value <= sum(hi[s] for s in event)+1e-12
            comparisons += 2
        kernels += 1
a,b=0.5,0.25
d=a*a-b*b
p=math.sqrt(d)
assert (p+0.001)**2 > d
hm=2/(1/(a-b)+1/(a+b))
assert abs(hm-0.375) < 1e-14 and hm < p
emit('C0036', dict(kernels=kernels, increasing_event_comparisons=comparisons,
                  failures=0, sharpness_negative_control='density raised by 0.001 fails the all-present event',
                  harmonic_mean=hm, geometric_mean=p))

# P0013: exact theta values by matching independence and clique-cover certificates.
def graph_data(n, graph_mask, edge_pairs):
    edges = {edge_pairs[i] for i in range(len(edge_pairs)) if graph_mask & (1<<i)}
    subsets = range(1<<n)
    independent = lambda s: all(not(s&(1<<u) and s&(1<<v)) for u,v in edges)
    clique = lambda s: all((u,v) in edges for u,v in edge_pairs if s&(1<<u) and s&(1<<v))
    alpha = max(s.bit_count() for s in subsets if independent(s))
    cover=[0]+[n]*(2**n-1)
    for s in range(1,1<<n):
        c=s
        while c:
            if clique(c): cover[s]=min(cover[s],1+cover[s^c])
            c=(c-1)&s
    assert alpha == cover[-1]  # Sandwich alpha<=theta<=clique-cover certifies theta exactly.
    return alpha
theta_rows=[]
graphs=0
for n in range(1,5):
    pairs=list(itertools.combinations(range(n),2))
    mask_all=(1<<len(pairs))-1
    values=[]
    defect_product=defect_imbalance=0.0
    for mask in range(mask_all+1):
        t=graph_data(n,mask,pairs)
        tc=graph_data(n,mask_all^mask,pairs)
        x,y=t/math.sqrt(n),tc/math.sqrt(n)
        R=math.sqrt(x*y)
        Z=(math.log(x)-math.log(y))/2
        assert R >= 1-1e-12
        values.append(t)
        defect_product+=R-1
        defect_imbalance+=R*(math.cosh(Z)-1)
        graphs+=1
    count=len(values)
    lhs=sum(values)/count/math.sqrt(n)-1
    rhs=(defect_product+defect_imbalance)/count
    assert abs(lhs-rhs) < 1e-12
    theta_rows.append(dict(n=n, graphs=count, expected_theta=sum(values)/count,
                           product_defect=defect_product/count,
                           imbalance_defect=defect_imbalance/count))
emit('P0013', dict(graphs_certified=graphs, max_n=4, failures=0, finite_only=True, rows=theta_rows))

emit('P0150', dict(label='generic graph obstruction, not a critical configuration-model construction',
                  rows=[dict(m=m, path_vertices=math.isqrt(m),
                             rescaled_diameter=(math.isqrt(m)+1)/m**0.25,
                             probability_sample_of_10_hits_path=1-(m/(m+math.isqrt(m)))**10,
                             tip_radius_one_mass_upper=(math.floor(m**0.25)+1)/(m+math.isqrt(m)))
                        for m in [64,256,1024,4096,16384,65536]]))

laplace=[]
for L in [10,20,50,100]:
    lam=math.exp(-L)
    row={'log_inverse_lambda':L}
    for a in [0,1]:
        integral, error=quad(lambda x: math.exp(-math.exp(x-L))/x**a,1,L+math.log(40),
                             epsabs=1e-10,epsrel=1e-11,limit=150)
        F=-math.expm1(-lam*math.e)/math.e+lam*integral
        row['a'+str(a)+'_ratio_to_lambda_log']=F/(lam*L)
        row['a'+str(a)+'_ratio_to_predicted_scale']=F/(lam*(L if a==0 else math.log(L)))
        row['a'+str(a)+'_quadrature_error_estimate']=error
    laplace.append(row)
assert laplace[-1]['a0_ratio_to_lambda_log'] > 0.99
assert laplace[-1]['a1_ratio_to_lambda_log'] < 0.06
emit('C0003',dict(label='scalar-law route counterexample; no DGFF axioms claimed',rows=laplace))

bypass=[]
for H in [0,1,2,8,32]:
    start=(-1,0);target=(1,0)
    distances={start:0};queue=deque([start])
    while queue:
        x,y=queue.popleft()
        for xx,yy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            v=(xx,yy)
            if not(-1<=xx<=1 and -H-1<=yy<=H+1) or (xx==0 and abs(yy)<=H):continue
            if v not in distances:
                distances[v]=distances[(x,y)]+1;queue.append(v)
    assert distances[target]==2*H+4
    bypass.append(dict(H=H, removed_vertices=2*H+1, shortest_bypass=distances[target]))
emit('C0060',dict(finite_fiber_cases=len(bypass), failures=0, rows=bypass))

# C0085: all priority orders of the seven edges of a 2 by 3 ladder.
edges=[(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5)]
orders=0
for order in itertools.permutations(range(7)):
    ranks={edge:rank+1 for rank,edge in enumerate(order)}
    cluster={0}
    changed=True
    while changed:
        changed=False
        for ei,(u,v) in enumerate(edges):
            if ranks[ei]<=3 and ((u in cluster) != (v in cluster)):
                cluster.add(u);cluster.add(v);changed=True
    invaded={0}
    while True:
        boundary=[(ranks[ei],u,v) for ei,(u,v) in enumerate(edges) if (u in invaded)!=(v in invaded)]
        if not boundary or min(boundary)[0]>3:break
        rank,u,v=min(boundary)
        invaded.add(u);invaded.add(v)
    assert invaded==cluster
    orders+=1
emit('C0085',dict(edge_priority_orders=orders, finite_cluster_prefix_failures=0,
                  label='checks the finite sublevel-cluster lemma; does not test the invasion asymptotic'))

emit('C0131',dict(label='analytic stopping-time proof; the numbers below are illustrative bounds only',
                  neighbor_miss_bounds=[dict(opportunities=k, bound=(7/8)**k) for k in [8,32,128]],
                  mixed_walk_min_transition=1/8, biased_branch_drift=1/4,
                  mixed_walk_recurrence_probability=1/2,
                  iid_cookie_counterexample=False))

rng=np.random.default_rng(343)
frames=[]
minor_count=0
for m in range(1,7):
    subsets=np.array(list(itertools.combinations(range(2*m-1),m)),dtype=int)
    scaled=[]
    for _ in range(64):
        A=rng.normal(size=(2*m-1,m))
        singular=np.linalg.svd(A[subsets],compute_uv=False)
        omega=float(singular[:,-1].min())
        assert omega>0
        scaled.append(4**m*omega)
        minor_count+=len(subsets)
    frames.append(dict(m=m, frames=64, minors_per_frame=len(subsets),
                       median_four_to_m_omega=float(np.median(scaled)),
                       scaled_p10=float(np.quantile(scaled,.1)),scaled_p90=float(np.quantile(scaled,.9))))
emit('P0016',dict(label='finite numerical evidence for a cited existing answer; no limit-law inference',
                  seed=343, frames=384, minors_evaluated=minor_count, rows=frames,
                  m1_exact_law='absolute value of a standard normal'))

# P0046: exact finite-window connectivity sum, with rational probability.
delta=Fraction(1,10)
connected=Fraction(0)
for mask in range(256):
    if (mask&15) and (mask&240):
        k=mask.bit_count()
        connected+=delta**k*(1-delta)**(8-k)
expected=(1-(1-delta)**4)**2
assert connected==expected
emit('P0046',dict(exhaustive_finite_edge_configurations=256, rational_formula_verified=True,
                  finite_interfaces_probability=float(connected),
                  window_rows=[dict(H=H,delta=.01,columns=5,
                                    connectivity_probability=(1-(1-.01)**(2*H+1))**4)
                               for H in [2,8,32,128,512]],
                  general_fusf_interface_hypothesis_unproved=True))

summary={'elapsed_seconds':time.perf_counter()-started, 'problems_checked':len(all_results),
         'results':all_results}
root.joinpath('measurement_remaining_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print('ELAPSED_SECONDS',summary['elapsed_seconds'])
