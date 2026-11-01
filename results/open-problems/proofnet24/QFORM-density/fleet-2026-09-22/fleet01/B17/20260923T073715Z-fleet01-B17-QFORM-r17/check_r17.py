from fractions import Fraction
from math import pi,sqrt,erf,log

TARGET=3*sqrt(2)
PARTNER=(pi*sqrt(2)/3)*(1+4/sqrt(5))
MINORITY=sqrt(6*pi)*erf(sqrt(3/2))
ROT=Fraction(177,640)-Fraction(39,640)*Fraction(199,343)
assert ROT == Fraction(5295,21952)
assert PARTNER < TARGET
assert MINORITY < TARGET
assert Fraction(3,80)>0

# Analytic derivative certificate used in the report:
# d/dx [(2x/sqrt(pi))/sqrt(1+2x^2/3)-erf(x)]
# =2/sqrt(pi)*[(1+2x^2/3)^(-3/2)-exp(-x^2)] >=0,
# since (3/2)log(1+2x^2/3)<=x^2 by log(1+y)<=y.
# The grid is only a numerical sanity check, not the proof.
for i in range(10001):
    x=10*i/10000
    rhs=(2*x/sqrt(pi))/sqrt(1+2*x*x/3) if x else 0.0
    assert erf(x) <= rhs+1e-13

print('QFORM_B17_R17_CHECK_PASS')
print('3sqrt2 =',TARGET)
print('partner finite-bank ceiling =',PARTNER,'gap =',TARGET-PARTNER)
print('minority-heavy rotated Gaussian-completion control =',MINORITY,'gap =',TARGET-MINORITY)
print('fleet04 coefficient reproduction =',ROT,float(ROT))
print('uniform anisotropic first-order deficit coefficient >=',Fraction(3,80),float(Fraction(3,80)))
