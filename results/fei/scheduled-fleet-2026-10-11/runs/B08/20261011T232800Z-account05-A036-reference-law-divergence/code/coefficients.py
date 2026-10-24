from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[1],-x[0]
def scale(x,a):return (x[0]*a,x[1]*a) if a>=0 else (x[1]*a,x[0]*a)
def mul(x,y):
 p=[a*b for a in x for b in y];return min(p),max(p)
def inv(x):assert x[0]>0;return 1/x[1],1/x[0]
def powi(x,n):
 z=(F(1),F(1))
 for _ in range(n):z=mul(z,x)
 return z
def enc(x):
 g=10**14
 return {'lower':str(F((x[0]*g).__floor__(),g)),'upper':str(F((x[1]*g).__ceil__(),g))}
n=24
lo=sum((F(1,factorial(j)) for j in range(n+1)),F(0))
e=(lo,lo+F(n+2,(n+1)*factorial(n+1)))
ie=inv(e);ie2=mul(ie,ie);e4=powi(e,4)
z=add(add(e4,scale(e,-12)),add(scale(ie,30),scale(ie2,-13)))
z1=add(add(scale(e4,4),scale(e,-32)),add(scale(ie,56),scale(ie2,-20)))
tau=mul(z1,inv(z));kap=scale(tau,F(1,2));c=add((F(4),F(4)),neg(kap))
assert z[0]>0
assert F(23,10)<kap[0]<kap[1]<F(5,2)
assert F(3,2)<c[0]<c[1]<F(17,10)
t=F(1,3);nlog=18
s=sum((2*t**(2*j+1)/F(2*j+1) for j in range(nlog)),F(0))
ln2=(s,s+2*t**(2*nlog+1)/(F(2*nlog+1)*(1-t*t)))
loge=inv(ln2)
b05_payment=add((F(8,5),F(8,5)),neg(loge))
lowI_payment=add((F(2),F(2)),neg(loge))
assert b05_payment[0]>F(1573,10000)
assert lowI_payment[0]>F(5573,10000)
data={'e':enc(e),'z':enc(z),'z1':enc(z1),'tau':enc(tau),'kappa_necessary':enc(kap),'c_necessary':enc(c),'log2_e':enc(loge),'B05_asymptotic_payment_floor':enc(b05_payment),'lowI_addressing_payment_floor':enc(lowI_payment),'near_Dirac_recovery_coefficient':enc(add((F(2),F(2)),loge)),'arithmetic':'Fraction exponential/log series plus geometric tails; exact interval arithmetic; outward rational exports','all_assertions_passed':True}
(Path('out')/'coefficient_certificate.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps(data))
