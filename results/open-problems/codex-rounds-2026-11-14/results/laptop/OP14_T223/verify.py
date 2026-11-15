"""Bounded standard-library audit of PROOF.md; no network training.

Run with OMP_NUM_THREADS=1 and BelowNormal priority. The script checks
identities and quadratures, not a discretization used as proof.
"""
import ctypes
import json
import math
import os
import sys
import time
from fractions import Fraction as F
from pathlib import Path

os.environ['OMP_NUM_THREADS'] = '1'
if os.name == 'nt':
    ctypes.windll.kernel32.SetPriorityClass(
        ctypes.windll.kernel32.GetCurrentProcess(), 0x00004000)

START = time.monotonic()
OUT = Path(__file__).resolve().parent
checks = []


def check(name, value, expected, tolerance=0):
    error = abs(value - expected)
    assert error <= tolerance, (name, value, expected, error, tolerance)
    checks.append(dict(name=name, value=float(value), expected=float(expected),
                       absolute_error=float(error), tolerance=tolerance))


def simpson(fun, lo, hi, n=4000):
    assert n % 2 == 0
    h = (hi - lo) / n
    return h / 3 * (fun(lo) + fun(hi) + math.fsum(
        (4 if i % 2 else 2) * fun(lo + i * h) for i in range(1, n)))


def phi(z):
    return math.exp(-z * z / 2) / math.sqrt(2 * math.pi)


# Lane A: Cartesian conditional Gaussian integrals, integrating a analytically.
prob_sector = simpson(lambda w: phi(w) * math.erf(w / math.sqrt(2)), 0, 10)
q_sector = 2 * simpson(lambda w: phi(w) * (
    (w * w + 1) * math.erf(w / math.sqrt(2)) - 2 * w * phi(w)), 0, 10)
check('unconditional Gaussian probability of one cone sector', prob_sector, .25, 2e-11)
check('Cartesian q per conditioned sector', q_sector, 1., 2e-10)

# Lane B: radial integral and angular sector length, without Cartesian formula.
radial_q = simpson(lambda r: r ** 3 * math.exp(-r * r / 2), 0, 10)
q_polar = .5 * radial_q
check('polar q per conditioned sector', q_polar, 1., 2e-10)
check('agreement of independent Gaussian integral lanes', q_polar, q_sector, 2e-10)
check('Gaussian half-line input second moment', simpson(lambda x: x*x*phi(x), 0, 10), .5, 2e-10)

# Exact rational ensemble; q,m use original probability weights, not conditional.
particles = [(F(1, 5), F(1), F(2)),
             (F(3, 10), F(-1), F(3)),
             (F(1, 2), F(1, 2), F(1))]
m0 = sum(p*a*b for p,a,b in particles)
q0 = sum(p*(a*a+b*b) for p,a,b in particles)
check('rational ensemble total mass', sum(p for p,_,_ in particles), F(1))
C, S = F(5,4), F(3,4)  # cosh(log(2)), sinh(log(2))
transformed = [(p, C*a+S*b, S*a+C*b) for p,a,b in particles]
m_direct = sum(p*a*b for p,a,b in transformed)
q_direct = sum(p*(a*a+b*b) for p,a,b in transformed)
cosh2, sinh2 = C*C+S*S, 2*C*S
check('exact hyperbolic m identity', m_direct, m0*cosh2+q0*sinh2/2)
check('exact hyperbolic q identity', q_direct, q0*cosh2+2*m0*sinh2)
check('exact moment invariant', q_direct*q_direct-4*m_direct*m_direct, q0*q0-4*m0*m0)
for j, ((_,a,b), (_,at,bt)) in enumerate(zip(particles,transformed)):
    check('exact particle balance '+str(j), bt*bt-at*at, b*b-a*a)
    assert bt > abs(at)

# Independent differential lane: product rule on particles, not (9).
c = F(-7, 5)
e = m_direct-c
derivatives = [(p, -e*b/2, -e*a/2, a, b) for p,a,b in transformed]
mp = sum(p*(ap*b+a*bp) for p,ap,bp,a,b in derivatives)
qp = sum(p*(2*a*ap+2*b*bp) for p,ap,bp,a,b in derivatives)
check('exact moment ODE m', mp, -e*q_direct/2)
check('exact moment ODE q', qp, -2*e*m_direct)
check('exact differentiated moment invariant', 2*q_direct*qp-8*m_direct*mp, F(0))
rp = e*mp/2
speed2 = sum(p*(ap*ap+bp*bp) for p,ap,bp,_,_ in derivatives)
check('exact energy dissipation', -rp, speed2)

# Independent input lane: integrate the population residual, not the moment ODE.
ep, en = 1.25, -2.5
half_variance = simpson(lambda x: x*x*phi(x), 0, 10)
r_population = .5 * (ep*ep + en*en) * half_variance
check('population-risk factor one quarter', r_population, (ep*ep+en*en)/4, 2e-10)

# Root formula, q lower bound and L2 coupling bound on a fixed deterministic grid.
D = math.sqrt(float(q0*q0-4*m0*m0))


def moment(u):
    return float(m0)*math.cosh(2*u)+float(q0)/2*math.sinh(2*u)


def second(u):
    return float(q0)*math.cosh(2*u)+2*float(m0)*math.sinh(2*u)


max_root_error = max_coupling_excess = 0.
for target in [-10., -1., 0., 1., 10.]:
    star = (math.asinh(2*target/D)-math.asinh(2*float(m0)/D))/2
    max_root_error = max(max_root_error, abs(moment(star)-target))
    Q = max(float(q0), math.sqrt(D*D+4*target*target))
    for j in range(41):
        u = star*j/40
        assert second(u) >= D-1e-12
        # Finite-difference check of M'(u)=q(u), separately from product rule.
        h = 1e-5
        numerical = (moment(u+h)-moment(u-h))/(2*h)
        assert abs(numerical-second(u)) <= 1e-7*max(1,second(u))
        direct_cost = 0.
        for p,a,b in particles:
            at = math.cosh(u)*float(a)+math.sinh(u)*float(b)
            bt = math.sinh(u)*float(a)+math.cosh(u)*float(b)
            ast = math.cosh(star)*float(a)+math.sinh(star)*float(b)
            bst = math.sinh(star)*float(a)+math.cosh(star)*float(b)
            direct_cost += float(p)*((at-ast)**2+(bt-bst)**2)
        bound = Q*(u-star)**2
        max_coupling_excess = max(max_coupling_excess, direct_cost-bound)
        assert direct_cost <= bound+1e-11
check('maximum root residual on five signed targets', max_root_error, 0., 1e-12)
check('maximum positive coupling-bound excess', max(0,max_coupling_excess), 0., 1e-11)

# Adversarial omitted case: a full Gaussian contains a positive-mass open set
# near (a,b)=(2,1). Under a negative clock, b hits zero at u=-atanh(1/2).
hit_clock = -math.atanh(.5)
hit_b = math.sinh(hit_clock)*2+math.cosh(hit_clock)
hit_a = math.cosh(hit_clock)*2+math.sinh(hit_clock)
check('outside-cone finite-clock kink collision', hit_b, 0., 1e-14)
check('outside-cone surviving a at collision', hit_a, math.sqrt(3), 1e-14)

# Boundary case: balanced wrong-sign neuron has D=0, can stall at positive risk.
# For a=-b and target c>0, m=-b^2, q=2b^2, m'=b^2(b^2+c)>0;
# m approaches 0 from below, never reaches the positive teacher coefficient.
check('balanced single-neuron moment discriminant', F(2)**2-4*F(-1)**2, F(0))

result = {'status':'PASS', 'checks':checks,
          'notes': ['No ML training, GPU, torch, or external file writes.',
                    'Floating-point checks are audits, not substitutes for the proof.',
                    'Gaussian integration cutoffs are 10; analytic tails are negligible at these tolerances.'],
          'elapsed_seconds':time.monotonic()-START,
          'python_version':sys.version.split()[0], 'OMP_NUM_THREADS':os.environ['OMP_NUM_THREADS']}
if os.name == 'nt':
    from ctypes import wintypes

    class ProcessMemoryCounters(ctypes.Structure):
        _fields_ = [('cb', wintypes.DWORD), ('PageFaultCount', wintypes.DWORD)] + [
            (name, ctypes.c_size_t) for name in [
                'PeakWorkingSetSize', 'WorkingSetSize', 'QuotaPeakPagedPoolUsage',
                'QuotaPagedPoolUsage', 'QuotaPeakNonPagedPoolUsage',
                'QuotaNonPagedPoolUsage', 'PagefileUsage', 'PeakPagefileUsage']]

    kernel = ctypes.windll.kernel32
    kernel.GetCurrentProcess.restype = wintypes.HANDLE
    kernel.GetPriorityClass.argtypes = [wintypes.HANDLE]
    process_handle = kernel.GetCurrentProcess()
    priority = kernel.GetPriorityClass(process_handle)
    counters = ProcessMemoryCounters()
    counters.cb = ctypes.sizeof(counters)
    get_memory = ctypes.windll.psapi.GetProcessMemoryInfo
    get_memory.argtypes = [wintypes.HANDLE, ctypes.POINTER(ProcessMemoryCounters), wintypes.DWORD]
    assert get_memory(process_handle, ctypes.byref(counters), counters.cb)
    assert priority == 0x00004000
    assert counters.PeakWorkingSetSize < 1024**3
    assert counters.PeakPagefileUsage < 1024**3
    result['resources'] = {'priority_class':'BelowNormal',
                           'peak_working_set_bytes':counters.PeakWorkingSetSize,
                           'peak_commit_bytes':counters.PeakPagefileUsage}
(OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
lines = ['PASS: '+str(len(checks))+' identity/quadrature/adversarial checks.',
         'Cartesian conditioned-sector q = '+format(q_sector,'.15g'),
         'Polar conditioned-sector q = '+format(q_polar,'.15g'),
         'Maximum root residual = '+format(max_root_error,'.6g'),
         'Maximum positive coupling-bound excess = '+format(max(0,max_coupling_excess),'.6g'),
         'Outside-cone kink: u = '+format(hit_clock,'.15g')+', a = '+format(hit_a,'.15g'),
         'Data: verification.json']
summary='\n'.join(lines)+'\n'
(OUT/'verification_output.txt').write_text(summary,encoding='utf-8')
print(summary,end='')
