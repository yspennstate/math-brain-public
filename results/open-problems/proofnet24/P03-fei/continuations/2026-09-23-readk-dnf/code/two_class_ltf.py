# The strengthened biased inequality for f = x_0 T_a + (1 - x_0) T_b with T_c = 1[N >= c], N the number of ones among m
# light inputs of bias q, x_0 a heavy input of bias q0 (every linear threshold function with one heavy input and m equal
# light ones has this form, a <= b).  Exact by level: for B inside the light inputs, |B| = k,
#     f~(B) = s^k (q0 D_k(a) + (1 - q0) D_k(b))  (k >= 1),     f~(B + {0}) = s0 s^k (D_k(a) - D_k(b))  (k >= 0),
# with s = sqrt(q(1-q)), s0 = sqrt(q0(1-q0)) and D_k(c) = sum_j (-1)^{k-j} C(k,j) P(N' >= c - j), N' ~ Bin(m - k, q).
# P(A) = 4 f~(A)^2.  Reports the largest ratio sum P ln(sigma^2/P) / (I - Var) in bits over a grid, against 2 + 4 log2 e.
import mpmath as mp, sys, itertools

def ratio(m, q, q0, a, b):
    mp.mp.dps = 80 + 7 * (m + 1)                     # the smallest cell probability is about (1e-6)^(m+1): 6 digits per input
    q = mp.mpf(q); q0 = mp.mpf(q0)
    s2 = q * (1 - q); s02 = q0 * (1 - q0)
    lhs = mp.mpf(0); I = mp.mpf(0); V = mp.mpf(0)
    for k in range(0, m + 1):
        n = m - k
        pmf = [mp.binomial(n, j) * q ** j * (1 - q) ** (n - j) for j in range(n + 1)]
        tail = [mp.mpf(0)] * (n + 2)
        for j in range(n, -1, -1): tail[j] = tail[j + 1] + pmf[j]
        def F(c):
            if c <= 0: return mp.mpf(1)
            if c > n: return mp.mpf(0)
            return tail[c]
        def D(c): return mp.fsum((-1) ** (k - j) * mp.binomial(k, j) * F(c - j) for j in range(k + 1))
        Da, Db = D(a), D(b)
        cnt = mp.binomial(m, k)
        sig_k = (4 * s2) ** k
        if k >= 1:
            PB = 4 * s2 ** k * (q0 * Da + (1 - q0) * Db) ** 2
            if PB > 0:
                lhs += cnt * PB * mp.log(sig_k / PB); I += cnt * k * PB; V += cnt * PB
        P0 = 4 * s02 * s2 ** k * (Da - Db) ** 2
        if P0 > 0:
            lhs += cnt * P0 * mp.log(4 * s02 * sig_k / P0); I += cnt * (k + 1) * P0; V += cnt * P0
    if I - V <= 0: return None
    return lhs / (I - V) / mp.log(2)

if __name__ == '__main__':
    ref = 2 + 4 / mp.log(2)
    best = (mp.mpf(0), None)
    grid_q = ['1e-6', '1e-3', '0.05', '0.3', '0.5', '0.7', '0.95', '0.999', '0.999999']
    for m in [int(x) for x in sys.argv[1].split(',')]:
        mbest = (mp.mpf(0), None)
        for q in grid_q:
            for q0 in grid_q:
                mean = float(q) * m
                cands = sorted(set([0, 1, 2, max(0, int(mean) - 1), int(mean), int(mean) + 1, int(mean) + 2, m // 2, m - 1, m]))
                for a, b in itertools.combinations_with_replacement(cands, 2):
                    if a == b: continue                                   # a < b, else x_0 is irrelevant
                    r = ratio(m, q, q0, a, b)
                    if r is not None and r > mbest[0]: mbest = (r, (m, q, q0, a, b))
        print('m %4d  max ratio %s bits at (m, q, q0, a, b) = %s   [2 + 4 log2 e = %s]' % (m, mp.nstr(mbest[0], 8), mbest[1], mp.nstr(ref, 8)), flush=True)
        if mbest[0] > best[0]: best = mbest
    print('DONE overall max %s at %s; exceeds 2 + 4 log2 e: %s' % (mp.nstr(best[0], 10), best[1], best[0] > ref + mp.mpf('1e-9')))
