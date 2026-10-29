"""Lemma A (iii): drift of |w|^2 per unit u near the corner (agent H)."""
import random
import mpmath as mp
from gen_b1e import generator, W2_of
from checks import corner, schur
mp.mp.dps = 100
random.seed(11)
tau0 = mp.mpf("0.7")
def w2(V):
    a, w, X = schur(V)
    return sum(x * x for x in w)
for m in (3, 4):
    for g2 in map(mp.mpf, ["0.5", "1"]):
        kap = g2 * (m - 2) / (2 * m * (m - 1))
        a = mp.mpf(10) ** 6
        for ws, phi in (("1e-3", "1e-14"), ("1e-5", "1e-14"), ("0", "1e-6"), ("0", "1e-9")):
            ws = mp.mpf(ws); phi = mp.mpf(phi)
            rows = []
            for _ in range(4):
                n = m - 1
                A = mp.matrix([[mp.mpf(random.gauss(0, 1)) for _ in range(n)] for _ in range(n)])
                Xs = A * A.T + mp.eye(n) * mp.mpf("0.01")
                Xs = Xs * (phi * a / sum(Xs[i, i] for i in range(n)))
                wv = [mp.mpf(random.gauss(0, 1)) for _ in range(n)]
                nr = mp.sqrt(sum(x * x for x in wv)); wv = [x * ws / nr for x in wv] if ws else [mp.mpf(0)] * n
                V = corner(m, a, wv, Xs)
                dr, qv = generator(w2, V, g2, tau0, with_c=False)
                u = dr / (W2_of(V) / tau0 ** 2)
                rows.append(float(u / (ws ** 2)) if ws else float(u / phi))
            lab = "drift/|w|^2 (expect -2kappa=%.6f)" % float(-2 * kap) if ws else "drift/Phi_S"
            print("m%d g2 %.1f |w| %.0e Phi %.0e: %s %s" % (m, float(g2), float(ws), float(phi), lab, ["%.6f" % r for r in rows]), flush=True)
