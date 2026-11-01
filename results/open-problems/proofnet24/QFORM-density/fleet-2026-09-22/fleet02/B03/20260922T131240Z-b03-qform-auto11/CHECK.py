import itertools
import sympy as sp


def family(m):
    n = 2*m + 1
    U = sp.zeros(n, 3)
    U[0, 0] = 1
    a = sp.sqrt(sp.Rational(1, m))
    for j in range(m):
        U[1+j, 1] = a
        U[1+m+j, 2] = a
    Lam = sp.diag(1, 1, -1)
    A = sp.simplify(U*Lam*U.T)
    return U, A


def check(m):
    U, A = family(m)
    n = U.rows
    assert sp.simplify(U.T*U) == sp.eye(3)
    assert A.rank() == 3
    ev = A.eigenvals()
    assert ev.get(sp.Integer(1), 0) == 2
    assert ev.get(sp.Integer(-1), 0) == 1
    assert ev.get(sp.Integer(0), 0) == 2*m-2

    weights = {}
    for I in itertools.combinations(range(n), 3):
        d = sp.simplify(U[list(I), :].det())
        if d != 0:
            weights[I] = sp.simplify(d*d)
    assert len(weights) == m*m
    assert set(weights.values()) == {sp.Rational(1, m*m)}
    assert sp.simplify(sum(weights.values())) == 1
    R = sp.Integer(0)
    for I,wI in weights.items():
        for J,wJ in weights.items():
            if set(I).isdisjoint(J):
                R += wI*wJ
    assert sp.simplify(R) == 0

    lev = [sp.simplify((U[i,:]*U[i,:].T)[0]) for i in range(n)]
    kappa = sp.simplify(1-sum(x*x for x in lev))
    assert kappa == -sp.Rational(2,m)

    sigmas = []
    dets = []
    for I in itertools.combinations(range(n), 3):
        B = A.extract(I,I)
        if B.det() != 0:
            dets.append(sp.simplify(B.det()))
            eigabs = [abs(x) for x in B.eigenvals().keys()]
            sigmas.append(min(eigabs))
    assert sigmas and set(sigmas) == {sp.Rational(1,m)}
    assert set(dets) == {-sp.Rational(1,m*m)}
    for I in itertools.combinations(range(n), 4):
        assert A.extract(I,I).det() == 0

    max_cross_rank = 0
    # Fix the hub on the S side to quotient out complement symmetry.
    for mask in range(1 << (n-1)):
        S = [0] + [i+1 for i in range(n-1) if (mask >> i) & 1]
        T = [i for i in range(1,n) if i not in S]
        if not T:
            continue
        r = A.extract(S,T).rank()
        max_cross_rank = max(max_cross_rank, r)
    assert max_cross_rank <= 2

    c2 = sp.simplify((sp.Rational(m,m-1))**(m-1))
    print(f"m={m} n={n} spectrum={{1x2,-1x1,0x{2*m-2}}} bases={len(weights)} "
          f"max_w={sp.Rational(1,m*m)} R={R} kappa={kappa} "
          f"principal_sigma_min={sp.Rational(1,m)} max_cross_rank={max_cross_rank} c_m^2={c2}")


for m in range(2,6):
    check(m)
print("STATUS=PASS")
