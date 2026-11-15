"""Independent finite checks for PROOF.md; no diffusion simulation.
Run: OMP_NUM_THREADS=1 nice -n 15 python3 audit_stationarity.py
"""
import math
import os
import resource
import sys
import time

started = time.monotonic()
assert os.environ.get('OMP_NUM_THREADS') == '1'
print('nice', os.getpriority(os.PRIO_PROCESS, 0))

def kappa(j):
    return math.pi**(j/2) / math.gamma(1+j/2)

def simpson(f, a, b, n=2048):
    h = (b-a)/n
    return h/3 * (f(a)+f(b)+sum((4 if k%2 else 2)*f(a+k*h)
                               for k in range(1,n)))

# Projection proof versus angular integration, using independently normalized
# sphere areas via the gamma function.
flux_error = 0.0
for d in range(2,10):
    projection = kappa(d-1)/(d*kappa(d))
    area_ratio = math.gamma(d/2)/(math.sqrt(math.pi)*math.gamma((d-1)/2))
    angular = area_ratio * simpson(
        lambda a: math.cos(a)*math.sin(a)**(d-2),0,math.pi/2)
    err = abs(projection-angular)
    flux_error = max(flux_error,err)
    assert err < 2e-11, (d,projection,angular)
    if d == 2: assert math.isclose(projection,1/math.pi,rel_tol=1e-14)
    if d == 3: assert math.isclose(projection,1/4,rel_tol=1e-14)
print('c_d: projection vs angular integration d=2..9 max absolute error %.3g' % flux_error)
print('c_2=1/pi; c_3=1/4')

# One-hit phase-tube Jacobian by coordinate determinant. Coordinates (phi,theta,s)
# map to (x1,x2,theta), with y=r(cos(phi),sin(phi)), x=y-s*w(theta).
# The theta column drops out after expanding the 3x3 determinant on its last row.
max_jac_error = 0.0
for r in (0.2,1.0,3.0):
    for phi in (-1.3,0.0,0.8):
        for delta in (2.0,2.6,3.1):
            theta=phi+delta
            column_phi=(-r*math.sin(phi),r*math.cos(phi))
            column_s=(-math.cos(theta),-math.sin(theta))
            det=abs(column_phi[0]*column_s[1]-column_s[0]*column_phi[1])
            flux=r*abs(math.cos(theta-phi))
            reflected=2*phi+math.pi-theta
            max_jac_error=max(max_jac_error,abs(det-flux))
            assert math.isclose(det,flux,rel_tol=1e-13,abs_tol=1e-14)
            assert math.isclose(abs(math.cos(reflected-phi)),
                                abs(math.cos(theta-phi)),rel_tol=1e-13)
            # (phi,theta)->(phi,2phi+pi-theta) has determinant -1.
            assert 1*(-1)-0*2 == -1
print('tube determinant and reflection flux max absolute error %.3g' % max_jac_error)

# Shell volume: direct powers, odd binomial terms, and face-slab upper bound.
shell_error=0.0
for d in range(2,10):
    for ratio in (0.5,0.1,0.01,0.001):
        powers=(1+ratio)**d-(1-ratio)**d
        odd=2*sum(math.comb(d,k)*ratio**k for k in range(1,d+1,2))
        strips=2*d*ratio*(1+ratio)**(d-1)
        shell_error=max(shell_error,abs(powers-odd))
        assert math.isclose(powers,odd,rel_tol=2e-12,abs_tol=2e-14)
        assert odd <= strips*(1+1e-14)
for d in (2,3,5):
    z=1e-6
    leading=2*sum(math.comb(d,k)*z**k for k in range(1,d+1,2))/z
    assert math.isclose(leading,2*d,rel_tol=5e-12)
print('shell: powers vs binomial max absolute error %.3g; slab bound PASS' % shell_error)
print('normalized shell / (|t|/R) -> 2d')

# Check both correlation factors independently. The double-square midpoint sum
# is grouped by time difference, including its discrete diagonal. This is a
# consistency example C(s)=exp(-gamma*s), not a claim about the Lorentz gas.
max_corr_error=0.0
for t,gamma in ((0.7,0.0),(1.0,0.3),(3.0,2.0)):
    n=4096
    h=t/n
    square=h*h*(n+2*sum((n-k)*math.exp(-gamma*k*h) for k in range(1,n)))
    triangular=2*simpson(lambda s:(t-s)*math.exp(-gamma*s),0,t)
    exact=t*t if gamma == 0 else 2*(t/gamma+math.expm1(-gamma*t)/(gamma*gamma))
    assert math.isclose(triangular,exact,rel_tol=2e-11)
    err=abs(square-exact)/max(1,abs(exact))
    max_corr_error=max(max_corr_error,err)
    assert err < 5e-7, (t,gamma,err)
    for d in (2,3,7):
        diagonal=triangular/d
        assert math.isclose(d*diagonal,exact,rel_tol=2e-11)
print('correlation identity: full square vs triangle vs closed form max relative error %.3g' % max_corr_error)
print('C=1 gives E|X_t|^2=t^2; per-coordinate factor is 1/d')

# Recheck earlier leading rate by radius-one dimensional rescaling.
for d in range(2,8):
    lam,r=0.23,0.7
    shadow=d/(lam*kappa(d-1)*r**(d-1))
    rescaled=r*d/(lam*r**d*kappa(d-1))
    assert math.isclose(shadow,rescaled,rel_tol=1e-14)
print('earlier d/a coefficient: shadow and radius-one rescaling agree d=2..7')

rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if sys.platform != 'darwin': rss*=1024
assert rss < 1024**3
print('peak resident bytes',rss)
print('PASS; elapsed %.3f seconds' % (time.monotonic()-started))
