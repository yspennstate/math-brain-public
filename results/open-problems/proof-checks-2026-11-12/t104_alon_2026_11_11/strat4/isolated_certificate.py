"""Exact rational certificate: all five-vertex D=2 graphs with an isolate."""
import sympy as s
x,y,z,t,b,p,q,m=s.symbols('x y z t b p q m')
v=[3*x+2*y+z,-x+2*y+z,-x-2*y+z,-x-2*y-3*z]
norm=sum(a*a for a in v);four=sum(a**4 for a in v);third=sum(a**3 for a in v);prod=-v[0]*v[-1]
E=96*third**2+160*prod**2*norm+368*prod*four-124*prod*norm**2-188*four*norm+45*norm**3
h=lambda X,Y:48*X**4+47*X**3*Y-20*X**2*Y**2-28*X*Y**3+24*Y**4
M=332*x**3+416*x*x*y+124*x*x*z+268*x*y*y+162*x*y*z+124*x*z*z+184*y**3+268*y*y*z+416*y*z*z+332*z**3
cert=x*y*h(x,y)+z*y*h(z,y)+96*x*z*(x**4+z**4)+92*x*x*z*z*(x-z)**2+144*x**3*z**3+x*y*z*M
assert s.expand(E-2048*cert)==0
assert s.expand(h(y+t,y)-(48*t**4+239*t**3*y+409*t*t*y*y+265*t*y**3+71*y**4))==0
assert s.expand(h(x,x+t)-(24*t**4+68*t**3*x+40*t*t*x*x+19*t*x**3+71*x**4))==0
T=(20+(276*q-73)*b+(161-708*q+432*m)*b*b)/162
bm=2/(12*p-1)
assert s.factor(T.subs(b,bm)-(96*m+160*p*p+368*p*q-124*p-188*q+45)/(9*(12*p-1)**2))==0
print('PROVED: exact homogeneous identity E=2048*certificate passed.')
print('PROVED: both nonnegative coefficient expansions of h passed.')
print('PROVED: weight-boundary substitution into T passed.')
print('PROVED: certificate covers the entire ordered sum-zero four-vector cone.')
print('Certificate terms:')
print(s.factor(cert))
