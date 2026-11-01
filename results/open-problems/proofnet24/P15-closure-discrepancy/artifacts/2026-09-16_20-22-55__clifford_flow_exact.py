import sympy as sp

I = sp.I
sigma1 = sp.Matrix([[0, 1], [1, 0]])
sigma2 = sp.Matrix([[0, -I], [I, 0]])
sigma3 = sp.Matrix([[1, 0], [0, -1]])
Id = sp.eye(2)

assert sigma1 * sigma1 == Id
assert sigma2 * sigma2 == Id
assert sigma1 * sigma2 - sigma2 * sigma1 == 2 * I * sigma3

n, tau, a, b, c, d = sp.symbols("n tau a b c d")
B1 = I * tau * n * sigma1
B2 = I * tau * n * sigma2
C = sp.simplify((B1 * B1 + B2 * B2) / 2)
Comm = sp.simplify(B1 * B2 - B2 * B1)

assert C == -tau**2 * n**2 * Id
assert Comm == -2 * I * tau**2 * n**2 * sigma3

R1 = a * B1 + b * B2
R2 = c * B1 + d * B2
assert sp.simplify(R1 * R2 - R2 * R1 - (a * d - b * c) * Comm) == sp.zeros(2)

# Exact rational orthogonal rotation [[3/5,4/5],[-4/5,3/5]].
aa, bb = sp.Rational(3, 5), sp.Rational(4, 5)
cc, dd = -sp.Rational(4, 5), sp.Rational(3, 5)
RB1 = aa * B1 + bb * B2
RB2 = cc * B1 + dd * B2
assert sp.simplify((RB1 * RB1 + RB2 * RB2) - (B1 * B1 + B2 * B2)) == sp.zeros(2)
assert sp.simplify((RB1 * RB2 - RB2 * RB1) - Comm) == sp.zeros(2)

print("sigma1^2=sigma2^2=I")
print("[sigma1,sigma2]=2*i*sigma3")
print("C=(B1^2+B2^2)/2=-tau^2*n^2*I")
print("[B1,B2]=-2*i*tau^2*n^2*sigma3")
print("[aB1+bB2,cB1+dB2]=(ad-bc)[B1,B2]")
print("3-4-5 orthogonal noise rotation preserves sum-of-squares correction and commutator")
print("ALL_EXACT_CHECKS_PASSED")
