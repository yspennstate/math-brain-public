"""B03 lead: exact spectrum of the projective-plane union PP_q = OR_{lines L} AND(L), q = 2,3,4.

Frozen spec (written before running):
  family   : PP_q on the points of PG(2,q); variable i true <-> bit i = 1; g = 1[some line all true]; f = 2g-1.
  domain   : q in {2,3,4} only (n = 7, 13, 21); no automatic escalation.
  arithmetic: integer Walsh-Hadamard transform (exact), Fractions for influences/masses,
             entropy as an exact finite sum grouped by |W| and evaluated with mpmath at 60 digits.
  checks   : (1) I from Inf_j counts equals sum |S| W^2/4^n exactly.
             (2) interference remainder r = d_j g - sum_{L ni j} E_L: exact ||r||^2 vs proved bound 2q(q+1)^2 4^-q.
             (3) Cauchy-Schwarz loss actually realised by the paper's least-line pieces of d_j f.
             (4) spectral mass on sets with |S|>=2 inside one line vs the rest.
  memory   : < 250 MB at q = 4 (arrays of 2^21 int64 / float64, processed sequentially).
  runtime  : < 3 minutes.
"""
import sys, json, itertools, time
from fractions import Fraction
import numpy as np
import mpmath as mp

mp.mp.dps = 60
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'


# ---------- finite fields GF(2), GF(3), GF(4) ----------
def field(q):
    if q in (2, 3):
        els = list(range(q))
        add = lambda a, b: (a + b) % q
        mul = lambda a, b: (a * b) % q
        return els, add, mul
    if q == 4:  # elements 0,1,2=w,3=w+1 with w^2 = w+1 ; addition = xor on 2-bit vectors
        els = [0, 1, 2, 3]
        add = lambda a, b: a ^ b
        def mul(a, b):
            # polynomial multiplication mod x^2+x+1 over GF(2)
            r = 0
            for i in range(2):
                if (b >> i) & 1:
                    r ^= a << i
            if r & 4:
                r ^= 0b111
            return r
        return els, add, mul
    raise ValueError(q)


def proj_plane(q):
    els, add, mul = field(q)
    vecs = [v for v in itertools.product(els, repeat=3) if any(v)]
    # normalise: first nonzero coordinate = 1
    def norm(v):
        for c in v:
            if c:
                # find inverse of c
                inv = next(e for e in els if mul(c, e) == 1)
                return tuple(mul(inv, x) for x in v)
    pts = sorted(set(norm(v) for v in vecs))
    idx = {p: i for i, p in enumerate(pts)}
    lines = []
    for L in pts:  # dual coordinates
        on = [idx[p] for p in pts if add(add(mul(L[0], p[0]), mul(L[1], p[1])), mul(L[2], p[2])) == 0]
        lines.append(sorted(on))
    return len(pts), lines


def wht(a):
    a = a.astype(np.int64).copy()
    n = a.shape[0]
    h = 1
    while h < n:
        a = a.reshape(-1, 2, h)
        x = a[:, 0, :].copy()
        y = a[:, 1, :].copy()
        a[:, 0, :] = x + y
        a[:, 1, :] = x - y
        a = a.reshape(n)
        h *= 2
    return a


def entropy_exact(W, n):
    """H = sum_S p log2(1/p), p = W^2/4^n, grouped by |W| (exact finite sum, mpmath evaluation)."""
    vals, cnts = np.unique(np.abs(W[W != 0]), return_counts=True)
    H = mp.mpf(0)
    four_n = mp.mpf(4) ** n
    for v, c in zip(vals.tolist(), cnts.tolist()):
        p = mp.mpf(v) ** 2 / four_n
        H += c * p * mp.log(1 / p, 2)
    return H


def main():
    res = {}
    t0 = time.time()
    for q in (2, 3, 4):
        n, lines = proj_plane(q)
        assert n == q * q + q + 1 and len(lines) == n and all(len(L) == q + 1 for L in lines)
        # every point on q+1 lines, two lines meet in exactly one point
        for i in range(n):
            assert sum(i in L for L in lines) == q + 1
        for L1, L2 in itertools.combinations(lines, 2):
            assert len(set(L1) & set(L2)) == 1
        N = 1 << n
        X = np.arange(N, dtype=np.int64)
        masks = [sum(1 << i for i in L) for L in lines]
        g = np.zeros(N, dtype=bool)
        for m in masks:
            g |= (X & m) == m
        f = np.where(g, 1, -1).astype(np.int64)
        W = wht(f)
        assert int(W[0]) == int(f.sum())
        pc = np.zeros(N, dtype=np.int64)
        for i in range(n):
            pc += (X >> i) & 1
        four_n = 4 ** n
        # check Parseval
        assert int((W * W).sum()) == four_n * N // N * 1 or True
        tot = int(np.sum(W.astype(object) ** 2)) if n <= 13 else int(np.sum((W // 1) ** 2))
        assert tot == four_n, (tot, four_n)
        I_spec = Fraction(int(np.sum((W * W) * pc)), four_n)
        # influences by counting
        infl = []
        for j in range(n):
            flip = X ^ (1 << j)
            infl.append(Fraction(int(np.count_nonzero(f != f[flip])), N))
        I_cnt = sum(infl)
        assert I_cnt == I_spec, (I_cnt, I_spec)
        H = entropy_exact(W, n)
        k = q + 1
        # mass classification
        nz = W != 0
        inline = np.zeros(N, dtype=bool)
        for m in masks:
            inline |= (X & ~m) == 0
        line_sets = inline & (pc >= 2) & nz
        other = nz & ~line_sets & (X != 0)
        m_line = Fraction(int(np.sum(W[line_sets] ** 2)), four_n)
        m_other = Fraction(int(np.sum(W[other] ** 2)), four_n)
        I_line = Fraction(int(np.sum(W[line_sets] ** 2 * pc[line_sets])), four_n)
        I_other = Fraction(int(np.sum(W[other] ** 2 * pc[other])), four_n)
        # interference at coordinate j = 0 (PG(2,q) is point-transitive)
        j = 0
        hi = X | (1 << j)
        lo = X & ~(1 << j)
        dg = (g[hi].astype(np.int64) - g[lo].astype(np.int64))  # in {0,1}
        assert dg.min() >= 0
        thr = [L for L in lines if j in L]
        EL = []
        for L in thr:
            mm = sum(1 << i for i in L if i != j)
            EL.append(((X & mm) == mm).astype(np.int64))
        S = sum(EL)
        r = dg - S
        r2 = Fraction(int(np.sum(r * r)), N)
        infj = Fraction(int(np.sum(dg * dg)), N)
        assert infj == infl[j]
        bound = Fraction(2 * q * (q + 1) ** 2, 4 ** q)
        assert r2 <= bound, (r2, bound)
        # paper pieces: least line through j for which j is pivotal for that AND (E_L = 1)
        least = np.full(N, -1, dtype=np.int64)
        for t in range(len(thr) - 1, -1, -1):
            least = np.where(EL[t] == 1, t, least)
        Wd = wht(dg).astype(np.float64)
        num = Wd ** 2  # proportional to nu_j(T) * Inf_j * N^2
        den = np.zeros(N, dtype=np.float64)
        alphas = []
        for t in range(len(thr)):
            piece = np.where(least == t, dg, 0)
            a_t = int(np.sum(piece * piece))
            alphas.append(a_t)
            Wp = wht(piece).astype(np.float64)
            den += Wp ** 2  # sum_l alpha_l nu_l(T) * N^2 (unnormalised)
            del Wp, piece
        alphas = np.array(alphas, dtype=np.float64)
        a = alphas / alphas.sum()
        Keff = float(np.sum(np.sqrt(a)) ** 2)
        pos = den > 0
        ratio_max = float(np.max(num[pos] / den[pos]))
        # mass of nu_j above the piece mixture, and TV distance
        nu = num / num.sum()
        mix = den / den.sum()
        excess = float(np.sum(np.maximum(nu - mix, 0)))
        out = dict(q=q, n=n, k=k, lines=len(lines), I=str(I_cnt), I_float=float(I_cnt),
                   H=mp.nstr(H, 25), H_over_I=mp.nstr(H / mp.mpf(I_cnt.numerator) * I_cnt.denominator, 20),
                   paper_bound_41_7logk=41 + 7 * float(mp.log(k, 2)),
                   Inf_j=str(infj), Inf_j_float=float(infj),
                   r2=str(r2), r2_float=float(r2), r2_bound=str(bound), r2_bound_float=float(bound),
                   r2_over_Inf_j=float(r2 / infj),
                   pieces=len(thr), piece_masses=[int(x) for x in alphas], K_eff=Keff,
                   CS_loss_max_ratio=ratio_max, nu_excess_over_piece_mixture=excess,
                   mass_line_sets=str(m_line), mass_line_sets_float=float(m_line),
                   mass_other_nonempty=str(m_other), mass_other_float=float(m_other),
                   I_line_sets=float(I_line), I_other=float(I_other),
                   mean_size_line_sets=float(I_line / m_line) if m_line else None,
                   seconds=round(time.time() - t0, 2))
        res[q] = out
        print(json.dumps(out, indent=1))
        del W, f, g, X, pc, inline, dg, S, r, EL, least, Wd, num, den, nu, mix
    with open(OUT + '/pp_exact.json', 'w', encoding='utf8') as fh:
        json.dump(res, fh, indent=1)


if __name__ == '__main__':
    main()
