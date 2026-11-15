"""Independent deterministic audit; never imports or executes authors' code.

Run with a single BLAS thread. Outputs are also saved in referee_numeric.txt.
Enumeration uses quadratic dynamic programming for LIS, not pile sorting.
Mean series uses the hook-length formula, not Aitken/Cauchy--Binet.
"""
import itertools
import math
import time
from collections import Counter
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 40
START = time.monotonic()
LOG = []


def say(s):
    print(s, flush=True)
    LOG.append(s)


def num(x):
    return mp.mpf(x.numerator) / x.denominator if isinstance(x, Fraction) else mp.mpf(x)


def E(t, a, b):
    """Definition (1.3), directly summed with a geometric remainder test."""
    t = num(t)
    n = max(0, b-a)
    term = t**n / (mp.factorial(n)*mp.factorial(a+n-b))
    ans = term
    while term:
        ratio = t / ((n+1)*(a+n+1-b))
        term *= ratio
        n += 1
        ans += term
        next_ratio = t / ((n+1)*(a+n+1-b))
        if next_ratio < 1 and abs(term)*next_ratio/(1-next_ratio) < mp.power(10, -mp.mp.dps-8):
            break
    return ans


def p(t, a, b):
    if a < b:
        return mp.mpf(0)
    return num(t)**(a-b)/mp.factorial(a-b)


def determinant(obs, reverse_ties=False):
    """Accepts already sorted times and nondecreasing particle indices."""
    T, k = obs[-1]
    d = k-1
    if not d:
        return mp.exp(-num(T)), 0
    markers = [(s, z) for s, k in obs[:-1] for z in range(d-k+1)]
    if reverse_ties:
        markers.sort(key=lambda x: (x[0], -x[1]))
    q = len(markers)
    mat = mp.matrix(d+q)
    for i in range(d):
        for j in range(d):
            mat[i, j] = E(T, i, j)
        for a, (s, z) in enumerate(markers):
            mat[i, d+a] = p(s, z, i)
    for a, (s, z) in enumerate(markers):
        for j in range(d):
            mat[d+a, j] = -E(T-s, z, j)
        for b, (u, w) in enumerate(markers):
            mat[d+a, d+b] = -p(u-s, w, z) if s < u else 0
    return mp.exp(-num(T))*mp.det(mat), d+q


def lis_profile(perm):
    ends, best, profile = [], 0, [0]
    for j, value in enumerate(perm):
        v = 1+max((ends[i] for i in range(j) if perm[i] < value), default=0)
        ends.append(v)
        best = max(best, v)
        profile.append(best)
    return tuple(profile)


def compositions(n, r):
    if r == 1:
        yield (n,)
    else:
        for h in range(n+1):
            for rest in compositions(n-h, r-1):
                yield (h,)+rest


def enumeration(obs, profiles, cutoff=9):
    times, limits = zip(*obs)
    delta = [times[0]]+[times[j]-times[j-1] for j in range(1, len(times))]
    exact = Fraction(0)
    for n in range(cutoff+1):
        for h in compositions(n, len(obs)):
            levels = list(itertools.accumulate(h))
            good = sum(c for prof, c in profiles[n].items()
                       if all(prof[level] < k for level, k in zip(levels, limits)))
            w = Fraction(good, math.factorial(n))
            for dt, hh in zip(delta, h):
                w *= dt**hh/math.factorial(hh)
            exact += w
    # Rigorous upper bound on the omitted Poisson tail, from successive ratios.
    T = num(times[-1])
    lo = mp.exp(-T)*num(exact)
    first = mp.exp(-T)*T**(cutoff+1)/mp.factorial(cutoff+1)
    bound = first/(1-T/(cutoff+2))
    return lo, bound


def partitions_at_most(n, d, largest=None):
    if d == 0:
        if n == 0:
            yield ()
        return
    top = n if largest is None else min(n, largest)
    for v in range(top, (n+d-1)//d-1, -1):
        for rest in partitions_at_most(n-v, d-1, v):
            yield (v,)+rest


def hook_dimension(part, factorials):
    n, d = sum(part), len(part)
    # Equivalent to multiplying all hook lengths, specialized to <=3 rows.
    shifted = [part[j]+d-1-j for j in range(d)]
    numerator = factorials[n]
    for i in range(d):
        for j in range(i+1, d):
            numerator *= shifted[i]-shifted[j]
    denominator = math.prod(factorials[x] for x in shifted)
    quotient, remainder = divmod(numerator, denominator)
    assert remainder == 0
    return quotient


def toeplitz_survival(s, d):
    if d == 0:
        return mp.exp(-s)
    b = [mp.besseli(j, 2*mp.sqrt(s)) for j in range(d)]
    if d == 1:
        value = b[0]
    elif d == 2:
        value = b[0]**2-b[1]**2
    elif d == 3:
        value = b[0]**3-2*b[0]*b[1]**2+2*b[1]**2*b[2]-b[0]*b[2]**2
    else:
        value = mp.det(mp.matrix([[b[abs(i-j)] for j in range(d)] for i in range(d)]))
    return mp.exp(-s)*value


def main():
    say('40-digit arithmetic; all decimal inputs constructed as exact rationals.')
    profiles = [Counter(lis_profile(pm) for pm in itertools.permutations(range(n)))
                for n in range(10)]
    cases = [
        [('0.2', 1), ('1', 2)],
        [('0.4', 2), ('1', 2)],
        [('0.2', 1), ('1', 4)],
        [('0.4', 2), ('1', 4)],
        [('0.2', 1), ('0.6', 2), ('1', 3)],
        [('0.2', 1), ('0.6', 3), ('1', 4)],
        [('0.2', 2), ('0.6', 2), ('1', 4)],
        [('0.2', 1), ('0.6', 1), ('1', 4)],
        [('0.2', 2), ('0.6', 4), ('1', 4)],
        [('0.2', 1), ('0.6', 1), ('1', 1)],
        [('1.5', 3)], [('2', 4)], [('3', 5)],
    ]
    for case in cases:
        obs = [(Fraction(t), k) for t, k in case]
        value, size = determinant(obs)
        lo, bound = enumeration(obs, profiles)
        tied, _ = determinant(obs, reverse_ties=True)
        assert abs(value-tied) < mp.mpf('1e-36')
        assert -mp.mpf('1e-36') <= value-lo <= bound
        if len(obs) == 1:
            assert abs(value-toeplitz_survival(num(obs[0][0]), obs[0][1]-1)) < mp.mpf('1e-36')
        say(f'{case}; size={size}; determinant={mp.nstr(value,40)}; '
            f'enumeration_N<=9={mp.nstr(lo,40)}; difference={mp.nstr(value-lo,8)}; '
            f'rigorous_tail<={mp.nstr(bound,8)}; reversed_marker_ties=PASS')

    say('Corollary 1.3: endpoints s=0,T and interior, independent enumeration.')
    for s, T in [('0','1'), ('0.25','1'), ('1','1'), ('1.75','3.5')]:
        obs = [(Fraction(s), 1), (Fraction(T), 2)]
        lo, bound = enumeration(obs, profiles)
        closed = mp.exp(-num(Fraction(T)))*mp.besseli(0, 2*mp.sqrt(num(Fraction(T)-Fraction(s))))
        assert -mp.mpf('1e-36') <= closed-lo <= bound
        say(f's={s},T={T}; closed={mp.nstr(closed,40)}; enum_difference={mp.nstr(closed-lo,8)}; tail<={mp.nstr(bound,8)}')

    say('Means: hook-length counts for every n<=180, conjugate shapes with <=1,2,3 rows.')
    factorials = [math.factorial(n) for n in range(185)]
    for d in [1, 2, 3]:
        counts = []
        accumulator = 0
        for n in range(181):
            count = sum(hook_dimension(part, factorials)**2 for part in partitions_at_most(n, d))
            counts.append(count)
            accumulator = n*accumulator+count if n else count
            if n <= 9:
                brute = sum(c for prof, c in profiles[n].items() if prof[-1] <= d)
                assert count == brute
        mean = num(Fraction(accumulator, factorials[180]))
        q = num(Fraction(counts[30], factorials[30]))
        # Consecutive disjoint blocks of 30 must each have LIS<=d.
        discrete_tail = 30*q**6/(1-q)
        integral = mp.quad(lambda s: toeplitz_survival(s, d),
                           [0, 2, 5, 10, 20, 40, 80, 160, 320, 600])
        i = d+1
        bounds = [(mp.binomial(m, m-i+1)*mp.exp(-mp.mpf(m-i+1)*600/m**2)
                   *m**2/(m-i+1), m) for m in range(i, 35)]
        integral_tail, best_m = min(bounds)
        assert abs(mean-integral) <= discrete_tail+integral_tail+mp.mpf('1e-30')
        say(f'EX_{i}: series={mp.nstr(mean,38)}; missing_series<={mp.nstr(discrete_tail,8)}; '
            f'q30={mp.nstr(q,8)}; integral_0^600={mp.nstr(integral,38)}; '
            f'missing_integral<={mp.nstr(integral_tail,8)} (m={best_m}); '
            f'absolute_difference={mp.nstr(abs(mean-integral),8)}')
    say(f'EX_2 exact exponential sum = e = {mp.nstr(mp.e,40)}')
    say(f'Elapsed seconds: {time.monotonic()-START:.3f}')
    with open('referee_numeric.txt', 'w') as out:
        out.write('\n'.join(LOG)+'\n')


if __name__ == '__main__':
    main()
