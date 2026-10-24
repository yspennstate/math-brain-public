import math
import random

rng = random.Random(20260924)
min_slack = float('inf')
max_ratio = 0.0
cases = 0

for m in range(2, 50):
    for _ in range(1000):
        s = [rng.gauss(0.0, 1.0) for _ in range(m)]
        t = [rng.gauss(0.0, 1.0) for _ in range(m)]
        sigma = 10.0 ** rng.uniform(-3.0, 3.0)
        ss = sum(x*x for x in s)
        tt = sum(x*x for x in t)
        S = sigma*sigma*sum((x*y)**2 for x, y in zip(s, t))
        R2 = sigma*sigma*ss*tt
        slack = R2-S
        assert slack >= -1e-10*max(1.0, R2)
        min_slack = min(min_slack, slack)
        if R2 > 0.0:
            max_ratio = max(max_ratio, S/R2)
        cases += 1

constants = {
    'direct_V1': 6.0*(3125.0/4.0)**(1.0/6.0),
    'L1_V1': 12.0*math.pi*(3125.0/4.0)**(1.0/6.0),
    'direct_abs': 6.0*3125.0**(1.0/6.0),
    'L1_abs': 12.0*math.pi*3125.0**(1.0/6.0),
    'partner_base': 2.0**(29.0/12.0)*3.0**(1.0/4.0),
    'partner_V1': 2.0**(29.0/12.0)*3.0**(1.0/4.0)*(3125.0/4.0)**(1.0/8.0),
    'partner_abs': 2.0**(29.0/12.0)*3.0**(1.0/4.0)*3125.0**(1.0/8.0),
}

print('QFORM_B02_R40_GROUPED_SCHUR_CHECK_PASS')
print('cases', cases)
print('min_slack', repr(min_slack))
print('max_ratio_S_over_R2', repr(max_ratio))
for k, v in constants.items():
    print(k, repr(v))
