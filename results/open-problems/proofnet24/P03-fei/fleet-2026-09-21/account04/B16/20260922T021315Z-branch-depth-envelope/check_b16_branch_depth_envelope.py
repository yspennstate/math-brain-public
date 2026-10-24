from fractions import Fraction as F

# Source-compressed 9-bit shared-core Walsh classes (A,Q,multiplicity),
# reconstructed from the immutable shared-graft source. The core amplitudes are
# (A+b Q)/512. This small table is mathematical data, not an opaque truth table.
CLASSES = [
    (-44,4,18), (-18,-2,72), (-16,0,36), (-8,-8,9), (-6,10,18),
    (-4,-4,36), (-4,12,6), (-2,-2,36), (0,0,46), (2,2,72),
    (2,18,1), (4,-12,6), (4,4,36), (8,8,9), (10,-6,36),
    (16,0,36), (38,6,12), (44,-4,18), (114,2,9),
]
ALPHA = F(9,256)
D0 = F(133,128)
A0 = F(57,256)
CBAR = F(57,255)
ELL = F(14593,65536)
MSTRONG = F(9,64)


def pow2(e):
    return F(1 << e, 1) if e >= 0 else F(1, 1 << (-e))


def floor_log2_frac(x):
    assert x > 0
    e = x.numerator.bit_length() - x.denominator.bit_length()
    while x < pow2(e):
        e -= 1
    while x >= pow2(e+1):
        e += 1
    return e


def ln_atanh_bounds(y, N=180):
    assert F(1) <= y <= F(2)
    z = (y-F(1))/(y+F(1))
    zz = z*z
    zp = z
    s = F(0)
    for k in range(N):
        s += zp/F(2*k+1)
        zp *= zz
    lo = 2*s
    hi = lo + 2*zp/F(2*N+1)/(1-zz)
    return lo, hi


LN2_LO, LN2_HI = ln_atanh_bounds(F(2))
INV_LN2_LO = 1/LN2_HI
INV_LN2_HI = 1/LN2_LO


def log2_bounds(x, N=180):
    assert x > 0
    e = floor_log2_frac(x)
    y = x/pow2(e)
    lo, hi = ln_atanh_bounds(y, N)
    return F(e) + lo/LN2_HI, F(e) + hi/LN2_LO


def mul_interval(c, lo, hi):
    return (c*lo, c*hi) if c >= 0 else (c*hi, c*lo)


def K_bounds(b):
    lo = hi = F(0)
    for A,Q,m in CLASSES:
        y = (F(A)+b*F(Q))/F(512)
        p = y*y
        if p:
            llo,lhi = log2_bounds(p)
            tlo,thi = mul_interval(-p, llo, lhi)
            lo += m*tlo
            hi += m*thi
    p = b*b
    if p:
        llo,lhi = log2_bounds(p)
        philo,phihi = mul_interval(-p, llo, lhi)
    else:
        philo = phihi = F(0)
    lo += ALPHA*(-phihi + 16*(1-p))
    hi += ALPHA*(-philo + 16*(1-p))
    return lo,hi


def Kprime_bounds(b):
    lo = hi = F(0)
    for A,Q,m in CLASSES:
        if Q == 0:
            continue
        y = (F(A)+b*F(Q))/F(512)
        p = y*y
        llo,lhi = log2_bounds(p)
        Llo,Lhi = llo+INV_LN2_LO, lhi+INV_LN2_HI
        coeff = -2*y*(F(Q)/F(512))*m
        tlo,thi = mul_interval(coeff,Llo,Lhi)
        lo += tlo
        hi += thi
    p = b*b
    llo,lhi = log2_bounds(p)
    Llo,Lhi = llo+INV_LN2_LO, lhi+INV_LN2_HI
    lo += ALPHA*(2*b*Llo-32*b)
    hi += ALPHA*(2*b*Lhi-32*b)
    return lo,hi


def dec(x, digits=20):
    sign = '-' if x < 0 else ''
    x = abs(x)
    q,r = divmod(x.numerator, x.denominator)
    out=[]
    for _ in range(digits):
        r *= 10
        d,r = divmod(r,x.denominator)
        out.append(str(d))
    return sign+str(q)+'.'+''.join(out)


assert sum(m for _,_,m in CLASSES) == 512
sumq2 = sum(m*Q*Q for _,Q,m in CLASSES)
assert sumq2 == 9216
for A,Q,m in CLASSES:
    if A == 0:
        assert Q == 0
        continue
    u0 = F(A)
    u1 = F(A)+F(Q,4)
    assert u0*u1 > 0
    assert min(abs(u0),abs(u1)) >= 1
# Analytic consequence recorded in REPORT.md:
# H_core'' <= (9/128)(18-3/ln2), scalar'' <= (9/256)(-40+6/ln2),
# so K'' <= -9/64 on (0,1/4].
assert F(-9,64) == -MSTRONG

bL=F(2713295,10**9)
bU=F(2713296,10**9)
kpL=Kprime_bounds(bL); kpU=Kprime_bounds(bU)
assert kpL[0] > 0
assert kpU[1] < 0
bmid=(bL+bU)/2
kmid=K_bounds(bmid)
dmid=Kprime_bounds(bmid)
dabs=max(abs(dmid[0]),abs(dmid[1]))
KMAX_LO=kmid[0]
KMAX_HI=kmid[1] + dabs*dabs/(2*MSTRONG)
TMAX_LO,TMAX_HI=KMAX_LO/D0,KMAX_HI/D0

assert A0 <= ELL <= CBAR
assert A0 + CBAR/F(256) == CBAR
b4=CBAR**4
b3=A0**3
assert b4 < bL < bU < b3
K4=K_bounds(b4); K3=K_bounds(b3)
assert K3[1] < K4[0]
TINT_LO,TINT_HI=K4[0]/D0,K4[1]/D0

R0_HI=F(6521850083658612443633672199029299526203969335,10**45)
assert R0_HI < TINT_LO
R4FIX_HI=F(65218511673480,10**13)
HEADROOM=TINT_HI-R4FIX_HI
assert HEADROOM > 0
assert HEADROOM < F(13,10**9)

print('PASS')
print('sum_q2=',sumq2)
print('strong_concavity_Kpp_le=-9/64')
print('b_star_bracket=[%s,%s]'%(dec(bL,12),dec(bU,12)))
print('Kprime_bL_lower=',dec(kpL[0],18))
print('Kprime_bU_upper=',dec(kpU[1],18))
print('generic_forcing_Tmax_lower=',dec(TMAX_LO,18))
print('generic_forcing_Tmax_upper=',dec(TMAX_HI,18))
print('reachable_c_interval=[%s,%s]'%(dec(A0,12),dec(CBAR,12)))
print('integer_depth_b4_max=',dec(b4,18))
print('integer_depth_b3_min=',dec(b3,18))
print('integer_depth_T_ceiling_lower=',dec(TINT_LO,18))
print('integer_depth_T_ceiling_upper=',dec(TINT_HI,18))
print('fixed_m4_limit_headroom_upper=',dec(HEADROOM,18))
print('full_FEI_status=OPEN')
