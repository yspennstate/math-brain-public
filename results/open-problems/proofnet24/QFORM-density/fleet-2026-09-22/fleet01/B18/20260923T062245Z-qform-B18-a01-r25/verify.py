import sympy as sp

# Symbols for r>=1: t=1/sqrt(1+r^2), k=r/sqrt(1+r^2), so k^2=1-t^2.
t, k = sp.symbols('t k', positive=True, real=True)
rt2 = sp.sqrt(2)

# Active conditional matrix in (X0,P,N).
H = sp.Matrix([
    [0, k, -k],
    [k, 1 + 2*t, 1],
    [-k, 1, 1 - 2*t],
])

# Pair rotation: C=(P-N)/sqrt(2), D=(P+N)/sqrt(2).
U = sp.Matrix([
    [1, 0, 0],
    [0, 1/rt2, 1/rt2],
    [0, -1/rt2, 1/rt2],
])
Hp = sp.simplify(U.T * H * U)
expected = sp.Matrix([
    [0, rt2*k, 0],
    [rt2*k, 0, 2*t],
    [0, 2*t, 2],
])
assert sp.simplify(Hp - expected) == sp.zeros(3)
assert sp.factor(H.det()) == -4*k**2
assert sp.factor(Hp.det()) == -4*k**2

# Partner parameters beta=sqrt(2)k, gamma=2.
beta = rt2*k
gamma = sp.Integer(2)
assert sp.simplify(beta**2 * gamma - 4*k**2) == 0

# With K=1 and M=8, partner bound simplifies exactly to 12*k^(-2/3).
B = sp.Integer(3) * (sp.Integer(16))**(sp.Rational(2,3)) * (4*k**2)**(-sp.Rational(1,3))
assert sp.simplify(B - 12*k**(-sp.Rational(2,3))) == 0

# r>=1 gives k^2>=1/2 and hence B<=12*2^(1/3).
print('Hprime =', Hp)
print('det(Hprime) =', sp.factor(Hp.det()))
print('partner bound =', sp.simplify(B))
print('uniform constant =', float(12 * 2**(sp.Rational(1,3))))
print('one-sheet partner constant pi*sqrt(2) =', float(sp.pi * sp.sqrt(2)))
