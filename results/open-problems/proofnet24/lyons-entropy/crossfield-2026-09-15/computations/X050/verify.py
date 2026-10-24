"""Exact logarithmic certificate plus independent complete atom-Hessian check.

No random search, external theorem, or floating-point positivity certificate.
The strong witness's inequalities use Fraction arithmetic and an explicit
geometric-series remainder. Numerical Hessians only check the derived identities.
"""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import json
import numpy as np
import sympy as sp

OUT = Path(__file__).with_name('results.json')
I4 = sp.eye(4)
C = sp.Matrix([[sp.Rational(19, 20), sp.Rational(3, 100)],
               [sp.I / 50, sp.Rational(7, 10)]])
Z = C / 2
K = I4 / 2
K[:2, 2:] = Z
K[2:, :2] = Z.conjugate().T
spins = list(product((-1, 1), repeat=4))

def frac(x):
    x = sp.Rational(x)
    return F(int(x.p), int(x.q))

def add(a, b):
    return a[0] + b[0], a[1] + b[1]

def scale(a, c):
    return (c*a[0], c*a[1]) if c >= 0 else (c*a[1], c*a[0])

def log_unit(u, terms=24):
    assert 1 <= u <= 2
    t = (u-1)/(u+1)
    value = sum((2*t**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
    tail = 2*t**(2*terms+1)/(F(2*terms+1)*(1-t*t))
    return value, value+tail

def log_interval(q):
    assert q > 0
    exponent = 0
    while q < 1:
        q *= 2
        exponent -= 1
    while q >= 2:
        q /= 2
        exponent += 1
    return add(log_unit(q), scale(log_unit(F(2)), F(exponent)))

densities = []
f_intervals = []
for signs in spins:
    q = 1 + abs(C.det())**2 * int(np.prod(signs))
    for i in range(2):
        for j in range(2):
            q -= abs(C[i,j])**2 * signs[i] * signs[j+2]
    densities.append(frac(q))
    f_intervals.append(scale(log_interval(frac(q)), F(-1)))

alpha = [[(F(0), F(0)) for _ in range(4)] for _ in range(4)]
for i, j in combinations(range(4), 2):
    value = (F(0), F(0))
    for signs, interval in zip(spins, f_intervals):
        value = add(value, scale(interval, F(signs[i]*signs[j], 4)))
    alpha[i][j] = alpha[j][i] = value

tau = (F(0), F(0))
for signs, interval in zip(spins, f_intervals):
    tau = add(tau, scale(interval, F(int(np.prod(signs)))))
assert F(1302, 10**6) < tau[0] < tau[1] < F(1303, 10**6)

# Coarse rational endpoint table used in the written certificate.
table = {(0,1):22764, (0,2):5942485, (0,3):30565,
         (1,2):22651, (1,3):2144568, (2,3):28617}
for (i,j), lo in table.items():
    assert F(lo, 10**6) < alpha[i][j][0]
    assert alpha[i][j][1] < F(lo+1, 10**6)

# ||C||op^2 <= ||C||1 ||C||infinity <= (97/100)(98/100) < 24/25.
# Therefore ||Z||op^2 < gamma=6/25. Both norms are sums of exact moduli.
gamma = F(6, 25)
assert F(97,100)*F(98,100) < 4*gamma
Sigma = sp.eye(4)/4
for i in range(4):
    for j in range(4):
        if i != j:
            Sigma[i,j] = -abs(K[i,j])**2
Sinv = Sigma.inv()
row_lower = []
for i in range(4):
    bound = frac(Sinv[i,i]) - tau[1]*gamma
    for j in range(4):
        if i != j:
            interval = add((frac(Sinv[i,j]),)*2, scale(alpha[i][j], F(-1)))
            bound -= max(abs(interval[0]), abs(interval[1]))
    row_lower.append(bound)
assert all(b > F(24,5) for b in row_lower)
assert all(alpha[i][j][0]-tau[1]/4 > F(1,50)
           for i,j in combinations(range(4),2))

# Exact determinant acceleration identity in a general complex within-block
# direction. It is checked coefficientwise in t, including the quartic term.
U = sp.Matrix([[sp.Rational(2,7), sp.Rational(1,5)+sp.I/9],
               [sp.Rational(1,5)-sp.I/9, -sp.Rational(3,11)]])
V = sp.Matrix([[-sp.Rational(1,6), -sp.Rational(2,9)+sp.I/13],
               [-sp.Rational(2,9)-sp.I/13, sp.Rational(4,15)]])
A0 = sp.diag(U,V)
Q = Z.adjugate()
t = sp.Symbol('t', real=True)
quartic = sp.expand((K-I4/2+t*A0).det())
assert sp.simplify(quartic-(abs(Z.det())**2
    -t*t*sp.trace(Q.conjugate().T*V*Q*U)+t**4*U.det()*V.det())) == 0

# Independent signed-column atom probabilities and exact first/second jets.
exact_jets = []
for signs, density in zip(spins, densities):
    M = sp.zeros(4)
    D = sp.zeros(4)
    for j in range(4):
        M[:,j] = K[:,j] if signs[j] == 1 else (I4-K)[:,j]
        D[:,j] = signs[j]*A0[:,j]
    p = sp.simplify(M.det())
    assert frac(p) == density/16
    dp = 0
    ddp = 0
    for j in range(4):
        R = M.copy()
        R[:,j] = D[:,j]
        dp += R.det()
    for i,j in combinations(range(4),2):
        R = M.copy()
        R[:,i], R[:,j] = D[:,i], D[:,j]
        ddp += 2*R.det()
    exact_jets.append((sp.simplify(dp), sp.simplify(ddp)))
assert sum(a for a,b in exact_jets) == 0
assert sum(b for a,b in exact_jets) == 0
for mask in range(1,16):
    indices = [i for i in range(4) if mask >> i & 1]
    lhs = sum(ddp*sp.prod(sp.Rational(signs[i],2) for i in indices)
              for signs,(dp,ddp) in zip(spins,exact_jets))
    sub = (K-I4/2+t*A0).extract(indices,indices)
    rhs = sp.diff(sub.det(),t,2).subs(t,0)
    assert sp.simplify(lhs-rhs) == 0

# Complete numerical Hessian, calculated directly from all sixteen atoms.
Kn = np.array(K, dtype=complex)
basis = []
labels = []
for i in range(4):
    B = np.zeros((4,4),complex); B[i,i] = 1
    basis.append(B); labels.append(('diag',i,i))
for i,j in combinations(range(4),2):
    for im in (False,True):
        B = np.zeros((4,4),complex)
        B[i,j] = (1j if im else 1)/np.sqrt(2)
        B[j,i] = B[i,j].conjugate()
        basis.append(B); labels.append(('edge',i,j))
Hess = np.zeros((16,16))
Fisher = np.zeros((16,16))
frozen = np.zeros((16,16))
for signs in spins:
    signs = np.array(signs)
    M = np.column_stack([Kn[:,j] if signs[j] == 1 else (np.eye(4)-Kn)[:,j]
                         for j in range(4)])
    p = np.linalg.det(M).real
    Minv = np.linalg.inv(M)
    R = np.array([Minv@(B*signs[np.newaxis,:]) for B in basis])
    traces = np.trace(R,axis1=1,axis2=2)
    dp = p*traces.real
    ddp = p*(np.outer(traces,traces)-np.einsum('aij,bji->ab',R,R)).real
    Fisher += np.outer(dp,dp)/p
    frozen += ddp*np.log(p)
Hess = -Fisher-frozen
cross = [i for i,z in enumerate(labels) if z[0]=='edge' and z[1]<2<=z[2]]
within = [i for i in range(16) if i not in cross]
mixed_residual = float(np.max(np.abs(Hess[np.ix_(cross,within)])))
assert mixed_residual < 1e-11
assert np.max(np.linalg.eigvalsh(Hess)) < -1/50
an = np.array([sum(a)/2 for row in alpha for a in row],float).reshape(4,4)
taun = float(sum(tau)/2)
Un, Vn = np.array(U,complex), np.array(V,complex)
A0n = np.array(A0,complex)
diag = np.diag(A0n).real
Qn = np.array(Q,complex)
expected_frozen = -diag@an@diag + an[0,1]*np.linalg.norm(Un-np.diag(np.diag(Un)))**2
expected_frozen += an[2,3]*np.linalg.norm(Vn-np.diag(np.diag(Vn)))**2
expected_frozen += 2*taun*np.trace(Qn.conj().T@Vn@Qn@Un).real
coords = np.array([np.trace(B@A0n).real for B in basis])
frozen_residual = abs(coords@frozen@coords-expected_frozen)
assert frozen_residual < 1e-11

result = {
    'status':'PASS',
    'certificate_arithmetic':'Exact rational, 24 positive log-series terms plus remainder',
    'alpha_microintervals':{f'{i+1}{j+1}':[lo,lo+1] for (i,j),lo in table.items()},
    'tau_microinterval':[1302,1303],
    'certified_minimum_diagonal_dominance':'24/5',
    'certified_minimum_alpha_minus_tau_over_four':'1/50',
    'certified_full_hessian_upper_bound':'-1/50 times Frobenius norm squared',
    'numerical_singular_values_squared':np.linalg.svd(np.array(C,complex),compute_uv=False).__pow__(2).tolist(),
    'numerical_full_hessian_eigenvalues':np.linalg.eigvalsh(Hess).tolist(),
    'numerical_diagonal_dominance_lower_bounds':[float(v) for v in row_lower],
    'mixed_sector_residual':mixed_residual,
    'complete_frozen_acceleration_residual':float(frozen_residual),
    'exact_atom_jets_and_all_centered_moments':'PASS',
    'exact_determinant_polynomial':'PASS',
}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
