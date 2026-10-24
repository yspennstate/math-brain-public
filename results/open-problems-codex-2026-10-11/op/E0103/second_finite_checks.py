from pathlib import Path
import json, math, time
import numpy as np
from scipy.integrate import quad

start=time.time()
rng=np.random.default_rng(103112026)
lam,b=1.,.4
old=json.loads(Path('second_checks.json').read_text())
finite=[]
for row in old['direct_exponential_speed_particle_simulations']:
    L,p0,z=row['L'],row['p0'],row['z']
    m=1-p0
    t=(math.log(lam*L)+z-lam*b)/(lam*m)
    rho=math.exp(-lam*(b+t*m))*lam
    def integrand(x):
        e=math.exp(-x)
        if x==0 and p0==0:delta=-rho
        else:
            logratio=math.log1p(-m*e)+lam*m*t*e
            delta=rho*math.expm1(logratio)
        return (L-b-t*x)*delta
    xmax=min((L-b)/t,100.)
    points=[x for x in [1.,5.,20.,50.] if x<xmax]
    val,err=quad(integrand,0,xmax,points=points,epsabs=1e-8,limit=250)
    integral=-rho*(L*b-b*b/2)+t*val
    exactvar=math.exp(-z)+2*rho*integral
    mean_se=math.sqrt(exactvar/row['replicates'])
    assert abs(row['empirical_hole_mean']-row['exact_hole_mean'])<5*mean_se
    finite.append({'p0':p0,'L':L,'z':z,'finite_exact_variance':exactvar,
                   'empirical_variance':row['empirical_hole_variance'],
                   'asymptotic_variance':row['limiting_hole_variance'],
                   'mean_standard_error_from_exact_variance':mean_se})

# A separate direct construction, with bounded moving speed 1. It has much
# faster local-kernel convergence and tests the stationary-atom correction.
bounded=[]
for p0 in [0.,.4,.8]:
    L,reps,z=3000.,5000,0.
    t=(math.log(L)-b)/(1-p0)
    maxell=b+t
    covered=0
    holes=[]
    for _ in range(reps):
        n=rng.poisson(L+maxell)
        ends=rng.uniform(0,L+maxell,n)
        lens=b+t*(rng.random(n)>=p0)
        starts=ends-lens
        order=np.argsort(starts)
        starts,ends=starts[order],ends[order]
        running=np.maximum.accumulate(ends)
        ce=np.r_[running[:-1][starts[1:]>running[:-1]],running[-1]]
        cs=starts[np.r_[True,starts[1:]>running[:-1]]]
        H=np.count_nonzero((ce>0)&(ce<L))
        holes.append(H)
        ok=np.any((cs<=0)&(ce>=L))
        assert ok==((H==0) and np.any(starts<=0))
        covered+=bool(ok)
    J=p0*math.exp(-b)/(1-p0)
    theta=1/(1+J)
    pred=math.exp(-theta)
    bounded.append({'p0':p0,'L':L,'replicates':reps,
                    'empirical_coverage':covered/reps,'corrected_limit':pred,
                    'uncorrected_limit':math.exp(-1.),
                    'empirical_hole_mean':float(np.mean(holes)),
                    'empirical_hole_variance':float(np.var(holes)),
                    'limiting_variance':1+2*J,
                    'binomial_standard_error':math.sqrt(pred*(1-pred)/reps)})
out={'exponential_speed_finite_pair_moments':finite,'bounded_mixture_direct_simulation':bounded,
     'elapsed_seconds':time.time()-start,'note':'Exponential-speed CDFs at modest L have visible finite-size errors. Finite exact moments check the formula; simulations do not prove limits.'}
Path('second_finite_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
