#!/usr/bin/env python3
from fractions import Fraction
from hashlib import sha256
from decimal import Decimal, getcontext
from math import comb
from collections import Counter

getcontext().prec = 90

EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
 (TOP, BOT),
 (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
 (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
 ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00", "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
 (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
 (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
 ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
 ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
 ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
 ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]

def dec(q):
    return Decimal(q.numerator) / Decimal(q.denominator)

def reconstruct():
    base = int("".join(SLICES[0]),16)
    masks=[int("".join(row),16)^base for row in SLICES[1:]]
    seen=base
    hosts=[]
    for m in masks:
        assert not (seen&m)
        assert m.bit_count()==2
        seen |= m
        hosts.append([x for x in range(512) if (m>>x)&1])
    core=[-1 if (base>>x)&1 else 1 for x in range(512)]
    tab=[]
    for y in range(512):
        for x in range(512):
            v=core[x]
            for j,cells in enumerate(hosts):
                if x in cells and ((y>>j)&1):
                    v=-1
                    break
            tab.append(v)
    got=sha256(",".join(map(str,tab)).encode()).hexdigest()
    assert got==EXPECTED_SHA, got
    return core,hosts

def atanh_log_interval(x, terms=34):
    k=0
    y=x
    while y >= 2:
        y /= 2
        k += 1
    while y < 1:
        y *= 2
        k -= 1
    z=(y-1)/(y+1)
    s=Fraction(0)
    p=z
    for j in range(terms):
        s += p/Fraction(2*j+1)
        p *= z*z
    rem = 2*p/Fraction((2*terms+1),1)/(1-z*z)
    return 2*s, 2*s+rem, k

def ln2_interval(terms=60):
    z=Fraction(1,3)
    s=Fraction(0)
    p=z
    for j in range(terms):
        s += p/Fraction(2*j+1)
        p*=z*z
    rem=2*p/Fraction(2*terms+1)/(1-z*z)
    return 2*s,2*s+rem

LN2_LO,LN2_HI=ln2_interval()

def log2_interval(x,terms=34):
    lo,hi,k=atanh_log_interval(x,terms)
    if lo>=0:
        return Fraction(k)+lo/LN2_HI, Fraction(k)+hi/LN2_LO
    return Fraction(k)+lo/LN2_LO, Fraction(k)+hi/LN2_HI

def neg_plogp_bounds(p):
    if p==0: return Fraction(0),Fraction(0)
    llo,lhi=log2_interval(1/p)
    return p*llo,p*lhi

def entropy_bounds(probs):
    lo=Fraction(0); hi=Fraction(0)
    for p in probs:
        a,b=neg_plogp_bounds(p)
        lo+=a; hi+=b
    return lo,hi

def entropy_bounds_counts(counts,den):
    lo=Fraction(0); hi=Fraction(0)
    for num,mult in counts.items():
        if num==0: continue
        p=Fraction(num,den)
        a,b=neg_plogp_bounds(p)
        lo += mult*a
        hi += mult*b
    return lo,hi

def biased_sq_nums(values,P=2501,Q=2499,D=5000):
    # Exact tensor transform. For each coordinate, the S-bit 0 row is
    # [Q,P] and the S-bit 1 row is [-1,1].
    a=list(map(int,values))
    n=9
    for bit in range(n):
        step=1<<bit
        block=step<<1
        b=a[:]
        for base in range(0,1<<n,block):
            for j in range(step):
                i0=base+j; i1=i0+step
                v0=a[i0]; v1=a[i1]
                b[i0]=Q*v0+P*v1
                b[i1]=-v0+v1
        a=b
    nums=[]
    PQ=P*Q
    for S,N in enumerate(a):
        nums.append((PQ**S.bit_count())*N*N)
    return nums

def source_scalars(u):
    po = Fraction(1,2)+Fraction(513,256)*u-Fraction(105,16)*u**3+Fraction(99,8)*u**5-9*u**7+u**9
    dc = Fraction(513,256)-Fraction(315,16)*u**2+Fraction(495,8)*u**4-63*u**6+9*u**8
    dh = 9*(Fraction(1,4)-u**2)**4
    W = (Fraction(133,512)-Fraction(199935,65536)*u**2+Fraction(19863,2048)*u**4+
         Fraction(13095,1024)*u**6-Fraction(16767,128)*u**8+Fraction(34083,128)*u**10-
         Fraction(1887,8)*u**12+Fraction(423,4)*u**14-18*u**16+u**18)
    return po,dc,dh,W

def main():
    core,hosts=reconstruct()
    assert hosts == [[78,79],[113,121],[228,484],[170,186],[149,151],
                     [338,466],[284,316],[291,295],[393,457]], hosts
    T=set(sum(hosts,[]))
    edge_data=[]
    for a,b in hosts:
        d=a^b
        assert d and d&(d-1)==0
        r=d.bit_length()-1
        fixed_ones=(a & ~(1<<r)).bit_count()
        assert fixed_ones==4
        edge_data.append((a,b,r,fixed_ones))
    assert sorted(r for _,_,r,_ in edge_data)==list(range(9))

    g=[0 if x in T else core[x] for x in range(512)]
    indicators=[]
    for a,b in hosts:
        vals=[0]*512; vals[a]=vals[b]=1
        indicators.append(vals)

    P,Q,D=2501,2499,5000
    den=D**18
    nums=biased_sq_nums(g,P,Q,D)
    for vals in indicators:
        nums.extend(biased_sq_nums(vals,P,Q,D))
    assert sum(nums)==den
    nz=[a for a in nums if a]
    assert len(nums)==5120
    assert len(nz)==2816
    distinct=len(set(nz))
    assert distinct==31, distinct

    full_counts=Counter(nz)
    Hlo,Hhi=entropy_bounds_counts(full_counts,den)

    p=Fraction(P,D); q=Fraction(Q,D)
    m=(p*q)**4
    hp_lo,hp_hi=entropy_bounds([p,q])
    logm_lo,logm_hi=log2_interval(1/m)
    Hhost_lo=9*m*(logm_lo+8*hp_lo)
    Hhost_hi=9*m*(logm_hi+8*hp_hi)

    gnums=biased_sq_nums(g,P,Q,D)
    Hglo,Hghi=entropy_bounds_counts(Counter(a for a in gnums if a),den)
    assert Hglo+Hhost_lo <= Hhi and Hlo <= Hghi+Hhost_hi

    u=Fraction(1,5000)
    V=1-4*u*u
    hVlo,hVhi=entropy_bounds([V,1-V])

    po,dc,dh,W=source_scalars(u)
    assert po > Fraction(1,2)
    r1=Fraction(1,2)-u
    r2=1-po

    C0=Fraction(64548,10000)
    adag=Fraction(268204856,10**9)
    G1=2*C0

    dx1lo,dx1hi=log2_interval(Fraction(2500,2499))
    dx12lo,dx12hi=log2_interval(r1/r2)

    basecoef=dc*r1-r2
    Pconst=basecoef*G1+dh*C0
    A1lo,A1hi=basecoef*dx1lo,basecoef*dx1hi
    A12lo,A12hi=-r2*dx12hi,-r2*dx12lo

    Tlo=Hlo-dc*hVhi-adag*W
    Thi=Hhi-dc*hVlo-adag*W
    B0lo=Pconst-Thi
    B0hi=Pconst-Tlo

    qlo=(-A12hi)/A1hi
    qhi=(-A12lo)/A1lo
    thlo=(-B0hi)/A1hi
    thhi=(-B0lo)/A1lo

    Slo=A1lo+A12lo
    Shi=A1hi+A12hi
    assert Slo>0
    mlo=(-B0hi)/Shi
    mhi=(-B0lo)/Slo

    def defect_interval_at_equal(mv):
        if mv>=0:
            return B0lo+(A1lo+A12lo)*mv, B0hi+(A1hi+A12hi)*mv
        return B0lo+(A1hi+A12hi)*mv, B0hi+(A1lo+A12lo)*mv
    d0=defect_interval_at_equal(Fraction(0))
    d30=defect_interval_at_equal(Fraction(30))
    assert d0[1] < 0
    assert d30[0] > 0

    print("PASS")
    print("truth_sha256 =",EXPECTED_SHA)
    print("source_edges =",hosts)
    print("edge_fixed_ones =",[x[3] for x in edge_data])
    print("formal_coefficients =",len(nums))
    print("nonzero_coefficients =",len(nz))
    print("distinct_nonzero_masses =",distinct)
    print("H_lo =",dec(Hlo))
    print("H_hi =",dec(Hhi))
    print("H_width =",dec(Hhi-Hlo))
    print("H_host_lo =",dec(Hhost_lo))
    print("H_host_hi =",dec(Hhost_hi))
    print("H_empty_lo =",dec(Hglo))
    print("H_empty_hi =",dec(Hghi))
    print("h2V_lo =",dec(hVlo))
    print("h2V_hi =",dec(hVhi))
    print("p_out =",dec(po))
    print("d_core =",dec(dc))
    print("d_host =",dec(dh))
    print("W =",dec(W))
    print("Pconst =",dec(Pconst))
    print("B0_lo =",dec(B0lo))
    print("B0_hi =",dec(B0hi))
    print("A1_lo =",dec(A1lo))
    print("A1_hi =",dec(A1hi))
    print("A12_lo =",dec(A12lo))
    print("A12_hi =",dec(A12hi))
    print("q_ratio_lo =",dec(qlo))
    print("q_ratio_hi =",dec(qhi))
    print("theta_lo =",dec(thlo))
    print("theta_hi =",dec(thhi))
    print("equal_slope_mcrit_lo =",dec(mlo))
    print("equal_slope_mcrit_hi =",dec(mhi))
    print("D_equal_0_hi =",dec(d0[1]))
    print("D_equal_30_lo =",dec(d30[0]))
    print("checks = exact source SHA; exact edge geometry; exact rational Parseval; 31 mass types; rigorous log intervals; two-secant defect interface; peer |G'|<31 box undecided")

if __name__=="__main__":
    main()
