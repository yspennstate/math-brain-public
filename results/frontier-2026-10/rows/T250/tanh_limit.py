"""T250 (agent A, 18 Oct 2026): prediction for E q_L / qbar_L in the critical tanh chain at L/n = t.
Small q: q' = q chi2_n/n - 2 q^2 + ..., the same structure as T244's angle (log-multiplier mean -1/n, variance 2/n, quadratic absorption),
so 2 L q_L -> 1/A_t with T244's A_t = (1/t) int_0^t exp(s + sqrt 2 W_s) ds, and E q/qbar -> E[1/A_t]."""
import numpy as np
rng = np.random.default_rng(11); P, m = 40000, 1500
for t in [0.32, 0.64, 1.28, 2.56]:
    dq = t / m; B = np.zeros(P); I = np.zeros(P)
    for j in range(m):
        e = np.exp(j * dq + np.sqrt(2) * B); B += np.sqrt(dq) * rng.standard_normal(P)
        I += 0.5 * (e + np.exp((j + 1) * dq + np.sqrt(2) * B)) * dq
    A = I / t; r = 1 / A
    print(f"t {t:4.2f}: E[1/A_t] {r.mean():.4f}  sd(sqrt(1/A_t)) {np.sqrt(r).std():.4f}  (rel. coupling bound would be sqrt(E(sqrt(1/A)-1)^2) = {np.sqrt(np.mean((np.sqrt(r) - 1) ** 2)):.4f})", flush=True)
