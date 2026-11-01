from fractions import Fraction
import sympy as sp

# Exact self-check for P15-I0066-RANDOMIZATION-NOGO-06.
# This checks only the finite algebraic core; the infinite-depth SMR failure
# is inherited from the already-proved geometric-shift endpoint theorem.

eps = Fraction(1, 1000)
r = Fraction(2, 1)
annealed = eps * r
assert annealed == Fraction(1, 500)
assert annealed < 2

O = sp.Matrix([[sp.Rational(3,5), sp.Rational(4,5)],
               [sp.Rational(-4,5), sp.Rational(3,5)]])
assert O.T * O == sp.eye(2)

B1 = sp.Matrix([[0,1],[2,-1]])
B2 = sp.Matrix([[1,2],[-1,0]])
Bt1 = O[0,0]*B1 + O[0,1]*B2
Bt2 = O[1,0]*B1 + O[1,1]*B2

sum_orig = B1.T*B1 + B2.T*B2
sum_rot = Bt1.T*Bt1 + Bt2.T*Bt2
assert sp.simplify(sum_rot - sum_orig) == sp.zeros(2)

H = sp.Matrix([[sp.Rational(7,3), sp.Rational(2,5)],
               [sp.Rational(2,5), sp.Rational(11,4)]])
y = sp.Matrix([sp.Rational(5,7), sp.Rational(-3,8)])

def hess_q(B):
    v = B*y
    return sp.expand((v.T*H*v)[0])

hess_orig = sp.simplify(hess_q(B1) + hess_q(B2))
hess_rot = sp.simplify(hess_q(Bt1) + hess_q(Bt2))
assert hess_orig == hess_rot

print('P15 I0066 randomization no-go exact checker')
print('orthogonal_O =', O)
print('sum_BtB_original =', sum_orig)
print('sum_BtB_rotated =', sum_rot)
print('generic_hessian_sum =', hess_orig)
print('annealed_eps =', eps)
print('annealed_E_c2_times_r =', annealed)
print('bad_environment_probability =', eps)
print('bad_environment_endpoint_c2r =', r)
print('ALL_EXACT_CHECKS_PASSED')
