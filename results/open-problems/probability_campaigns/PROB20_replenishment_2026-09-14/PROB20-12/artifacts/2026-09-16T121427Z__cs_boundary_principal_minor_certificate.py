import sympy as sp

# PROB20-12 exact symbolic checker, 2026-09-16T121427Z.
# Verifies the principal-minor factorizations used for the two
# CS boundary cases of the 540-facet strong operator inequality.

a,b,s,t,p0,p1,p2=sp.symbols('a b s t p0 p1 p2', real=True)
G=sp.groebner([
    s**2+a**2-1,
    t**2+b**2-1,
    p0**2+p1**2+p2**2-1,
],s,t,p0,p1,p2,a,b,order='grevlex')

def red(expr):
    return sp.expand(G.reduce(sp.expand(expr))[1])

x=a**2; y=b**2; u=p1**2; v=p2**2
d=(1-x)*(1-y)

# Case b in K cap B (P_H0 b=0).
Mb=sp.Matrix([
    [x*y-y*v+s**2*(1-p0**2), a*b*p1*p2, b*p0*p2*(s**2-1)],
    [a*b*p1*p2, x*y-x*u+t**2*(1-p0**2), a*p0*p1*(1-t**2)],
    [b*p0*p2*(s**2-1), a*p0*p1*(1-t**2),
     x*y+x*t**2*(1-u)+y*s**2*(1-v)-p0**2+s**2*t**2],
])
L=x*y+(1-x)*u+(1-y)*v
M=x*y-(x+y-1)*(u+v)
J1=(1-x+x*y)*u+d*v
J2=d*u+(1-y+x*y)*v
checks=[
    (Mb.extract([0,1],[0,1]).det(),L*M),
    (Mb.extract([0,2],[0,2]).det(),L*J1),
    (Mb.extract([1,2],[1,2]).det(),L*J2),
    (Mb.det(),d*(u+v)*L**2),
]
for lhs,rhs in checks:
    assert red(lhs-rhs)==0

# Case a in K cap A (P_H0 a=0); reuse p variables for q coordinates.
Ma=sp.Matrix([
    [x*y+x*(1-p0**2)-x-y-v*t**2+1, p1*p2*s*t, p0*p2*t*(x-1)],
    [p1*p2*s*t, x*y-x+y*(1-p0**2)-y-u*s**2+1, p0*p1*s*(1-y)],
    [p0*p2*t*(x-1), p0*p1*s*(1-y),
     x*y+x*t**2*(1-v)+y*s**2*(1-u)-p0**2+s**2*t**2],
])
L2=d+x*u+y*v
M2=d+(x+y-1)*(u+v)
K1=(1-y+x*y)*u+x*y*v
K2=x*y*u+(1-x+x*y)*v
checks2=[
    (Ma.extract([0,1],[0,1]).det(),L2*M2),
    (Ma.extract([0,2],[0,2]).det(),L2*K1),
    (Ma.extract([1,2],[1,2]).det(),L2*K2),
    (Ma.det(),x*y*(u+v)*L2**2),
]
for lhs,rhs in checks2:
    assert red(lhs-rhs)==0

print('case_b_principal_minors_factored=True')
print('case_a_principal_minors_factored=True')
print('ALL EXACT CHECKS PASSED')
