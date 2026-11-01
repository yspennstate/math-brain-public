"""Exact certificates for C063. Run from the campaign root with Python/SymPy."""

from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial
from pathlib import Path
import json

import sympy as s


def rat(x):
    x = s.cancel(x)
    assert x.is_Rational, x
    return F(int(x.p), int(x.q))


def enc(x):
    if isinstance(x, F):
        return f"{x.numerator}/{x.denominator}"
    if isinstance(x, s.MatrixBase):
        return [[str(y) for y in row] for row in x.tolist()]
    if isinstance(x, dict):
        return {str(k): enc(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [enc(y) for y in x]
    return x


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(c, a):
    return (c*a[0], c*a[1]) if c >= 0 else (c*a[1], c*a[0])


def log_unit(x, terms=48):
    assert F(1) <= x <= F(2)
    z = (x-1)/(x+1)
    lo = 2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    tail = 2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    return lo, lo+tail


@lru_cache(None)
def log_interval(x):
    assert x > 0
    power = 0
    while x < 1:
        x *= 2
        power -= 1
    while x >= 2:
        x /= 2
        power += 1
    lo, hi = add(log_unit(x), scale(F(power), log_unit(F(2))))
    # Outward rational rounding keeps certificates small without a float step.
    denominator = 10**40
    lower = lo.numerator*denominator//lo.denominator
    upper = -((-hi.numerator*denominator)//hi.denominator)
    return F(lower, denominator), F(upper, denominator)


def log_sum(coefficients, arguments):
    out = (F(0), F(0))
    for c, a in zip(coefficients, arguments):
        out = add(out, scale(c, log_interval(a)))
    return out


def display(interval):
    return [float(interval[0]), float(interval[1])]


def norm2(A):
    return rat(s.trace(A*A.conjugate().T))


def main():
    n = 6
    theta = F(63, 64)
    M = 10000
    x = s.Matrix([M+1, M-1, M, M, M, M])
    D = rat((x.T*x)[0])
    P = x*x.T/s.Rational(D.numerator, D.denominator)
    Q = s.eye(n)-P
    K = s.eye(n)/2+s.Rational(theta.numerator, 2*theta.denominator)*P
    eps = max(abs(n*rat(P[i, i])-1) for i in range(n))
    d = 4*theta*theta/(n+(n-2)*theta)**2
    assert d == F(441, 11236)
    assert eps <= d/F(16*(n-1))
    assert eps < F(1, 2)
    assert theta == 1-F(1, 2**n)
    assert (1+theta)/(1-theta) == 127
    assert rat(s.trace(K)) == F(n, 2)+theta/2
    assert K != s.eye(n)/2+s.Rational(theta.numerator, 2*n*theta.denominator)*s.ones(n)
    r = F(n)*(1-theta)/(2*theta)
    assert r == F(1, 21)
    var = (n-theta*theta)/4
    mu = F(n, 2)+theta/2

    # Exact finite-difference coefficient vectors for beta and gamma.
    beta_dist = [F(0) for _ in range(n-1)]
    b = (1+theta)/2
    for k in range(n-2):
        mass = F(comb(n-3, k), 2**(n-3))
        beta_dist[k] += (1-b)*mass
        beta_dist[k+1] += b*mass
    gamma_dist = [F(comb(n-2, k), 2**(n-2)) for k in range(n-1)]
    def diff_coeff(dist):
        out = [F(0) for _ in range(n+1)]
        for k, mass in enumerate(dist):
            out[k] += mass
            out[k+1] -= 2*mass
            out[k+2] += mass
        return out
    bc = diff_coeff(beta_dist)
    gc = diff_coeff(gamma_dist)
    flat = [F(1, 2**n)*(1+theta*F(2*k-n, n)) for k in range(n+1)]
    beta = log_sum([-c for c in bc], flat)
    gamma = log_sum([-c for c in gc], flat)
    assert beta[0] > d
    assert gamma[0] > beta[1]
    h = scale(F(1, 2), add(beta, gamma))
    assert var*h[1] < F(253, 320)
    assert log_interval(F(2))[1] < F(25, 36)
    assert F(2, 5)+F(25, 64) == F(253, 320)

    # The nonflat log residual and the complete signed atom matrices.
    atoms = []
    residuals = []
    for mask in range(2**n):
        sign = [1 if mask >> i & 1 else -1 for i in range(n)]
        k = mask.bit_count()
        E = s.diag(*sign)
        w = sum((rat(P[i, i]) for i in range(n) if sign[i] == 1), F(0))
        factor = 1+theta*(2*w-1)
        p = F(1, 2**n)*factor
        R = 2*E-s.Rational(2*theta/factor/D)*(E*x)*(x.T*E)
        atom_matrix = K-s.diag(*[0 if t == 1 else 1 for t in sign])
        assert atom_matrix*R == s.eye(n)
        assert rat((-1)**(n-k)*atom_matrix.det()) == p
        residuals.append(log_interval(flat[k]/p))
        atoms.append((mask, k, p, R))
    assert sum((p for _, _, p, _ in atoms), F(0)) == 1
    osc_bound = log_interval((1+eps)/(1-eps))
    residual_min = min(lo for lo, hi in residuals)
    residual_max = max(hi for lo, hi in residuals)
    assert residual_max-residual_min <= osc_bound[1]
    assert 2*(n-1)*osc_bound[1] < d/2
    assert 8*(n-1)*eps <= d/2

    w = s.Matrix([1, -1, 0, 0, 0, 0])
    dangerous = s.eye(n)-s.Rational(3, 4)*(w*w.T)
    assert norm2(dangerous) == F(21, 4)
    assert dangerous.det() == -s.Rational(1, 2)
    assert dangerous.eigenvals() == {-s.Rational(1, 2): 1, s.Integer(1): 5}
    commutator = K*dangerous-dangerous*K
    assert rat(commutator[0, 2]) == 3*theta*M/(4*D) > 0
    imaginary = s.zeros(n)
    for i in range(0, n, 2):
        imaginary[i, i+1] = s.I
        imaginary[i+1, i] = -s.I
    dense = s.diag(1, -2, 3, -1, 2, -3)
    for i in range(n):
        for j in range(i+1, n):
            dense[i, j] = s.Rational((-1)**(i+j)*(i+1), 7)+s.I*s.Rational(j-i, 11)
            dense[j, i] = s.conjugate(dense[i, j])
    directions = {"full_rank_inertia_5_1": dangerous,
                  "full_rank_pure_imaginary": imaginary,
                  "dense_mixed_complex": dense}
    results = {}
    for name, A in directions.items():
        assert A == A.conjugate().T
        u = rat(s.trace(P*A))
        y = rat(s.trace(Q*A))
        t = rat(s.trace(A))
        assert t == u+y
        Bnorm = norm2(Q*A*Q)
        vnorm = norm2(Q*A*P)
        Anorm = norm2(A)
        assert Anorm == u*u+Bnorm+2*vnorm
        pc = [F(0) for _ in range(n+1)]
        qc = [F(0) for _ in range(n+1)]
        rc = [F(0) for _ in range(n+1)]
        jet = []
        fisher = F(0)
        for mask, k, p, R in atoms:
            score = rat(s.trace(R*A))
            second = score*score-rat(s.trace(R*A*R*A))
            q, acc = p*score, p*second
            pc[k] += p
            qc[k] += q
            rc[k] += acc
            fisher += q*q/p
            jet.append((mask, p, q, acc))
        assert sum(qc) == sum(rc) == 0
        assert sum(k*qc[k] for k in range(n+1)) == t
        assert sum(k*rc[k] for k in range(n+1)) == 0
        assert sum((F(k)-mu)**2*pc[k] for k in range(n+1)) == var
        assert all(pc[k] == comb(n, k)*flat[k] for k in range(n+1))
        count_fisher = sum(qc[k]**2/pc[k] for k in range(n+1))
        within_count = fisher-count_fisher
        count_residual = count_fisher-t*t/var
        assert within_count >= 0 and count_residual >= 0
        if name == "full_rank_pure_imaginary":
            assert fisher == 0
        # Exact equality of every frozen cardinality-log coefficient.
        first_coeff = y*y-Bnorm
        second_coeff = 2*(u*y-vnorm)
        predicted = [first_coeff*bc[k]+second_coeff*gc[k] for k in range(n+1)]
        assert rc == predicted
        # Exact complete-square coefficients of beta and gamma.
        beta_square = t*t/2-Anorm+(u-y)**2/2+2*vnorm
        gamma_square = t*t/2-(u-y)**2/2-2*vnorm
        assert beta_square == first_coeff and gamma_square == second_coeff
        actual_frozen = log_sum([-j[3] for j in jet], [j[1] for j in jet])
        count_frozen = log_sum([-c for c in rc], flat)
        residual_frozen = add(actual_frozen, scale(F(-1), count_frozen))
        hessian_negative = add((fisher, fisher), scale(F(-1), actual_frozen))
        certified_bound = F(67, 320)*fisher+(d/2)*Anorm
        assert hessian_negative[0] > certified_bound
        assert max(abs(residual_frozen[0]), abs(residual_frozen[1])) <= 2*(n-1)*osc_bound[1]*Anorm
        if name == "full_rank_inertia_5_1":
            assert F(14, 5) < actual_frozen[0] < actual_frozen[1] < F(29, 10)
            assert F(20) < hessian_negative[0] < hessian_negative[1] < F(21)
        results[name] = {
            "direction": A, "norm_squared": Anorm, "trace": t,
            "fisher": fisher, "count_fisher": count_fisher,
            "within_count_score_variance": within_count,
            "count_score_remainder": count_residual,
            "frozen_curvature_interval": actual_frozen,
            "frozen_curvature_display": display(actual_frozen),
            "residual_curvature_interval": residual_frozen,
            "negative_hessian_interval": hessian_negative,
            "negative_hessian_display": display(hessian_negative),
            "theorem_lower_bound": certified_bound,
            "atom_jets": jet,
        }

    # Sharpness of the general oscillation acceleration bound.
    z = s.symbols("z")
    parity_expectation = (1+(1-2*z)**n)/2
    assert s.diff(parity_expectation, z, 2).subs(z, 0) == 2*n*(n-1)

    # The old C047 all-direction sufficient budget fails exactly at kappa=127.
    # log(128^2/(4*127)) > log 16 = 4 log 2 > 8/3.
    ratio = F(128**2, 4*127)
    assert ratio > 16
    assert log_interval(F(2))[0] > F(2, 3)
    assert F(5, 6)*F(8, 3) > 1
    assert F(4, 5)*F(8, 3) > 1

    output = {
        "status": "PASS",
        "n": n, "theta": theta, "integer_vector": list(x),
        "normalizing_square_sum": D, "kernel": K,
        "spectrum": {"1/2": n-1, "127/128": 1},
        "odds_condition_number": 127,
        "relative_magnitude_deviation": eps,
        "allowed_relative_deviation": d/F(16*(n-1)),
        "frobenius_gap_before_residual": d,
        "frobenius_gap_after_residual": d/2,
        "fisher_fraction": F(67, 320),
        "beta_interval": beta, "beta_display": display(beta),
        "gamma_interval": gamma, "gamma_display": display(gamma),
        "oscillation_upper_interval": osc_bound,
        "nonzero_commutator_entry_1_3": rat(commutator[0, 2]),
        "directions": results,
        "checks": ["64 exact signed atom determinants and inverses",
                   "192 exact atom derivative triples",
                   "full count-acceleration and matrix-square identities",
                   "nonflat residual and all-direction analytic constants",
                   "actual frozen curvature positive in rank-six indefinite direction",
                   "sharp oscillation constant and C047 budget failure"],
    }
    target = Path(__file__).with_name("exact_certificate.json")
    target.write_text(json.dumps(enc(output), indent=2, default=str)+"\n")
    for item in output["checks"]:
        print("PASS:", item)
    for name, result in results.items():
        print(name, "-H'' enclosure", result["negative_hessian_display"])


if __name__ == "__main__":
    main()
