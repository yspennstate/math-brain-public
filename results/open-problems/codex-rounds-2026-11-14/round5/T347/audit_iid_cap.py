#!/usr/bin/env python3
"""Finite algebra and independent constant checks for PROOF.md; no writes."""
import itertools
import math
import os
import random
import resource
import signal
import sys
import time
from decimal import Decimal, localcontext
from fractions import Fraction

signal.alarm(120)
started = time.monotonic()
print('priority', os.getpriority(os.PRIO_PROCESS, 0))
print('OMP_NUM_THREADS', os.environ.get('OMP_NUM_THREADS'))


def check_moments():
    for n in range(2, 10):
        first = second = fourth = cross = fourth_linear = 0
        count = 1 << n
        for eta in itertools.product((-1, 1), repeat=n):
            total = sum(eta)
            v = [x*total-1 for x in eta]
            first += v[0]
            second += v[0]**2
            fourth += v[0]**4
            cross += v[0]*v[1]
            fourth_linear += (2*v[0]-3*v[1])**4
        assert first == 0
        assert second == count*(n-1)
        assert fourth == count*(3*(n-1)**2-2*(n-1))
        assert cross == count
        assert fourth_linear <= count*24*(2**4+3**4)*(n-1)**2
    print('N=2,...,9: complete sign enumeration confirms all field moments, '
          'two-site covariance and Lyapunov fourth-moment bound PASS')


def check_stability():
    rng = random.Random(34705)
    total_states = total_minima = total_caps = 0
    for n, m in ((6, 5), (8, 7), (10, 9)):
        rows = [[rng.choice((-1, 1)) for _ in range(n)] for _ in range(m)]
        off = [[sum(p[i]*p[j] for p in rows) if i != j else 0
                for j in range(n)] for i in range(n)]
        radius = max(sum(abs(x) for x in row) for row in off)
        states = list(itertools.product((-1, 1), repeat=n))
        qvalues = [sum(sum(x*y for x, y in zip(p, s))**2 for p in rows)
                   for s in states]
        minima = []
        for mask, s in enumerate(states):
            fields = [sum(off[i][j]*s[j] for j in range(n)) for i in range(n)]
            differences = [qvalues[mask]-qvalues[mask ^ (1 << (n-1-i))]
                           for i in range(n)]
            assert differences == [4*s[i]*fields[i] for i in range(n)]
            if min(differences) >= 0:
                minima.append(s)
        for x in rows:
            gx = [x[i]*sum(off[i][j]*x[j] for j in range(n)) for i in range(n)]
            for threshold in (1, 2, 3):
                unstable = {i for i, value in enumerate(gx) if value <= -threshold}
                if unstable:
                    total_caps += 1
                for s in minima:
                    d = sum(a != b for a, b in zip(x, s))
                    corrections = [sum(off[i][j]*(s[j]-x[j]) for j in range(n))
                                   for i in range(n)]
                    squared = sum(v*v for v in corrections)
                    assert threshold**2*max(len(unstable)-d, 0) <= squared
                    # Symmetric row-sum bound supplies a certified operator bound.
                    assert squared <= 4*radius**2*d
                    assert d*(threshold**2+4*radius**2) >= threshold**2*len(unstable)
        total_states += len(states)
        total_minima += len(minima)
        print(f'N={n} M={m}: actual projection energies and all neighbors PASS; '
              f'minima={len(minima)}; deterministic cap inequality at every minimum PASS')
    assert total_caps > 0
    print('total_states', total_states, 'total_minima', total_minima,
          'nonempty_threshold_tests', total_caps)


def decimal_tail(z):
    # Integrate exp(-x^2/2) term by term from 0 to z. No erfc call.
    with localcontext() as ctx:
        ctx.prec = 65
        pi = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923')
        power_term = z
        integral = power_term
        for k in range(1, 1000):
            power_term *= -z*z/Decimal(2*k)
            increment = power_term/Decimal(2*k+1)
            integral += increment
            if abs(increment) < Decimal('1e-58'):
                break
        else:
            raise AssertionError('series did not converge')
        return +(Decimal('0.5')-integral/(2*pi).sqrt())


def constants():
    alpha, t = 1/7, 1/5
    z = (1+t)/math.sqrt(alpha)
    p = math.erfc(z/math.sqrt(2))/2
    ell = 8*(1+alpha)*math.log(9)-alpha
    cap = p*t*t/(t*t+4*ell*ell)
    with localcontext() as ctx:
        ctx.prec = 60
        a_dec, t_dec = Decimal(1)/7, Decimal(1)/5
        z_dec = (1+t_dec)/a_dec.sqrt()
        p_dec = decimal_tail(z_dec)
        ell_dec = 8*(1+a_dec)*Decimal(9).ln()-a_dec
        cap_dec = p_dec*t_dec*t_dec/(t_dec*t_dec+4*ell_dec*ell_dec)
    assert math.isclose(p, float(p_dec), rel_tol=2e-14)
    assert math.isclose(ell, float(ell_dec), rel_tol=2e-14)
    assert math.isclose(cap, float(cap_dec), rel_tol=2e-14)
    # Entirely rational certification in PROOF.md, independently of both tails.
    assert Fraction(25, 22)*Fraction(11, 4)**5 < 180
    assert Fraction(80, 281*540) > Fraction(1, 2000)
    assert sum(Fraction(9, 4)**k/math.factorial(k) for k in range(6)) > 9
    assert Fraction(143, 7) < 21
    rational_cap = Fraction(1, 2000)*Fraction(1, 25)/(Fraction(1, 25)+4*21**2)
    assert rational_cap == Fraction(1, 88202000)
    assert rational_cap > Fraction(1, 100000000)
    assert p > 1/2000 and ell < 21 and cap > float(rational_cap)
    print('alpha=1/7 t=1/5')
    print('p_erfc', format(p, '.16g'))
    print('p_independent_decimal_integral', format(p_dec, '.40g'))
    print('L_alpha', format(ell, '.16g'))
    print('R_alpha', format(cap, '.16g'))
    print('R_independent_decimal', format(cap_dec, '.40g'))
    print('rational_lower_bound', rational_cap, '>', '1/100000000 PASS')
    # The cap tends to zero at small load; no alpha=0 endpoint is asserted.
    for a in (0.01, 0.056, 0.071, 0.113, 0.138, 1/7, 0.2, 1.0):
        ell_a = 8*(1+a)*math.log(9)-a
        p_a = math.erfc((1+t)/math.sqrt(2*a))/2
        r_a = p_a*t*t/(t*t+4*ell_a*ell_a)
        assert 0 < r_a < p_a < 0.5
        print(f'illustration_only alpha={a:.12g} t=0.2 R={r_a:.12g}')


if __name__ == '__main__':
    check_moments()
    check_stability()
    constants()
    divisor = 1024**2 if sys.platform == 'darwin' else 1024
    print('peak_rss_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/divisor, 3))
    print('elapsed_seconds', round(time.monotonic()-started, 3))
