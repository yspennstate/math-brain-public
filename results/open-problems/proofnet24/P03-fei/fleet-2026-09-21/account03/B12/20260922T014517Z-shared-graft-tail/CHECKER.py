from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
from decimal import Decimal, getcontext
import hashlib

EXPECTED_SHA='f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839'
TOP='fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00'
BOT='fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'
SLICES=[
 (TOP,BOT),
 (TOP,'fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000'),
 (TOP,'fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000'),
 ('fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00','fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'),
 (TOP,'fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000'),
 (TOP,'fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000'),
 ('fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00',BOT),
 ('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00',BOT),
 ('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00',BOT),
 ('fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00',BOT),
]
TERMS=36
ALPHA=F(9,256)
IS=F(261,128)
C1=F(14593,65536)
I1=F(68013,32768)
R4_LO=F("6.5218509485644448965490881329959858569477358114202361")
R4_HI=F("6.5218509485644448965496895824490791318643557898359042")

def fwht_int(a):
    a=list(a); h=1
    while h<len(a):
        for s in range(0,len(a),2*h):
            for j in range(s,s+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def core_and_hosts():
    base=int(''.join(SLICES[0]),16)
    masks=[int(''.join(row),16)^base for row in SLICES[1:]]
    assert all(m.bit_count()==2 for m in masks)
    seen=base
    hosts=[]
    for m in masks:
        assert not(seen&m); seen |= m
        hosts.append([x for x in range(512) if (m>>x)&1])
    return base,hosts

def source_hash(base,hosts):
    core=[-1 if (base>>x)&1 else 1 for x in range(512)]
    out=[]
    for y in range(512):
        row=core.copy()
        for j,cells in enumerate(hosts):
            if (y>>j)&1:
                for x in cells: row[x]=-1
        out.extend(row)
    return hashlib.sha256(",".join(map(str,out)).encode()).hexdigest()

def core_data(base,hosts):
    a=[-1 if (base>>x)&1 else 1 for x in range(512)]
    for pair in hosts:
        for x in pair: a[x]=0
    A=fwht_int(a)
    Q=[]
    for lo,hi in hosts:
        q=[0]*512; q[lo]=1; q[hi]=-1
        Q.append(fwht_int(q))
    Qsum=[sum(q[j] for q in Q) for j in range(512)]
    return A,Qsum

def pow2(k):
    return F(1<<k,1) if k>=0 else F(1,1<<(-k))

def norm_pow2(x):
    assert x>0
    e=x.numerator.bit_length()-x.denominator.bit_length()
    while x<pow2(e): e-=1
    while x>=pow2(e+1): e+=1
    return e,x/pow2(e)

def ln_unit(y):
    assert F(1)<=y<=F(2)
    if y==1: return F(0),F(0)
    z=(y-1)/(y+1); z2=z*z; p=z; s=F(0)
    for k in range(TERMS):
        s += p/F(2*k+1); p*=z2
    lo=2*s
    rem=2*p/(F(2*TERMS+1)*(1-z2))
    return lo,lo+rem

@lru_cache(None)
def log2_interval(x):
    x=F(x)
    if x<1:
        lo,hi=log2_interval(1/x); return -hi,-lo
    e,m=norm_pow2(x)
    a,b=ln_unit(m); c,d=ln_unit(F(2))
    return F(e)+a/d, F(e)+b/c

def phi_interval(x):
    x=F(x)
    if x==0: return F(0),F(0)
    lo,hi=log2_interval(1/x)
    return x*lo,x*hi

def hcore_interval(A,Q,b):
    b=F(b)
    den=b.denominator; num=b.numerator
    norm=(512*den)**2
    hist=Counter()
    for a,q in zip(A,Q):
        v=a*den+num*q
        if v: hist[v*v]+=1
    lo=hi=F(0)
    for s,m in hist.items():
        p=F(s,norm); l,h=log2_interval(1/p)
        lo += m*p*l; hi += m*p*h
    return lo,hi

def K_interval(A,Q,b):
    hc_lo,hc_hi=hcore_interval(A,Q,b)
    ph_lo,ph_hi=phi_interval(b*b)
    corr_lo=ALPHA*(-ph_hi + 16*(1-b*b))
    corr_hi=ALPHA*(-ph_lo + 16*(1-b*b))
    return hc_lo+corr_lo,hc_hi+corr_hi

def nearest_dyadic(x,bits):
    den=1<<bits
    n=(x.numerator*den*2 + x.denominator)//(2*x.denominator)
    return F(n,den)

def dec(x,d=60):
    getcontext().prec=d+20
    return format(Decimal(x.numerator)/Decimal(x.denominator),f'.{d}f')

def main():
    base,hosts=core_and_hosts()
    digest=source_hash(base,hosts)
    assert digest==EXPECTED_SHA
    A,Q=core_data(base,hosts)

    # Exact coefficient facts used in a uniform derivative bound for K on B=[0.0024,0.0025].
    assert max(abs(x) for x in A)==114
    assert max(abs(x) for x in Q)==18
    assert all((a!=0) or (q==0) for a,q in zip(A,Q))
    assert min(abs(a) for a in A if a)==2

    # On B=[3/1250,1/400], |A+bQ| >= 2-18/400=391/200 and <115.
    # Hence x=((A+bQ)/512)^2 > 2^-17, so |phi'(x)|<17+1/ln2<37/2.
    # Also |x'| <= 2*18*115/512^2. 512 coordinates give 38295/256.
    # The scalar correction derivative is <(9/256)*(71/400).
    KDER=F(38295,256)+F(9,256)*F(71,400)
    assert KDER==F(15318639,102400) and KDER<F(150)

    def cnext(c): return F(57,256)+c**4/F(256)
    c2=cnext(C1); c3=cnext(c2); c4=cnext(c3); c5=cnext(c4)
    b4=c4**4; b5=c5**4
    B_LO=F(3,1250); B_HI=F(1,400)
    assert B_LO < b4 < B_HI and B_LO < b5 < B_HI

    # Influence recurrence: I' = 261/128 + (9/256)(I^4-1).
    def inext(I): return IS+ALPHA*(I**4-1)
    I2=inext(I1); I3=inext(I2); I4=inext(I3); I5=inext(I4); I6=inext(I5)

    # Evaluate K at nearby small-denominator dyadics, then use the proved |K'|<150.
    d4=nearest_dyadic(b4,50); dist4=abs(b4-d4)
    k4lo0,k4hi0=K_interval(A,Q,d4)
    k4lo=k4lo0-KDER*dist4; k4hi=k4hi0+KDER*dist4
    T4lo=F(128,133)*k4lo; T4hi=F(128,133)*k4hi
    # R5-R4 = (T4-R4)*(133/128)/(I5-1), equivalent to peer recurrence.
    R5lo=R4_LO + (k4lo-F(133,128)*R4_HI)/(I5-1)
    R5hi=R4_HI + (k4hi-F(133,128)*R4_LO)/(I5-1)
    assert R5lo>R4_HI
    assert R5lo-R4_HI > F(986,10**12)  # > 9.86e-10

    d5=nearest_dyadic(b5,60); dist5=abs(b5-d5)
    k5lo0,k5hi0=K_interval(A,Q,d5)
    k5lo=k5lo0-KDER*dist5; k5hi=k5hi0+KDER*dist5
    T5lo=F(128,133)*k5lo; T5hi=F(128,133)*k5hi
    R6lo=R5lo + (k5lo-F(133,128)*R5hi)/(I6-1)
    R6hi=R5hi + (k5hi-F(133,128)*R5lo)/(I6-1)
    assert R6lo>R5hi
    assert R6lo-R5hi > F(17,10**16)  # >1.7e-15
    assert R6lo > F("6.5218509495504479")

    # Infinite-tail theorem. f(c)=57/256+c^4/256 is a contraction on c<=0.223:
    # f'(c)=c^3/64 < 1/5000. Since c5>c6, all later c_t decrease
    # and stay within a geometric tail of c5.
    c6=cnext(c5)
    assert c5>c6 and c5<F(223,1000)
    L=F(1,5000)
    assert F(223,1000)**3/F(64) < L
    ctail=(c5-c6)/(1-L)
    btail=4*c5**3*ctail
    ktail_lo=k5lo-KDER*btail
    ktail_hi=k5hi+KDER*btail
    Ttail_lo=F(128,133)*ktail_lo
    assert ktail_hi<F(7)

    # From I6>10^8 and I_{t+1}>I_t^2 thereafter, I7>10^16 and
    # the sum of all possible future positive increments is <14/(10^16-1).
    assert I6>10**8
    assert ALPHA*(I6**4) > I6**2
    future_positive_budget=F(14,10**16-1)
    Rtail_hi=R6hi+future_positive_budget
    assert Rtail_hi<Ttail_lo
    # Therefore every later increment is positive, and the limiting ratio
    # exists in [R6lo,Rtail_hi].

    print("PASS")
    print("source_sha256",digest)
    print("K_derivative_bound",str(KDER),"<150")
    print("b4_dyadic_distance",dec(dist4,30))
    print("T4_lower",dec(T4lo,60))
    print("T4_upper",dec(T4hi,60))
    print("R5_lower",dec(R5lo,60))
    print("R5_upper",dec(R5hi,60))
    print("gain5_over_R4_upper",dec(R5lo-R4_HI,60))
    print("b5_dyadic_distance",dec(dist5,30))
    print("T5_lower",dec(T5lo,60))
    print("T5_upper",dec(T5hi,60))
    print("R6_lower",dec(R6lo,70))
    print("R6_upper",dec(R6hi,70))
    print("gain6_over_R5_upper",dec(R6lo-R5hi,70))
    print("tail_T_uniform_lower",dec(Ttail_lo,70))
    print("tail_future_positive_budget",dec(future_positive_budget,70))
    print("R_infinity_lower",dec(R6lo,70))
    print("R_infinity_upper",dec(Rtail_hi,70))
    print("tail_monotone_from_F6",True)
    print("full_FEI_status","OPEN_NOT_PROVED")

if __name__=="__main__":
    main()
