from math import e, exp, log, sqrt

L = 64.0
eps = 1.0 / 64.0
m = 8
H = [
    [14, -2, -3, -4],
    [-2, 11, -6, -8],
    [-3, -6, 6, -12],
    [-4, -8, -12, -1],
]
HH = [[sum(H[i][k] * H[j][k] for k in range(4)) for j in range(4)] for i in range(4)]
assert HH == [[225 if i == j else 0 for j in range(4)] for i in range(4)]
for s in (1, -1):
    # residual row is proportional to row_3(V) + s*eps*row_4(V)
    dense_numerators = [64 * H[2][j] + s * H[3][j] for j in range(4)]
    assert all(x != 0 for x in dense_numerators)

W11 = L**4 * (1 + eps**2)
W10 = L**2 * eps**2
W01 = W10
Hpair = L**4 * eps**2
Z3 = W11 + W10 + W01
assert W11 == 16781312.0
assert W10 == W01 == 1.0
assert Hpair == 4096.0
assert Z3 == 16781314.0

# At fixed h, strict concavity plus symmetry gives q11=2h-1, q10=q01=1-h.
def dlog_bound(h):
    return (-1.0 / (2*h) + 4.0 / (3 - 4*h)
            - (1.0/3.0) * log(W11 * (1-h) / (W10 * (2*h-1))))

lo, hi = 0.500000000001, 0.749999999999
for _ in range(200):
    mid = (lo + hi) / 2
    if dlog_bound(mid) > 0:
        hi = mid
    else:
        lo = mid
hstar = (lo + hi) / 2
logG = ((2*hstar-1) * log(W11/(2*hstar-1))
        + 2*(1-hstar) * log(W10/(1-hstar)))
Gstar = exp(logG)
B_Dprime = 6*sqrt(e) * (2*hstar)**(-0.5) * (3-4*hstar)**(-1) * Gstar**(-1/6)
B_D = 6*sqrt(e) * 2**(-1/6)
B_pair_E3 = 3*2**(5/6) * W11**(-1/6)
B_partner_E4 = 2**(17/8) * Hpair**(-1/8)
C_E3 = 3*2**(4/3)*exp(1/3)
B_generic_E3 = C_E3 * Z3**(-1/6)

# Residual physical row marginals at the globally optimal h are (3-2h)/m.
alpha_res = (3 - 2*hstar) / m
assert alpha_res < hstar

# Direct ridge impossibility on this same left-right crossing.
# Ridge eigenvalues: kL twice, k1, ke. The maximum physical row leverage is kL.
# theta <= 4*kL. If kL>=1/2 then q>=2*kL => 2q>=4*kL>=theta.
# If kL<1/2 then q>=1 => 2q>=2>4*kL>=theta. Either way theta>2q is impossible.
for g in (1e-12, 1e-8, 1e-4, 1e-2, 1.0, 100.0, 10000.0, 1e8):
    kL = L**2 / (L**2 + g)
    k1 = 1 / (1 + g)
    ke = eps**2 / (eps**2 + g)
    theta = 2*kL + k1 + ke
    maxlev = max(kL, (k1 + ke)/m)
    assert abs(maxlev-kL) < 1e-12
    qmin = max(1.0, 2*maxlev)
    assert not (theta > 2*qmin)

print('QFORM_B04_R20_PAIR_E3_CHECK_PASS')
print('hstar=', repr(hstar))
print('Gstar=', repr(Gstar))
print('B_pair_E3=', repr(B_pair_E3))
print('B_generic_E3=', repr(B_generic_E3))
print('B_partner_E4=', repr(B_partner_E4))
print('B_global_Dprime=', repr(B_Dprime))
print('B_pinned_D=', repr(B_D))
print('alpha_res=', repr(alpha_res))
print('Z3=', repr(Z3), 'Hpair=', repr(Hpair))
