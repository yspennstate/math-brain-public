"""Reproduce constants, with exact rational logarithm enclosures for final C."""
from fractions import Fraction as F
from decimal import Decimal, localcontext
import json,math

def ln_interval(q,N=60):
    z=(q-1)/(q+1)
    total=2*sum((z**(2*k+1)/F(2*k+1) for k in range(N)),F(0))
    error=2*abs(z)**(2*N+1)/(F(2*N+1)*(1-z*z))
    return total-error,total+error

l2,u2=ln_interval(F(2));M=F(633,100)*161
assert F(99,70)**2>2
assert sum((F(1,2)**k/F(math.factorial(k)) for k in range(4)),F(0))>F(100,61)
mcs_upper_rational=F(32,3)*(2+3*F(99,70)+2*F(61,100))
assert mcs_upper_rational<80
e_lower=sum((F(1,math.factorial(k)) for k in range(7)),F(0))
noise_upper_rational=4/(1-1/e_lower)
assert noise_upper_rational<F(633,100)
lr,ur=ln_interval((1+2*M)/2048)
# C=26+(3+2 ln((1+2M)/2048))/ln2; its numerator is positive.
lo=26+(3+2*lr)/u2;hi=26+(3+2*ur)/l2
assert lo<hi<F(7579,250)<31
with localcontext() as ctx:
    ctx.prec=65
    decimals=[str(Decimal(q.numerator)/Decimal(q.denominator)) for q in (lo,hi)]
bound=2+3*math.sqrt(2)+2/math.sqrt(math.e)
o={'K0':3,'Mcs_rational_upper':str(mcs_upper_rational),'noise_rational_upper':str(noise_upper_rational),'supremum_analytic_upper':bound,'Mcs_analytic_upper':32/3*bound,'Mcs_rounded':80,'M':float(M),'M_exact':str(M),'C_expression':3/math.log(2)+4+2*math.log2(1+2*float(M)),'C_rounded':31,'C_safe_decimal':'30.316','C_rational_lower':str(lo),'C_rational_upper':str(hi),'C_interval_decimal_for_display':decimals,'C_decimal_upper_exact_check':str(F(7579,250)),'noise_factor':4/(1-1/math.e),'kernel_lower':(23/24)**2,'kernel_constant_upper':math.sqrt(2*math.pi)*(24/23)**2}
assert F(576,529)**2*F(44,7)<9
open('constants.json','w').write(json.dumps(o,indent=2)+'\n')
print(json.dumps({k:v for k,v in o.items() if not k.startswith('C_rational')},indent=2))
