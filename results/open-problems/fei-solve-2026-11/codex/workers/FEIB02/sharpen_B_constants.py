"""Rigorous rational enclosure of 3+R(25)/ln 2."""
from fractions import Fraction as F
from math import isqrt
import json

def atan_bounds(q,M):
 x=F(1,q)
 s=sum((-1)**j*x**(2*j+1)/(2*j+1) for j in range(M))
 nextterm=(-1)**M*x**(2*M+1)/(2*M+1)
 return min(s,s+nextterm),max(s,s+nextterm)
a,b=atan_bounds(5,40);c,d=atan_bounds(239,12)
pi_lo=16*a-4*d;pi_hi=16*b-4*c
scale=10**32
sqrt2_hi=F(isqrt(2*scale*scale)+1,scale)
sqrtpi_hi=F(isqrt((pi_hi*scale*scale).numerator//(pi_hi*scale*scale).denominator)+1,scale)
dlo=(2-sqrt2_hi)/sqrtpi_hi
ln2lo=2*sum(F(1,3)**(2*j+1)/(2*j+1) for j in range(40))
clo=2*ln2lo-1
Rhi=(2-dlo)/5-clo/25+F(1,1200)+F(1,1000)
upper=3+Rhi/ln2lo
assert upper<F(3462071,1000000)
import mpmath as mp
mp.mp.dps=70
print(json.dumps({'chosen_B_bound':'3462071/1000000','rational_enclosure_decimal':mp.nstr(mp.mpf(upper.numerator)/upper.denominator,65),'enclosure_numerator':str(upper.numerator),'enclosure_denominator':str(upper.denominator),'passes':True},indent=2))
