from fractions import Fraction as F

# Fourier-ratio coefficients for exp(theta t^2/24) * sinc(sqrt(theta)t/2).
c2 = F(1,1920) + F(1,1152) - F(1,576)
c3 = -F(1,322560) + F(1,82944) - F(1,27648) + F(1,46080)
assert c2 == -F(1,2880)
assert c3 == -F(1,181440)

# Gaussian cone moments in standardized coordinates.
Ez3_2, Ez3_4, Ez3_6 = F(1,2), F(3,4), F(15,8)
Ez1_2, Ez1_4, Ez1_6 = F(1,4), F(9,32), F(75,128)

H4p = Ez1_4 - 6*Ez1_2 + 3
H4n = Ez3_4 - 6*Ez3_2 + 3
H6p = Ez1_6 - 15*Ez1_4 + 45*Ez1_2 - 15
H6n = Ez3_6 - 15*Ez3_4 + 45*Ez3_2 - 15
assert H4p == F(57,32)
assert H4n == F(3,4)
assert H6p == -F(945,128)
assert H6n == -F(15,8)

qpos = H4p/F(20,1)
qneg = H4n/F(20,1)
cpos = H6p/F(105,1)
cneg = H6n/F(105,1)
assert qpos == F(57,640)
assert qneg == F(3,80)
assert cpos == -F(9,128)
assert cneg == -F(1,56)
assert 2*qpos + qneg == F(69,320)
assert 2*cpos + cneg == -F(71,448)

print('PASS')
print('theta2_fourier_ratio', c2)
print('theta3_fourier_ratio', c3)
print('H4_positive', H4p, 'H4_negative', H4n)
print('H6_positive', H6p, 'H6_negative', H6n)
print('quadratic_positive', -qpos, 'quadratic_negative', -qneg)
print('cubic_positive', cpos, 'cubic_negative', cneg)
print('symmetric_quadratic', -(2*qpos+qneg))
print('symmetric_cubic', 2*cpos+cneg)
