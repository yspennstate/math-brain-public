#!/usr/bin/env python3
import math

alpha = 157/320
C_second_pivot = math.sqrt(2) * (12 + math.log(625/2))
C_outer_second = C_second_pivot / math.sqrt(alpha)
C_two_cross_halfriesz = 32.0
C_outer_two_cross = C_two_cross_halfriesz / math.sqrt(alpha)

# f(a)=a^{-1/2}(12+log(625a)) decreases for a>=1/2.
derivative_numerator_at_half = 1 - 0.5*(12 + math.log(625/2))
assert derivative_numerator_at_half < 0

assert C_second_pivot < 25.095
assert C_outer_second < 35.827
assert C_outer_two_cross < 45.686

print('C_second_pivot =', C_second_pivot)
print('C_outer_second =', C_outer_second)
print('C_two_cross_halfriesz =', C_two_cross_halfriesz)
print('C_outer_two_cross =', C_outer_two_cross)
print('derivative numerator at a=1/2 =', derivative_numerator_at_half)
print('PASS')
