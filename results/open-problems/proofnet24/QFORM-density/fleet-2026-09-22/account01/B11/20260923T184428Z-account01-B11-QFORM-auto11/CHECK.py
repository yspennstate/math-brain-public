import math
import numpy as np

rng = np.random.default_rng(20260923)
mx = 0.0
for _ in range(1000):
    O, _ = np.linalg.qr(rng.normal(size=(2, 2)))
    ev = 1/32 + 0.8*rng.random(2)
    W = O @ np.diag(ev) @ O.T
    q = rng.normal(size=2)
    c = 63/64 + (1-63/64)*rng.random()
    beta = (0.2+rng.random()) * (1 if rng.random()<0.5 else -1)
    gamma = rng.normal()
    delta = rng.normal()
    lam = (0.2+rng.random()) * (1 if rng.random()<0.5 else -1)
    M = np.array([[0,beta,0],[beta,gamma,delta],[0,delta,lam]], dtype=float)
    vals, vecs = np.linalg.eigh(W)
    Wsqrt = vecs @ np.diag(np.sqrt(vals)) @ vecs.T
    C = np.block([[np.array([[math.sqrt(c)]]), q.reshape(1,2) @ Wsqrt],
                  [np.zeros((2,1)), Wsqrt]])
    H = C.T @ M @ C
    lhs = np.linalg.det(H)
    rhs = c*np.linalg.det(W)*np.linalg.det(M)
    mx = max(mx, abs(lhs-rhs)/(1+abs(rhs)))

Ctrue = 3*2**(4/3)*(1024*64/63)**(1/3)
print(f"max_normalized_det_error={mx:.17g}")
print(f"true_near_coloop_constant={Ctrue:.15f}")
assert mx < 1e-12
assert Ctrue < 76.597
print("QFORM_B11_GRAPH_BANK_ZERO_PIVOT_CHECK_PASS")
