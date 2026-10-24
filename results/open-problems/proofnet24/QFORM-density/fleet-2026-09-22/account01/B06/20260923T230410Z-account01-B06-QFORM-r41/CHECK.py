import math
import random

# r41 constant checks.
C1 = 8 * math.pi**0.25 * math.e**0.125 / (math.gamma(0.25) * math.cos(math.pi/8))
Cstar = 2 * math.sqrt(3) * C1
Csmall = Cstar * 2**(5/16)
Ctarget = Csmall * 16**(3/4) * (1/16)**(1/8) * (81/2**24)**(-1/16)

print('C1', repr(C1))
print('Cstar', repr(Cstar))
print('Csmall', repr(Csmall))
print('Ctarget', repr(Ctarget))

assert abs(C1 - 3.6030297197863614) < 1e-12
assert abs(Cstar - 12.481261071701265) < 1e-12
assert abs(Csmall - 15.499951566420881) < 1e-12
assert abs(Ctarget - 188.43866121660622) < 1e-10

# Direct exact-formula Schur check for the physical pair (X,Z_i).
# B=[[0,a],[a,c]], B^{-1}=[[-c/a^2,1/a],[1/a,0]].
def binv_apply(a, c, x, y):
    return (-c*x/(a*a) + y/a, x/a)

random.seed(24092026)
max_err = 0.0
for m in (2, 3, 7, 12):
    for _ in range(10):
        aa = [random.uniform(-2,2) for _ in range(m)]
        bb = [random.uniform(-2,2) for _ in range(m)]
        i = random.randrange(m)
        if abs(aa[i]) < 0.15:
            aa[i] += 1.0
        c = random.uniform(-2,2)
        a = aa[i]
        bi = bb[i]

        # Y-Y correction: [0,bi] B^{-1} [0,bi]^T = 0.
        u0, u1 = binv_apply(a, c, 0.0, bi)
        yy_corr = 0.0*u0 + bi*u1
        max_err = max(max_err, abs(yy_corr))

        for j in range(m):
            if j == i:
                continue
            Cij = random.uniform(-2,2)
            u0, u1 = binv_apply(a, c, aa[j], Cij)
            schur_yj = bb[j] - (0.0*u0 + bi*u1)
            expected = bb[j] - (bi/a)*aa[j]
            max_err = max(max_err, abs(schur_yj-expected))

print('max_schur_error', repr(max_err))
assert max_err < 1e-12
print('QFORM_B06_R41_CHECK_PASS')
