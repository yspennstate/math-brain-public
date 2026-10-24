"""Deterministic exact checks for C075; no random signs are used as proof."""
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
import json
import sympy as sp

ZERO = F(0)
ONE = F(1)
ROUND_DEN = 10**45


def conv(a, b):
    c = [ZERO] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def add(a, b):
    assert len(a) == len(b)
    return [x+y for x, y in zip(a, b)]


@lru_cache(None)
def pb(parameters):
    result = [ONE]
    for p in parameters:
        result = conv(result, [1-p, p])
    return tuple(result)


def law(parameters):
    return list(pb(tuple(sorted(parameters))))


def direct_jets(parameters, slopes):
    f, df, ddf = [ONE], [ZERO], [ZERO]
    for p, v in zip(parameters, slopes):
        factor = [1-p, p]
        tangent = [-v, v]
        f, df, ddf = (
            conv(f, factor),
            add(conv(df, factor), conv(f, tangent)),
            add(conv(ddf, factor), [2*x for x in conv(df, tangent)]),
        )
    return f, df, ddf


def gh(parameters, slopes):
    n = len(parameters)
    g, h = [ZERO]*n, [ZERO]*(n-1)
    for i in range(n):
        deleted = law(parameters[:i] + parameters[i+1:])
        for j, x in enumerate(deleted):
            g[j] += slopes[i]*x
        for ell in range(i+1, n):
            deleted2 = law([p for z, p in enumerate(parameters)
                            if z not in (i, ell)])
            for j, x in enumerate(deleted2):
                h[j] += 2*slopes[i]*slopes[ell]*x
    return g, h


def rounded(lo, hi):
    lscaled, hscaled = lo*ROUND_DEN, hi*ROUND_DEN
    return (F(lscaled.numerator//lscaled.denominator, ROUND_DEN),
            F(-((-hscaled.numerator)//hscaled.denominator), ROUND_DEN))


def small_log_bounds(x, terms=60):
    """For 1 <= x <= 2, exact positive atanh series and rational tail."""
    assert 1 <= x <= 2
    z = (x-1)/(x+1)
    z2 = z*z
    power = z
    total = ZERO
    for k in range(terms):
        total += 2*power/(2*k+1)
        power *= z2
    tail = 2*power/((2*terms+1)*(1-z2))
    return total, total+tail


LOG2 = small_log_bounds(F(2))


def scale_interval(v, bounds):
    lo, hi = bounds
    return (v*lo, v*hi) if v >= 0 else (v*hi, v*lo)


@lru_cache(None)
def log_bounds(x):
    assert x > 0
    if x == 1:
        return ZERO, ZERO
    exponent = 0
    y = x
    while y < 1:
        y *= 2
        exponent -= 1
    while y > 2:
        y /= 2
        exponent += 1
    lo, hi = small_log_bounds(y)
    elo, ehi = scale_interval(exponent, LOG2)
    return rounded(lo+elo, hi+ehi)


def log_expression(constant, terms):
    lo = hi = constant
    for argument, coefficient in terms:
        lterm, hterm = scale_interval(coefficient, log_bounds(argument))
        lo += lterm
        hi += hterm
    return rounded(lo, hi)


def interval_json(bounds):
    return {"lower": str(bounds[0]), "upper": str(bounds[1]),
            "midpoint_float": float((bounds[0]+bounds[1])/2)}


def check_count(parameters, slopes, label):
    n = len(parameters)
    f, df, ddf = direct_jets(parameters, slopes)
    assert f == law(parameters)
    g, h = gh(parameters, slopes)
    assert df == conv(g, [-ONE, ONE])
    assert ddf == conv(h, [ONE, -2*ONE, ONE])
    assert sum(f) == 1 and sum(df) == 0 and sum(ddf) == 0
    q = [f[j]/comb(n, j) for j in range(n+1)]
    fisher = sum((df[j]**2/f[j] for j in range(n+1)), ZERO)
    boundary = g[0]**2/f[1]+g[-1]**2/f[-2]
    quadratics = []
    ratios = []
    coefficient = [ZERO]*(n+1)
    local_intervals = []
    for j in range(n-1):
        assert q[j+1]**2 >= q[j]*q[j+2]
        assert f[j+1]**2 > f[j]*f[j+2]
        structural_left = h[j]*(f[j+1]**2-f[j]*f[j+2])
        structural_right = (2*g[j]*g[j+1]*f[j+1]
                            -g[j]**2*f[j+2]-g[j+1]**2*f[j])
        assert structural_left <= structural_right
        Q = (g[j]**2/f[j]-2*g[j]*g[j+1]/f[j+1]
             +g[j+1]**2/f[j+2])
        assert Q >= 0
        quadratics.append(Q)
        ratio = q[j]*q[j+2]/q[j+1]**2
        ratios.append(ratio)
        local_interval = log_expression(Q, [(ratio, h[j])])
        assert local_interval[0] >= 0, (label, j, local_interval)
        local_intervals.append(local_interval)
        coefficient[j] += h[j]
        coefficient[j+1] -= 2*h[j]
        coefficient[j+2] += h[j]
    assert fisher == boundary+sum(quadratics)
    assert coefficient == ddf  # equality of every formal log(q_j) coefficient
    negative_hessian = log_expression(fisher, list(zip(ratios, h)))
    assert negative_hessian[0] >= boundary
    return {
        "label": label, "n": n,
        "parameters": [str(x) for x in parameters],
        "slopes": [str(x) for x in slopes],
        "all_rational_identities": "PASS",
        "source_inequality_exact": "PASS",
        "local_weighted_sign_intervals": "PASS",
        "positive_h_j_count": sum(x > 0 for x in h),
        "negative_h_j_count": sum(x < 0 for x in h),
        "boundary_fisher_certificate": str(boundary),
        "negative_entropy_second_derivative": interval_json(negative_hessian),
    }


def rational(x):
    x = sp.simplify(x)
    assert x.is_Rational, x
    return F(int(x.p), int(x.q))


def sym(x):
    return sp.Rational(x.numerator, x.denominator)


def formal_hessian(p, jets):
    fisher = ZERO
    logs = {}
    for atom, (dp, ddp) in zip(p, jets):
        fisher += dp*dp/atom
        logs[atom] = logs.get(atom, ZERO)+ddp
    return fisher, {x: y for x, y in logs.items() if y}


def formal_sub(a, b, c):
    logs = dict(a[1])
    for part in (b, c):
        for x, coefficient in part[1].items():
            logs[x] = logs.get(x, ZERO)-coefficient
    return a[0]-b[0]-c[0], {x: y for x, y in logs.items() if y}


def check_hermitian(n, a, c, pure_imaginary=False):
    P = sp.ones(n)/n
    K = sym(a)*(sp.eye(n)-P)+sym(c)*P
    A = sp.zeros(n)
    if not pure_imaginary:
        for i in range(n):
            A[i, i] = sp.Rational(2*i-n+1, 7)+sp.Rational(1, 5)
    for i in range(n):
        for j in range(i+1, n):
            real = (0 if pure_imaginary else
                    sp.Rational((i+j)%3-1, 11)+sp.Rational(1, 17))
            imag = sp.Rational(2*i+j+1, 13)
            A[i, j] = real+sp.I*imag
            A[j, i] = real-sp.I*imag
    assert A == A.conjugate().T
    v = rational(sp.trace(P*A))
    u = rational((sp.trace(A)-sp.trace(P*A))/(n-1))
    A0 = sym(u)*(sp.eye(n)-P)+sym(v)*P
    Aperp = A-A0
    if not pure_imaginary:
        assert A0 != sp.zeros(n) and Aperp != sp.zeros(n)
    assert sp.trace(Aperp) == 0
    assert sp.simplify(sp.trace(P*Aperp)) == 0
    masses, cardinalities = [], []
    direction_jets = [[], [], []]
    for mask in range(1 << n):
        included = [(mask >> j) & 1 for j in range(n)]
        cardinalities.append(sum(included))
        Q = K-sp.diag(*[1-x for x in included])
        mass = rational((-1)**(n-sum(included))*Q.det())
        assert mass > 0
        masses.append(mass)
        inv = Q.inv()
        for dest, direction in zip(direction_jets, (A, A0, Aperp)):
            R = inv*direction
            tr = sp.trace(R)
            dfirst = rational(sym(mass)*tr)
            dsecond = rational(sym(mass)*(tr*tr-sp.trace(R*R)))
            dest.append((dfirst, dsecond))
    assert sum(masses) == 1
    for jets in direction_jets:
        assert sum(x[0] for x in jets) == 0
        assert sum(x[1] for x in jets) == 0
    forms = [formal_hessian(masses, j) for j in direction_jets]
    assert formal_sub(*forms) == (ZERO, {})
    f, df, ddf = direct_jets([a]*(n-1)+[c], [u]*(n-1)+[v])
    for j in range(n+1):
        indices = [i for i, sz in enumerate(cardinalities) if sz == j]
        assert sum(masses[i] for i in indices) == f[j]
        assert sum(direction_jets[1][i][0] for i in indices) == df[j]
        assert sum(direction_jets[1][i][1] for i in indices) == ddf[j]
    curvature_bounds = []
    if a == c:
        # Here log p(S)=|S| log a+(n-|S|) log(1-a). Check the
        # exact modular cancellation rather than treating these logs
        # as formally independent numbers.
        for (const, logs), jets in zip(forms, direction_jets):
            assert sum(sz*jet[1] for sz, jet in zip(cardinalities, jets)) == 0
            curvature_bounds.append((const, const))
    else:
        for const, logs in forms:
            curvature_bounds.append(log_expression(const, list(logs.items())))
    if a != c:
        assert curvature_bounds[0][0] > 0
        assert curvature_bounds[2][0] > 0
    elif pure_imaginary:
        assert curvature_bounds[0] == (ZERO, ZERO)
    return {
        "n": n, "a": str(a), "c": str(c),
        "direction": "pure imaginary Hermitian" if pure_imaginary
                     else "mixed complex Hermitian",
        "atom_jets_and_invariant_count_match": "PASS",
        "formal_cross_hessian_vanishes_exactly": "PASS",
        "negative_full_curvature": interval_json(curvature_bounds[0]),
        "negative_perpendicular_curvature": interval_json(curvature_bounds[2]),
    }


def main():
    results = {"proof_is_dimension_uniform": True,
               "count_checks": [], "hermitian_checks": []}
    for n in [2, 3, 4, 8, 20]:
        a, c = F(1, 4), F(3, 4)
        for u, v in [(1, 1), (1, -1), (1, -(n-1)),
                     (1, F(-1, 7)), (0, 1), (1, 0)]:
            u, v = F(u), F(v)
            record = check_count([a]*(n-1)+[c], [u]*(n-1)+[v],
                                 f"exchangeable n={n}, slopes=({u},{v})")
            assert F(record["boundary_fisher_certificate"]) > 0
            results["count_checks"].append(record)
    for n, a, c in [(4, F(1, 1000), F(99, 100)),
                    (5, F(2, 3), F(1, 6)),
                    (5, F(3, 7), F(3, 7))]:
        for u, v in [(F(1), F(-1, 3)), (F(1), F(-(n-1)))]:
            results["count_checks"].append(check_count(
                [a]*(n-1)+[c], [u]*(n-1)+[v], "boundary/complement/product"))
    for n in [3, 5, 8]:
        parameters = [F((3*i+2)%11+1, 13) for i in range(n)]
        slopes = [F((-1)**i*(i+1), 5) for i in range(n)]
        results["count_checks"].append(check_count(
            parameters, slopes, "general Bernoulli parameter vector"))
    for n, a, c in [(4, F(1, 4), F(3, 4)), (5, F(2, 3), F(1, 6))]:
        for pure in (False, True):
            results["hermitian_checks"].append(check_hermitian(n, a, c, pure))
    results["hermitian_checks"].append(
        check_hermitian(4, F(2, 5), F(2, 5), True))
    results["status"] = "PASS"
    path = Path(__file__).with_name("verification_results.json")
    path.write_text(json.dumps(results, indent=2)+"\n")
    print(f"PASS: {len(results['count_checks'])} deterministic count checks; "
          f"{len(results['hermitian_checks'])} exact Hermitian checks")
    print(path)


if __name__ == "__main__":
    main()
