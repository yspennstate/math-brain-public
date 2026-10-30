from fractions import Fraction
import math

# Exact determinant-permutation threshold.
tau=Fraction(1,4)
m=Fraction(1,2)
bound=tau**4+6*m*m*tau*tau+8*m**3*tau+9*m**4
assert bound == Fraction(233,256)
assert bound < 1

# Normalized branch constants.
case_a=2*math.sqrt(204)*4**(1/3)
case_b=4*math.sqrt(32*math.sqrt(30))*(16/3)**(1/8)*4**(1/4)
assert case_a < 46
assert case_b < 93

# Partner/new three-hub splice.
partner_threehub=3*math.sqrt(2)*256**(1/3)
assert partner_threehub < 26.940

print('QFORM_B06_R46_CHECK_PASS')
print('det_threshold=', bound, float(bound))
print('case_a=', case_a)
print('case_b=', case_b)
print('partner_threehub=', partner_threehub)
