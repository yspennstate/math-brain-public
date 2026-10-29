# Audit of agent B's RR next-order term with momentum and eps > 0 (T354, NOTE section of 20 Oct 04:2x, next_order_rr_eps.py).
# agent A, 20 Oct 2026. Claim: x*/x0 = 1 + d (r K - p2 T H/(r K B2 B3)) + O(d^2), x0 = r d K B3/(2 B2), r = s/(s+eps),
# p2 = psi''(1) = s(eps+3s)/(4(eps+s)^2), s = sqrt(B2). Checks: (1) psi'(1), psi''(1) by finite differences; (2) exact roots from
# rr_exact_mom_eps.py at (beta1, eps) pairs the peer did not run (0.3 and 0.7, eps 3), three beta2 each, with the gap/d flat test
# and a linear extrapolation of the exact column to d = 0 against the limit coefficient r K0 - p2 T H/(r K0 B2 B3).
import sys, runpy, numpy as np
B2, B3, T, n = 9.0, 72.0, 4608.0, 10; s = 3.0
def psi(y, e): return (s + e) / (s * np.sqrt(y) + e)
for e in [1.0, 3.0, 10.0]:
    hh = 1e-4; fd1 = (psi(1 + hh, e) - psi(1 - hh, e)) / (2 * hh); fd2 = (psi(1 + hh, e) - 2 * psi(1, e) + psi(1 - hh, e)) / hh ** 2
    print(f"eps {e}: psi'(1) fd {fd1:.8f} vs -r/2 {-s / (s + e) / 2:.8f} | psi''(1) fd {fd2:.6f} vs p2 {s * (e + 3 * s) / (4 * (e + s) ** 2):.6f}")
hf = lambda p: 1 - 3 * p / (n - 1) + 2 * p * (p - 1) / ((n - 1) * (n - 2))
sys.path.insert(0, "../agent_B"); from kfactor import K_rr
pairs = [(float(a), float(b)) for a, b in (x.split(":") for x in sys.argv[1].split(","))]
b2s = [float(x) for x in sys.argv[2].split(",")]
for b1, e in pairs:
    r = s / (s + e); p2 = s * (e + 3 * s) / (4 * (e + s) ** 2)
    H = np.mean([(1 - b1 ** (p + 1)) * hf(p) for p in range(n)]); K0 = np.mean([(1 - b1 ** (p + 1)) * (1 - p / (n - 1)) for p in range(n)])
    lim = r * K0 - p2 * T * H / (r * K0 * B2 * B3); ds = []; cs = []
    for b2 in b2s:
        sys.argv = ["rr_exact_mom_eps.py", str(b1), str(b2), str(e)]
        g = runpy.run_path("rr_exact_mom_eps.py"); d = 1 - b2; K = K_rr(n, b1, b2)
        c = (g["xs"] / g["x0"] - 1) / d; pred = r * K - p2 * T * H / (r * K * B2 * B3)
        print(f"  b1 {b1} eps {e} beta2 {b2}: exact (x*/x0-1)/d {c:.6f} predicted {pred:.6f} gap/d {(c - pred) / d:.3f}", flush=True)
        ds.append(d); cs.append(c)
    sl = (cs[1] - cs[0]) / (ds[1] - ds[0]); print(f"b1 {b1} eps {e}: H {H:.6f} K0 {K0:.6f} limit {lim:.6f} | exact extrapolated to d=0 (two smallest d) {cs[0] - sl * ds[0]:.6f}", flush=True)
