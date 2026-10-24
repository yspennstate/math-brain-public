#!/usr/bin/env python3
"""Exact symbolic self-check for R08/F0083 quartic screening coefficients.

Checks only the finite algebraic core of the accompanying analytic proof:
(1) one-layer gain G(a,b) in the transversely symmetric two-layer tangent;
(2) critical-corner loss a^4/24;
(3) the exact two-neighbor amplification root rho_layer;
(4) the face-neighbor-only gain upper bound at one 4D Voronoi corner;
(5) the exact universal small-deficit screening root rho_face.

It does NOT certify the asymptotic localization argument or F0083 itself.
"""
import sympy as sp

U,t,A,N,a,b,r=sp.symbols('U t A N a b r', positive=True)

# A sum U of 3 nonnegative transverse coordinates has slice density U^2/2.
G=sp.integrate(sp.integrate(U**2/sp.Integer(2),(U,a+t,b-t)),(t,0,(b-a)/2))
G_closed=(b-a)**2*(7*b**2+10*a*b+7*a**2)/sp.Integer(192)
assert sp.simplify(G-G_closed)==0

# Baseline critical-corner loss for threshold a.
loss=sp.integrate(sp.integrate(U**2/sp.Integer(2),(U,0,a-t)),(t,0,a))
assert sp.simplify(loss-a**4/sp.Integer(24))==0
assert sp.simplify(16*loss-sp.Rational(2,3)*a**4)==0

# Layered quartic recurrence: G(a,b_-)+G(a,b_+)=a^4/12.
Gr=sp.factor(G_closed.subs(b,r*a)/a**4)
assert Gr==(r-1)**2*(7*r**2+10*r+7)/sp.Integer(192)
P_layer=sp.expand((r-1)**2*(7*r**2+10*r+7)-8)
assert P_layer==7*r**4-4*r**3-6*r**2-4*r-1
assert sp.factor(sp.diff(Gr,r))==(r-1)*(7*r**2+4*r+1)/sp.Integer(48)
lo_layer=sp.Rational(1466,1000); hi_layer=sp.Rational(1467,1000)
assert P_layer.subs(r,lo_layer)<0<P_layer.subs(r,hi_layer)

# Universal face-neighbor-only upper gain at one corner.
# k coordinates have crossed their Voronoi faces. For fixed center score A,
# each crossed coordinate p_i must satisfy p_i < (b-A)/2 if its face neighbor
# has threshold at most b. Remaining 4-k negative coordinates sum to N=A+P.
face_terms=[]
for k in (1,2,3):
    q=4-k
    ps=sp.symbols('p0:'+str(k), nonnegative=True)
    Psum=sum(ps)
    expr=(A+Psum)**(q-1)/sp.factorial(q-1)
    upper=(b-A)/2
    for p in ps:
        expr=sp.integrate(expr,(p,0,upper))
    expr=sp.integrate(expr,(A,a,b))
    face_terms.append((k,sp.factor(expr)))

expected={
  1:(b-a)**2*(7*b**2+10*a*b+7*a**2)/sp.Integer(192),
  2:(b-a)**3*(5*b+3*a)/sp.Integer(96),
  3:(b-a)**4/sp.Integer(32),
}
for k,expr in face_terms:
    assert sp.simplify(expr-expected[k])==0

Uface=sp.factor(sum(sp.binomial(4,k)*expr for k,expr in face_terms))
Uface_closed=(b-a)**2*(7*b**2-2*a*b+a**2)/sp.Integer(12)
assert sp.simplify(Uface-Uface_closed)==0

# Equality Uface(a,r a)=a^4/24 defines the sharp limiting amplification
# threshold for this face-neighbor-only upper bound.
P_face=sp.expand(2*(r-1)**2*(7*r**2-2*r+1)-1)
assert P_face==14*r**4-32*r**3+24*r**2-8*r+1
lo_face=sp.Rational(1233,1000); hi_face=sp.Rational(1234,1000)
assert P_face.subs(r,lo_face)<0<P_face.subs(r,hi_face)

roots_layer=sp.nroots(P_layer,n=40,maxsteps=100)
rho_layer=[sp.re(x) for x in roots_layer if abs(complex(x).imag)<1e-30 and float(sp.re(x))>1]
assert len(rho_layer)==1
roots_face=sp.nroots(P_face,n=40,maxsteps=100)
rho_face=[sp.re(x) for x in roots_face if abs(complex(x).imag)<1e-30 and float(sp.re(x))>1]
assert len(rho_face)==1

print('PASS exact symbolic checks')
print('corner_loss =', sp.factor(loss))
print('layer_gain_G(a,b) =', sp.factor(G))
print('layer_rho_polynomial =', P_layer)
print('layer_rho_bracket = (1466/1000, 1467/1000)')
print('rho_layer ~=', sp.N(rho_layer[0],18))
for k,expr in face_terms:
    print(f'face_gain_k={k} =', sp.factor(expr))
print('face_gain_total =', sp.factor(Uface))
print('face_rho_polynomial =', P_face)
print('face_rho_bracket = (1233/1000, 1234/1000)')
print('rho_face ~=', sp.N(rho_face[0],18))
