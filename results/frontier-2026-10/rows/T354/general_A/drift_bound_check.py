"""T354 general case (agent A, 21 Oct 2026): check of the frozen-x drift bound on a nonconvex finite sum in d = 2.
f_i(x) = a_i |x|^2/2 + b_i.x + c_i (cos x_1 + cos x_2), sum b_i = 0, skewed b (B3 != 0), mean c > mean a (nonconvex).
At frozen x, Adam with reshuffling drives m, v through linear filters of the gradient stream g_{pi(t)}(x) (bias correction
dies geometrically), so h(x) = E[m/(sqrt v + eps)] is a time average over a long reshuffled stream. The claim, coordinate j,
with phi(v) = 1/(sqrt v + eps), B2 = mean g_j^2:
    h_j = d_j f phi(B2) + phi'(B2) Cov(m_j, v_j) + R_j,   |R_j| <= G_j C2_j Var(v_j),
    |Cov(m_j, v_j)| <= (1 - b2) |Cov(g_j, g_j^2)| [(1 - b1)/(1 - b1 b2) + n/(n - 1)],  Var(v_j) <= (1 - b2)/(1 + b2) Var(g_j^2),
the remainder split at v = B2/4 (Taylor constant above, Hoeffding tail below; see Rbound), G_j = max_i |g_ij|. Then an Adam run with step
eta/sqrt(k) is compared with the zero of the first-order drift. argv: b1 b2 eps n T seed steps"""
import sys, math
import numpy as np
from scipy.signal import lfilter
b1, b2, eps = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
n, T, seed, steps = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])
rng = np.random.default_rng(seed)
a = rng.uniform(0.5, 1.5, n); c = rng.uniform(1.5, 2.5, n)
b = rng.exponential(1.0, (n, 2)) - 1.0; b -= b.mean(0)            # skewed, mean zero
def grads(x):                                                       # (n, 2)
    return a[:, None] * x[None, :] + b - c[:, None] * np.sin(x)[None, :]
def gradf(x):
    return grads(x).mean(0)
phi = lambda v: 1.0 / (np.sqrt(v) + eps)
dphi = lambda v: -1.0 / (2 * np.sqrt(v) * (np.sqrt(v) + eps) ** 2)
def C2(B2):
    # half the sup of |phi''| on [B2/4, inf): the Taylor constant away from the lower tail
    v = B2 * np.logspace(np.log10(0.25), 6, 4000); h = 1e-5 * v
    return float(0.5 * np.max(np.abs(phi(v + h) - 2 * phi(v) + phi(v - h)) / h ** 2))
def Rbound(G, B2):
    # |E m R| <= G [C2 Var(v) + (phi(v_lo) + phi(B2) + |phi'(B2)| B2) P(v < B2/4)], Var and the Hoeffding tail at their iid values
    # (reshuffled draws are negatively associated, Shao's comparison), v_lo = (1 - b2) b2^(2n) n B2 (one full epoch in 2n steps)
    Gj = np.abs(G).max(0); out = []
    for j in range(G.shape[1]):
        vb = (1 - b2) / (1 + b2) * (G[:, j] ** 2).var(); vlo = (1 - b2) * b2 ** (2 * n) * n * B2[j]
        tail = math.exp(-1.125 * B2[j] ** 2 * (1 + b2) / ((1 - b2) * Gj[j] ** 4))
        out.append(Gj[j] * (C2(B2[j]) * vb + (min(1 / eps, 1 / math.sqrt(vlo)) + phi(B2[j]) + abs(dphi(B2[j])) * B2[j]) * tail))
    return np.array(out)
def stream(x, T, r):
    order = np.concatenate([r.permutation(n) for _ in range(T // n + 1)])[:T]
    return grads(x)[order]
def frozen(x, r):
    g = stream(x, T, r); burn = int(20 / (1 - b2))
    m = lfilter([1 - b1], [1, -b1], g, axis=0)[burn:]; v = lfilter([1 - b2], [1, -b2], g * g, axis=0)[burn:]
    h = (m / (np.sqrt(v) + eps)).mean(0)
    G = grads(x); B2 = (G * G).mean(0); df = G.mean(0)
    cov = ((m - m.mean(0)) * (v - v.mean(0))).mean(0); varv = v.var(0)
    first = df * phi(B2) + dphi(B2) * cov
    Cg = ((G - df) * (G * G - B2)).mean(0)                        # Cov(g, g^2) over the n examples
    covb = (1 - b2) * np.abs(Cg) * ((1 - b1) / (1 - b1 * b2) + n / (n - 1))
    varb = (1 - b2) / (1 + b2) * (G * G).var(0)
    Rb = Rbound(G, B2)
    return h, first, df * phi(B2), cov, covb, varv, varb, Rb, B2
print(__doc__, flush=True)
print(f"b1 {b1} b2 {b2} eps {eps} n {n} T {T} seed {seed}; mean a {a.mean():.3f} mean c {c.mean():.3f}", flush=True)
r = np.random.default_rng([seed, 1])
for x in (np.array([0.3, -0.2]), np.array([1.0, 2.0]), np.array([-2.5, 0.7])):
    h, first, zeroth, cov, covb, varv, varb, Rb, B2 = frozen(x, r)
    for j in range(2):
        print(f"x {x} j {j}: h {h[j]:+.6e}  0th {zeroth[j]:+.6e}  1st {first[j]:+.6e}  |h-1st| {abs(h[j]-first[j]):.2e} <= Rbound {Rb[j]:.2e}"
              f"  |h-0th| {abs(h[j]-zeroth[j]):.2e}  Cov {cov[j]:+.3e} (bound {covb[j]:.3e})  Var v {varv[j]:.3e} (bound {varb[j]:.3e})", flush=True)
# Adam-RR, eta_k = eta0/sqrt(k), from a nonconvex start; then the zero of the first-order drift near the endpoint
x = np.array([2.0, -1.5]); m = np.zeros(2); v = np.zeros(2); eta0 = 0.05; k = 0
G0 = None; ra = np.random.default_rng([seed, 2])
gs = grads; xs = []
while k < steps:
    for i in ra.permutation(n):
        k += 1
        g = a[i] * x + b[i] - c[i] * np.sin(x)
        m = b1 * m + (1 - b1) * g; v = b2 * v + (1 - b2) * g * g
        mh = m / (1 - b1 ** k); vh = v / (1 - b2 ** k)
        x = x - eta0 / math.sqrt(k) * mh / (np.sqrt(vh) + eps)
        if k > steps - 20 * n: xs.append(x.copy())
        if k >= steps: break
xe = np.mean(xs, 0)
print(f"Adam-RR {steps} steps, eta0 {eta0}/sqrt(k): endpoint {xe}  grad f {gradf(xe)}", flush=True)
# zero of the first-order drift by Newton on the measured first-order expression, Cov from the frozen stream
y = xe.copy(); rz = np.random.default_rng([seed, 3])
for it in range(6):
    _, F, *_ = frozen(y, np.random.default_rng([seed, 3]))
    J = np.zeros((2, 2)); hh = 1e-4
    for j in range(2):
        e = np.zeros(2); e[j] = hh
        J[:, j] = (frozen(y + e, np.random.default_rng([seed, 3]))[1] - frozen(y - e, np.random.default_rng([seed, 3]))[1]) / (2 * hh)
    y = y - np.linalg.solve(J, F)
h, first, zeroth, cov, covb, varv, varb, Rb, B2 = frozen(y, np.random.default_rng([seed, 4]))
print(f"first-order zero {y}: grad f {gradf(y)}; predicted residual -phi'Cov/phi = {-dphi(B2) * cov / phi(B2)}", flush=True)
print(f"bound on the residual (sqrt B2 + eps)(1 - b2) Q: {(np.sqrt(B2) + eps) * (np.abs(dphi(B2)) * covb + Rb)}", flush=True)
print(f"endpoint - first-order zero: {xe - y}  (|grad f(endpoint)| / |grad f(zero)| = {np.abs(gradf(xe)) / np.abs(gradf(y))})", flush=True)
print("DONE", flush=True)
