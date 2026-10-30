from fractions import Fraction
from itertools import combinations, product

def walsh(vals):
    N=len(vals); n=N.bit_length()-1
    out=[]
    for S in range(N):
        sm=0
        for x,v in enumerate(vals):
            sm += v * (-1 if ((S & x).bit_count() & 1) else 1)
        out.append(Fraction(sm,N))
    return out

def influences(vals):
    N=len(vals); n=N.bit_length()-1
    inf=[]
    for i in range(n):
        c=sum(vals[x] != vals[x^(1<<i)] for x in range(N))
        inf.append(Fraction(c,N))
    return inf

def antipodal_defect(n):
    N=1<<n
    vals=[]
    for x in range(N):
        v=1 if ((x>>0)&1)==0 else -1
        if x in (0,N-1): v=-v
        vals.append(v)
    return vals

def restriction_functions(vals,n,A):
    A=tuple(sorted(A)); B=tuple(i for i in range(n) if i not in A)
    fs=[]
    for abit in product((0,1), repeat=len(A)):
        arr=[]
        for bbit in product((0,1), repeat=len(B)):
            x=0
            for i,v in zip(A,abit): x |= v<<i
            for i,v in zip(B,bbit): x |= v<<i
            arr.append(vals[x])
        fs.append(tuple(arr))
    return fs

checks=0
# General character-tube identities on every balanced Boolean function
# through n=3, modulo global output sign.
general_instances=0
for n in (2,3):
    N=1<<n
    for neg in combinations(range(1,N), N//2):
        if len(neg) != N//2: continue
        vals=[1]*N
        for x in neg: vals[x]=-1
        if sum(vals)!=0: continue
        wg=walsh(vals); Ig=sum(influences(vals))
        for T in range(1,N):
            chi=[-1 if ((T & x).bit_count()&1) else 1 for x in range(N)]
            dplus=sum(vals[x]!=chi[x] for x in range(N))
            dminus=N-dplus
            sigma=1 if dplus<=dminus else -1
            mism=min(dplus,dminus)
            alpha=Fraction(mism,N)
            h=[sigma*chi[x]*vals[x] for x in range(N)]
            wh=walsh(h); infh=influences(h); Ih=sum(infh)
            k=T.bit_count()
            rhs=Ih + k - 1 - 2*sum(infh[i] for i in range(n) if (T>>i)&1)
            assert Ig-1 == rhs
            checks += 1
            tail=1-wh[0]*wh[0]
            assert tail == 4*alpha*(1-alpha)
            checks += 1
            for S in range(N):
                assert wg[S]*wg[S] == wh[S^T]*wh[S^T]
                checks += 1
            general_instances += 1

# Infinite antipodal two-point-defect family formulas and primitivity witness.
family_rows=[]
for n in range(3,9):
    N=1<<n; vals=antipodal_defect(n); w=walsh(vals)
    assert sum(vals)==0; checks+=1
    for S,a in enumerate(w):
        expected = Fraction(N-4,N) if S==1 else (Fraction(-4,N) if S.bit_count()%2 else Fraction(0))
        assert a==expected
        checks+=1
    I=sum(influences(vals))
    assert I == 1 + Fraction(4*(n-2),N)
    checks+=1
    for i in range(n):
        assert any(vals[x]!=vals[x^(1<<i)] for x in range(N))
        checks+=1
    min_distinct=10**9
    for k in range(2,n):
        for A in combinations(range(n),k):
            d=len(set(restriction_functions(vals,n,A)))
            min_distinct=min(min_distinct,d)
            assert d>=3
            checks+=1
    safeA=tuple(range(1,n))
    fs=restriction_functions(vals,n,safeA)
    assert set(fs).issubset({(1,1),(-1,-1),(1,-1),(-1,1)})
    assert len(set(fs))==3
    checks+=2
    family_rows.append((n, str(I-1), min_distinct))

print("PASS")
print("general_balanced_character_instances=", general_instances)
print("family_dimensions=3..8")
print("exact_checks=", checks)
for n,delta,md in family_rows:
    print(f"n={n}  excess_I={delta}  min_distinct_block_restrictions={md}")
