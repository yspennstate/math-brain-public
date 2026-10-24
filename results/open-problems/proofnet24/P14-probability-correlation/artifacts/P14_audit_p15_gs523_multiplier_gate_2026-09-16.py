N=523
TARGET=4*N
D=[d for d in range(1,N) if (N-1)%d==0]

def possible_abs_rowsums(d):
    k=(N-1)//d
    vals=set()
    for j in range(k+1):
        s=k-2*j
        for e0 in (-1,1):
            vals.add(abs(e0+d*s))
    return sorted(vals)

def profiles(d):
    R=[x for x in possible_abs_rowsums(d) if x*x<=TARGET]
    pairs={}
    for i,a in enumerate(R):
        for b in R[i:]:
            s=a*a+b*b
            if s<=TARGET:
                pairs.setdefault(s,[]).append((a,b))
    sol=set()
    for s,ablist in pairs.items():
        for a,b in ablist:
            for c,e in pairs.get(TARGET-s,()):
                sol.add(tuple(sorted((a,b,c,e))))
    return sorted(sol)

survivors={}
for d in D:
    sols=profiles(d)
    survivors[d]=sols
    print(f'd={d} profile_count={len(sols)}')
    if d in (6,9): print('profiles=',sols)
print('surviving_orders=',[d for d,v in survivors.items() if v])
assert [d for d,v in survivors.items() if v]==[1,2,3,6,9]
assert survivors[9]==[(1,19,19,37),(17,17,17,35)]
assert survivors[6]==[(5,5,19,41),(7,19,29,29)]
assert len(survivors[3])==22
assert len(survivors[2])==33
assert len(survivors[1])==33
print('P14_AUDIT_P15_GS523_MULTIPLIER_GATE_56 PASS')
print('scope: necessary row-sum gate for common-K multiplier-invariant four-circulant GS at length 523 only')
