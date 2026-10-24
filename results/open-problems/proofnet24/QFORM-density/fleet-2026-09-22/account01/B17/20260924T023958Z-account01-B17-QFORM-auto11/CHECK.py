import sympy as s

M = s.Integer(100000)
D = M**2 + 5
n = s.Matrix([2*M, 4*M, M**2 - 5]) / D
assert s.simplify((n.T*n)[0]) == 1

B = s.eye(3) - 2*n*n.T
assert (B*B - s.eye(3)).applyfunc(s.simplify) == s.zeros(3)

claimed = {
    (0,0): (M**4 + 2*M**2 + 25)/D**2,
    (1,1): (M**4 - 22*M**2 + 25)/D**2,
    (2,2): (-M**4 + 30*M**2 - 25)/D**2,
    (0,1): -16*M**2/D**2,
    (0,2): -4*M*(M**2 - 5)/D**2,
    (1,2): -8*M*(M**2 - 5)/D**2,
}
for (i,j), v in claimed.items():
    assert s.simplify(B[i,j] - v) == 0
    if i != j:
        assert s.simplify(B[j,i] - v) == 0
assert all(B[i,j] != 0 for i in range(3) for j in range(3))

Aleaf = s.Matrix([[0,4,1],[4,0,0],[1,0,4]])
K = Aleaf**2 - s.eye(3)
mins = [K[:k,:k].det() for k in (1,2,3)]
assert mins == [16, 240, 3344]

x = s.symbols('x', positive=True)
f12 = 2*s.pi - 8*s.sqrt(2*x) + 4*x
h = s.sqrt(2)/s.sqrt(x) - 2
pj = s.simplify(s.integrate(f12*h, (x, 0, s.Rational(1,2))))
assert s.simplify(pj - (2*s.pi - s.Rational(7,3))) == 0

lb = s.N(pj - 6*s.pi*s.sqrt(30)/M, 40)
assert lb > s.Float('3.9488')
partner = s.N((2+s.log(4))/4, 40)
assert partner < 1

print('PASS QFORM_B17_DENSE_SIX_WITNESS')
print('aligned_tip=', s.N(pj, 20))
print('certified_dense_tip_lower=', lb)
print('partner_actual_target_bound=', partner)
print('Aleaf_A2minusI_leading_minors=', mins)
