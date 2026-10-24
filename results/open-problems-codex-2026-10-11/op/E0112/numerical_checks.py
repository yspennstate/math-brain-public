"""Deterministic quadrature checks; these are not critical-point estimates."""
from pathlib import Path
import json, math
import scipy.integrate as si

gamma = 4 * math.pi / 3
K = 8 * math.pi / 15

def v(h):
    return math.pi * (4 + h) * (2 - h) ** 2 / 12 if 0 <= h <= 2 else 0

def ev(s):
    if s <= 1e-12:
        return gamma
    # D_s ~ N(0, 2s I_3). The rescaling avoids a narrow peak near s=0.
    top = min(2 / math.sqrt(s), 24)
    value, err = si.quad(
        lambda z: 4 * math.pi * z*z * (4*math.pi)**(-1.5)
        * math.exp(-z*z/4) * v(math.sqrt(s)*z),
        0, top, epsabs=1e-10, epsrel=1e-9,
    )
    return value

green, green_error = si.quad(lambda h: h*v(h), 0, 2, epsabs=1e-12)
rows=[]
for t in [0.1, 1, 10, 100, 1000]:
    free, ef = si.quad(ev, 0, t, epsabs=1e-8, epsrel=1e-8, limit=200)
    bridge, eb = si.quad(lambda s: 2*ev(s*(1-s/t)), 0, t/2,
                         epsabs=1e-8, epsrel=1e-8, limit=200)
    rows.append(dict(t=t,free_occupation=free,bridge_occupation=bridge,
                     free_error=ef,bridge_error=eb))

# Finite exchangeable fields show that Jensen alone admits no reverse
# bound with a positive constant uniform over the number of cells.
controls=[dict(N=n,point_to_level=1.0,point_to_point_halfmoment=1/math.sqrt(n))
          for n in [1,4,100,10000]]
out=dict(model='d=3, R=1, difference generator Delta',
         K_formula=K,K_radial_integral=green,K_quadrature_error=green_error,
         occupation=rows,Jensen_negative_control=controls,
         limitations='Quadrature is numerical evidence only. Exchangeable controls are not Poisson polymers.')
assert abs(green-K)<1e-10
assert all(z['free_occupation']<=K+1e-8 for z in rows)
Path('numerical_results.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
