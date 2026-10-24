from fractions import Fraction
import math
import mpmath as mp

mp.mp.dps = 80

# ln(4/3) < alternating five-term upper < 0.288.
log_upper_5 = (Fraction(1,3)-Fraction(1,18)+Fraction(1,81)
               -Fraction(1,324)+Fraction(1,1215))
assert log_upper_5 == Fraction(1399,4860)
assert log_upper_5 < Fraction(36,125)

# Elementary certificate ln(10)<2.303: positive degree-9 Taylor sum of exp(2.303) already exceeds 10.
x = Fraction(2303,1000)
exp_t9 = sum(x**k / Fraction(math.factorial(k),1) for k in range(10))
assert exp_t9 > 10

# Standard harmonic-log remainder: gamma > H_n-ln n-1/(2n). At n=10 this gives gamma>0.57.
H10 = sum(Fraction(1,k) for k in range(1,11))
gamma_lb = H10 - Fraction(2303,1000) - Fraction(1,20)
assert gamma_lb == Fraction(18143,31500)
assert gamma_lb > Fraction(57,100)

# Small-output exact upper comparison. Use pi>3.14 and sqrt(2)>1.414.
B_ub = Fraction(5,2)+Fraction(36,125)-Fraction(57,100)
Csmall_rat_ub = 6*B_ub/Fraction(157,50)
sqrt2_lb = Fraction(707,500)
assert sqrt2_lb*sqrt2_lb < 2
assert Csmall_rat_ub == Fraction(3327,785)
assert Csmall_rat_ub < 3*sqrt2_lb

# Large-output endpoint comparison.
# e^(3/4)> degree-6 Taylor > 1/.473.
x75=Fraction(3,4)
exp75_t6=sum(x75**k/Fraction(math.factorial(k),1) for k in range(7))
assert exp75_t6 > Fraction(1000,473)
# sqrt(2)<1.415 and e^.882>degree-6 Taylor>2.415, hence acosh(sqrt2)<.882.
sqrt2_ub=Fraction(283,200)
assert sqrt2_ub*sqrt2_ub > 2
x882=Fraction(441,500)
exp882_t6=sum(x882**k/Fraction(math.factorial(k),1) for k in range(7))
assert exp882_t6 > Fraction(483,200)
assert 1+sqrt2_ub == Fraction(483,200)
# sqrt(3/pi)<.978 follows from pi>3.14; pi<22/7 in the bracket.
assert Fraction(150,157) < Fraction(489,500)**2
Clarge_rat_ub=(2*Fraction(489,500)
               *(Fraction(11,14)*Fraction(1473,1000)+Fraction(441,500)))
assert Clarge_rat_ub == Fraction(13961439,3500000)
assert Clarge_rat_ub < 3*sqrt2_lb

# High-precision values (diagnostic only; inequalities above carry rational certificates apart from standard pi bounds).
gamma=mp.euler
Csmall=6/mp.pi*(mp.mpf(5)/2+mp.log(mp.mpf(4)/3)-gamma)
Clarge=2*mp.sqrt(3/mp.pi)*(mp.pi/4*(1+mp.e**(-mp.mpf(3)/4))+mp.acosh(mp.sqrt(2)))
baseline=3*mp.sqrt(2)
actual0=12/mp.pi*mp.quad(lambda z: mp.besselk(0,6*z*z), [0, mp.mpf('0.5')])

print('PASS QFORM-ONE-HEAVY-MAJORITY-GAUSSIAN-NOESCAPE-v1')
print('log_upper_5', log_upper_5, mp.nstr(mp.mpf(log_upper_5.numerator)/log_upper_5.denominator,30))
print('gamma_lower_certificate', gamma_lb, mp.nstr(mp.mpf(gamma_lb.numerator)/gamma_lb.denominator,30))
print('Csmall_rational_upper', Csmall_rat_ub, mp.nstr(mp.mpf(Csmall_rat_ub.numerator)/Csmall_rat_ub.denominator,30))
print('Clarge_rational_upper', Clarge_rat_ub, mp.nstr(mp.mpf(Clarge_rat_ub.numerator)/Clarge_rat_ub.denominator,30))
print('Csmall', mp.nstr(Csmall,30))
print('Clarge', mp.nstr(Clarge,30))
print('3sqrt2', mp.nstr(baseline,30))
print('small_gap', mp.nstr(baseline-Csmall,30))
print('large_gap', mp.nstr(baseline-Clarge,30))
print('centered_heavy_p0_diagnostic', mp.nstr(actual0,30))
