from fractions import Fraction

m = Fraction(3501, 8000)
r = Fraction(1, 1024)
delta = Fraction(1, 64) - r*r

# Sequential-two-pivot branch at |d|=1/1024 with log_+=0:
# 256*sqrt(2)/sqrt(m) < 548.
assert Fraction(256**2 * 2, 1) < Fraction(548**2, 1) * m

# Small-small branch: |det Schur_2| > 1/64 - 1/1024^2.
# Physical-triple bound 128*(m^2*delta)^(-1/4) < 548.
assert Fraction(128**4, 1) < Fraction(548**4, 1) * m*m*delta

# Activation point of log_+ in the sequential theorem is u0=4/625,
# and r<u0. Above u0, derivative of u^(-1/2)(2+log(Ku^(1/4))) is negative.
assert r < Fraction(4, 625)

print("QFORM_B20_R18_V2_CHECK_PASS")
