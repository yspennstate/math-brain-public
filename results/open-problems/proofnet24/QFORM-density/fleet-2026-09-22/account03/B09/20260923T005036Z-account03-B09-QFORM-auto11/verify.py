import math
import sympy as sp

C_lin = 5 * 3**(3/5) / 2**(6/5)
C_phys = C_lin * math.e**(1/10)
print('C_lin =', repr(C_lin))
print('C_phys =', repr(C_phys))
assert C_lin < 4.208
assert C_phys < 4.650

lam = sp.symbols('lam')
M = sp.Matrix([
    [2,1,0,1,0],
    [1,0,0,1,0],
    [0,0,0,0,1],
    [1,1,0,0,0],
    [0,0,1,0,0],
])
cp = sp.factor(M.charpoly(lam).as_expr())
expected = sp.factor(lam*(lam-3)*(lam-1)*(lam+1)**2)
print('charpoly =', cp)
assert sp.expand(cp-expected) == 0

# Verify the left-shear kernel identity symbolically in the survivor r=C*kappa,
# s=B.T*kappa, a=kappa.T*C*kappa.
c11,c12,c22,b11,b12,b21,b22,k1,k2,d11,d12,d22 = sp.symbols(
    'c11 c12 c22 b11 b12 b21 b22 k1 k2 d11 d12 d22'
)
C = sp.Matrix([[c11,c12],[c12,c22]])
B = sp.Matrix([[b11,b12],[b21,b22]])
D = sp.Matrix([[d11,d12],[d12,d22]])
k = sp.Matrix([k1,k2])
r = C*k
s = B.T*k
a = (k.T*C*k)[0]
M5 = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.Matrix([[a]]), r.T, s.T),
    sp.Matrix.hstack(r, C, B),
    sp.Matrix.hstack(s, B.T, D),
)
h = sp.Matrix([1,-k1,-k2,0,0])
res = sp.simplify(M5*h)
print('kernel residual =', list(res))
assert res == sp.zeros(5,1)

print('all checks passed')
