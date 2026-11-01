import mpmath as mp

mp.mp.dps = 60
K0 = lambda z: mp.besselk(0, z)
K1 = lambda z: mp.besselk(1, z)

Cinf = (mp.mpf(12)/mp.pi) * mp.quad(lambda x: K0(6*x*x), [0, mp.mpf('0.5')])
kappa = (mp.mpf(12)/mp.pi) * (
    mp.mpf(1)/8 * K0(mp.mpf(3)/2)
    + mp.quad(lambda x: (mp.mpf(1)/20 + mp.mpf(36)/5*x**4)*K0(6*x*x), [0, mp.mpf('0.5')])
)
corr = (mp.mpf(12)/mp.pi) * mp.quad(
    lambda x: 3*x*x*K1(6*x*x) - (mp.mpf(36)/5*x**4 + mp.mpf(3)/10)*K0(6*x*x),
    [0, mp.mpf('0.5')]
)
baseline = 3*mp.sqrt(2)
old_upper = (mp.mpf(6)/mp.pi)*(mp.mpf(5)/2 + mp.log(mp.mpf(4)/3) - mp.euler)

assert abs(corr + kappa) < mp.mpf('1e-45')
assert kappa > 0
assert Cinf < baseline
assert Cinf < old_upper < baseline

print('C_sharp_limit =', mp.nstr(Cinf, 50))
print('kappa          =', mp.nstr(kappa, 50))
print('direct_corr    =', mp.nstr(corr, 50))
print('3sqrt2         =', mp.nstr(baseline, 50))
print('sharp_gap      =', mp.nstr(baseline-Cinf, 50))
print('old_upper      =', mp.nstr(old_upper, 50))
print('upper_slack    =', mp.nstr(old_upper-Cinf, 50))
print('PASS QFORM-ONE-HEAVY-MAJORITY-EXACT-EXTREMIZER-v1')
