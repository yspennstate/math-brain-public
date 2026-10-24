"""C041. Exact six-site exterior identities, using Python standard library only.

Run: python computations/C041/verify.py
All proof checks use Fraction/integer arithmetic. Floats occur only in a labeled
optional display of the already exactly signed logarithmic quadratic form.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import math

OUT = Path(__file__).resolve().parent
N = 6
SUBSETS = [tuple(i for i in range(N) if mask >> i & 1) for mask in range(1 << N)]
PAIRS = list(combinations(range(N), 2))
PAIR_INDEX = {p: i for i, p in enumerate(PAIRS)}
UPAIRS = list(combinations(range(4), 2))


def zero(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(A):
    return [list(r) for r in zip(*A)]


def mm(A, B):
    return [[sum((a*b for a, b in zip(row, col)), F(0)) for col in zip(*B)] for row in A]


def det(A):
    n = len(A)
    if not n:
        return F(1)
    A = [row[:] for row in A]
    ans = F(1)
    for i in range(n):
        p = next((p for p in range(i, n) if A[p][i]), None)
        if p is None:
            return F(0)
        if p != i:
            A[i], A[p] = A[p], A[i]
            ans = -ans
        pivot = A[i][i]
        ans *= pivot
        for j in range(i+1, n):
            scale = A[j][i]/pivot
            for k in range(i+1, n):
                A[j][k] -= scale*A[i][k]
    return ans


def sub(A, rows, cols):
    return [[A[i][j] for j in cols] for i in rows]


def quadratic(A, z):
    return sum((z[i]*A[i][j]*z[j] for i in range(len(z)) for j in range(len(z))), F(0))


def mobius(f):
    c = [F(a) for a in f]
    for i in range(N):
        for mask in range(1 << N):
            if mask >> i & 1:
                c[mask] -= c[mask ^ (1 << i)]
    return c


def exterior_operator(K, f):
    """Canonical second cofactor operator at rank-two real symmetric K."""
    c = mobius(f)
    T = zero(15)
    for k in range(2, 5):
        for S in combinations(range(N), k):
            coeff = c[sum(1 << i for i in S)]
            if not coeff:
                continue
            for ai in combinations(range(k), 2):
                I = tuple(S[j] for j in ai)
                rest_I = tuple(S[j] for j in range(k) if j not in ai)
                for aj in combinations(range(k), 2):
                    J = tuple(S[j] for j in aj)
                    rest_J = tuple(S[j] for j in range(k) if j not in aj)
                    T[PAIR_INDEX[I]][PAIR_INDEX[J]] += (
                        coeff * (-1)**(sum(ai)+sum(aj)) * det(sub(K, rest_I, rest_J))
                    )
    return T


def c_matrix(x, y, r, s):
    x, y, r, s = map(F, (x, y, r, s))
    A = -r+3*s+3*x+9*y
    B = r/3+2*s/3+x+3*y
    t = (s-r)/3
    return [
        [A,-r,r,-s,-s,0],
        [-r,A,-r,s,0,s],
        [r,-r,A,0,-s,-s],
        [-s,s,0,B,t,t],
        [-s,0,-s,t,B,t],
        [0,s,-s,t,t,B],
    ]


def orbit(S):
    return tuple(sorted(sum(i//2 == j for i in S) for j in range(3)))


ORBITS = {
    'a': (0,0,1), 'b': (0,0,2), 'c': (0,1,1),
    'd': (0,1,2), 'e': (1,1,1), 'f': (0,2,2), 'g': (1,1,2)
}


def charpoly(A):
    """Exact coefficients, descending, via Faddeev--LeVerrier."""
    n = len(A)
    B = eye(n)
    out = [F(1)]
    for k in range(1, n+1):
        B = mm(A, B)
        ck = -sum(B[i][i] for i in range(n))/k
        out.append(ck)
        for i in range(n):
            B[i][i] += ck
    assert B == zero(n)
    return out


def polymul(a, b):
    c = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def polyproduct(factors):
    out = [F(1)]
    for f in factors:
        out = polymul(out, list(map(F, f)))
    return out


def exact_json(obj):
    if isinstance(obj, F):
        return str(obj)
    if isinstance(obj, dict):
        return {str(k):exact_json(v) for k,v in obj.items()}
    if isinstance(obj, (tuple, list)):
        return [exact_json(v) for v in obj]
    return obj


def main():
    # Original odds pairs: 01 | 23 | 45. Projection pairs: 03 | 14 | 25.
    P = [[F(1,2)*(F(i%3 == j%3)-F(1,3)) for j in range(6)] for i in range(6)]
    U = [[F(1)] + [F(i == j)-F(i == j+3) for j in range(3)] for i in range(6)]
    Q = [[det(sub(U, I, J)) for J in UPAIRS] for I in PAIRS]
    assert mm(P, P) == P
    assert sum(P[i][i] for i in range(6)) == 2
    assert mm(P, U) == zero(6, 4)
    assert mm(transpose(U), U) == [[F([6,2,2,2][i]) if i == j else F(0) for j in range(4)] for i in range(4)]
    assert all(P[i][j] != 0 for i in range(6) for j in range(6) if i != j)

    operator_coefficients = {}
    witness_coefficients = {}
    z = list(map(F, [0,-1,0,1,-1,1,-1,0,1,0,-1,0,1,-1,0]))
    for name, shape in ORBITS.items():
        values = [F(orbit(S) == shape) for S in SUBSETS]
        T = exterior_operator(P, values)
        operator_coefficients[name] = T
        witness_coefficients[name] = quadratic(T, z)
        compressed = mm(mm(transpose(Q), T), Q)
        v = {k:F(k == name) for k in ORBITS}
        x = v['b']+v['g']-2*v['d']
        y = v['c']+v['g']-v['d']-v['e']
        r = v['d']-v['e']
        s = v['f']-v['g']
        assert compressed == c_matrix(x, y, r, s), name
    assert witness_coefficients == dict(a=F(-13),b=F(-5,4),c=F(35,4),d=F(-3,2),e=F(-3,2),f=F(1),g=F(3,4))
    # One Pluecker relation already proves this negative-test form is not simple.
    plucker = z[PAIR_INDEX[(0,1)]]*z[PAIR_INDEX[(2,3)]]-z[PAIR_INDEX[(0,2)]]*z[PAIR_INDEX[(1,3)]]+z[PAIR_INDEX[(0,3)]]*z[PAIR_INDEX[(1,2)]]
    assert plucker == -1

    rays = [
        ((0,1,1,0), [[1,-10],[1,-7],[1,-7],[1,F(-8,3)],[1,F(-11,3)],[1,F(-11,3)]]),
        ((0,1,-1,0), [[1,-8],[1,-11],[1,-11],[1,F(-10,3)],[1,F(-7,3)],[1,F(-7,3)]]),
        ((0,0,1,1), [[1,0],[1,0],[1,0],[1,-5],[1,-2],[1,-2]]),
        ((0,0,0,1), [[1,0],[1,0],[1,0],[1,F(-13,3)],[1,F(-10,3)],[1,F(-10,3)]]),
        ((2,1,-1,-2), [[1,F(-32,3),F(16,3)],[1,F(-44,3),F(109,3)],[1,F(-44,3),F(109,3)]]),
        ((1,0,0,0), [[1,-3],[1,-3],[1,-3],[1,-1],[1,-1],[1,-1]]),
    ]
    ray_records = []
    for ray, factors in rays:
        C = c_matrix(*ray)
        cp = charpoly(C)
        assert cp == polyproduct(factors)
        ray_records.append(dict(ray=ray, matrix=C, characteristic_polynomial=cp, factors=factors))
    # Check the explicit conic decomposition algebra on representative exact cases.
    for x,y,r,s in [(2,3,F(3,2),1),(2,1,2,3),(2,1,F(-1,2),-1),(4,2,-1,-2),(0,0,0,0)]:
        x,y,r,s = map(F,(x,y,r,s))
        assert min(x,y,x+s,y+r,y+s-r) >= 0
        if s >= 0:
            t = max(F(0),r-y)
            coeff = [(y+r-t)/2,(y-r+t)/2,t,s-t,F(0),x]
        else:
            h = -s
            coeff = [(y+r)/2,(y-r-h)/2,F(0),F(0),h/2,x-h]
        assert min(coeff) >= 0
        assert [sum(coeff[j]*rays[j][0][i] for j in range(6)) for i in range(4)] == [x,y,r,s]

    eps = F(1,100)
    L0 = [[F(2 if i//2 == j//2 else -1) for j in range(6)] for i in range(6)]
    L = [[L0[i][j]+eps*F(i == j) for j in range(6)] for i in range(6)]
    assert mm(L0,L0) == [[6*x for x in row] for row in L0]
    assert sum(L0[i][i] for i in range(6)) == 12
    # Thus L0 has eigenvalues 6 (twice), 0 (four times), and L>0 exactly.
    minors = []
    for S in SUBSETS:
        m = [sum(i//2 == j for i in S) for j in range(3)]
        k = len(S)
        formula = eps**k*(1+F(2*k)/eps+3*sum(m[i]*m[j] for i,j in combinations(range(3),2))/eps**2)
        actual = det(sub(L,S,S))
        assert actual == formula and actual > 0
        minors.append(dict(subset=S, class_counts=m, determinant=actual))
    # Exact logarithmic witness, exp(4 <z,T z>) = R. No floating sign test.
    R = F(201**48*401**5*60601**6,101**35*301**26*601**4*501**3)
    orbit_dets = {name: next(v['determinant'] for v in minors if orbit(v['subset']) == shape) for name,shape in ORBITS.items()}
    R_from_minors = F(1)
    for name, coeff in witness_coefficients.items():
        exponent = -4*coeff  # f = -log det
        assert exponent.denominator == 1
        R_from_minors *= orbit_dets[name]**int(exponent)
    assert R == R_from_minors
    assert 32*R.numerator < R.denominator
    # Opposite triangle-product signs exclude both diagonal +/- rank-one odds
    # and diagonal-unitary gauges to Stieltjes matrices.
    triangle_products = {
        'two_sites_in_one_class':L[0][1]*L[1][2]*L[2][0],
        'one_site_in_each_class':L[0][2]*L[2][4]*L[4][0],
    }
    assert triangle_products == dict(two_sites_in_one_class=F(2),one_site_in_each_class=F(-1))
    cert = dict(status='PASS', arithmetic='exact Python fractions and integers',
        original_pairs=[[0,1],[2,3],[4,5]], projection_pairs=[[0,3],[1,4],[2,5]],
        projection=P, complement_basis=U, exterior_pair_order=PAIRS,
        complement_exterior_pair_order=UPAIRS, wedge_embedding=Q,
        orbit_shapes=ORBITS, full_operator_orbit_coefficients=operator_coefficients,
        ray_certificates=ray_records, epsilon=eps, odds=L, principal_minors=minors,
        witness=z, plucker_0123=plucker, witness_log_table_coefficients=witness_coefficients,
        exp_four_times_witness=R, exact_inequality='32 * numerator < denominator',
        triangle_products=triangle_products,
        illustrative_witness_decimal=math.log(float(R))/4)
    (OUT/'certificate.json').write_text(json.dumps(exact_json(cert),indent=2)+'\n')
    summary = dict(status='PASS', canonical_matrix_identity='all seven independent orbit tables',
        ray_characteristic_polynomials='all six, exact', principal_minor_checks=64,
        projection_rank=2, projection_all_off_diagonal_nonzero=True,
        nondecomposable_witness_plucker='-1', log_witness_bound='< -(5/4) log 2',
        illustrative_log_witness=math.log(float(R))/4,
        external_or_frozen_odds_link='independent; no linked physical entropy counterexample')
    (OUT/'verified_output.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__ == '__main__':
    main()
