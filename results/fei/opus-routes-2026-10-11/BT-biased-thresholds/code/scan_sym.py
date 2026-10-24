import math, time, sys
import mpmath as mp
import levels
from levels import spectrum_1group
def run(m, t, p, dps):
    mp.mp.dps = dps
    return spectrum_1group(lambda a: int(a >= t), m, mp.mpf(p))
t0 = time.time()
for mm in [2, 4, 8, 16, 24, 32, 40]:
    best = (0, None)
    for t in range(1, mm + 1):
        for p in ['0.5','0.3','0.1','0.03','0.01','0.001','0.7','0.9','0.97','0.99','0.999']:
            dps = 30 + int(3 * mm * max(1, abs(math.log10(min(float(p), 1 - float(p))))))
            r = run(mm, t, p, dps)
            if r['ratio_HD'] == r['ratio_HD'] and r['ratio_HD'] > best[0]:
                r2 = run(mm, t, p, dps + 40)
                best = (r['ratio_HD'], (t, p), abs(r['ratio_HD'] - r2['ratio_HD']))
    print('sym m', mm, 'best H+/Delta', round(best[0], 5), best[1], 'precision gap', best[2], round(time.time() - t0, 1), 's', flush=True)
