from fractions import Fraction as Q
from math import comb
D=248; P=Q(19,50); PMIN=Q(3,8); L0=Q(1661,2500); L=Q(2,3); U=Q(69567,100000)
QLOW=Q(49163,100000)

def bmin(n,l): return Q(n)*(1-l)/(Q(n)-Q(n-1)*l)
def chord(n,l):
    c=1-l; lo=bmin(n,l); hi=Q(n)/(Q(n)+l); s=(hi-lo)/l
    return lo-s*c,s

def high_lower(D,p,l):
    a1,s1=chord(1,l); aD,sD=chord(D,l)
    mu=((1-p)*a1+p*aD)/(1-((1-p)*s1+p*sD))
    return aD+sD*mu

UD=Q(D)*U/(L0+Q(D)*U)
A=P*UD/(L0+UD)
# Scalar refinement F(x)=(1-P)x/(L0+x)+A has fixed-point polynomial
# G(x)=x^2+[L0-A-(1-P)]x-A L0.  It has one positive and one negative root.
b=L0-A-(1-P); c=-A*L0
def G(x): return x*x+b*x+c
assert c<0 and QLOW>0 and G(QLOW)<0   # hence QLOW is strictly below positive root x_*

M=high_lower(D,PMIN,L)
pref=Q(D)*M*(M-(1-L0))/L0
s=Q(0)
for k in range(D+1):
    pr=Q(comb(D,k))*P**k*(1-P)**(D-k)
    den=M+Q(D-k)*QLOW+Q(k)*UD-(1-L)
    s += pr/(den*den)
J_optimistic=pref*s

t=(1+L)/(Q(D)+L)
th=P*t/(1-P+P*t)
C=L/(1-L)-P*L*J_optimistic
delta=1+Q(D-1)*th-Q(D-1)*C*th*(1-th)
margin=2*delta/(1+Q(D-1)*th+L)**2
assert delta<0
print('ALL_EXACT_CHECKS_PASS')
print('G(QLOW)=',float(G(QLOW)))
print('QLOW=',float(QLOW),'is below scalar-refinement fixed point')
print('optimistic_J=',float(J_optimistic))
print('optimistic_delta=',float(delta))
print('optimistic_margin=',float(margin))
