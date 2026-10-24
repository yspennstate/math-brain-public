from sympy import Matrix, Rational, cos, diff, simplify, symbols

# Exact calibration: a bi-affine S^2 x S^2 model can have a Schur-singular
# isolated global maximum.  On the great-circle kernel path this reduces to
# phi(s,t)=cos(s)+cos(t)-1/2 cos(s-t).
s, t, r = symbols('s t r', real=True)
phi = cos(s) + cos(t) - Rational(1, 2) * cos(s - t)
H = Matrix([[diff(phi, u, v).subs({s:0,t:0}) for v in (s,t)] for u in (s,t)])
z = Matrix([1,-1])
path = simplify(phi.subs({s:r,t:-r}))
path4 = simplify(diff(path,r,4).subs(r,0))
assert H == Matrix([[-Rational(1,2),-Rational(1,2)],[-Rational(1,2),-Rational(1,2)]])
assert H*z == Matrix([0,0])
assert path == 2*cos(r)-Rational(1,2)*cos(2*r)
assert path4 == -6

# Exact pair-Hessian Schur-boundary algebra.  Write a=r0^2, b=s0^2 and
# singular values s1=2 r0 s0, s2=k.  In SVD coordinates A=-H_pair.
r0, s0, k = symbols('r0 s0 k', positive=True, real=True)
A = Matrix([
    [2*r0**2, 0, -2*r0*s0, 0],
    [0, 2*r0**2, 0, -k],
    [-2*r0*s0, 0, 2*s0**2, 0],
    [0, -k, 0, 2*s0**2],
])
zk = Matrix([s0,0,r0,0])
w = Matrix([r0,0,-s0,0])
assert simplify(A*zk) == Matrix([0,0,0,0])
assert simplify(A*w - 2*(r0**2+s0**2)*w) == Matrix([0,0,0,0])

# Lyapunov-Schmidt t^4 coefficient in the simplest one-kernel polynomial
# model F(x,y)=-lambda*y^2/2 + c*x^2*y/2 + q*x^4/24.
lam, c, q, d = symbols('lam c q d', positive=True, real=True)
coeff = -Rational(1,2)*lam*d**2 + Rational(1,2)*c*d + q/Rational(24)
dstar = c/(2*lam)
coeffstar = simplify(coeff.subs(d,dstar))
assert coeffstar == c**2/(8*lam) + q/Rational(24)

print('PASS exact symbolic checks')
print('torus_hessian=', H.tolist())
print('torus_kernel=', list(z), 'fourth_derivative=', path4)
print('schur_kernel_verified=', simplify(A*zk) == Matrix([0,0,0,0]))
print('schur_positive_mode_eigenvalue=', 2*(r0**2+s0**2))
print('optimized_t4_coefficient=', coeffstar)
print('necessary_scalar_gate: q + 3*c^2/lam <= 0')
