"""T246 Target 2 (agent A, 16 Oct 2026): log |J u|^2 for deep random tanh networks at sigma_w = 1, sigma_b = 0, against L/n.
x_l = phi(W_l x_(l-1)), W_l iid N(0, sigma_w^2/n), |x_0|^2 = n q_0, u a unit tangent; v_l = phi'(W_l x_(l-1)) * (W_l v_(l-1)), J u = v_L.
Records log |v_L|^2 at each L in LS, with the mean-field drift sum_l log chi_l (chi_l = sigma_w^2 E phi'(sqrt(q_l) z)^2, q_l from
the variance map) for comparison. ReLU at sigma_w^2 = 2 as the control (Hanin-Nica: per-layer log-variance 5/n).
argv: act n B LS(comma) seed"""
import sys, numpy as np
act, n, B, LS, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), [int(s) for s in sys.argv[4].split(',')], int(sys.argv[5])
rng = np.random.default_rng(seed)
if act == "tanh":
    sw2 = 1.0; f = np.tanh; fp = lambda h: 1/np.cosh(h)**2
else:
    sw2 = 2.0; f = lambda h: np.maximum(h, 0); fp = lambda h: (h > 0).astype(float)
z, wq = np.polynomial.hermite_e.hermegauss(80); wq = wq/wq.sum()
q = 1.0; drift = 0.0; mf = {}
for l in range(1, max(LS) + 1):
    chi = sw2*np.sum(wq*fp(np.sqrt(q)*z)**2); drift += np.log(chi)
    q = sw2*np.sum(wq*f(np.sqrt(q)*z)**2)
    if l in LS: mf[l] = (drift, q)
x = rng.standard_normal((B, n)); x *= np.sqrt(n)/np.linalg.norm(x, axis=1, keepdims=True)
v = rng.standard_normal((B, n)); v /= np.linalg.norm(v, axis=1, keepdims=True)
logn = np.zeros(B); out = {}
for l in range(1, max(LS) + 1):
    W = rng.standard_normal((B, n, n))*np.sqrt(sw2/n)
    h = np.einsum('bij,bj->bi', W, x); g = np.einsum('bij,bj->bi', W, v)
    x = f(h); v = fp(h)*g
    nv = np.linalg.norm(v, axis=1); logn += 2*np.log(nv); v /= nv[:, None]
    if l in LS:
        m, s2 = logn.mean(), logn.var(ddof=1); k3 = np.mean((logn - m)**3)/s2**1.5; k4 = np.mean((logn - m)**4)/s2**2 - 3
        d, ql = mf[l]
        print(f"{act} n={n} L={l:>4} t={l/n:.3f} | mean log|Ju|^2 {m:+.4f} (mean-field drift {d:+.4f}, mean - drift {m-d:+.4f}) | "
              f"var {s2:.4f} var*n/L {s2*n/l:.3f} | skew {k3:+.3f} exkurt {k4:+.3f} | q_L {ql:.4f} | B={B}", flush=True)
