"""Exact four-site checks for X049; decimals only illustrate log identities."""
from itertools import combinations, product
from pathlib import Path
import json
import sympy as s
import mpmath as mp

mp.mp.dps = 70
R, I = s.Rational, s.I
d = [R(9, 25), R(7, 16), R(5, 9), R(3, 4)]
c = [R(4, 5), R(3, 4), R(2, 3), R(1, 2)]
D = s.diag(*d)
V = s.Matrix([[1, 1], [1, -1], [1, I], [1, -I]]) / 2
B = s.diag(*c) * V
M = s.Matrix([[R(1, 5), (1 + I) / 30], [(1 - I) / 30, R(1, 4)]])
Mbar = R(2, 5) * s.eye(2)
K = D + B * M * B.H
H1 = B.H * (s.eye(4) - D).inv() * B
N = (M.inv() - H1).inv()
Nbar = (Mbar.inv() - H1).inv()
states = list(product([0, 1], repeat=4))
checks = 0


def eq(a, b=0):
    global checks
    if isinstance(a, s.MatrixBase):
        assert all(s.simplify(x) == 0 for x in a - b)
    else:
        assert s.simplify(a - b) == 0, (a, b)
    checks += 1


def pos2(A):
    assert A == A.H and A[0, 0] > 0 and s.simplify(A.det()) > 0


def dec(x):
    x = s.simplify(x)
    assert s.im(x) == 0
    return mp.mpf(str(s.N(x, 75)))


def atom(J, z):
    C = s.zeros(4)
    for j in range(4):
        C[:, j] = J[:, j] if z[j] else s.eye(4)[:, j] - J[:, j]
    return s.simplify(C.det())


eq(H1, s.eye(2))
eq(V.H * V, s.eye(2))
pos2(M)
pos2(Mbar - M)
pos2(M.inv() - H1)
q, T, p = {}, {}, {}
for z in states:
    q[z] = s.prod(d[i] if z[i] else 1 - d[i] for i in range(4))
    T[z] = sum(((R(z[i], 1) / d[i] - R(1-z[i], 1) / (1-d[i]))
                * B[i, :].H * B[i, :] for i in range(4)), s.zeros(2))
    p[z] = atom(K, z)
    assert p[z] > 0
    eq(p[z], q[z] * (s.eye(2) + M * T[z]).det())
eq(sum(p.values()), 1)
eq(sum((q[z] * T[z] for z in states), s.zeros(2)), s.zeros(2))
eq(sum(q[z] * T[z].det() for z in states))

L = s.simplify(K * (s.eye(4) - K).inv())
Lambda = D * (s.eye(4) - D).inv()
C = (s.eye(4) - D).inv() * B
eq(L, Lambda + C * N * C.H)
gamma = [s.simplify((B[i, :] * N * B[i, :].H)[0] / (d[i]*(1-d[i])))
         for i in range(4)]
v = [s.simplify(K[i, i]*(1-K[i, i])) for i in range(4)]
S = sum(v[i]*gamma[i]**2 for i in range(4))
rho = sum(1/di**2 for di in d) / 36
eq(rho, R(890957, 1786050))
assert S < rho < R(1, 2)
J = mp.mpf(0)
face_errors = []
for i, j in combinations(range(4), 2):
    rem = [a for a in range(4) if a not in (i, j)]
    cij = s.simplify(abs(B[[i, j], :].det())**2)
    for bits in product([0, 1], repeat=2):
        z = [0]*4
        for a, bit in zip(rem, bits):
            z[a] = bit
        zz = []
        for u, w in [(0, 0), (1, 0), (0, 1), (1, 1)]:
            z[i], z[j] = u, w
            zz.append(tuple(z))
        ratio = s.simplify(p[zz[1]]*p[zz[2]]/(p[zz[0]]*p[zz[3]]))
        Rset = [a for a, bit in zip(rem, bits) if bit]
        Q = L[[i, j], [i, j]]
        if Rset:
            Q -= L[[i, j], Rset] * L[Rset, Rset].inv() * L[Rset, [i, j]]
        eq(ratio, Q[0, 0]*Q[1, 1]/Q.det())
        P = N.inv() + sum((B[a, :].H*B[a, :]/(d[a]*(1-d[a]))
                           for a in Rset), s.zeros(2))
        NR = P.inv()
        eq(Q, Lambda[[i, j], [i, j]] + C[[i, j], :]*NR*C[[i, j], :].H)
        ell = mp.log(dec(ratio))
        bound = gamma[i]*gamma[j]/(1+gamma[i]+gamma[j])
        assert 0 <= ell < dec(bound)
        weight = s.prod(d[a] if bit else 1-d[a] for a, bit in zip(rem, bits))
        J += dec(cij*weight)*ell
        face_errors.append(abs(ell-mp.log(dec(Q[0, 0]*Q[1, 1]/Q.det()))))

# Ten fixed velocities recover all entries of the Hermitian Hessian.
basis = [s.diag(1, 0), s.diag(0, 1), s.Matrix([[0, 1], [1, 0]]),
         s.Matrix([[0, I], [-I, 0]])]
velocities = basis + [basis[i]+basis[j] for i, j in combinations(range(4), 2)]
velocities += [s.Matrix([[3, I-1], [-I-1, 3]])]
records = []
max_curvature_error = mp.mpf(0)
for E in velocities:
    A = B*E*B.H
    dp, ddp = {}, {}
    for z in states:
        dp[z] = s.simplify(q[z]*(s.trace(E*T[z])
                    + s.trace(M.adjugate()*E)*T[z].det()))
        ddp[z] = s.simplify(2*E.det()*q[z]*T[z].det())
        # The direct determinant has degree <=4. Five exact values therefore
        # prove the whole polynomial, including cancellation of degrees 3,4.
        for t in [-2, -1, 0, 1, 2]:
            eq(atom(K+t*A, z), p[z]+t*dp[z]+R(t*t, 2)*ddp[z])
    eq(sum(dp.values()))
    eq(sum(ddp.values()))
    FI = s.simplify(sum(dp[z]**2/p[z] for z in states))
    curvature = dec(FI) + sum(dec(ddp[z])*mp.log(dec(p[z])) for z in states)
    exact_reduction = dec(FI) - 2*dec(E.det())*J
    max_curvature_error = max(max_curvature_error, abs(curvature-exact_reduction))
    assert curvature >= (1-dec(S))*dec(FI) - mp.mpf('1e-60')
    if E.det() > 0:
        a = [s.simplify(A[i, i]) for i in range(4)]
        assert all(ai > 0 for ai in a)
        A0 = sum(a[i]**2/v[i] for i in range(4))
        assert FI >= A0
        for i, j in combinations(range(4), 2):
            assert E.det()*abs(B[[i,j],:].det())**2 <= a[i]*a[j]
    records.append({'det_E': str(E.det()), 'FI': mp.nstr(dec(FI), 25),
                    'negative_entropy_curvature': mp.nstr(curvature, 25)})

# Exact physical-domain, dilution, and comparable-endpoint formulas.
for k in [1, 2, 3, 6, 20]:
    tk = R(2*k, 2*k+3)
    rk = tk/(1-tk)
    eq(rk, R(2*k, 3))
    eq(sum((rk/(2*di*k*k))**2*k*k/4 for di in d), rho)
    M0 = tk*s.Matrix([[2, 1], [1, 2]])/8
    M1 = tk*s.Matrix([[5, I], [-I, 5]])/8
    for Q in [M0, M1, tk*s.eye(2)-M0, tk*s.eye(2)-M1, M1-M0]:
        pos2(Q)
    assert M0*M1 != M1*M0

G0 = sum((V[i,:].H*V[i,:]/d[i] for i in range(4)), s.zeros(2))
odds_det = {}
for k in [1, 6, 20]:
    value = (s.eye(2)+R(2*k,3)*G0).det()
    log_value = mp.log(dec(value))-sum(k*k*mp.log(1+1/(3*k*dec(di))) for di in d)
    odds_det[str(k)] = mp.nstr(mp.exp(log_value), 25)

out = {'exact_equalities': checks,
       'four_site_atoms': len(states), 'conditioned_faces': 24,
       'fixed_Hermitian_velocities': len(velocities),
       'rho': str(rho), 'S_at_fixed_base': mp.nstr(dec(S),25),
       'maximum_gaussian_face_log_error': mp.nstr(max(face_errors),5),
       'maximum_complete_curvature_identity_error': mp.nstr(max_curvature_error,5),
       'curvatures': records, 'replicated_odds_correlation_determinants': odds_det,
       'scope': 'Exact identities plus illustrative high-precision logarithms; signs proved analytically in X049.md.'}
Path(__file__).with_name('certificate.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
