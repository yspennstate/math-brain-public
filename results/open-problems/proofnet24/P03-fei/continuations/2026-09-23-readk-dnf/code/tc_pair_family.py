# The family A = x_1 OR (x_2 AND ... AND x_{m+1}) (weights (m,1,...,1), threshold m), with q_i = q for the conjunction
# and q_1 = q^m, so the two branches of A are equally likely.  Predicted: rmin ~ (m/2) ln 2 (the one-step inequality
# fails), while alpha TC / I stays below (ln 2)/2.
import mpmath as mp
import tc_pairwise as T
for m in [2, 3, 4, 5, 6, 7]:
    for qe in [3, 6]:
        n = m + 1
        mp.mp.dps = 40 + qe * m * 2 + 2 * n
        q = [mp.mpf(10) ** (-qe * m)] + [mp.mpf(10) ** (-qe)] * m
        w = [float(m)] + [1.0] * m
        inA = [sum(w[i] for i in range(n) if (x >> i) & 1) >= m for x in range(1 << n)]
        o = T.analyse(n, q, inA, check_split=False)
        print('m', m, 'q 1e-%d' % qe, 'alpha TC/I %.4f' % float(o['tc']), 'rmin %.4f' % float(o['rmin']),
              '(m/2) ln2 %.4f' % (m / 2 * float(mp.log(2))), 'ravg %.4f' % float(o['ravg']))
