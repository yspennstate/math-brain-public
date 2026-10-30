"""T246 (agent A, 17 Oct 2026): the independent-layer prediction for Var log|Ju|^2 in deep tanh nets at sigma_w = 1,
sigma_b = 0. Per layer, |v_l|^2 = (1/n) sum_i phi'(h_i)^2 g_i^2 with g_i ~ N(0,1) independent of h_i ~ N(0, q_(l-1)) gives
Var log|v_l|^2 ~ (3 E phi'^4 / (E phi'^2)^2 - 1)/n. Summed along the mean-field q_l: n Var = sum_l k_l = 2L + K(L)."""
import numpy as np
z, w = np.polynomial.hermite_e.hermegauss(200); w = w / w.sum()
q = 1.0; tot = 0.0; out = {}
for l in range(1, 1025):
    fp2 = 1 / np.cosh(np.sqrt(q) * z) ** 4; m2 = w @ fp2; m4 = w @ fp2 ** 2
    tot += 3 * m4 / m2 ** 2 - 1; q = w @ np.tanh(np.sqrt(q) * z) ** 2
    if l in (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024): out[l] = tot
for l, v in out.items(): print(f"L={l:5d}  sum k_l {v:9.3f}  minus 2L {v - 2*l:7.3f}  per-layer avg {v/l:.4f}")
