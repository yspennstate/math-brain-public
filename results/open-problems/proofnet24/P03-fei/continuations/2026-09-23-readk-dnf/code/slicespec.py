"""Threshold gates Thr_{t,r} under i.i.d. bias p: the derivative is the slice indicator D = 1[|y| = t-1] on r-1
coordinates. Its biased spectral level law nu(u) (u = |T|) and normalized coefficients b_u satisfy
  sum_{u>=1} nu(u) log2(1/b_u^2)/(u+1)  <=?  C nu(u >= 1)      (this is exactly the non-singleton FEI+ part).
We measure, over r <= 60, all t, and p on a log grid:
  Q  = sum_{u>=1} nu(u) log2(1/b_u^2)/(u+1) / nu(u>=1)           (the per-unit cost; must stay bounded)
  NS = max_K nu(u <= K) / sqrt(K/A),  A = (r-1) sigma^2           (biased noise sensitivity, rank-tail form)
  LV = E_nu[ min(u, L) ] / L with L = log2(1/pi)                  (does the level reach log(1/pi)?)
Exact with mpmath (the Krawtchouk sums alternate)."""
import mpmath as mp
mp.mp.dps = 60

def slice_law(r, t, p):
    p = mp.mpf(p); q = 1 - p; s2 = 4 * p * q; n = r - 1; k = t - 1
    pi = mp.binomial(n, k) * p ** k * q ** (n - k)
    nu = []; b2 = []
    for u in range(n + 1):
        m = n - u
        # b_u = 2^{-u} sum_c Pr[Bin(m,p)=c] (-1)^{u-(k-c)} C(u, k-c)
        acc = mp.mpf(0)
        for c in range(max(0, k - u), min(m, k) + 1):
            acc += mp.binomial(m, c) * p ** c * q ** (m - c) * (-1) ** (u - (k - c)) * mp.binomial(u, k - c)
        b = acc / mp.mpf(2) ** u
        w = mp.binomial(n, u) * s2 ** u * b * b          # level mass of D (total should be pi)
        nu.append(w); b2.append(b * b)
    tot = mp.fsum(nu)
    assert abs(tot - pi) < mp.mpf('1e-40') * max(1, pi) + mp.mpf('1e-50'), (tot, pi)
    nu = [w / pi for w in nu]
    return nu, b2, pi, n * s2

worstQ = (0, None); worstNS = (0, None); worstLV = (mp.inf, None)
ps = [mp.mpf(10) ** (-e) for e in (1, 2, 3, 5)] + [mp.mpf(x) / 10 for x in (2, 3, 4, 5)]
for r in list(range(3, 21)) + [25, 30, 40, 60]:
    for t in range(1, r + 1):
        for p in ps:
            nu, b2, pi, A = slice_law(r, t, p)
            m1 = mp.fsum(nu[1:])
            if m1 < mp.mpf('1e-40'): continue
            Q = mp.fsum([nu[u] * mp.log(1 / b2[u], 2) / (u + 1) for u in range(1, len(nu)) if b2[u] > 0]) / m1
            if Q > worstQ[0]: worstQ = (Q, (r, t, mp.nstr(p, 3)))
            if A > 1:
                cum = mp.mpf(0)
                for K in range(0, len(nu)):
                    cum += nu[K]
                    if K >= 1:
                        v = cum / mp.sqrt(K / A)
                        if v > worstNS[0]: worstNS = (v, (r, t, mp.nstr(p, 3), K))
            L = mp.log(1 / pi, 2)
            if L > 2:
                lv = mp.fsum([nu[u] * min(u, L) for u in range(len(nu))]) / L
                if lv < worstLV[0]: worstLV = (lv, (r, t, mp.nstr(p, 3)))
print('max per-unit non-singleton cost Q =', mp.nstr(worstQ[0], 6), 'at (r,t,p)', worstQ[1])
print('max nu(u<=K)/sqrt(K/A) over A>1 =', mp.nstr(worstNS[0], 6), 'at (r,t,p,K)', worstNS[1])
print('min E[min(u,L)]/L with L = log2(1/pi) > 2 =', mp.nstr(worstLV[0], 6), 'at (r,t,p)', worstLV[1])
