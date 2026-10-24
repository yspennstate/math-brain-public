from fractions import Fraction
SCALE=10**15
K=40

def ln2_bounds():
    z=Fraction(1,3); s=Fraction(0); zz=z
    for k in range(K):
        s += zz/Fraction(2*k+1); zz *= z*z
    lo=2*s
    hi=lo+Fraction(2)*zz/Fraction(2*K+1)/(1-z*z)
    return lo,hi

def ln_m_bounds(m):
    z=(m-1)/(m+1); s=Fraction(0); zz=z
    for k in range(K):
        s += zz/Fraction(2*k+1); zz *= z*z
    lo=2*s
    hi=lo+Fraction(2)*zz/Fraction(2*K+1)/(1-z*z)
    return lo,hi

def log2_upper(x):
    e=x.numerator.bit_length()-x.denominator.bit_length()
    m=x/Fraction(2**e,1) if e>=0 else x*Fraction(2**(-e),1)
    while m<1: e-=1; m*=2
    while m>=2: e+=1; m/=2
    _,him=ln_m_bounds(m); ln2lo,_=ln2_bounds()
    return Fraction(e)+him/ln2lo

def table(N):
    out={}
    for w in range(2,N+1,2):
        x=Fraction(N*N,w*w)
        term=Fraction(0) if x<=1 else Fraction(w*w,N*N)*log2_upper(x)
        out[w]=(term.numerator*SCALE+term.denominator-1)//term.denominator
    return out
for N in (32,64):
    print(N,table(N))
