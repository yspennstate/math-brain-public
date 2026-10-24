#!/usr/bin/env python3
from itertools import combinations, product
from functools import lru_cache
from fractions import Fraction
from collections import Counter
from math import comb

ONE_THIRD = Fraction(1,3)
TWO_THIRDS = Fraction(2,3)

def transitive_closure(rel):
    n=len(rel)
    rel=[row[:] for row in rel]
    for k in range(n):
        for i in range(n):
            if rel[i][k]:
                for j in range(n):
                    if rel[k][j]:
                        rel[i][j]=True
    return rel

def closure_from_mask(n, mask):
    pairs=list(combinations(range(n),2))
    rel=[[False]*n for _ in range(n)]
    for k,(i,j) in enumerate(pairs):
        if (mask>>k)&1:
            rel[i][j]=True
    rel=transitive_closure(rel)
    sig=0
    for k,(i,j) in enumerate(pairs):
        if rel[i][j]:
            sig |= 1<<k
    return sig,rel

def natural_posets(n):
    seen=set()
    for mask in range(1<<(n*(n-1)//2)):
        sig,rel=closure_from_mask(n,mask)
        if sig in seen:
            continue
        seen.add(sig)
        yield sig,rel

def dp_counter(rel):
    n=len(rel)
    pred=[0]*n
    for j in range(n):
        m=0
        for i in range(n):
            if rel[i][j]:
                m |= 1<<i
        pred[j]=m
    @lru_cache(None)
    def f(mask):
        if mask==(1<<n)-1:
            return 1
        ans=0
        for x in range(n):
            if not ((mask>>x)&1) and (pred[x] & ~mask)==0:
                ans += f(mask | (1<<x))
        return ans
    return f

def extension_count(rel):
    return dp_counter(rel)(0)

def pair_numerator(rel,x,y):
    assert not rel[x][y] and not rel[y][x]
    rel2=[row[:] for row in rel]
    rel2[x][y]=True
    rel2=transitive_closure(rel2)
    return extension_count(rel2)

def pair_probability(rel,x,y):
    e=extension_count(rel)
    return Fraction(pair_numerator(rel,x,y),e)

def width(rel):
    n=len(rel)
    best=0
    for mask in range(1<<n):
        bits=[i for i in range(n) if (mask>>i)&1]
        ok=True
        for i,j in combinations(bits,2):
            if rel[i][j] or rel[j][i]:
                ok=False
                break
        if ok:
            best=max(best,len(bits))
    return best

def inc_adj(rel):
    n=len(rel)
    a=[set() for _ in range(n)]
    for i,j in combinations(range(n),2):
        if not rel[i][j] and not rel[j][i]:
            a[i].add(j); a[j].add(i)
    return a

def connected_inc(rel):
    a=inc_adj(rel)
    n=len(rel)
    seen={0}; st=[0]
    while st:
        x=st.pop()
        for y in a[x]:
            if y not in seen:
                seen.add(y); st.append(y)
    return len(seen)==n

def is_autonomous_chain(rel,M):
    n=len(rel); M=set(M)
    for a,b in combinations(sorted(M),2):
        if not (rel[a][b] or rel[b][a]):
            return False
    for z in range(n):
        if z in M:
            continue
        kinds=[]
        for m in M:
            if rel[z][m]:
                kinds.append(-1)
            elif rel[m][z]:
                kinds.append(+1)
            else:
                kinds.append(0)
        if len(set(kinds)) != 1:
            return False
    return True

def type_isotone(qrel,types):
    n=len(qrel)
    for i in range(n):
        for j in range(n):
            if qrel[i][j] and types[i]>types[j]:
                return False
    return True

def build_module_poset(qrel,types,m):
    # types: 0=D below module, 1=I incomparable, 2=U above module
    r=len(qrel); n=r+m
    rel=[[False]*n for _ in range(n)]
    for i in range(r):
        for j in range(r):
            rel[i][j]=qrel[i][j]
    for a in range(m):
        for b in range(a+1,m):
            rel[r+a][r+b]=True
    for z,t in enumerate(types):
        if t==0:
            for a in range(m):
                rel[z][r+a]=True
        elif t==2:
            for a in range(m):
                rel[r+a][z]=True
    rel=transitive_closure(rel)
    # intended I-elements must stay incomparable with every module element
    for z,t in enumerate(types):
        if t==1:
            for a in range(m):
                if rel[z][r+a] or rel[r+a][z]:
                    return None
    return rel

def linear_extensions(rel):
    n=len(rel)
    pred=[set(i for i in range(n) if rel[i][j]) for j in range(n)]
    out=[]
    def rec(pref,rem):
        if not rem:
            out.append(tuple(pref)); return
        mins=[x for x in rem if not (pred[x] & rem)]
        for x in mins:
            rec(pref+[x], rem-{x})
    rec([],set(range(n)))
    return out

def module_corridor_distribution(qrel,types,m):
    exts=linear_extensions(qrel)
    D={i for i,t in enumerate(types) if t==0}
    U={i for i,t in enumerate(types) if t==2}
    dist=Counter()
    total=0
    n=len(types)
    for tau in exts:
        lastD=max((tau.index(d) for d in D), default=-1)
        firstU=min((tau.index(u) for u in U), default=n)
        middle=tau[lastD+1:firstU]
        assert all(types[x]==1 for x in middle)
        r=len(middle)
        w=comb(m+r,m)
        dist[(r,w)] += 1
        total += w
    return dist,total,len(exts)

def induced_rel(rel,verts):
    return [[rel[a][b] for b in verts] for a in verts]

def balanced(p):
    return ONE_THIRD <= p <= TWO_THIRDS

def named_partner_check():
    n=9
    covers=[(0,2),(0,3),(0,4),(1,4),(2,5),(3,6),(4,7),(4,8),(5,8),(6,8)]
    rel=[[False]*n for _ in range(n)]
    for a,b in covers:
        rel[a][b]=True
    rel=transitive_closure(rel)
    M=(2,5)
    assert is_autonomous_chain(rel,M)
    Q=[i for i in range(n) if i not in M]
    qrel=induced_rel(rel,Q)
    idx={v:i for i,v in enumerate(Q)}
    types=[]
    for z in Q:
        if all(rel[z][m] for m in M): types.append(0)
        elif all(rel[m][z] for m in M): types.append(2)
        else:
            assert all(not rel[z][m] and not rel[m][z] for m in M)
            types.append(1)
    dist,weighted_sum,eq=module_corridor_distribution(qrel,types,len(M))
    ep=extension_count(rel)
    assert ep==420 and eq==25 and weighted_sum==ep
    assert dist==Counter({(3,10):3,(4,15):12,(5,21):10})
    q01=pair_probability(qrel,idx[0],idx[1])
    p01=pair_probability(rel,0,1)
    cross=pair_probability(rel,2,3)
    assert q01==Fraction(16,25) and p01==Fraction(5,7) and cross==Fraction(1,2)
    return {
        "E_P":ep, "E_Q":eq,
        "corridor_distribution":sorted((r,w,c) for (r,w),c in dist.items()),
        "uniform_Q_Pr_0_before_1":str(q01),
        "weighted_P_Pr_0_before_1":str(p01),
        "cross_Pr_2_before_3":str(cross),
    }

def seven_point_countercheck():
    n=7
    covers=[(0,1),(1,2),(2,5),(3,5),(5,6)]
    rel=[[False]*n for _ in range(n)]
    for a,b in covers:
        rel[a][b]=True
    rel=transitive_closure(rel)
    M=(5,6)
    assert is_autonomous_chain(rel,M)
    assert width(rel)==3 and connected_inc(rel)
    Q=[0,1,2,3,4]
    qrel=induced_rel(rel,Q)
    types=[0,0,0,0,1]
    dist,weighted_sum,eq=module_corridor_distribution(qrel,types,2)
    ep=extension_count(rel)
    assert ep==28 and eq==20 and weighted_sum==ep
    assert dist==Counter({(0,1):16,(1,3):4})
    p54=pair_probability(rel,5,4)
    p64=pair_probability(rel,6,4)
    q13=pair_probability(qrel,1,3)
    p13=pair_probability(rel,1,3)
    assert (p54,p64)==(Fraction(2,7),Fraction(1,7))
    assert q13==p13==Fraction(1,2)
    return {
        "E_P":ep,"E_Q":eq,
        "corridor_distribution":sorted((r,w,c) for (r,w),c in dist.items()),
        "cross_Pr_5_before_4":str(p54),
        "cross_Pr_6_before_4":str(p64),
        "uniform_Q_Pr_1_before_3":str(q13),
        "weighted_P_Pr_1_before_3":str(p13),
    }

def exhaustive_dichotomy():
    stats=Counter()
    checked=0
    for r in range(2,6):
        for _,qrel in natural_posets(r):
            for types in product(range(3),repeat=r):
                if 1 not in types or not type_isotone(qrel,types):
                    continue
                for m in (2,3):
                    rel=build_module_poset(qrel,types,m)
                    if rel is None or width(rel)>3 or not connected_inc(rel):
                        continue
                    checked += 1
                    ep=extension_count(rel)
                    qind=induced_rel(rel,list(range(r)))
                    dist,w_sum,eq=module_corridor_distribution(qind,types,m)
                    assert w_sum==ep
                    # Rescue A: balanced module--I pair in P.
                    cross=False
                    for z,t in enumerate(types):
                        if t!=1:
                            continue
                        for c in range(r,r+m):
                            if balanced(pair_probability(rel,c,z)):
                                cross=True; break
                        if cross: break
                    if cross:
                        stats[(r,m,"cross")] += 1
                        continue
                    # Rescue B: a pair balanced under uniform Q remains balanced under P.
                    quotient=False
                    for a,b in combinations(range(r),2):
                        if qind[a][b] or qind[b][a]:
                            continue
                        q=pair_probability(qind,a,b)
                        if balanced(q) and balanced(pair_probability(rel,a,b)):
                            quotient=True; break
                    if quotient:
                        stats[(r,m,"quotient")] += 1
                    else:
                        stats[(r,m,"FAIL")] += 1
                        raise AssertionError(("autonomous-chain dichotomy failed",r,m,types))
    assert checked==28550
    assert sum(v for k,v in stats.items() if k[2]=="FAIL")==0
    return checked,stats

def main():
    partner=named_partner_check()
    seven=seven_point_countercheck()
    checked,stats=exhaustive_dichotomy()
    print("POS3_AUTONOMOUS_CHAIN_BINOMIAL_CHECK_PASS")
    print("named_partner_9pt",partner)
    print("seven_point_cross_shortcut_counterexample",seven)
    print("structured_dichotomy_cases",checked)
    for k in sorted(stats):
        print("dichotomy",k,stats[k])
    print("dichotomy_failures",sum(v for k,v in stats.items() if k[2]=="FAIL"))

if __name__=="__main__":
    main()
