#!/usr/bin/env python3
"""Exact verifier for HARD8-05, 2026-09-16 subset-product budget checkpoint.
Standard library only; integer arithmetic throughout.
"""
from math import gcd
from functools import lru_cache
from collections import Counter

MODULI=(16,20,32,40,48,56,60,80,120)

def units(m):
    return [r for r in range(1,m) if gcd(r,m)==1]

def order_mod(r,m):
    x=1
    for k in range(1,10*m+1):
        x=(x*r)%m
        if x==1:
            return k
    raise AssertionError((r,m))

def closure(m, gens):
    H={1}
    changed=True
    while changed:
        changed=False
        for h in tuple(H):
            for g in gens:
                x=(h*g)%m
                if x not in H:
                    H.add(x); changed=True
    return frozenset(H)

def all_subgroups(m):
    U=units(m)
    start=frozenset({1})
    subs={start}; stack=[start]
    while stack:
        H=stack.pop()
        for g in U:
            if g in H: continue
            K=closure(m, tuple(H)+(g,))
            if K not in subs:
                subs.add(K); stack.append(K)
    return subs

def maximal_avoiding(m):
    tau=m-1
    subs=[H for H in all_subgroups(m) if tau not in H]
    ans=[]
    for H in subs:
        if not any(H < K for K in subs):
            ans.append(H)
    return sorted(ans,key=lambda H:(len(H),tuple(sorted(H))))

def old_budget(m,K):
    return sum(order_mod(r,m)-2 for r in units(m) if r not in K)

def complement_budget(m,K):
    tau=m-1
    outside=set(units(m))-set(K)
    seen=set(); total=0
    for r in sorted(outside):
        if r in seen: continue
        br=max(0,order_mod(r,m)-2)
        c=(tau*pow(r,-1,m))%m
        if c in outside:
            if c==r:
                total += min(br,1)
                seen.add(r)
            else:
                bc=max(0,order_mod(c,m)-2)
                total += max(br,bc)
                seen.add(r); seen.add(c)
        else:
            total += br
            seen.add(r)
    return total

def exact_budget(m,K):
    U=units(m); pos={r:i for i,r in enumerate(U)}
    tau=m-1; target_bit=1<<pos[tau]
    outside=[r for r in U if r not in K and order_mod(r,m)-2>0]
    caps=[order_mod(r,m)-2 for r in outside]
    @lru_cache(None)
    def dp(i,mask):
        if i==len(outside): return 0
        best=dp(i+1,mask)
        r=outside[i]; cur=mask
        for e in range(1,caps[i]+1):
            new=cur
            for j,h in enumerate(U):
                if (cur>>j)&1:
                    new |= 1<<pos[(h*r)%m]
            cur=new
            if cur & target_bit:
                break
            best=max(best,e+dp(i+1,cur))
        return best
    return dp(0,1<<pos[1])

def has_target(m, counts):
    tau=m-1
    reachable={1}
    for r,e in counts.items():
        for _ in range(e):
            reachable |= {(x*r)%m for x in tuple(reachable)}
    return tau in reachable

def mod40_fixed_total_lengths(K,R):
    m=40
    outs=[r for r in units(m) if r not in K and order_mod(r,m)-2>0]
    caps=[order_mod(r,m)-2 for r in outs]
    lengths=set()
    def rec(i, counts):
        if i==len(outs):
            if has_target(m,counts): return
            prod=1
            for r,e in counts.items(): prod=(prod*pow(r,e,m))%m
            kpart=(R*pow(prod,-1,m))%m
            if kpart in K: lengths.add(sum(counts.values()))
            return
        r=outs[i]
        for e in range(caps[i]+1):
            counts[r]=e; rec(i+1,counts)
        counts.pop(r,None)
    rec(0,{})
    return tuple(sorted(lengths))

def fixed_q_840_cover():
    M=840
    hard=[r for r in range(M) if r%24==1 and gcd(r,M)==1]
    wit={}
    for u in range(1,M//4+1):
        if M%(4*u): continue
        for q in range(1,M//(4*u)+1):
            if M%(4*u*q): continue
            for a in range(1,101):
                if gcd(a,u)!=1 or (q+u)%a: continue
                mod=4*u*q
                rr=(-((q+u)//a))%mod
                for r in hard:
                    if r%mod==rr:
                        cand=(max(a,u,q),a,u,q,mod,rr)
                        if r not in wit or cand<wit[r]: wit[r]=cand
    residual=tuple(r for r in hard if r not in wit)
    squares=tuple(sorted({(x*x)%M for x in range(M) if gcd(x,M)==1}))
    assert residual==squares==(1,121,169,289,361,529)
    checks=0
    for r,cand in wit.items():
        _,a,u,q,mod,rr=cand
        assert r%mod==rr
        for t in range(3):
            n=r+840*t
            s=(a*n+u)//q
            assert a*n+u==q*s
            assert s%(4*a*u)==(4*a*u-1)%(4*a*u)
            T=(s+1)//(4*a*u)
            x=u*q*T; y=a*n*q*T; z=a*n*u*T
            assert min(x,y,z)>0
            assert 4*x*y*z==n*(y*z+x*z+x*y)
            checks+=1
    return tuple(hard), residual, checks

def main():
    expected={
      16:Counter({(2,4,4,4):2,(4,8,4,4):1}),
      20:Counter({(2,4,4,4):2,(4,8,4,4):1}),
      32:Counter({(2,28,28,24):2,(4,52,28,28):1,(8,56,28,28):1}),
      40:Counter({(2,8,8,8):4,(4,16,8,8):2}),
      48:Counter({(2,8,8,8):4,(4,16,8,8):2}),
      56:Counter({(2,32,32,16):4}),
      60:Counter({(2,8,8,8):4,(4,16,8,8):2}),
      80:Counter({(2,24,24,16):4,(4,40,24,20):6}),
      120:Counter({(2,16,16,16):8,(4,32,16,16):4}),
    }
    total_subgroups=0
    print('budget table: index, old, complement, exact')
    for m in MODULI:
        rows=[]
        for K in maximal_avoiding(m):
            idx=len(units(m))//len(K)
            row=(idx,old_budget(m,K),complement_budget(m,K),exact_budget(m,K))
            rows.append(row)
        C=Counter(rows)
        assert C==expected[m],(m,C,expected[m])
        total_subgroups += sum(C.values())
        print(m, dict(sorted(C.items())))

    K40=maximal_avoiding(40)
    lengths={R:[mod40_fixed_total_lengths(K,R) for K in K40] for R in (7,23)}
    expected_lengths=[(1,3,5,7),(1,3,5,7),(0,2,4,6,8),(1,3,5,7),(0,2,4,6,8),(1,3,5,7)]
    assert lengths[7]==expected_lengths
    assert lengths[23]==expected_lengths
    print('mod40 fixed-total exception lengths', lengths)

    hard,residual,checks=fixed_q_840_cover()
    print('hard unit residues mod840',len(hard))
    print('fixed-q covered',len(hard)-len(residual),'residual',residual)
    print('fixed-q exact identity checks',checks)
    print('maximal avoiding subgroups checked',total_subgroups)
    print('ALL_CHECKS_PASSED')

if __name__=='__main__': main()
