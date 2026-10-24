"""Independent exact evaluator for FEI quantities (audit tool, written separately from the groups' code).

Conventions: a Boolean function is a +-1 truth table, entry x = f(x), bit i of x is coordinate i, -1 means TRUE.
p = Pr[f = -1] (probability of TRUE), mu = E f = 1 - 2p, V = 1 - mu^2 = 4p(1-p).

Exact parts use Python integers / Fractions; entropies are enclosed with python-flint arb balls (rigorous).

Node types for disjoint compositions:
    ("var",)                      a fresh variable: p = 1/2, I = 1, H = 0
    ("table", tab)                an explicit function on its own fresh variables (numpy int array of +-1)
    ("gate", tab, [child, ...])   gate tab on k inputs, input i fed by child i (all on disjoint variables)
"""
from fractions import Fraction
import numpy as np
import flint

flint.ctx.prec = 256          # bits of working precision for arb; results are rigorous balls anyway
LN2 = flint.arb(2).log()


def arb_log2_frac(q):
    """Rigorous enclosure of log2(q) for a positive Fraction q."""
    return (flint.arb(q.numerator).log() - flint.arb(q.denominator).log()) / LN2


def xlog_inv(w):
    """Rigorous enclosure of w*log2(1/w) for a Fraction 0 <= w <= 1 (0 at w = 0)."""
    if w == 0:
        return flint.arb(0)
    return -flint.arb(w.numerator) / w.denominator * arb_log2_frac(w)


def h2(v):
    """Binary entropy (bits) of a Fraction v, rigorous."""
    return xlog_inv(v) + xlog_inv(1 - v)


def walsh_int(tab):
    """Integer Walsh-Hadamard transform: W[S] = sum_x f(x) chi_S(x); fhat(S) = W[S]/2^n."""
    a = np.asarray(tab, dtype=np.int64).copy()
    h = 1
    while h < len(a):
        b = a.reshape(-1, 2 * h)
        x = b[:, :h].copy()
        y = b[:, h:].copy()
        b[:, :h] = x + y
        b[:, h:] = x - y
        h *= 2
    return a


def table_quantities(tab):
    """Exact p, I (Fractions) and rigorous H (arb) of an explicit +-1 table."""
    tab = np.asarray(tab)
    N = len(tab)
    n = N.bit_length() - 1
    assert 1 << n == N
    W = walsh_int(tab)
    D = N * N
    ptrue = Fraction(int(np.count_nonzero(tab == -1)), N)
    pc = np.array([bin(s).count("1") for s in range(N)], dtype=np.int64)
    W2 = W.astype(object) ** 2
    I = Fraction(int(sum(int(W2[s]) * int(pc[s]) for s in range(N) if W[s])), D)
    # group by |W| so that each distinct weight is logged once
    mags, counts = np.unique(np.abs(W[W != 0]), return_counts=True)
    H = flint.arb(0)
    for m, c in zip(mags.tolist(), counts.tolist()):
        H += int(c) * xlog_inv(Fraction(int(m) * int(m), D))
    assert sum(int(c) * int(m) * int(m) for m, c in zip(mags.tolist(), counts.tolist())) == D
    return ptrue, I, H


def biased_sq_coeffs(tab, ps):
    """Exact squared biased Fourier coefficients of gate tab (k inputs) at input TRUE-probabilities ps (Fractions).

    Returns an object array G2 with G2[T] = Ghat_mu(T)^2 (Fractions), T indexed by bitmask.
    Orthonormal basis for input i: phi_i(x) = (x - mu_i)/sqrt(V_i); Ghat_mu(T) = E_mu[G prod_{i in T} phi_i].
    Unnormalised a(T) = E_mu[G prod_{i in T}(x_i - mu_i)] is rational; Ghat^2 = a^2 / prod_{i in T} V_i.
    Axis step for coordinate i with q = Pr[x_i = -1] (so Pr[x_i=+1] = 1-q), A = value at x_i=+1, B = at x_i=-1:
        mean part   (1-q) A + q B
        phi part    (1-q)(1-mu) A + q(-1-mu) B = 2q(1-q) (A - B)       (since 1 - mu = 2q, -1 - mu = -2(1-q))
    """
    k = len(ps)
    arr = np.array([Fraction(int(v)) for v in np.asarray(tab).tolist()], dtype=object)
    N = 1 << k
    assert len(arr) == N
    for i in range(k):
        q = Fraction(ps[i])
        b = arr.reshape(-1, 2, 1 << i)      # axis i: index 0 -> bit i = 0 (x_i = +1), 1 -> bit i = 1 (x_i = -1)
        A = b[:, 0, :].copy()
        B = b[:, 1, :].copy()
        b[:, 0, :] = (1 - q) * A + q * B
        b[:, 1, :] = 2 * q * (1 - q) * (A - B)
    V = [4 * Fraction(p) * (1 - Fraction(p)) for p in ps]
    den = np.array([Fraction(1)] * N, dtype=object)
    idx = np.arange(N)
    for i in range(k):
        m = ((idx >> i) & 1).astype(bool)
        den[m] = den[m] * V[i]
    G2 = arr * arr / den
    return G2, arr[0]


def evaluate(node):
    """Returns (p_true, I, H) for a composition node; p_true, I exact Fractions, H an arb ball."""
    kind = node[0]
    if kind == "var":
        return Fraction(1, 2), Fraction(1), flint.arb(0)
    if kind == "table":
        return table_quantities(node[1])
    if kind == "gate":
        tab, children = node[1], node[2]
        ev = [evaluate(c) for c in children]
        ps = [e[0] for e in ev]
        k = len(ps)
        G2, E = biased_sq_coeffs(tab, ps)
        assert sum(G2) == 1, "biased Parseval failed"
        p_out = (1 - E) / 2          # E = Ghat_mu(empty) = E_mu[G]
        idx = np.arange(1 << k)
        It = [sum(G2[((idx >> i) & 1).astype(bool)]) for i in range(k)]
        V = [4 * p * (1 - p) for p in ps]
        Ht = flint.arb(0)
        vals = {}
        for T in range(1 << k):
            w = G2[T]
            if w:
                vals[w] = vals.get(w, 0) + 1
        for w, c in vals.items():
            Ht += c * xlog_inv(w)
        I = sum(It[i] / V[i] * ev[i][1] for i in range(k))
        H = Ht
        for i in range(k):
            H += flint.arb(It[i].numerator) / It[i].denominator / flint.arb(V[i].numerator) * V[i].denominator * (ev[i][2] - h2(V[i]))
        return p_out, I, H
    raise ValueError(kind)


def expand_table(node):
    """Build the full +-1 truth table of a composition (for small cross-checks). Returns (table, n)."""
    kind = node[0]
    if kind == "var":
        return np.array([1, -1], dtype=np.int64), 1
    if kind == "table":
        t = np.asarray(node[1], dtype=np.int64)
        return t, len(t).bit_length() - 1
    tab, children = np.asarray(node[1], dtype=np.int64), node[2]
    subs = [expand_table(c) for c in children]
    ntot = sum(s[1] for s in subs)
    N = 1 << ntot
    x = np.arange(N, dtype=np.int64)
    gate_index = np.zeros(N, dtype=np.int64)
    off = 0
    for i, (t, n) in enumerate(subs):
        local = (x >> off) & ((1 << n) - 1)
        bit = (t[local] == -1).astype(np.int64)
        gate_index |= bit << i
        off += n
    return tab[gate_index], ntot


def AND_table(k):
    """+-1 table of AND of k inputs (TRUE = -1): TRUE iff all inputs TRUE."""
    N = 1 << k
    t = np.ones(N, dtype=np.int64)
    t[N - 1] = -1
    return t


def OR_table(k):
    N = 1 << k
    t = -np.ones(N, dtype=np.int64)
    t[0] = 1
    return t


if __name__ == "__main__":
    # Controls. 1) Numaro's g directly: H/(I-1) must be 6.521845710923046575...
    g = np.load(r"~/mop-fei-opus/proofnet24/P03-fei/continuations/2026-09-22-opus-team/inputs/numaro18_pm1_table.npy").astype(np.int64)
    p, I, H = table_quantities(g)
    print("g: p =", p, " I =", I, " H =", H.str(20, radius=True))
    print("   H/(I-1) =", (H / (flint.arb(I.numerator) / I.denominator - 1)).str(22, radius=True))
    # 2) composition identity vs direct expansion on a small random composition
    rng = np.random.default_rng(1)
    for trial in range(5):
        G = rng.choice([-1, 1], size=8)
        c1 = ("gate", AND_table(2), [("var",), ("var",)])
        c2 = ("gate", OR_table(3), [("var",), ("gate", AND_table(2), [("var",), ("var",)]), ("var",)])
        c3 = ("table", rng.choice([-1, 1], size=16))
        node = ("gate", G, [c1, c2, c3])
        pc, Ic, Hc = evaluate(node)
        full, n = expand_table(node)
        pd, Id, Hd = table_quantities(full)
        ok = (pc == pd) and (Ic == Id) and bool(abs(Hc - Hd) < flint.arb("1e-60"))
        print(f"   trial {trial}: n={n} p {pc}=={pd} I {Ic}=={Id} H diff {(Hc-Hd).str(5)} ok={ok}")
    # 3) the fleet's biased point: one core coordinate at p = 3/8
    ps = [Fraction(3, 8)] + [Fraction(1, 2)] * 17
    node = ("gate", g, [("table", np.array([1, 1, 1, -1, -1, -1, 1, 1]))] + [("var",)] * 17)
    # first input: a 3-variable function with Pr[TRUE] = 3/8 (entries 3,4,5 TRUE)
    G2, E = biased_sq_coeffs(g, ps)
    k = 18
    idx = np.arange(1 << k)
    It1 = sum(G2[(idx & 1).astype(bool)])
    Ito = sum(G2[((idx >> i) & 1).astype(bool)].sum() for i in range(1, k))
    Ht = flint.arb(0)
    vals = {}
    for w in G2.tolist():
        if w: vals[w] = vals.get(w, 0) + 1
    for w, c in vals.items(): Ht += c * xlog_inv(w)
    print("   fleet point: p_out =", (1 - E) / 2, " It_1 =", It1, " sum_{i>=2} It_i =", Ito, " Htilde =", Ht.str(22, radius=True))
