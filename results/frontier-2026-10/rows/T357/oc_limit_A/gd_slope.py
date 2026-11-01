"""T357, GD: is the late GD path radial? Gaussian integration by parts gives E[z sig''(beta z)] = (i_par - i_perp)/beta, so the
slowest eigenvector of the Hessian at the MLE tilts into w_perp by tau = E[z sig''(beta z)]/(i_par - i_perp) = 1/beta:
w_perp(kappa) = w_perp_hat (1 + (kappa - kappa_hat)/beta) to leading order, i.e. the late path is a rescaling of the MLE, and
d ln s / d ln kappa -> 2 kappa/beta (s = |w_perp|^2). If instead w_perp had converged first, the slope would be 0.
Prints the local slope (central difference over +-1 time unit) along the path. argv: d alpha beta seeds tmax"""
import sys, math
import numpy as np
d = int(sys.argv[1]); alpha = float(sys.argv[2]); beta = float(sys.argv[3]); seeds = int(sys.argv[4]); tmax = float(sys.argv[5])
n = int(alpha * d); ETA = 0.1
sig = lambda t: 0.5 * (1 + np.tanh(t / 2))
for sd in range(seeds):
    rng = np.random.default_rng(100 + sd)
    X = rng.standard_normal((n, d)); y = np.where(rng.random(n) < sig(beta * X[:, 0]), 1.0, -1.0)
    w = np.zeros(d); K, S = [], []
    for k in range(1, int(tmax / ETA) + 1):
        m = y * (X @ w); w = w + ETA * (X.T @ (y * sig(-m))) / n
        K.append(w[0]); S.append(float(w[1:] @ w[1:]))
    K, S = np.array(K), np.array(S); T = ETA * np.arange(1, len(K) + 1)
    out = []
    for t in (10, 20, 30, 40, 60, 80, 100):
        j = int(round(t / ETA)) - 1
        if j + 10 >= len(K): break
        sl = (math.log(S[j + 10]) - math.log(S[j - 10])) / (math.log(K[j + 10]) - math.log(K[j - 10]))
        out.append(f"t {t}: kappa {K[j]:.4f} alpha*s {alpha * S[j]:.4f} slope {sl:+.3f} (radial {2 * K[j] / beta:.3f})")
    print(f"seed {sd}: " + " | ".join(out), flush=True)
