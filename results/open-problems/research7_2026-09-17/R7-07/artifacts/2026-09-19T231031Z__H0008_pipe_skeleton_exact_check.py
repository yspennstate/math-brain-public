from fractions import Fraction

# Exact one-type H0008 pipe-resolvent sanity check.
a = Fraction(3, 4)
s = (2*a - 1) / (a*a)
t = a*s
Q = 2*(1-t)*a
EL = Q/(1-Q)
EL2 = Q*(1+Q)/(1-Q)**2

assert s == Fraction(8, 9)
assert t == Fraction(2, 3)
assert Q == Fraction(1, 2)
assert EL == 1
assert EL2 == 3

# Exact deterministic regular-skeleton test.
b = 2
L = 3
Etau2 = Fraction(1, 1) + Fraction(2*L, b-1) + Fraction((b+1)*L*L, (b-1)**2)
assert Etau2 == 34

# Random-pipe formula test with E[L]=2, E[L^2]=5 at b=2.
mu1 = Fraction(2, 1)
mu2 = Fraction(5, 1)
Erand = Fraction(1, 1) + Fraction(2*mu1 + mu2, b-1) + Fraction(2*mu1*mu1, (b-1)**2)
assert Erand == 18

print(f"survival_s={s}")
print(f"positive_child_mass_t={t}")
print(f"pipe_Q={Q}")
print(f"E_L={EL}")
print(f"E_L2={EL2}")
print(f"regular_binary_L3_E_tau2={Etau2}")
print(f"random_pipe_test_E_tau2={Erand}")
print("ALL_EXACT_CHECKS_PASS")
