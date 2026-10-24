"""Independent random-interval simulations and kernel checks for Theorem F."""
from pathlib import Path
import math, json, time
import numpy as np
from scipy.integrate import quad

rng=np.random.default_rng(1031102026)
start=time.time()
lam, b = 1., .4
rows=[]

def base_speeds(n, p0):
    u=rng.exponential(size=n)
    u[rng.random(n)<p0]=0.
    return u

def sample_local_intervals(L,t,p0):
    # Exact marked-Poisson restriction to intervals meeting [0,L], including
    # arbitrarily large exponential speeds. Endpoints in [0,L] have base marks;
    # endpoints beyond L have length-biased marks and range L to L+ell.
    m=1-p0
    n=rng.poisson(lam*L)
    ends=rng.uniform(0,L,n)
    lens=b+t*base_speeds(n,p0)
    mean_len=b+t*m
    n2=rng.poisson(lam*mean_len)
    # Length bias of b+tU is the mixture b*mu plus t*m*(U-size-biased mu).
    ub=rng.gamma(2.,size=n2)
    choose_base=rng.random(n2)<b/mean_len
    ub[choose_base]=base_speeds(int(choose_base.sum()),p0)
    lens2=b+t*ub
    ends2=L+rng.random(n2)*lens2
    ends=np.r_[ends,ends2]
    lens=np.r_[lens,lens2]
    if len(ends)==0:
        return 0,False
    starts=ends-lens
    order=np.argsort(starts)
    starts,ends=starts[order],ends[order]
    running=np.maximum.accumulate(ends)
    component_ends=np.r_[running[:-1][starts[1:]>running[:-1]],running[-1]]
    H=int(np.count_nonzero((component_ends>0)&(component_ends<L)))
    # Independently identify component starts to check the boundary lemma.
    newcomponent=np.r_[True,starts[1:]>running[:-1]]
    component_starts=starts[newcomponent]
    covered=bool(np.any((component_starts<=0)&(component_ends>=L)))
    zero_covered=bool(np.any(starts<=0))
    assert covered == ((H==0) and zero_covered)
    return H,covered

for p0 in [0.,.4,.8]:
    J=p0*math.exp(-lam*b)/(1-p0)
    theta=1/(1+J)
    for L,reps in [(300.,3000),(3000.,2500)]:
        for z in [-1.,0.,1.]:
            t=(math.log(lam*L)+z-lam*b)/(lam*(1-p0))
            values=np.empty(reps,dtype=int)
            covered=0
            for i in range(reps):
                values[i],ok=sample_local_intervals(L,t,p0)
                covered+=ok
            mu=math.exp(-z)
            limit=math.exp(-theta*mu)
            empirical=covered/reps
            rows.append({'p0':p0,'L':L,'z':z,'replicates':reps,
                         'empirical_coverage':empirical,'limiting_coverage':limit,
                         'uncorrected_Poisson_prediction':math.exp(-mu),
                         'empirical_hole_mean':float(values.mean()),'exact_hole_mean':mu,
                         'empirical_hole_variance':float(values.var()),
                         'limiting_hole_variance':mu*(1+2*J),
                         'binomial_standard_error':math.sqrt(limit*(1-limit)/reps)})

# Nonzero speeds exponential: F(h) and E min(h,b+tU) are explicit. With an
# atom at zero, E min = b + (1-p0)*t*(1-exp(-(h-b)/t)) for h>b.
def kernel(h,t,p0):
    if h<=b:return 0.
    x=(h-b)/t
    F=p0+(1-p0)*(-math.expm1(-x))
    emin=b+(1-p0)*t*(-math.expm1(-x))
    return lam*F*math.exp(-lam*emin)

krows=[]
for p0 in [0.,.4,.8]:
    m=1-p0
    J=p0*math.exp(-lam*b)/m
    # Integrate only up to t^2: relative far-tail error is exp-small, and
    # subtraction of the tiny rho background is harmless at these t values.
    for t in [10.,50.,200.]:
        val,err=quad(lambda h:kernel(h,t,p0),b,t*t,points=[b+t],epsabs=1e-8,limit=200)
        rho=lam*math.exp(-lam*(b+t*m))
        krows.append({'p0':p0,'t':t,'kernel_mass_up_to_t_squared':val,
                      'background_rho_times_t_squared':rho*t*t,
                      'limiting_local_mass_J':J,'quadrature_error':err})

out={'direct_exponential_speed_particle_simulations':rows,'explicit_kernel_integrals':krows,
     'elapsed_seconds':time.time()-start,'seed':1031102026}
Path('second_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
