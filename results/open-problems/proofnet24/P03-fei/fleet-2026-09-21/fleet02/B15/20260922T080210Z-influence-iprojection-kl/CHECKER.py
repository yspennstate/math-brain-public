"""Exact/rational downstream check for fleet02/B15 influence-I-projection theorem.

Consumes the source-bound off-centre Numaro influence vector and entropy enclosure
from completed peer reports. All new root/log bounds are exact Fraction work.
"""
from fractions import Fraction
from math import prod

IT = [
    Fraction(855,4096),
    *([Fraction(125,512)]*4),
    *([Fraction(103,512)]*4),
    Fraction(1,256),
    *([Fraction(3,1024)]*4),
    *([Fraction(5,1024)]*4),
]
V = Fraction(1045327,1048576)
M = [x/V for x in IT]
assert sum(IT) == Fraction(8295,4096)
assert sum(M) == Fraction(2123520,1045327)

# Source-bound total spectral entropy enclosure from fleet03/B12.
H_LO = Fraction(67442547370563132664, 10**19)
H_HI = Fraction(67442547370563132665, 10**19)

def root_eq(c):
    return c - 1 + prod((1-c*x) for x in M)

C_LO = Fraction(8535793515, 10**10)
C_HI = Fraction(8535793516, 10**10)
assert root_eq(C_LO) < 0 < root_eq(C_HI)

def pow2(k):
    return Fraction(1<<k,1) if k >= 0 else Fraction(1,1<<(-k))

def normalize_pow2(x):
    assert x > 0
    k = x.numerator.bit_length() - x.denominator.bit_length()
    while x < pow2(k):
        k -= 1
    while x >= pow2(k+1):
        k += 1
    return k, x/pow2(k)

def ln_unit_bounds(y, terms=100):
    assert 1 <= y <= 2
    z=(y-1)/(y+1)
    z2=z*z
    zp=z
    s=Fraction(0)
    for j in range(terms):
        s += zp/Fraction(2*j+1)
        zp *= z2
    lo=2*s
    tail=2*zp/Fraction(2*terms+1)/(1-z2)
    return lo,lo+tail

LN2_LO,LN2_HI=ln_unit_bounds(Fraction(2))

def log2_bounds(x):
    k,y=normalize_pow2(x)
    lo,hi=ln_unit_bounds(y)
    return Fraction(k)+lo/LN2_HI, Fraction(k)+hi/LN2_LO

def h2_bounds(x):
    if x == 0 or x == 1:
        return Fraction(0),Fraction(0)
    lx_lo,lx_hi=log2_bounds(x)
    ly_lo,ly_hi=log2_bounds(1-x)
    return (-x*lx_hi-(1-x)*ly_hi,
            -x*lx_lo-(1-x)*ly_lo)

def hmu_at(c):
    nlo=Fraction(0); nhi=Fraction(0)
    for mi in M:
        lo,hi=h2_bounds(c*mi)
        nlo += lo; nhi += hi
    hc_lo,hc_hi=h2_bounds(c)
    return (nlo-hc_hi)/c, (nhi-hc_lo)/c

E0_LO,E0_HI=hmu_at(C_LO)
E1_LO,E1_HI=hmu_at(C_HI)
# On this interval c>.85 and every c*m_i lies in (.002,.21).
# Hence |h2'|<9 there and |h2'(c)|<3.  With
# N=sum_i h(c*m_i)-h(c), |N'|<22, |N|<=19, so |(N/c)'|<60.
DERIV=Fraction(60)
width=C_HI-C_LO
HMU_LO=min(E0_LO,E1_LO)-DERIV*width
HMU_HI=max(E0_HI,E1_HI)+DERIV*width
assert HMU_LO > Fraction(700117149,10**8)
assert HMU_HI < Fraction(700117151,10**8)

hv_lo,hv_hi=h2_bounds(V)
HPLUS_LO=(H_LO-hv_hi)/V
HPLUS_HI=(H_HI-hv_lo)/V
KINT_LO=HMU_LO-HPLUS_HI
KINT_HI=HMU_HI-HPLUS_LO
assert KINT_LO > Fraction(26633566,10**8)
assert KINT_HI < Fraction(26633568,10**8)

# Source-exact Gamma^dagger node values from fleet03/B12.
C_DAG=Fraction(6521851214,10**9)
C0=Fraction(64548,10000)
A_DAG=4*(C_DAG-C0)
p1=Fraction(3,8)
q=Fraction(967,2048)
V1=Fraction(15,16)
G1_NODE=Fraction(8766995320315105,562949953421312)
GQ_NODE=Fraction(7680879056207109,562949953421312)
GAMMA1=p1*G1_NODE+A_DAG*p1*(1-p1)
GAMMAQ=q*GQ_NODE+A_DAG*q*(1-q)

h1_lo,h1_hi=h2_bounds(V1)
a1_lo=(GAMMA1+h1_lo)/V1
a1_hi=(GAMMA1+h1_hi)/V1
aq_lo=(GAMMAQ+hv_lo)/V
aq_hi=(GAMMAQ+hv_hi)/V
m1=M[0]
d=sum(M)
sum_a_lo=m1*a1_lo+(d-m1)*C_DAG
sum_a_hi=m1*a1_hi+(d-m1)*C_DAG
RMF_LO=HMU_LO+aq_lo-sum_a_hi
RMF_HI=HMU_HI+aq_hi-sum_a_lo
assert RMF_LO > Fraction(28400182,10**8)
assert RMF_HI < Fraction(28400184,10**8)

DEFN_LO=KINT_LO-RMF_HI
DEFN_HI=KINT_HI-RMF_LO
assert DEFN_HI < Fraction(-1766614,10**8)
assert DEFN_LO > Fraction(-1766620,10**8)

def dec(x, digits=15):
    scale=10**digits
    if x >= 0:
        n=(x.numerator*scale)//x.denominator
        return f"{n//scale}.{n%scale:0{digits}d}"
    y=-x
    n=(y.numerator*scale)//y.denominator
    return f"-{n//scale}.{n%scale:0{digits}d}"

print("PASS")
print("sum_It", f"{sum(IT).numerator}/{sum(IT).denominator}")
print("variance", f"{V.numerator}/{V.denominator}")
print("sum_m", f"{sum(M).numerator}/{sum(M).denominator}")
print("c_bracket", dec(C_LO), dec(C_HI))
print("Hmu_bracket", dec(HMU_LO), dec(HMU_HI))
print("Hplus_bracket", dec(HPLUS_LO), dec(HPLUS_HI))
print("Kint_bracket", dec(KINT_LO), dec(KINT_HI))
print("Rmf_Gammadag_bracket", dec(RMF_LO), dec(RMF_HI))
print("normalized_defect_bracket", dec(DEFN_LO), dec(DEFN_HI))
