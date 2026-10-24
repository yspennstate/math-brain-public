"""Exact recheck (Fractions + prime factorisation of log arguments, mpmath 40 digits) of
min over relevant i of B_i/Inf_i for (a) f = -1 iff sum x_i 2^i < 3 on 5 uniform bits (lexicographic t=3),
(b) the 3-bit point defect (should equal K*), (c) lexicographic t=13 on 7 bits."""
from fractions import Fraction
import mpmath as mp, json, sys
mp.mp.dps = 40
def factor(q):
    d = {}
    for val, sg in ((q.numerator, 1), (q.denominator, -1)):
        v = val; pr = 2
        while v > 1:
            while v % pr == 0:
                d[pr] = d.get(pr, 0) + sg; v //= pr
            pr += 1
    return d
def exact_min_ratio(n, fneg):
    N = 1 << n
    W = [sum((-1 if fneg(x) else 1) * (-1) ** bin(S & x).count('1') for x in range(N)) for S in range(N)]
    p = [Fraction(w * w, N * N) for w in W]
    out = []
    for i in range(n):
        bit = 1 << i; tot = {}; Inf = Fraction(0)
        for T in range(N):
            if T & bit: continue
            pa, pb = p[T], p[T | bit]; Inf += pb; m = pa + pb
            for x in (pa, pb):
                if 0 < x < m:
                    for pr, e in factor(m / x).items():
                        tot[pr] = tot.get(pr, Fraction(0)) + x * e
        if Inf == 0: continue
        val = sum(mp.mpf(v.numerator) / v.denominator * mp.log(pr, 2) for pr, v in tot.items()) / (mp.mpf(Inf.numerator) / Inf.denominator)
        out.append((i, {str(k): str(v / Inf) for k, v in tot.items() if v != 0}, mp.nstr(val, 30)))
    best = min(out, key=lambda r: mp.mpf(r[2]))
    return {'min_ratio': best[2], 'coord': best[0], 'coeffs_of_log2_primes': best[1], 'all_coords': [(r[0], r[2]) for r in out]}
Kstar = 4 + mp.mpf(5) / 2 * mp.log(5, 2) - mp.mpf(9) / 2 * mp.log(3, 2)
res = {'Kstar': mp.nstr(Kstar, 30),
       'lex5_t3': exact_min_ratio(5, lambda x: x < 3),
       'pointdefect3': exact_min_ratio(3, lambda x: x == 0),
       'lex7_t13': exact_min_ratio(7, lambda x: x < 13)}
res['lex5_t3_minus_Kstar'] = mp.nstr(mp.mpf(res['lex5_t3']['min_ratio']) - Kstar, 20)
res['lex7_t13_minus_Kstar'] = mp.nstr(mp.mpf(res['lex7_t13']['min_ratio']) - Kstar, 20)
json.dump(res, open(sys.argv[1], 'w', encoding='utf-8'), indent=1)
print(json.dumps(res, indent=1)[:3500])
