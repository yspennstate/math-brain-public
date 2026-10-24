"""Constants for the read-k union theorem H <= (C0 + C1 k) I.
C1 = 2 (vacuum) + beta + c1 (dense cover) + a L1/ln2 (rank tail per piece) + c2 K_beta (level tail per piece),
c1 = 1 + a/(a-1), c2 = 1 + c1/beta, L1 = 2 ln B + 2, B = 3 sqrt(3/pi);
K_beta = sup_{lam > 1} beta*lam * phi_l(2^{1-beta*lam}), l = ceil(lam) - 2,
phi_0(al) = al, phi_l(al) = al (2e ln(1/al)/l)^l (valid and increasing in al when l <= ln(1/al)).
C0 = 2.8854 + 1."""
import mpmath as mp
mp.mp.dps = 30
B = 3 * mp.sqrt(3 / mp.pi); L1 = 2 * mp.log(B) + 2

def K(beta):
    best = mp.mpf(0); arg = None
    lam = mp.mpf(1) + mp.mpf('1e-9')
    while lam < 400:
        l = int(mp.ceil(lam)) - 2
        al = 2 ** (1 - beta * lam)
        if l == 0: ph = al
        else:
            assert l <= mp.log(1 / al), (beta, lam)
            ph = al * (2 * mp.e * mp.log(1 / al) / l) ** l
        v = beta * lam * ph
        if v > best: best, arg = v, lam
        lam += mp.mpf('0.001')
    return best, arg

def C1(a, beta, Kb):
    c1 = 1 + a / (a - 1); c2 = 1 + c1 / beta
    return 2 + beta + c1 + a * L1 / mp.log(2) + c2 * Kb

Ks = {}
for beta in (4, 5, 6, 7, 8, 9, 10, 12):
    Ks[beta] = K(beta)
    print('beta', beta, 'K =', mp.nstr(Ks[beta][0], 6), 'at lam', mp.nstr(Ks[beta][1], 5), flush=True)
best = None
for beta in Ks:
    for a in [mp.mpf(x) / 100 for x in range(110, 301, 2)]:
        c = C1(a, beta, Ks[beta][0])
        if best is None or c < best[0]: best = (c, a, beta)
print('best C1 = %s at a = %s, beta = %s' % (mp.nstr(best[0], 6), mp.nstr(best[1], 4), best[2]))
print('C0 = 2.8854 + 1 = 3.8854')

# Explicit check of the paper's K: K = max_l 5(l+1) phi_l(2^{-5l-4}), the maximum at l = 1, and the claims used:
# (i) l <= ln(1/alpha) at alpha = 2^{-5l-4}; (ii) the log-derivative 1/lam - beta ln2 (1 - l/((beta lam - 1) ln2))
# is negative on (l+1, l+2]; (iii) the coefficient of k is < 21.2 and C0 < 3.9.
beta = 5; a = mp.mpf('1.44')
vals = []
for l in range(0, 400):
    al = mp.mpf(2) ** (-5 * l - 4)
    assert l <= mp.log(1 / al)
    ph = al if l == 0 else al * (2 * mp.e * mp.log(1 / al) / l) ** l
    vals.append(5 * (l + 1) * ph)
    lam_grid = [l + 1 + mp.mpf(t) / 1000 for t in range(1, 1001)]
    for lam in lam_grid:
        der = 1 / lam - beta * mp.log(2) * (1 - l / ((beta * lam - 1) * mp.log(2)))
        assert der < 0, (l, lam)
Kx = max(vals); lmax = vals.index(Kx)
print('K = max_l 5(l+1) phi_l(2^-5l-4) =', mp.nstr(Kx, 12), 'at l =', lmax, '; values l=0..5:', [mp.nstr(v, 5) for v in vals[:6]])
print('tail check: values decrease from l=1 on:', all(vals[i+1] < vals[i] for i in range(1, 399)))
c1 = 1 + a / (a - 1); c2 = 1 + c1 / beta
coef = 2 + beta + c1 + a * L1 / mp.log(2) + c2 * Kx
print('c1 =', mp.nstr(c1, 6), 'c2 =', mp.nstr(c2, 6), 'a L1/ln2 =', mp.nstr(a * L1 / mp.log(2), 6), 'c2 K =', mp.nstr(c2 * Kx, 6))
print('coefficient of k =', mp.nstr(coef, 10), '(< 21.2:', coef < mp.mpf('21.2'), ')')
