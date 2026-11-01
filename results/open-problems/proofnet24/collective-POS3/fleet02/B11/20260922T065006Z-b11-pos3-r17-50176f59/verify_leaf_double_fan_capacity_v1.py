from itertools import combinations
from functools import lru_cache
from fractions import Fraction
from collections import Counter

def closure_from_mask(n, mask):
    rows=[0]*n
    k=0
    for i in range(n):
        for j in range(i+1,n):
            if (mask>>k)&1:
                rows[i] |= 1<<j
            k+=1
    for i in range(n-1,-1,-1):
        bits=rows[i]
        for j in range(i+1,n):
            if (bits>>j)&1:
                bits |= rows[j]
        rows[i]=bits
    return tuple(rows)

def all_nat_posets(n):
    m=n*(n-1)//2
    return sorted({closure_from_mask(n,mask) for mask in range(1<<m)})

def lt(rows,a,b):
    return bool((rows[a]>>b)&1)

def comp(rows,a,b):
    return lt(rows,a,b) or lt(rows,b,a)

def induced(rows, vertices):
    vv=list(vertices)
    out=[0]*len(vv)
    for i,a in enumerate(vv):
        for j,b in enumerate(vv):
            if lt(rows,a,b):
                out[i] |= 1<<j
    return tuple(out)

@lru_cache(None)
def le_count(rows):
    n=len(rows)
    pred=[0]*n
    for i in range(n):
        for j in range(n):
            if lt(rows,i,j):
                pred[j] |= 1<<i
    dp=[0]*(1<<n)
    dp[0]=1
    for S in range(1<<n):
        if not dp[S]:
            continue
        for x in range(n):
            if not ((S>>x)&1) and pred[x]&~S==0:
                dp[S|1<<x] += dp[S]
    return dp[-1]

def extensions(rows):
    n=len(rows)
    pred=[0]*n
    for i in range(n):
        for j in range(n):
            if lt(rows,i,j):
                pred[j] |= 1<<i
    ans=[]
    def rec(S, seq):
        if len(seq)==n:
            ans.append(tuple(seq))
            return
        for x in range(n):
            if not ((S>>x)&1) and pred[x]&~S==0:
                rec(S|1<<x, seq+(x,))
    rec(0,())
    return ans

def width(rows):
    n=len(rows)
    best=0
    for mask in range(1,1<<n):
        if mask.bit_count()<=best:
            continue
        vv=[i for i in range(n) if (mask>>i)&1]
        if all(not comp(rows,a,b) for a,b in combinations(vv,2)):
            best=len(vv)
    return best

def pair_count(exts,a,b):
    return sum(e.index(a)<e.index(b) for e in exts)

def covers(rows):
    n=len(rows)
    out=[]
    for a in range(n):
        for b in range(n):
            if lt(rows,a,b) and not any(z not in (a,b) and lt(rows,a,z) and lt(rows,z,b) for z in range(n)):
                out.append((a,b))
    return out

def graph_connected(rows, comparable_graph):
    n=len(rows)
    adj=[[] for _ in range(n)]
    for a,b in combinations(range(n),2):
        edge=comp(rows,a,b) if comparable_graph else not comp(rows,a,b)
        if edge:
            adj[a].append(b); adj[b].append(a)
    seen={0}; todo=[0]
    while todo:
        v=todo.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w); todo.append(w)
    return len(seen)==n

stats=Counter()
witness=None

for n in range(2,7):
    posets=all_nat_posets(n)
    stats["natural_posets"] += len(posets)
    for rows in posets:
        if width(rows)>3:
            continue
        stats["width_le3"] += 1
        exts=extensions(rows)
        E=len(exts)
        for x in range(n):
            inc=[b for b in range(n) if b!=x and not comp(rows,x,b)]
            if len(inc)!=1:
                continue
            b=inc[0]
            stats["leaf_states"] += 1
            D=[z for z in range(n) if lt(rows,z,x)]
            U=[z for z in range(n) if lt(rows,x,z)]
            d=le_count(induced(rows,D)) if D else 1
            u=le_count(induced(rows,U)) if U else 1
            l=le_count(induced(rows,D+[b]))
            r=le_count(induced(rows,U+[b]))
            N_bx=pair_count(exts,b,x)
            assert N_bx == l*u
            assert E-N_bx == d*r
            Acap=Fraction(l,d)
            Bcap=Fraction(r,u)
            assert Fraction(N_bx,E) == Acap/(Acap+Bcap)
            I=[z for z in D if not lt(rows,z,b)]
            assert all(not comp(rows,z,b) for z in I)
            for i in I:
                for z in D:
                    if lt(rows,i,z):
                        assert z in I
            T=[i for i in I if not any(lt(rows,i,j) for j in I if j!=i)]
            assert len(T)<=2
            for t in T:
                assert not any(z not in (t,x) and lt(rows,t,z) and lt(rows,z,x) for z in range(n))
            reverse_union=sum(1 for e in exts if any(e.index(b)<e.index(t) for t in T))
            assert reverse_union == (l-d)*u
            if 3*N_bx <= 2*E:
                continue
            stats["strong_b_before_x"] += 1
            assert Acap > 2*Bcap
            assert 3*reverse_union > E
            strict_descent=any(3*pair_count(exts,b,z)>2*E for z in I)
            T_balanced=[t for t in T if E <= 3*pair_count(exts,b,t) <= 2*E]
            if strict_descent:
                stats["strict_span_descent"] += 1
                continue
            stats["no_strict_span_descent"] += 1
            if T_balanced:
                stats["balanced_T_channel"] += 1
                continue
            stats["hard_local_leaf_states"] += 1
            assert len(T)==2
            vals=[pair_count(exts,b,t) for t in T]
            assert all(3*v<E for v in vals)
            assert 3*reverse_union>E
            assert 6*max(vals)>E
            if graph_connected(rows,True) and graph_connected(rows,False):
                stats["hard_local_biconnected"] += 1
            if witness is None and graph_connected(rows,True) and graph_connected(rows,False):
                balanced=[(a,c,pair_count(exts,a,c)) for a,c in combinations(range(n),2) if not comp(rows,a,c) and E <= 3*pair_count(exts,a,c) <= 2*E]
                witness={"n":n,"covers":covers(rows),"x":x,"b":b,"E":E,"T":T,"channel_counts":vals,"reverse_union":reverse_union,"leaf_count_b_before_x":N_bx,"balanced_pairs":balanced}

print("natural_posets",stats["natural_posets"])
print("width_le3",stats["width_le3"])
print("leaf_states",stats["leaf_states"])
print("strong_b_before_x",stats["strong_b_before_x"])
print("no_strict_span_descent",stats["no_strict_span_descent"])
print("balanced_T_channel",stats["balanced_T_channel"])
print("hard_local_leaf_states",stats["hard_local_leaf_states"])
print("hard_local_biconnected",stats["hard_local_biconnected"])
print("witness",witness)
print("POS3_LEAF_DOUBLE_FAN_CAPACITY_V1_PASS")
