"""Rational log linear forms, exact products, and signed outward enclosures."""
from fractions import Fraction as F
from math import lcm,prod
VERSION='A073-rational-log-product/1'

def factor(n):
    if n<1: raise ValueError('Positive integer required')
    ans={};p=2
    while p*p<=n:
        while n%p==0:ans[p]=ans.get(p,0)+1;n//=p
        p+=1
    if n>1:ans[n]=ans.get(n,0)+1
    return ans

def add_log(form,weight,x):
    x=F(x);weight=F(weight)
    if x<=0:raise ValueError('Positive log argument required')
    for n,sign in [(x.numerator,1),(x.denominator,-1)]:
        for p,e in factor(n).items():form[p]=form.get(p,F(0))+sign*weight*e

def add_entropy(form,weight,masses):
    masses=list(map(F,masses))
    if any(x<0 for x in masses) or sum(masses)!=1:raise ValueError('Probability law required')
    for x in masses:
        if x:add_log(form,-F(weight)*x,x)

def product_certificate(form):
    form={p:F(c) for p,c in form.items() if c}
    L=lcm(*(c.denominator for c in form.values())) if form else 1
    exponents={p:int(L*c) for p,c in form.items()}
    U=prod(p**e for p,e in exponents.items() if e>0)
    V=prod(p**(-e) for p,e in exponents.items() if e<0)
    sign=(U>V)-(U<V)
    # Certified dyadic ratio bounds require only shifts/comparisons.
    k=U.bit_length()-V.bit_length()
    def ge_power(k):return U>=V<<k if k>=0 else U<<(-k)>=V
    while not ge_power(k):k-=1
    while ge_power(k+1):k+=1
    exact=(U==V<<k if k>=0 else U<<(-k)==V)
    bounds=(F(k,L),F(k,L)) if exact else (F(k,L),F(k+1,L))
    return L,exponents,U,V,sign,bounds,exact

def ln_reduced(t,N=8):
    t=F(t)
    if not 1<=t<=2:raise ValueError('Range reduction required')
    y=(t-1)/(t+1)
    lo=2*sum((y**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
    tail=2*y**(2*N+1)/(F(2*N+1)*(1-y*y))
    return lo,lo+tail

def multiply(c,bounds):
    a,b=bounds;return (c*a,c*b) if c>=0 else (c*b,c*a)

def log2_bounds(x,N=8):
    x=F(x)
    if x<=0:raise ValueError('Positive log argument required')
    k=0;t=x
    while t<1:t*=2;k-=1
    while t>=2:t/=2;k+=1
    if t==1:return F(k),F(k)
    a,b=ln_reduced(t,N);c,d=ln_reduced(F(2),N)
    # k is exact; divide only the nonnegative reduced numerator.
    return F(k)+a/d,F(k)+b/c

def form_bounds(form,N=8):
    lo=hi=F(0)
    for p,c in form.items():
        a,b=multiply(c,log2_bounds(p,N));lo+=a;hi+=b
    return lo,hi
