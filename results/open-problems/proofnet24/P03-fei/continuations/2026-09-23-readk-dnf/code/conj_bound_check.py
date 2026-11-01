# The damped ratio of the conjunction d = y_1 ... y_m under an arbitrary product measure.  With w_i = 1 - q_i and
# P_w the product measure on subsets (i in B with probability w_i), d~(B)^2 = rho P_w(B) (rho = prod q_i) and
#     Psi/Var = E_w[(|B| ln 4 + 2 sum_{i not in B} ln(1/q_i)) / (|B| + 1) | B != empty].
# Claimed bound: since q ln(1/q) <= 1 - q and sum_i w_i E[g(B \ {i})] = P(|B| >= 2) for g(S) = 1[S != empty]/(|S|+1),
#     Psi/Var <= ln 4 E[|B|/(|B|+1) | B != empty] + 2 P(|B| >= 2)/P(B != empty) < 2 + ln 4.
# Checks the formula against the direct biased transform (m <= 7) and the bound on random unequal biases (m <= 12).
import mpmath as mp, random, itertools
from slab_damped import biased_transform, popcount
mp.mp.dps = 60
rng = random.Random(7)
worst_ratio = mp.mpf(0); worst_slack = mp.mpf(10); maxerr = mp.mpf(0)
for t in range(300):
    m = rng.randint(1, 12)
    q = [mp.mpf(rng.choice([rng.uniform(0.001, 0.999), 1 - 10 ** -rng.uniform(1, 6), 10 ** -rng.uniform(1, 6)])) for _ in range(m)]
    w = [1 - x for x in q]
    rho = mp.fprod(q)
    num = mp.mpf(0); pos = mp.mpf(0); p2 = mp.mpf(0); lead = mp.mpf(0)
    for B in range(1, 1 << m):
        pB = mp.fprod(w[i] if (B >> i) & 1 else q[i] for i in range(m))
        b = popcount(B)
        num += pB * (b * mp.log(4) + 2 * mp.fsum(mp.log(1 / q[i]) for i in range(m) if not (B >> i) & 1)) / (b + 1)
        pos += pB; lead += pB * b / (b + 1)
        if b >= 2: p2 += pB
    ratio = num / pos
    bound = mp.log(4) * lead / pos + 2 * p2 / pos
    worst_ratio = max(worst_ratio, ratio)
    worst_slack = min(worst_slack, bound - ratio)
    if m <= 7:                                   # direct check of the formula
        d = [1 if y == (1 << m) - 1 else 0 for y in range(1 << m)]
        c = biased_transform(d, q)
        var = c[0] * (1 - c[0]); psi = mp.mpf(0)
        for B in range(1, 1 << m):
            sB = mp.fprod(4 * q[i] * (1 - q[i]) for i in range(m) if (B >> i) & 1)
            psi += c[B] ** 2 / (popcount(B) + 1) * mp.log(sB / c[B] ** 2)
        maxerr = max(maxerr, abs(psi / var - ratio) / ratio)
print('instances 300, m <= 12: max Psi/Var = %s (2 + ln 4 = %s); min(bound - ratio) = %s (must be >= 0); formula vs transform rel err %s'
      % (mp.nstr(worst_ratio, 8), mp.nstr(2 + mp.log(4), 8), mp.nstr(worst_slack, 4), mp.nstr(maxerr, 3)))
