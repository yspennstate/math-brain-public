# T021: the entropy split cost D_k = H(f) - (H(f_{k,+}) + H(f_{k,-}))/2 (nats) on the alternating read-once trees of
# q31_iterated.py, against Q_k. D_k = sum_{S not ni k} Phi(f^(S)^2, f^(S u k)^2), with
#   Phi(l, m) = h(l) + h(m) - [h((sqrt l + sqrt m)^2) + h((sqrt l - sqrt m)^2)]/2,  h(t) = -t ln t,
# 1-homogeneous. One level f' = -1 + 2 prod_j g_j, g_j = (1 - h_j)/2: coefficients factor and sum_T g^(T)^2 = mu, so
#   D' = P [D - Phi(c0^2, c1^2) + Phi(4 mu^2, c1^2)] - P^2 Phi(4 mu^2, c1^2) + Phi(c0'^2, c1'^2),  P = mu^(s-1).
# Part 1 checks the recursion against truth tables (D from the restrictions' entropies directly). Part 2 iterates.
import numpy as np, mpmath as mp

def h(t): return mp.mpf(0) if t == 0 else -t * mp.log(t)
def Phi(l, m):
    a, b = mp.sqrt(l), mp.sqrt(m)
    return h(l) + h(m) - (h((a + b) ** 2) + h((a - b) ** 2)) / 2

def step(st, s):
    c0, c1, I, N, D = st
    mu = (1 - c0) / 2; P = mu ** (s - 1); ms = mu ** s
    A0 = mu * c1 / 2; A = (N - abs(c0) * c1) / 4 + A0
    c0n, c1n = -1 + 2 * ms, c1 * P
    Nn = 4 * (A * P - A0 * P * P) + c1 * P * abs(2 * ms - 1)
    Dn = P * (D - Phi(c0 ** 2, c1 ** 2) + Phi(4 * mu ** 2, c1 ** 2)) - P * P * Phi(4 * mu ** 2, c1 ** 2) + Phi(c0n ** 2, c1n ** 2)
    return (c0n, c1n, I * P, Nn, Dn)

def wht(v):
    v = v.astype(np.float64).copy(); n = v.size; hh = 1
    while hh < n:
        v = v.reshape(-1, 2 * hh); a = v[:, :hh].copy(); b = v[:, hh:].copy(); v[:, :hh] = a + b; v[:, hh:] = a - b; v = v.reshape(-1); hh *= 2
    return v / n

def ent(c):
    p = c * c; p = p[p > 1e-300]; return float(-(p * np.log(p)).sum())

def table(ss):
    n = 1
    for s in ss: n *= s
    N = 1 << n; x = ((np.arange(N)[:, None] >> np.arange(n)[None, :]) & 1)  # bit 1 = -1 = "true"
    cur = (x == 1)                       # level 0: true iff x_i = -1
    for s in ss:
        cur = cur.reshape(N, -1, s)
        cur = ~cur.all(axis=2)           # f' = +1 iff all inputs true; its "true" for the next level is f' = -1
    f = np.where(cur[:, 0], -1, 1)       # cur True means f' = -1
    return n, f

if __name__ == "__main__":
    mp.mp.dps = 50; ok = True
    for ss in [(2,), (3,), (2, 2), (3, 2), (2, 3), (4, 3), (2, 2, 2), (3, 2, 2), (2, 3, 2), (2, 2, 3), (5, 3), (3, 5), (2, 2, 4), (4, 2, 2), (2, 2, 2, 2)]:
        n, f = table(ss); c = wht(f); S = np.arange(1 << n); H = ent(c)
        st = (mp.mpf(0), mp.mpf(1), mp.mpf(1), mp.mpf(0), mp.mpf(0))
        for s in ss: st = step(st, s)
        errs = []
        for k in range(n):
            m = 1 << k; lo = S[(S & m) == 0]
            # restrictions: f with x_k = +1 is f[lo], with x_k = -1 is f[lo | m]
            Dk = H - (ent(wht(f[lo])) + ent(wht(f[lo | m]))) / 2
            Ik = float((c[lo | m] ** 2).sum()); Qk = float(np.abs(c[lo] * c[lo | m]).sum()) / Ik
            errs.append(max(abs(Dk - float(st[4])), abs(Ik - float(st[2])), abs(Qk - float(st[3] / st[2]))))
        e = max(errs); ok &= e < 1e-9
        print("levels %-13s n=%2d  recursion D/I=%.10f Q=%.6f  truth-table max err %.2e" % (ss, n, float(st[4] / st[2]), float(st[3] / st[2]), e))
    print("D, I, Q recursion equal the truth-table values on every case (err < 1e-9):", ok)
    mp.mp.dps = 1500  # Phi cancels to O(c1^2); c1^2 reaches ~1e-210 at eps=0.01, L=40, so 50 digits is not enough here
    for eps in (mp.mpf(1) / 4, mp.mpf("0.01")):
        st = (mp.mpf(0), mp.mpf(1), mp.mpf(1), mp.mpf(0), mp.mpf(0)); log2n = mp.mpf(0); worst = mp.mpf(0)
        for L in range(1, 41):
            mu = (1 - st[0]) / 2; s = 1
            while mu ** s > eps: s += 1
            st = step(st, s); log2n += mp.log(s, 2); r = st[4] / st[2]; worst = max(worst, r)
            if L in (1, 2, 3, 4, 5, 8, 10, 20, 30, 40):
                print("eps=%s L=%2d log2(n)=%8s  Q_k=%10s  D_k/I_k (nats)=%s" % (mp.nstr(eps, 3), L, mp.nstr(log2n, 6), mp.nstr(st[3] / st[2], 8), mp.nstr(r, 10)))
        print("eps=%s: max over L<=40 of D_k/I_k = %s nats = %s bits" % (mp.nstr(eps, 3), mp.nstr(worst, 10), mp.nstr(worst / mp.log(2), 10)))
