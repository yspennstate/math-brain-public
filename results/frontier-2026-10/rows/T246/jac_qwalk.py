"""T246 (agent A, 17 Oct 2026): the independent-layer prediction plus the random walk of the forward norm.
Deep tanh, sigma_w = 1, sigma_b = 0, |x_0|^2/n = 1. Layer l: h_l ~ N(0, qhat_(l-1)) given the past, qhat_l = mean tanh(h_l)^2,
log |v_l|^2/|v_(l-1)|^2 = log m2(qhat_(l-1)) + eta_l, m2(q) = E sech^4(sqrt q z). To first order in 1/n:
    qhat_l = F(qhat_(l-1)) + xi_l,   Var xi_l = Var tanh^2 / n,   Var eta_l = (3 m4/m2^2 - 1)/n,
    Cov(xi_l, eta_l) = Cov(tanh^2, sech^4)/(n m2)   (same h_l; the backward Gaussian factor is independent with mean square 1),
and log|v_L|^2 - drift = sum_k (G_k xi_k + eta_k), G_k = sum_(l>k) c_l prod_(k<j<l) a_j, c = (log m2)'(q), a = F'(q).
Prints n Var for the independent-layer part (sum Var eta), the walk part (sum G^2 Var xi), the cross part, and the total."""
import numpy as np
z, w = np.polynomial.hermite_e.hermegauss(300); w = w / w.sum()
def stats(q):
    s = np.sqrt(q) * z; t2 = np.tanh(s) ** 2; f4 = 1 / np.cosh(s) ** 4
    m2 = w @ f4; m4 = w @ f4 ** 2; Ft = w @ t2; vt = w @ t2 ** 2 - Ft ** 2; cv = w @ (t2 * f4) - Ft * m2
    return m2, m4, Ft, vt, cv
def deriv(fn, q, h=1e-6): return (fn(q * (1 + h)) - fn(q * (1 - h))) / (2 * q * h)
print(__doc__.strip())
for L in (16, 32, 64, 128, 256, 512):
    q = [1.0]
    for l in range(L): q.append(stats(q[-1])[2])
    q = np.array(q)                                  # q[l] = mean-field q_l, l = 0..L
    a = np.array([deriv(lambda x: stats(x)[2], q[l - 1]) for l in range(1, L + 1)])          # a[l-1] = F'(q_(l-1))
    c = np.array([deriv(lambda x: np.log(stats(x)[0]), q[l - 1]) for l in range(1, L + 1)])  # c[l-1] for layer l
    ind = walk = cross = 0.0
    for k in range(1, L + 1):                        # xi_k, eta_k use h_k ~ N(0, q_(k-1))
        m2, m4, Ft, vt, cv = stats(q[k - 1])
        G, P = 0.0, 1.0
        for l in range(k + 1, L + 1):                # delta q_k enters log m2(q_k) at layer k+1
            G += c[l - 1] * P; P *= a[l - 1]
        ind += 3 * m4 / m2 ** 2 - 1; walk += G * G * vt; cross += 2 * G * cv / m2
    print(f"L={L:4d} | n Var: independent {ind:8.2f}  walk {walk:8.2f}  cross {cross:8.2f}  total {ind+walk+cross:8.2f} | q_L {q[-1]:.4f}")
