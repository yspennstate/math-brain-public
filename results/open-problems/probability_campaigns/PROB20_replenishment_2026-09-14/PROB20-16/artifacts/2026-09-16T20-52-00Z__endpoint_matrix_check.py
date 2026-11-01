#!/usr/bin/env python3
"""
PROB20-16 exact symbolic self-check for the endpoint matrix inequality
on ordered two-site rank-one pairs.

All assertions are symbolic algebraic identities. Positivity/sign statements
used in the proof are stated separately in the report from strict atom
positivity and monotonicity of logarithm.
"""
import sympy as sp

x,y,s=sp.symbols("x y s", positive=True)
p00=(1-x)*(1-y)-s
p10=x*(1-y)+s
p01=(1-x)*y+s
p11=x*y-s
P=sp.expand(p00*p10*p01*p11)

A=sp.log(p00/p01)
B=sp.log(p10/p11)
E=sp.log(p10/p01)
L=sp.log(p10*p01/(p00*p11))
H=-(p00*sp.log(p00)+p10*sp.log(p10)+p01*sp.log(p01)+p11*sp.log(p11))
Hx=sp.diff(H,x)
Hy=sp.diff(H,y)

def z(expr):
    return sp.factor(sp.together(sp.expand_log(expr, force=True)))

assert z(Hy-((1-x)*A+x*B)) == 0
assert z(L-(B-A)) == 0
assert z(sp.diff(A,x)+s/(p00*p01)) == 0
assert z(sp.diff(B,x)+s/(p10*p11)) == 0
assert z(sp.diff(E,x)-((1-y)/p10+y/p01)) == 0

# Re-express H_x through A,B,E.
assert z(Hx-((1-y)*A+y*B-E)) == 0

# Previously found pointwise differential identity and its stronger 2x2 form.
Hxx=sp.diff(H,x,2)
Hxy=sp.diff(Hy,x)
gap=s*(x*y*(1-x)*(1-y)-s**2)/P
assert z(L-Hxy-gap) == 0
Hxx_manual=-(1-y)**2*(1/p00+1/p10)-y**2*(1/p01+1/p11)
assert z(Hxx-Hxx_manual) == 0
Lx_manual=-s*(y*(1-y)*(1-2*x)+s*(1-2*y))/P
assert z(sp.diff(L,x)-Lx_manual) == 0
# det( L e22 - d/dx grad H ) = s*y*(1-y)/P
assert z(Hxx_manual*(Hxy-L)-s*Lx_manual**2-s*y*(1-y)/P) == 0

# Endpoint secant identities. x1<x0; define positive decrements
# u=A(x1)-A(x0), v=B(x1)-B(x0).
x0,x1,u,v=sp.symbols("x0 x1 u v", real=True)
A0,A1,B0,B1=sp.symbols("A0 A1 B0 B1", real=True)
rho=x0-x1
F0=(1-x0)*A0+x0*B0
F1=(1-x1)*A1+x1*B1
L0=B0-A0
L1=B1-A1
# Substitute A0-A1=-u, B0-B1=-v after simplifying.
expr0=sp.expand(F0-F1-rho*L0).subs({A0:A1-u,B0:B1-v})
expr1=sp.expand(F0-F1-rho*L1).subs({A0:A1-u,B0:B1-v})
assert sp.expand(expr0 + (1-x1)*u+x1*v) == 0
assert sp.expand(expr1 + (1-x0)*u+x0*v) == 0

# Determinant lower-bound identity at either endpoint x=xi:
# [(1-y)u+yv][(1-xi)u+xiv]-s(u-v)^2
# = p00(xi)u^2 +(p10(xi)+p01(xi))uv+p11(xi)v^2.
xi=sp.symbols("xi", real=True)
p00i=(1-xi)*(1-y)-s
p10i=xi*(1-y)+s
p01i=(1-xi)*y+s
p11i=xi*y-s
lhs=((1-y)*u+y*v)*((1-xi)*u+xi*v)-s*(u-v)**2
rhs=p00i*u**2+(p10i+p01i)*u*v+p11i*v**2
assert sp.expand(lhs-rhs) == 0

print("status=PASS")
print("Hy_decomposition=PASS")
print("A_B_monotonic_derivatives=PASS")
print("E_increasing_derivative=PASS")
print("Hx_decomposition=PASS")
print("pointwise_L_minus_Hxy_identity=PASS")
print("local_matrix_determinant_identity=PASS")
print("two_endpoint_secant_identities=PASS")
print("endpoint_determinant_atom_sum_identity=PASS")
print("NOTE=self-check only; theorem proof also uses strict physical atom positivity.")
