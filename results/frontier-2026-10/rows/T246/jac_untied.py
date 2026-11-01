"""T246 (agent A, 17 Oct 2026): where the excess variance of log|Ju|^2 comes from. Deep tanh, sigma_w = 1, sigma_b = 0.
mode tied:      the network (as jac_tanh.py): h = W x, v <- phi'(h) * (W v).
mode untied:    backward weights independent of forward ones: v <- phi'(h) * (W' v), W' an independent copy (the gradient
                independence assumption); the forward pass and its fluctuations are kept.
mode meanfield: h_i iid N(0, q_l) from the mean-field variance map, v <- phi'(h) * (W' v): no forward fluctuation, no tie.
Independent-layer prediction (jac_pred.py): n Var = 2L + 4.2 for L >= 64 (35.8, 68.0, 132.1, 260.1, 516.2 at L = 16..256).
argv: mode n B LS seed"""
import sys, numpy as np
mode, n, B, LS, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), [int(s) for s in sys.argv[4].split(',')], int(sys.argv[5])
rng = np.random.default_rng(seed); fp = lambda h: 1/np.cosh(h)**2
z, wq = np.polynomial.hermite_e.hermegauss(80); wq = wq/wq.sum(); qs = [1.0]
for l in range(max(LS)): qs.append(float(wq @ np.tanh(np.sqrt(qs[-1])*z)**2))
x = rng.standard_normal((B, n)); x *= np.sqrt(n)/np.linalg.norm(x, axis=1, keepdims=True)
v = rng.standard_normal((B, n)); v /= np.linalg.norm(v, axis=1, keepdims=True); logn = np.zeros(B)
for l in range(1, max(LS) + 1):
    if mode == "meanfield":
        h = rng.standard_normal((B, n))*np.sqrt(qs[l-1])
    else:
        W = rng.standard_normal((B, n, n))/np.sqrt(n); h = np.einsum('bij,bj->bi', W, x); x = np.tanh(h)
    Wb = W if mode == "tied" else rng.standard_normal((B, n, n))/np.sqrt(n)
    v = fp(h)*np.einsum('bij,bj->bi', Wb, v); nv = np.linalg.norm(v, axis=1); logn += 2*np.log(nv); v /= nv[:, None]
    if l in LS:
        m, s2 = logn.mean(), logn.var(ddof=1)
        print(f"{mode} n={n} L={l:4d} | mean {m:+.4f} | var {s2:.4f} n*var {n*s2:8.2f} (+- {n*s2*np.sqrt(2/(B-1)):.1f}) n*var/L {n*s2/l:.3f} | B={B}", flush=True)
