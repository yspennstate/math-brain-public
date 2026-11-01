from fractions import Fraction
import math
import numpy as np


def constants(r):
    alpha=(r-1.0)/r
    theta=r/(2.0*r-1.0)
    eta=alpha*theta
    A=(1.0+alpha)/(math.pi*alpha)
    B=(alpha*math.pi/2.0)*(2.0/(r-1.0))**(1.0/r)*(2.0*math.pi)**alpha
    C_one=A*B**theta/(1.0-eta)
    C_det=2.0**(theta/2.0)*C_one
    return alpha,theta,eta,C_one,C_det

print('identity eta=(r-1)/(2r-1)')
for r in [2.0,1.5,4.0/3.0,1.2,1.05]:
    a,t,e,co,cd=constants(r)
    rhs=(r-1.0)/(2.0*r-1.0)
    print(r, e, rhs, abs(e-rhs))
    assert abs(e-rhs)<1e-14
    assert 0.0<e<1.0

print('r=2 exact determinant constant')
exact=9.0/(2.0*2.0**(1.0/3.0))
num=constants(2.0)[4]
print(exact,num,abs(exact-num))
assert abs(exact-num)<1e-13

print('q-scale cancellation and constants')
for q in [2,3,4,5,10]:
    r=q/(q-1.0)
    _,theta,eta,_,Cdet=constants(r)
    kexp=-r/(2.0*r-1.0)+q*(r-1.0)/(2.0*r-1.0)
    print(q,r,kexp,Cdet)
    assert abs(kexp)<1e-13

print('full A scaling exponent')
for r in [2.0,1.5,4.0/3.0,1.2]:
    total=4.0*r/(4.0*(2.0*r-1.0))+(r-1.0)/(2.0*r-1.0)
    print(r,total)
    assert abs(total-1.0)<1e-13

print('stress matrix spectrum and target count')
A=np.array([
[0,0,1,0,1,0],
[0,0,0,1,0,0],
[1,0,1,0,0,0],
[0,1,0,0,0,0],
[1,0,0,0,0,1],
[0,0,0,0,1,0]],dtype=float)
w=np.linalg.eigvalsh(A)
print(w)
count=int(np.sum(np.abs(w)>=1.0-1e-12))
print('count |lambda|>=1:',count)
assert count>=3

# exact characteristic polynomial coefficients for
# (x-1)^2 (x+1) (x^3-3x-1)
p1=np.poly1d([1,-1])**2
p2=np.poly1d([1,1])
p3=np.poly1d([1,0,-3,-1])
expected=np.polymul(np.polymul(p1,p2),p3)
actual=np.poly(A)
print('charpoly expected:',expected.coeffs)
print('charpoly numeric :',actual)
assert np.max(np.abs(expected.coeffs-actual))<1e-10

print('fractional-pole constants')
for eta in [1/3,1/4,1/5,0.9]:
    centered=2.0*((0.5)**(1.0-eta))/(1.0-eta)
    formula=2.0**eta/(1.0-eta)
    scaled=(2.0**(-eta))*formula
    print(eta,centered,formula,scaled,1.0/(1.0-eta))
    assert abs(centered-formula)<1e-13
    assert abs(scaled-1.0/(1.0-eta))<1e-13

print('STATUS=PASS')
