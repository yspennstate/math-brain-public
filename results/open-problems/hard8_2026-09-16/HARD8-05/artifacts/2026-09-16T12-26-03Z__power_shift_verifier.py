from math import gcd
from functools import lru_cache
from collections import Counter

MODULI=(16,20,32,40,48,56,60,80,120)

def units(m):
    return [r for r in range(1,m) if gcd(r,m)==1]

def order_mod(r,m):
    x=1
    for k in range(1,10*m+1):
        x=x*r%m
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
                x=h*g%m
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

def maximal_avoiding(m,tau):
    subs=[H for H in all_subgroups(m) if tau not in H]
    return sorted([H for H in subs if not any(H<K for K in subs)],
                  key=lambda H:(len(H),tuple(sorted(H))))

def target_reachable(m, counts, h, tau):
    reach={1}
    for r,e in counts.items():
        for _ in range(h*e):
            reach |= {(x*r)%m for x in tuple(reach)}
    return tau in reach

def exact_power_budget(m,tau,K,h):
    U=units(m); pos={r:i for i,r in enumerate(U)}
    tbit=1<<pos[tau]
    outs=[]; caps=[]
    for r in U:
        if r not in K:
            c=max(0,(order_mod(r,m)-2)//h)
            if c:
                outs.append(r); caps.append(c)
    @lru_cache(None)
    def dp(i,mask):
        if i==len(outs): return 0
        best=dp(i+1,mask)
        r=outs[i]; cur=mask
        for e in range(1,caps[i]+1):
            for _ in range(h):
                new=cur
                for j,x in enumerate(U):
                    if (cur>>j)&1:
                        new |= 1<<pos[(x*r)%m]
                cur=new
            if cur&tbit:
                break
            best=max(best,e+dp(i+1,cur))
        return best
    return dp(0,1<<pos[1])

def fixed_total_lengths(m,tau,K,h,R):
    outs=[]; caps=[]
    for r in units(m):
        if r not in K:
            c=max(0,(order_mod(r,m)-2)//h)
            if c:
                outs.append(r);caps.append(c)
    ans=set()
    def rec(i,counts):
        if i==len(outs):
            if target_reachable(m,counts,h,tau): return
            prod=1
            for r,e in counts.items():
                prod=prod*pow(r,e,m)%m
            if R*pow(prod,-1,m)%m in K:
                ans.add(sum(counts.values()))
            return
        r=outs[i]
        for e in range(caps[i]+1):
            counts[r]=e;rec(i+1,counts)
        counts.pop(r,None)
    rec(0,{})
    return tuple(sorted(ans))

def factor(n):
    out=[]
    p=2
    while p*p<=n:
        while n%p==0:
            out.append(p); n//=p
        p += 1 if p==2 else 2
    if n>1: out.append(n)
    return out

def divisors_from_factor_list(factors):
    C=Counter(factors)
    ds=[1]
    for p,e in C.items():
        ds=[d*(p**j) for d in ds for j in range(e+1)]
    return ds

def isprime(n):
    if n<2:return False
    if n%2==0:return n==2
    p=3
    while p*p<=n:
        if n%p==0:return False
        p+=2
    return True

def fixed_shift_witness(n,c):
    assert (n+c)%4==0 and gcd(n,c)==1
    X=(n+c)//4
    for d in divisors_from_factor_list(factor(X*X)):
        if d%c == (-X)%c:
            Y=(X+d)//c
            Z=(X+X*X//d)//c
            assert min(X,Y,Z)>0
            assert 4*X*(n*Y)*(n*Z)==n*((n*Y)*(n*Z)+X*(n*Z)+X*(n*Y))
            return (X,d,Y,Z)
    return None

def main():
    expected={
      16:Counter({(2,2):2,(4,2):1}),
      20:Counter({(2,2):2,(4,2):1}),
      32:Counter({(2,12):2,(4,14):1,(8,14):1}),
      40:Counter({(2,4):4,(4,4):2}),
      48:Counter({(2,4):4,(4,4):2}),
      56:Counter({(2,8):4}),
      60:Counter({(2,4):4,(4,4):2}),
      80:Counter({(2,8):4,(4,10):6}),
      120:Counter({(2,8):8,(4,8):4}),
    }
    total_subgroups=0
    print('square-budget table: (index,budget)->multiplicity')
    for m in MODULI:
        tau=m-1
        C=Counter()
        for K in maximal_avoiding(m,tau):
            idx=len(units(m))//len(K)
            C[(idx,exact_power_budget(m,tau,K,2))]+=1
        assert C==expected[m],(m,C)
        total_subgroups += sum(C.values())
        print(m,dict(sorted(C.items())))

    cube=[exact_power_budget(40,39,K,3) for K in maximal_avoiding(40,39)]
    assert cube==[0]*6
    print('mod40 cube budgets',cube)

    Ks=maximal_avoiding(40,39)
    expected_lengths=[(1,3),(1,3),(0,2,4),(1,3),(0,2,4),(1,3)]
    for R in (7,23):
        got=[fixed_total_lengths(40,39,K,2,R) for K in Ks]
        assert got==expected_lengths,(R,got)
        print('mod40 square lengths',R,got)

    checked=0; successes=0; failures=0
    for n in range(25,200001,24):
        if not isprime(n): continue
        X=(n+3)//4
        fs=factor(X)
        criterion=any(p%3==2 for p in fs)
        wit=fixed_shift_witness(n,3)
        assert (wit is not None)==criterion,(n,X,fs,wit)
        if wit: successes+=1
        else:
            failures+=1
            assert all(p%3==1 for p in fs)
        checked+=1
    print('shift3 hard primes checked',checked,'successes',successes,'failures',failures)

    hard=(1,121,169,289,361,529)
    rows={}
    for R840 in hard:
        nr=R840%7
        assert nr in (1,2,4)
        Xr=(2*nr)%7
        tau=(-Xr)%7
        data=[]
        for K in maximal_avoiding(7,tau):
            b=exact_power_budget(7,tau,K,2)
            lens=fixed_total_lengths(7,tau,K,2,Xr)
            data.append((tuple(sorted(K)),b,lens))
            assert b<=2
        rows[R840]=(nr,Xr,tau,tuple(data))
    for k,v in rows.items():
        print('shift7 class',k,v)

    print('maximal subgroups in square table',total_subgroups)
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    main()
