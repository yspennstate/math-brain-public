"""Small exact audits and high-precision checks for PROOF.md; standard library only."""

from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import combinations
from math import comb, log, atan2
import os
import resource
import signal
import time


def dec(x):
    x = F(x)
    return Decimal(x.numerator) / Decimal(x.denominator)


def mean(xs):
    return sum(xs, F(0)) / len(xs)


def check_scalar():
    populations = instances = tails = mgfs = pairs = 0
    for n in range(2, 11):
        weights_list = [(F(1, n),) * n,
                        (F(1),) + (F(0),) * (n - 1),
                        tuple(F(2 * (i + 1), n * (n + 1)) for i in range(n))]
        for w in weights_list:
            assert sum(w) == 1
            b = max(w)
            z = tuple(x - F(1, n) for x in w)
            v = mean([x * x for x in z])
            assert max(abs(x) for x in z) <= b
            assert sum(x*x for x in w) <= b
            assert v <= b / n - F(1, n*n)
            for k in range(n + 1):
                subsets = list(combinations(range(n), k))
                values = [sum((z[i] for i in sub), F(0)) for sub in subsets]
                assert mean(values) == 0
                exact_var = mean([x*x for x in values])
                assert exact_var == F(k * (n-k), n-1) * v
                # Re-derive through ordered-draw covariance, not indicators.
                cov = mean([z[i]*z[j] for i in range(n) for j in range(n) if i != j])
                assert cov == -v / (n-1)
                assert exact_var == k*v + k*(k-1)*cov
                for sub, val in zip(subsets, values):
                    complement = sum((z[i] for i in range(n) if i not in sub), F(0))
                    assert val == -complement
                instances += len(values)
                populations += 1
                if 0 < k < n and v:
                    q = min(k, n-k)
                    thresholds = {abs(x) for x in values if x}
                    thresholds |= {t / 2 for t in thresholds}
                    for t in thresholds:
                        actual = F(sum(abs(x) > t for x in values), len(values))
                        exponent = t*t / (2 * (q*v + b*t/3))
                        bound = 2 * (-dec(exponent)).exp()
                        assert dec(actual) <= bound + Decimal('1e-65')
                        tails += 1
        # Exact elementary-symmetric/mgf comparison, for rational a_i>0.
        for a in [tuple(F(i+1, n) for i in range(n)),
                  tuple(F(2)**(i-n//2) for i in range(n)),
                  tuple(F(2)**(n//2-i) for i in range(n))]:
            for q in range(n+1):
                e = sum((product(a[i] for i in sub)
                         for sub in combinations(range(n), q)), F(0))
                assert e / comb(n, q) <= mean(a)**q
                mgfs += 1
                if q >= 2:
                    for i, j in combinations(range(n), 2):
                        other = [a[l] for l in range(n) if l not in (i,j)]
                        ep = elementary(other, q-2)
                        averaged = list(a)
                        averaged[i] = averaged[j] = (a[i]+a[j])/2
                        diff = elementary(averaged, q)-e
                        assert diff == (a[i]-a[j])**2 * ep / 4
                        assert diff >= 0
                        pairs += 1
    print('PASS scalar_cases', populations, 'subset_instances', instances,
          'Bernstein_tails', tails, 'exact_mgf_comparisons', mgfs,
          'pair_smoothing_identities', pairs)


def product(xs):
    p = F(1)
    for x in xs:
        p *= x
    return p


def elementary(a, q):
    if q < 0 or q > len(a):
        return F(0)
    coeff = [F(1)] + [F(0)] * q
    for value in a:
        for j in range(q, 0, -1):
            coeff[j] += value * coeff[j-1]
    return coeff[q]


def check_constants():
    count = 0
    for n in range(2, 30):
        for k in range(1, n):
            q = min(k, n-k)
            for ell in [F(1), F(3,2), F(4)]:  # ell=L^2
                for r in [F(1,10), F(1), F(5)]:
                    t = F(k,2*n)*r
                    direct = n*n*t*t / (2*ell*(q+n*t/3))
                    claimed = k*k*r*r / (8*ell*(q+k*r/6))
                    assert direct == claimed
                    t_simple = F(k,n)*r
                    assert n*n*t_simple*t_simple/(2*ell*(q+n*t_simple/3)) == k*k*r*r/(2*ell*(q+k*r/3))
                    # Independent quadratic-root inversion at high precision.
                    x = dec(F(7,3))
                    a = 8*q*dec(ell)*x
                    b = Decimal(4)/3*dec(ell)*x
                    upper = a.sqrt()+b
                    root = (b+(b*b+4*a).sqrt())/2
                    assert upper >= root
                    exponent = upper*upper/(8*dec(ell)*(q+upper/6))
                    assert exponent >= x - Decimal('1e-65')
                    count += 1
    print('PASS constant_substitutions_and_quadratic_inversions', count)


def check_compressions():
    directions = [(F(-1),F(0))]
    for j in range(-64,65):
        t = F(j,8)
        directions.append(((1-t*t)/(1+t*t), 2*t/(1+t*t)))
    directions.sort(key=lambda y: atan2(float(y[1]),float(y[0])))
    for y in directions:
        assert sum(v*v for v in y) == 1
    for a,b in zip(directions, directions[1:]+directions[:1]):
        assert sum((a[i]-b[i])**2 for i in range(2)) <= F(1,16)
    # The explicit fine net is used only to audit (11), not its 9^m count.
    compressions = forms = 0
    for n in [4,8]:
        h = [[(-1)**((i&j).bit_count()%2) for j in range(n)] for i in range(n)]
        for cols in [(0,1),(1,2)]:
            for k in range(1,n):
                for sub in combinations(range(n), k):
                    c = [[F(sum(h[i][a]*h[i][b] for i in sub),n)
                          -F(k,n)*(a==b) for b in cols] for a in cols]
                    # Direct characteristic-polynomial formula for the norm.
                    mid = dec((c[0][0]+c[1][1])/2)
                    rad = (dec((c[0][0]-c[1][1])/2)**2+dec(c[0][1])**2).sqrt()
                    norm = max(abs(mid+rad),abs(mid-rad))
                    values = []
                    for y in directions:
                        form = sum((y[a]*c[a][b]*y[b] for a in range(2) for b in range(2)),F(0))
                        # Independent mass calculation in the normalized Walsh basis.
                        direct = sum(((sum(y[a]*h[i][cols[a]] for a in range(2)))**2/F(n) for i in sub),F(0))-F(k,n)
                        assert form == direct
                        values.append(abs(form))
                        forms += 1
                    assert norm <= 2*dec(max(values))+Decimal('1e-65')
                    compressions += 1
    print('PASS repeated_eigenspace_compressions',compressions,'quadratic_forms',forms,
          'explicit_net_points',len(directions))


def check_obstruction():
    for s in [2,4,8,16,32,64,128]:
        n = s*s
        exact = F(comb(n-s,s),comb(n,s))
        direct = product(F(n-s-j,n-j) for j in range(s))
        assert exact == direct
        xs = [F(s,n-j) for j in range(s)]
        assert F(1) <= sum(xs) <= F(s*s,n-s+1)
        assert sum(x*x for x in xs) <= max(xs)*sum(xs)
        print('MISS_SUPPORT s',s,'probability',round(float(exact),8),
              'minus_log_probability',round(-log(float(exact)),8))
    # Actual simple-spectrum block matrix, exact without square roots.
    for s in [2,4,8]:
        n=s*s
        h=[[(-1)**((i&j).bit_count()%2) for j in range(s)] for i in range(s)]
        for block in range(s):
            mat=[[F(sum(h[i][j]*(block*s+j+1)*h[l][j] for j in range(s)),s)
                  for l in range(s)] for i in range(s)]
            for col in range(s):
                for i in range(s):
                    assert sum(mat[i][j]*h[j][col] for j in range(s)) == (block*s+col+1)*h[i][col]
                assert F(1,s) == F(s,n)  # max squared coordinate = L^2/N
    print('PASS block_Walsh_obstruction_exact_matrices s=2,4,8')


def main():
    signal.alarm(90)
    resource.setrlimit(resource.RLIMIT_CPU,(80,80))
    priority=os.getpriority(os.PRIO_PROCESS,0)
    assert priority>=15
    assert os.environ.get('OMP_NUM_THREADS')=='1'
    start=time.monotonic()
    print('nice',priority,'OMP_NUM_THREADS',os.environ['OMP_NUM_THREADS'])
    with localcontext() as ctx:
        ctx.prec=80
        check_scalar()
        check_constants()
        check_compressions()
        check_obstruction()
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert rss<1_000_000_000
    print('peak_rss_bytes',rss,'elapsed_seconds',round(time.monotonic()-start,3))


if __name__=='__main__':
    main()
