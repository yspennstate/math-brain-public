#!/usr/bin/env python3
from fractions import Fraction
from collections import Counter, defaultdict

ASSERTIONS = 0

def check(cond, msg=""):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def deg(p):
    return p.bit_length() - 1

def polymod(a, b):
    db = deg(b)
    while a and deg(a) >= db:
        a ^= b << (deg(a) - db)
    return a

def polydiv(a, b):
    q = 0
    db = deg(b)
    while a and deg(a) >= db:
        sh = deg(a) - db
        q ^= 1 << sh
        a ^= b << sh
    return q, a

def polymul(a,b):
    out=0
    while b:
        if b&1: out ^= a
        b >>=1
        a <<=1
    return out

def monic_polys(n):
    if n == 0:
        return [1]
    return [(1 << n) | low for low in range(1 << n)]

def mobius(n):
    x=n
    cnt=0
    p=2
    while p*p<=x:
        if x%p==0:
            x//=p; cnt+=1
            if x%p==0: return 0
            while x%p==0: x//=p
        p+=1
    if x>1: cnt+=1
    return -1 if cnt%2 else 1

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

MAXN=10
IRR=[]
IRR_BY_DEG=defaultdict(list)
for n in range(1,MAXN+1):
    for p in monic_polys(n):
        irreducible=True
        for g in IRR:
            if deg(g)>n//2:
                break
            if polymod(p,g)==0:
                irreducible=False
                break
        if irreducible:
            IRR.append(p)
            IRR_BY_DEG[n].append(p)

for n in range(1,MAXN+1):
    formula=sum(mobius(d)*(2**(n//d)) for d in divisors(n))//n
    check(len(IRR_BY_DEG[n])==formula, f"I_2({n})")

def factor_mult(p):
    if p==1:
        return []
    x=p
    fac=[]
    for g in IRR:
        if deg(g)>deg(x):
            break
        c=0
        while x != 1 and polymod(x,g)==0:
            x,rem=polydiv(x,g)
            check(rem==0, "division remainder")
            c+=1
        if c:
            fac.append((g,c))
        if x==1:
            break
    check(x==1, f"factorization failed {p}")
    rec=1
    degree_sum=0
    for g,c in fac:
        for _ in range(c):
            rec=polymul(rec,g)
            degree_sum += deg(g)
    check(rec==p, "reconstruction")
    check(degree_sum==deg(p), "degree sum")
    return fac

OMEGA_BY_N={}
SELECT_DIRECT={}
for N in range(0,MAXN+1):
    omega=[]
    direct=defaultdict(Fraction)
    polys=monic_polys(N)
    for f in polys:
        fac=factor_mult(f)
        occ=[]
        for g,c in fac:
            occ += [deg(g)]*c
        O=len(occ)
        if N==0:
            check(O==0)
        else:
            check(O>=1)
            for m in occ:
                direct[m]+=Fraction(1, (2**N)*O)
        omega.append(O)
    OMEGA_BY_N[N]=omega
    if N>=1:
        check(sum(direct.values(), Fraction(0))==1, f"direct degree dist N={N}")
    SELECT_DIRECT[N]=dict(direct)

def A(n,r):
    vals=OMEGA_BY_N[n]
    return sum((Fraction(1,r+o) for o in vals), Fraction(0))/len(vals)

# Exact dual identity for the uniform-first law.
for N in range(1,MAXN+1):
    via={}
    for m in range(1,N+1):
        v=Fraction(0)
        I=len(IRR_BY_DEG[m])
        for r in range(1,N//m+1):
            v += Fraction(I,2**(r*m))*A(N-r*m,r)
        via[m]=v
        check(v==SELECT_DIRECT[N].get(m,Fraction(0)),
              f"dual identity N={N} m={m}: {v} != {SELECT_DIRECT[N].get(m)}")
    check(sum(via.values(),Fraction(0))==1, f"dual normalization N={N}")

def fall(n,k):
    if k>n:
        return 0
    z=1
    for a in range(k):
        z*=n-a
    return z

def sprob(N,m,i,j):
    b=i+j
    return Fraction(
        fall(m,i)*fall(N-m,j)+fall(m,j)*fall(N-m,i),
        fall(N,b)
    )

def qsplit(N,i,j):
    return sum((pm*sprob(N,m,i,j) for m,pm in SELECT_DIRECT[N].items()), Fraction(0))

for N in range(2,MAXN+1):
    check(qsplit(N,1,1)>0)
    if N>=4:
        check(qsplit(N,2,2)>=0)
        check(qsplit(N,1,3)>=0)
    for b in range(2,min(N,6)+1):
        for i in range(1,b):
            j=b-i
            check(qsplit(N,i,j)==qsplit(N,j,i), f"split symmetry N={N} {i},{j}")

check(SELECT_DIRECT[4] == {
    1: Fraction(9,16),
    2: Fraction(1,8),
    3: Fraction(1,8),
    4: Fraction(3,16),
}, f"N=4 selected-degree law {SELECT_DIRECT[4]}")
check(qsplit(4,1,1)==Fraction(41,96))
check(qsplit(4,2,2)==Fraction(1,24))
check(qsplit(4,1,3)==Fraction(11,64))
check(qsplit(4,2,2)/qsplit(4,1,1)==Fraction(4,41))
check(qsplit(4,1,3)/qsplit(4,1,1)==Fraction(33,82))

# Independent reconstruction of the preceding C048 Palm-occurrence rates.
def I2(m):
    return len(IRR_BY_DEG[m])
def W(N,m):
    return I2(m)*sum((Fraction(1,2**(r*m)) for r in range(1,N//m+1)), Fraction(0))
def q_palm(N,i,j):
    return sum((W(N,m)*sprob(N,m,i,j) for m in range(1,N+1)), Fraction(0))
check(q_palm(4,1,1)==Fraction(61,48))
check(q_palm(4,2,2)==Fraction(5,48))
check(q_palm(4,1,3)==Fraction(17,32))
check(q_palm(4,2,2)/q_palm(4,1,1)==Fraction(5,61))
check(qsplit(4,2,2)/qsplit(4,1,1) != q_palm(4,2,2)/q_palm(4,1,1))
check(qsplit(4,1,3)/qsplit(4,1,1) != q_palm(4,1,3)/q_palm(4,1,1))

for N in range(1,MAXN+1):
    cnt=Counter(OMEGA_BY_N[N])
    total_occ=sum(o*c for o,c in cnt.items())
    total_from_W=sum(W(N,m) for m in range(1,N+1))*2**N
    check(Fraction(total_occ,1)==total_from_W, f"Palm first moment N={N}")
    check(sum(cnt.values())==2**N)

print("N=4 selected_degree=", {m:str(v) for m,v in sorted(SELECT_DIRECT[4].items())})
print("N=4 p11=", qsplit(4,1,1))
print("N=4 p22=", qsplit(4,2,2))
print("N=4 p13=", qsplit(4,1,3))
print("N=4 normalized_p22=", qsplit(4,2,2)/qsplit(4,1,1))
print("N=4 normalized_p13=", qsplit(4,1,3)/qsplit(4,1,1))
print("C048 normalized_q22=", q_palm(4,2,2)/q_palm(4,1,1))
print("C048 normalized_q13=", q_palm(4,1,3)/q_palm(4,1,1))
for N in range(4,MAXN+1):
    p11=qsplit(N,1,1)
    print("diag",N,
          "p11",p11,
          "r22",qsplit(N,2,2)/p11,
          "r13",qsplit(N,1,3)/p11)
print("ASSERTIONS=",ASSERTIONS)
print("ALL_EXACT_CHECKS_PASS")
