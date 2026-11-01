from fractions import Fraction
from math import comb
from itertools import permutations

A = 0
def check(cond, msg):
    global A
    A += 1
    if not cond:
        raise AssertionError(msg)

def divisors(n):
    return [d for d in range(1,n+1) if n % d == 0]

def mobius(n):
    if n == 1:
        return 1
    x=n
    parity=0
    p=2
    while p*p <= x:
        if x % p == 0:
            x //= p
            parity ^= 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        parity ^= 1
    return -1 if parity else 1

def Iq(q,m):
    num=sum(mobius(d)*q**(m//d) for d in divisors(m))
    check(num % m == 0, f"Iq divisibility q={q} m={m}")
    return num//m

# Direct irreducibility over F_2 for small degrees.
def gf2_deg(p):
    return p.bit_length()-1

def gf2_mod(f,g):
    dg=gf2_deg(g)
    while f and gf2_deg(f) >= dg:
        f ^= g << (gf2_deg(f)-dg)
    return f

def gf2_divmod(f,g):
    q=0
    r=f
    dg=gf2_deg(g)
    while r and gf2_deg(r) >= dg:
        sh=gf2_deg(r)-dg
        q ^= 1 << sh
        r ^= g << sh
    return q,r

def irreducible_gf2(f):
    m=gf2_deg(f)
    if m <= 0:
        return False
    for d in range(1,m//2+1):
        for low in range(1<<d):
            g=(1<<d)|low
            if gf2_mod(f,g)==0:
                return False
    return True

irreducibles_by_degree={}
for m in range(1,9):
    L=[]
    for low in range(1<<m):
        f=(1<<m)|low
        if irreducible_gf2(f):
            L.append(f)
    irreducibles_by_degree[m]=L
    check(len(L)==Iq(2,m), f"direct irreducibles m={m}")

# Coefficient bound used in the written singularity proof.
for m in range(2,121):
    err=abs(m*Iq(2,m)-2**m)
    check(err <= m*2**((m+1)//2), f"tail bound m={m}")

R=6

# Exact degree-profile enumeration of squarefree monic polynomials with R factors.
def profiles_fixed(N,R=R):
    I=[0]+[Iq(2,m) for m in range(1,N+1)]
    out=[]
    def rec(m, remN, remR, d):
        if remR==0:
            if remN==0:
                out.append(dict(d))
            return
        if m > N or remN <= 0:
            return
        maxk=min(I[m], remR, remN//m)
        for k in range(maxk+1):
            if k:
                d[m]=k
            rec(m+1, remN-k*m, remR-k, d)
            if k:
                del d[m]
    rec(1,N,R,{})
    return out

def profile_weight(p):
    w=1
    for m,k in p.items():
        w *= comb(Iq(2,m),k)
    return w

def falling(x,n):
    r=1
    for t in range(n):
        r *= x-t
    return r

def degree_list(p):
    out=[]
    for m in sorted(p):
        out += [m]*p[m]
    return out

def inj_sum(degs,sizes):
    r=len(sizes)
    total=0
    for js in permutations(range(len(degs)),r):
        z=1
        for a,j in enumerate(js):
            z *= falling(degs[j],sizes[a])
        total += z
    return total

def Z_and_profiles(N):
    ps=profiles_fixed(N)
    return sum(profile_weight(p) for p in ps), ps

def specified_partition_probability(N,sizes):
    Z,ps=Z_and_profiles(N)
    check(Z>0, f"conditioning class nonempty N={N}")
    b=sum(sizes)
    num=0
    for p in ps:
        num += profile_weight(p)*inj_sum(degree_list(p),sizes)
    den=falling(N,b)*Z
    return Fraction(num,den)

# Product-GF DP gives the same Z_N,R.
def Z_dp(N,R=R):
    # coeffs z^n u^r of product_m (1+u z^m)^{I_2(m)}
    dp=[[0]*(R+1) for _ in range(N+1)]
    dp[0][0]=1
    for m in range(1,N+1):
        I=Iq(2,m)
        ndp=[[0]*(R+1) for _ in range(N+1)]
        for n in range(N+1):
            for r in range(R+1):
                if not dp[n][r]:
                    continue
                for k in range(0,min(I,R-r,(N-n)//m)+1):
                    ndp[n+k*m][r+k] += dp[n][r]*comb(I,k)
        dp=ndp
    return dp[N][R]

Zvals={}
for N in range(6,31):
    Z,ps=Z_and_profiles(N)
    Zvals[N]=Z
    check(Z==Z_dp(N), f"profile/OGF count match N={N}")
    if N < 14:
        check(Z==0, f"minimal degree barrier N={N}")
    else:
        check(Z>0, f"positive conditioning class N={N}")

check(Zvals[14]==3, "Z14=3")
check(Zvals[15]==12, "Z15=12")
check(Zvals[16]==49, "Z16=49")

# Direct enumeration at N=14,15 verifies actual squarefree-polynomial counts/profiles.
irreducibles=[]
for d in range(1,8):
    irreducibles += irreducibles_by_degree[d]

def factor_degrees_squarefree(f):
    original=gf2_deg(f)
    rem=f
    ds=[]
    for g in irreducibles:
        d=gf2_deg(g)
        if d > original//2:
            continue
        q,r=gf2_divmod(rem,g)
        if r==0:
            ds.append(d)
            rem=q
            q2,r2=gf2_divmod(rem,g)
            if r2==0:
                return None
    if rem != 1:
        check(irreducible_gf2(rem), f"leftover irreducible deg={gf2_deg(rem)}")
        ds.append(gf2_deg(rem))
    return tuple(sorted(ds))

for N,expected in [(14,3),(15,12)]:
    cnt=0
    prof={}
    for low in range(1<<N):
        f=(1<<N)|low
        ds=factor_degrees_squarefree(f)
        if ds is not None and len(ds)==R:
            cnt += 1
            prof[ds]=prof.get(ds,0)+1
    check(cnt==expected, f"direct squarefree count N={N}")

# Exact minimal-degree root profiles.
Z14,ps14=Z_and_profiles(14)
weighted14={tuple(degree_list(p)):profile_weight(p) for p in ps14}
check(weighted14=={(1,1,2,3,3,4):3}, "N14 deterministic degree multiset")
Z15,ps15=Z_and_profiles(15)
weighted15={tuple(degree_list(p)):profile_weight(p) for p in ps15}
check(weighted15=={
    (1,1,2,3,3,5):6,
    (1,1,2,3,4,4):6
}, "N15 exact profile weights")

# Restricted-growth strings enumerate all set partitions of [b].
def set_partitions(b):
    if b==0:
        yield ()
        return
    a=[0]*b
    def rec(i,mx):
        if i==b:
            blocks=[[] for _ in range(mx+1)]
            for idx,v in enumerate(a):
                blocks[v].append(idx)
            yield tuple(tuple(B) for B in blocks)
            return
        for v in range(mx+2):
            a[i]=v
            yield from rec(i+1,max(mx,v))
    a[0]=0
    yield from rec(1,0)

# Exact visible restriction probabilities normalize.
for N in range(14,24):
    for b in range(2,6):
        mass=Fraction(0,1)
        for pi in set_partitions(b):
            sizes=tuple(len(B) for B in pi)
            if len(sizes) <= R:
                mass += specified_partition_probability(N,sizes)
        check(mass==1, f"restriction normalization N={N} b={b}")

p11={}
for N in range(14,31):
    p=specified_partition_probability(N,(1,1))
    p11[N]=p
    check(0<p<=1, f"pair separation N={N}")

check(p11[14]==Fraction(6,7), "p11 N14")
check(p11[15]==Fraction(59,70), "p11 N15")
check(p11[16]==Fraction(4889,5880), "p11 N16")

# Root degree is exactly six under the conditioning, and the raw attempt is legal
# for delta_N=min(N^-2,p11/2).
for N in range(14,31):
    Z,ps=Z_and_profiles(N)
    for p in ps:
        check(sum(p.values())==6, f"root degree profile N={N}")
    delta=min(Fraction(1,N*N),p11[N]/2)
    attempt=delta/p11[N]
    check(0<attempt<=Fraction(1,2), f"attempt legality N={N}")

print("R11 I0054 C046 squarefree F2 six-factor fragmentation exact self-check")
print(f"ASSERTIONS={A}")
print("I2(1..14)=" + repr([Iq(2,m) for m in range(1,15)]))
print(f"Z14={Zvals[14]}; Z15={Zvals[15]}; Z16={Zvals[16]}")
print("N14_PROFILE=(1,1,2,3,3,4) WITH COUNT=3")
print("N15_PROFILES={(1,1,2,3,3,5):6,(1,1,2,3,4,4):6}")
print(f"P11_N14={p11[14]}; P11_N15={p11[15]}; P11_N16={p11[16]}")
print("ROOT_DEGREE=6 FOR EVERY CONDITIONED PROPOSAL")
print("ALL_EXACT_CHECKS_PASS")
