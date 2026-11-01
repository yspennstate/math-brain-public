"""Block restriction along a minterm (or maxterm): is the block erasure O(E|S cap W|) where single coordinates fail?

For a block W, restricting all of W at once has step Delta_W = H(S cap W | S - W) + JS_W with
JS_W <= (2/ln 2) E|S cap W| (Gross's inequality on the W-cube), and I drops by E|S cap W|. So a class closed under
restrictions in which every nonconstant member has a block W with H(S cap W | S - W) <= K E|S cap W| satisfies
H <= (K + 2/ln 2) I. Every monotone function is the DNF of its minterms, so K uniform over minterm blocks would give
FEI for all monotone functions.

For each function: kappa_min = min over minterms and maxterms W of H(S cap W | S - W) / E|S cap W|, the exact block
step ratio Delta_W / E|S cap W| at that W, and for comparison min_v B_v / Inf_v and rho_0 = min_v Delta_v / Inf_v.
"""
import itertools
import sys
import functools
import numpy as np

print = functools.partial(print, flush=True)


def fwht(G):
    G = G.astype(np.float64).copy()
    N = G.shape[-1]
    h = 1
    while h < N:
        G = G.reshape(-1, N // (2 * h), 2, h)
        a = G[:, :, 0, :].copy(); b = G[:, :, 1, :]
        G[:, :, 0, :] = a + b; G[:, :, 1, :] = a - b
        G = G.reshape(-1, N)
        h *= 2
    return G / N


def phi(p):
    q = np.where(p > 1e-300, p, 1.0)
    return np.where(p > 1e-300, -p * np.log2(q), 0.0)


def spec(tt):
    F = np.where(tt, -1.0, 1.0)
    return fwht(F[None, :])[0] ** 2


def minterms(tt, n):
    ones = [x for x in range(1 << n) if tt[x]]
    mins = []
    for x in ones:
        if all(not tt[x & ~(1 << i)] for i in range(n) if (x >> i) & 1):
            mins.append(x)
    return mins


def maxterms(tt, n):
    # maxterm = minimal M with f(complement of M) = 0: minimal zeros-complements
    full = (1 << n) - 1
    zeros = [x for x in range(1 << n) if not tt[x]]
    maxz = [x for x in zeros if all(tt[x | (1 << i)] for i in range(n) if not (x >> i) & 1)]
    return [full & ~x for x in maxz]


def block_quantities(P, n, Wmask):
    """H(S cap W | S - W), E|S cap W|, exact block step Delta_W."""
    N = 1 << n
    idx = np.arange(N)
    rest = idx & ~Wmask
    H = phi(P).sum()
    marg = np.bincount(rest, weights=P, minlength=N)
    Hrest = phi(marg).sum()
    pcW = np.array([bin(x & Wmask).count('1') for x in range(N)])
    EW = float((P * pcW).sum())
    return H - Hrest, EW


def block_step(tt, n, Wmask):
    """Exact Delta_W = H(f) - average over x_W of H(f restricted)."""
    N = 1 << n
    Wbits = [i for i in range(n) if (Wmask >> i) & 1]
    rbits = [i for i in range(n) if not (Wmask >> i) & 1]
    H = phi(spec(tt)).sum()
    tot = 0.0
    for assign in itertools.product((0, 1), repeat=len(Wbits)):
        sub = []
        for r in range(1 << len(rbits)):
            x = 0
            for j, i in enumerate(rbits):
                if (r >> j) & 1:
                    x |= 1 << i
            for j, i in enumerate(Wbits):
                if assign[j]:
                    x |= 1 << i
            sub.append(tt[x])
        tot += phi(spec(np.array(sub))).sum()
    return H - tot / (1 << len(Wbits))


def coord_quantities(P, n):
    N = 1 << n
    idx = np.arange(N)
    out = []
    for v in range(n):
        low = idx[((idx >> v) & 1) == 0]
        X = P[low]; Y = P[low | (1 << v)]
        B = float((phi(X) + phi(Y) - phi(X + Y)).sum())
        out.append((B, float(Y.sum())))
    return out


def analyse(tt, n, want_step=True):
    P = spec(tt)
    I = float((P * np.array([bin(x).count('1') for x in range(1 << n)])).sum())
    if I < 1e-12:
        return None
    blocks = set(minterms(tt, n)) | set(maxterms(tt, n))
    best = None
    for W in blocks:
        if W == 0:
            continue
        HW, EW = block_quantities(P, n, W)
        if EW < 1e-15:
            continue
        r = HW / EW
        if best is None or r < best[0]:
            best = (r, W)
    cq = coord_quantities(P, n)
    bmin = min(B / inf for B, inf in cq if inf > 1e-15)
    res = {'kappa': best[0], 'W': best[1], 'bmin': bmin, 'HI': phi(P).sum() / I}
    if want_step:
        res['stepW'] = block_step(tt, n, best[1]) / block_quantities(P, n, best[1])[1]
    return res


def mono_all(n):
    sys.path.insert(0, 'code')
    from mono_enum import monotone_masks
    return monotone_masks(n)


def tt_from_mask(m, n):
    return np.array([(int(m) >> x) & 1 for x in range(1 << n)], dtype=bool)


def dnf_tt(n, terms):
    x = np.arange(1 << n)
    f = np.zeros(1 << n, dtype=bool)
    for t in terms:
        m = sum(1 << i for i in t)
        f |= (x & m) == m
    return f


def main():
    for n in range(2, 6):
        masks = mono_all(n)
        worst = None
        for m in masks:
            tt = tt_from_mask(m, n)
            r = analyse(tt, n, want_step=False)
            if r is None:
                continue
            if worst is None or r['kappa'] > worst[0]['kappa']:
                worst = (r, int(m))
        r, m = worst
        tt = tt_from_mask(m, n)
        st = block_step(tt, n, r['W']) / block_quantities(spec(tt), n, r['W'])[1]
        print(f"all monotone n={n}: max over f of min-block kappa = {r['kappa']:.4f} (block step ratio there {st:.4f}; "
              f"min_v B_v/Inf_v there {r['bmin']:.4f}, H/I {r['HI']:.4f})")
    fams = []
    for k in (2, 3, 4, 5, 6, 7, 8):
        fams.append((f'matching{k}', 2 * k, [(2 * i, 2 * i + 1) for i in range(k)]))
    for k, t in ((3, 3), (3, 4), (4, 3), (4, 4), (3, 5), (2, 7)):
        fams.append((f'tribes{k}x{t}', k * t, [tuple(range(i * t, (i + 1) * t)) for i in range(k)]))
    E6 = list(itertools.combinations(range(6), 2))
    fams.append(('K6 triangle', 15, [tuple(E6.index(e) for e in itertools.combinations(T, 2)) for T in itertools.combinations(range(6), 3)]))
    E5 = list(itertools.combinations(range(5), 2))
    fams.append(('K5 triangle', 10, [tuple(E5.index(e) for e in itertools.combinations(T, 2)) for T in itertools.combinations(range(5), 3)]))
    for n in (5, 7, 9, 11, 13):
        fams.append((f'majority{n}', n, list(itertools.combinations(range(n), (n + 1) // 2))))
    rng = np.random.default_rng(7)
    for w in (2, 3, 4, 5):
        for trial in range(3):
            n = 14
            m = int(rng.integers(8, 20))
            terms = [tuple(sorted(rng.choice(n, size=w, replace=False))) for _ in range(m)]
            fams.append((f'random {w}-DNF #{trial} ({m} terms)', n, terms))
    for name, n, terms in fams:
        tt = dnf_tt(n, terms)
        r = analyse(tt, n, want_step=(n <= 14))
        if r is None:
            continue
        st = r.get('stepW', float('nan'))
        print(f"{name:28s} n={n:2d}: min-block kappa {r['kappa']:.4f} (|W|={bin(r['W']).count('1')}, block step "
              f"ratio {st:.4f}); min_v B_v/Inf_v {r['bmin']:.4f}; H/I {r['HI']:.4f}")


if __name__ == "__main__":
    main()
