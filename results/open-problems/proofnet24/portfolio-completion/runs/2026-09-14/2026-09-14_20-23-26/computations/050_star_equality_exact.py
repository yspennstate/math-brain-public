"""Exact finite certificates for agents/050.md (standard library only).

The proofs are analytic and all-dimensional. These finite checks audit the
Gaussian-rational atom identities, nontrivial flat examples, a connected
zero-Fisher/strict-curvature example, and the noise-gradient lemma for all
20 monotone Boolean functions on three coordinates.
"""

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import json


@dataclass(frozen=True)
class G:
    r: Q = Q(0)
    i: Q = Q(0)

    def __post_init__(self):
        object.__setattr__(self, "r", Q(self.r))
        object.__setattr__(self, "i", Q(self.i))

    @staticmethod
    def of(x):
        return x if isinstance(x, G) else G(x)

    def __add__(self, x):
        x = self.of(x)
        return G(self.r + x.r, self.i + x.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, x):
        return self + (-self.of(x))

    def __rsub__(self, x):
        return self.of(x) + (-self)

    def __mul__(self, x):
        x = self.of(x)
        return G(self.r*x.r-self.i*x.i, self.r*x.i+self.i*x.r)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = self.of(x)
        d = x.r*x.r+x.i*x.i
        return self*x.conj()*G(1/d)

    def conj(self):
        return G(self.r, -self.i)

    def __str__(self):
        return str(self.r) if self.i == 0 else f"{self.r}+({self.i})i"


ZERO = G()


def det(M):
    n = len(M)
    a = [row[:] for row in M]
    answer = G(1)
    for j in range(n):
        pivot = next((k for k in range(j, n) if a[k][j] != ZERO), None)
        if pivot is None:
            return ZERO
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            answer = -answer
        p = a[j][j]
        answer *= p
        for k in range(j+1, n):
            ratio = a[k][j]/p
            for ell in range(j+1, n):
                a[k][ell] -= ratio*a[j][ell]
    return answer


def inverse(M):
    n = len(M)
    a = [row[:] + [G(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for j in range(n):
        pivot = next(k for k in range(j, n) if a[k][j] != ZERO)
        a[j], a[pivot] = a[pivot], a[j]
        p = a[j][j]
        a[j] = [x/p for x in a[j]]
        for k in range(n):
            if k != j:
                ratio = a[k][j]
                a[k] = [x-ratio*y for x, y in zip(a[k], a[j])]
    return [row[n:] for row in a]


def indices(mask, n):
    return [j for j in range(n) if mask >> j & 1]


def principal(M, ids):
    return [[M[i][j] for j in ids] for i in ids]


def check_psd(M, strict=False):
    n = len(M)
    assert all(M[i][j] == M[j][i].conj() for i in range(n) for j in range(n))
    for mask in range(1, 1 << n):
        value = det(principal(M, indices(mask, n)))
        assert value.i == 0
        assert value.r > 0 if strict else value.r >= 0


def check_contraction(K, strict=False):
    n = len(K)
    check_psd(K, strict)
    check_psd([[G(int(i == j))-K[i][j] for j in range(n)] for i in range(n)], strict)


def multiply_poly(a, b, degree):
    out = [G() for _ in range(degree+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i+j <= degree:
                out[i+j] += x*y
    return out


def atom_polynomials(K, A):
    n = len(K)
    output = []
    for mask in range(1 << n):
        total = [G() for _ in range(n+1)]
        for perm in permutations(range(n)):
            parity = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
            term = [G((-1)**parity)]
            for row, col in enumerate(perm):
                if mask >> col & 1:
                    factor = [K[row][col], A[row][col]]
                else:
                    factor = [G(int(row == col))-K[row][col], -A[row][col]]
                term = multiply_poly(term, factor, n)
            total = [x+y for x, y in zip(total, term)]
        assert all(x.i == 0 for x in total)
        output.append([x.r for x in total])
    for degree in range(n+1):
        assert sum(p[degree] for p in output) == int(degree == 0)
        if degree > 2:
            assert all(p[degree] == 0 for p in output)
    return output


def add_log(out, q, coefficient):
    """Accumulate coefficient*log(q) in the prime-log rational basis."""
    assert q > 0
    for value, sign in ((q.numerator, 1), (q.denominator, -1)):
        prime = 2
        while prime*prime <= value:
            exponent = 0
            while value % prime == 0:
                value //= prime
                exponent += 1
            if exponent:
                out[prime] = out.get(prime, Q(0)) + coefficient*sign*exponent
            prime += 1
        if value > 1:
            out[value] = out.get(value, Q(0)) + coefficient*sign
    for key in list(out):
        if out[key] == 0:
            del out[key]


def star(n, links, alpha=0):
    A = [[G() for _ in range(n)] for _ in range(n)]
    A[0][0] = G(alpha)
    for j, v in links.items():
        A[j][0] = v
        A[0][j] = v.conj()
    return A


def flat_case(name, K, A, expected_quartic=None, boundary=False):
    check_contraction(K, not boundary)
    n = len(K)
    # A fixed nonzero feasible point also certifies a feasible two-sided interval.
    quarter = [[K[i][j]+A[i][j]/4 for j in range(n)] for i in range(n)]
    check_contraction(quarter, not boundary)
    atoms = atom_polynomials(K, A)
    log_term = {}
    chi_coefficient = Q(0)
    positive = 0
    for p in atoms:
        assert p[1] == 0
        if p[0] == 0:
            assert all(x == 0 for x in p)
            continue
        positive += 1
        assert p[0] > 0
        add_log(log_term, p[0], p[2])
        chi_coefficient += p[2]**2/p[0]
    assert log_term == {}
    quartic = -chi_coefficient/2
    assert quartic < 0
    if expected_quartic is not None:
        assert quartic == expected_quartic
    return {
        "name": name,
        "dimension": n,
        "positive_base_atoms": positive,
        "boundary_kernel": boundary,
        "all_first_atom_derivatives_zero": True,
        "cross_entropy_quadratic_coefficient_exactly_zero": True,
        "quartic_entropy_coefficient": str(quartic),
        "fourth_entropy_derivative": str(24*quartic),
        "K": [[str(x) for x in row] for row in K],
        "A": [[str(x) for x in row] for row in A],
        "atom_polynomials": [[str(x) for x in p] for p in atoms],
    }


def expectation_gradient(C, g):
    n = len(C)
    gradient = [[G() for _ in range(n)] for _ in range(n)]
    for mask in range(1, 1 << n):
        coefficient = Q(0)
        sub = mask
        while True:
            coefficient += (-1)**((mask ^ sub).bit_count())*g[sub]
            if sub == 0:
                break
            sub = (sub-1) & mask
        if coefficient == 0:
            continue
        ids = indices(mask, n)
        minor = principal(C, ids)
        determinant = det(minor)
        inv = inverse(minor)
        for i, row in enumerate(ids):
            for j, col in enumerate(ids):
                gradient[row][col] += coefficient*determinant*inv[i][j]
    return gradient


def noise_gradient_checks():
    C = [[G(Q(1,2)), G(1,1)/16, G()],
         [G(1,-1)/16, G(Q(1,2)), G(1,-2)/32],
         [G(), G(1,2)/32, G(Q(1,2))]]
    epsilon = Q(1,8)
    scale = 1-2*epsilon
    D = [[(C[i][j]-G(epsilon if i == j else 0))/scale for j in range(3)] for i in range(3)]
    check_contraction(C, True)
    check_contraction(D, True)
    count = 0
    active_count_histogram = {}
    for table in range(256):
        g = [Q(table >> mask & 1) for mask in range(8)]
        if any(g[mask] > g[mask | 1 << j] for mask in range(8) for j in range(3)):
            continue
        count += 1
        edge_sums = [sum(g[mask | 1 << j]-g[mask] for mask in range(8) if not mask >> j & 1) for j in range(3)]
        active = [j for j in range(3) if edge_sums[j] > 0]
        active_count_histogram[len(active)] = active_count_histogram.get(len(active), 0)+1
        gradient = expectation_gradient(C, g)
        lower = [[gradient[i][j]-G(epsilon**2*edge_sums[i] if i == j else 0) for j in range(3)] for i in range(3)]
        check_psd(lower)
        check_psd(principal(gradient, active), True)
        assert all(gradient[i][j] == ZERO for i in range(3) for j in range(3) if i not in active or j not in active)
        h = [sum(epsilon**((mask ^ other).bit_count())*(1-epsilon)**(3-(mask ^ other).bit_count())*g[other] for other in range(8)) for mask in range(8)]
        noisy_gradient = expectation_gradient(D, h)
        assert all(noisy_gradient[i][j] == scale*gradient[i][j] for i in range(3) for j in range(3))
    assert count == 20
    return {
        "monotone_boolean_functions_checked": count,
        "active_count_histogram": active_count_histogram,
        "epsilon": str(epsilon),
        "all_gradient_lower_bounds_psd_exactly": True,
        "all_active_principal_blocks_positive_definite_exactly": True,
        "all_inactive_rows_columns_exactly_zero": True,
        "noise_gradient_chain_identity_exact": True,
    }


def connected_zero_fisher_case():
    K = [[G(Q(1,2)), G(Q(1,8)), G()],
         [G(Q(1,8)), G(Q(1,2)), G(Q(1,8))],
         [G(), G(Q(1,8)), G(Q(1,2))]]
    A = star(3, {2: G(0, Q(1,10))})
    check_contraction(K, True)
    atoms = atom_polynomials(K, A)
    assert all(p[1] == 0 for p in atoms)
    odds = [atoms[mask << 1][0]/atoms[(mask << 1) | 1][0] for mask in range(4)]
    assert odds == [Q(7,8), Q(9,8), Q(8,9), Q(8,7)]
    assert odds[3]*odds[0] == odds[1]*odds[2]
    exact_hessian = {}
    for p in atoms:
        add_log(exact_hessian, p[0], -2*p[2])
    predicted = {}
    add_log(predicted, Q(64,63), -Q(1,50))
    assert exact_hessian == predicted
    return {
        "name": "connected_real_chain_imaginary_star_tangent",
        "all_first_atom_derivatives_zero": True,
        "conditional_odds_in_bitmask_order": [str(x) for x in odds],
        "Q_g_diagonal": ["log(9/7)", "log(64/63)"],
        "Q_g_off_diagonal": "0",
        "exact_hessian": "-log(64/63)/50 < 0",
        "verified_prime_log_coefficients": {str(p): str(c) for p, c in exact_hessian.items()},
    }


def main():
    w = G(1,1)/8
    K3 = [[G(Q(1,2)), w.conj(), G()],
          [w, G(Q(1,2)), G()],
          [G(), G(), G(Q(1,3))]]
    K4 = [[G(Q(1,2)), w.conj(), G(), G()],
          [w, G(Q(1,2)), G(), G()],
          [G(), G(), G(Q(1,3)), G(1,1)/20],
          [G(), G(), G(1,-1)/20, G(Q(2,5))]]
    Kb = [[G(Q(1,2)), G(), G()],
          [G(), G(Q(1,2)), G()],
          [G(), G(), G()]]
    output = {
        "method": "Exact Gaussian-rational determinants and prime-log cancellation; no numerical sign tests.",
        "limitations": "Finite consistency certificates only; all-dimensional proofs are in agents/050.md.",
        "flat_cases": [
            flat_case("complex_nondiagonal_base_three_sites", K3, star(3, {2: G(1,2)/10}), -Q(4,175)),
            flat_case("two_complex_nondiagonal_blocks_four_sites", K4, star(4, {2: G(1,2)/10, 3: G(2,-1)/15})),
            flat_case("entirely_boundary_path_with_deterministic_coordinate", Kb, star(3, {1: G(1)}), -Q(8), True),
        ],
        "connected_zero_fisher_case": connected_zero_fisher_case(),
        "noise_gradient_checks": noise_gradient_checks(),
        "all_exact_checks_passed": True,
    }
    path = Path(__file__).with_name("050_star_equality_exact_output.json")
    path.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps({"all_exact_checks_passed": True,
                      "flat_case_quartics": {x["name"]: x["quartic_entropy_coefficient"] for x in output["flat_cases"]},
                      "monotone_functions_checked": output["noise_gradient_checks"]["monotone_boolean_functions_checked"],
                      "output": str(path)}, indent=2))


if __name__ == "__main__":
    main()
