"""Exact arithmetic corroboration of the abstract energy counterexample."""
from fractions import Fraction as F
from pathlib import Path
import json
import time

started=time.perf_counter()
def p(x): return F(3,4) if x>0 else F(1,4) if x<0 else F(1,2)
def h(x): return F(1,2) if x==0 else 1-F(1,2*3**x) if x>0 else F(1,2*3**(-x))
def energy(x): return p(x)*(h(x+1)-h(x))**2+(1-p(x))*(h(x-1)-h(x))**2
for x in range(-30,31):
    assert p(x)*h(x+1)+(1-p(x))*h(x-1)==h(x)
    assert energy(x)==(F(1,9) if x==0 else F(1,3**(2*abs(x)+1)))
mass=F(1,2)+2*F(1,4)*(F(1,2)/(1-F(1,2)))
original_energy=F(1,18)+F(1,6)*(F(1,18)/(1-F(1,18)))
original_variance=F(1,8)+F(1,4)*(F(1,6)/(1-F(1,6)))-F(1,8)*(F(1,18)/(1-F(1,18)))
assert mass==1
assert original_energy==F(10,153)
assert original_variance==F(57,340)

# An exact finite-horizon check from zero of the same telescoping identity.
law={0:F(1)}
initial_square=h(0)**2
cumulative=F(0)
observations=[]
for n in range(64):
    cumulative+=sum(weight*energy(x) for x,weight in law.items())
    next_law={}
    for x,weight in law.items():
        for y,prob in ((x+1,p(x)),(x-1,1-p(x))):
            next_law[y]=next_law.get(y,F(0))+weight*prob
    law=next_law
    square=sum(weight*h(x)**2 for x,weight in law.items())
    assert sum(law.values())==1
    assert cumulative==square-initial_square
    assert cumulative<=F(1,4)
    if n+1 in (1,8,32,64):
        observations.append({'N':n+1,'mean_energy_from_zero_approx':float(cumulative/(n+1)),'exact_bound':str(F(1,4*(n+1)))})
result={
 'command':'python -X utf8 ~/brain_workers/w577/check_starvation.py',
 'method':'Exact geometric-series arithmetic plus 64 exact finite-horizon square-martingale identities',
 'fresh_compute_gate':{'harmonicity_vertices':61,'time_horizon':64,'maximum_states':65,'gpu':False,'training':False,'wall_limit_seconds':60},
 'full_support_initial_measure_mass':str(mass),'original_measure_energy':str(original_energy),
 'original_measure_escape_variance':str(original_variance),
 'cesaro_energy_bound':'57/(340*N), proved for the full-support initial measure',
 'finite_horizon_checks':observations,'elapsed_seconds':time.perf_counter()-started,
 'iid_spatial_stationarity':False,'target_solved':False,
}
assert result['elapsed_seconds']<60
Path(__file__).with_name('STARVATION_MEASUREMENT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
