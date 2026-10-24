from fractions import Fraction
from itertools import combinations
from math import e, exp, log, sqrt


def ek(vals,k):
    out=Fraction(0)
    for C in combinations(vals,k):
        p=Fraction(1)
        for v in C: p*=v
        out+=p
    return out

x=[Fraction(256),Fraction(1),Fraction(1),Fraction(1),Fraction(1,256)]
E3,E4,E5=ek(x,3),ek(x,4),ek(x,5)
Win=x[0]*ek(x[1:],2)
Wout=ek(x[1:],3)
q0=Win/E3
assert E3==Fraction(197635,256)
assert E4==Fraction(66305,256)
assert E5==1
assert Win==771 and Wout==Fraction(259,256)
assert q0==Fraction(197376,197635)

alpha_s=Fraction(1,4)*(Fraction(171,257)+Fraction(258,259))
alpha_w=Fraction(1,4)*(Fraction(1,257)+Fraction(3,259))
assert alpha_s<Fraction(1,2) and alpha_w<Fraction(1,2)
assert Fraction(1,2)+6*alpha_s+2*alpha_w==3

G=sqrt(199689)/8
B_D=6*sqrt(e)*G**(-1/6)
d0=3+log(259/197376)/6
assert d0>0
B_D5=5*sqrt(2*e)

# Explicit ridge scale g=1/4096.
g=Fraction(1,4096)
k0=Fraction(256)/(Fraction(256)+g)
k=Fraction(1)/(Fraction(1)+g)
kw=Fraction(1,256)/(Fraction(1,256)+g)
q=2*k0
theta=k0+3*k+kw
gap=theta-2*q
D=(1+Fraction(256)/g)*(1+Fraction(1)/g)**3*(1+Fraction(1,256)/g)
assert k0==Fraction(1048576,1048577)
assert k==Fraction(4096,4097)
assert kw==Fraction(16,17)
assert Fraction(1)<=q<=2 and gap>0
B_r=e/(sqrt(2*float(q))*sqrt(float(g)))*float(theta/gap)*float(D)**(-1/(2*float(theta)))

# Independently reconstruct partner projected residual E3 currency.
dirs=[0,0,1,1,2,2,3,3]
norm2=[0.5]*6+[1/512]*2
trip=[]
for S in combinations(range(8),3):
    if len({dirs[i] for i in S})<3: continue
    z=1.0
    for i in S: z*=norm2[i]
    trip.append((S,z))
Z=sum(z for S,z in trip)
mu=[z/Z for S,z in trip]
beta=[sum(p for ((S,z),p) in zip(trip,mu) if i in S) for i in range(8)]
Gamma=exp(sum(p*log(z) for ((S,z),p) in zip(trip,mu))-sum(b*log(b) for b in beta))
Omega=256*Gamma
B_hub=2**(9/4)*Omega**(-1/8)
assert abs(Z-259/256)<1e-14
assert max(beta)<0.5
assert abs(B_hub-2.378720371807186)<1e-12

print('QFORM_B04_R17_CARRIER_BALANCE_CHECK_PASS')
print('E3=',E3,'E4=',E4,'E5=',E5)
print('Win=',Win,'Wout=',Wout,'q0=',float(q0))
print('alpha_strong=',float(alpha_s),'alpha_weak=',float(alpha_w))
print('Gstar=',G,'D_bound=',B_D,'Dprime_endpoint_derivative=',d0)
print('ridge_theta=',float(theta),'ridge_gap=',float(gap),'ridge_bound=',B_r)
print('D5_bound=',B_D5)
print('partner_Gamma=',Gamma,'partner_Omega=',Omega,'partner_bound=',B_hub)
