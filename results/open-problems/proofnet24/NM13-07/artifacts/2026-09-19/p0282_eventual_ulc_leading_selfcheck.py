from fractions import Fraction
from math import factorial

JMAX=12

def parts(n,maxp=None):
    if n==0:
        yield (); return
    if maxp is None or maxp>n: maxp=n
    for first in range(maxp,0,-1):
        rem=n-first
        if rem==0:
            yield (first,)
        else:
            for t in parts(rem,min(first,rem)):
                yield (first,)+t

def hook_dim(mu):
    n=sum(mu); hp=1
    for i,row in enumerate(mu):
        for c in range(row):
            hp *= (row-c) + sum(1 for rr in mu[i+1:] if rr>c)
    return factorial(n)//hp

def mul(a,b):
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def add(a,b):
    c=[Fraction(0)]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return c

def dim_poly(j,mu):
    # Same Weyl-polynomial formula independently used by the fixed-defect certificates.
    r=1+len(mu); C=Fraction(1)
    for a in range(len(mu)):
        for b in range(a+1,len(mu)):
            C *= mu[a]-mu[b]+(b-a)
    for t,val in enumerate(mu): C /= factorial(val+r-t-2)
    p=[Fraction(1)]
    for s in range(max(0,j-r+1)): p=mul(p,[Fraction(-s),Fraction(1)])
    for t,val in enumerate(mu,start=1): p=mul(p,[Fraction(-j-val+t),Fraction(1)])
    return [C*x for x in p]

def Epoly(j):
    if j==0: return [Fraction(1)]
    s=[Fraction(0)]
    for mu in parts(j):
        d=dim_poly(j,mu)
        s=add(s,mul(d,d))
    while len(s)>1 and s[-1]==0:s.pop()
    return s

print('P0282 exact self-check of universal fixed-defect ULC asymptotic coefficients')
for j in range(1,JMAX+1):
    ss=sum(hook_dim(mu)**2 for mu in parts(j))
    assert ss==factorial(j), ('REGULAR_REP_FAIL',j,ss)
    E=Epoly(j)
    assert len(E)-1==2*j
    a=Fraction(1,factorial(j))
    b=-Fraction(j*(j+1),factorial(j))
    assert E[-1]==a and E[-2]==b, ('E_TOP2_FAIL',j,E[-2:],b,a)

    am=Fraction(1,factorial(j-1))
    ap=Fraction(1,factorial(j+1))
    bm=-Fraction((j-1)*j,factorial(j-1)) if j>1 else Fraction(0)
    bp=-Fraction((j+1)*(j+2),factorial(j+1))
    # coefficient of n^(4j) after exact cancellation of n^(4j+1)
    lead1 = j*(2*a*b-(j+1)*a*a)
    lead2 = -(j+1)*((am*bp+bm*ap)-j*am*ap)
    Mlead=lead1+lead2
    expected=Fraction(j,factorial(j)**2)
    assert Mlead==expected and Mlead>0, ('M_LEAD_FAIL',j,Mlead,expected)
    print(f'j={j} sum_fmu_sq={ss} E_lead={a} E_next={b} M_lead={Mlead}')
print('SELF_CHECK_SCOPE=j<=12; theorem itself is proved symbolically in the run report')
print('ALL_EXACT_CHECKS_PASS')
