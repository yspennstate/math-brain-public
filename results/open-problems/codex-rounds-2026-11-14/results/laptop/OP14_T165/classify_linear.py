"""Exact LCP audit: principal supports versus independent vertex enumeration.

Run through run_limited.py. Only Python's standard library is used.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
import json
from pathlib import Path
import time

START = time.monotonic()

def matrix(m, a, b, c, d):
    n = m + 2
    R = [[F(1) for _ in range(n)] for _ in range(n)]
    for i in range(1, n - 1):
        R[0][i] += b
        R[i][-1] -= c
        R[-1][i] -= c
        for j in range(1, n - 1):
            if i != j:
                R[i][j] -= c
    R[0][-1] -= d
    R[-1][0] += a
    return R

def det(A):
    """Leibniz expansion, independent of Gaussian elimination."""
    n = len(A)
    ans = F(0)
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = F((-1) ** inversions)
        for i in range(n):
            term *= A[i][p[i]]
        ans += term
    return ans

def solve(A, rhs):
    """Exact Gauss-Jordan elimination; None means singular."""
    n = len(rhs)
    M = [list(row) + [rhs[i]] for i, row in enumerate(A)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if M[i][j]), None)
        if pivot is None:
            return None
        M[j], M[pivot] = M[pivot], M[j]
        scale = M[j][j]
        M[j] = [v / scale for v in M[j]]
        for i in range(n):
            if i != j:
                scale = M[i][j]
                M[i] = [x - scale * y for x, y in zip(M[i], M[j])]
    return tuple(M[i][-1] for i in range(n))

def velocity(R, u):
    return tuple(sum(x * y for x, y in zip(row, u)) - 1 for row in R)

def principal_supports(R, save_rows=False):
    n = len(R)
    answers, rows, singular = set(), [], []
    for mask in range(1 << n):
        S = [i for i in range(n) if mask >> i & 1]
        A = [[R[i][j] for j in S] for i in S]
        x = solve(A, [F(1)] * len(S))
        determinant = det(A)
        assert (x is None) == (determinant == 0)
        if x is None:
            singular.append([i + 1 for i in S])
            continue
        u = tuple(x[S.index(i)] if i in S else F(0) for i in range(n))
        v = velocity(R, u)
        valid = min(u + v) >= 0 and all(u[i] * v[i] == 0 for i in range(n))
        if valid:
            answers.add((u, v))
        if save_rows:
            rows.append(dict(support=[i + 1 for i in S], determinant=str(determinant),
                             u=list(map(str, u)), v=list(map(str, v)), valid=valid))
    return answers, rows, singular

def vertices(R):
    """Enumerate vertices of {u>=0, Ru>=1} by Cramer's rule.

    Choose any n of the 2n bounding hyperplanes, independently of an LCP support.
    Filter resulting feasible vertices for complementarity afterward.
    """
    n = len(R)
    equations = [(tuple(F(int(i == j)) for j in range(n)), F(0)) for i in range(n)]
    equations += [(tuple(row), F(1)) for row in R]
    answers = set()
    checked = 0
    for choice in combinations(range(2 * n), n):
        A = [equations[i][0] for i in choice]
        rhs = [equations[i][1] for i in choice]
        denominator = det(A)
        if denominator == 0:
            continue
        checked += 1
        u = []
        for j in range(n):
            B = [list(row) for row in A]
            for i in range(n):
                B[i][j] = rhs[i]
            u.append(det(B) / denominator)
        u = tuple(u)
        v = velocity(R, u)
        if min(u + v) >= 0 and all(x * y == 0 for x, y in zip(u, v)):
            answers.add((u, v))
    return answers, checked

def predicted(m, a, b, c, d):
    n = m + 2
    first_u = (F(1),) + (F(0),) * (n - 1)
    first_v = (F(0),) * (n - 1) + (a,)
    q = d - m * (b + c)
    if q <= 0:
        w = 1 / (m + 1 - m * c)
        u = (F(0),) + (w,) * (m + 1)
        v = (-q * w,) + (F(0),) * (m + 1)
    else:
        A = m - (m - 1) * c
        B = m * b + (m - 1) * c
        D = c * q + a * (A * (d - c) + (1 - c) * B)
        u = (c * q / D,) + (a * (d - c) / D,) * m + (a * B / D,)
        v = (F(0),) * n
    return {(first_u, first_v), (u, v)}

def serialize(pairs):
    return [dict(u=list(map(str, u)), v=list(map(str, v))) for u, v in sorted(pairs)]

def main():
    a = b = c = F(1, 20)
    R = matrix(2, a, b, c, F(3, 5))
    found, supports, singular = principal_supports(R, True)
    independent, count = vertices(R)
    assert not singular
    assert found == independent == predicted(2, a, b, c, F(3, 5))
    assert det(R) == F(323, 80000)
    assert ((F(80, 323), F(110, 323), F(110, 323), F(30, 323)), (F(0),) * 4) in found
    print("Heyda d=4: 16 principal supports; 0 singular; 2 distinct LCP solutions.")
    for pair in serialize(found):
        print("u=" + ",".join(pair["u"]) + "; v=" + ",".join(pair["v"]))
    print("det(R)=323/80000; independent vertex enumeration agrees.")

    # Both sides and equality at q=0, including strongly asymmetric parameters.
    cases = []
    for m in (1, 2, 3):
        for aa, bb, cc in product((F(1, 20), F(2, 5)), (F(1, 40), F(1, 10)), (F(1, 20), F(1, 5))):
            critical = m * (bb + cc)
            for dd in (critical / 2, critical, (1 + critical) / 2):
                if not 0 < dd < 1:
                    continue
                rr = matrix(m, aa, bb, cc, dd)
                observed, _, bad = principal_supports(rr)
                # A singular excluded support cannot be resolved by this enumerator;
                # the symbolic proof is what covers those cases in general.
                assert not bad, (m, aa, bb, cc, dd, bad)
                assert observed == predicted(m, aa, bb, cc, dd)
                cases.append(dict(m=m, a=str(aa), b=str(bb), c=str(cc), d=str(dd),
                                  regime="below" if dd < critical else "equal" if dd == critical else "above",
                                  solutions=serialize(observed)))
    independent_cases = []
    for m in (1, 2, 3):
        critical = m * (b + c)
        for dd in (critical / 2, critical, (1 + critical) / 2):
            rr = matrix(m, a, b, c, dd)
            answer, checked = vertices(rr)
            assert answer == predicted(m, a, b, c, dd)
            independent_cases.append(dict(m=m, d=str(dd), nonsingular_vertices=checked,
                                          solutions=serialize(answer)))
    print(f"Parameter audit: {len(cases)} exact cases in dimensions 3,4,5; all agree with the formula.")
    print(f"Independent Cramer/vertex audit: {len(independent_cases)} threshold/below/above cases; all agree.")
    data = dict(fixed_matrix=[[str(x) for x in row] for row in R],
                fixed_supports=supports, fixed_solutions=serialize(found),
                fixed_vertex_systems=count, parameter_cases=cases, independent_cases=independent_cases)
    Path("linear_fluid_data.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print("Saved linear_fluid_data.json")
    print(f"Elapsed seconds: {time.monotonic() - START:.3f}")

if __name__ == "__main__":
    main()
