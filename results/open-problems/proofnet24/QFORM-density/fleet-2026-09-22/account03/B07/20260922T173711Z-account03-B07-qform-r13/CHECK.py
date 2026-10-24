from fractions import Fraction
from math import e, sqrt

# Exact collars used in REPORT.md.
E = Fraction(1, 256)
assert E / 16 == Fraction(1, 4096)
assert (E / 16) * Fraction(1, 16) == Fraction(1, 65536)

# Heavy-triple contraction determinant gate.
assert 3 * Fraction(3, 4) - 2 == Fraction(1, 4)
# Transpose 11/16 heavy-triple determinant gate.
assert 3 * Fraction(11, 16) - 2 == Fraction(1, 16)

# Peer theorem bound at q=11/8 and E_H=1/4096.
q = Fraction(11, 8)
assert 3 - 2*q == Fraction(1, 4)
# Exactly: 4096 = 4^6, hence E_H^(-1/6)=4.
assert 4**6 == 4096
bound = 96 * e / sqrt(11)
assert bound < 79

# Six-coordinate determinant collar.
# squared determinant >=1/65536, hence absolute determinant >=1/256.
assert Fraction(1, 256) ** 2 == Fraction(1, 65536)

print({
    "E_over_16": str(E/16),
    "row_heavy_det_gate": str(3*Fraction(3,4)-2),
    "transpose_det_gate": str(3*Fraction(11,16)-2),
    "cross_minor_sq_floor": str(Fraction(1,65536)),
    "peer_density_bound": bound,
})
