"""Does the two-term reduction reduce the difficulty, or only relocate it?

Phi(u) = int_1^2 cos(2 pi u t) P_(K-1)(t) dt expands over the same characters:
    Phi(u) = (1/2) sum_eps c_eps [ W(nu_eps + u) + W(nu_eps - u) ],   W(v) = int_1^2 e(vt) dt,
with |W(v)| <= min(1, 1/(pi|v|)). So the triangle bound on Phi is the c-weight sitting within O(1) of
+-u - the SAME counting problem that defeats the triangle inequality for A_K. If the ratio of that bound
to the true |Phi| is exponential in K, the two-term form is a simplification of shape, not of difficulty.
Measure it.
"""
import numpy as np

def frequencies(K):
    lam = [(1.5 ** m) / 3.0 for m in range(K)]
    nu = np.zeros(1); c = np.ones(1)
    for L in lam:
        nu = np.concatenate([nu - L, nu, nu + L])
        c = np.concatenate([c * 0.5, c, c * 0.5])
    return nu, c

def W_abs(v):
    v = np.abs(v)
    return np.where(v < 1e-12, 1.0, np.minimum(1.0, 1.0 / (np.pi * np.maximum(v, 1e-12))))

N = 1 << 20
x = 1 + (np.arange(N) + 0.5) / N
f = lambda K: (1.5 ** K) / 3.0

print(f"{'K':>4} {'|Phi(f_K)| true':>17} {'triangle bound':>16} {'ratio':>12} {'(4/3)^K':>10}")
for K in (8, 10, 12, 14):
    P = np.ones(N)
    for m in range(K):
        P *= 1.0 + np.cos(2 * np.pi * x * f(m))
    true = abs(float((np.cos(2 * np.pi * f(K) * x) * P).mean()))
    nu, c = frequencies(K)
    u = f(K)
    bound = 0.5 * float((c * (W_abs(nu + u) + W_abs(nu - u))).sum())
    print(f"{K:>4} {true:>17.8f} {bound:>16.4f} {bound/max(true,1e-18):>12.2e} {(4/3)**K:>10.2f}")
print()
print("If the ratio grows exponentially, the increment needs the same cancellation A_K does,")
print("and the two-term form has moved the difficulty rather than reduced it.")
