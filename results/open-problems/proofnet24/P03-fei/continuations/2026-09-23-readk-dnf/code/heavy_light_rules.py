# The heavy-plus-light family f = x_0 OR 1[N >= m/2] (weights (m, 1, ..., 1), threshold m/2, all biases 1/2) at large m,
# computed exactly by level.  With T = 1[N >= m/2] on the m light inputs, P(B + {0}) = P(B) = T~(B)^2 for nonempty B, and
# T~(B)^2 = 4^{-b} (backward difference of order b-1 at m/2 - 1 of the Bin(m-b, 1/2) pmf)^2.  Each set is divided among
# its elements with shares proportional to w^{-gamma}; the table gives max over coordinates of charge/budget
# (budget = sum of share * |A| * P(A)).  gamma = 0 is equal division (the damped scheme).
import mpmath as mp, sys

def binpmf(n):
    return [mp.binomial(n, k) / mp.mpf(2) ** n for k in range(n + 1)]

def table(m):
    mp.mp.dps = 60 + m                                  # order-b differences of a 2^-m pmf cancel ~m digits
    th = m // 2
    T2 = {}
    for b in range(1, m + 1):
        p = binpmf(m - b)
        get = lambda k: p[k] if 0 <= k <= m - b else mp.mpf(0)
        diff = mp.fsum((-1) ** k * mp.binomial(b - 1, k) * get(th - 1 - k) for k in range(b))
        T2[b] = diff ** 2 / mp.mpf(4) ** b
    # Parseval: sum_b C(m, b) T2[b] = Var(T) for the 0/1 function T = 1[N >= m/2]
    pT = mp.fsum(mp.binomial(m, k) for k in range(th, m + 1)) / mp.mpf(2) ** m
    pars = abs(mp.fsum(mp.binomial(m, b) * T2[b] for b in T2) - pT * (1 - pT)) / (pT * (1 - pT))
    out = {'parseval': pars}
    for gamma in (0, 1, 2):
        wh = mp.mpf(m) ** (-gamma)
        ch0 = bu0 = chl = bul = mp.mpf(0)
        for b in range(1, m + 1):
            t2 = T2[b]
            if t2 == 0: continue
            lg = mp.log(1 / t2)                      # sigma = 1 at bias 1/2
            h = wh / (wh + b); l = 1 / (wh + b)
            # sets {0} + B, |B| = b: C(m, b) of them for the heavy input, C(m-1, b-1) contain a given light input
            ch0 += mp.binomial(m, b) * h * t2 * lg; bu0 += mp.binomial(m, b) * h * (b + 1) * t2
            chl += mp.binomial(m - 1, b - 1) * l * t2 * lg; bul += mp.binomial(m - 1, b - 1) * l * (b + 1) * t2
            if b >= 2:                               # sets B inside the light inputs, shared equally
                chl += mp.binomial(m - 1, b - 1) * t2 * lg / b; bul += mp.binomial(m - 1, b - 1) * t2
        out[gamma] = (ch0 / bu0, chl / bul)
    return out

for m in [8, 32, 128, 512]:
    o = table(m)
    print('m %4d  ' % m + '   '.join('gamma %d: heavy %.3f light %.3f' % (g, float(o[g][0]), float(o[g][1])) for g in (0, 1, 2))
          + '   Parseval rel err %s' % mp.nstr(o['parseval'], 3), flush=True)
