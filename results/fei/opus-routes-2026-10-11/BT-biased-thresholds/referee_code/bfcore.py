"""Referee core: exact biased Walsh analysis, written independently of the route's code/.

Conventions (match NOTES.md section 0):
  inputs y in {0,1}^n, bit i of an index = y_i, product law with P(y_i=1)=q_i (Fractions),
  sigma_i^2 = 4 q_i (1-q_i), phi_i = (y_i - q_i)/sqrt(q_i(1-q_i)),
  f = 2T-1 in {-1,1}; P(S) = fhat(S)^2;  E = sum_{S nonempty} P ln(sigma_S^2/P)  (nats).

Two independent ways to get P(S):
  * butterfly G-transform: fhat(S) = sigma_S * G[S], with per-coordinate (a,b) -> ((1-q)a+qb, (b-a)/2);
  * direct definition: fhat(S)^2 = (E[f prod_{i in S}(y_i-q_i)])^2 / prod_{i in S} q_i(1-q_i).
Everything rational is exact (Fractions).  Logarithms use mpmath (mp or iv).
"""
from fractions import Fraction as Fr
import itertools
import mpmath

mpmath.mp.dps = 60


def sig2(q):
    return 4 * q * (1 - q)


def popcount(x):
    return bin(x).count("1")


def gtrans(tab, qs):
    """Butterfly G-transform over all coordinates (bit i <-> qs[i])."""
    n = len(qs)
    G = list(tab)
    N = 1 << n
    for i in range(n):
        q = qs[i]
        bit = 1 << i
        for idx in range(N):
            if not idx & bit:
                a = G[idx]
                b = G[idx | bit]
                G[idx] = (1 - q) * a + q * b
                G[idx | bit] = (b - a) / 2
    return G


def sigS2(S, qs):
    r = Fr(1)
    i = 0
    while S:
        if S & 1:
            r *= sig2(qs[i])
        S >>= 1
        i += 1
    return r


def spectrum(ftab, qs):
    """ftab: +-1 values (ints).  Returns list P[S] (Fractions), exact."""
    G = gtrans([Fr(v) for v in ftab], qs)
    return [sigS2(S, qs) * G[S] * G[S] for S in range(len(G))]


def mu_weights(qs):
    n = len(qs)
    w = []
    for y in range(1 << n):
        p = Fr(1)
        for i in range(n):
            p *= qs[i] if (y >> i) & 1 else (1 - qs[i])
        w.append(p)
    return w


def spectrum_direct(ftab, qs):
    """Independent O(4^n) computation of P(S) from the definition."""
    n = len(qs)
    w = mu_weights(qs)
    P = []
    for S in range(1 << n):
        acc = Fr(0)
        for y in range(1 << n):
            prod = Fr(1)
            for i in range(n):
                if (S >> i) & 1:
                    prod *= ((y >> i) & 1) - qs[i]
            acc += w[y] * ftab[y] * prod
        den = Fr(1)
        for i in range(n):
            if (S >> i) & 1:
                den *= qs[i] * (1 - qs[i])
        P.append(acc * acc / den)
    return P


def metrics_exact(P):
    """Exact rational V, I, Delta, J from the spectrum."""
    V = sum(P[S] for S in range(1, len(P)))
    I = sum(popcount(S) * P[S] for S in range(len(P)))
    D = sum((popcount(S) - 1) * P[S] for S in range(len(P)) if popcount(S) >= 2)
    J = sum(popcount(S) * P[S] for S in range(len(P)) if popcount(S) >= 2)
    return V, I, D, J


def mpq(x):
    """mpf of a Fraction at current precision."""
    return mpmath.mpf(x.numerator) / x.denominator


def ivq(x):
    return mpmath.iv.mpf(x.numerator) / x.denominator


def corrected_entropy(P, qs, ctx=None, only_ge2=False):
    """E = sum_{S nonempty} P ln(sigma_S^2/P) as mpf (ctx=None) or iv interval (ctx='iv')."""
    tot = mpmath.iv.mpf(0) if ctx == "iv" else mpmath.mpf(0)
    for S in range(1, len(P)):
        if only_ge2 and popcount(S) < 2:
            continue
        p = P[S]
        if p == 0:
            continue
        ratio = sigS2(S, qs) / p
        if ctx == "iv":
            tot += ivq(p) * mpmath.iv.log(ivq(ratio))
        else:
            tot += mpq(p) * mpmath.log(mpq(ratio))
    return tot


def xlnx_inv(x, ctx=None):
    """x ln(1/x) for a Fraction x>=0."""
    if x == 0:
        return mpmath.iv.mpf(0) if ctx == "iv" else mpmath.mpf(0)
    if ctx == "iv":
        return ivq(x) * mpmath.iv.log(ivq(1 / x))
    return mpq(x) * mpmath.log(mpq(1 / x))


def is_monotone(tab, n):
    for y in range(1 << n):
        for i in range(n):
            if not (y >> i) & 1:
                if tab[y] > tab[y | (1 << i)]:
                    return False
    return True


def desirability_ok(tab, n, order):
    """order: list of coordinates, earlier = more desirable.
    Check T(y^{a<-1,b<-0}) >= T(y^{a<-0,b<-1}) for a earlier than b, all y."""
    pos = {c: k for k, c in enumerate(order)}
    for a in range(n):
        for b in range(n):
            if a == b or pos[a] > pos[b]:
                continue
            for y in range(1 << n):
                ya = (y | (1 << a)) & ~(1 << b)
                yb = (y | (1 << b)) & ~(1 << a)
                if tab[ya] < tab[yb]:
                    return False
    return True


def regular_order(tab, n):
    """Return a desirability order if T is regular monotone, else None."""
    for order in itertools.permutations(range(n)):
        if desirability_ok(tab, n, list(order)):
            return list(order)
    return None


def pivotal(tab, n, i):
    """d_i(y) = T(y^{i<-1}) - T(y^{i<-0}) as a table over all y (independent of y_i)."""
    bit = 1 << i
    return [tab[y | bit] - tab[y & ~bit] for y in range(1 << n)]


def threshold_table(w, theta):
    n = len(w)
    return [1 if sum(w[i] for i in range(n) if (y >> i) & 1) >= theta else 0 for y in range(1 << n)]
