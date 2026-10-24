from fractions import Fraction

ETA = Fraction(1, 16)
A = Fraction(7, 8)  # 1 - 2*ETA
LAMBDA = Fraction(8, 5)

max_ratio = Fraction(0)
argmax_ratio = None
max_kraft = Fraction(0)
argmax_kraft = None

for r in range(1, 257):
    # Code alphabet at one robust pivotal row:
    # typical: flag=0, row-child bit, orientation bit (4 words, length 3)
    # exceptional: flag=1, row-child bit, orientation bit, index of
    # actual trigger word among all words except the proxy word.
    # For r=1 the exceptional trigger word is unique, so no index bit is needed.
    m = 0 if r == 1 else r
    kraft = Fraction(4, 2**3) + Fraction(4 * (2**r - 1), 2**(3 + m))
    assert kraft <= 1

    ratio = (Fraction(3) + ETA * m) / (Fraction(1) + A * r)
    assert ratio <= LAMBDA

    if ratio > max_ratio:
        max_ratio = ratio
        argmax_ratio = r
    if kraft > max_kraft:
        max_kraft = kraft
        argmax_kraft = r

# Genuine Boolean orientation witness:
# f(x_i,y,z)=z*(x_i if y is the trigger word else 1).
# On the trigger subcube, D_i f=z, so the sign is balanced and cannot be dropped.
signs = []
for z in (-1, 1):
    f_plus = z
    f_minus = -z
    d_i = (f_plus - f_minus) // 2
    signs.append(d_i)
assert sorted(signs) == [-1, 1]

print("eta", ETA)
print("max_ratio", max_ratio, "argmax_r", argmax_ratio)
print("max_kraft", max_kraft, "argmax_r", argmax_kraft)
for r in (1, 2, 3, 8, 32):
    m = 0 if r == 1 else r
    kraft = Fraction(4, 8) + Fraction(4 * (2**r - 1), 2**(3 + m))
    ratio = (Fraction(3) + ETA * m) / (Fraction(1) + A * r)
    print(r, "kraft", kraft, "ratio", ratio)
print("orientation_witness_signs", signs)
print("RESULT PASS")
