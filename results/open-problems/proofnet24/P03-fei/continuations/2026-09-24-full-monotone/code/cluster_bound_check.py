"""Exact check of every inequality in the cluster-coding proof, on small monotone DNFs.

Families of clusters <-> sets J of terms (J -> its connected components in the overlap graph).
a_J = q(V(J)) (-1)^{|J|} 2^{-|V(J)|};  Zhat(T) = (-1)^{|T|} sum_{J in F(T)} a_J, where F(T) = {J : V(J) >= T and
every component of J meets T};  P(T) = 4 Zhat(T)^2 for T nonempty.
Checked, for beta in {1, 2, 3}:
 (A) P(T) = 4 (sum_{J in F(T)} a_J)^2                                          [cluster formula]
 (B) sum_T P(T) min_J sp_J(T) <= 4 (diag_sp + off_sp)                          [Cauchy-Schwarz / min <= average]
     sp_J(T) = total size of the components of J with |T cap V(c)| < |V(c)|/beta
     diag_sp = sum_J a_J^2 sum_{T in Tset(J)} sp_J(T),  off_sp = sum_{J != J'} |a_J||a_J'| sum_{T in both} sp_J(T)
 (C) I >= 4 (diagI - offI), diagI = sum_J a_J^2 sum_{T in Tset(J)} |T|, offI = sum_{J != J'} |a_J||a_J'| sum_{both} |T|
 (D) H <= h(eps) + eps*Lambda + 2 sum_T P(T) min_{J in F(T)} (|V(J)| + comp-count*log2(1/c))  with the cluster reference
     p_gamma = c 2^{-|V(gamma)|}, Lambda = sum over clusters log2(1/(1 - p_gamma))  (c = 1 here)
Also printed: the ratios off/diag that the theorem needs to be small.
"""
import itertools, functools, math
import numpy as np
print = functools.partial(print, flush=True)


def wht(v):
    a = v.astype(np.float64).copy(); n = a.size; h = 1
    while h < n:
        a = a.reshape(-1, 2 * h); x = a[:, :h].copy(); y = a[:, h:].copy()
        a[:, :h] = x + y; a[:, h:] = x - y; a = a.reshape(n); h *= 2
    return a / n


def pc(x):
    return bin(x).count('1')


def comps_of(J, terms):
    J = list(J); out = []; seen = set()
    for t in J:
        if t in seen:
            continue
        stack = [t]; comp = [t]; seen.add(t)
        while stack:
            u = stack.pop()
            for s in J:
                if s not in seen and terms[s] & terms[u]:
                    seen.add(s); stack.append(s); comp.append(s)
        V = 0
        for s in comp:
            V |= terms[s]
        out.append(V)
    return out


def analyse(n, terms, betas=(1, 2, 3)):
    m = len(terms); N = 1 << n; x = np.arange(N)
    Z = np.ones(N)
    for t in terms:
        Z[(x & t) == t] = 0.0
    q = Z.mean()
    Zh = wht(Z)
    P = 4 * Zh ** 2; P[0] = (2 * q - 1) ** 2
    eps = 1 - P[0]
    pcs = np.array([pc(t) for t in range(N)])
    I = float((P * pcs).sum())
    phi = lambda p: -p * math.log2(p) if p > 0 else 0.0
    H = sum(phi(p) for p in P)
    qc = {}
    def qU(U):
        if U not in qc:
            ok = np.ones(N, dtype=bool)
            for t in terms:
                if not (t & U):
                    ok &= (x & t) != t
            qc[U] = ok.mean()
        return qc[U]
    fams = []   # (J, comps, V, a)
    for r in range(m + 1):
        for J in itertools.combinations(range(m), r):
            cs = comps_of(J, terms)
            V = 0
            for c in cs:
                V |= c
            a = qU(V) * (-1) ** r * 2.0 ** (-pc(V))
            fams.append((J, cs, V, a))
    # F(T) membership
    def members(T):
        return [k for k, (J, cs, V, a) in enumerate(fams) if (V & T) == T and all(c & T for c in cs)]
    mem = [members(T) for T in range(N)]
    # (A)
    errA = 0.0
    for T in range(1, N):
        s = sum(fams[k][3] for k in mem[T])
        errA = max(errA, abs(4 * s * s - P[T]))
    # clusters for the vacuum
    clusters = set()
    for r in range(1, m + 1):
        for J in itertools.combinations(range(m), r):
            if len(comps_of(J, terms)) == 1:
                clusters.add(J)
    Lam = 0.0
    for J in clusters:
        V = 0
        for t in J:
            V |= terms[t]
        p = 2.0 ** (-pc(V))
        Lam += math.log2(1 / (1 - p)) if p < 1 else float('inf')
    out = {'H': H, 'I': I, 'eps': eps, 'q': q, 'errA': errA, 'Lam': Lam}
    # (C)
    diagI = 0.0; offI = 0.0
    for T in range(1, N):
        ks = mem[T]
        for k in ks:
            diagI += fams[k][3] ** 2 * pc(T)
        for k in ks:
            for k2 in ks:
                if k2 != k:
                    offI += abs(fams[k][3]) * abs(fams[k2][3]) * pc(T)
    out['diagI'] = 4 * diagI; out['offI'] = 4 * offI
    out['C_ok'] = I >= 4 * (diagI - offI) - 1e-12
    for beta in betas:
        def sp(k, T):
            return sum(pc(c) for c in fams[k][1] if pc(T & c) < pc(c) / beta)
        lhs = 0.0; diag = 0.0; off = 0.0; mincover = 0.0
        for T in range(1, N):
            ks = mem[T]
            if not ks:
                continue
            lhs += P[T] * min(sp(k, T) for k in ks)
            mincover += P[T] * min(pc(fams[k][2]) for k in ks)
            for k in ks:
                diag += fams[k][3] ** 2 * sp(k, T)
                for k2 in ks:
                    if k2 != k:
                        off += abs(fams[k][3]) * abs(fams[k2][3]) * sp(k, T)
        hb = (lambda e: 0 if e <= 0 or e >= 1 else -e * math.log2(e) - (1 - e) * math.log2(1 - e))(eps)
        bound = hb + eps * Lam + 2 * mincover
        out[beta] = dict(lhs=lhs, rhs=4 * (diag + off), diag=4 * diag, off=4 * off, B_ok=lhs <= 4 * (diag + off) + 1e-12,
                         dense_ok=mincover <= beta * I + lhs + 1e-12, gibbs=bound, D_ok=H <= bound + 1e-9)
    return out


def main():
    rng = np.random.default_rng(3)
    cases = []
    # tribes (no overlaps), a matching-like 2-DNF, near-disjoint and heavily overlapping random DNFs
    cases.append(('tribes 3x3', 9, [0b000000111, 0b000111000, 0b111000000]))
    cases.append(('path 2-DNF', 7, [0b11 << i for i in range(6)]))
    for trial in range(10):
        n = int(rng.integers(8, 12)); m = int(rng.integers(3, 7)); ts = []
        w = int(rng.integers(2, 5))
        for _ in range(m):
            ts.append(int(sum(1 << int(i) for i in rng.choice(n, size=w, replace=False))))
        ts = [t for t in dict.fromkeys(ts)]
        ts = [t for t in ts if not any((s != t and (s & t) == s) for s in ts)]   # antichain
        cases.append((f'random w={w} #{trial}', n, ts))
    for name, n, ts in cases:
        o = analyse(n, ts)
        print(f"{name:18s} n={n:2d} m={len(ts)}: H/I={o['H']/o['I']:.3f} q={o['q']:.3f} errA={o['errA']:.1e} "
              f"(C) {'ok' if o['C_ok'] else 'FAIL'} offI/diagI={o['offI']/max(o['diagI'],1e-300):.3f}")
        for beta in (1, 2, 3):
            b = o[beta]
            print(f"      beta={beta}: (B) {'ok' if b['B_ok'] else 'FAIL'} lhs={b['lhs']:.4f} rhs={b['rhs']:.4f} "
                  f"off/diag={b['off']/max(b['diag'],1e-300):.3f}; dense {'ok' if b['dense_ok'] else 'FAIL'}; "
                  f"(D) {'ok' if b['D_ok'] else 'FAIL'} Gibbs bound/I={b['gibbs']/o['I']:.2f} vs H/I={o['H']/o['I']:.3f}")


if __name__ == "__main__":
    main()
