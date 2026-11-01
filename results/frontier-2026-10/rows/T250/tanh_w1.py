"""T250 (agent A, 18 Oct 2026): critical tanh MLP (W ~ N(0, 1/n), no bias), one input, q0 = 1. Given layer l-1,
h_l ~ N(0, q_(l-1) I_n), q_l = |tanh(h_l)|^2/n (a random scalar chain, exactly simulable). GP limit: qbar_l = E tanh(sqrt(qbar_(l-1)) Z)^2,
qbar_l ~ 1/(2 l)... decaying. Synchronous coupling: W1(h_L/sqrt n, GP/sqrt n) <= sqrt(E(sqrt q_(L-1) - sqrt qbar_(L-1))^2).
Prints the bound, the bound relative to sqrt(qbar), and that ratio times sqrt(n/L).
usage: tanh_w1.py n paths"""
import sys, numpy as np
n, P = int(sys.argv[1]), int(sys.argv[2]); rng = np.random.default_rng(7 + n)
gz, gw = np.polynomial.hermite_e.hermegauss(80); gw = gw / gw.sum()
q = np.ones(P); qb = 1.0
print(f"n {n} paths {P}", flush=True)
for l in range(1, 4 * n + 1):
    if l in (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048):
        b = np.sqrt(np.mean((np.sqrt(q) - np.sqrt(qb)) ** 2)); rel = b / np.sqrt(qb)
        print(f"  L {l:5d} (L/n {l / n:6.3f}): qbar {qb:.5f} (l qbar {l * qb:.3f})  bound {b:.5f}  bound/sqrt(qbar) {rel:.4f}"
              f"  *sqrt(n/(L-1)) {rel * np.sqrt(n / (l - 1)):.4f}  E q/qbar {q.mean() / qb:.4f}", flush=True)
    h = np.sqrt(q)[:, None] * rng.standard_normal((P, n)); q = (np.tanh(h) ** 2).mean(1)
    qb = float(np.sum(gw * np.tanh(np.sqrt(qb) * gz) ** 2))
