import mpmath as mp
mp.mp.dps = 80
exec(open('svd_defect_limit.py').read().split("for lam in")[0])
t = mp.mpf('1e-12')
f = lambda eta: defect([[t, 1], [t*t*(1 - eta), t]])
lo, hi = mp.mpf(2), mp.mpf(8)
for it in range(60):   # golden section on the unimodal profile
    m1 = lo + (hi - lo)*0.381966; m2 = lo + (hi - lo)*0.618034
    if f(m1) < f(m2): lo = m1
    else: hi = m2
e = (lo + hi)/2
print('argmax eta =', mp.nstr(e, 12), ' max ratio =', mp.nstr(f(e), 15))
