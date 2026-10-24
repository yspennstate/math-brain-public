from mpmath import mp

mp.dps = 80

ALPHAS = [
    mp.mpf('3.52'),
    mp.mpf('3.6'),
    mp.mpf('4.0'),
    mp.mpf('4.39539'),
    mp.mpf('4.4898'),
]


def q_majority(alpha):
    mu = mp.mpf(3) * alpha / 2
    x = 2 * mu
    return (1 - mp.e**(-x) * (mp.besseli(0, x) + mp.besseli(1, x))) / 2


def analytic_lower(q):
    return q**3 / (1 + (1 - q*q)**(mp.mpf(3)/2))**2


def one_shot_uniform(alpha):
    mu = mp.mpf(3) * alpha / 2
    q = q_majority(alpha)
    K = 80
    pmf = [mp.e**(-mu)]
    for k in range(K):
        pmf.append(pmf[-1] * mu / (k+1))
    EZ = mp.mpf('0')
    EM = mp.mpf('0')
    numF = mp.mpf('0')
    numT = mp.mpf('0')
    for p in range(K+1):
        for n in range(K+1):
            pr = pmf[p] * pmf[n]
            z = min(p, n)
            m = max(p, n)
            EZ += pr*z
            EM += pr*m
            numF += pr*z*(1-q*q)**m
            if m:
                numT += pr*m*(1-q*q)**(m-1)
    a0 = numF/EZ
    b0 = numT/EM

    def U(theta):
        a = theta*a0
        b = theta*b0
        return (q**3*(1-a)**3
                + 3*q*(1-q)**2*b*b*(1-a)
                + (1-q)**3*b**3)

    # Golden-section search on [0,1], diagnostic only.
    lo, hi = mp.mpf('0'), mp.mpf('1')
    gr = (mp.sqrt(5)-1)/2
    c = hi-gr*(hi-lo)
    d = lo+gr*(hi-lo)
    fc, fd = U(c), U(d)
    for _ in range(160):
        if fc < fd:
            hi, d, fd = d, c, fc
            c = hi-gr*(hi-lo)
            fc = U(c)
        else:
            lo, c, fc = c, d, fd
            d = lo+gr*(hi-lo)
            fd = U(d)
    theta = (lo+hi)/2
    return a0, b0, theta, U(theta)


print('T04 zero-break independent-thinning diagnostic')
print('mp.dps =', mp.dps)
for alpha in ALPHAS:
    q = q_majority(alpha)
    L = analytic_lower(q)
    a0, b0, theta, Umin = one_shot_uniform(alpha)
    print()
    print('alpha =', mp.nstr(alpha, 20))
    print('q =', mp.nstr(q, 30))
    print('analytic universal lower per clause L(q) =', mp.nstr(L, 30))
    print('analytic universal lower per variable alpha*L(q) =', mp.nstr(alpha*L, 30))
    print('uniform-kernel cavity a0 =', mp.nstr(a0, 30))
    print('uniform-kernel cavity b0 =', mp.nstr(b0, 30))
    print('uniform-kernel theta* =', mp.nstr(theta, 30))
    print('uniform-kernel U(theta*) =', mp.nstr(Umin, 30))
