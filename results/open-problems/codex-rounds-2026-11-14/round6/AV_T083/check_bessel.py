"""Exact finite audits of the height-bin and scalar Bessel proof.

Run: OMP_NUM_THREADS=1 nice -n 15 python3 -B check_bessel.py
Only standard-library arithmetic; no files written, network, or workers.
"""

from fractions import Fraction as F
from itertools import product
from collections import Counter
from pathlib import Path
import math
import os
import resource
import time

started = time.monotonic()
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))


def floorlog2(x):
    assert x > 0
    k = x.numerator.bit_length() - x.denominator.bit_length()
    if x < F(2)**k:
        k -= 1
    assert F(2)**k <= x < F(2)**(k+1)
    return k


def budgets(p, b):
    h = math.factorial(p) * b**(p*p+p)
    ratio = 4*p*h
    ceiling = (ratio-1).bit_length()
    assert 2**ceiling >= ratio
    assert ceiling == 0 or 2**(ceiling-1) < ratio
    return ratio, p*(ceiling+2)


scenarios = [
    (3, (F(1),)),
    (3, (F(1), F(2)**40)),
    (2, (F(1), F(2)**40, F(2)**40 + F(1, 2)**40)),
    (3, (F(1), -F(1) + F(1, 2)**60)),
    (2, (F(0), F(0), F(0))),
    (2, (F(0),)),
]
range_checks = multiplicity_checks = scale_checks = separation_checks = 0
maximum_bins = maximum_ranges = 0
nonzero_tiny_seen = exact_zero_seen = False

for b, theta in scenarios:
    d, p = len(theta), len(theta)+1
    q = sorted({F(n, den) for den in range(1, b+1)
                for n in range(-b, b+1)})
    assert len(q) <= 3*b*b
    centers = sorted({sum((a*t for a, t in zip(v, theta)), F(0))
                      for v in product(q, repeat=d)})
    assert len(centers) <= (3*b*b)**d
    ratio, scale_bound = budgets(p, b)
    # Include exact center hits and a nonzero Fourier frequency extremely
    # close to a center; magnitude and signs of theta are unrestricted.
    xis = {F(0), F(1, 2), -centers[0], -centers[-1],
           -centers[len(centers)//2] + F(1, 2)**80}
    data = []
    all_lengths = set()
    for xi in sorted(xis):
        magnitudes = sorted({abs(xi+nu) for nu in centers if xi+nu})
        exact_zero_seen |= any(xi+nu == 0 for nu in centers)
        nonzero_tiny_seen |= any(0 < v < F(1, 2)**50 for v in magnitudes)
        bins = {floorlog2(v) for v in magnitudes}
        maximum_bins = max(maximum_bins, len(bins))
        # Direct greedy covering, independently of the number-of-bins test.
        starts = []
        for v in magnitudes:
            if not starts or v > ratio*starts[-1]:
                starts.append(v)
        assert len(starts) <= p
        assert all(any(s <= v <= ratio*s for s in starts)
                   for v in magnitudes)
        maximum_ranges = max(maximum_ranges, len(starts))
        assert len(bins) <= scale_bound
        range_checks += 1
        if bins:
            # Independent enumeration of all integer lengths for shell 0.
            brute = {k for k in range(-max(bins), -min(bins)+1)
                     if any(1 <= F(2)**k*v < 2 for v in magnitudes)}
            assert brute == {-j for j in bins}
            assert len(brute) <= scale_bound
            scale_checks += 1
        for ell in range(-6, 7):
            all_lengths.update(ell-j for j in bins)
        data.append((xi, bins))

    # A single center selection for each length, shared by all testing xi.
    # Greedy selection has the exact permitted minimum separation 1/r.
    selected = {}
    for k in sorted(all_lengths):
        spacing = F(2)**(-k)
        keep = []
        for nu in centers:
            if not keep or nu-keep[-1] >= spacing:
                keep.append(nu)
        assert all(v-u >= spacing for u, v in zip(keep, keep[1:]))
        separation_checks += 1
        selected[k] = keep

    for xi, bins in data:
        total = Counter()
        scales = {ell: set() for ell in range(-6, 7)}
        for k, keep in selected.items():
            local = Counter()
            for nu in keep:
                if xi+nu:
                    ell = k + floorlog2(abs(xi+nu))
                    if -6 <= ell <= 6:
                        # Compare logarithmic indexing against the actual
                        # shell inequalities, including equality endpoints.
                        assert F(2)**ell <= F(2)**k*abs(xi+nu) < F(2)**(ell+1)
                        local[ell] += 1
                        scales[ell].add(k)
            for ell, count in local.items():
                assert count <= 2*(1+F(2)**ell)
                total[ell] += count
        for ell in range(-6, 7):
            assert len(scales[ell]) <= scale_bound
            assert total[ell] <= 2*scale_bound*(1+F(2)**ell)
            multiplicity_checks += 1

assert nonzero_tiny_seen and exact_zero_seen
print(f'height-range checks={range_checks}; direct scale enumerations={scale_checks}')
print(f'global separated-center selections={separation_checks}; shell multiplicity checks={multiplicity_checks}')
print(f'maximum occupied magnitude bins={maximum_bins}; maximum greedy ranges={maximum_ranges}')
print('exact zeros, signs, 2^40 frequencies and nonzero <2^-50 cancellations exercised')


def add(a, b):
    return [(a[i] if i < len(a) else F(0))
            + (b[i] if i < len(b) else F(0))
            for i in range(max(len(a), len(b)))]


def mul(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def deriv(a):
    return [i*x for i, x in enumerate(a) if i] or [F(0)]


def integ(a):
    return [F(0)] + [x/F(i+1) for i, x in enumerate(a)]


def value(a, t):
    return sum((x*t**i for i, x in enumerate(a)), F(0))


def integral(a, left=F(0), right=F(1)):
    z = integ(a)
    return value(z, right)-value(z, left)


def compose(a, inner):
    ans, power = [F(0)], [F(1)]
    for x in a:
        ans = add(ans, [x*y for y in power])
        power = mul(power, inner)
    return ans


# w(t)=t^3(1-t)^3(t-1/2); insert in y in [1/4,3/4]
# with t=2y-1/2 and set it to zero elsewhere. Its extension is C^2.
w = mul(mul([F(0)]*3+[F(1)], [F(1), F(-3), F(3), F(-1)]),
        [F(-1, 2), F(1)])
assert integral(w) == 0
for j in range(3):
    assert value(w, F(0)) == value(w, F(1)) == 0
    w = deriv(w) if j < 2 else w
w0 = mul(mul([F(0)]*3+[F(1)], [F(1), F(-3), F(3), F(-1)]),
         [F(-1, 2), F(1)])
omega = compose(w0, [F(-1, 2), F(2)])
left, right = F(1, 4), F(3, 4)
assert integral(omega, left, right) == 0
assert integral(mul(omega, omega), left, right) > 0
a_bound = max(sum(abs(x) for x in z)*2**j
              for j, z in enumerate([w0, deriv(w0), deriv(deriv(w0))]))
identity_checks = 0
for n in range(15):
    u = add([F(0)]*n+[F(1)], [F(-2*(-1)**n), F(3*(-1)**n)])
    v = integ(integ(u))
    assert deriv(deriv(v)) == u
    original = integral(mul(omega, u), left, right)
    ibp = integral(mul(deriv(deriv(omega)), v), left, right)
    assert original == ibp
    mean = integral(u)
    centered = add(u, [-mean])
    variance = integral(mul(centered, centered))
    derivative_energy = integral(mul(deriv(u), deriv(u)))
    assert variance <= derivative_energy
    assert original**2 <= a_bound**2 * variance
    assert ibp**2 <= a_bound**2 * integral(mul(v, v), left, right)
    identity_checks += 1
print(f'exact interior C2 bump: A={a_bound}; cancellation, Poincare and double-antiderivative checks={identity_checks}')

# Negative control: allowing a different multiplier on every interval
# destroys a depth-independent Bessel bound, even at the sole center 0.
# For f=1 and psi_I=sign(omega_I), each depth contributes the same c^2.
absolute_mean = (integral(omega, F(1, 2), right)
                 - integral(omega, left, F(1, 2)))
assert absolute_mean > 0
assert absolute_mean == F(1, 8)*F(1, 2)**8 == F(1, 2048)
for depths in [1, 4, 8]:
    direct = sum((sum((F(1, 2)**s * absolute_mean**2
                       for _ in range(2**s)), F(0))
                  for s in range(depths)), F(0))
    assert direct == depths*absolute_mean**2
    assert depths*absolute_mean**2 / absolute_mean**2 == depths
print(f'variable-multiplier negative control: c={absolute_mean}; squared output at h depths=h*c^2')

# Independent finite sums plus exact remainders audit the infinite sums.
for n in range(1, 65):
    assert sum((F(1, 2)**j for j in range(1, n+1)), F(0)) + F(1, 2)**n == 1
    q = F(3, 8)  # rational majorant for 2^(-3/2)
    assert sum((q**j for j in range(n)), F(0)) + q**n/(1-q) == F(8, 5)
assert F(3, 8)**2 > F(1, 8)
assert F(176, 7) + F(4, 45) == F(7948, 315) < 26
assert 26**2 == 676
budget_checks = 0
for p, b in product(range(1, 16), [2, 3, 4, 16, 257]):
    ratio, s = budgets(p, b)
    upper = p*(5+(p+1)*math.log2(p)+(p*p+p)*math.log2(b))
    assert s <= upper
    assert upper <= 9*p**3*math.log2(2*p*b)
    budget_checks += 1
print(f'exact geometric-sum/remainder checks=128; rational constant 26 and square 676 passed')
print(f'supplementary budget comparisons={budget_checks}')

here = Path(__file__).resolve().parent
old = Path('~/codex_op_1114r5/briefs/AV_T083/sources')
for name in ['candidate1-introduction.tex', 'candidate2-introduction.tex',
             'candidate3-introduction.tex', 'candidate1-inputs.tex', 'candidate3-base.tex']:
    assert (here/'sources'/name).read_text().rstrip() == (old/name).read_text().rstrip()
if (here/'VERIFY.md').exists():
    verification = (here/'VERIFY.md').read_text()
    for n in range(1, 4):
        s = (here/'sources'/f'candidate{n}-introduction.tex').read_text()
        a = s.index(r'\begin{theorem}\label{thm:main}')
        b = s.index(r'\end{theorem}', a) + len(r'\end{theorem}')
        assert s[a:b] in verification
    print('three exact main-theorem quotation checks passed')
print('five fresh source comparisons with round 5 passed')
print(f'nice={os.getpriority(os.PRIO_PROCESS, 0)}')
print(f'peak RSS (macOS bytes)={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}')
print(f'elapsed seconds={time.monotonic()-started:.3f}')
