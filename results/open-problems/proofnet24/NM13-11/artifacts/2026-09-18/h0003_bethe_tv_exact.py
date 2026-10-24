from fractions import Fraction

# H0003 / Conjecture 11.8, source Example 9.2:
# d=3 and one-edge transmission probability p=3/4.
# Proposition 9.1 gives offspring Bin(d-1,p)=Bin(2,3/4).

p = Fraction(3, 4)

def f(s):
    return (1 - p + p * s) ** 2

q = Fraction(1, 9)
assert f(q) == q
assert f(Fraction(1, 1)) == 1

# 9 q^2 - 10 q + 1 = (9q-1)(q-1).
assert 9*q*q - 10*q + 1 == 0
survival = 1 - q
assert survival == Fraction(8, 9)

# Exact extinction-conditioned offspring law.
# For a GW law with extinction probability q,
# P(K=k | eventual extinction) = P(K=k) q^k / q.
base = [
    (1-p)**2,
    2*p*(1-p),
    p**2,
]
conditioned = [base[k] * q**(k-1) for k in range(3)]
expected_conditioned = [Fraction(9,16), Fraction(3,8), Fraction(1,16)]
assert conditioned == expected_conditioned
assert sum(conditioned) == 1
assert sum(Fraction(k) * conditioned[k] for k in range(3)) == Fraction(1,2)

# This is Bin(2,1/4): coefficients 9/16, 6/16, 1/16.
r = Fraction(1,4)
bin21_4 = [(1-r)**2, 2*r*(1-r), r**2]
assert conditioned == bin21_4

print('offspring=Bin(2,3/4)')
print('extinction_q=1/9')
print('survival_s=8/9')
print('full_tree_TV_lower_bound=8/9')
print('conditioned_offspring=Bin(2,1/4)')
print('conditioned_mean=1/2')
print('ALL_EXACT_CHECKS_PASS')
