from fractions import Fraction
from itertools import permutations, combinations
import math

ASSERTIONS = 0

def check(cond, msg=""):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def H(n):
    return sum(Fraction(1,r) for r in range(1,n+1))

def beta(i,j):
    return Fraction(math.factorial(i-1)*math.factorial(j-1), math.factorial(i+j-1))

def all_unordered_splits(labels):
    labels=list(labels)
    root=labels[0]
    allset=set(labels)
    out=[]
    for r in range(1,len(labels)):
        for At in combinations(labels,r):
            A=set(At)
            if root not in A:
                continue
            B=allset-A
            if B:
                out.append((tuple(sorted(A)),tuple(sorted(B))))
    return out

def rate_for_split(N, perm, A, B):
    total=Fraction(0)
    for u in range(1,N):
        cnt=0
        for t in range(N):
            def red(l):
                return perm[(t+l)%N] <= u
            pat1 = all(red(a) for a in A) and all(not red(b) for b in B)
            pat2 = all(red(b) for b in B) and all(not red(a) for a in A)
            cnt += int(pat1 or pat2)
        total += Fraction(cnt, 2*u*(N-u))
    return total

def swap_perm(p,a,b):
    p=list(p)
    p[a],p[b]=p[b],p[a]
    return tuple(p)

# A. Exact expectation identity E_rho Q_rho(A|B)=B(i,j),
# exhaustively for N <= 6 and all unordered split tests on first m<=4 labels.
for N in range(3,7):
    plist=list(permutations(range(1,N+1)))
    for m in range(2,min(4,N)+1):
        for A,B in all_unordered_splits(range(m)):
            s=sum(rate_for_split(N,p,A,B) for p in plist)
            avg=s/Fraction(len(plist),1)
            check(avg==beta(len(A),len(B)),
                  ("expectation",N,A,B,avg,beta(len(A),len(B))))

# B. Exact transposition sensitivity bound
# |Delta Q| <= 2m H_{N-1}/N.
for N in range(3,7):
    splits=[]
    for m in range(2,min(4,N)+1):
        splits.extend(all_unordered_splits(range(m)))
    for p in permutations(range(1,N+1)):
        for a,b in combinations(range(N),2):
            pp=swap_perm(p,a,b)
            for A,B in splits:
                lhs=abs(rate_for_split(N,p,A,B)-rate_for_split(N,pp,A,B))
                rhs=Fraction(2*(len(A)+len(B)),N)*H(N-1)
                check(lhs<=rhs, ("transposition",N,p,a,b,A,B,lhs,rhs))

# C. Finite pair separability for every permutation through N=7.
for N in range(2,8):
    for p in permutations(range(1,N+1)):
        for a,b in combinations(range(N),2):
            found=False
            for t in range(N):
                ra=p[(t+a)%N]
                rb=p[(t+b)%N]
                if ra!=rb:
                    u=min(ra,rb)
                    if u < max(ra,rb):
                        found=True
                        break
            check(found, ("pair-separability",N,p,a,b))

# D. C069 finite witness at N=4 with identity ranking.
N=4
p=(1,2,3,4)
rates={}
for A,B in all_unordered_splits(range(N)):
    rates[(A,B)] = rate_for_split(N,p,A,B)

singleton = sorted(v for (A,B),v in rates.items() if {len(A),len(B)}=={1,3})
balanced = sorted(v for (A,B),v in rates.items() if len(A)==len(B)==2)
check(singleton == [Fraction(1,3)]*4, ("singleton",singleton))
check(balanced == [Fraction(0),Fraction(1,4),Fraction(1,4)], ("balanced",balanced))
check(sum(rates.values()) == Fraction(11,6), ("root total",sum(rates.values())))
check(balanced != [Fraction(1,6)]*3, "source CTCS balanced multiset")
check(balanced != [Fraction(7,30)]*3, "C068 balanced multiset")

# E. The threshold-u=1 orbit is not exact strength 2: every mask has exactly one red label.
for N in range(3,9):
    p=tuple(range(1,N+1))
    for t in range(N):
        reds=[ell for ell in range(N) if p[(t+ell)%N] <= 1]
        check(len(reds)==1, ("u=1 one-red",N,t,reds))
    rr=0
    for t in range(N):
        if p[t] <= 1 and p[(t+1)%N] <= 1:
            rr += 1
    check(rr==0, ("not strength2",N,rr))

print("R11-I0054-U048/C069 exact self-check")
print("ASSERTIONS={}".format(ASSERTIONS))
print("N4_singleton_multiset={}".format(",".join(str(x) for x in singleton)))
print("N4_balanced_multiset={}".format(",".join(str(x) for x in balanced)))
print("N4_total_root_rate={}".format(sum(rates.values())))
print("source_CTCS_N4_balanced_each=1/6")
print("C068_N4_balanced_each=7/30")
print("u1_exact_strength2=FALSE")
print("ALL_EXACT_CHECKS_PASS")
