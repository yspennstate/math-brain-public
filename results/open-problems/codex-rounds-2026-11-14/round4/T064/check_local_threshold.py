#!/usr/bin/env python3
"""Independent midpoint quadrature and finite-grid maximin audits.

Run with OMP_NUM_THREADS=1 under nice -n 15. Standard library only;
no files written, one process, constant-memory quadrature.
"""
import ctypes
import heapq
import math
import os
import resource
import sys
import time


def guard():
    libc = ctypes.CDLL(None, use_errno=True)
    libc.getpriority.argtypes = (ctypes.c_int, ctypes.c_uint)
    libc.getpriority.restype = ctypes.c_int
    ctypes.set_errno(0)
    priority = libc.getpriority(0, 0)
    assert ctypes.get_errno() == 0 and priority >= 15, priority
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    # Quadrature uses generators; each grid has only 1681 sites. Peak
    # resident memory is checked and reported at completion.
    print(f'niceness={priority}; threads=1; CPU cap=60s')


PI = math.pi
ROOTPI = math.sqrt(PI)


def phi(t):
    return math.exp(-t*t/2)/math.sqrt(2*PI)


def mid(fun, a, b, n):
    step = (b-a)/n
    return step*math.fsum(fun(a+(i+.5)*step) for i in range(n))


def quad(fun, a, b):
    # Independent of the preceding worker's Simpson rule.
    coarse = mid(fun, a, b, 2048)
    fine = mid(fun, a, b, 4096)
    return (4*fine-coarse)/3


def close(a, b, tol=2e-9):
    assert abs(a-b) < tol, (a, b, abs(a-b))


def B(t):
    return math.exp(-t*t)/(2*ROOTPI)+t*math.erf(t)/2


def beta(t):
    return phi(t)*B(t)/ROOTPI


def saddle(t):
    return phi(t)*math.exp(-t*t)/(4*PI)


def alpha(t):
    return phi(t)*(t*t-1+2*math.exp(-t*t))/(4*PI)


def density(t, L, H):
    return (L*H*saddle(t)+(L+H)*beta(t)/2
            +(H-L)*t*phi(t)/(4*ROOTPI)+phi(t))


def S(d):
    return math.erf(math.sqrt(1.5)*d)/(8*PI*math.sqrt(3))


def J(d):
    return (math.sqrt(3)*math.erf(math.sqrt(1.5)*d)/(4*PI)
            -phi(d)*math.erf(d)/(2*ROOTPI))


def K(d):
    return math.erf(d/math.sqrt(2))/2


def old_I(d):
    return (math.erf(math.sqrt(1.5)*d)/math.sqrt(3)-d*phi(d))/(4*PI)


def closed_bound(u, L, H):
    d = abs(u)
    signed = math.copysign(1, u)*(H-L)*(phi(0)-phi(d))/(4*ROOTPI)
    return L*H*S(d)+(L+H)*J(d)/2+K(d)+signed


def widest_grid(fun, L=1., H=1., n=40):
    # A maximum-capacity path via a heap, independently of the local-type
    # formulas. Grid results are only audits; the proposition is continuous.
    width = n+1
    values = [fun(L*i/n, H*j/n) for j in range(width) for i in range(width)]
    capacities = [-math.inf]*len(values)
    heap = []
    for j in range(width):
        k = j*width
        capacities[k] = values[k]
        heapq.heappush(heap, (-values[k], k))
    while heap:
        negative, k = heapq.heappop(heap)
        cap = -negative
        if cap < capacities[k]:
            continue
        i, j = k % width, k // width
        if i == n:
            return cap
        neighbours = []
        if i > 0:
            neighbours.append(k-1)
        if i < n:
            neighbours.append(k+1)
        if j > 0:
            neighbours.append(k-width)
        if j < n:
            neighbours.append(k+width)
        for nxt in neighbours:
            proposed = min(cap, values[nxt])
            if proposed > capacities[nxt]:
                capacities[nxt] = proposed
                heapq.heappush(heap, (-proposed, nxt))
    raise AssertionError('finite rectangle must have a grid crossing')


def main():
    guard()
    start = time.monotonic()
    max_jet_error = 0.
    sigma = math.sqrt(1/8)
    for t in (-4., -1., -.2, 0., .2, 1., 4.):
        c = t*t/4
        tail = quad(lambda z: (z-c)*4*math.exp(-4*z), c, 20)
        close(tail, math.exp(-t*t)/4)
        full = quad(lambda z: (c-z)*4*math.exp(-4*z), 0, c)+tail
        close(full, (t*t-1+2*math.exp(-t*t))/4)
        pivot = t/(2*sigma)
        negative = quad(lambda z: (t/2-sigma*z)*phi(z), -12, pivot)
        positive = quad(lambda z: (sigma*z-t/2)*phi(z), pivot, 12)
        close(negative, (B(t)+t/2)/2)
        close(positive, (B(t)-t/2)/2)
        max_jet_error = max(max_jet_error,
                            abs(tail-math.exp(-t*t)/4),
                            abs(negative-(B(t)+t/2)/2),
                            abs(positive-(B(t)-t/2)/2))
        # Obtain boundary contributions directly from two truncated normal
        # integrals, not from their signed closed-form rearrangement.
        for L, H in ((.01, 4.), (1., 1.), (4., .01)):
            edge = phi(t)*(H*negative+L*positive)/ROOTPI
            rearranged = ((L+H)*beta(t)/2
                          +(H-L)*t*phi(t)/(4*ROOTPI))
            close(edge, rearranged)
    print(f'conditional jets / signed edge max error={max_jet_error:.3e}')

    quadrant = quad(phi, 0, 12)**2
    close(quadrant, .25)
    print(f'corner eligible quadrant={quadrant:.12f}; four-corner factor={4*quadrant:.12f}')

    max_integral_error = 0.
    for L, H in ((.001, .002), (1., 1.), (.01, 100.), (100., .01)):
        for u in (-2., -.1, -.001, .001, .1, 2.):
            got = quad(lambda t: density(t, L, H), min(0, u), max(0, u))
            want = closed_bound(u, L, H)
            close(got, want)
            max_integral_error = max(max_integral_error, abs(got-want))
            old = L*H*old_I(abs(u))+2*(L+H)*J(abs(u))+4*K(abs(u))
            assert 0 <= want < old
            close(want, closed_bound(-u, H, L))
            close(quad(alpha, 0, abs(u)), old_I(abs(u)))
    print(f'24 interval / orientation / prior-I audits; max error={max_integral_error:.3e}')

    for L, H in ((.001, .002), (1., 1.), (.01, 100.), (100., .01)):
        for t in (i/10 for i in range(-80, 81)):
            d = density(t, L, H)
            old = L*H*alpha(t)+2*(L+H)*beta(t)+4*phi(t)
            assert 0 <= d <= old+1e-14
            close(d, density(-t, H, L))
    print('644 pointwise positivity / domination / duality audits passed')
    close(quad(saddle, -12, 12), 1/(4*PI*math.sqrt(3)))
    close(quad(beta, -12, 12), math.sqrt(3)/(2*PI))
    print(f'total saddle density={1/(4*PI*math.sqrt(3)):.12f}')

    # Eight normal forms evaluated through continuous-exact boundary paths
    # whose bottlenecks are present on this grid. The unused edge's
    # critical value is zero; only the eligible form has threshold zero.
    tests = (
        ('vertical eligible: +normal,-tangent', lambda x,y: 2*x-(y-.5)**2, 0.),
        ('vertical excluded: +normal,+tangent', lambda x,y: 2*x+(y-.5)**2, .25),
        ('vertical excluded: -normal,-tangent', lambda x,y: -2*x-(y-.5)**2, -2.),
        ('vertical excluded: -normal,+tangent', lambda x,y: -2*x+(y-.5)**2, -1.75),
        ('horizontal eligible: -normal,+tangent', lambda x,y: -2*y+(x-.5)**2, 0.),
        ('horizontal excluded: +normal,+tangent', lambda x,y: 2*y+(x-.5)**2, 2.),
        ('horizontal excluded: +normal,-tangent', lambda x,y: 2*y-(x-.5)**2, 1.75),
        ('horizontal excluded: -normal,-tangent', lambda x,y: -2*y-(x-.5)**2, -.25),
    )
    for name, fun, expected in tests:
        got = widest_grid(fun)
        close(got, expected, 1e-12)
        print(f'{name}: grid threshold={got:.6f}')
    for a in (-1.3, 1.3):
        for b in (-.7, .7):
            got = widest_grid(lambda x,y: a*x+b*y)
            exact = min(0., a)+max(0., b)
            close(got, exact, 1e-12)
            print(f'affine a={a:+.1f} b={b:+.1f}: grid={got:.6f}; exact={exact:.6f}')

    print('square u=R^(-3), prior and refined bounds:')
    for R in (10., 100., 1000.):
        d = R**(-3)
        new = closed_bound(d, R, R)
        old = R*R*old_I(d)+4*R*J(d)+4*K(d)
        print(f'  R={R:g}: old={old:.12g}; refined={new:.12g}')
    print('small square d=.1; refined bound approaches Phi(.1)-Phi(0):')
    for R in (.1, .01, .001):
        print(f'  R={R:g}: bound={closed_bound(.1,R,R):.12f}; Gaussian={K(.1):.12f}')

    elapsed = time.monotonic()-start
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib = rss/(1024**2) if sys.platform == 'darwin' else rss/1024
    assert rss_mib < 1024 and elapsed < 60
    print(f'PASS; elapsed={elapsed:.3f}s; peak RSS={rss_mib:.2f} MiB')


if __name__ == '__main__':
    main()
