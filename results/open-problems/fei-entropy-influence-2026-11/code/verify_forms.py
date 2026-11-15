"""Check the up-set decomposition of Fourier entropy on all 4-variable Boolean functions
and on random / structured functions with more variables.

mu(S)   = fhat(S)^2
up(S)   = sum_{U >= S} mu(U) = E[(D_S f)^2]
A       = sum mu(S) log2(1/up(S))
B       = sum mu(S) log2(up(S)/mu(S))
H = A + B (identity);  claims: A <= B + 2I - 2,  H <= 2B + 2I - 2,
B_lam <= B <= B_lam + I log2(1/(1-lam)),
T0: H <= 2 Hlev + 2I - 2 + 2 sum_k W_k log2(sum_j W_j C(j,k)).
"""
import numpy as np, itertools, math, sys

def wht(a):
    a = a.copy().astype(np.float64)
    n = a.shape[-1].bit_length() - 1
    h = 1
    while h < a.shape[-1]:
        a = a.reshape(a.shape[:-1] + (-1, 2, h))
        x = a[..., 0, :] + a[..., 1, :]
        y = a[..., 0, :] - a[..., 1, :]
        a = np.stack([x, y], axis=-2).reshape(a.shape[:-3] + (-1,))
        h *= 2
    return a / a.shape[-1]

def upsum(m, lam=1.0):
    """up_lam(S) = sum_{U>=S} m(U) lam^{|U\S|}"""
    m = m.copy()
    N = m.shape[-1]
    n = N.bit_length() - 1
    idx = np.arange(N)
    for i in range(n):
        lo = idx[(idx >> i) & 1 == 0]
        m[..., lo] = m[..., lo] + lam * m[..., lo | (1 << i)]
    return m

def stats(F, lam=0.5):
    """F: (M, 2^n) array of +-1 truth tables."""
    N = F.shape[-1]; n = N.bit_length() - 1
    fh = wht(F); mu = fh ** 2
    pc = np.array([bin(s).count('1') for s in range(N)])
    I = (mu * pc).sum(-1)
    with np.errstate(divide='ignore', invalid='ignore'):
        H = np.where(mu > 0, -mu * np.log2(mu), 0).sum(-1)
        up = upsum(mu); upl = upsum(mu, lam)
        A = np.where(mu > 0, -mu * np.log2(up), 0).sum(-1)
        B = np.where(mu > 0, mu * np.log2(up / mu), 0).sum(-1)
        Bl = np.where(mu > 0, mu * np.log2(up / upl), 0).sum(-1)
    W = np.stack([mu[..., pc == k].sum(-1) for k in range(n + 1)], -1)
    with np.errstate(divide='ignore', invalid='ignore'):
        Hlev = np.where(W > 0, -W * np.log2(W), 0).sum(-1)
        T = np.zeros(F.shape[0])
        for k in range(n + 1):
            mom = sum(W[..., j] * math.comb(j, k) for j in range(k, n + 1))
            T += np.where(W[..., k] > 0, W[..., k] * np.log2(np.maximum(mom, 1e-300)), 0)
    T0 = 2 * Hlev + 2 * I - 2 + 2 * T
    return dict(H=H, I=I, A=A, B=B, Bl=Bl, T0=T0, Hlev=Hlev)

def report(name, F, lam=0.5):
    s = stats(F, lam)
    H, I, A, B, Bl, T0 = (s[k] for k in ('H', 'I', 'A', 'B', 'Bl', 'T0'))
    nz = I > 1e-12
    e = 1e-9
    print(f"== {name}: {F.shape[0]} functions, {nz.sum()} non-constant")
    print("  max |H-(A+B)|            ", np.abs(H - A - B).max())
    print("  max A-(B+2I-2)   (<=0?)  ", (A - (B + 2 * I - 2))[nz].max())
    print("  max H-(2B+2I-2)  (<=0?)  ", (H - (2 * B + 2 * I - 2))[nz].max())
    print("  max Bl-B         (<=0?)  ", (Bl - B).max())
    print("  max B-Bl-I*log2(1/(1-lam)) (<=0?)", (B - Bl - I * math.log2(1 / (1 - lam))).max())
    print("  max H-T0         (<=0?)  ", (H - T0)[nz].max())
    for nm, num in (('H/I', H), ('B/I', B), ('A/I', A), ('Bl/I', Bl), ('T0/I', T0)):
        r = np.where(nz, num / np.maximum(I, 1e-300), -1)
        j = int(r.argmax())
        print(f"  sup {nm:5s} = {r[j]:.6f}  at I={I[j]:.4f} H={H[j]:.4f}")
    return s

if __name__ == '__main__':
    n = 4
    N = 1 << n
    tt = np.arange(1 << N, dtype=np.uint32)
    F = 1 - 2 * ((tt[:, None] >> np.arange(N)[None, :]) & 1).astype(np.float64)
    report('all n=4', F)
    rng = np.random.default_rng(1)
    for n, M in ((5, 200000), (6, 100000), (8, 20000)):
        F = rng.choice([-1.0, 1.0], size=(M, 1 << n))
        report(f'random n={n}', F)
        # biased random
        for p in (0.1, 0.03):
            F = np.where(rng.random((M // 4, 1 << n)) < p, -1.0, 1.0)
            report(f'random n={n} bias {p}', F)
    # structured: majority, tribes, AND
    def table(n, fn):
        return np.array([[fn([(x >> i) & 1 for i in range(n)]) for x in range(1 << n)]], dtype=np.float64)
    for n in (3, 5, 7, 9, 11, 13):
        report(f'majority {n}', table(n, lambda b: 1 - 2 * (sum(b) > n // 2)))
    for w, t in ((2, 2), (2, 3), (3, 3), (3, 4), (4, 3)):
        report(f'tribes w={w} t={t}', table(w * t, lambda b: 1 - 2 * any(all(b[i * w:(i + 1) * w]) for i in range(t))))
    for n in (2, 3, 6, 10):
        report(f'AND {n}', table(n, lambda b: 1 - 2 * all(b)))
