from mpmath import mp
mp.dps = 50

c = mp.sqrt(6/mp.pi)
I0 = c*mp.quad(lambda u: u**(-mp.mpf('0.5'))*mp.e**(-6*u)*mp.log(1/u), [0,1])
whole = mp.euler + mp.log(24)
tail = c*mp.quad(lambda u: u**(-mp.mpf('0.5'))*mp.e**(-6*u)*mp.log(u), [1, mp.inf])
baseline = 3*mp.sqrt(2)
assert abs(I0-(whole+tail)) < mp.mpf('1e-40')
assert I0 < baseline
assert tail < mp.mpf('0.001')
assert mp.mpf('3.801') < mp.mpf('4.2') < baseline

# Check the principal-value Gaussian Hilbert-transform identity away from zero.
def pv_numeric(t):
    eps = mp.mpf('1e-8')*t
    f = lambda u: u**(-mp.mpf('0.5'))*mp.e**(-6*u)/(u-t)
    return mp.quad(f,[0,t-eps]) + mp.quad(f,[t+eps, mp.inf])

def pv_formula(t):
    return -mp.pi*mp.e**(-6*t)*mp.erfi(mp.sqrt(6*t))/mp.sqrt(t)

for t in map(mp.mpf,['0.01','0.1','1.0']):
    # truncated PV numerical error is O(eps/t); this is only a sanity check.
    assert abs(pv_numeric(t)-pv_formula(t)) < mp.mpf('2e-5')

print('PASS QFORM-SATURATED-OPPOSITE-HEAVY-GLOBAL-v1')
print('C_log =', mp.nstr(I0, 30))
print('gamma+log24 =', mp.nstr(whole, 30))
print('tail =', mp.nstr(tail, 30))
print('3sqrt2 =', mp.nstr(baseline, 30))
print('gap =', mp.nstr(baseline-I0, 30))
print('uniform finite-return factor = 4sqrt3 =', mp.nstr(4*mp.sqrt(3), 30))
