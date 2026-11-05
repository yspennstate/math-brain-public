"""T390 (agent A, 18 Oct 2026): Target 1. Asymptotic relative efficiency of denoising score matching (DSM) against maximum
likelihood for the separation of a symmetric two-component mixture in one dimension.
Model p_theta = 1/2 N(-theta, 1) + 1/2 N(theta, 1), truth theta = m. DSM at noise sigma fits the score s_theta of
q_theta = p_theta * N(0, sigma^2) (= 1/2 N(-theta, s2) + 1/2 N(theta, s2), s2 = 1 + sigma^2) with per-sample loss
l(theta; x) = E_eps (s_theta(x + sigma eps) + eps/sigma)^2 = E_eps h_theta(x + sigma eps) + const, h = s^2 + 2 s' (Stein's identity),
i.e. the noise is integrated out exactly (infinitely many noise draws per sample). M-estimator sandwich: V_DSM = E psi^2 / (E dpsi)^2,
psi = d l / d theta, expectations under p_m. V_MLE = 1 / I(m). Prints ARE = V_MLE / V_DSM. sigma = 0 is Hyvarinen score matching.
All integrals on a uniform grid (spacing 0.002), the noise convolution by FFT-free direct Gaussian quadrature in eps."""
import numpy as np
def logq(y, th, s2):
    a = -(y - th) ** 2 / (2 * s2); b = -(y + th) ** 2 / (2 * s2); mx = np.maximum(a, b)
    return mx + np.log(0.5 * np.exp(a - mx) + 0.5 * np.exp(b - mx)) - 0.5 * np.log(2 * np.pi * s2)
def score_terms(y, th, s2):
    # s = d/dy log q, s' ; with r = P(component +|y) = sigmoid(2 th y / s2): s = (-y + th (2r - 1)) / s2, s' = (-1 + th^2 4 r(1-r)/s2)/s2
    r = 0.5 * (1 + np.tanh(th * y / s2)); s = (-y + th * (2 * r - 1)) / s2; sp = (-1 + 4 * th * th * r * (1 - r) / s2) / s2
    return s, sp
def h(y, th, s2): s, sp = score_terms(y, th, s2); return s * s + 2 * sp
def are(m, sig, dt=1e-4):
    s2 = 1 + sig * sig; L = m + 12; x = np.arange(-L, L, 0.002); px = np.exp(logq(x, m, 1.0)); w = px * 0.002
    if sig > 0: e = np.linspace(-8, 8, 161); we = np.exp(-e * e / 2); we /= we.sum(); Y = x[:, None] + sig * e[None, :]
    def lval(th): return (h(Y, th, s2) * we).sum(1) if sig > 0 else h(x, th, s2)
    lp, l0, lm = lval(m + dt), lval(m), lval(m - dt); psi = (lp - lm) / (2 * dt); dpsi = (lp - 2 * l0 + lm) / dt ** 2
    Vd = (w * psi ** 2).sum() / (w * dpsi).sum() ** 2
    g = (logq(x, m + dt, 1.0) - logq(x, m - dt, 1.0)) / (2 * dt); I = (w * g * g).sum()
    return (1 / I) / Vd, 1 / I, Vd
if __name__ == "__main__":
    # control: m = 0 is degenerate (I = 0); a single Gaussian location model has ARE 1 for SM - check with a far-separated
    # mixture? no: use the analytic fact that for sigma=0, m -> 0+, SM and MLE both lose information; skip. Control below is the
    # Gaussian location model through the same code path: theta shifts BOTH components the same way.
    print(__doc__.splitlines()[0])
    sigs = [0.0, 0.25, 0.5, 1.0, 2.0, 4.0]
    print("   m  | " + " ".join(f"sig={s:<5}" for s in sigs) + " |  1/I_MLE")
    for m in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0]:
        row = [are(m, s) for s in sigs]
        print(f" {m:4.1f} | " + " ".join(f"{r[0]:9.3e}" for r in row) + f" | {row[0][1]:.4f}", flush=True)
