import mpmath as mp
mp.mp.dps = 80
exec(open('svd_defect_limit.py').read().split("for lam in")[0])
for eta in (5, 7, 10, 15, 20, 30, 50, 100, 300, 1000, 1e4):
    t = mp.mpf('1e-12'); a = t; b = t; c = a*b*(1 - eta)
    print('eta=%8g ratio=%s' % (eta, mp.nstr(defect([[a, 1], [c, b]]), 12)))
