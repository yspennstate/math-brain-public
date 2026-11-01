from itertools import combinations
from functools import lru_cache
from collections import Counter

def tc_from_mask(n, mask):
    rows=[0]*n; idx=0
    for i in range(n):
        for j in range(i+1,n):
            if mask>>idx & 1: rows[i] |= 1<<j
            idx += 1
    changed=True
    while changed:
        changed=False
        for i in range(n):
            rr=rows[i]; x=rows[i]
            while x:
                b=x & -x; j=b.bit_length()-1; x-=b
                rr |= rows[j]
            if rr != rows[i]:
                rows[i]=rr; changed=True
    return tuple(rows)

def all_nat_posets(n):
    seen=set()
    for mask in range(1 << (n*(n-1)//2)):
        r=tc_from_mask(n,mask)
        if r not in seen:
            seen.add(r); yield r

def lt(R,i,j): return bool(R[i]>>j & 1)
def comparable(R,i,j): return i==j or lt(R,i,j) or lt(R,j,i)
def inc(R,i,j): return i!=j and not comparable(R,i,j)

def width(R):
    n=len(R); ans=0
    for mask in range(1,1<<n):
        k=mask.bit_count()
        if k<=ans: continue
        X=[i for i in range(n) if mask>>i & 1]
        if all(inc(R,a,b) for a,b in combinations(X,2)): ans=k
    return ans

def inc_components(R, removed=None):
    V=[i for i in range(len(R)) if i!=removed]
    unseen=set(V); comps=[]
    while unseen:
        s=next(iter(unseen)); unseen.remove(s); C={s}; stack=[s]
        while stack:
            u=stack.pop()
            ns=[v for v in list(unseen) if inc(R,u,v)]
            for v in ns:
                unseen.remove(v); C.add(v); stack.append(v)
        comps.append(tuple(sorted(C)))
    return comps

def comp_before(R,A,B):
    return all(lt(R,a,b) for a in A for b in B)

def ordered_inc_components(R, removed=None):
    cs=inc_components(R,removed)
    if len(cs)<=1: return cs
    # distinct incomparability components are uniformly comparable; sort by one representative
    return sorted(cs,key=lambda C: sum(1 for D in cs if D!=C and comp_before(R,D,C)))

def is_inc_connected(R): return len(inc_components(R))==1

def linear_extensions(R, subset=None):
    n=len(R)
    S=(1<<n)-1 if subset is None else sum(1<<i for i in subset)
    pred=[0]*n
    for i in range(n):
        for j in range(n):
            if lt(R,j,i): pred[i]|=1<<j
    out=[]
    def rec(mask,pfx):
        if mask==S: out.append(tuple(pfx)); return
        for v in range(n):
            if not (S>>v)&1 or (mask>>v)&1: continue
            if pred[v] & S & ~mask == 0:
                rec(mask|1<<v,pfx+[v])
    rec(0,[]); return out

def prob_count(exts,a,b): return sum(e.index(a)<e.index(b) for e in exts)

def check_component_order(R,cs):
    for i in range(len(cs)):
        for j in range(i+1,len(cs)):
            assert comp_before(R,cs[i],cs[j])

def allowed_insertions(R,v,lam):
    ans=[]
    for p in range(len(lam)+1):
        e=lam[:p]+(v,)+lam[p:]
        pos={x:i for i,x in enumerate(e)}
        if all(not lt(R,a,b) or pos[a]<pos[b] for a in range(len(R)) for b in range(len(R))):
            ans.append(p)
    return ans

def restrict_tuple(e,S):
    S=set(S); return tuple(x for x in e if x in S)

stats=Counter()
for n in range(2,7):
    for R in all_nat_posets(n):
        stats['posets']+=1
        if width(R)>3: continue
        stats['width_le3']+=1
        if not is_inc_connected(R): continue
        stats['inc_connected']+=1
        for v in range(n):
            cs=ordered_inc_components(R,v)
            if len(cs)<=1: continue
            stats['inc_cut_states']+=1
            check_component_order(R,cs)
            # connectivity of Inc(P) means v has an incomparable neighbour in each component
            assert all(any(inc(R,v,q) for q in C) for C in cs)
            # boundary localization
            for i,C in enumerate(cs):
                if i>0: assert all(not lt(R,q,v) for q in C)
                if i<len(cs)-1: assert all(not lt(R,v,q) for q in C)
            # every interior component is entirely incomparable with v
            for C in cs[1:-1]:
                assert all(inc(R,v,q) for q in C)
                stats['interior_components_checked']+=1
                if len(C)>1: stats['nontrivial_interior']+=1
            # exact uniform marginal on each interior component under full extensions of P
            if cs[1:-1]:
                full=linear_extensions(R)
                for C in cs[1:-1]:
                    marg=Counter(restrict_tuple(e,C) for e in full)
                    local=linear_extensions(R,C)
                    assert set(marg)==set(local)
                    vals=set(marg.values())
                    assert len(vals)==1
            # singleton-corridor gap law
            if cs[1:-1] and all(len(C)==1 for C in cs[1:-1]):
                stats['singleton_corridor_states']+=1
                z=[C[0] for C in cs[1:-1]]
                if len(z)>=2:
                    full=linear_extensions(R); E=len(full)
                    W=len(linear_extensions(R,cs[0]))*len(linear_extensions(R,cs[-1]))
                    for a,b in zip(z,z[1:]):
                        assert lt(R,a,b)
                        diff=prob_count(full,v,b)-prob_count(full,v,a)
                        assert diff==W
                        stats['universal_gaps_checked']+=1
                    assert E >= (len(z)+1)*W

# Five-point adversary to the stronger false shortcut "a cut vertex must itself have a balanced pair".
# Covers: 0<3,0<4,1<2,1<4,2<3.
n=5
covers=[(0,3),(0,4),(1,2),(1,4),(2,3)]
R=[0]*n
for a,b in covers: R[a]|=1<<b
changed=True
while changed:
    changed=False
    for i in range(n):
        rr=R[i]; x=R[i]
        while x:
            bb=x & -x; j=bb.bit_length()-1; x-=bb; rr|=R[j]
        if rr!=R[i]: R[i]=rr; changed=True
R=tuple(R)
assert width(R)==2 and is_inc_connected(R)
v=2; cs=ordered_inc_components(R,v)
assert cs==[(0,1),(3,4)]
exts=linear_extensions(R); E=len(exts)
assert E==8
assert prob_count(exts,v,0)==2
assert prob_count(exts,v,4)==6
assert prob_count(exts,0,1)==3
assert prob_count(exts,3,4)==3

print('POS3_ARTICULATION_CORRIDOR_V1_PASS')
for k in ['posets','width_le3','inc_connected','inc_cut_states','interior_components_checked','nontrivial_interior','singleton_corridor_states','universal_gaps_checked']:
    print(f'{k}={stats[k]}')
print('adversary_covers=' + ','.join(f'({a},{b})' for a,b in covers))
print(f'adversary_E={E}')
print(f'articulation_v={v}')
print(f'N(v<0)={prob_count(exts,v,0)}')
print(f'N(v<4)={prob_count(exts,v,4)}')
print(f'balanced_elsewhere_N(0<1)={prob_count(exts,0,1)}')
print(f'balanced_elsewhere_N(3<4)={prob_count(exts,3,4)}')
