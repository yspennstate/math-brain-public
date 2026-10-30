#!/usr/bin/env python3
from itertools import combinations
from functools import lru_cache
from fractions import Fraction
from math import comb

def closure(n, mask):
    pairs=list(combinations(range(n),2))
    pred=[0]*n
    for k,(i,j) in enumerate(pairs):
        if (mask>>k)&1:
            pred[j]|=1<<i
    changed=True
    while changed:
        changed=False
        for j in range(n):
            new=pred[j]
            q=pred[j]
            while q:
                bit=q & -q
                i=bit.bit_length()-1
                new |= pred[i]
                q -= bit
            if new != pred[j]:
                pred[j]=new
                changed=True
    rel=0
    for k,(i,j) in enumerate(pairs):
        if (pred[j]>>i)&1:
            rel |= 1<<k
    return rel, tuple(pred)

def is_ideal(pred,S):
    return all(not ((S>>v)&1) or pred[v]&~S==0 for v in range(len(pred)))

def ext_count(pred):
    n=len(pred); full=(1<<n)-1
    @lru_cache(None)
    def c(S):
        if S==full: return 1
        ans=0
        for v in range(n):
            if not ((S>>v)&1) and pred[v]&~S==0:
                ans += c(S|1<<v)
        return ans
    return c(0)

def event_before_count(pred,a,b):
    n=len(pred); full=(1<<n)-1
    @lru_cache(None)
    def c(S, seen_a):
        if S==full: return 1
        ans=0
        for v in range(n):
            if (S>>v)&1 or pred[v]&~S: continue
            if v==b and not seen_a: continue
            ans += c(S|1<<v, seen_a or v==a)
        return ans
    return c(0,False)

def induced(pred, verts):
    idx={v:i for i,v in enumerate(verts)}
    out=[]
    for v in verts:
        m=0
        for u in verts:
            if (pred[v]>>u)&1:
                m |= 1<<idx[u]
        out.append(m)
    return tuple(out)

def incomparable(pred,a,b):
    return not ((pred[b]>>a)&1 or (pred[a]>>b)&1)

def succset(pred,x):
    return {v for v in range(len(pred)) if (pred[v]>>x)&1}

def predset(pred,x):
    return {v for v in range(len(pred)) if (pred[x]>>v)&1}

def width_at_most_3(pred):
    n=len(pred)
    for S in combinations(range(n),4):
        if all(incomparable(pred,a,b) for a,b in combinations(S,2)):
            return False
    return True

def chain(pred, verts):
    return all(not incomparable(pred,a,b) for a,b in combinations(verts,2))

def balanced(num,den):
    return 3*num>=den and 3*num<=2*den

seen=set()
posets=leaf_states=factor_checks=lower_chain_cases=upper_chain_cases=0
for n in range(2,7):
    for mask in range(1<<(n*(n-1)//2)):
        rel,pred=closure(n,mask)
        if (n,rel) in seen: continue
        seen.add((n,rel))
        if not width_at_most_3(pred): continue
        posets += 1
        E=ext_count(pred)
        for x in range(n):
            inc=[b for b in range(n) if b!=x and incomparable(pred,x,b)]
            if len(inc)!=1: continue
            b=inc[0]; leaf_states += 1
            D=sorted(predset(pred,x)); U=sorted(succset(pred,x))
            assert set(D)|set(U)|{x,b}==set(range(n))
            assert set(D).isdisjoint(U)
            assert all((pred[u]>>d)&1 for d in D for u in U)
            assert predset(pred,b) <= set(D)
            assert succset(pred,b) <= set(U)
            ED=ext_count(induced(pred,D))
            EU=ext_count(induced(pred,U))
            L=D+[b]; R=U+[b]
            EL=ext_count(induced(pred,L))
            ER=ext_count(induced(pred,R))
            nbx=event_before_count(pred,b,x)
            nxb=event_before_count(pred,x,b)
            assert nbx==EL*EU
            assert nxb==ED*ER
            assert E==nbx+nxb
            factor_checks += 1
            if 3*nbx>2*E and D and chain(pred,D) and predset(pred,b) < set(D):
                lower_chain_cases += 1
                found=False
                for d in D:
                    if incomparable(pred,d,b):
                        nd=event_before_count(pred,d,b)
                        if balanced(nd,E):
                            found=True; break
                assert found
            if 3*nxb>2*E and U and chain(pred,U) and succset(pred,b) < set(U):
                upper_chain_cases += 1
                found=False
                for u in U:
                    if incomparable(pred,b,u):
                        nb=event_before_count(pred,b,u)
                        if balanced(nb,E):
                            found=True; break
                assert found

def pm(m):
    names=['e','d','x','y','u']+[f'r{i}' for i in range(1,m+1)]
    idx={s:i for i,s in enumerate(names)}
    edges=[('e','x'),('e','y'),('d','y'),('d','u'),('x','u')]
    if m:
        edges += [('e','r1')]
        edges += [(f'r{i}',f'r{i+1}') for i in range(1,m)]
        edges += [(f'r{m}','u')]
    pred=[0]*len(names)
    for a,b in edges: pred[idx[b]] |= 1<<idx[a]
    changed=True
    while changed:
        changed=False
        for j in range(len(names)):
            new=pred[j]; q=pred[j]
            while q:
                bit=q&-q; i=bit.bit_length()-1
                new |= pred[i]; q-=bit
            if new!=pred[j]: pred[j]=new; changed=True
    return names,tuple(pred)

pm_checks=0
for m in range(9):
    names,pred=pm(m)
    E=ext_count(pred)
    p=comb(m+3,3); q=comb(m+2,2); r=m+1
    assert E==3*p+4*q+r
    e=names.index('e'); d=names.index('d')
    assert [names[j] for j in range(len(names)) if j!=e and incomparable(pred,e,j)]==['d']
    Ned=event_before_count(pred,e,d)
    Nde=event_before_count(pred,d,e)
    assert Ned==3*p+2*q
    assert Nde==2*q+r
    if m>=1:
        U=sorted(succset(pred,e))
        assert not chain(pred,U)
        assert width_at_most_3(induced(pred,U))
        assert 3*Ned>2*E
    pm_checks += 1

print("POS3_LEAF_SPLICE_V1_PASS")
print(f"width_le_3_natural_posets_through_n6={posets}")
print(f"incomparability_leaf_states_checked={leaf_states}")
print(f"exact_factorizations_checked={factor_checks}")
print(f"lower_chain_strong_branch_cases={lower_chain_cases}")
print(f"upper_chain_strong_branch_cases={upper_chain_cases}")
print(f"partner_Pm_cases_checked={pm_checks}")
