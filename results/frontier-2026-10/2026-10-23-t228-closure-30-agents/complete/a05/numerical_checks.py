"""Sanity checks for A05's algebra; these do not replace the proofs."""
import json
import math
from pathlib import Path
import numpy as np

rng = np.random.default_rng(20261023)
checks = {}

# Gaussian scalar KL upper bound, with no small-relative-error assumption.
max_kl_ratio = 0.0
for _ in range(20000):
    s = 10.0 ** rng.uniform(-3, 3)
    v = s * 10.0 ** rng.uniform(0, 3)
    w = s * 10.0 ** rng.uniform(0, 3)
    dm = rng.normal() * math.sqrt(s)
    kl = 0.5 * (math.log(w/v) + v/w - 1 + dm*dm/w)
    upper = dm*dm/(2*s) + (v-w)**2/(4*s*s)
    assert kl <= upper + 1e-9 * max(1.0, upper)
    max_kl_ratio = max(max_kl_ratio, kl / upper if upper else 0.0)
checks['gaussian_kl_inequality'] = {'cases': 20000, 'max_ratio': max_kl_ratio}

# Tail second moment bound used in the unbounded-label bridge.
worst_tail_ratio = 0.0
for t in np.linspace(1.0, 300.0, 3000):
    a = math.sqrt(2*t)
    phi = math.exp(-t) / math.sqrt(2*math.pi)
    exact = 2*(a*phi + 0.5*math.erfc(a/math.sqrt(2)))
    upper = 3/math.sqrt(math.pi)*math.sqrt(t)*math.exp(-t)
    assert exact <= upper * (1+1e-12)
    worst_tail_ratio = max(worst_tail_ratio, exact/upper)
checks['gaussian_tail_moment'] = {'cases': 3000, 'max_ratio': worst_tail_ratio}

# Explicit t choice indeed bounds the report's full tail expression.
for _ in range(10000):
    n = int(rng.integers(1, 1000))
    s = 10.0 ** rng.uniform(-3, 3)
    k = 10.0 ** rng.uniform(-3, 3)
    eta = 10.0 ** rng.uniform(-10, 0)
    v0 = s+k
    c = n*(3*k/(s*math.sqrt(math.pi)) + 4*n*k*v0/s**2 + k*k/(2*s*s))
    t = max(1.0, 2*math.log(max(1.0, 2*c/(math.e*eta))))
    tail = n*math.exp(-t)*(3*k/(s*math.sqrt(math.pi))*math.sqrt(t)
                           + 4*n*k*v0/s**2*t + k*k/(2*s*s))
    assert tail <= eta*(1+1e-12)
checks['explicit_tail_threshold'] = {'cases': 10000}

# GP bounded-label posterior mean norm bound.
for _ in range(1000):
    n = int(rng.integers(1, 15))
    rank = int(rng.integers(1, 10))
    s = 10.0 ** rng.uniform(-2, 2)
    k = 10.0 ** rng.uniform(-2, 2)
    b = 10.0 ** rng.uniform(-2, 2)
    z = rng.normal(size=(n+1, rank))
    z *= math.sqrt(k) / np.maximum(np.linalg.norm(z, axis=1, keepdims=True), 1)
    g = z[:-1] @ z[:-1].T
    cross = z[:-1] @ z[-1]
    y = rng.uniform(-b, b, size=n)
    mean = cross @ np.linalg.solve(g+s*np.eye(n), y)
    assert abs(mean) <= b*math.sqrt(n*k/s)*(1+1e-12)
checks['bounded_context_mean'] = {'cases': 1000}

# Counterexample and its exact closed form.
s, eta, g = 1.0, 0.5, 0.1
alpha, c = 1-eta*(1+s), 1-eta*s/g
context, query = 0.0, 0.0
counterexample = []
for l in range(9):
    fixed = g/(1+s)
    coeff = g*(1-g)/(g*(1+s)-s)
    exact = fixed + coeff*c**l - eta/((1+s)*(c-alpha))*alpha**l
    assert abs(query-exact) <= 1e-10*max(1, abs(query))
    counterexample.append({'layer': l, 'context': context, 'query': query,
                           'exact_posterior_mean': fixed,
                           'raw_predictive_variance': 2-g*query})
    next_context = alpha*context+eta
    next_query = c*query+eta*(1-context)
    context, query = next_context, next_query
assert any(x['raw_predictive_variance'] < 0 for x in counterexample)
checks['query_normalization_counterexample'] = counterexample

# Chebyshev formula matches polynomial residual extrema.
for kappa in (1.01, 2, 10, 100, 10000):
    a = (kappa+1)/(kappa-1)
    rho = (math.sqrt(kappa)-1)/(math.sqrt(kappa)+1)
    for degree in (1, 2, 5, 10):
        exact = 1/math.cosh(degree*math.acosh(a))
        formula = 2*rho**degree/(1+rho**(2*degree))
        assert abs(exact-formula) <= 1e-12*max(1, exact)
checks['chebyshev_formula'] = {'cases': 25}

out = Path(__file__).with_name('numerical_checks.json')
out.write_text(json.dumps({'status': 'PASS', 'checks': checks}, indent=2)+'\n')
print(json.dumps({'status': 'PASS', 'algebra_cases': 34025, 'output': str(out)}))
