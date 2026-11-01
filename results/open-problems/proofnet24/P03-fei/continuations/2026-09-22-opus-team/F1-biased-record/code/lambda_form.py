"""Leading small-bias term of the flat-potential slack: eps^2 log2(1/eps^2) * Lambda(v),
Lambda(v) = sum_i Inf_i v_i^2 - sum_{T: ghat(T)=0} (sum_{i not in T} v_i ghat(T u i))^2."""
import numpy as np
from gate import load_table, biased_spectrum, N
t = load_table(); c = biased_spectrum(t, [0.5] * N)
W = np.rint(c * (1 << N)).astype(np.int64)
idx = np.arange(1 << N)
zero = np.nonzero(W == 0)[0]
# matrix A[T, i] = ghat(T u i) for T in zero set, i not in T
A = np.zeros((len(zero), N))
for i in range(N):
    notin = ((zero >> i) & 1) == 0
    A[notin, i] = W[zero[notin] | (1 << i)] / 2.0 ** N
Inf = np.array([W[1 << i] / 2.0 ** N for i in range(N)])
L = np.diag(Inf) - A.T @ A
ev, evec = np.linalg.eigh(L)
print("Lambda eigenvalues:", np.round(ev, 6))
cvec = Inf / np.linalg.norm(Inf)
P = np.eye(N) - np.outer(cvec, cvec)
evb = np.linalg.eigvalsh(P @ L @ P)
print("on the balanced subspace (sum c_i v_i = 0):", np.round(evb, 6))
# Lambda' = Lambda + c c^T: the T = empty term (the output mean, repaid by h(V_out) when F is used as an input) removed
Lp = L + np.outer(Inf, Inf)
evp = np.linalg.eigvalsh(Lp)
print("Lambda' = Lambda + c c^T eigenvalues:", np.round(evp, 6))
