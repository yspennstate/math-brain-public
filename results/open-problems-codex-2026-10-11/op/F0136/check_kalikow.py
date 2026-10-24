from fractions import Fraction as F
from pathlib import Path
import json

root = Path(__file__).resolve().parent
alpha = [F(10, 32), F(4, 32), F(9, 32), F(4, 32)]
a, b = alpha[0], alpha[2]
A = sum(alpha)
delta = a-b
kappa = 2*A-max(a+b, alpha[1]+alpha[3])
c = F(1)
minus_sum = plus_sum = F(0)
prefixes = []
for n in range(8):
    minus = c*(delta-n)/(A+n)
    plus = c*(delta+n)/(A+n)
    minus_sum += minus
    plus_sum += plus
    if n >= 1:
        assert minus < 0
    assert plus > 0
    prefixes.append(dict(n=n, term=str(minus), signed_partial_sum=str(minus_sum),
                         positive_pair_sum=str(plus_sum), decimal=float(minus_sum)))
    c *= (a+n)*(b+n)/(A+n)**2
assert prefixes[1]['signed_partial_sum'] == '-133/4779'
assert kappa == F(35, 32) > 1 and delta == F(1, 32) > 0

family = []
for j in range(1, 101):
    eps = F(j, 3200)
    aa = b+eps
    total = aa+b+F(1, 4)
    kk = 2*total-max(aa+b, F(1, 4))
    lhs = eps*total*(total+1)
    rhs = aa*b*(1-eps)
    assert lhs < rhs
    assert kk == F(17, 16)+eps > 1
    family.append(dict(epsilon=str(eps), kappa=str(kk),
                       negative_prefix_condition_margin=str(rhs-lhs)))

result = dict(alpha=[str(x) for x in alpha], A=str(A), delta=str(delta),
              kappa=str(kappa), signed_sums=prefixes,
              family_exact_rational_tests=family,
              limitation='Checks the auxiliary-kernel obstruction, not zero speed or the failure of (T).')
(root/'kalikow_probe.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(dict(prefix=prefixes[1]['signed_partial_sum'],
                     kappa=str(kappa), family_tests=len(family),
                     status='all exact rational assertions passed'), indent=2))
