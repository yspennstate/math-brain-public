#!/usr/bin/env python3
"""Independent calculations for PAPER.tex. No author code or network access."""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
import signal
import resource
import sys
import time
import math
import cmath
from pathlib import Path

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
current_nice = os.getpriority(os.PRIO_PROCESS, 0)
if current_nice < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
old_soft, old_hard = resource.getrlimit(resource.RLIMIT_DATA)
data_cap = min(768 * 1024**2, old_hard) if old_hard != resource.RLIM_INFINITY else 768 * 1024**2
try:
    resource.setrlimit(resource.RLIMIT_DATA, (data_cap, data_cap))
except (ValueError, OSError) as exc:
    # macOS may refuse this despite its reported inherited limits. The scripts
    # allocate only small scalar problems; report measured peak RSS below.
    print('RLIMIT_DATA unavailable:', repr(exc), 'inherited:', old_soft, old_hard)
signal.signal(signal.SIGALRM, lambda *_: sys.exit('240 second time limit'))
signal.alarm(240)
started = time.monotonic()
import mpmath as mp
mp.mp.dps = 70


def stable_series(alpha, x):
    # Rigorous convergence follows from Stirling, independent of this cutoff.
    total = mp.mpf(0)
    quiet = 0
    for k in range(1, 10001):
        term = ((-1)**(k+1) * mp.gamma(k*alpha+1) / mp.factorial(k)
                * mp.sin(mp.pi*k*alpha) / mp.pi * x**(-k*alpha-1))
        total += term
        quiet = quiet+1 if abs(term) < mp.mpf('1e-58')*max(abs(total), 1) else 0
        # Consecutive tiny terms prevent sin(k*pi*alpha)=0 from stopping early.
        if quiet >= 25:
            return total, k
    raise RuntimeError('series cutoff reached')


def step3():
    rows = ['alpha,x,series,dehoog_laplace,relative_error,terms']
    for astr in ('0.3', '0.5', '0.7'):
        a = mp.mpf(astr)
        for xstr in ('0.5', '1', '2', '5'):
            x = mp.mpf(xstr)
            val, terms = stable_series(a, x)
            inv = mp.invertlaplace(lambda s: mp.exp(-s**a), x, method='dehoog')
            err = abs(val-inv)/abs(inv)
            rows.append(','.join((astr, xstr, mp.nstr(val, 18), mp.nstr(inv, 18),
                                  mp.nstr(err, 5), str(terms))))
    print('\n'.join(rows))
    (ROOT/'step3.csv').write_text('\n'.join(rows)+'\n')
    # Additional independent checks using the alpha=1/2 closed form.
    print('half-stable: x, density, numerical derivative, closed derivative')
    for x in map(mp.mpf, ('0.1', '0.1666666666666666666666666666666667', '1', '4')):
        g = lambda u: mp.exp(-1/(4*u))/(2*mp.sqrt(mp.pi)*u**mp.mpf('1.5'))
        der = g(x)*(1/(4*x*x)-mp.mpf('1.5')/x)
        print(*(mp.nstr(v, 18) for v in (x, g(x), mp.diff(g, x), der)))
    for s in map(mp.mpf, ('0.25', '1', '4')):
        val = mp.quad(lambda u: mp.exp(-s*u-1/(4*u))/(2*mp.sqrt(mp.pi)*u**mp.mpf('1.5')),
                      [0, mp.mpf('0.1'), 1, mp.inf])
        print('Laplace', mp.nstr(s), mp.nstr(val, 20), mp.nstr(mp.exp(-mp.sqrt(s)), 20))


ATOMS = (0.0, -4.0, -16.0)
WEIGHTS = (0.9, 0.07, 0.03)


def finite_G(w):
    return sum(p/(w-s) for s, p in zip(ATOMS, WEIGHTS))


def finite_H(w):
    return w-1j*cmath.sqrt(1/finite_G(w))


def finite_Hprime(w):
    g = finite_G(w)
    i2 = sum(p/(w-s)**2 for s, p in zip(ATOMS, WEIGHTS))
    f = 1/g
    return 1-0.5j*i2/(g*g*cmath.sqrt(f))


def inverse_H(z, seed):
    w = complex(seed)
    for it in range(120):
        res = finite_H(w)-z
        if abs(res) < 3e-13:
            return w, abs(res), it
        step = res/finite_Hprime(w)
        damp = 1.0
        for _ in range(60):
            trial = w-damp*step
            if trial.imag > 0 and abs(finite_H(trial)-z) < abs(res):
                w = trial
                break
            damp *= 0.5
        else:
            raise RuntimeError(f'Newton line search: z={z}, w={w}, res={res}')
    raise RuntimeError(f'Newton iterations: z={z}, w={w}')


def bisect(fun, lo, hi):
    flo = fun(lo)
    if flo*fun(hi) >= 0:
        raise ValueError('not bracketed')
    for _ in range(100):
        mid = (lo+hi)/2
        if mid == lo or mid == hi:
            return mid
        fm = fun(mid)
        if flo*fm > 0:
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo+hi)/2


def atom_image(s):
    hi = 1.0
    while finite_H(complex(s, hi)).imag < 0:
        hi *= 2
    y = bisect(lambda yy: finite_H(complex(s, yy)).imag, 1e-14, hi)
    w = complex(s, y)
    return y, finite_H(w).real, -finite_G(w).imag/math.pi


def real_Hprime(x):
    g = finite_G(x)
    if g >= 0:
        return float('nan')
    i2 = sum(p/(x-s)**2 for s, p in zip(ATOMS, WEIGHTS))
    return 1-0.5*i2*(-g)**(-1.5)


def gap_component(left, right):
    # Independently scan for the region G<0, H'>0, then bracket endpoints.
    nodes = [left+(right-left)*j/20000 for j in range(1, 20000)]
    positive = [j for j, x in enumerate(nodes) if real_Hprime(x) > 0]
    first, last = positive[0], positive[-1]
    lroot = bisect(real_Hprime, nodes[first-1], nodes[first])
    rroot = bisect(real_Hprime, nodes[last], nodes[last+1])
    image = lambda x: x+1/math.sqrt(-finite_G(x))
    return lroot, rroot, image(lroot), image(rroot)


def step7():
    print('finite measure: atoms', ATOMS, 'weights', WEIGHTS, 'alpha=0.5,t=1')
    gaps = []
    print('real_gap_input,left_w,right_w,left_H,right_H')
    for lo, hi in ((-16, -4), (-4, 0)):
        vals = gap_component(lo, hi)
        gaps.append(vals)
        print(f'({lo}:{hi}),'+','.join(f'{v:.14g}' for v in vals))
    print('atom,f(atom),h(atom),boundary_density')
    atom_rows = []
    for s in sorted(ATOMS):
        vals = atom_image(s)
        atom_rows.append((s, *vals))
        print(','.join(f'{v:.14g}' for v in (s, *vals)))
    print('midpoint c=-8: Hprime', real_Hprime(-8), 'H', -8+1/math.sqrt(-finite_G(-8)))
    rows = ['eps,x,w_real,w_imag,p_eps,residual,iterations']
    maxima = []
    for eps in (1e-4, 1e-7):
        w = complex(-18, 4)
        maxres, maxit = 0.0, 0
        for j in range(1301):
            x = -18+0.02*j
            z = complex(x, eps)
            try:
                w, res, it = inverse_H(z, w)
            except RuntimeError:
                w, res, it = inverse_H(z, z+4j)
            p = -finite_G(w).imag/math.pi
            rows.append(','.join((f'{eps:.1e}', f'{x:.8f}', f'{w.real:.16g}',
                                  f'{w.imag:.16g}', f'{p:.16g}', f'{res:.5g}', str(it))))
            maxres, maxit = max(maxres, res), max(maxit, it)
        maxima.append((eps, maxres, maxit))
    (ROOT/'step7_grid.csv').write_text('\n'.join(rows)+'\n')
    print('grid eps,maxres,max_iterations', maxima)
    print('target,x,eps,density,residual')
    targets = [(f'atom_{s:g}', h) for s, f, h, p in atom_rows]
    targets += [('gap1_middle', (gaps[0][2]+gaps[0][3])/2),
                ('gap2_middle', (gaps[1][2]+gaps[1][3])/2)]
    for tag, x in targets:
        for eps in (1e-4, 1e-7, 1e-10):
            w, res, it = inverse_H(complex(x, eps), complex(x, 4))
            print(','.join((tag, f'{x:.14g}', f'{eps:.1e}',
                            f'{-finite_G(w).imag/math.pi:.14g}', f'{res:.5g}')))
    print('paper mu_*: alpha,t,n,A,c,G,I2,Hprime,finite_difference,log10_omitted_mass_bound')
    table = ['alpha,t,n,A,c,G,I2,Hprime,finite_difference,log10_omitted_mass_bound']
    # All atomic terms up to N are included, even when extraordinarily tiny.
    # The remaining mass is <=2^(-N-2) exp(-A_(N+1)^2).
    for astr in ('0.1', '0.5', '0.9'):
        a = mp.mpf(astr)
        for tint in (1, 100):
            t = mp.mpf(tint)
            n = 2
            while mp.power(mp.mpf(2)**(2**n), a) < 18*(1-a)*t:
                n += 1
            A = mp.mpf(2)**(2**n)
            c = -A/2
            N = max(3, n+1)
            locations = [mp.mpf(2)**(2**k) for k in range(1, N+1)]
            weights = [mp.mpf(2)**(-k-2)*mp.exp(-s*s) for k, s in enumerate(locations, 1)]
            p0 = 1-sum(weights)
            g = lambda x: p0/x+sum(p/(x+s) for s, p in zip(locations, weights))
            gc = g(c)
            i2 = p0/c**2+sum(p/(c+s)**2 for s, p in zip(locations, weights))
            hp = 1-(1-a)*t*i2*(-gc)**(a-2)
            h = lambda x: x+t*(-g(x))**(a-1)
            d = A*mp.mpf('1e-20')
            fd = (h(c+d)-h(c-d))/(2*d)
            log10tail = -(N+2)*mp.log10(2)-(mp.mpf(2)**(2**(N+1)))**2/mp.log(10)
            row = [astr, str(tint), str(n), mp.nstr(A, 18), mp.nstr(c, 18),
                   mp.nstr(gc, 18), mp.nstr(i2, 18), mp.nstr(hp, 18),
                   mp.nstr(fd, 18), mp.nstr(log10tail, 8)]
            table.append(','.join(row))
            print(','.join(row))
    (ROOT/'step7_paper.csv').write_text('\n'.join(table)+'\n')


def step8():
    atoms = (0.0, -4.0, -16.0, -256.0)
    weights = (0.85, 0.07, 0.05, 0.03)
    def g(u):
        return math.exp(-1/(4*u))/(2*math.sqrt(math.pi)*u**1.5) if u > 0 else 0.0
    def gd(u):
        return g(u)*(1/(4*u*u)-1.5/u) if u > 0 else 0.0
    def q(x):
        return sum(p*g(x-s) for s, p in zip(atoms, weights))
    def qd(x):
        return sum(p*gd(x-s) for s, p in zip(atoms, weights))
    print('atoms', atoms, 'weights', weights, 'alpha=0.5,t=1')
    print('x,q,qprime')
    table = ['x,q,qprime']
    for x in (-255.99, -255.9, -250, -240, -225, -210, -200, -20, -15.9, -3.9, 0.1):
        row = f'{x:.8f},{q(x):.17g},{qd(x):.17g}'
        print(row)
        table.append(row)
    (ROOT/'step8_table.csv').write_text('\n'.join(table)+'\n')
    points = [(-250+0.01*j) for j in range(5001)]
    vals = [q(x) for x in points]
    differences = [b-a for a, b in zip(vals, vals[1:])]
    print('decrease_grid [-250,-200],step=0.01,points', len(points))
    print('all_adjacent_differences_negative', all(d < 0 for d in differences))
    print('min_difference,max_difference', min(differences), max(differences))
    print('min_derivative,max_derivative', min(qd(x) for x in points), max(qd(x) for x in points))
    with (ROOT/'step8_grid.csv').open('w') as out:
        out.write('x,q,qprime\n')
        for j in range(26101):
            x = -256+0.01*j
            out.write(f'{x:.8f},{q(x):.16g},{qd(x):.16g}\n')
    x, y, z = -255.9, -20.0, -15.9
    print('nonunimodality triple', [(xx, q(xx)) for xx in (x, y, z)])
    print('strict_valley', q(y) < min(q(x), q(z)))


if __name__ == '__main__':
    {'3': step3, '7': step7, '8': step8}[sys.argv[1]]()
    print('elapsed_seconds', round(time.monotonic()-started, 3))
    print('peak_rss_bytes_macos', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
