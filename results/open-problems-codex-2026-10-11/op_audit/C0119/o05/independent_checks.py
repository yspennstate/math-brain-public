"""Independent finite-volume checks; no claimant code is imported."""
import json
from pathlib import Path
import numpy as np

rng = np.random.default_rng(2026101205119)
beta = 4.0
N = 200000
# n=2, spatial d=3: one common origin and six independent terminal sites.
X = rng.normal(size=(N, 7))
Y = rng.normal(size=(N, 7))

def observable(x, ground=False):
    if ground:
        p = np.zeros_like(x)
        p[:, 0] = 1
        p[np.arange(len(x)), 1 + np.argmax(x[:, 1:], axis=1)] = 1
        return x[:, 0] + np.max(x[:, 1:], axis=1), p
    a = beta * x[:, 1:]
    top = a.max(axis=1)
    w = np.exp(a - top[:, None])
    den = w.sum(axis=1)
    p = np.column_stack((np.ones(len(x)), w / den[:, None]))
    return x[:, 0] + (top + np.log(den)) / beta, p

out = {'seed': 2026101205119, 'samples': N, 'n': 2, 'd': 3, 'beta': beta}
for ground in [False, True]:
    f, p = observable(X, ground)
    rho = rng.uniform(size=N)
    z = rho[:, None] * X + np.sqrt(1 - rho**2)[:, None] * Y
    _, pz = observable(z, ground)
    integrand = np.sum(p * pz, axis=1)
    f2 = (f - f.mean())**2
    residual = f2 - integrand
    values = []
    for t in [0, .01, .1, .5, 2, 10]:
        _, pt = observable(np.exp(-t)*X + np.sqrt(1-np.exp(-2*t))*Y, ground)
        q = np.sum(p * pt, axis=1)
        values.append({'t': t, 'mean_overlap': float(q.mean()), 'se': float(q.std(ddof=1)/np.sqrt(N))})
    result = {'variance': float(f.var(ddof=1)), 'overlap_integral': float(integrand.mean()),
              'identity_residual': float(residual.mean()),
              'residual_se': float(residual.std(ddof=1)/np.sqrt(N)), 'overlap_curve': values}
    if not ground:
        U = np.sum(X*p, axis=1)
        ibp = U - beta*(2 - np.sum(p*p, axis=1))
        result['ibp_residual'] = float(ibp.mean())
        result['ibp_se'] = float(ibp.std(ddof=1)/np.sqrt(N))
        result['baseline_bound'] = float(2*(1-np.sqrt(2*np.log(6))/beta))
        result['mean_same_environment_overlap'] = float(np.sum(p*p,axis=1).mean())
    out['ground' if ground else 'finite_temperature'] = result

# Coordinatewise finite differences for free energies and occupancy derivatives.
x = rng.normal(size=(1,7))
g, p = observable(x)
h = 1e-5
gradient_errors, hessian_diagonal_errors = [], []
for j in range(7):
    xp, xm = x.copy(), x.copy()
    xp[0,j] += h
    xm[0,j] -= h
    gp, pp = observable(xp)
    gm, pm = observable(xm)
    gradient_errors.append(abs(float((gp-gm)[0]/(2*h)-p[0,j])))
    hessian_diagonal_errors.append(abs(float((pp-pm)[0,j]/(2*h)-beta*p[0,j]*(1-p[0,j]))))
out['max_gradient_error'] = max(gradient_errors)
out['max_occupancy_derivative_error'] = max(hessian_diagonal_errors)

# Exact finite-family indexing checks, independently enumerated.
from itertools import product
directions = [tuple(sign if j==axis else 0 for j in range(3)) for axis in range(3) for sign in [-1,1]]
def path(steps):
    pos=(0,0,0)
    vertices=[pos]
    for s in steps:
        pos=tuple(a+b for a,b in zip(pos,s))
        vertices.append(pos)
    return tuple(vertices)
weighted=[path(s) for s in product(directions,repeat=2)]
full=[path(s) for s in product(directions,repeat=3)]
sites={(i,v) for p in weighted for i,v in enumerate(p)}
weights={j:float(rng.normal()) for j in sorted(sites)}
z_ours=sum(np.exp(beta*sum(weights[(i,v)] for i,v in enumerate(p))) for p in weighted)
z_paper=sum(np.exp(beta*sum(weights[(i,v)] for i,v in enumerate(p[:-1]))) for p in full)
out['terminal_unweighted_factor'] = float(z_paper/z_ours)
positive_dirs=[(1,0,0),(0,1,0),(0,0,1)]
positive_paths=[path(s) for s in product(positive_dirs,repeat=3)]
positive_sites={v for p in positive_paths for v in p}
positive_weights={v:float(rng.normal()) for v in sorted(positive_sites)}
m=max(sum(positive_weights[v] for v in p) for p in positive_paths)
t=max(sum(positive_weights[v] for v in p[1:]) for p in positive_paths)
out['origin_decomposition_error']=abs(m-positive_weights[(0,0,0)]-t)
out['positive_path_incidence_distinct']=len({frozenset(p) for p in positive_paths})==len(positive_paths)
Path('independent_results.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
