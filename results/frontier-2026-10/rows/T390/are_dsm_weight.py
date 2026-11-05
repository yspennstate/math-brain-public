"""T390 (agent A, 18 Oct 2026): companion to are_dsm.py. Same mixture, but the parameter is the WEIGHT:
p_w = w N(-m, 1) + (1 - w) N(m, 1), truth w = 1/2, means known. DSM at noise sigma with the noise integrated out exactly;
ARE = V_MLE / V_DSM by the sandwich formula. Score matching sees the weight only through the score in the valley between the
modes, so ARE at sigma = 0 should fall like exp(-c m^2); sigma of order m fills the valley."""
import numpy as np
def logq(y, w, m, s2):
    a = np.log(w) - (y + m) ** 2 / (2 * s2); b = np.log(1 - w) - (y - m) ** 2 / (2 * s2); mx = np.maximum(a, b)
    return mx + np.log(np.exp(a - mx) + np.exp(b - mx)) - 0.5 * np.log(2 * np.pi * s2)
def h(y, w, m, s2):
    r = 0.5 * (1 + np.tanh(m * y / s2 + 0.5 * np.log((1 - w) / w)))       # P(component at +m | y)
    s = (-y + m * (2 * r - 1)) / s2; sp = (-1 + 4 * m * m * r * (1 - r) / s2) / s2
    return s * s + 2 * sp
def are(m, sig, dt=1e-4):
    s2 = 1 + sig * sig; L = m + 12; x = np.arange(-L, L, 0.002); w = np.exp(logq(x, 0.5, m, 1.0)) * 0.002
    if sig > 0: e = np.linspace(-8, 8, 161); we = np.exp(-e * e / 2); we /= we.sum(); Y = x[:, None] + sig * e[None, :]
    lv = (lambda u: (h(Y, u, m, s2) * we).sum(1)) if sig > 0 else (lambda u: h(x, u, m, s2))
    lp, l0, lm = lv(0.5 + dt), lv(0.5), lv(0.5 - dt); psi = (lp - lm) / (2 * dt); dpsi = (lp - 2 * l0 + lm) / dt ** 2
    Vd = (w * psi ** 2).sum() / (w * dpsi).sum() ** 2
    g = (logq(x, 0.5 + dt, m, 1.0) - logq(x, 0.5 - dt, m, 1.0)) / (2 * dt); I = (w * g * g).sum()
    return (1 / I) / Vd
print(__doc__.splitlines()[0])
sigs = [0.0, 0.5, 1.0, 2.0, 4.0, 8.0]
print("   m  | " + " ".join(f"sig={s:<5}" for s in sigs) + " | ln ARE(0)/m^2")
for m in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0]:
    row = [are(m, s) for s in sigs]
    print(f" {m:4.1f} | " + " ".join(f"{r:9.3e}" for r in row) + f" | {np.log(row[0]) / m ** 2:+.4f}", flush=True)
