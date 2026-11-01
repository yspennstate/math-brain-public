from fractions import Fraction
import math

root = 3456 ** (1/5)
C_half = 5 * math.e * root
q = Fraction(6, 5)
gap = Fraction(5, 2) - 2*q
assert gap == Fraction(1, 10)
C_three_fifths = 5 * math.e / (math.sqrt(float(q)) * (5 - 4*float(q))) * root
C_three_fifths_alt = 25 * math.e * math.sqrt(5/6) * root
assert abs(C_three_fifths - C_three_fifths_alt) < 1e-12
assert C_half < 70
assert C_three_fifths < 317
assert Fraction(3,5) / 6912 == Fraction(1,11520)

# Check the general coefficient specializes correctly.
def coeff(q):
    return 5*math.e/(math.sqrt(q)*(5-4*q))

assert abs(coeff(1.0) - 5*math.e) < 1e-12
assert abs(coeff(6/5) - 25*math.e*math.sqrt(5/6)) < 1e-12

# Coarse entropy-factor inequality log H_q(c) <= c(1-log q)/2
# sampled only as an arithmetic regression check, not as the proof.
def logH(q,c):
    if c == 0:
        return 0.0
    return (q/2-c)*math.log(q) - (q-c)*math.log(q-c)/2

for qv in (1.0, 1.05, 1.125, 1.2, 1.24):
    for j in range(101):
        c = (qv/2)*j/100
        assert logH(qv,c) <= c*(1-math.log(qv))/2 + 1e-12

print('root_3456_1_5', root)
print('C_half', C_half)
print('q_three_fifths', float(q))
print('integrability_gap', float(gap))
print('C_three_fifths', C_three_fifths)
print('nested_fraction', float(Fraction(1,11520)))
print('QFORM_B08_R28_CHECK_PASS')
