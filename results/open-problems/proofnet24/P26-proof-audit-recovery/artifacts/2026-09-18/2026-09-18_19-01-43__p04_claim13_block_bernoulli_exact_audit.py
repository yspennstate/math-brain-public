from math import comb

# Exact finite audit for P04-I0101-REGULAR-S3-BLOCK-BERNOULLI-13.
# No floating point is used.

assert sum(comb(8,r)*(r-1) for r in range(2,9)) == 769

def chi(a,p):
    a %= p
    if a == 0:
        return 0
    x = pow(a,(p-1)//2,p)
    return 1 if x == 1 else -1

def inv(a,p):
    return pow(a%p,-1,p)

def orbit_s3(y,p):
    # Closure under r(x)=1-x and s(x)=1/x.
    seen={y%p}
    todo=[y%p]
    while todo:
        x=todo.pop()
        for z in ((1-x)%p, inv(x,p)):
            if z not in seen:
                seen.add(z); todo.append(z)
    return tuple(sorted(seen))

def Vset(p):
    return [x for x in range(p) if x not in (0,1) and chi(x,p)==1 and chi(x-1,p)==1]

def check_prime(p):
    assert p % 24 == 5
    V=Vset(p)
    assert len(V)==(p-5)//4
    unseen=set(V); orbits=[]
    while unseen:
        y=min(unseen)
        O=orbit_s3(y,p)
        assert len(O)==6
        assert set(O) <= set(V)
        unseen -= set(O)
        orbits.append(O)
    q=(p-5)//24
    assert len(orbits)==q

    max_scaled=0
    for O in orbits:
        y=O[0]
        targets=orbit_s3(y,p)
        assert len(set((0,1)) | set(targets)) == 8
        counts={}
        for x in V:
            vals=tuple(chi(x-g,p) for g in targets)
            if 0 in vals:
                continue
            counts[vals]=counts.get(vals,0)+1
        assert sum(counts.values()) == len(V)-6
        # Every one of the 64 target patterns may be absent; audit exact bound.
        for mask in range(64):
            eps=tuple(1 if ((mask>>j)&1) else -1 for j in range(6))
            N=counts.get(eps,0)
            # Claim: |N-p/256| <= (769/256)*sqrt(p)+8.
            # Multiply by 256: |256N-p| <= 769 sqrt(p)+2048.
            lhs=abs(256*N-p)
            max_scaled=max(max_scaled,lhs)
            if lhs > 2048:
                assert (lhs-2048)**2 <= 769**2 * p

        # Direct orbit-level k histogram and pattern-summed histogram agree.
        direct=[0]*7
        for Osrc in orbits:
            if Osrc==O:
                continue
            x=Osrc[0]
            k=sum(1 for g in targets if chi(x-g,p)==1)
            direct[k]+=1
        via=[0]*7
        for eps,N in counts.items():
            k=sum(1 for e in eps if e==1)
            via[k]+=N
        for k in range(7):
            assert via[k] % 6 == 0
            assert via[k]//6 == direct[k]
            # Explicit consequence bound around binomial q/64 center.
            # |M_k-C(6,k)q/64| <= C(6,k)*(769 sqrt(p)/1536 + 8/6 + 5/1536)
            M=direct[k]
            C=comb(6,k)
            # 1536*|M-C*q/64| <= C*(769 sqrt(p)+2053)
            left=abs(1536*M - 24*C*q)
            base=C*2053
            if left > base:
                assert (left-base)**2 <= (C*769)**2 * p
    return len(V),q,max_scaled

assert Vset(5) == []  # p=5: theorem is vacuous because there is no y in V.
print("p=5 |V|=0 theorem_vacuous=YES")

for p in (29,53,101,149):
    n,q,max_scaled=check_prime(p)
    print(f"p={p} |V|={n} q={q} max_abs_256N_minus_p={max_scaled}")
print("P26-P04-CLAIM13-BLOCK-BERNOULLI-EXACT-AUDIT: PASS_END")
