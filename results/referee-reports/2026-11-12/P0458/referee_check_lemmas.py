"""Auxiliary rational and algebra checks, independent of code/checks.py."""
from fractions import Fraction as Q
from math import comb, factorial
from referee_exact import add,mul,anti,scale,integ,cdf

def shift_down(p,power):
    assert all(x==0 for x in p[:power])
    return p[power:]

def beta_pdf(a,b):
    const=Q(factorial(a+b-1),factorial(a-1)*factorial(b-1))
    return [Q(0)]*(a-1)+[const*comb(b-1,j)*(-1)**j for j in range(b)]

def expectation(p,density): return integ(mul(p,density))

checks=0
for n in range(3,13):
    for k in range(1,n-1):
        # F=Beta(k,n-k-1) CDF, from a binomial order statistic.
        f=add([1],scale(cdf(n-2,k-1),-1))
        q=shift_down(anti(f),1)
        b=shift_down(anti(add([1],scale(cdf(n-3,k-1),-1))),1)
        # E_W[(F(x)-F(W))_+] = x F(x)-int_0^x F.
        first=add(mul([0,1],f),scale(anti(f),-1))
        pmean=add(b,scale(shift_down(first,1),Q(1,n-2)))
        assert add(pmean,scale(q,-1))==[Q(0)]*max(len(pmean),len(q))
        # E_W[(F(x)-F(W))_+^2] before subtracting its mean square.
        second=add(mul([0,1],mul(f,f)),scale(mul(f,anti(f)),-2),anti(mul(f,f)))
        cov=scale(shift_down(add(second,scale(mul(first,first),-1)),2),Q(1,(n-2)**2))
        density=beta_pdf(k+1,n-k-1)
        eq=expectation(q,density); eq2=expectation(mul(q,q),density)
        vh=k*(eq-eq2)+k*(k-1)*expectation(cov,density)+k*k*(eq2-eq*eq)
        from referee_exact import moments
        eh0,vh0=moments(n,k)
        assert k*eq==eh0 and vh==vh0
        checks+=1
print(f'{checks} exact polynomial checks: conditional mean p=q and variance identity agree with direct two-edge calculation, 3<=n<=12, all 1<=k<=n-2: PASS')

for r in range(1,61):
    mu=sum((Q((r-l)*factorial(r-1+l),factorial(l)*factorial(r-1)*2**(r+l)) for l in range(r)),Q(0))
    closed=Q(r*comb(2*r,r),4**r)
    ds=Q((2*r-1)*comb(2*r-2,r-1),2**(2*r-1))
    assert mu==closed==ds
print('mu_r finite sum = gamma closed form = c_r, r=1..60: PASS')

for a in range(1,81):
    for b in range(1,81):
        kurt=Q(6*((a-b)**2*(a+b+1)-a*b*(a+b+2)),a*b*(a+b+2)*(a+b+3))
        assert abs(kurt)<=Q(6,a)+Q(6,b)+Q(6,a+b)
print('beta kurtosis inequality, a,b=1..80 (exact): PASS')

for n in range(4,101):
    for k in range(1,n-1):
        s2=Q(k*(n-k),n)
        vx=Q((k+1)*(n-k-1),n*n*(n+1))
        vt=Q(k*(n-k-1),(n-1)**2*n)
        assert vx<=2*s2/(n*n) and vt<=2*s2/(n*n)
print('beta variance bounds in Lemma 2.4, 4<=n<=100 (exact): PASS')
