from itertools import combinations, permutations
from fractions import Fraction

# Exact Viennot-shadow enumerator, matching the retained RSK/shadow convention.
def rsk_partial(R):
    P=[]; Q=[]
    for x,y in sorted(R):
        v=y; row=0
        while True:
            if row==len(P):
                P.append([v]); Q.append([x]); break
            a=P[row]
            pos=next((i for i,z in enumerate(a) if z>v),len(a))
            if pos==len(a):
                a.append(v); Q[row].append(x); break
            a[pos],v=v,a[pos]
            row+=1
    return P,Q

def is_shadow(R,n):
    P,Q=rsk_partial(R)
    usedx={x for x,y in R}; usedy={y for x,y in R}
    firstQ=set(Q[0] if Q else []); firstP=set(P[0] if P else [])
    sx=sy=0
    for i in range(1,n+1):
        sx += 1 if i in firstQ else (-1 if i not in usedx else 0)
        sy += 1 if i in firstP else (-1 if i not in usedy else 0)
        if sx>0 or sy>0:
            return False
    return True

def matchings(n,r):
    for xs in combinations(range(1,n+1),r):
        for ys in combinations(range(1,n+1),r):
            for yp in permutations(ys):
                yield frozenset(zip(xs,yp))

def valid_sets(n,r):
    return [S for S in matchings(n,r) if is_shadow(S,n)]

def extensions(S,n):
    ux={x for x,y in S}; uy={y for x,y in S}; out=[]
    for x in range(1,n+1):
        if x in ux: continue
        for y in range(1,n+1):
            if y in uy: continue
            T=S|{(x,y)}
            if is_shadow(T,n):
                out.append(T)
    return out

expected={
    2:[1,1],
    3:[1,4,1],
    4:[1,9,13,1],
    5:[1,16,61,41,1],
    6:[1,25,181,381,131,1],
}
levels={}
ec={}
for n in range(2,7):
    levels[n]=[valid_sets(n,r) for r in range(n)]
    counts=[len(x) for x in levels[n]]
    assert counts==expected[n], ("SHADOW_COUNT_FAIL",n,counts)
    ec[n]=[{S:len(extensions(S,n)) for S in levels[n][r]} for r in range(n)]

def rank_stats(n,r):
    L=levels[n][r]
    e=ec[n][r]
    q={S:Fraction(e[S],(n-r)**2) for S in L}
    a={}
    for S in L:
        kids=extensions(S,n)
        if kids:
            a[S]=sum(Fraction(ec[n][r+1][T],(n-r-1)**2) for T in kids)/len(kids)
        else:
            a[S]=Fraction(0)
    Eq=sum(q.values(),Fraction(0))/len(L)
    Ee=sum(Fraction(e[S]) for S in L)/len(L)
    Ea=sum(a.values(),Fraction(0))/len(L)
    Eea=sum(Fraction(e[S])*a[S] for S in L)/len(L)
    cov=Eea-Ee*Ea
    child=levels[n][r+1]
    child_mean=sum(Fraction(ec[n][r+1][T],(n-r-1)**2) for T in child)/len(child)
    # Exact edge-size-bias identity.
    assert child_mean==Eea/Ee
    return Eq,Ee,Ea,Eea,cov,child_mean,a

# First obstruction to the tempting negative-covariance strengthening.
Eq,Ee,Ea,Eea,cov,child_mean,a=rank_stats(4,1)
assert cov==Fraction(8,243) and cov>0
assert Eq==Fraction(26,81)
assert child_mean==Fraction(3,52)

# First parentwise averaged-regression obstruction in the checked n<=6 range.
first=None
for n in range(2,7):
    for r in range(n-1):
        Eq,Ee,Ea,Eea,cov,child_mean,a=rank_stats(n,r)
        for S in levels[n][r]:
            if a[S]>Eq:
                first=(n,r,S,ec[n][r][S],a[S],Eq,child_mean)
                break
        if first:
            break
    if first:
        break

assert first is not None
n,r,S,eS,aS,Eq,child_mean=first
assert n==6 and r==3
assert S==frozenset({(2,6),(3,5),(5,3)})
assert eS==3
assert aS==Fraction(1,6)
assert Eq==Fraction(524,3429)
assert child_mean==Fraction(5,524)
assert aS>Eq
assert child_mean<Eq

print("P0282 exact averaged-shadow regression falsifier")
print("shadow_counts_n2_to_n6=PASS")
print("edge_size_bias_identity=PASS for all ranks n=2..6")
print("negative_covariance_shortcut_fails_at_n4_r1=True")
print("cov_uniform_parent_e_vs_child_average_n4_r1=8/243 > 0")
print("mean_q_parent_n4_r1=26/81 child_global_mean_q=3/52")
print("first_parentwise_average_domination_failure_n6_r3=True")
print("S={(2,6),(3,5),(5,3)} eS=3")
print("child_average_q_from_S=1/6")
print("global_parent_mean_q=524/3429")
print("strict_failure: 1/6 > 524/3429")
print("actual_child_global_mean_q=5/524 < 524/3429")
print("interpretation=local negative-regression strengthenings are false; the desired rank-average inequality requires global compensation")
print("ALL_EXACT_CHECKS_PASS")
