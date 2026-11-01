from fractions import Fraction as F
from itertools import combinations
from math import comb

ASSERTIONS = 0

def check(cond, msg="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def H(n):
    return sum((F(1,j) for j in range(1,n+1)), F(0))

def D(K):
    if K <= 1:
        return 0
    return sum(comb(K,m)*(2**(m-1)-1) for m in range(2,K+1))

for K in range(1,10):
    check(2*D(K) == 3**K - 2**(K+1) + 1)

def coords_for(K):
    leaves=tuple(range(K))
    out=[]
    for m in range(2,K+1):
        for Vt in combinations(leaves,m):
            V=set(Vt)
            root=min(V)
            rest=sorted(V-{root})
            for mask in range(1<<(m-1)):
                A={root}
                for j,x in enumerate(rest):
                    if (mask>>j)&1:
                        A.add(x)
                if A==V:
                    continue
                B=V-A
                out.append((tuple(sorted(V)),tuple(sorted(A)),tuple(sorted(B))))
    check(len(out)==D(K))
    return out

def contrib_for_translation(p,d,coord,t):
    Vt,At,Bt=coord
    V=set(Vt); A=set(At); B=set(Bt)
    reps={ell:pow((t+ell)%p,d,p) for ell in V}
    q=F(0)
    for u in range(1,p):
        red={ell for ell,v in reps.items() if v<u}
        if red==A or red==B:
            q += F(p,2*u*(p-u))
    return q

def vector_for_subset(p,d,K,S):
    cs=coords_for(K)
    L=len(S)
    vals=[]
    for c in cs:
        vals.append(sum((contrib_for_translation(p,d,c,t) for t in S),F(0))/L)
    return cs, vals

def root_rates(N,p,d,S):
    V=tuple(range(N))
    cs=[]
    rest=list(range(1,N))
    for mask in range(0,(1<<(N-1))-1):
        A={0}
        for j,x in enumerate(rest):
            if (mask>>j)&1:
                A.add(x)
        B=set(V)-A
        cs.append((V,tuple(sorted(A)),tuple(sorted(B))))
    vals=[sum((contrib_for_translation(p,d,c,t) for t in S),F(0))/len(S) for c in cs]
    return cs,vals

p,d=5,3
S=(0,1)
cs, vals=root_rates(4,p,d,S)

singleton=[]
balanced=[]
for (_,A,B),v in zip(cs,vals):
    a,b=len(A),len(B)
    if sorted((a,b))==[1,3]:
        singleton.append(v)
    elif a==2 and b==2:
        balanced.append(v)

check(sorted(singleton)==sorted([F(25,48),F(5,16),F(5,24),F(0)]))
check(sorted(balanced)==sorted([F(5,24),F(5,24),F(0)]))
check(any(v==0 for v in singleton))
check(any(v==0 for v in balanced))
source_single=F(1,3)
source_bal=F(1,6)
check(source_single>0)
check(source_bal>0)

total=sum(vals,F(0))
balanced_total=sum(balanced,F(0))
check(total==F(35,24))
check(balanced_total==F(5,12))
check(balanced_total/total==F(2,7))

proposal=sum((F(p,2*len(S)*u*(p-u)) for t in S for u in range(1,p)),F(0))
check(proposal==H(p-1))

def Lp(p,r):
    return H(r)-H(p-1-r)

def pair_rate(p,d,a,b,t):
    x=pow((t+a)%p,d,p); y=pow((t+b)%p,d,p)
    lo,hi=sorted((x,y))
    return sum((F(p,2*u*(p-u)) for u in range(lo+1,hi+1)),F(0))

for p,d in [(5,3),(7,5),(11,3)]:
    vals_perm=[pow(x,d,p) for x in range(p)]
    check(len(set(vals_perm))==p)
    M=sum((Lp(p,r)**2 for r in range(p)),F(0))/p
    check(M < 8)
    for a,b in combinations(range(min(p,6)),2):
        rs=[]
        for t in range(p):
            r=pair_rate(p,d,a,b,t)
            x=pow((t+a)%p,d,p); y=pow((t+b)%p,d,p)
            check(r==F(1,2)*abs(Lp(p,y)-Lp(p,x)))
            rs.append(r)
        mean2=sum((r*r for r in rs),F(0))/p
        check(mean2 <= M)

for K in [2,3,4]:
    for c in coords_for(K):
        V,A,B=c
        a=A[0]; b=B[0]
        for t in range(5):
            g=contrib_for_translation(5,3,c,t)
            r=pair_rate(5,3,a,b,t)
            check(g<=r)

cs3=coords_for(3)
full=[sum((contrib_for_translation(5,3,c,t) for t in range(5)),F(0))/5 for c in cs3]
for idx,c in enumerate(cs3):
    population=[contrib_for_translation(5,3,c,t) for t in range(5)]
    mu=full[idx]
    popvar=sum(((x-mu)**2 for x in population),F(0))/5
    pop2=sum((x*x for x in population),F(0))/5
    check(pop2 < 8)
    for L in [2,3]:
        subset_means=[]
        for T in combinations(range(5),L):
            subset_means.append(sum((population[t] for t in T),F(0))/L)
        var=sum(((x-mu)**2 for x in subset_means),F(0))/len(subset_means)
        expected=F(5-L, L*(5-1))*popvar
        check(var==expected)
        check(var<=F(8,L))

sporadic={}
for K in [2,3]:
    _, fullv=vector_for_subset(5,3,K,tuple(range(5)))
    matches=[]
    for L in range(1,6):
        for T in combinations(range(5),L):
            _,v=vector_for_subset(5,3,K,T)
            if v==fullv:
                matches.append(T)
    sporadic[K]=matches
    check(matches==[(0,1,2,3,4)])

print("R11-I0054-U054/C075 exact self-check")
print("ASSERTIONS="+str(ASSERTIONS))
print("D_1="+str(D(1))+" D_2="+str(D(2))+" D_3="+str(D(3))+" D_4="+str(D(4)))
print("C075_N4_support="+",".join(map(str,S)))
print("C075_N4_singleton_multiset="+",".join(str(x) for x in sorted(singleton)))
print("C075_N4_balanced_multiset="+",".join(str(x) for x in sorted(balanced)))
print("C075_N4_total_root_rate="+str(total))
print("C075_N4_balanced_probability="+str(balanced_total/total))
print("source_CTCS_N4_singleton_each="+str(source_single))
print("source_CTCS_N4_balanced_each="+str(source_bal))
print("proposal_rate="+str(proposal)+" H4="+str(H(4)))
print("sporadic_exact_K2="+repr(sporadic[2]))
print("sporadic_exact_K3="+repr(sporadic[3]))
print("ALL_EXACT_CHECKS_PASS")
