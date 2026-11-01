"""H and I of all AND/OR chains (decision lists = lexicographic LTFs, weights 2^i with any
threshold) of length n, via the exact AND-composition formulas (Hod 2017, Lemma 3.1; read-once
report section 2).  A chain is G_1 = x_1, G_{k+1} = AND(x_{k+1}, G_k) or OR(x_{k+1}, G_k).
Pr = probability of 'true' (= -1).  Vectorised over all 2^(n-1) chains.
Optionally the bottom of the chain is an arbitrary function with given (p, H, I)."""
import sys
import numpy as np

try:
    import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
except Exception:
    pass


def phi(w):
    w = np.asarray(w, dtype=np.float64)
    out = np.zeros_like(w)
    m = w > 1e-300
    out[m] = -w[m] * np.log2(w[m])
    return out


def hbin(v):
    v = np.asarray(v, dtype=np.float64)
    return phi(v) + phi(1 - v)


def and_compose(p, Ha, Ia, q, Hb, Ib):
    """g = AND(a, b), Pr[a]=p, Pr[b]=q."""
    Vp = 4 * p * (1 - p); Vq = 4 * q * (1 - q)
    Ita = q * Vp; Itb = p * Vq
    wE = (1 - 2 * p * q) ** 2
    wab = wE + Ita + Itb - 1
    Ht = phi(wE) + phi(Ita - wab) + phi(Itb - wab) + phi(wab)
    Hp_a = np.where(Vp > 0, (Ha - hbin(Vp)) / np.where(Vp > 0, Vp, 1), 0.0)
    Hp_b = np.where(Vq > 0, (Hb - hbin(Vq)) / np.where(Vq > 0, Vq, 1), 0.0)
    H = Ita * Hp_a + Itb * Hp_b + Ht
    I = q * Ia + p * Ib
    return p * q, H, I


def extend(P, H, I):
    """All one-step extensions by a fresh variable x: AND(x, G) and OR(x, G)."""
    half = np.full_like(P, 0.5); zero = np.zeros_like(P); one = np.ones_like(P)
    pa, Ha, Ia = and_compose(half, zero, one, P, H, I)
    po, Ho, Io = and_compose(half, zero, one, 1 - P, H, I)  # OR = not AND(not x, not G)
    po = 1 - po
    return (np.concatenate([pa, po]), np.concatenate([Ha, Ho]), np.concatenate([Ia, Io]))


def all_chains(n, base=(0.5, 0.0, 1.0)):
    P = np.array([base[0]]); H = np.array([base[1]]); I = np.array([base[2]])
    for k in range(n - 1):
        P, H, I = extend(P, H, I)
    return P, H, I


if __name__ == "__main__":
    for n in [int(a) for a in sys.argv[1:]]:
        P, H, I = all_chains(n)
        r = H / I
        k = np.argmax(r)
        print("n=%d chains=%d best H/I=%.8f at p=%.6g (AND_n: %.8f)" % (n, len(r), r[k], P[k], r[np.argmin(P)]))
