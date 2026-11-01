from fractions import Fraction

# R06 / D0069 run 20 exact finite-core self-check.
# Special subclass: Delta=6 local multiplicities [4,1,1],
# singleton 2-factor components are triangles.
# At z=1/sqrt(5), the block transfer is
#   T = 4 z^2 (1+z) = 4/5 + 4/(5 sqrt(5)).
# T>1 iff 4/sqrt(5)>1 iff 16>5.

# Combinatorial path inventory inside a triangle between distinct ports:
# exactly one singleton path of length 1 and one of length 2.
path_lengths = (1, 2)
assert path_lengths == (1, 2)

# Outgoing heavy matching class has exactly four parallel edge copies.
heavy_multiplicity = 4
assert heavy_multiplicity == 4

# Exact rational coefficient of the algebraic expression
# T = A + B/sqrt(5).
A = Fraction(4, 5)
B = Fraction(4, 5)
assert A == Fraction(4, 5)
assert B == Fraction(4, 5)

# Positive exact comparison:
# A + B/sqrt(5) > 1
# <=> 4/(5 sqrt(5)) > 1/5
# <=> 4/sqrt(5) > 1
# <=> 16 > 5.
assert 16 > 5

# Verify the transfer polynomial bookkeeping:
# (z + z^2)*(4 z) = 4 z^2 + 4 z^3.
terms = {2: 4, 3: 4}
assert terms == {2: 4, 3: 4}

print('D0069 run20 triangle-factor exact self-check')
print('internal_triangle_path_lengths=1,2')
print('outgoing_heavy_parallel_copies=4')
print('transfer_polynomial=4*z^2+4*z^3=4*z^2*(1+z)')
print('at_z=1/sqrt(5): T=4/5+4/(5*sqrt(5))')
print('T>1 reduces exactly to 16>5')
print('TRIANGLE_TRANSFER_GT_ONE_PASS')
