"""
PROB20-07 exploratory complex-spectrum diagnostic, run 2026-09-15T170307Z.

STATUS: numerical evidence only, NOT a proof.

At endpoint floor a=1/12:
1. Enumerate all 3^6 deterministic symmetric residual kernels.
2. Numerically solve their fixed-point equations from a bounded grid.
3. Record the largest observed det(T), where
       T_{jk} = sum_i x_i P_{ij,k}.
4. Run a small seeded SLSQP search over continuous residual rows and the fixed-point
   constraint to maximize det(R), where T = a*ones + b*R and det(T)=b^2 det(R).

Requires numpy/scipy.
"""

import itertools
import numpy as np
from scipy.optimize import root, minimize

a = 1.0/12.0
b = 3.0/4.0

pairs = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
pair_index = {p:i for i,p in enumerate(pairs)}
maps = np.array(list(itertools.product(range(3), repeat=6)), dtype=int)

def residual_W(x, m):
    out = np.zeros(3)
    for i in range(3):
        for j in range(3):
            out[m[pair_index[tuple(sorted((i,j)))]]] += x[i]*x[j]
    return out

def residual_R(x, m):
    R = np.zeros((3,3))
    for j in range(3):
        for i in range(3):
            R[j, m[pair_index[tuple(sorted((i,j)))]]] += x[i]
    return R

def V12(z, m):
    x = np.array([z[0], z[1], 1-z[0]-z[1]])
    y = a*np.ones(3) + b*residual_W(x,m)
    return y[:2]

starts = [
    np.array([u,v])
    for u in np.linspace(0.09,0.82,5)
    for v in np.linspace(0.09,0.82,5)
    if u+v < 0.91
]

best_det_T = -1.0
best_record = None
fixed_count = 0

for m in maps:
    sols = []
    for st in starts:
        rr = root(lambda z: V12(z,m)-z, st)
        if not rr.success:
            continue
        z = rr.x
        x = np.array([z[0], z[1], 1-z.sum()])
        if np.any(x < a-1e-7) or np.any(x > 1+1e-7):
            continue
        if any(np.linalg.norm(x-y) < 1e-6 for y in sols):
            continue
        sols.append(x)

    for x in sols:
        fixed_count += 1
        R = residual_R(x,m)
        T = a*np.ones((3,3)) + b*R
        d = np.linalg.det(T)
        if d > best_det_T:
            best_det_T = d
            best_record = (x.copy(), m.copy(), R.copy(), T.copy(), np.linalg.eigvals(T))

print("deterministic residual fixed points recovered:", fixed_count)
print("largest observed det(T):", best_det_T)
if best_record is not None:
    x,m,R,T,eig = best_record
    print("best fixed point:", x)
    print("best deterministic map:", m)
    print("R=\n", R)
    print("T eigenvalues:", eig)

# Continuous SLSQP search.
def unpack(z):
    x = np.array([z[0], z[1], 1-z[0]-z[1]])
    Q = np.zeros((6,3))
    for t in range(6):
        q1,q2 = z[2+2*t:4+2*t]
        Q[t] = [q1,q2,1-q1-q2]
    return x,Q

def R_from_Q(x,Q):
    R = np.zeros((3,3))
    for j in range(3):
        for i in range(3):
            R[j] += x[i]*Q[pair_index[tuple(sorted((i,j)))]]
    return R

def W_from_Q(x,Q):
    out = np.zeros(3)
    for i in range(3):
        for j in range(3):
            out += x[i]*x[j]*Q[pair_index[tuple(sorted((i,j)))]]
    return out

def objective(z):
    x,Q = unpack(z)
    return -np.linalg.det(R_from_Q(x,Q))

def fixed_eq(z):
    x,Q = unpack(z)
    return (a*np.ones(3)+b*W_from_Q(x,Q)-x)[:2]

def nonnegative(z):
    x,Q = unpack(z)
    vals = list(x-a)
    vals.extend(Q.ravel())
    return np.array(vals)

best_cont = -1.0
for seed in range(15):
    rng = np.random.default_rng(seed)
    x0 = a + b*rng.dirichlet(np.ones(3))
    Q0 = rng.dirichlet(np.ones(3), size=6)
    z0 = np.r_[x0[:2], Q0[:,:2].ravel()]
    rr = minimize(
        objective,
        z0,
        method="SLSQP",
        constraints=[
            {"type":"eq", "fun":fixed_eq},
            {"type":"ineq", "fun":nonnegative},
        ],
        options={"maxiter":1500, "ftol":1e-11, "disp":False},
    )
    if rr.success:
        best_cont = max(best_cont, -rr.fun)

print("largest continuous-search det(R):", best_cont)
print("corresponding det(T) scale b^2*det(R):", b*b*best_cont)
print("reference values: 1/3 =", 1/3, "; 3/16 =", 3/16)
