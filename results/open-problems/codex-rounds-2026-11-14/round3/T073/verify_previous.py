"""Independent check of the preceding worker's finite claims; no file writes."""
import os
import resource
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
from fractions import Fraction as Q
from itertools import product
from math import comb

def g(k):
    return min(2, max(0, k-1))

counts = {}
for low in product((0,1), repeat=4):
    for high in product((0,1), repeat=4):
        if any(l > h for l,h in zip(low,high)):
            continue
        D = [h-l for l,h in zip(low,high)]
        blocked = sum(D[i] for i in range(4)
                      if len({low[j] for j in range(4) if j != i}) == 1
                      and all(low[j] == high[j] for j in range(4) if j != i))
        increment = g(sum(high))-g(sum(low))
        assert increment <= sum(D)-blocked
        counts[sum(D)] = counts.get(sum(D),0)+1
assert sum(counts.values()) == 81
integral = sum(Q((-1)**j * comb(3,j), j+1) for j in range(4))
assert integral == Q(1,4)
e = Q(2481,10000)
C = (2-4*e)*(1-e**3/2)
assert C == Q(4999531215835321,5000000000000000) < 1
lo = Q(558619565237287,2251799813685248)
hi = Q(69827445654661,281474976710656)
def f(e):
    return (2-4*e)*(1-e**3/2)-1
assert f(lo)>0>f(hi)
print('PASS: ordered pairs by M:', counts)
print('PASS: independent integral:', integral)
print('PASS: earlier endpoint contraction:', C)
print('PASS: earlier exact root bracket signs')
print('priority:',os.getpriority(os.PRIO_PROCESS,0))
print('peak_rss_bytes_macos:',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
