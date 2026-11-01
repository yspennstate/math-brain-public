# T084, agent B: the exact AM-GM certificate on R10, every one of its 45 pairs (no symmetry assumed).
import itertools
exec(open('amgm_cert.py').read().split("if __name__")[0])
A = [0b11001, 0b11100, 0b01110, 0b00111, 0b10011]
colsR10 = [1 << i for i in range(5)] + [sum(((A[row] >> (4 - c)) & 1) << row for row in range(5)) for c in range(5)]
for e, f in itertools.combinations(range(10), 2): certify('R10', colsR10, e, f)
