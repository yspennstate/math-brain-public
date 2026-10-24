#!/usr/bin/env python3
"""I0067 exact algebra self-check for second stuck-recovery shear geometry.

This does NOT prove Agresti--Veraar Problem 10. It verifies only the
finite symbolic identities used to isolate the moving-Hodge endpoint module.
"""
import sympy as sp

q = sp.symbols("q", real=True)
F = sp.Matrix([[1,q,0],[0,1,0],[0,0,1]])
Finv = F.inv()
A = sp.simplify(Finv*Finv.T)
assert sp.factor(F.det()) == 1
assert Finv == sp.Matrix([[1,-q,0],[0,1,0],[0,0,1]])
assert A == sp.Matrix([[1+q**2,-q,0],[-q,1,0],[0,0,1]])
assert sp.factor(A.det()) == 1
cp = A.charpoly()
z = cp.gen
assert sp.simplify(cp.as_expr() - (z-1)*(z**2-(2+q**2)*z+1)) == 0

x1,x2,x3,sigma = sp.symbols("x1 x2 x3 sigma")
a = sp.Function("a")(x2)
u1 = sp.Function("u1")(x1,x2,x3)
u2 = sp.Function("u2")(x1,x2,x3)
u3 = sp.Function("u3")(x1,x2,x3)
xs = (x1,x2,x3)
us = (u1,u2,u3)
f = [sigma*a*sp.diff(ui,x1) for ui in us]
divf = sum(sp.diff(f[i],xs[i]) for i in range(3))
divu = sum(sp.diff(us[i],xs[i]) for i in range(3))
remainder = sp.simplify(divf - sigma*a*sp.diff(divu,x1))
assert sp.simplify(remainder - sigma*sp.diff(a,x2)*sp.diff(u2,x1)) == 0

phi = sp.Function("phi")(x1,x2,x3)
qf = sp.Function("q")(x2)
Af = sp.Matrix([[1+qf**2,-qf,0],[-qf,1,0],[0,0,1]])
grad = sp.Matrix([sp.diff(phi,x1),sp.diff(phi,x2),sp.diff(phi,x3)])
flux = Af*grad
divAgrad = sum(sp.diff(flux[i],xs[i]) for i in range(3))
Dphi = sp.diff(phi,x2)-qf*sp.diff(phi,x1)
square_form = sp.diff(phi,x1,2) + (sp.diff(Dphi,x2)-qf*sp.diff(Dphi,x1)) + sp.diff(phi,x3,2)
assert sp.simplify(divAgrad-square_form) == 0

print("status=PASS")
print("det_F=1")
print("F_inverse=[[1,-q,0],[0,1,0],[0,0,1]]")
print("A=F_inverse*F_inverse^T=[[1+q^2,-q,0],[-q,1,0],[0,0,1]]")
print("det_A=1")
print("A_2x2_characteristic=lambda^2-(2+q^2)lambda+1")
print("shear_divergence_identity=div(b*d1u)-b*d1(div u)=sigma*a_prime*d1u2")
print("scalar_metric_identity=div(A grad phi)=d1^2 phi+(d2-q d1)^2 phi+d3^2 phi")
print("source_endpoint_certified=False")
