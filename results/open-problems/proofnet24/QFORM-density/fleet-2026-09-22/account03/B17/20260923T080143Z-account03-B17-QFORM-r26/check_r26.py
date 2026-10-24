import mpmath as mp

mp.mp.dps = 60

c = mp.sqrt(6/mp.pi)

def cross_env(w):
    return 2*mp.asinh(1/(2*mp.sqrt(w)))

def k(w):
    return c*w**(-mp.mpf('0.5'))*mp.e**(-6*w)

def H4sqrt12w(w):
    return 144*w*w - 72*w + 3

C2h = mp.quad(lambda w: k(w)*cross_env(w), [0, 1, mp.inf])
J2h = mp.quad(lambda w: k(w)*cross_env(w)*H4sqrt12w(w), [0, 1, mp.inf])
analytic_upper = mp.log(24) + mp.euler + 2/mp.sqrt(6*mp.pi)
target = 3*mp.sqrt(2)

# Coarse rational enclosures used in the written strict comparison.
coarse_left = mp.mpf('3.179') + mp.mpf('0.578') + mp.mpf('0.461')
coarse_right = 3*mp.mpf('1.414')

print('C2h =', mp.nstr(C2h, 30))
print('J2h =', mp.nstr(J2h, 30))
print('analytic_upper =', mp.nstr(analytic_upper, 30))
print('3sqrt2 =', mp.nstr(target, 30))
print('analytic_gap =', mp.nstr(target-analytic_upper, 30))
print('coarse_left =', coarse_left)
print('coarse_right =', coarse_right)

assert C2h < analytic_upper
assert analytic_upper < target
assert coarse_left < coarse_right
assert J2h > 0

# Exact spectrum statement for A_m = diag(1,-1,J_m/m):
# J_m/m has eigenvalues 1 (once) and 0 (m-1 times), hence
# A_m has nonzero spectrum {1,-1,1} for every m>=1.
print('exact_spectrum_A_m = {1,-1,1} (plus m-1 zeros)')
print('QFORM_B17_R26_CHECK_PASS')
