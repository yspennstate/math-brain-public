"""C043 exact signed-cycle and Laplace-obstruction certificates.

Run: python computations/C043/verify.py
Uses only the Python standard library. All assertions use rational/integer
arithmetic; floating logarithms appear only in separately labeled displays.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import json
import math

OUT = Path(__file__).resolve().parent
N = 4
SUBSETS = [tuple(i for i in range(N) if mask >> i & 1) for mask in range(16)]
PAIRS = list(combinations(range(N), 2))
PAIR_INDEX = {p: i for i, p in enumerate(PAIRS)}
EDGES = {(0, 1), (1, 2), (2, 3), (0, 3)}


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(r) for r in zip(*a)]


def mm(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def sub(a, rows, cols=None):
    cols = rows if cols is None else cols
    return [[a[i][j] for j in cols] for i in rows]


def det(a):
    n = len(a)
    if not n:
        return F(1)
    a = [row[:] for row in a]
    ans = F(1)
    for i in range(n):
        pivot_row = next((j for j in range(i, n) if a[j][i]), None)
        if pivot_row is None:
            return F(0)
        if pivot_row != i:
            a[i], a[pivot_row] = a[pivot_row], a[i]
            ans = -ans
        pivot = a[i][i]
        ans *= pivot
        for j in range(i+1, n):
            scale = a[j][i]/pivot
            for k in range(i+1, n):
                a[j][k] -= scale*a[i][k]
    return ans


def mobius(values):
    result = list(values)
    for i in range(N):
        for mask in range(16):
            if mask >> i & 1:
                result[mask] -= result[mask ^ (1 << i)]
    return result


def exterior_operator(k, values):
    """Canonical cofactor operator, independent of eigenvalue representation."""
    c = mobius(values)
    result = [[F(0) for _ in PAIRS] for _ in PAIRS]
    for mask, s in enumerate(SUBSETS):
        if len(s) < 2 or not c[mask]:
            continue
        for ipos in combinations(range(len(s)), 2):
            i = tuple(s[j] for j in ipos)
            ri = tuple(s[j] for j in range(len(s)) if j not in ipos)
            for jpos in combinations(range(len(s)), 2):
                j = tuple(s[l] for l in jpos)
                rj = tuple(s[l] for l in range(len(s)) if l not in jpos)
                result[PAIR_INDEX[i]][PAIR_INDEX[j]] += (
                    c[mask] * (-1)**(sum(ipos)+sum(jpos))
                    * det(sub(k, ri, rj)))
    return result


def wedge2(u):
    return [[det(sub(u, i, j)) for j in PAIRS] for i in PAIRS]


def diagonal(v):
    return [[v[i] if i == j else F(0) for j in range(len(v))]
            for i in range(len(v))]


def permutation_sign(p):
    return (-1)**sum(p[i] > p[j] for i in range(len(p))
                     for j in range(i+1, len(p)))


def cycle_count(p):
    seen = set()
    count = 0
    for i in range(len(p)):
        if i not in seen:
            count += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    return count


def squarefree_product(a, b):
    """Multiply modulo t_i^2=0, sufficient for the squarefree top coefficient."""
    out = [F(0)]*16
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if not i & j:
                out[i | j] += x*y
    return out


def fractional_power_top(principal_minors, alpha):
    y = list(principal_minors)
    y[0] -= 1
    power = [F(1)] + [F(0)]*15
    binomial = F(1)
    out = F(0)
    for k in range(5):
        out += binomial*power[15]
        power = squarefree_product(power, y)
        binomial *= (-alpha-k)/(k+1)
    return out


def laurent_add(a, b):
    out = dict(a)
    for key, val in b.items():
        out[key] = out.get(key, F(0)) + val
        if not out[key]:
            del out[key]
    return out


def laurent_product(a, b):
    out = {}
    for (r, z), x in a.items():
        for (rr, zz), y in b.items():
            key = r+rr, z+zz
            out[key] = out.get(key, F(0)) + x*y
    return {key: val for key, val in out.items() if val}


def laurent_det(a):
    out = {}
    for p in permutations(range(len(a))):
        term = {(0, 0): F(permutation_sign(p))}
        for i in range(len(a)):
            term = laurent_product(term, a[i][p[i]])
        out = laurent_add(out, term)
    return out


def rational_json(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(k): rational_json(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [rational_json(x) for x in value]
    return value


def main():
    signed_adjacency = [
        [0, 1, 0, -1], [1, 0, 1, 0],
        [0, 1, 0, 1], [-1, 0, 1, 0],
    ]
    a = [[F(x) for x in row] for row in signed_adjacency]
    assert mm(a, a) == [[2*x for x in row] for row in eye(4)]
    ell = [[F(i == j)+a[i][j]/2 for j in range(4)] for i in range(4)]
    k = [[(3*F(i == j)+a[i][j])/7 for j in range(4)] for i in range(4)]
    ik = [[F(i == j)-k[i][j] for j in range(4)] for i in range(4)]
    ipell = [[F(i == j)+ell[i][j] for j in range(4)] for i in range(4)]
    assert mm(k, ipell) == ell
    assert det(ipell) == F(49, 4)
    for matrix in (ell, k, ik):
        assert all(det(sub(matrix, range(j))) > 0 for j in range(1, 5))

    minors = [det(sub(ell, s)) for s in SUBSETS]
    atoms = []
    atom_details = []
    for mask, s in enumerate(SUBSETS):
        edges = sum(set(e).issubset(s) for e in EDGES)
        hinge = max(0, len(s)-2)
        predicted = F(3, 4)**edges * F(8, 9)**hinge
        assert minors[mask] == predicted
        atom_matrix = [[k[i][j] if j in s else F(i == j)-k[i][j]
                        for j in range(4)] for i in range(4)]
        p = det(atom_matrix)
        assert p == F(4, 49)*minors[mask] and p > 0
        atoms.append(p)
        atom_details.append({"subset": s, "minor": minors[mask],
                             "probability": p, "cycle_edges": edges,
                             "hinge": hinge})
    assert sum(atoms, F(0)) == 1
    delta4_log_argument = F(1)
    for s, minor in zip(SUBSETS, minors):
        delta4_log_argument *= minor**((-1)**(len(s)+1))
    assert delta4_log_argument == F(64, 81) < 1

    # Exact spectral certificate for a dense independent external contraction.
    h = list(map(F, (1, 2, 3, 4)))
    h_norm = sum(x*x for x in h)
    u = [[F(i == j)-2*h[i]*h[j]/h_norm for j in range(4)]
         for i in range(4)]
    assert mm(transpose(u), u) == eye(4)
    lam = list(map(F, ("1/7", "2/5", "3/5", "6/7")))
    external = mm(mm(u, diagonal(lam)), transpose(u))
    hinge_table = [F(max(0, len(s)-2)) for s in SUBSETS]
    hinge_mobius = mobius(hinge_table)
    assert all(hinge_mobius[m] == (1 if len(s) == 3 else
                                  -2 if len(s) == 4 else 0)
               for m, s in enumerate(SUBSETS))
    hinge_operator = exterior_operator(external, hinge_table)
    weights = []
    for pair in PAIRS:
        i, j = [i for i in range(4) if i not in pair]
        weights.append(lam[i]*(1-lam[j])+lam[j]*(1-lam[i]))
    assert all(w > 0 for w in weights)
    wu = wedge2(u)
    assert hinge_operator == mm(mm(wu, diagonal(weights)), transpose(wu))

    linked_hinge_operator = exterior_operator(k, hinge_table)
    linked_leading_minors = [det(sub(linked_hinge_operator, range(j)))
                             for j in range(1, 7)]
    assert all(x > 0 for x in linked_leading_minors)

    # All phases: symbolic Laurent determinant in rho and z=e^{i phi}.
    symbolic = [[{} for _ in range(4)] for _ in range(4)]
    for i in range(4):
        symbolic[i][i] = {(0, 0): F(1)}
    for i, j in ((0, 1), (1, 2), (2, 3)):
        symbolic[i][j] = symbolic[j][i] = {(1, 0): F(1)}
    symbolic[3][0] = {(1, 1): F(1)}
    symbolic[0][3] = {(1, -1): F(1)}
    symbolic_full = laurent_det(symbolic)
    assert symbolic_full == {(0, 0): F(1), (2, 0): F(-4),
                             (4, 0): F(2), (4, 1): F(-1), (4, -1): F(-1)}
    for s in combinations(range(4), 3):
        assert laurent_det(sub(symbolic, s)) == {(0, 0): F(1), (2, 0): F(-2)}

    # Fractional determinant-power obstruction by two independent exact formulas.
    alpha_polynomial = [F(0)]*5
    for p in permutations(range(4)):
        product = F(1)
        for i in range(4):
            product *= ell[i][p[i]]
        alpha_polynomial[cycle_count(p)] += product
    assert alpha_polynomial == list(map(F, ("0", "-1/8", "1/8", "1", "1")))
    alpha = F(1, 4)
    derivative = sum(c*alpha**j for j, c in enumerate(alpha_polynomial))
    assert derivative == fractional_power_top(minors, alpha) == F(-1, 256)

    # Finite table det(L_S)^(-1/4): rigorous elementary radical bounds.
    assert F(99, 70)**2 > 2
    assert F(19, 16)**4 < 2
    assert F(43, 40)**4 > F(4, 3)
    radical_upper_bound = F(99, 70)-4*F(19, 16)+4*F(43, 40)-1
    assert radical_upper_bound == F(-1, 28)

    result = {
        "status": "all exact checks passed",
        "L": ell, "linked_K": k,
        "atoms": atom_details,
        "fourth_log_difference": {"argument": delta4_log_argument,
                                  "sign": "negative, since 64 < 81"},
        "exterior_cancellation": {
            "hinge_mobius": hinge_mobius,
            "external_K": external,
            "orthogonal_eigenbasis": u,
            "eigenvalues": lam,
            "hinge_exterior_eigenweights": weights,
            "hinge_exterior_operator": hinge_operator,
            "linked_hinge_operator": linked_hinge_operator,
            "linked_hinge_sylvester_minors": linked_leading_minors,
        },
        "general_phase_determinant_laurent_terms": symbolic_full,
        "fractional_power": {
            "alpha_polynomial_ascending": alpha_polynomial,
            "alpha": alpha, "fourth_mixed_derivative_at_zero": derivative,
            "finite_table_fourth_difference_strict_upper_bound": radical_upper_bound,
        },
        "floating_displays_only": {
            "a": math.log(4/3), "b": math.log(9/8),
            "fourth_log_difference": math.log(64/81),
            "finite_fractional_fourth_difference": 4**0.25-4*2**0.25+4*(4/3)**0.25-1,
        },
    }
    path = OUT / "results.json"
    path.write_text(json.dumps(rational_json(result), indent=2)+"\n")
    print(json.dumps({"status": result["status"],
                      "fourth_log_argument": "64/81",
                      "fractional_power_mixed_derivative": "-1/256",
                      "hinge_operator_exact_decomposition": True,
                      "results_path": str(path)}, indent=2))


if __name__ == "__main__":
    main()
