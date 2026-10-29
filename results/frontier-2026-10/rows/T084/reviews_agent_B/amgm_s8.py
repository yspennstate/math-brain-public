# T084, agent B: the AM-GM certificate on the control S8 (binary, not Rayleigh, bad pair (0,4)) and its good pair (0,7):
# which monomials stay uncovered, and what the coefficient is.
exec(open('amgm_cert.py').read().split("if __name__")[0])
A = [0b0111, 0b1011, 0b1101, 0b1111]
cols = [1, 2, 4, 8] + [sum(((A[r] >> (3 - c)) & 1) << r for r in range(4)) for c in range(4)]
for e, f in [(0, 4), (0, 7), (0, 1), (4, 5)]: certify('S8', cols, e, f)
