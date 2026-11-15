# Direct finite-state generator and Poisson uniformization, independent of rate tree.
import csv,json,math,pathlib
import numpy as np
root=pathlib.Path(__file__).resolve().parents[1]
result=[]
for label,q in [('055',.55),('070',.7)]:
    n=5; states=list(range(2**n-1)); N=len(states); Q=np.zeros((N,N)); p=1-q
    for s in states:
        for j in range(n):
            enabled=(j>0 and (s>>(j-1))&1==0) or (j+1<n and (s>>(j+1))&1==0)
            if enabled:
                dest=s^(1<<j); rate=q if (s>>j)&1 else p
                assert dest<N
                Q[s,dest]+=rate; Q[s,s]-=rate
    weights=np.array([p**s.bit_count()*q**(n-s.bit_count()) for s in states]); weights/=weights.sum()
    initial=(2**n-1)^(1<<(n//2)); row=np.zeros(N); row[initial]=1
    rate=max(-np.diag(Q)); P=np.eye(N)+Q/rate
    def evolve(t):
        term=row.copy(); mass=math.exp(-rate*t); total=mass*term
        for k in range(1,1000):
            term=term@P;mass*=rate*t/k;total+=mass*term
            if k>rate*t+15 and mass<1e-16:break
        assert abs(total.sum()-1)<2e-13
        return total
    hist={int(r['occupation_bits']):int(r['count']) for r in csv.DictReader((root/'data'/f'check{label}_hist.csv').open())}
    paths=sum(hist.values()); exact=evolve(5)
    residuals=[]
    for s in states:
        se=math.sqrt(exact[s]*(1-exact[s])/paths)
        residuals.append((hist[s]/paths-exact[s])/se)
    time_checks=[]
    for r in csv.DictReader((root/'data'/f'check{label}.csv').open()):
        t=float(r['time']); dist=evolve(t); target=sum(dist[s] for s in states if (s>>(n//2))&1==0)
        measured=float(r['origin_zero_mean']); se=math.sqrt(target*(1-target)/paths)
        time_checks.append({'t':t,'exact':target,'mc':measured,'z':(measured-target)/se if se else 0})
    result.append({'q':q,'paths':paths,'row_sum_max':float(abs(Q.sum(axis=1)).max()),'detailed_balance_max':float(abs(weights[:,None]*Q-weights[None,:]*Q.T).max()),'stationary_residual_max':float(abs(weights@Q).max()),'histogram_max_abs_z':float(max(map(abs,residuals))),'time_checks':time_checks})
(root/'data'/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
