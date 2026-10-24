from itertools import combinations, permutations
from fractions import Fraction

# RSK for a partial permutation (rook placement), with x-labels in Q and y-labels in P.
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
        if sx>0 or sy>0: return False
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
            if is_shadow(T,n): out.append(T)
    return out

def first_pointwise_failure(limit=5):
    expected={2:[1,1],3:[1,4,1],4:[1,9,13,1],5:[1,16,61,41,1]}
    for n in range(2,limit+1):
        levels=[valid_sets(n,r) for r in range(n)]
        counts=[len(x) for x in levels]
        assert counts==expected[n], ('SHADOW_COUNT_FAIL',n,counts)
        ec=[{S:len(extensions(S,n)) for S in levels[r]} for r in range(n)]
        for r in range(n-1):
            for S in levels[r]:
                qS=Fraction(ec[r][S],(n-r)**2)
                for T in extensions(S,n):
                    if r+1==n: continue
                    qT=Fraction(ec[r+1][T],(n-r-1)**2) if n-r-1 else Fraction(0)
                    if qT>qS:
                        return n,r,S,T,qS,qT,ec[r][S],ec[r+1][T]
    return None

print('P0282 exact falsification of pointwise normalized shadow-extension monotonicity')
f=first_pointwise_failure(5)
assert f is not None
n,r,S,T,qS,qT,eS,eT=f
assert n==5 and r==1
assert S==frozenset({(3,4)}) and T==frozenset({(3,4),(2,5)})
assert qS==Fraction(7,16) and qT==Fraction(4,9)
print('all inclusion edges for n=2,3,4: no failure')
print('first_failure_n=5 rank_parent=1')
print('S={(3,4)} valid_extensions=7 ambient_extensions=16 qS=7/16')
print('T={(2,5),(3,4)} valid_extensions=4 ambient_extensions=9 qT=4/9')
print('strict_failure: 4/9 > 7/16 because 64>63')
print('shadow_counts_n5=[1,16,61,41,1]')
print('ALL_EXACT_CHECKS_PASS')
