# (C3) near q = 1/2 in 60-digit arithmetic: sup over s of Phi_q(s) against K = 2 + ln(1/(4q(1-q))).
import mpmath as mp
mp.mp.dps = 60
def Phi(q, s):
    q = mp.mpf(q); s = mp.mpf(s); t = mp.sqrt(q / (1 - q))
    X0 = (s - t) ** 2; X1 = (s + 1 / t) ** 2; M = s * s + 1
    f = lambda X: X * mp.log(X / M) if X > 0 else mp.mpf(0)
    return (1 - q) * f(X0) + q * f(X1)
for q in ('0.3', '0.4', '0.45', '0.49', '0.499', '0.4999'):
    K = 2 + mp.log(1 / (4 * mp.mpf(q) * (1 - mp.mpf(q))))
    best = (mp.mpf(-1), None)
    for e in range(-30, 71):
        for sign in (1, -1):
            s = sign * mp.mpf(10) ** (mp.mpf(e) / 10)
            v = Phi(q, s)
            if v > best[0]: best = (v, s)
    # refine around the best point with a golden-section style scan
    s0 = best[1]
    for k in range(40):
        for fac in (mp.mpf('1.05'), mp.mpf(1) / mp.mpf('1.05')):
            v = Phi(q, s0 * fac)
            if v > best[0]: best = (v, s0 * fac); s0 = s0 * fac
    print('q=%-7s sup Phi %s at s=%s   K=%s   margin %s' % (q, mp.nstr(best[0], 12), mp.nstr(best[1], 6), mp.nstr(K, 12), mp.nstr(K - best[0], 6)))
    print('          Phi(1e3)=%s Phi(-1e3)=%s Phi(1e6)=%s Phi(-1e6)=%s' % tuple(mp.nstr(Phi(q, x), 10) for x in (1000, -1000, 10**6, -10**6)))
