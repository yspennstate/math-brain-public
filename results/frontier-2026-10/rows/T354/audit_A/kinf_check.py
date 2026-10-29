"""inf over n >= 2 of K_rr(n, beta1, beta2) at fixed beta1, beta2 (agent A, 20 Oct 2026; B's request).
K from agent_B/kclosed.py, cross-checked against the direct lag sum
K = sum_i w_i [ beta2-weighted lag sum ] computed here independently from the definition E[m eta]/(d E[bZ]/V) with the RR pair rule."""
import sys, numpy as np
sys.path.insert(0, "../agent_B")
from kclosed import K_closed

def K_direct(n, b1, b2, L=None):
    # K = sum_{i,j>=0} w_i b2^j * c(|i-j|), w_i = (1-b1) b1^i, c(0) = 1, c(l) = -(n-l)/(n(n-1)) for 1 <= l <= n-1 (same epoch,
    # prob (n-l)/n, pair corr -1/(n-1)), c(l) = 0 beyond. Truncated at L terms each.
    d = 1 - b2
    L = L or int(min(4e4, 60 / min(1 - b1 if b1 > 0 else 1, d)))
    i = np.arange(L); w = (1 - b1) * b1 ** i; v = b2 ** i
    lag = np.abs(i[:, None] - i[None, :]).astype(float)
    c = np.where(lag == 0, 1.0, np.where(lag < n, -(n - lag) / (n * (n - 1)), 0.0))
    return float(w @ c @ v)

worst = 0.0
for n in (2, 5, 30):
    for b1 in (0.0, 0.5, 0.9):
        for b2 in (0.9, 0.99):
            a, b = K_closed(n, b1, b2), K_direct(n, b1, b2, L=3000); worst = max(worst, abs(a - b))
print("closed vs direct lag sum, 18 cells: max diff %.2e" % worst)
ns = np.unique(np.concatenate([np.arange(2, 2001), np.logspace(np.log10(2000), 7, 400).astype(int)]))
for b1 in (0.0, 0.5, 0.9, 0.99, 0.999):
    for b2 in (0.9, 0.99, 0.999, 0.9999):
        K = np.array([K_closed(int(n), b1, b2) for n in ns]); j = K.argmin()
        print("b1 %-6s b2 %-7s inf_n K %.6g at n %d | n->inf (1-b1)/(1-b1 b2) %.6g | K(n=2) %.6g" % (b1, b2, K[j], ns[j], (1 - b1) / (1 - b1 * b2), K[0]))
