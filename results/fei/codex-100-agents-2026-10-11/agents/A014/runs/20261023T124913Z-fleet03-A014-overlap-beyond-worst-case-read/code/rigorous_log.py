from fractions import Fraction as F
from functools import lru_cache
import math
SCALE=1<<64
TAIL=F(9,148*3**37)
def ceildiv(a,b):return -((-a)//b)
def ln_unit(x):
    # 1<=x<=2. Every operation is a directed integer enclosure.
    assert 1<=x<=2
    z=(x-1)/(x+1)
    low=(z.numerator*SCALE)//z.denominator;high=ceildiv(z.numerator*SCALE,z.denominator)
    square_low=low*low//SCALE;square_high=ceildiv(high*high,SCALE)
    power_low=low;power_high=high;sum_low=sum_high=0
    for j in range(18):
        odd=2*j+1
        sum_low+=power_low//odd;sum_high+=ceildiv(power_high,odd)
        power_low=power_low*square_low//SCALE;power_high=ceildiv(power_high*square_high,SCALE)
    return F(2*sum_low,SCALE),F(2*sum_high,SCALE)+TAIL
LN2=ln_unit(F(2))
@lru_cache(None)
def lg(x):
    x=F(x);assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length()
    x=x/F(2**k) if k>=0 else x*2**(-k)
    while x<1:x*=2;k-=1
    while x>=2:x/=2;k+=1
    if x==1:return F(k),F(k)
    low,high=ln_unit(x);scale=1<<40
    low=low/LN2[1]+k;high=high/LN2[0]+k
    return F(math.floor(low*scale),scale),F(math.ceil(high*scale),scale)
