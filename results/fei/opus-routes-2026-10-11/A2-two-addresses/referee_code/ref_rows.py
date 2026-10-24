"""Exact per-row analysis for a two-address row (my own derivation of the route's Lemmas 1-6).

A row is given by the integer vector V[u] = W[T u U] (u indexes subsets U of C, |C| = m) of a Boolean f on
n = m + 2 variables, so ghat_T(U) = V[u] / 2^n.  Everything below is exact (Fractions / LogLin)."""
from fractions import Fraction
from math import isqrt, gcd
from refk2 import LogLin, factor_small


def v2(k):
    k = abs(int(k))
    if k == 0:
        return 10 ** 9
    e = 0
    while k % 2 == 0:
        k //= 2
        e += 1
    return e


def h_loglin(p, q):
    """binary entropy (bits) of m = q^2/(p^2+q^2), as LogLin: log2 S - 2 m log2 q - 2 (1-m) log2 p"""
    S = p * p + q * q
    m = Fraction(q * q, S)
    out = LogLin()
    out.add_log2_int(1, S)
    out.add_log2_int(-2 * m, q)
    out.add_log2_int(-2 * (1 - m), p)
    return out


def cstar():
    return LogLin(Fraction(16, 3), {3: Fraction(-3, 2)})


def analyse_row(V, m, n, tsize):
    """Returns None for a zero row, False if the law is not product, else a dict with the exact
    quantities of Lemmas 2, 3, 6 and the per-row values w e_T and w ebar_T (LogLin)."""
    V = [int(v) for v in V]
    a = [v * v for v in V]
    Z = sum(a)
    if Z == 0:
        return None
    D = 4 ** n
    w = Fraction(Z, D)
    alpha = [Fraction(sum(a[u] for u in range(1 << m) if (u >> i) & 1), Z) for i in range(m)]
    # product test
    for u in range(1 << m):
        pr = Fraction(1)
        for i in range(m):
            pr *= alpha[i] if (u >> i) & 1 else 1 - alpha[i]
        if Fraction(a[u], Z) != pr:
            return False
    D0 = [i for i in range(m) if alpha[i] == 0]
    D1 = [i for i in range(m) if alpha[i] == 1]
    R = [i for i in range(m) if 0 < alpha[i] < 1]
    r = len(R)
    pairs = []
    for i in R:
        mi = min(alpha[i], 1 - alpha[i])
        k2 = (1 - mi) / mi
        P, Q = k2.numerator, k2.denominator
        p, q = isqrt(P), isqrt(Q)
        assert p * p == P and q * q == Q, "ratio of a product row is not a rational square"
        assert gcd(p, q) == 1 and p >= q >= 1
        pairs.append((p, q, mi, alpha[i]))
    # Lemma 2: support is the full face {U : D1 subset U subset D1 u R}
    D1mask = sum(1 << i for i in D1)
    Rmask = sum(1 << i for i in R)
    for u in range(1 << m):
        on_face = (u & D1mask) == D1mask and (u & ~(D1mask | Rmask) & ((1 << m) - 1)) == 0
        assert (V[u] != 0) == on_face, "support is not the full face"
    # row values g_T(x) on C: g(x) = sum_U ghat(U) chi_U(x); 2^n g(x) = sum_u V[u] chi_u(x)
    gx = []
    for x in range(1 << m):
        s = 0
        for u in range(1 << m):
            s += V[u] * (-1 if bin(x & u).count("1") % 2 else 1)
        # g(x) = s / 2^n ;  must lie in {0, +-1/2, +-1}  (Lemma 1)
        gx.append(Fraction(s, 2 ** n))
    for g in gx:
        assert g in (0, Fraction(1, 2), Fraction(-1, 2), 1, -1), "row value outside {0,+-1/2,+-1}"
    # Lemma 3: kappa = min |phihat| = min |V| / 2^n over the support; nu = 2^(r+1) kappa
    kappa = Fraction(min(abs(v) for v in V if v != 0), 2 ** n)
    nu = kappa * 2 ** (r + 1)
    assert nu.denominator == 1, "nu not an integer"
    nu = nu.numerator
    prodq = 1
    for (p, q, _, _) in pairs:
        prodq *= q
    assert nu % prodq == 0, "prod q_i does not divide nu"
    nup = nu // prodq
    prodS = 1
    for (p, q, _, _) in pairs:
        prodS *= p * p + q * q
    assert w == Fraction(nup * nup * prodS, 4 ** (r + 1)), "weight formula fails"
    # class: number of points of the R-cube with |phi| = 1/2 ; phi(x_R) = chi_D1 * g ; |g| depends on x_R only
    # count over the full C-cube and divide by 2^(m - r)
    nhalf_full = sum(1 for g in gx if abs(g) == Fraction(1, 2))
    assert nhalf_full % (2 ** (m - r)) == 0
    nhalf = nhalf_full // 2 ** (m - r)
    # Lemma 5: |g| is a cylinder over R: check |g(x)| depends only on x_R
    for x in range(1 << m):
        xr = x & Rmask
        assert abs(gx[x]) == abs(gx[xr]), "|g| not a cylinder over R"
    odd_class = (nhalf % 2 == 1)
    # all 2^{r+1} phihat in one parity class
    par = set((abs(v) * 2 ** (r + 1) // 2 ** n) % 2 for v in V if v != 0) if True else None
    # 2^{r+1} phihat(U) = V * 2^{r+1} / 2^n must be an integer
    for v in V:
        assert (v * 2 ** (r + 1)) % (2 ** n) == 0
    pars = set(((v * 2 ** (r + 1)) // (2 ** n)) % 2 for v in V if v != 0)
    assert len(pars) == 1, "coefficients not in one class"
    assert (pars == {1}) == odd_class, "parity class does not match the half-point count"
    if odd_class:
        assert nup % 2 == 1 and all(p % 2 == 1 and q % 2 == 1 for (p, q, _, _) in pairs)
    else:
        assert nup % 2 == 0
    # Lemma 6
    ec = sum(1 for (p, q, _, _) in pairs if (p * p + q * q) % 2 == 1)
    zero_one = all(g in (0, 1, -1) for g in gx)
    assert 2 * v2(nup) >= ec + (2 if zero_one else 0), "Lemma 6 fails"
    # exact per-row e_T and the identity L + H(q) = 2 - 2 log2 nu' + sum Ft
    # w (L + H(q)) = sum_U ghat^2 log2(1/ghat^2) ; ghat = V/2^n
    wLH = LogLin()
    wI = Fraction(0)
    for u in range(1 << m):
        if V[u] == 0:
            continue
        p_ = Fraction(V[u] * V[u], D)
        wLH.q0 += p_ * 2 * n
        wLH.add_log2_int(-2 * p_, abs(V[u]))
        wI += p_ * (tsize + bin(u).count("1"))
    # identity check: L + H(q) == 2 - 2 log2 nu' + sum_i Ft(p_i, q_i)
    rhs = LogLin(Fraction(2))
    rhs.add_log2_int(-2, nup)
    for (p, q, _, _) in pairs:
        rhs.q0 += 2
        rhs.add_log2_int(-1, p * p + q * q)
        rhs.add(h_loglin(p, q))
    lhs = LogLin()
    lhs.add(wLH, Fraction(1) / w)
    diff = LogLin().add(lhs).add(rhs, -1).clean()
    assert diff.q0 == 0 and not diff.ql, "Lemma 3(c) identity fails"
    # w e_T = w(L + H) - c * w (|T| + I(q))  (exact)
    c = cstar()
    we = LogLin().add(wLH).add(c, -wI).clean()
    # ebar_T = 2 - 2 log2 nu' + delta f + sum_unf (Ft - c m) - c |T| ; delta = 2 - c/2
    nfair = sum(1 for (p, q, _, _) in pairs if p == q)
    eb = LogLin(Fraction(2))
    eb.add_log2_int(-2, nup)
    delta = LogLin(Fraction(2)).add(c, Fraction(-1, 2))
    eb.add(delta, nfair)
    for (p, q, mi, _) in pairs:
        if p == q:
            continue
        eb.q0 += 2
        eb.add_log2_int(-1, p * p + q * q)
        eb.add(h_loglin(p, q))
        eb.add(c, -mi)
    eb.add(c, -tsize)
    web = LogLin().add(eb, w).clean()
    return dict(w=w, alpha=alpha, D0=D0, D1=D1, R=R, r=r, pairs=[(p, q) for (p, q, _, _) in pairs],
                nu=nu, nup=nup, odd=odd_class, nhalf=nhalf, ec=ec, zero_one=zero_one, gx=gx,
                we=we, web=web, wI=wI, nfair=nfair)
