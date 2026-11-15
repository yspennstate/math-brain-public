"""Certify the exact decreasing-envelope bound, improving the simplified R(n)."""
from fractions import Fraction as F
from math import isqrt,factorial
from pathlib import Path
import json,sys
sys.set_int_max_str_digits(0)

def atan_bounds(q,M):
 x=F(1,q);s=sum((-1)**j*x**(2*j+1)/(2*j+1) for j in range(M));t=(-1)**M*x**(2*M+1)/(2*M+1)
 return min(s,s+t),max(s,s+t)
def ln_bounds(x,M=90):
 y=(x-1)/(x+1);lo=2*sum(y**(2*j+1)/(2*j+1) for j in range(M));hi=lo+2*y**(2*M+1)/((2*M+1)*(1-y*y));return lo,hi
p,q=atan_bounds(5,45);r,s=atan_bounds(239,15);pi_hi=16*q-4*r
scale=10**40
def sqrt_upper(x):return F(isqrt((x*scale*scale).numerator//(x*scale*scale).denominator)+1,scale)
sq2=sqrt_upper(F(2));sq101=sqrt_upper(F(101));sq24pi=sqrt_upper(24*pi_hi)
ln2lo,_=ln_bounds(F(2));_,log2512hi=ln_bounds(F(25,12));_,asinhhi=ln_bounds((sq101+1)/10)
rest=-(2-sq2)/sq24pi+F(1,48)+F(12,13)*log2512hi+2*asinhhi+(sq101-1)/50
upper=2+rest/ln2lo
assert upper<F(3459354,1000000)
assert sum(F(10,9)**k/factorial(k) for k in range(5))>3
assert F(625,576)<F(9,8)
import mpmath as mp
mp.mp.dps=90
n=mp.mpf(25);a=2*mp.asinh(1/(2*mp.sqrt(n)));d=(2-mp.sqrt(2))/mp.sqrt(mp.pi);x=(n+1)/(2*n)
exact=(mp.log(4)-d/mp.sqrt(n-1)+1/(2*(n-1))-(1-x)*mp.log(1-x)/x+a+1/(n*mp.expm1(a)))/mp.log(2)
print(json.dumps({'chosen_B_bound':'3459354/1000000','analytic_envelope_at_25':str(exact),'rational_upper_decimal':mp.nstr(mp.mpf(upper.numerator)/upper.denominator,80),'upper_numerator':str(upper.numerator),'upper_denominator':str(upper.denominator),'passes':True},indent=2))
