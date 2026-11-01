#!/usr/bin/env python3
import sympy as sp

z,t,a,b,x,u,v,s=sp.symbols('z t a b x u v s')

# Explicit quartic source-admissible k=1 witness.
V = sp.Rational(2,5)*x**4 - sp.Rational(16,15)*x**3 + sp.Rational(2,5)*x**2 + sp.Rational(8,5)*x
Vp = sp.diff(V,x)

# One-cut resolvent data: h(z)=(8/5)(z-1)^2 and R(z)=sqrt(z^2-1)~z.
h = sp.Rational(8,5)*(z-1)**2
ht = sp.Rational(8,5)*(1/t-1)**2 * (1/t)*sp.sqrt(1-t**2)
ht_ser = sp.series(ht, t, 0, 6).removeO().expand()
poly_part = sum(term for term in sp.Add.make_args(ht_ser) if term.as_powers_dict().get(t,0) <= 0)
poly_part_z = sp.expand(poly_part.subs(t,1/z))
assert sp.simplify(poly_part_z - Vp.subs(x,z)) == 0
G_t = sp.series(Vp.subs(x,1/t) - ht, t, 0, 5)
assert sp.expand(G_t.removeO()).coeff(t,1) == 1
assert all(sp.expand(G_t.removeO()).coeff(t,j)==0 for j in [0,-1,-2,-3])
# rho=(8/(5*pi))(1-x)^2 sqrt(1-x^2) on [-1,1] is normalized:
# int sqrt(1-x^2)=pi/2, int x sqrt(...)=0, int x^2 sqrt(...)=pi/8.
assert sp.simplify(sp.Rational(8,5)*(sp.Rational(1,2)+sp.Rational(1,8)) - 1) == 0

# KRV local Hamiltonian W(a,b)=[1]V(a+b(z+z^{-1})).
y=sp.symbols('y')
Vy=sp.expand(V.subs(x,a+b*y))
ct_moment={0:1,1:0,2:2,3:0,4:6}
W=sp.expand(sum(Vy.coeff(y,j)*ct_moment[j] for j in range(5)))
W_expected=sp.Rational(2,15)*(3*a**4-8*a**3+36*a**2*b**2+3*a**2-48*a*b**2+12*a+18*b**4+6*b**2)
assert sp.expand(W-W_expected)==0

F = W - (1-s)*sp.log(b)
Fa=sp.diff(F,a)
Fb=sp.diff(F,b)

# Break symmetry deliberately by endpoint variables R=a+2b=1-u, L=a-2b=-1+v.
asub=(v-u)/2
bsub=(2-u-v)/4
Pnum=sp.factor(sp.together(Fa.subs({a:asub,b:bsub})).as_numer_denom()[0])
Qnum=sp.factor(sp.together(Fb.subs({a:asub,b:bsub})).as_numer_denom()[0])
P_expected=-5*u**3+3*u**2*v-3*u*v**2+8*u*v+5*v**3-24*v**2+32*v
Q_expected=-80*s-15*u**4-12*u**3*v+40*u**3+6*u**2*v**2-8*u**2*v-12*u*v**3+56*u*v**2-64*u*v-15*v**4+104*v**3-256*v**2+256*v
assert sp.expand(Pnum-P_expected)==0
assert sp.expand(Qnum+Q_expected)==0  # overall numerator sign is immaterial

# Exact Puiseux branch represented parametrically by u. Solve P=0 formally for v(u).
c3,c4,c5,c6,c7=sp.symbols('c3 c4 c5 c6 c7')
vans=c3*u**3+c4*u**4+c5*u**5+c6*u**6+c7*u**7
pser=sp.series(P_expected.subs(v,vans),u,0,9).removeO().expand()
sol={}
for power,c in [(3,c3),(4,c4),(5,c5),(6,c6),(7,c7)]:
    eq=sp.expand(pser.subs(sol)).coeff(u,power)
    sol[c]=sp.solve(sp.Eq(eq,0),c)[0]
vser=sp.expand(vans.subs(sol))
expected_v=sp.Rational(5,32)*u**3-sp.Rational(5,128)*u**4-sp.Rational(5,1024)*u**5+sp.Rational(95,4096)*u**6-sp.Rational(25,2048)*u**7
assert sp.expand(vser-expected_v)==0

sexact=sp.solve(sp.Eq(Q_expected,0),s)[0]
sser=sp.series(sexact.subs(v,vser),u,0,8).removeO().expand()
expected_s=u**3-sp.Rational(7,16)*u**4-sp.Rational(5,256)*u**6+sp.Rational(5,1024)*u**7
assert sp.expand(sser-expected_s)==0

# Hessian at the local critical point and soft mode.
H=sp.hessian(F,(a,b))
H0=sp.simplify(H.subs({a:0,b:sp.Rational(1,2),s:0}))
H0_expected=sp.Matrix([[sp.Rational(16,5),-sp.Rational(32,5)],[-sp.Rational(32,5),sp.Rational(64,5)]])
assert H0==H0_expected
assert H0*sp.Matrix([2,1])==sp.zeros(2,1)

Hbranch=H.subs({a:asub,b:bsub,v:vser,s:sser})
det_ser=sp.series(sp.det(Hbranch),u,0,6).removeO().expand()
tr_ser=sp.series(sp.trace(Hbranch),u,0,5).removeO().expand()
assert det_ser == sp.Rational(384,5)*u**2+sp.Rational(64,5)*u**3+sp.Rational(12,5)*u**4-18*u**5
assert tr_ser == 16+4*u+9*u**2-sp.Rational(35,8)*u**3+sp.Rational(5,32)*u**4
lam_small=(sp.trace(Hbranch)-sp.sqrt(sp.trace(Hbranch)**2-4*sp.det(Hbranch)))/2
lam_ser=sp.series(lam_small,u,0,5).removeO().expand()
assert lam_ser == sp.Rational(24,5)*u**2-sp.Rational(2,5)*u**3-sp.Rational(101,100)*u**4

# KRV Proposition 7: for edge direction q=(1,2), q^T Sigma q = -4 b E'(s).
# Here E=1-u and s=s(u), so this is 4 b/(ds/du).
bbranch=sp.expand(bsub.subs(v,vser))
qSigmaq=4*bbranch/sp.diff(sser,u)
qs_ser=sp.series(qSigmaq,u,0,2)
qs_expected=sp.Rational(2,3)/u**2+sp.Rational(1,18)/u+sp.Rational(7,216)-sp.Rational(37,5184)*u
assert sp.expand(qs_ser.removeO()-qs_expected)==0

# General exotic no-go for retaining regular uniform covariance estimate Var block <= C ell/n.
k=sp.symbols('k', integer=True, positive=True)
collapse_exp=sp.simplify(sp.Rational(3,1)/(4*k+3)-1)
assert collapse_exp == -4*k/(4*k+3)

print('V_star =', V)
print('density = (8/(5*pi))*(1-x)^2*sqrt(1-x^2), normalized = True')
print('W =', W)
print('P_endpoint =', P_expected)
print('Q_endpoint =', Q_expected)
print('v(u) =', vser)
print('s(u) =', sser, '+ O(u^8)')
print('H(0) =', H0.tolist())
print('det H =', det_ser, '+ O(u^6)')
print('tr H =', tr_ser, '+ O(u^5)')
print('lambda_min H =', lam_ser, '+ O(u^5)')
print('edge covariance q^T Sigma q =', qs_ser)
print('uniform-covariance scaled variance exponent =', collapse_exp, '< 0 for every k>=1')
print('ALL_EXACT_CHECKS_PASS True')
