#!/usr/bin/env python3
"""C051: exact exchangeable-kernel Gibbs certificates and numerical illustrations.

Run from the campaign root. SymPy assertions are exact; mpmath values illustrate
the proved integral identities and are not used as universal sign evidence.
"""
import itertools
import json
from pathlib import Path

import mpmath as mp
import sympy as s

mp.mp.dps = 70
OUT = Path(__file__).resolve().parent


def atom(K, mask):
    n = K.rows
    absent = s.diag(*[0 if (mask >> j) & 1 else 1 for j in range(n)])
    return s.factor((-1) ** (n - mask.bit_count()) * (K - absent).det())


def numeric(x):
    return mp.mpf(str(s.N(x, 80)))


def entropy(p):
    return -mp.fsum(numeric(x) * mp.log(numeric(x)) for x in p if x)


# Exact exchangeable atom formula, tested in four and six measured coordinates.
records = {}
for n, a, lam in [(4, s.Rational(13, 30), s.Rational(3, 5)),
                  (6, s.Rational(1, 4), s.Rational(3, 4))]:
    b = (lam - a) / n
    c = a * (1 - lam)
    Kbar = a * s.eye(n) + b * s.ones(n)
    probs = [atom(Kbar, mask) for mask in range(1 << n)]
    for mask, p in enumerate(probs):
        k = mask.bit_count()
        formula = a**k * (1-a)**(n-k) * (c+b*k) / (a*(1-a))
        assert s.factor(p - formula) == 0
    assert sum(probs) == 1
    assert all(p > 0 for p in probs)
    records[f"exchangeable_n{n}"] = {
        "a": str(a), "lambda": str(lam), "b": str(b), "c": str(c),
        "atom_by_cardinality": [str(probs[(1 << k)-1]) for k in range(n+1)],
    }


# A connected complex four-site kernel, with a nonzero determinant-integral gap.
I = s.I
K = s.Matrix([[8, 1, 2+I, -I],
              [1, 11, -1+2*I, 1],
              [2-I, -1-2*I, 9, 2],
              [I, 1, 2, 10]]) / 20
n = 4
ones = s.ones(n, 1)
lam = (ones.T * K * ones)[0] / n
a = (s.trace(K)-lam)/(n-1)
b = (lam-a)/n
c = a*(1-lam)
assert (a, lam, b, c) == (s.Rational(13,30), s.Rational(3,5),
                         s.Rational(1,24), s.Rational(13,75))
Kbar = a*s.eye(n)+b*s.ones(n)
permutation_average = s.zeros(n)
for perm in itertools.permutations(range(n)):
    permutation_average += K.extract(perm, perm)
permutation_average /= s.factorial(n)
assert permutation_average == Kbar

# Strictness certified by all leading principal minors of K and I-K.
leading_K = [s.factor(K[:j,:j].det()) for j in range(1,n+1)]
leading_IK = [s.factor((s.eye(n)-K)[:j,:j].det()) for j in range(1,n+1)]
assert all(x > 0 for x in leading_K+leading_IK)
p = [atom(K, mask) for mask in range(1 << n)]
q = [atom(Kbar, mask) for mask in range(1 << n)]
assert sum(p) == sum(q) == 1
assert all(x > 0 for x in p+q)

eta = s.symbols("eta", real=True)
det_K = s.factor((s.eye(n)-eta*K).det())
det_bar = s.factor((s.eye(n)-eta*Kbar).det())
det_difference = s.factor(det_bar-det_K)
assert s.Poly(det_difference, eta).coeff_monomial(eta) == 0
delta_norm_sq = s.factor(s.trace((K-Kbar)**2))
assert s.Poly(det_difference,eta).coeff_monomial(eta**2) == delta_norm_sq/2

kl = mp.fsum(numeric(x)*mp.log(numeric(x/y)) for x,y in zip(p,q))
cross_gap = mp.fsum(numeric(x-y)*mp.log(numeric(y)) for x,y in zip(p,q))
det_fun = s.lambdify(eta, det_difference, "mpmath")
ratio = numeric(c/b)
def integrand(x):
    if x == 0 or x == 1:
        return mp.mpf(0)
    return (1-x)**(ratio-1)*det_fun(x)/(-mp.log1p(-x))
integral = mp.quad(integrand, [0, mp.mpf('.25'), mp.mpf('.5'), mp.mpf('.75'), 1])
gap = entropy(q)-entropy(p)
assert abs(cross_gap-integral) < mp.mpf('1e-60')
assert abs(gap-kl-integral) < mp.mpf('1e-60')
assert atom(s.eye(n)-K, 3) == atom(K, (1 << n)-1-3)
records["complex_four_site"] = {
    "leading_principal_minors_K": list(map(str,leading_K)),
    "leading_principal_minors_I_minus_K": list(map(str,leading_IK)),
    "K": [[str(z) for z in row] for row in K.tolist()],
    "Kbar": [[str(z) for z in row] for row in Kbar.tolist()],
    "determinant_difference": str(det_difference),
    "delta_frobenius_squared": str(delta_norm_sq),
    "entropy_gap": mp.nstr(gap,50),
    "KL_gap": mp.nstr(kl,50),
    "determinant_integral_gap": mp.nstr(integral,50),
    "identity_error": mp.nstr(abs(gap-kl-integral),8),
}


# Six-site full-rank phase direction: exact atom jets and cardinality curvature.
n = 6
a, lam = s.Rational(1,4), s.Rational(3,4)
b, c = (lam-a)/n, a*(1-lam)
Kbar = a*s.eye(n)+b*s.ones(n)
J = s.Matrix([[0,I],[-I,0]])
A = s.diag(J,J,J)
assert A*A == s.eye(n)
assert s.trace(A) == 0
assert (s.ones(1,n)*A*s.ones(n,1))[0] == 0
assert A.det() == -1
assert s.trace(A*A) == 6
p, g, h = [], [], []
for mask in range(1 << n):
    absent = s.diag(*[0 if (mask >> j) & 1 else 1 for j in range(n)])
    Q = Kbar-absent
    prob = (-1)**(n-mask.bit_count())*Q.det()
    R = Q.inv()*A
    first = s.factor(prob*s.trace(R))
    second = s.factor(prob*(s.trace(R)**2-s.trace(R*R)))
    p.append(prob); g.append(first); h.append(second)
assert sum(p) == 1 and sum(g) == sum(h) == 0
assert all(x == 0 for x in g)

z = s.symbols("z")
count_second_from_atoms = s.expand(sum(h[mask]*z**mask.bit_count() for mask in range(1<<n)))
count_second_formula = -(z-1)**2 * (
    2*(1-a+a*z)**4 + 4*(1-lam+lam*z)*(1-a+a*z)**3)
assert s.expand(count_second_from_atoms-count_second_formula) == 0
curvature = -mp.fsum(numeric(x)*mp.log(numeric(y)) for x,y in zip(h,p))
f = lambda k: mp.log(numeric(c+b*k))
expected_first = mp.fsum(numeric(s.binomial(4,j)*a**j*(1-a)**(4-j)) *
                        (f(j+2)-2*f(j+1)+f(j)) for j in range(5))
expected_second = mp.mpf(0)
for bit in [0,1]:
    for j in range(4):
        weight = lam**bit*(1-lam)**(1-bit)*s.binomial(3,j)*a**j*(1-a)**(3-j)
        k = bit+j
        expected_second += numeric(weight)*(f(k+2)-2*f(k+1)+f(k))
assert abs(curvature-(2*expected_first+4*expected_second)) < mp.mpf('1e-60')
kappa = mp.log(mp.mpf(529)/513)
assert curvature <= -6*kappa

# Exact rational constants for a uniform concave interval about the base.
radius = s.Rational(1,20_000_000)
third_derivative_bound = s.Integer(2988)*512
gap_lower = s.Rational(96,529)
assert radius < s.Rational(1,8)
assert radius*third_derivative_bound < gap_lower/2
records["six_site_full_rank_direction"] = {
    "rank": int(A.rank()),
    "atom_first_derivatives_all_zero": True,
    "count_second_derivative": str(s.factor(count_second_from_atoms)),
    "entropy_second_derivative": mp.nstr(curvature,50),
    "uniform_center_gap_at_least": "6*log(529/513)",
    "rational_center_gap_at_least": str(gap_lower),
    "uniform_concavity_interval": f"abs(t) <= {radius}",
    "uniform_entropy_second_derivative_upper_bound": "-48/529",
    "third_derivative_absolute_bound": str(third_derivative_bound),
}


# Concrete failure of either measured-Gaussian extremality at fixed covariance.
c = s.Rational(1,8)
K2 = s.Matrix([[s.Rational(1,2),c],[c,s.Rational(1,2)]])
pg = [atom(K2,mask) for mask in range(4)]
uniform = [s.Rational(1,4)]*4
lower = [s.Rational(3,8),s.Rational(1,8),s.Rational(1,8),s.Rational(3,8)]
def state(diagonal):
    rho = s.diag(*diagonal)
    rho[1,2] = rho[2,1] = c
    return rho
for diagonal in [pg,uniform,lower]:
    rho = state(diagonal)
    assert s.trace(rho) == 1
    assert all(e >= 0 for e in rho.eigenvals())
    assert diagonal[1]+diagonal[3] == diagonal[2]+diagonal[3] == s.Rational(1,2)
records["fixed_covariance_extremality_obstruction"] = {
    "gaussian_diagonal": list(map(str,pg)),
    "higher_entropy_diagonal": list(map(str,uniform)),
    "lower_entropy_diagonal": list(map(str,lower)),
    "entropies_lower_gaussian_upper": [mp.nstr(entropy(x),40) for x in [lower,pg,uniform]],
}

result = {"status": "all exact assertions passed", "records": records}
(OUT / "results.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
