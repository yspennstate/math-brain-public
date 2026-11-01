#!/usr/bin/env python3
from fractions import Fraction
import json, random

SEED=20260921
rng=random.Random(SEED)

def wt(x): return x.bit_count()

def relation_ok(mask,n):
    cnt=0; xo=0
    for v in range(1<<n):
        if (mask>>v)&1:
            cnt+=1; xo^=v
    return cnt%2==0 and xo==0

def bmask(n,v,piv,anchor=0):
    ei=1<<piv
    pts=(anchor,anchor^ei,anchor^v,anchor^v^ei)
    assert len(set(pts))==4
    m=0
    for x in pts: m ^= 1<<x
    return m

def pivots_default(n):
    return {v:(v & -v).bit_length()-1 for v in range(1<<n) if wt(v)>=2}

def basis(n,anchor=0,pivots=None):
    if pivots is None: pivots=pivots_default(n)
    return [(v,pivots[v],bmask(n,v,pivots[v],anchor))
            for v in range(1<<n) if wt(v)>=2]

def expand(n,A,anchor=0,pivots=None):
    B=basis(n,anchor,pivots)
    res=A; coeff={}
    for v,i,b in sorted(B,key=lambda t:wt(t[0]), reverse=True):
        if (res>>(anchor^v))&1:
            coeff[v]=1; res^=b
    return coeff,res

def phase(f,A,n):
    z=1
    for v in range(1<<n):
        if (A>>v)&1: z*=f[v]
    return z

def edge(u,i):
    return tuple(sorted((u,u^(1<<i))))

def qedges(anchor,v,i):
    return edge(anchor,i),edge(anchor^v,i)

def all_codewords(n,B):
    m=len(B)
    for comb in range(1<<m):
        A=0
        for j,(_,_,b) in enumerate(B):
            if (comb>>j)&1: A^=b
        yield A,comb

def radial_coeff(A):
    k=A.bit_count()
    return Fraction((-1)**(k//2), k+1)

def check_basis():
    rec=[]
    for n in range(2,5):
        B=basis(n); m=(1<<n)-n-1
        assert len(B)==m and all(relation_ok(b,n) for _,_,b in B)
        count=0
        bm={v:b for v,_,b in B}
        for A,comb in all_codewords(n,B):
            c,res=expand(n,A)
            assert res==0
            R=0
            for v in c:R^=bm[v]
            assert R==A
            count+=1
        assert count==1<<m
        rec.append({"n":n,"dimension":m,"codewords_checked":count})
    for n in range(3,7):
        N=1<<n
        for _ in range(80):
            anchor=rng.randrange(N)
            p={}
            for v in range(N):
                if wt(v)>=2:
                    supp=[i for i in range(n) if (v>>i)&1]
                    p[v]=rng.choice(supp)
            B=basis(n,anchor,p)
            assert len(B)==N-n-1 and all(relation_ok(b,n) for _,_,b in B)
            A=0
            for _,_,b in B:
                if rng.getrandbits(1): A^=b
            _,res=expand(n,A,anchor,p)
            assert res==0
    return rec

def check_transport():
    stats=[]
    for n in (2,3,4):
        B=basis(n); m=len(B); words=list(all_codewords(n,B))
        fs=[]
        N=1<<n
        if n<=3:
            for bits in range(1<<N):
                fs.append([(-1 if (bits>>x)&1 else 1) for x in range(N)])
        else:
            for _ in range(192):
                fs.append([rng.choice((-1,1)) for _ in range(N)])
        instances=0
        for f in fs:
            z=[]; mapped=[]
            for v,i,b in B:
                zv=phase(f,b,n); z.append(zv)
                es=qedges(0,v,i)
                taus=[f[a]*f[c] for a,c in es]
                assert zv==taus[0]*taus[1]
                if zv==-1:
                    assert taus.count(-1)==1
                    mapped.append(es[taus.index(-1)])
                else:
                    mapped.append(None)
            P=Fraction(0); loads=[Fraction(0) for _ in B]
            for A,comb in words:
                if A==0: continue
                c=radial_coeff(A)
                active=[]
                mon=1
                for j in range(m):
                    if (comb>>j)&1:
                        mon*=z[j]
                        if z[j]==-1: active.append(j)
                assert mon==phase(f,A,n)
                q=len(active)
                if q:
                    integ=Fraction(1,q) if q%2 else Fraction(0)
                else:
                    integ=Fraction(0)
                if mon==-1:
                    assert q%2==1
                    P+=c
                    for j in active:
                        loads[j]+=c*integ
                else:
                    assert q%2==0
                instances+=1
            assert sum(loads,Fraction(0))==P
            edge_load={}
            for j,L in enumerate(loads):
                if mapped[j] is None:
                    assert L==0
                else:
                    edge_load[mapped[j]]=edge_load.get(mapped[j],Fraction(0))+L
            assert sum(edge_load.values(),Fraction(0))==P
        stats.append({"n":n,"functions_checked":len(fs),
                      "relation_function_instances":instances})
    return stats

def expected_incidence_bruteforce(n,e):
    N=1<<n
    total=Fraction(0)
    for a in range(N):
        for v in range(N):
            k=wt(v)
            if k<2: continue
            for i in range(n):
                if (v>>i)&1:
                    if e in qedges(a,v,i):
                        total += Fraction(1,N*k)
    return total

def check_incidence():
    out=[]
    for n in range(2,6):
        N=1<<n
        for i in range(n):
            e=edge(0,i)
            got=expected_incidence_bruteforce(n,e)
            want=Fraction(4*(N-n-1),n*N)
            assert got==want
        out.append({"n":n,"expected_support_incidence":
                    f"{4*(N-n-1)}/{n*N}",
                    "reduced":str(Fraction(4*(N-n-1),n*N))})
    return out

def main():
    result={
      "status":"PASS",
      "scope":"engineering self-check of exact algebra; not FEI closure",
      "seed":SEED,
      "basis":check_basis(),
      "transport":check_transport(),
      "incidence":check_incidence(),
      "claims":[
        "q-flip basis spans C0 exactly",
        "frustrated relation decomposes into an odd number of frustrated basis q-flips",
        "Aumann-Shapley 1/q loads conserve arbitrary signed relation weights",
        "each frustrated q-flip routes to its unique physical disagreement edge",
        "random anchor/pivot expected support incidence per physical edge is 4(2^n-n-1)/(n2^n)"
      ]
    }
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=="__main__": main()
