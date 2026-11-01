import sympy as sp

rho, k = sp.symbols('rho k', positive=True)
R0 = sp.Matrix([
    [sp.Rational(1,2),  sp.sqrt(rho)/2, 0],
    [sp.Rational(1,2),  sp.sqrt(rho)/2, 0],
    [sp.Rational(1,2), -sp.sqrt(rho)/2, 0],
    [sp.Rational(1,2), -sp.sqrt(rho)/2, 0],
    [0, sp.sqrt(1-rho)/2,  sp.Rational(1,2)],
    [0, sp.sqrt(1-rho)/2,  sp.Rational(1,2)],
    [0, sp.sqrt(1-rho)/2, -sp.Rational(1,2)],
    [0, sp.sqrt(1-rho)/2, -sp.Rational(1,2)],
])
assert sp.simplify(R0.T*R0 - sp.eye(3)) == sp.zeros(3)

def vol2(ids):
    B = R0[list(ids), :]
    return sp.simplify(B.det()**2)

assert vol2((0,2,4)) == rho/16
assert vol2((1,3,7)) == rho/16
assert vol2((0,4,6)) == (1-rho)/16
assert vol2((3,5,7)) == (1-rho)/16

M = sp.Matrix([[1,0,0],[0,0,1],[0,1,0]])
assert sorted(M.eigenvals().keys(), key=lambda x: float(x)) == [-1,1]

srow = sp.Matrix([1/(2*sp.sqrt(k)), sp.sqrt(rho)/(2*sp.sqrt(k)), 0])
tprow = sp.Matrix([0, sp.sqrt(1-rho)/(2*sp.sqrt(k)), 1/(2*sp.sqrt(k))])
tmrow = sp.Matrix([0, sp.sqrt(1-rho)/(2*sp.sqrt(k)), -1/(2*sp.sqrt(k))])
q = lambda r: sp.simplify((r.T*M*r)[0])
assert q(srow) == 1/(4*k)
assert q(tprow) == sp.sqrt(1-rho)/(2*k)
assert q(tmrow) == -sp.sqrt(1-rho)/(2*k)

theta_T = sp.simplify(rho*(sp.Rational(1,4)/k)*sp.sqrt(1-rho)/(2*k))
theta_S = sp.simplify((1-rho)*(sp.Rational(1,4)/k)*(sp.Rational(1,4)/k))
assert theta_T == rho*sp.sqrt(1-rho)/(8*k**2)
assert theta_S == (1-rho)/(16*k**2)
assert sp.simplify(theta_T.subs(rho,sp.Rational(1,2)) - sp.sqrt(2)/(32*k**2)) == 0
assert sp.simplify(theta_S.subs(rho,sp.Rational(1,2)) - 1/(32*k**2)) == 0

row_norm_sq = sp.simplify((srow.T*srow)[0].subs(rho,sp.Rational(1,2)))
assert row_norm_sq == sp.Rational(3,8)/k
hadamard_vol_cap = sp.simplify(row_norm_sq**3)
assert hadamard_vol_cap == sp.Rational(27,512)/k**3

C = sp.simplify(6*2**(sp.Rational(5,3)))
print('R0^T R0 = I3: PASS')
print('SST triple volume^2 = rho/16: PASS')
print('STT triple volume^2 = (1-rho)/16: PASS')
print('M spectrum = {1,1,-1}: PASS')
print('theta_T = rho*sqrt(1-rho)/(8 k^2): PASS')
print('theta_S(reflected) = (1-rho)/(16 k^2): PASS')
print('rho=1/2: theta_T = sqrt(2)/(32 k^2), theta_S = 1/(32 k^2): PASS')
print('rho=1/2 raw triple Hadamard volume cap = 27/(512 k^3): PASS')
print('grouped partner constant 6*2^(5/3) =', sp.N(C, 15))
print('QFORM_B11_R32_GROUPED_FOUR_RAY_CHECK_PASS')
