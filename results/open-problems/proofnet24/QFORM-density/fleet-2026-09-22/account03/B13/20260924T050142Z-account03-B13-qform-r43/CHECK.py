import math
from fractions import Fraction

C5 = 2 * math.sqrt(30 * math.pi)
Ktau = 3688.287088390375
a = 10.3
EG = Ktau / a**2
ED = 2 * C5 / (3 * a)
W2 = EG + ED
W = math.sqrt(W2)
H = EG + W2
Kdiag = 1.5 * H
frob_const = math.sqrt(1 + W2)
low_row_const = math.sqrt(a)
high_row_const = math.sqrt(2/7) * W

p = Fraction(2, 5)
q = 1 - 2*p
frob_exp = q/2
diffuse_exp = 3*p - 1

assert 19.4162 < C5 < 19.4163
assert 34.7656 < EG < 34.7657
assert 1.2567 < ED < 1.2568
assert 36.0223 < W2 < 36.0224
assert 6.0018 < W < 6.0019
assert 70.7879 < H < 70.7881
assert 106.1819 < Kdiag < 106.1821
assert 6.0845 < frob_const < 6.0847
assert 3.2093 < low_row_const < 3.2094
assert 3.2080 < high_row_const < 3.2082
assert q == Fraction(1, 5)
assert frob_exp == Fraction(1, 10)
assert diffuse_exp == Fraction(1, 5)

# The p=2/5 choice strictly improves both r42 aggregate exponents.
assert frob_exp > Fraction(1, 12)
assert diffuse_exp > Fraction(1, 6)

# Low-cardinality high-bank diagonal estimate is dominated by Kdiag rho^-q for rho>=1.
assert 2*C5/3 < Kdiag

print(f"C5={C5:.15f}")
print(f"EG={EG:.15f}")
print(f"ED={ED:.15f}")
print(f"W2={W2:.15f}")
print(f"W={W:.15f}")
print(f"H={H:.15f}")
print(f"Kdiag={Kdiag:.15f}")
print(f"frob_const={frob_const:.15f}")
print(f"low_row_const={low_row_const:.15f}")
print(f"high_row_const={high_row_const:.15f}")
print(f"p={p}, q={q}, frob_exp={frob_exp}, diffuse_exp={diffuse_exp}")
print("QFORM_B13_R43_PARETO_SPLIT_CHECK_PASS")
