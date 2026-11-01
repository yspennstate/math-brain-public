"""Tiny exact controls for the measure-change and martingale failure modes.

These controls are finite mathematical examples, not blind test-bank items and
not a computer proof of C0044. Only Python's standard library is used.
"""
import itertools
import json
import time
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
gate = {'task': 'C0044 finite exact controls', 'max_path_length': 6,
        'max_path_cases': 20000, 'max_wall_seconds': 10,
        'gpu': False, 'training': False, 'network': False,
        'parallel_workers': 1, 'writes': 'w579 folder only'}
(ROOT / 'COMPUTE_GATE.json').write_text(json.dumps(gate, indent=2)+'\n', encoding='utf-8')
start = time.perf_counter()
cases = 0
checks = 0

def check(flag):
    global checks
    assert flag
    checks += 1

def path_prob(phase, x, steps):
    global cases
    cases += 1
    assert cases <= gate['max_path_cases']
    assert time.perf_counter()-start < gate['max_wall_seconds']
    p = F(1)
    rights = [F(1,4), F(1,2), F(3,4)]
    for e in steps:
        q = rights[(phase+x)%3]
        p *= q if e==1 else 1-q
        x += e
    return x,p

# Three-phase periodic environment: independent endpoint path enumeration,
# reverse incoming mass, and adjoint recurrence must give the same density.
rights = [F(1,4), F(1,2), F(3,4)]
previous = [F(1)]*3
max_density_residual = F(0)
one_step_mu = None
one_step_density = None
for n in range(gate['max_path_length']+1):
    paths = list(itertools.product((-1,1), repeat=n))
    mu = [F(0)]*3
    for phase in range(3):
        for steps in paths:
            x,p = path_prob(phase,0,steps)
            mu[(phase+x)%3] += p/3
    rev = []
    for phase in range(3):
        s = F(0)
        for x0 in range(-n,n+1):
            for steps in paths:
                x,p = path_prob(phase,x0,steps)
                if x==0:
                    s += p
        rev.append(s)
    for phase in range(3):
        residual = abs(rev[phase]-3*mu[phase])
        max_density_residual = max(max_density_residual,residual)
        check(residual==0)
        if n:
            adjoint = rights[(phase-1)%3]*previous[(phase-1)%3] + (1-rights[(phase+1)%3])*previous[(phase+1)%3]
            check(rev[phase]==adjoint)
    check(sum(mu)==1)
    if n==1:
        one_step_mu,one_step_density = mu,rev
    previous = rev

# Peer w580 owns the IID one-step covariance calculation. Keep this disjoint
# stationary ergodic periodic control: uniform phase law gives phi=1_(phase=1)
# probability 1/3, but direct endpoint enumeration gives 1/6 at time one.
check(one_step_density==[F(5,4),F(1,2),F(5,4)])
check(one_step_mu[1]==F(1,6))
static_error = abs(F(1,3)-one_step_mu[1])
corrected_error = abs(one_step_density[1]/3-one_step_mu[1])
check(static_error==F(1,6) and corrected_error==0)

# An absorbing symmetric gambler's ruin chain tests the energy normalization
# when M_0 is random. It is a generic martingale control, not an elliptic
# infinite-lattice environment or a C0044 counterexample.
h = [F(i,4) for i in range(5)]
dist = [F(0),F(1,2),F(0),F(1,2),F(0)]
initial_uncertainty = sum(dist[i]*h[i]*(1-h[i]) for i in range(5))
p = sum(dist[i]*h[i] for i in range(5))
energy = F(0)
check(initial_uncertainty==F(3,16) and p*(1-p)==F(1,4))
max_energy_residual = F(0)
for n in range(41):
    uncertainty = sum(dist[i]*h[i]*(1-h[i]) for i in range(5))
    residual = abs(uncertainty+energy-initial_uncertainty)
    max_energy_residual = max(max_energy_residual,residual)
    check(residual==0)
    energy += sum(dist[1:4])/16
    nxt = [F(0)]*5
    nxt[0] += dist[0]
    nxt[4] += dist[4]
    for i in range(1,4):
        nxt[i-1] += dist[i]/2
        nxt[i+1] += dist[i]/2
    dist = nxt

# Compactness alone: g_N=N*1_(0,1/N) on [0,1] has a singular weak limit.
# Exact moments exercise the UI/norm obstruction without a convergence claim
# about the actual RWRE. Norm squared = N and entropy = log N analytically.
compactness = []
for n in [2,4,8,16,32]:
    mass, uncertainty, l2sq = F(n)*F(1,n), F(n)*F(1,2*n*n), F(n*n)*F(1,n)
    check(mass==1 and uncertainty==F(1,2*n) and l2sq==n)
    compactness.append({'N':n,'uncertainty':str(uncertainty),'L2_squared':str(l2sq)})

result = {'passed':True,'exact_assertions':checks,'enumerated_path_cases':cases,
          'elapsed_seconds':round(time.perf_counter()-start,6),
          'max_reverse_density_residual':str(max_density_residual),
          'max_martingale_energy_residual':str(max_energy_residual),
          'periodic_stationary_one_step':{'uniform_ellipticity_lower_bound':'1/4',
             'iid':False,'density_values':list(map(str,one_step_density)),
             'static_phi_probability':'1/3','actual_phi_probability':str(one_step_mu[1]),
             'static_averaging_error_before':str(static_error),
             'density_weighted_error_after':str(corrected_error)},
          'random_M0_control':{'initial_uncertainty':str(initial_uncertainty),
             'p_times_1_minus_p':str(p*(1-p))},
          'compactness_control':compactness,
          'parent_problem_proved':False}
(ROOT/'CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
