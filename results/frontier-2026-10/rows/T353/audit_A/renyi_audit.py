import sys; sys.path.insert(0, '.')
import mpmath as mp, cert_renyi_int_arb as R, cert_chi2_arb as C
mp.mp.dps = 40
def Nm(z, mu): return mp.exp(-(z - mu) ** 2 / 2) / mp.sqrt(2 * mp.pi)
def direct(g, al):  # unexpanded forms, mpmath quad on (-inf, inf)
    g = mp.mpf(g); w0 = Nm(g, 0) / 2; aa = mp.exp(-g - .5); r = mp.exp(g - .5)
    S = w0 * (aa + r) ** al * mp.quad(lambda z: Nm(z, 1) ** al / (Nm(z, 1) + r * Nm(z, 0)) ** (al - 1), [-mp.inf, -5, 0, 5, mp.inf])
    A = w0 * mp.quad(lambda z: (aa * Nm(z, -1) + r * Nm(z, 1)) ** al / (Nm(z, -1) + r * Nm(z, 0)) ** (al - 1), [-mp.inf, -5, 0, 5, mp.inf])
    return S, A
print("alpha 2 vs cert_chi2 point():")
for g in [-1.0, 0.5, 2.2]:
    js, ja = R.point(g, 2); c = C.point(g); print(g, js.str(10), ja.str(10), "| chi2:", c)
for al, g in [(3, -2.2), (4, -3.0), (5, -3.5), (3, 0.7), (5, 1.5)]:
    js, ja = R.point(g, al); S, A = direct(g, al)
    print(f"alpha {al} g {g}: arb S {js.str(10)} A {ja.str(10)} | direct S {mp.nstr(S, 10)} A {mp.nstr(A, 10)} diff {mp.nstr(S - A, 6)}")
# monotonicity spot check of each A_k and IS in r
for al in (3, 5):
    for k in range(al + 1):
        v = [float(R.A(R.arb(r), al, k).mid()) for r in (0.02, 0.03, 0.05)]
        assert v[0] > v[1] > v[2], (al, k, v)
    v = [float(R.IS(R.arb(r), al).mid()) for r in (0.02, 0.03, 0.05)]; assert v[0] > v[1] > v[2]
print("monotone spot checks ok")
