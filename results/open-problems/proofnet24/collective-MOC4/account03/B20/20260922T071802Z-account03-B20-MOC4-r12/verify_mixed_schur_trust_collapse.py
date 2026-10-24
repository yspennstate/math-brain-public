import sympy as sp

a,b,rho,r2,s2,m,z = sp.symbols("a b rho r2 s2 m z", real=True, nonzero=True)
A=a**2
B=b**2
t=a*b
r1=b*rho
s1=-a*rho
H=A+B-2*z

# Mixed-Schur singular basis: M=diag(sqrt(AB),m).
Z=sp.Matrix([[t,0,r1],
             [0,m,r2],
             [s1,s2,z]])
p=sp.Matrix([-r1,-r2,A-z])
q=sp.Matrix([-s1,-s2,B-z])
L=A+B-z

Q0=sp.expand(p*p.T-Z*Z.T)
b0=sp.expand(-(L*p+Z*q))
c0=sp.expand(L**2-q.dot(q))
lam=-A*B

T=sp.Matrix.vstack(
    sp.Matrix.hstack(Q0-lam*sp.eye(3), b0),
    sp.Matrix.hstack(b0.T, sp.Matrix([[c0+lam]]))
)
T=sp.simplify(T)

D=A*B-m**2
E=A*r2+m*s2
C=A*(H-rho**2)-s2**2
expected=sp.Matrix([
    [0,0,0,0],
    [0,D,-E,E],
    [0,-E,C,-C],
    [0,E,-C,C],
])
assert all(sp.simplify(T[i,j]-expected[i,j])==0 for i in range(4) for j in range(4))

# The residual 3x3 quadratic is D*w^2 - 2E*w*(e-t) + C*(e-t)^2.
# Hence PSD is equivalent to [[D,-E],[-E,C]] >= 0.
det2=sp.expand(D*C-E**2)
ls_numer=sp.expand(
    A*D*(H-rho**2)
    - A*(A*r2**2+2*m*r2*s2+B*s2**2)
)
assert sp.simplify(det2-ls_numer)==0

# Exact great-circle factorization before imposing the cubic relation.
theta=sp.symbols("theta", real=True)
ru,su=sp.symbols("ru su", real=True)
x=1-sp.cos(theta)
y=sp.sin(theta)
Craw=A*H-(su**2+s2**2)
Draw=A*ru+t*su
phi_factored=sp.expand(Craw*x**2+2*Draw*x*y)

# Reconstruct the squared trust gap directly on n=(sin theta,0,cos theta)
Zraw=sp.Matrix([[t,0,ru],[0,m,r2],[su,s2,z]])
praw=sp.Matrix([-ru,-r2,A-z])
qraw=sp.Matrix([-su,-s2,B-z])
n=sp.Matrix([sp.sin(theta),0,sp.cos(theta)])
gap=sp.expand((L-(praw.dot(n)))**2 - (qraw+Zraw.T*n).dot(qraw+Zraw.T*n))
assert sp.trigsimp(gap-phi_factored)==0

# Double-singular case m=eps*sqrt(AB): D=0 forces E=0 and C>=0.
eps=sp.symbols("eps", real=True)
rho2=sp.symbols("rho2", real=True)
E_double=sp.expand(E.subs({m:eps*t,r2:b*rho2,s2:-eps*a*rho2}))
C_double=sp.expand(C.subs({r2:b*rho2,s2:-eps*a*rho2}))
for sign in (1,-1):
    assert sp.simplify(E_double.subs(eps,sign))==0
    assert sp.simplify(C_double.subs(eps,sign)-A*(H-rho**2-rho2**2))==0

print("PASS MOC4-MIXED-SCHUR-TRUST-COLLAPSE-v1")
print("trust_multiplier = -A*B")
print("residual_psd = [[A*B-m^2, -(A*r2+m*s2)], [-(A*r2+m*s2), A*(H-rho^2)-s2^2]]")
print("simple_boundary_equiv = H >= rho^2 + (A*r2^2+2*m*r2*s2+B*s2^2)/(A*B-m^2)")
print("great_circle_cubic = A*r1 + sqrt(A*B)*s1 = 0")
print("double_boundary_equiv = second cubic relation plus H >= rho1^2+rho2^2")
