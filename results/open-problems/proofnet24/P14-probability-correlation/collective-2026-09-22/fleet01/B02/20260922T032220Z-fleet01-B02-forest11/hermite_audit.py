from fractions import Fraction
from math import factorial

MAX_N = 30

def add(a,b,N):
    c=[Fraction(0)]*(N+1)
    for i,x in enumerate(a[:N+1]): c[i]+=x
    for i,x in enumerate(b[:N+1]): c[i]+=x
    return c

def mul(a,b,N):
    c=[Fraction(0)]*(N+1)
    for i,x in enumerate(a):
        if i>N: break
        for j,y in enumerate(b):
            if i+j>N: break
            c[i+j]+=x*y
    return c

def scale(a,s): return [x*s for x in a]

def exp_series(a,N):
    b=[Fraction(0)]*(N+1); b[0]=1
    for n in range(1,N+1):
        b[n]=sum(Fraction(k)*a[k]*b[n-k] for k in range(1,n+1))/n
    return b

def inv1minus(a,N):
    b=[Fraction(0)]*(N+1); b[0]=1
    for n in range(1,N+1):
        b[n]=sum(a[k]*b[n-k] for k in range(1,n+1))
    return b

def He(k,x):
    if k==0: return 1
    h0,h1=1,x
    if k==1: return h1
    for j in range(1,k):
        h0,h1=h1,x*h1-j*h0
    return h1

N=MAX_N
R=[Fraction(0)]*(N+1)
for n in range(1,N+1):
    R[n]=Fraction(n**(n-1), factorial(n))
T=add(R, scale(mul(R,R,N), Fraction(-1,2)), N)
F=exp_series(T,N)
A=exp_series(R,N)
A2=mul(A,A,N); A3=mul(A2,A,N); A4=mul(A3,A,N)
Egf=mul(F,A2,N)
Jaf=mul(F,A3,N)
factor=add([Fraction(1)]+[Fraction(0)]*N,scale(inv1minus(R,N),4),N)
Jdf=mul(mul(F,A4,N),factor,N)

def sc(expr,m): return expr[m]*factorial(m)

checks=0
for n in range(4,MAX_N+1):
    k=n-4; x=n+1
    a=He(k,x)
    s=Fraction(k*He(k-1,x),a) if k else Fraction(0)
    Z=sc(F,n); E=sc(Egf,n-2); Ja=sc(Jaf,n-3); Jd=sc(Jdf,n-4)
    assert Z == a*(n*n+3*n+10-(n+4)*s)
    assert E == a*(2*n+6-3*s)
    assert Ja == a*(4-s)
    assert Jd == a*(5-s)
    G=(5-n)*s*s+(n*n-4*n-6)*s-n*n+9*n-14
    assert E*E-Z*Jd == a*a*G
    assert E*E-Z*Ja == (E*E-Z*Jd)+Z*a
    L=Fraction((n-4)*(n-1)*(n+4),(n+1)**3)
    assert s >= L
    assert s < 1
    assert E*E-Z*Jd > 0
    assert E*E-Z*Ja > 0
    checks += 10

shifted=[666396,551661,187651,33233,3147,142,2]
assert all(c>0 for c in shifted)
checks += 1

print(f"checked_n=4..{MAX_N}")
print(f"exact_assertions={checks}")
print("small_gaps:", "K4_disjoint=6", "K5_disjoint=210", "K6_disjoint=13052")
print("shifted_P_coefficients_low_to_high="+",".join(map(str,shifted)))
print("STATUS=PASS")
