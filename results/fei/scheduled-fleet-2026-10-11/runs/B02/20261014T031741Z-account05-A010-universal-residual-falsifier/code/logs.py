from fractions import Fraction as Q
from functools import lru_cache
@lru_cache(maxsize=1024)
def log2_bounds(x):
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length(); y=x/Q(2)**k
    if y<1: y*=2; k-=1
    def ln(t):
        z=(t-1)/(t+1); term=z; s=Q(0)
        for j in range(16): s+=term/(2*j+1); term*=z*z
        return 2*s,2*s+2*term/(33*(1-z*z))
    a,b=ln(y); c,d=ln(Q(2)); return k+a/d,k+b/c
def dyadic(x,up):
    scale=1<<50
    return Q((x*scale).__ceil__() if up else (x*scale).__floor__(),scale)
def z_bounds():
    scale=1<<64; lo=0; hi=scale
    while hi-lo>1:
        mid=(lo+hi)//2
        if 64*mid**5<=scale**5: lo=mid
        else: hi=mid
    assert 64*lo**5<=scale**5<=64*hi**5
    return Q(lo,scale),Q(hi,scale)
