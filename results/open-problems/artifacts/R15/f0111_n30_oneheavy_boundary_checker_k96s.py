from fractions import Fraction as F
from math import comb, factorial

# Exact checker for the finite/rational core of R15's n=30 one-heavy boundary exclusion.
# No floating point arithmetic is used.


def bernstein_coeffs_on_2_5_3_5(power_coeffs):
    """P(d)=sum c_k d^k. Substitute d=(2+t)/5, t in [0,1], return degree-n Bernstein coefficients."""
    n = len(power_coeffs)-1
    a = [F(0) for _ in range(n+1)]
    # coefficient of t^j in P((2+t)/5)
    for k, ck in enumerate(power_coeffs):
        for j in range(k+1):
            a[j] += F(ck * comb(k,j) * (2**(k-j)), 5**k)
    beta=[]
    for m in range(n+1):
        beta.append(sum(a[j]*F(comb(m,j),comb(n,j)) for j in range(m+1)))
    return beta


def P_coeffs(N):
    # P_N(d) in C_N'(d) = -2 P_N(d) / positive denominator.
    return [
        N**3 - 21*N**2 + 162*N - 594,
        N**3 - 21*N**2 + 120*N - 774,
        -2*N**3 + 14*N**2 - 52*N - 318,
        -2*N**3 + 22*N**2 - 56*N - 42,
        N**3 + 7*N**2 - 14*N,
        N**3 - N**2,
    ]


def C_lower(d,N):
    a=1+d; b=1-d; D=3+d
    nu=a*a/(2*b*D)
    rho=F(3,1)/D
    L=F(6,1)/b
    E2=nu*(N-L)
    assert E2>0
    Rnum=F(1,1)/b-(b/a)*E2
    return rho+Rnum*Rnum/E2

print('EXACT CHECK: n=30 one-heavy z->1+ boundary')
print('1) Monotonicity C_N\'(delta)>0 on [2/5,3/5] for N=11..14')
for N in range(11,15):
    beta=bernstein_coeffs_on_2_5_3_5(P_coeffs(N))
    assert all(x<0 for x in beta), (N,beta)
    print(f'N={N} Bernstein(P_N)=', ', '.join(str(x) for x in beta))

# Rational points strictly below the lower feasible endpoint delta_N defined by 29(1+delta_N)^3=8N.
points={11:F(447,1000),12:F(2451,5000),13:F(53,100),14:F(71,125)}
print('2) Exact lower bound C_N(delta)>26 on every feasible interval')
for N,d in points.items():
    root_gap=F(8*N,1)-29*(1+d)**3
    assert root_gap>0 # d < delta_N
    c=C_lower(d,N)
    gap=c-26
    assert gap>0
    print(f'N={N} dhat={d} 8N-29(1+dhat)^3={root_gap} C_N(dhat)-26={gap}')

# Global feasibility constants.
dlo=F(2,5); dhi=F(3,5)
# f(delta)=b a^3; f' has sign 1-2delta, and f(1/2)=27/16.
assert 29*(1-dlo)*(1+dlo)**3-48 < 0
assert 29*(1-dhi)*(1+dhi)**3-48 < 0
assert (1-F(1,2))*(1+F(1,2))**3 == F(27,16)
# N range: L>10 and U<15 on (2/5,3/5)
assert F(6,1)/(1-dlo) == 10
assert 29*(1+dhi)**3/F(8,1) == F(1856,125) < 15
# Once N<=14 and N>=L, delta<=4/7.
assert 1-F(6,14) == F(4,7)

# Coarse constants used in value-contact upper bound.
# xi<1 on delta>2/5 because d^2+4d-1>0 there.
assert dlo*dlo+4*dlo-1 > 0
# rho<1 is immediate from D>3.
# nu<1 from a<8/5,b>2/5,D>17/5: ratio <16/17.
assert F(16,17)<1
# U-L <=75/256: numerator max 15/16 and 8b>16/5.
assert (F(15,16))/(F(16,5)) == F(75,256)
# E<9/16 and (b/a)E<1/4 using b/a<3/7.
assert F(75,256) < F(81,256)
assert F(3,7)*F(9,16) == F(27,112) < F(1,4)
# A=29abD/4 is decreasing for d>2/5 and A(2/5)<21.
A_at_dlo=29*(1-dlo)*(1+dlo)*(3+dlo)/4
assert A_at_dlo == F(10353,500) < 21
# A/gamma=29 b a^3 / 48 <=261/256 <51/50.
assert 29*F(27,16)/48 == F(261,256) < F(51,50)
# Qbase=(1+6/a)nu<4 for d<=4/7: numerator 9d^2+24d-17 is increasing and negative at 4/7.
dmax=F(4,7)
assert 9*dmax*dmax+24*dmax-17 == F(-17,49) < 0

print('3) Coarse feasibility/value constants: ALL EXACT')
print('A(2/5)=',A_at_dlo,'; max A/gamma=',F(261,256),'; E^2<',F(75,256))

# log(567)<7 from e^7 > partial Taylor sum > 567.
partial=sum(F(7**k,factorial(k)) for k in range(8))
assert partial == F(47273,72) > 567
# Psi(26) bound using sqrt(26)<6, log567<7:
psi26_upper=(F(2,1)+F(6,4))*7 + (4+6)/F(50,1)
assert psi26_upper == F(247,10) < 26
# Derivative upper for c>=26 using log<=2sqrt(c), sqrt(c)>5.
derivative_upper=F(1,4)+F(2,27)+F(1,20)+F(1,500)
assert derivative_upper < 1
print('4) Psi(26)<26 and Psi\'(c)<1 for c>=26: ALL EXACT')
print('Taylor partial for e^7:',partial,'; Psi(26) upper:',psi26_upper,'; derivative upper:',derivative_upper)
print('ALL_EXACT_CHECKS_PASS')
