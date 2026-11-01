"""Exact certificates for worker 036's rational two-row obstruction.

Uses only fractions, integer arithmetic, and the rational atanh-series remainder.
The computed Hessian certificate is pointwise; it is not a global slice proof.
Run: python computations/036_exact_certificate.py
"""
from fractions import Fraction as F
from itertools import product, permutations
import json


def det(M):
    ans = F(0)
    for perm in permutations(range(3)):
        inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i+1, 3))
        value = F((-1)**inversions)
        for i in range(3):
            value *= M[i][perm[i]]
        ans += value
    return ans


def add_interval(a, b):
    return a[0]+b[0], a[1]+b[1]


def scale_interval(c, x):
    return (c*x[0], c*x[1]) if c >= 0 else (c*x[1], c*x[0])


def logarithm_interval(q, terms=25):
    """A rational enclosure for log(q), with q positive rational."""
    q = F(q)
    assert q > 0
    k = 0
    while q < 1:
        q *= 2
        k -= 1
    while q >= 2:
        q /= 2
        k += 1

    def series(r):
        x = (r-1)/(r+1)
        assert 0 <= x <= F(1, 3)
        partial = 2*sum((x**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
        tail = 2*x**(2*terms+1)/(F(2*terms+1)*(1-x*x))
        return partial, partial+tail

    return add_interval(series(q), scale_interval(F(k), series(F(2))))


def matrix_basis():
    out = []
    for i in (0, 1):
        E = [[F(0) for _ in range(3)] for _ in range(3)]
        E[i][i] = F(1)
        out.append((E, 0))
    for phase in (0, 1):
        for i, j in ((0, 1), (0, 2), (1, 2)):
            E = [[F(0) for _ in range(3)] for _ in range(3)]
            E[i][j] = F(1)
            E[j][i] = F(1 if phase == 0 else -1)
            out.append((E, phase))
    return out


def atom_coefficients(K):
    basis = matrix_basis()
    result = []
    for bits in product((0, 1), repeat=3):
        signs = [2*b-1 for b in bits]
        M = [[K[i][j]*signs[j]+F(i == j)*(1-bits[j]) for j in range(3)] for i in range(3)]
        Es = [([[E[i][j]*signs[j] for j in range(3)] for i in range(3)], phase) for E, phase in basis]
        p = det(M)
        first = []
        for E, phase in Es:
            dp = F(0)
            for col in range(3):
                N = [row[:] for row in M]
                for row in range(3):
                    N[row][col] = E[row][col]
                dp += det(N)
            if phase:
                assert dp == 0
            first.append(dp)
        second = []
        for E, phase_E in Es:
            thisrow = []
            for Q, phase_Q in Es:
                ddp = F(0)
                for ca in range(3):
                    for cb in range(3):
                        if ca == cb:
                            continue
                        N = [row[:] for row in M]
                        for row in range(3):
                            N[row][ca] = E[row][ca]
                            N[row][cb] = Q[row][cb]
                        ddp += det(N)
                phases = phase_E+phase_Q
                if phases == 1:
                    assert ddp == 0
                elif phases == 2:
                    ddp = -ddp
                thisrow.append(ddp)
            second.append(thisrow)
        assert p > 0
        result.append((bits, p, first, second))
    assert sum(x[1] for x in result) == 1
    for i in range(8):
        assert sum(x[2][i] for x in result) == 0
        for j in range(8):
            assert sum(x[3][i][j] for x in result) == 0
            assert all(x[3][i][j] == x[3][j][i] for x in result)
    return result


def ldl(M):
    n = len(M)
    L = [[F(i == j) for j in range(n)] for i in range(n)]
    D = []
    for j in range(n):
        dj = M[j][j]-sum((L[j][k]**2*D[k] for k in range(j)), F(0))
        assert dj > 0
        D.append(dj)
        for i in range(j+1, n):
            L[i][j] = (M[i][j]-sum((L[i][k]*D[k]*L[j][k] for k in range(j)), F(0)))/dj
    for i in range(n):
        for j in range(n):
            assert M[i][j] == sum((L[i][k]*D[k]*L[j][k] for k in range(n)), F(0))
    return L, D


def main():
    K = [[F(1,5),F(3,20),F(1,4)], [F(3,20),F(9,10),F(0)], [F(1,4),F(0),F(1,2)]]
    complement = [[F(i == j)-K[i][j] for j in range(3)] for i in range(3)]
    assert det(K) == det(complement) == F(9, 400)
    assert K[0][0]*K[1][1]-K[0][1]**2 == F(63, 400)
    assert complement[0][0]*complement[1][1]-complement[0][1]**2 == F(23, 400)

    numerator = 3**38*19**37*11**13
    denominator = 2**80*7**64
    assert 6*denominator < numerator < 7*denominator
    g22 = scale_interval(F(1,40), logarithm_interval(F(numerator, denominator)))
    assert g22[0] > 0

    atoms = atom_coefficients(K)
    logs = [logarithm_interval(atom[1]) for atom in atoms]
    M = []  # M is minus the entropy Hessian in the raw real-coordinate basis.
    for i in range(8):
        row = []
        for j in range(8):
            fisher = sum((a[2][i]*a[2][j]/a[1] for a in atoms), F(0))
            entry = (fisher, fisher)
            for a, interval in zip(atoms, logs):
                entry = add_interval(entry, scale_interval(a[3][i][j], interval))
            row.append(entry)
        M.append(row)

    scale = 10**6
    R = []
    for row in M:
        rr = []
        for lo, hi in row:
            midpoint = (lo+hi)/2
            integer = (midpoint*scale+F(1,2)).numerator//(midpoint*scale+F(1,2)).denominator
            rounded = F(integer, scale)
            assert rounded-F(1,scale) <= lo <= hi <= rounded+F(1,scale)
            rr.append(rounded)
        R.append(rr)
    for i in range(8):
        for j in range(8):
            assert R[i][j] == R[j][i]

    # |M_ij-R_ij| <= 10^-6 implies M-R >= -8*10^-6 I.
    # Gram for ||D||_F^2 in this raw basis is diag(1,1,2,2,2,2,2,2).
    gram = [1,1,2,2,2,2,2,2]
    C = [[R[i][j]-F(i == j)*(F(gram[i],4)+F(8,scale)) for j in range(8)] for i in range(8)]
    _, pivots = ldl(C)
    pivot_lower = [F((p*scale).numerator//(p*scale).denominator, scale) for p in pivots]
    assert min(pivot_lower) > 0
    # Thus M >= (1/4) Gram, or H''(K)[D,D] <= -(1/4)||D||_F^2 for D_33=0.

    natural_coordinates = [F(1),F(1),F(0),F(0),F(1,4),F(0),F(0),F(0)]
    natural_first, natural_second = [], []
    for atom in atoms:
        natural_first.append(sum((atom[2][i]*natural_coordinates[i] for i in range(8)), F(0)))
        natural_second.append(sum((atom[3][i][j]*natural_coordinates[i]*natural_coordinates[j]
                                   for i in range(8) for j in range(8)), F(0)))
    natural_fisher = sum((dp*dp/atom[1] for dp, atom in zip(natural_first, atoms)), F(0))
    natural_curvature = (F(0), F(0))
    for ddp, interval in zip(natural_second, logs):
        natural_curvature = add_interval(natural_curvature, scale_interval(-ddp, interval))
    natural_hessian = add_interval((-natural_fisher, -natural_fisher), natural_curvature)
    assert natural_curvature[0] > 0
    assert natural_hessian[1] < 0

    result = {
        "exact_integer_gradient_certificate": {
            "numerator": str(numerator), "denominator": str(denominator),
            "proved_ratio_interval": [6, 7],
            "g22_approximate_interval": [float(g22[0]), float(g22[1])],
        },
        "basis_order": ["D11", "D22", "ReD12", "ReD13", "ReD23", "ImD12", "ImD13", "ImD23"],
        "atom_order": ["".join(map(str,a[0])) for a in atoms],
        "atom_probabilities": [str(a[1]) for a in atoms],
        "rational_hessian_approximation_scaled_by_1000000": [[int(e*scale) for e in row] for row in R],
        "certified_entrywise_absolute_error": "1/1000000",
        "ldl_shift": "Gram/4 + (8/1000000) I",
        "certified_ldl_pivot_lower_bounds": [str(p) for p in pivot_lower],
        "proved_pointwise_bound": "H''(K)[D,D] <= -||D||_F^2/4 for every Hermitian D with D33=0",
        "natural_mixed_direction": {
            "D": [["1","0","0"], ["0","1","1/4"], ["0","1/4","0"]],
            "atom_first_derivatives": [str(p) for p in natural_first],
            "atom_second_derivatives": [str(p) for p in natural_second],
            "fisher": str(natural_fisher),
            "certified_positive_curvature_approximate_interval": [float(x) for x in natural_curvature],
            "certified_negative_full_hessian_approximate_interval": [float(x) for x in natural_hessian],
            "positive_conditional_correction_approximate_interval": [float(x/F(8)) for x in g22],
        },
        "scope_warning": "One exact rational base kernel, not global two-row-slice concavity.",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
