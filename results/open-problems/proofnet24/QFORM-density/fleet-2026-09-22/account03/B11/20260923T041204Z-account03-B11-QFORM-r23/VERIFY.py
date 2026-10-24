import math

Kvol = 9*math.sqrt(3)*math.e/2
zcoef = 7/(512*3**4)          # 7/41472
Cpacket = Kvol * zcoef**(-1/6)
Ccross = 3*math.sqrt(3) * zcoef**(-1/6)
tube_exact = math.sqrt(7/2)/(16*3**2)
tube_simple = 1/80
partner_eta = 1-math.sqrt(15)/4
partner_const = 6*math.sqrt(math.pi)/(1-2*partner_eta)

print('Kvol=', repr(Kvol))
print('zcoef=', repr(zcoef), ' expected=', repr(7/41472))
print('Cpacket=', repr(Cpacket))
print('Ccross=', repr(Ccross))
print('tube_exact=', repr(tube_exact))
print('tube_simple=', repr(tube_simple))
print('partner_const=', repr(partner_const))

assert abs(zcoef - 7/41472) < 1e-18
assert tube_simple < tube_exact
assert Ccross < Cpacket
assert partner_const < 4*math.pi

# Singular-value perturbation algebra used in Lemma 2.1.
# Exact rank-one input supplies E3(M0) >= (7/2)c^6.
# If all four block norms <= L, ||M0|| <= 2L and hence
# E3(M0) <= 4(2L)^4 s3(M0)^2 = 64L^4 s3(M0)^2.
# Thus s3(M0) >= sqrt(7/2)c^3/(8L^2).  Half survives when
# eps <= sqrt(7/2)c^3/(16L^2), and then
# E3(M) >= c^4 [sqrt(7/2)c^3/(16L^2)]^2
#       = 7c^10/(512L^4).
for c in [0.1, 0.25, 0.5, 1.0, 2.0]:
    L=3.0
    surviving_s3_sq=(math.sqrt(7/2)*c**3/(16*L**2))**2
    lower=c**4*surviving_s3_sq
    target=7*c**10/(512*L**4)
    assert abs(lower-target) <= 1e-12*max(1,target)

# 4x4 concentrated third-volume branch: a heavy row and column leave
# exactly C(3,2)^2=9 incident 3x3 minors, so one has det^2 > Z/27.
assert math.comb(3,2)**2 == 9
# The r=3 square cross-block theorem then costs 3*27^(1/6)=3sqrt(3).
assert abs(3*27**(1/6)-3*math.sqrt(3)) < 1e-12

print('QFORM_B11_R23_ROBUST_RECOLOR_CHECK_PASS')
