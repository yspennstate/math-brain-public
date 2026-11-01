from fractions import Fraction

# Exact finite self-check for the critical m=2, {0,3}-supported obstruction
# isolated in the R7-02 D0059 run.  No floating point arithmetic is used.

m = 2
L = 3
p0 = Fraction(16, 17)
pL = Fraction(1, 17)

assert p0 + pL == 1

G0 = p0 + pL * (m ** L)
EXm = pL * L * (m ** L)
assert (m - 1) * EXm == G0  # exact criticality

G1 = (G0 ** m + (m - 1) * p0 ** m) / m
eps0 = G0 - 1
eps1 = G1 - 1

# Exact one-step decomposition from the source pgf recurrence:
# eps_{n+1}-eps_n = (m-1) [H_m(eps_n)-p_n],
# p_n=(1-G_n(0)^m)/m,
# H_m(e)=((1+e)^m-1-me)/(m(m-1)).
p_harris = (1 - p0 ** m) / m
H = ((1 + eps0) ** m - 1 - m * eps0) / (m * (m - 1))
assert eps1 - eps0 == (m - 1) * (H - p_harris)
assert eps1 > eps0

print(f"p0={p0}")
print(f"p3={pL}")
print(f"G0(2)={G0}")
print(f"E[X0*2^X0]={EXm}")
print(f"G1(2)={G1}")
print(f"eps0={eps0}")
print(f"eps1={eps1}")
print(f"eps1-eps0={eps1-eps0}")
print(f"p_0=(1-G0(0)^2)/2={p_harris}")
print(f"H_2(eps0)={H}")
print("EXACT_CHECK_PASS")
