#!/usr/bin/env python3
"""Exact certificates for agent 053; Python standard library only.

Computes affine principal determinants and atoms independently, checks the
commutator trace formula, verifies entropy logarithms by prime valuations,
and checks a feasible singular three-site coordinate-splitting example.
All sign certificates use rational/Gaussian-rational arithmetic.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations
import json
from pathlib import Path


@dataclass(frozen=True)
class G:
    r: F = F(0)
    i: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "r", F(self.r))
        object.__setattr__(self, "i", F(self.i))

    def __add__(self, other):
        other = as_g(other)
        return G(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, other):
        return self + -as_g(other)

    def __rsub__(self, other):
        return as_g(other) + -self

    def __mul__(self, other):
        other = as_g(other)
        return G(self.r * other.r - self.i * other.i,
                 self.r * other.i + self.i * other.r)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_g(other)
        den = other.r**2 + other.i**2
        assert den
        return self * G(other.r / den, -other.i / den)

    def conj(self):
        return G(self.r, -self.i)

    def norm2(self):
        return self.r**2 + self.i**2

    def __bool__(self):
        return bool(self.r or self.i)

    def __str__(self):
        if not self.i:
            return str(self.r)
        return f"({self.r})+({self.i})i"


def as_g(x):
    return x if isinstance(x, G) else G(x)


I = G(0, 1)


def ids(mask, n):
    return [j for j in range(n) if mask & (1 << j)]


def submatrix(M, mask):
    ix = ids(mask, len(M))
    return [[M[i][j] for j in ix] for i in ix]


def identity(n):
    return [[G(int(i == j)) for j in range(n)] for i in range(n)]


def complement(M):
    return [[G(int(i == j)) - M[i][j] for j in range(len(M))]
            for i in range(len(M))]


def matmul(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), G())
             for j in range(n)] for i in range(n)]


def inverse(A):
    n = len(A)
    M = [A[i][:] + identity(n)[i] for i in range(n)]
    for j in range(n):
        p = next(i for i in range(j, n) if M[i][j])
        M[j], M[p] = M[p], M[j]
        divisor = M[j][j]
        M[j] = [x / divisor for x in M[j]]
        for i in range(n):
            if i == j:
                continue
            c = M[i][j]
            M[i] = [x - c*y for x, y in zip(M[i], M[j])]
    return [row[n:] for row in M]


def polyadd(p, q):
    out = [G() for _ in range(max(len(p), len(q)))]
    for j, x in enumerate(p):
        out[j] += x
    for j, x in enumerate(q):
        out[j] += x
    return out


def polymul(p, q):
    out = [G() for _ in range(len(p) + len(q) - 1)]
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return out


def detpoly(K, A):
    n = len(K)
    out = [G() for _ in range(n+1)]
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j]
                         for i in range(n) for j in range(i+1, n))
        term = [G((-1)**inversions)]
        for i in range(n):
            term = polymul(term, [K[i][perm[i]], A[i][perm[i]]])
        out = polyadd(out, term)
    return out


def det(K):
    return detpoly(K, [[G() for _ in K] for _ in K])[0]


def coeff(p, j):
    return p[j] if j < len(p) else G()


def gauge(K, d):
    return [[I*(d[i]-d[j])*K[i][j] for j in range(len(K))]
            for i in range(len(K))]


def principal_polys(K, A):
    return {mask: detpoly(submatrix(K, mask), submatrix(A, mask))
            for mask in range(1 << len(K))}


def atom_polys(K, A, check_stationary=True):
    n = len(K)
    principal = principal_polys(K, A)
    atoms = {}
    for mask in range(1 << n):
        # Inclusion-exclusion from principal inclusion probabilities.
        out = [G() for _ in range(n+1)]
        for sup in range(1 << n):
            if sup & mask == mask:
                sign = (-1)**(sup.bit_count()-mask.bit_count())
                out = polyadd(out, [sign*x for x in principal[sup]])
        # Independent mixed-column determinant atom identity.
        M = [[K[i][j] if mask & (1 << j)
              else G(int(i == j))-K[i][j] for j in range(n)]
             for i in range(n)]
        B = [[A[i][j] if mask & (1 << j) else -A[i][j]
              for j in range(n)] for i in range(n)]
        assert out == detpoly(M, B)
        if check_stationary:
            assert not coeff(out, 1)
        assert all(not x.i for x in out)
        atoms[mask] = out
    total = [sum((atoms[s][j] for s in atoms), G()) for j in range(n+1)]
    assert total == [G(1)] + [G()]*n
    return atoms


def mobius_exp(atoms, mask):
    value = F(1)
    for sub in atoms:
        if sub & mask == sub:
            p = atoms[sub][0].r
            assert p > 0
            exponent = (-1)**(mask.bit_count()-sub.bit_count()+1)
            value *= p**exponent
    return value


def valuations(q):
    """Prime valuations of a positive rational, to compare log expressions."""
    q = F(q)
    assert q > 0
    out = {}
    for integer, sign in ((q.numerator, 1), (q.denominator, -1)):
        divisor = 2
        while divisor*divisor <= integer:
            while integer % divisor == 0:
                out[divisor] = out.get(divisor, 0) + sign
                integer //= divisor
            divisor += 1
        if integer > 1:
            out[integer] = out.get(integer, 0) + sign
    return {p: e for p, e in out.items() if e}


def logform(terms):
    out = {}
    for multiplier, arg in terms:
        for prime, power in valuations(arg).items():
            out[prime] = out.get(prime, F(0)) + multiplier*power
    return {p: v for p, v in out.items() if v}


def hessian_logform(atoms):
    assert all(not coeff(p, 1) for p in atoms.values())
    return logform([(-2*coeff(p, 2).r, p[0].r)
                    for p in atoms.values() if p[0]])


def verify_principal_trace(K, A):
    n = len(K)
    result = []
    for mask in range(1, 1 << n):
        KS, AS = submatrix(K, mask), submatrix(A, mask)
        assert all(KS[i][j] == KS[j][i].conj()
                   for i in range(len(KS)) for j in range(len(KS)))
        p = detpoly(KS, AS)
        assert p[0].r > 0 and not p[0].i
        assert not coeff(p, 1)
        R = matmul(inverse(KS), AS)
        assert not sum((R[i][i] for i in range(len(R))), G())
        RR = matmul(R, R)
        tr2 = sum((RR[i][i] for i in range(len(R))), G())
        assert not tr2.i and tr2.r >= 0
        assert 2*coeff(p, 2) == -p[0]*tr2
        assert (not tr2) == all(not x for row in AS for x in row)
        result.append({"set": ids(mask, n),
                       "det": str(p[0]),
                       "second_derivative": str(2*coeff(p, 2)),
                       "trace_square": str(tr2)})
    return result


def complex_example(diagonal):
    r = F(1, 10)
    K = [[G(diagonal), G(r), -I*r],
         [G(r), G(diagonal), G(r)],
         [I*r, G(r), G(diagonal)]]
    A = gauge(K, [0, 1, 2])
    principal = verify_principal_trace(K, A)
    verify_principal_trace(complement(K), [[-x for x in row] for row in A])
    assert det(A) == G(F(1, 250))
    atoms = atom_polys(K, A)
    d = [0, 1, 2]
    acceleration = [[-(d[i]-d[j])**2*K[i][j] for j in range(3)] for i in range(3)]
    acceleration_atoms = atom_polys(K, acceleration, check_stationary=False)
    for mask in atoms:
        assert 2*coeff(atoms[mask], 2) + coeff(acceleration_atoms[mask], 1) == G()
    pair_exp = [mobius_exp(atoms, m) for m in (3, 5, 6)]
    triple_exp = mobius_exp(atoms, 7)
    assert pair_exp[0] == pair_exp[1] == pair_exp[2]
    assert all(q > 1 for q in pair_exp)
    if diagonal == F(2, 5):
        assert pair_exp[0] == F(5776, 4851)
        assert triple_exp == F(11647251, 11413376) > 1
        expected = [(F(-3, 25), pair_exp[0]),
                    (F(-6, 125), triple_exp)]
    elif diagonal == F(1, 2):
        assert pair_exp[0] == F(13, 11)
        assert triple_exp == 1
        expected = [(F(-3, 25), F(13, 11))]
    else:
        assert diagonal == F(3, 5) and triple_exp < 1
        comp_atoms = atom_polys(complement(K), [[-x for x in row] for row in A])
        comp_pair = mobius_exp(comp_atoms, 3)
        comp_triple = mobius_exp(comp_atoms, 7)
        assert comp_pair == pair_exp[0]*triple_exp
        assert comp_triple == 1/triple_exp
        expected = [(F(-3, 25), comp_pair), (F(-6, 125), comp_triple)]
    assert hessian_logform(atoms) == logform(expected)

    L = matmul(K, inverse(complement(K)))
    normprod = L[0][0]*L[1][1]*L[2][2]
    cycle = L[0][1]*L[1][2]*L[2][0] / normprod
    x, y, z = [L[i][j].norm2() / (L[i][i].r*L[j][j].r)
               for i, j in ((0, 1), (1, 2), (2, 0))]
    normalized_det = det(L).r / normprod.r
    assert normalized_det == 1-x-y-z+2*cycle.r
    if diagonal == F(1, 2):
        assert 2*cycle.r == x*y+x*z+y*z-x*y*z
    return {"diagonal": str(diagonal),
            "K": [[str(x) for x in row] for row in K],
            "A": [[str(x) for x in row] for row in A],
            "det_A": str(det(A)),
            "curved_orbit_second_derivative_cancellation": "PASS for every atom",
            "principal_certificates": principal,
            "atoms_by_bitmask": {str(m): [str(x) for x in p]
                                 for m, p in atoms.items()},
            "pair_mobius_exponentials": list(map(str, pair_exp)),
            "triple_mobius_exponential": str(triple_exp),
            "entropy_second_derivative": [
                {"coefficient": str(c), "log_argument": str(q)} for c, q in expected],
            "L": [[str(x) for x in row] for row in L],
            "normalized_L_squared_edges": list(map(str, (x, y, z))),
            "normalized_L_cycle": str(cycle)}


def boundary_example():
    # K = V C V*, V = [v,e3], v=(3/5,4/5,0); zero eigenvector w=(-4/5,3/5,0).
    K = [[G(F(18, 125)), G(F(24, 125)), G(F(3, 50))],
         [G(F(24, 125)), G(F(32, 125)), G(F(2, 25))],
         [G(F(3, 50)), G(F(2, 25)), G(F(3, 5))]]
    A = gauge(K, [0, 0, 1])
    w = [G(F(-4, 5)), G(F(3, 5)), G()]
    assert all(not sum((M[i][j]*w[j] for j in range(3)), G())
               for M in (K, A) for i in range(3))
    assert not det(K)
    atoms = atom_polys(K, A)
    C = [[G(F(2, 5)), G(F(1, 10))],
         [G(F(1, 10)), G(F(3, 5))]]
    Ac = gauge(C, [0, 1])
    virtual_atoms = atom_polys(C, Ac)
    q = F(9, 25)
    expected = {0: virtual_atoms[0], 1: [q*x for x in virtual_atoms[1]],
                2: [(1-q)*x for x in virtual_atoms[1]],
                4: virtual_atoms[2], 5: [q*x for x in virtual_atoms[3]],
                6: [(1-q)*x for x in virtual_atoms[3]],
                3: [G()]*3, 7: [G()]*3}
    for mask, p in atoms.items():
        assert p == expected[mask] + [G()]
    for mask, p in atoms.items():
        if not p[0]:
            assert all(not x for x in p)
    expected_hessian = [(F(-1, 50), F(629, 529))]
    assert hessian_logform(atoms) == logform(expected_hessian)
    assert hessian_logform(atoms) == hessian_logform(virtual_atoms)
    # C +/- Ac remain strict contractions, an exact feasible two-sided segment.
    for sign in (-1, 1):
        Ct = [[C[i][j] + sign*Ac[i][j] for j in range(2)] for i in range(2)]
        assert det(Ct).r == F(11, 50) and det(complement(Ct)).r == F(11, 50)
        assert Ct[0][0].r > 0 and complement(Ct)[0][0].r > 0
    # A projection's nonzero gauge tangent is not affine feasible.
    P = [[G(F(1, 2)), G(F(1, 2))], [G(F(1, 2)), G(F(1, 2))]]
    AP = gauge(P, [0, 1])
    assert detpoly(P, AP) == [G(), G(), G(F(-1, 4))]
    return {"K": [[str(x) for x in row] for row in K],
            "A": [[str(x) for x in row] for row in A],
            "split_probability": str(q),
            "atoms_by_bitmask": {str(m): [str(x) for x in p] for m, p in atoms.items()},
            "entropy_second_derivative": "-(1/50) log(629/529)",
            "feasible_t_interval_certified": "[-1,1]",
            "projection_nonfeasibility_determinant": "-t^2/4"}


def all_n_cone_example():
    n = 4
    K = [[G(F(1, 2)) if i == j else G() for j in range(n)] for i in range(n)]
    for i, j, z in ((0, 1, G(F(1, 20), F(1, 30))),
                    (0, 2, G(F(-1, 25), F(1, 40))),
                    (0, 3, G(F(1, 50), F(-1, 20))),
                    (1, 2, G(F(1, 30), F(1, 25))),
                    (1, 3, G(F(-1, 40), F(1, 50))),
                    (2, 3, G(F(1, 20), F(1, 40)))):
        K[i][j], K[j][i] = z, z.conj()
    A = gauge(K, [0, 1, 3, 7])
    verify_principal_trace(K, A)
    verify_principal_trace(complement(K), [[-x for x in row] for row in A])
    alpha = {3: F(2), 7: F(3, 2), 15: F(1, 3)}
    beta = {6: F(1, 4), 11: F(5, 3), 15: F(2, 7)}
    f = {mask: sum((c for sup, c in alpha.items() if mask & sup == sup), F(0))
         + sum((c for sup, c in beta.items() if not (mask & sup)), F(0))
         for mask in range(1 << n)}
    for i in range(n):
        for j in range(i+1, n):
            for mask in range(1 << n):
                if mask & ((1 << i) | (1 << j)):
                    continue
                delta = f[mask | (1 << i) | (1 << j)] + f[mask] - f[mask | (1 << i)] - f[mask | (1 << j)]
                assert delta >= 0
    atoms = atom_polys(K, A)
    direct = sum((2*coeff(atoms[m], 2).r*f[m] for m in atoms), F(0))
    pp = principal_polys(K, A)
    pm = principal_polys(complement(K), [[-x for x in row] for row in A])
    inclusion_exclusion = sum((2*c*coeff(pp[m], 2).r for m, c in alpha.items()), F(0))
    inclusion_exclusion += sum((2*c*coeff(pm[m], 2).r for m, c in beta.items()), F(0))
    assert direct == inclusion_exclusion < 0
    return {"dimension": n, "K": [[str(x) for x in row] for row in K],
            "alpha_by_bitmask": {str(k): str(v) for k, v in alpha.items()},
            "beta_by_bitmask": {str(k): str(v) for k, v in beta.items()},
            "curvature": str(direct), "all_elementary_supermodular_inequalities": "PASS"}


def proper_cone_obstruction():
    # Agent 030's supermodular f = u34+u123+u124-u1234.
    n = 4
    c = {12: F(1), 7: F(1), 11: F(1), 15: F(-1)}
    f = {mask: sum((coef for sup, coef in c.items() if mask & sup == sup), F(0))
         for mask in range(1 << n)}

    def delta(i, j, mask):
        pair = (1 << i) | (1 << j)
        assert not mask & pair
        return f[mask | pair] + f[mask] - f[mask | (1 << i)] - f[mask | (1 << j)]

    for i in range(n):
        for j in range(i+1, n):
            for mask in range(1 << n):
                if not mask & ((1 << i) | (1 << j)):
                    assert delta(i, j, mask) >= 0
    exclusions = []
    for sup in range(1 << n):
        if sup.bit_count() < 2:
            continue
        if sup == 12:
            i, j, mask = 2, 3, 3
        else:
            i, j = next((i, j) for i in range(n) for j in range(i+1, n)
                        if sup & ((1 << i) | (1 << j)) == ((1 << i) | (1 << j))
                        and (i, j) != (2, 3))
            mask = 0
        # beta_sup's elementary second difference equals one here,
        # while f's is zero. All other cone contributions are nonnegative.
        assert not (mask & sup)
        assert delta(i, j, mask) == 0
        exclusions.append({"beta_support": ids(sup, n),
                           "zero_delta_pair": [i, j], "context": ids(mask, n)})
    assert c[15] < 0  # Once all beta vanish, this contradicts alpha >= 0.
    return {"mobius_by_bitmask": {str(k): str(v) for k, v in c.items()},
            "all_elementary_supermodular_inequalities": "PASS",
            "positive_beta_exclusions": exclusions,
            "remaining_obstruction": "c_full=-1 cannot equal nonnegative alpha_full"}


def main():
    result = {"status": "PASS: exact rational and Gaussian-rational arithmetic",
              "complex_three_site_examples": [complex_example(x) for x in (F(2, 5), F(1, 2), F(3, 5))],
              "feasible_boundary_example": boundary_example(),
              "positive_inclusion_exclusion_cone_example": all_n_cone_example(),
              "proper_cone_obstruction": proper_cone_obstruction()}
    path = Path(__file__).with_name("053_gauge_curvature_exact_output.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(result["status"])
    print("All three complex interior directions have det(A)=1/250 and zero atom first derivatives.")
    print("Triple Mobius signs: positive, zero, negative; all strict entropy formulas verified.")
    print("Feasible boundary split and nonfeasible projection tangent verified.")
    print("Four-site positive inclusion/exclusion cone curvature:", result["positive_inclusion_exclusion_cone_example"]["curvature"])
    print("Certificate:", path)


if __name__ == "__main__":
    main()
