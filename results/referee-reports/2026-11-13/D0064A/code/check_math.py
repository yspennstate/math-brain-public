"""Independent numerical checks of normalization and constants used in REPORT.md."""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS']:
    os.environ[k]='1'
import json, math, pathlib
import numpy as np
from scipy.integrate import quad
ROOT=pathlib.Path(__file__).resolve().parents[1]
assert os.getpriority(os.PRIO_PROCESS,0)>=10
ln2=math.log(2);nodes,weights=np.polynomial.hermite.hermgauss(80)
checks=[]
for alpha in [1.,.6]:
    for gamma2 in [.5,2.]:
        logt=(math.sqrt(gamma2)*math.sqrt(2*ln2)*nodes-(1+gamma2/2)*ln2)/alpha
        def m(q):return float(2*np.sum(weights*np.exp(q*logt))/math.sqrt(math.pi))
        analytic_derivative=ln2*(gamma2/2-1)/alpha
        h=1e-5;derivative=(m(alpha+h)-m(alpha-h))/(2*h)
        checks.append(dict(alpha=alpha,gamma2=gamma2,m_alpha_quadrature=m(alpha),
            mprime_quadrature=derivative,mprime_formula=analytic_derivative))
        assert abs(m(alpha)-1)<1e-12
        assert abs(derivative-analytic_derivative)<2e-8
alpha=.6
levy=[]
for q in [.25,1,4]:
    # Integrate over log z; combined tails below -45 and above 55 are <2e-7 for these q.
    f=lambda u:-math.expm1(-q*math.exp(u))*math.exp(-alpha*u)
    val=quad(f,-45,55,epsabs=1e-9)[0]
    exact=math.gamma(1-alpha)/alpha*q**alpha
    levy.append(dict(q=q,quadrature=val,formula=exact,error=val-exact))
    assert abs(val-exact)<2e-7
# Independent alpha=1/2 sampler: S=1/(2G^2) has Laplace exp(-sqrt(q)).
rng=np.random.default_rng(71264);s=1/(2*rng.normal(size=200000)**2)
half=[]
for q in [.25,1,4]:
    y=np.exp(-q*s);se=float(y.std(ddof=1)/math.sqrt(len(y)));mean=float(y.mean())
    half.append(dict(q=q,empirical=mean,exact=math.exp(-math.sqrt(q)),se=se))
    assert abs(mean-math.exp(-math.sqrt(q)))<5*se
# Explicit Gaussian first-generation Monte Carlo, independent of tree simulation.
root=[]
for alpha in [1,.6]:
    for gamma2 in [.5,2]:
        x=rng.normal(0,math.sqrt(ln2),(100000,2))
        t=np.exp((math.sqrt(gamma2)*x-(1+gamma2/2)*ln2)/alpha)
        mass=(t**alpha).sum(axis=1)
        mean=float(mass.mean());se=float(mass.std(ddof=1)/math.sqrt(len(mass)))
        root.append(dict(alpha=alpha,gamma2=gamma2,mean_sum_Talpha=mean,se=se))
        assert abs(mean-1)<5*se
out=dict(normalization=checks,levy_constant=levy,independent_half_stable=half,first_generation=root,
    all_checks_passed=True,nice=os.getpriority(os.PRIO_PROCESS,0))
(ROOT/'data'/'math_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
