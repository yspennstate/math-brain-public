from mpmath import mp

mp.dps = 80

Cinf = mp.sqrt(6*mp.pi) * mp.erf(mp.sqrt(mp.mpf(3)/2))
kappa = mp.mpf(9)/20 * mp.e**(-mp.mpf(3)/2) + mp.mpf(9)/80 * Cinf
barrier = 3*mp.sqrt(2)

# Direct quadrature checks of the exact formulas.
Cinf_quad = 12 * mp.quad(lambda x: mp.e**(-6*x*x), [0, mp.mpf('0.5')])
I1 = 12 * mp.quad(
    lambda x: mp.e**(-6*x*x) * (108*x**4 - 72*x**2 + 6),
    [0, mp.mpf('0.5')]
)
I1_closed = 9*mp.e**(-mp.mpf(3)/2) + mp.mpf(9)/4*Cinf

assert abs(Cinf - Cinf_quad) < mp.mpf('1e-70')
assert abs(I1 - I1_closed) < mp.mpf('1e-68')
assert abs(kappa - I1/20) < mp.mpf('1e-70')
assert Cinf < barrier
assert kappa > 0

# The analytic erf majorant used in the proof, sampled only as a diagnostic.
def erf_majorant(x):
    return 2*x/(mp.sqrt(mp.pi)*mp.sqrt(1 + 2*x*x/3))

for x in [mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf('0.5'), mp.mpf('1'), mp.sqrt(mp.mpf(3)/2), mp.mpf('3')]:
    assert mp.erf(x) <= erf_majorant(x)

print('C_infty =', mp.nstr(Cinf, 40))
print('3sqrt2   =', mp.nstr(barrier, 40))
print('gap       =', mp.nstr(barrier-Cinf, 40))
print('kappa     =', mp.nstr(kappa, 40))
print('I1 check  =', mp.nstr(I1, 40))
print('PASS')
