import itertools
import math
import numpy as np

SEED = 20260916014911
rng = np.random.default_rng(SEED)

def psd(d, eps=1e-4):
    X = rng.normal(size=(d,d)) + 1j*rng.normal(size=(d,d))
    A = X @ X.conj().T
    A /= np.linalg.norm(A, 2)
    A += eps*np.eye(d)
    A *= 10.0**rng.uniform(-1.0,1.0)
    return A

def op(A):
    return float(np.linalg.norm(A, 2))

def mpow(A,s):
    w,V = np.linalg.eigh(A)
    w = np.maximum(w,0.0)
    return (V*(w**s)) @ V.conj().T

def rho_prod(A,B):
    Bh = mpow(B,0.5)
    return op(Bh @ A @ Bh)

def word_norm(A,B,mask,n):
    W = np.eye(A.shape[0], dtype=complex)
    for k in range(n):
        W = W @ (A if k in mask else B)
    return op(W)

min_joint = float('inf')
min_bridge = float('inf')
min_occ = float('inf')
min_bal = float('inf')

for d in (2,3,5):
    for _ in range(80):
        A,B = psd(d), psd(d)
        # Joint log-convexity diagnostic.
        x0,y0 = rng.uniform(0.0,2.0,2)
        x1,y1 = rng.uniform(0.0,3.0,2)
        th = rng.uniform(0.0,1.0)
        lhs = op(mpow(A,(1-th)*x0+th*x1) @ mpow(B,(1-th)*y0+th*y1))
        g0 = op(mpow(A,x0) @ mpow(B,y0))
        g1 = op(mpow(A,x1) @ mpow(B,y1))
        rhs = g0**(1-th) * g1**th
        assert lhs <= rhs*(1+5e-10) + 1e-12
        min_joint = min(min_joint, rhs/max(lhs,1e-300))

        p = op(A@B)
        rho = rho_prod(A,B)
        b = op(B)
        if p < 1e-14:
            continue
        for r,s in ((2,1),(3,1),(3,2),(4,1),(4,2),(4,3),(5,2)):
            lhs_bridge = rho_prod(mpow(A,r),mpow(B,s))
            rhs_bridge = p**(2*r-2)/(rho**(r-2)*b**(r-s))
            assert lhs_bridge + 1e-10*max(1.0,lhs_bridge) >= rhs_bridge
            min_bridge = min(min_bridge, lhs_bridge/max(rhs_bridge,1e-300))

for d in (2,3,4):
    for _ in range(30):
        A,B = psd(d), psd(d)
        p = op(A@B)
        rho = rho_prod(A,B)
        b = op(B)
        for r,s in ((2,1),(3,1),(3,2),(4,1),(4,2),(4,3)):
            n = r+s
            total = 0.0
            for apos in itertools.combinations(range(n),r):
                total += word_norm(A,B,set(apos),n)
            cyc_bound = n*p**(2*r-2)/(rho**(r-2)*b**(r-s))
            assert total + 1e-10*max(1.0,total) >= cyc_bound
            min_occ = min(min_occ, total/max(cyc_bound,1e-300))

        for m in (3,4):
            total = 0.0
            for apos in itertools.combinations(range(2*m),m):
                total += word_norm(A,B,set(apos),2*m)
            bal_bound = 2*(m+1)*p**m
            assert total + 1e-10*max(1.0,total) >= bal_bound
            min_bal = min(min_bal,total/max(bal_bound,1e-300))

# Exact coefficient checks for the aggregate consequence.
assert math.isclose((3+1)/math.factorial(4), 1/6)
assert math.isclose((4+1)/math.factorial(6), 1/144)
assert math.isclose((5+1)/math.factorial(8), 1/6720)

print(f"seed={SEED}")
print(f"min joint-logconvex ratio rhs/lhs = {min_joint:.16g}")
print(f"min unbalanced spectral bridge ratio = {min_bridge:.16g}")
print(f"min complete unbalanced occupancy / cyclic bound = {min_occ:.16g}")
print(f"min complete balanced occupancy / [2(m+1)||AB||^m] = {min_bal:.16g}")
print("all deterministic corroborative checks passed")
