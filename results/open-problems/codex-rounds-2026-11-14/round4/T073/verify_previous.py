"""Independent, read-only audit of both earlier uniqueness criteria."""
import os
import resource
from fractions import Fraction as F
from itertools import product
from math import comb, factorial

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))

# Encode the ordered states as common 0, discrepancy, common 1.
# Calculate the probability difference directly from the task's update rule.
e = F(1, 5)
a = F(1, 2) - e
p = [e, e, F(1, 2), 1-e, 1-e]
counts = [0]*5
for states in product(range(3), repeat=4):
    lower = [int(v == 2) for v in states]
    upper = [int(v != 0) for v in states]
    m = states.count(1)
    blocked = sum(states[i] == 1 and
                  (all(states[j] == 0 for j in range(4) if j != i) or
                   all(states[j] == 2 for j in range(4) if j != i))
                  for i in range(4))
    delta = (p[sum(upper)]-p[sum(lower)])/a
    assert delta <= m-blocked-F(comb(m, 3), 2)
    counts[m] += 1
assert counts == [16, 32, 24, 8, 1]

# Count linear extensions by recursively removing minimal elements,
# independently of the previous script's permutation enumeration.
prereq = {0:set(), 1:set(), 2:set(), 3:set(),
          4:{0,1}, 5:{1,2}, 6:{2,3}}
def count(remaining):
    if not remaining:
        return 1
    return sum(count(remaining-{v}) for v in remaining
               if not (prereq[v] & remaining))
n = count(set(prereq))
assert n == 272
integral = sum(F((-1)**j*comb(7,j), j+1) for j in range(8))
assert integral == F(1, 8)
assert 2*F(n, factorial(7))*integral == F(17,1260)

def c0(t):
    return (2-4*t)*(1-t**3/2)
def c1(t):
    return c0(t)-F(17,630)*t**4*(F(1,2)-t)**4
lo = F(146438707495522750369, 590295810358705651712)
hi = F(1171509659964182002953, 4722366482869645213696)
assert c1(lo)>1>c1(hi)
endpoint = F(24807685,10**8)
assert c1(endpoint)<1<c0(endpoint)
assert c0(F(2481,10000)) == F(4999531215835321,5000000000000000)

print('PASS: 81 local ordered pairs, counts', counts)
print('PASS: earlier triple clock count', n)
print('PASS: triple age integral', integral, 'and coefficient', F(17,1260))
print('PASS: both earlier root/endpoint claims')
print('nice:', os.getpriority(os.PRIO_PROCESS,0))
print('peak_rss_bytes_macos:', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
