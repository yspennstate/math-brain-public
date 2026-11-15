"""Exact coupling/variance checks and small noncommuting matrix-mgf audits."""

from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
import os
import resource
import signal
import time


def dec(x):
    x = F(x)
    return Decimal(x.numerator) / Decimal(x.denominator)


def zero(m):
    return tuple(tuple(F(0) for _ in range(m)) for _ in range(m))


def eye(m):
    return tuple(tuple(F(i == j) for j in range(m)) for i in range(m))


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def scale(a, s):
    return tuple(tuple(x * s for x in row) for row in a)


def mul(a, b):
    m = len(a)
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(m))
                       for j in range(m)) for i in range(m))


def total(ms, m=2):
    ans = zero(m)
    for a in ms:
        ans = add(ans, a)
    return ans


def psd2(a):
    assert a[0][1] == a[1][0]
    return a[0][0] >= 0 and a[1][1] >= 0 and a[0][0]*a[1][1] >= a[0][1]**2


def eig2(a):
    mid = (dec(a[0][0]) + dec(a[1][1])) / 2
    radius = (((dec(a[0][0])-dec(a[1][1]))/2)**2 + dec(a[0][1])**2).sqrt()
    return mid - radius, mid + radius


def exp2(a):
    # Closed form from (A-mid*I)^2=radius^2*I, not a numerical eigensolver.
    mid = (dec(a[0][0]) + dec(a[1][1])) / 2
    delta = (dec(a[0][0]) - dec(a[1][1])) / 2
    off = dec(a[0][1])
    radius = (delta*delta + off*off).sqrt()
    em = mid.exp()
    if not radius:
        return ((em, Decimal(0)), (Decimal(0), em))
    ep, en = radius.exp(), (-radius).exp()
    co = (ep+en)/2
    si = (ep-en)/(2*radius)
    return ((em*(co+si*delta), em*si*off),
            (em*si*off, em*(co-si*delta)))


def trace_exp(a):
    e = exp2(a)
    return e[0][0] + e[1][1]


def trace_exp_series(a):
    # Independent power-series calculation at Decimal precision.
    d = tuple(tuple(dec(x) for x in row) for row in a)
    term = ((Decimal(1), Decimal(0)), (Decimal(0), Decimal(1)))
    ans = Decimal(2)
    for j in range(1, 161):
        term = tuple(tuple(sum(term[i][k]*d[k][l] for k in range(2))/j
                           for l in range(2)) for i in range(2))
        ans += term[0][0]+term[1][1]
    return ans


def coupling_checks():
    cases = draws = extensions = means = 0
    for n in range(2, 7):
        qs = sorted(set(range(1, min(n, 4)+1)) | {n})
        for q in qs:
            mass = defaultdict(F)
            first = defaultdict(lambda: [F(0)]*n)
            for js in product(range(n), repeat=q):
                occupied = set(js)
                unused = [i for i in range(n) if i not in occupied]
                completions = comb(n-len(occupied), q-len(occupied))
                weight = F(1, n**q * completions)
                counts = [js.count(i) for i in range(n)]
                for extra in combinations(unused, q-len(occupied)):
                    r = tuple(sorted(occupied | set(extra)))
                    mass[r] += weight
                    for i in range(n):
                        first[r][i] += weight*counts[i]
                    extensions += 1
                draws += 1
            assert len(mass) == comb(n, q)
            for r, p in mass.items():
                assert p == F(1, comb(n, q))
                for i in range(n):
                    assert first[r][i]/p == int(i in r)
                    means += 1
            cases += 1
    print('PASS exact_coupling_cases', cases, 'ordered_draws', draws,
          'subset_extensions', extensions, 'conditional_count_means', means)


def frame(n, cols=(0, 1)):
    v = tuple(F(i+1) for i in range(n))
    v2 = sum(x*x for x in v)
    h = [[F(i == j)-2*v[i]*v[j]/v2 for j in range(n)] for i in range(n)]
    for a in range(n):
        for b in range(n):
            assert sum(h[i][a]*h[i][b] for i in range(n)) == int(a == b)
    rows = [(h[i][cols[0]], h[i][cols[1]]) for i in range(n)]
    aa = [tuple(tuple(row[a]*row[b] for b in range(2)) for a in range(2))
          for row in rows]
    ell = n*max(sum(x*x for x in row) for row in rows)
    xx = [add(a, scale(eye(2), -F(1, n))) for a in aa]
    return rows, aa, xx, ell


def matrix_checks():
    frames = subsets = variance_cases = mass_checks = tails = mgfs = noncommuting = 0
    exp_checks = gt_checks = 0
    directions = [(F(1), F(0)), (F(0), F(1)),
                  (F(3,5), F(4,5)), (F(5,13), -F(12,13))]
    tolerance = Decimal('1e-45')
    for n in range(3, 9):
        for cols in [(0,1), (1,2)]:
            rows, aa, xx, ell = frame(n, cols)
            assert total(aa) == eye(2)
            assert total(xx) == zero(2)
            assert 2 <= ell <= n
            aa2 = total(mul(a, a) for a in aa)
            xx2 = total(mul(x, x) for x in xx)
            assert scale(xx2, F(1,n)) == add(scale(aa2,F(1,n)),scale(eye(2),-F(1,n*n)))
            assert psd2(add(scale(eye(2), (ell-1)/n**2), scale(xx2,-F(1,n))))
            assert any(mul(a,b) != mul(b,a) for a,b in combinations(aa,2))
            noncommuting += 1
            for x in xx:
                assert psd2(add(scale(eye(2),ell/n),x))
                assert psd2(add(scale(eye(2),ell/n),scale(x,-1)))
            for k in range(n+1):
                cs = [total(xx[i] for i in r) for r in combinations(range(n),k)]
                second = scale(total(mul(c,c) for c in cs),F(1,len(cs)))
                assert second == scale(xx2,F(k*(n-k),n*(n-1)))
                variance_cases += 1
                for r, c in zip(combinations(range(n),k), cs):
                    assert add(c,total(xx[i] for i in range(n) if i not in r)) == zero(2)
                    lo, hi = eig2(c)
                    norm = max(abs(lo),abs(hi))
                    for y in directions:
                        direct = sum(sum(rows[i][a]*y[a] for a in range(2))**2 for i in r)-F(k,n)
                        form = sum(y[a]*c[a][b]*y[b] for a in range(2) for b in range(2))
                        assert form == direct
                        assert abs(dec(form)) <= norm+tolerance
                        mass_checks += 1
                    subsets += 1
                if 0 < k < n:
                    q = min(k,n-k)
                    for rerr in [F(1,10),F(1,2),F(1),F(2)]:
                        t = F(k,n)*rerr
                        actual = F(sum(max(abs(z) for z in eig2(c)) > dec(t)+tolerance for c in cs),len(cs))
                        exponent = k*k*rerr*rerr/(2*ell*(q+k*rerr/3))
                        bound = 4*(-dec(exponent)).exp()  # 2m with m=2
                        assert dec(actual) <= bound+tolerance
                        tails += 1
            # Noncommuting trace mgfs; enumerate replacement and subset sums separately.
            if n <= 5:
                b = ell/n
                v = ell/n**2
                for q in range(1,min(n,3)+1):
                    for theta in [F(-2),F(-1,2),F(1,2),F(2)]:
                        if abs(theta)*b >= 3:
                            continue
                        sums_wr = [total(xx[i] for i in js) for js in product(range(n),repeat=q)]
                        sums_wo = [total(xx[i] for i in r) for r in combinations(range(n),q)]
                        wr = sum(trace_exp(scale(c,theta)) for c in sums_wr)/len(sums_wr)
                        wo = sum(trace_exp(scale(c,theta)) for c in sums_wo)/len(sums_wo)
                        h = v*theta*theta/(2*(1-b*abs(theta)/3))
                        upper = 2*dec(q*h).exp()
                        assert wo <= wr+tolerance
                        assert wr <= upper+tolerance
                        # Audit the single-draw matrix order used in (9).
                        em = tuple(tuple(sum(exp2(scale(x,theta))[i][j] for x in xx)/n
                                         for j in range(2)) for i in range(2))
                        maximum = (em[0][0]+em[1][1])/2 + (((em[0][0]-em[1][1])/2)**2+em[0][1]**2).sqrt()
                        assert maximum <= dec(h).exp()+tolerance
                        mgfs += 1
                for c in [xx[0],xx[1],add(xx[0],xx[1])]:
                    assert abs(trace_exp(c)-trace_exp_series(c)) <= tolerance
                    exp_checks += 1
                # Independent two-factor Golden–Thompson sanity check.
                for a,bmat in combinations(xx,2):
                    ea, eb = exp2(a), exp2(bmat)
                    rhs = sum(ea[i][j]*eb[j][i] for i in range(2) for j in range(2))
                    assert trace_exp(add(a,bmat)) <= rhs+tolerance
                    gt_checks += 1
            frames += 1
    print('PASS tight_frames',frames,'noncommuting_populations',noncommuting,
          'exact_subsets',subsets,'matrix_second_moments',variance_cases,
          'direct_mass_forms',mass_checks,'matrix_tail_comparisons',tails)
    print('PASS noncommuting_mgf_comparisons',mgfs,'independent_exponential_series',exp_checks,
          'two_factor_Golden_Thompson_checks',gt_checks)


def constant_checks():
    count = 0
    for n in range(2,41):
        for k in range(1,n):
            q = min(k,n-k)
            for ell in [F(1),F(3,2),F(4)]:
                for r in [F(1,10),F(1),F(5)]:
                    t = F(k,n)*r
                    raw = t*t/(2*(q*ell/n**2+(ell/n)*t/3))
                    claimed = k*k*r*r/(2*ell*(q+k*r/3))
                    assert raw == claimed
                    old = k*k*r*r/(8*ell*(q+k*r/6))
                    assert claimed >= old
                    x = dec(F(7,3))
                    a = 2*q*dec(ell)*x
                    b = Decimal(2)/3*dec(ell)*x
                    upper = a.sqrt()+b
                    root = (b+(b*b+4*a).sqrt())/2
                    assert upper >= root
                    assert upper*upper/(2*dec(ell)*(q+upper/3)) >= x-Decimal('1e-45')
                    count += 1
    # Prefactor summation uses sum dimensions=N, not #spaces times largest dimension.
    partitions = 0
    for n in range(1,13):
        for mask in range(1 << (n-1)):
            dims = []
            last = 0
            for j in range(1,n):
                if mask & (1 << (j-1)):
                    dims.append(j-last)
                    last = j
            dims.append(n-last)
            assert sum(2*m for m in dims) == 2*n
            partitions += 1
    print('PASS exponent_substitutions_and_root_inversions',count,
          'eigenspace_dimension_compositions',partitions)


def grouped_tail_checks():
    # Uniform-leverage, noncommuting rank-two frames. Count all subsets by
    # their four occupancy numbers, independently of ordered-draw enumeration.
    directions = [(F(1),F(0)),(F(0),F(1)),
                  (F(3,5),F(4,5)),(-F(4,5),F(3,5))]
    cases = groups = nonvacuous = positive_tails = 0
    for n,q in [(64,16),(128,32)]:
        size = n//4
        aa = [tuple(tuple(F(2,n)*y[i]*y[j] for j in range(2)) for i in range(2))
              for y in directions]
        assert scale(total(aa),size) == eye(2)
        assert any(mul(a,b) != mul(b,a) for a,b in combinations(aa,2))
        records = []
        total_ways = 0
        for a in range(q+1):
            for b in range(q-a+1):
                for c in range(q-a-b+1):
                    d = q-a-b-c
                    counts = (a,b,c,d)
                    if max(counts) > size:
                        continue
                    ways = 1
                    for value in counts:
                        ways *= comb(size,value)
                    mat = add(total(scale(x,value) for x,value in zip(aa,counts)),scale(eye(2),-F(q,n)))
                    norm = max(abs(z) for z in eig2(mat))
                    records.append((norm,ways))
                    total_ways += ways
                    groups += 1
        assert total_ways == comb(n,q)  # independent Vandermonde count
        for k in [q,n-q]:
            # The complement negates the same compression, but changes N/k.
            for r in ([F(1,2),F(3,4),F(9,10)] if k == q else [F(1,6),F(1,4),F(3,10)]):
                actual = F(sum(ways for norm,ways in records if norm > dec(F(k,n)*r)+Decimal('1e-45')),total_ways)
                exponent = k*k*r*r/(4*(q+k*r/3))  # 2 L^2 with L^2=2
                upper = 4*(-dec(exponent)).exp()
                assert dec(actual) <= upper+Decimal('1e-45')
                nonvacuous += upper < 1
                positive_tails += actual > 0
                print('GROUPED_TAIL N',n,'k',k,'r',str(r),
                      'actual',format(dec(actual),'.8g'),'bound',format(upper,'.8g'))
                cases += 1
    assert nonvacuous == 10 and positive_tails == cases
    print('PASS grouped_noncommuting_tails',cases,'occupancy_classes',groups,
          'nonvacuous_bounds',nonvacuous,'positive_tail_probabilities',positive_tails)


def main():
    signal.alarm(120)
    resource.setrlimit(resource.RLIMIT_CPU,(100,100))
    _, hard_data = resource.getrlimit(resource.RLIMIT_DATA)
    data_cap = 256_000_000 if hard_data == resource.RLIM_INFINITY else min(256_000_000,hard_data)
    try:
        resource.setrlimit(resource.RLIMIT_DATA,(data_cap,data_cap))
    except ValueError as exc:
        print('DATA_limit_unavailable', str(exc), 'inherited', hard_data)
    started = time.monotonic()
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    priority = os.getpriority(os.PRIO_PROCESS,0)
    assert priority >= 15
    print('nice',priority,'OMP_NUM_THREADS',os.environ['OMP_NUM_THREADS'])
    with localcontext() as ctx:
        ctx.prec = 65
        coupling_checks()
        matrix_checks()
        constant_checks()
        grouped_tail_checks()
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert rss < 1_000_000_000
    print('peak_rss_bytes',rss,'elapsed_seconds',round(time.monotonic()-started,3))


if __name__ == '__main__':
    main()
