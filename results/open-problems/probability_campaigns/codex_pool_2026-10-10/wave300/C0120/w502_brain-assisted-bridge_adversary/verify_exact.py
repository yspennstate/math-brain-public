"""Small exhaustive arithmetic check of the task's explicit cube counterexample.

Not a blind/test-bank item or a stochastic experiment. It does not certify the
polymer conjecture or replace independent mathematical review.
"""
from itertools import product
from pathlib import Path
import json
import math
import time

t = time.monotonic()
points = tuple(product((-1, 1), repeat=3))
def f(x):
    return x[0] if x[1] == x[2] == 1 else 0
derivatives = [(f(x) - f((-x[0], x[1], x[2]))) / 2 for x in points]
l1 = sum(abs(d) for d in derivatives) / len(points)
l2sq = sum(d*d for d in derivatives) / len(points)
assert l1 == 1/4 and l2sq == 1/4
ratio = math.sqrt(l2sq) / l1
denominator = 1 + math.log(ratio)
assert ratio == 2 and denominator > 1
result = {
    'command':'python -X utf8 verify_exact.py',
    'points':len(points), 'derivative_nonzero_points':sum(d!=0 for d in derivatives),
    'l1':l1, 'l2_squared':l2sq, 'l2':math.sqrt(l2sq),
    'norm_ratio':ratio, 'talagrand_denominator':denominator,
    'term_relative_to_efron_stein':1/denominator,
    'statement':'Refutes only the returned card explanatory clause; no variance-conjecture or theorem-proof certificate.',
    'elapsed_seconds':time.monotonic()-t,
}
Path(__file__).with_name('exact_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
