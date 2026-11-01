import sympy as sp

a = b = c = sp.Integer(1)
C = sp.Matrix([[0,a,c],[a,0,b],[c,b,0]])
M = C + sp.eye(3)
A = sp.zeros(5)
A[:3,:3] = sp.ones(3)
A[3,3] = 1
A[4,4] = 1

print('C_eigs=', C.eigenvals())
print('rank_one_completion_rank=', M.rank())
print('rank_one_completion=', M.tolist())
print('target_eigs=', A.eigenvals())

for y in [sp.Rational(1,100), sp.Rational(1,10000), sp.Rational(1,1000000)]:
    p = (sp.Rational(3,4)-y)/sp.sqrt(y)
    print('p_Q0', y, '=', sp.N(p, 12))

print('stationary_abs_constant=', sp.N(sp.Rational(3,4)*sp.sqrt(sp.pi), 16))

assert C.det() == 2
assert sorted([ev for ev,mult in C.eigenvals().items() for _ in range(mult)]) == [-1,-1,2]
assert M.rank() == 1
assert A.eigenvals()[sp.Integer(3)] == 1
assert A.eigenvals()[sp.Integer(1)] == 2
print('STATUS=PASS')
