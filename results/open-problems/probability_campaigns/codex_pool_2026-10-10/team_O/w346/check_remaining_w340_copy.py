"""Fast, reproducible checks of the eight scoped results; write each receipt immediately."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import json
import math
import time
from collections import deque
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
started=time.perf_counter()
def save(problem,details):
    payload={'problem_id':problem,'command':'python -X utf8 check_remaining.py','label':'finite checks; independent audit pending','elapsed_seconds':time.perf_counter()-started,**details}
    (ROOT/(problem.lower()+'_checks.json')).write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(problem,json.dumps(details,ensure_ascii=False),flush=True)

# C0135: invert in logarithmic coordinates to avoid overflowing a long clock.
inversions=[]
for log_t in [math.log(1e6),math.log(1e12),math.log(1e24),math.log(1e48),math.log(1e96),math.log(1e192)]:
    lo,hi=1e-8,log_t
    for _ in range(80):
        y=(lo+hi)/2
        if 2*y+math.log(y)<log_t: lo=y
        else: hi=y
    y=(lo+hi)/2
    log_u=(log_t+math.log(2)-math.log(log_t))/2
    log_wrong=log_t/2-math.log(log_t)
    inversions.append({'log_t':log_t,'exact_inverse_over_correct_asymptotic':math.exp(y-log_u),'exact_inverse_over_old_sqrt_t_over_log_t':math.exp(y-log_wrong),'log_clock_residual':2*y+math.log(y)-log_t})
assert max(abs(x['log_clock_residual']) for x in inversions)<2e-12
assert abs(inversions[-1]['exact_inverse_over_correct_asymptotic']-1)<abs(inversions[0]['exact_inverse_over_correct_asymptotic']-1)
save('C0135',{'clock':'m^2 log(m), an illustrative deterministic clock only','inversions':inversions,'warning':'No ERW backtracking estimate was measured or proved.'})

# P0109: two exact Laplace certificates, including a zero atom and an infinite-mean law.
Delta=6
theta=16.
q=.1+.9/(1+theta)  # .1 atom at zero plus .9 Exp(1)
ratio=(Delta-1)*q
assert ratio<1
theta_heavy=4.
q_upper=.1+.9*math.exp(-theta_heavy)  # positive component Pareto(alpha=.5) supported on [1,infinity)
assert (Delta-1)*q_upper<1
lengths=[10,20,40,80,160]
save('P0109',{'maximum_degree':Delta,'zero_atom':.1,'exponential_mixture_theta':theta,'exponential_mixture_path_ratio':ratio,'infinite_mean_pareto_mixture_theta':theta_heavy,'infinite_mean_path_ratio_upper_bound':(Delta-1)*q_upper,'normalized_geometric_terms':{str(n):ratio**n for n in lengths},'scope':'Certificates of a sufficient criterion, not a numerical resolution of the arbitrary-law question.'})

# P0441: direct cycle simulation, independent of the closed-form wait formula.
rng=np.random.default_rng(3400441)
lam,mu,tau=.8,1.4,1.1
rho=lam/mu
power_busy,power_idle,power_off,power_setup=200.,120.,5.,150.
results=[]
for grace in [0.,.5,2.,math.inf]:
    cycles=20000
    records=[]
    for _ in range(cycles):
        gap=float(rng.exponential(1/lam))
        hot_idle=min(gap,grace)
        off_idle=max(0.,gap-grace)
        setup=tau if gap>grace else 0.
        k=1
        jobs=1
        wait_area=0.
        if setup:
            extra=int(rng.poisson(lam*setup))
            jobs+=extra
            k+=extra
            arrival_times=rng.uniform(0,setup,extra)
            wait_area+=setup+float(np.sum(setup-arrival_times))
        busy=0.
        while k:
            dt=float(rng.exponential(1/(lam+mu)))
            busy+=dt
            wait_area+=(k-1)*dt
            if rng.random()<lam/(lam+mu):
                k+=1
                jobs+=1
            else:
                k-=1
        duration=gap+setup+busy
        power_area=busy*power_busy+hot_idle*power_idle+off_idle*power_off+setup*power_setup
        records.append((duration,jobs,wait_area,power_area,busy,hot_idle,off_idle,setup))
    data=np.array(records)
    p=0. if math.isinf(grace) else math.exp(-lam*grace)
    x=lam*tau
    y=p/(1+x*p)
    predicted_wait=lam/(mu*(mu-lam))+tau*(1+x/2)*y
    predicted_power=rho*power_busy+(1-rho)*power_idle+(1-rho)*(power_off+x*power_setup-(1+x)*power_idle)*y
    measured_wait=float(data[:,2].sum()/data[:,1].sum())
    measured_power=float(data[:,3].sum()/data[:,0].sum())
    wait_residual=data[:,2]-measured_wait*data[:,1]
    power_residual=data[:,3]-measured_power*data[:,0]
    wait_se=float(wait_residual.std(ddof=1)/math.sqrt(cycles)/data[:,1].mean())
    power_se=float(power_residual.std(ddof=1)/math.sqrt(cycles)/data[:,0].mean())
    assert abs(measured_wait-predicted_wait)<=5*wait_se+.003
    assert abs(measured_power-predicted_power)<=5*power_se+.03
    model_fractions=[rho,(1-rho)*(1-p)/(1+x*p),(1-rho)*p/(1+x*p),(1-rho)*x*p/(1+x*p)]
    assert abs(sum(model_fractions)-1)<1e-14
    results.append({'grace':'infinity' if math.isinf(grace) else grace,'cycles':cycles,'predicted_wait':predicted_wait,'measured_wait':measured_wait,'wait_standard_error':wait_se,'wait_z_score':(measured_wait-predicted_wait)/wait_se,'predicted_power':predicted_power,'measured_power':measured_power,'power_standard_error':power_se,'power_z_score':(measured_power-predicted_power)/power_se,'model_fractions':model_fractions,'observed_fractions':[float(data[:,k].sum()/data[:,0].sum()) for k in [4,5,6,7]],'observed_arrival_rate':float(data[:,1].sum()/data[:,0].sum())})
save('P0441',{'seed':3400441,'lambda':lam,'mu':mu,'setup':tau,'simulation':results,'scope':'M/M/1, deterministic grace/setup, no setup cancellation; Monte Carlo checks complement the proof.'})

# C0045: solve absorption probabilities independently by a linear system.
exit_checks=[]
theta=.5*math.log(3)
mgf=.45*math.exp(-theta)+.15*math.exp(theta)+.4
assert mgf<1
for L in [2,4,8,16,32]:
    states=2*L-1
    A=np.eye(states)*.6
    for i in range(states-1):
        A[i,i+1]=-.45
        A[i+1,i]=-.15
    b=np.zeros(states)
    b[0]=.15
    probability=float(np.linalg.solve(A,b)[L-1])
    bound=math.exp(-theta*L)
    assert 0<=probability<=bound
    exit_checks.append({'L':L,'backward_before_forward_probability':probability,'supermartingale_bound':bound})
save('C0045',{'homogeneous_first_coordinate_law':{'plus':.45,'minus':.15,'zero':.4},'mean_drift':.3,'theta':theta,'mgf':mgf,'absorption_checks':exit_checks,'scope':'Independent homogeneous increments, not general annealed RWRE increments.'})

# C0081: high precision avoids losing the exponentially small residue.
pole_checks=[]
with localcontext() as ctx:
    ctx.prec=100
    for d in [8,16,32,64]:
        dd=Decimal(d)
        a=Decimal(1)-Decimal(1)/dd
        residue=(-dd).exp()
        worst=Decimal(0)
        for numerator in range(81):
            z=Decimal(numerator)/Decimal(100)
            base=Decimal(1)/(1-z)
            F=(base+residue/(1-z/a))/(1+residue)
            worst=max(worst,abs(F-base))
        bound=Decimal(15)*residue  # eps=.2
        assert worst<=bound
        pole_checks.append({'d':d,'actual_pole':str(a),'pole_shift':str(1-a),'max_error_on_grid_0_to_0_8':str(worst),'uniform_error_bound':str(bound)})
save('C0081',{'precision_digits':100,'grid_points_per_d':81,'pole_examples':pole_checks,'scope':'Analytic countermodel to a general extrapolation step, not a percolation distribution.'})

# C0123: enumerate every high-level vertex and every one-bit edge.
def component_count(weights,delta):
    m=len(weights)
    bits=2*m
    allowed=set()
    for state in range(1<<bits):
        deficit=sum(weights[i] for i in range(m) if ((state>>(2*i))&1)!=((state>>(2*i+1))&1))
        if deficit<=delta+1e-12:
            allowed.add(state)
    total=len(allowed)
    components=0
    while allowed:
        components+=1
        seed=allowed.pop()
        queue=deque([seed])
        while queue:
            state=queue.popleft()
            for bit in range(bits):
                neighbor=state^(1<<bit)
                if neighbor in allowed:
                    allowed.remove(neighbor)
                    queue.append(neighbor)
    predicted=2**sum(w>delta+1e-12 for w in weights)
    assert components==predicted
    return {'bits':bits,'weights':weights,'delta':delta,'vertices_at_level':total,'components':components,'predicted_components':predicted}
component_checks=[]
for bits in [2,4,6,8,10,12]:
    for delta in [.9,1.]:
        component_checks.append(component_count([1.]* (bits//2),delta))
for delta in [.6,.7,1.1,1.2,2.]:
    component_checks.append(component_count([.7,1.2,2.],delta))
save('C0123',{'exhaustive_landscape_checks':component_checks,'scope':'Deterministic paired-block K=1 NK-form landscape.'})

# P0012: test the norm identity using explicit optimizers and independent unit vectors.
rng=np.random.default_rng(3400012)
norm_checks=0
max_optimizer_error=0.
for r in [2,3,4]:
    for p in [2.,3.,4.,5.,6.,8.,12.,math.inf]:
        for trial in range(30):
            a=rng.normal(size=7)
            if p<=r:
                norm=float(np.max(abs(a)))
                x=np.zeros(7)
                j=int(np.argmax(abs(a)))
                x[j]=1.
            elif math.isinf(p):
                norm=float(np.sum(abs(a)))
                x=np.ones(7)
            else:
                q=p/(p-r)
                norm=float(np.linalg.norm(a,ord=q))
                x=abs(a)**(1/(p-r))
                x=x/np.linalg.norm(x,ord=p)
            achieved=float(abs(np.sum(abs(a)*x**r)))
            max_optimizer_error=max(max_optimizer_error,abs(achieved-norm))
            assert abs(achieved-norm)<1e-10
            vectors=rng.normal(size=(r,7))
            for k in range(r):
                vectors[k]/=np.linalg.norm(vectors[k],ord=np.inf if math.isinf(p) else p)
            value=float(abs(np.sum(a*np.prod(vectors,axis=0))))
            assert value<=norm+1e-12
            norm_checks+=1
gaussian_checks=[]
for r,p in [(3,2.),(3,4.),(3,6.),(3,12.),(3,math.inf)]:
    d,n,samples=20,12,20000
    coefficients=rng.normal(size=(n,d))
    G=rng.normal(size=(samples,n))
    Z=G@coefficients
    if p<=r:
        tensor_norms=np.max(abs(coefficients),axis=1)
        observations=np.max(abs(Z),axis=1)
        factor=math.sqrt(2*math.log(2*d))
    else:
        q=1. if math.isinf(p) else p/(p-r)
        tensor_norms=np.linalg.norm(coefficients,ord=q,axis=1)
        observations=np.linalg.norm(Z,ord=q,axis=1)
        if q>=2:
            factor=math.exp((q/2*math.log(2)+math.lgamma((q+1)/2)-.5*math.log(math.pi))/q)
        else:
            factor=d**(1/q-.5)
    upper=factor*float(np.linalg.norm(tensor_norms))
    empirical=float(np.mean(observations))
    se=float(np.std(observations,ddof=1)/math.sqrt(samples))
    assert empirical<=upper+5*se
    gaussian_checks.append({'r':r,'p':'infinity' if math.isinf(p) else p,'samples':samples,'empirical_expected_norm':empirical,'standard_error':se,'proved_upper_bound':upper,'mean_over_bound':empirical/upper})
save('P0012',{'optimizer_checks':norm_checks,'max_optimizer_identity_error':max_optimizer_error,'gaussian_checks':gaussian_checks,'mixed_sign_even_polynomial_warning':{'r':2,'p':'infinity','a':[1,-1],'multilinear_norm':2,'homogeneous_same_vector_norm':1},'scope':'Diagonal multilinear tensors; source convention must be checked.'})

# P0038: exact rational layer resistance and a recurrent stretched branching tree.
resistances=[]
for depth in [4,8,16,32,64]:
    linear=sum((Fraction(k,2**k) for k in range(1,depth+1)),Fraction())
    expected=Fraction(2)-Fraction(depth+2,2**depth)
    assert linear==expected
    exponential=sum((Fraction(2**k,2**k) for k in range(1,depth+1)),Fraction())
    assert exponential==depth
    resistances.append({'depth':depth,'linear_corridor_resistance':float(linear),'linear_exact':str(linear),'exponential_corridor_resistance':int(exponential)})
save('P0038',{'exact_layer_checks':resistances,'linear_limit':2,'exponential_limit':'infinity','scope':'Subdivided binary trees and conditional finite-energy embedding; not general Bernoulli clusters.'})
