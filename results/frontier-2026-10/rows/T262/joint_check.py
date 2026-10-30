"""T262 joint law of (log phi, log|h|) at L = t n (agent A, 19 Oct). One-layer derivation: on the active set A (|A| = K ~ n/2)
the radial chi-square X = log(sum_A x^2 / K) enters log|h|^2 with + sign and log theta with -1/2, the tangent one (independent)
enters log theta with +1/2, and log K enters log|h|^2 only. Per layer: Var dlog|h|^2 = 5/n, Var dlog theta = 2/n, Cov = -2/n,
so corr = -2/sqrt(10) = -0.632. Limit: d log phi = (-1 - phi/(3 pi)) ds + sqrt2 dB1, d log|h|^2 = -5/2 ds + sqrt5 dB2,
d<B1,B2> = -(2/sqrt10) ds; phi enters from infinity (u = 1/phi from 0). Prints corr(log phi_t, log|h_t|) to compare with
two_input_run1.txt (theta_0 = 1, so small t is still forgetting the start)."""
import numpy as np
rng = np.random.default_rng(1); R = 200000; ds = 1e-3; rho = -2 / np.sqrt(10)
u = np.zeros(R); B1 = np.zeros(R); B2 = np.zeros(R); s = 0.0
for k in range(1, 2001):
    d1 = np.sqrt(ds) * rng.standard_normal(R); d2 = rho * d1 + np.sqrt(1 - rho ** 2) * np.sqrt(ds) * rng.standard_normal(R)
    u = u + (2 * u + 1 / (3 * np.pi)) * ds - np.sqrt(2) * u * d1; B1 += d1; B2 += d2; s = k * ds
    if k in (250, 500, 1000, 2000):
        lp = -np.log(u); lh = 0.5 * (-2.5 * s + np.sqrt(5) * B2)
        print(f"t {s:.2f}: corr(log phi, log|h|) {np.corrcoef(lp, lh)[0,1]:+.3f}  sd log phi {lp.std():.2f}  mean log phi {lp.mean():.2f}", flush=True)
