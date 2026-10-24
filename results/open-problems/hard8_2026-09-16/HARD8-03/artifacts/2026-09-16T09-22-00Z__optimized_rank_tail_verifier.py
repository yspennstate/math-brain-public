"""Exact verifier for HARD8-03 checkpoint 2026-09-16T09:22:00Z.
Pure Python / standard library only.
"""
from fractions import Fraction
from itertools import product


def rank_q(vectors):
    if not vectors:
        return 0
    a=[list(map(Fraction,v)) for v in vectors]
    m,n=len(a),len(a[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        pv=a[r][c]; a[r]=[x/pv for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                f=a[i][c]
                a[i]=[a[i][j]-f*a[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r


def dissociated(vectors):
    if not vectors: return True
    d=len(vectors[0]); sums={(0,)*d}
    for v in vectors:
        news=[]
        for s in sums:
            t=tuple(s[j]+v[j] for j in range(d))
            if t in sums: return False
            news.append(t)
        sums.update(news)
    return True


def widths_over_universe(basis, universe):
    """Minimum negative coefficient count for every universe vector."""
    target_index={v:i for i,v in enumerate(universe)}
    best=[99]*len(universe)
    d=len(universe[0])
    for coeff in product((-1,0,1), repeat=len(basis)):
        neg=sum(c<0 for c in coeff)
        out=[0]*d
        for c,v in zip(coeff,basis):
            if c:
                for j in range(d): out[j]+=c*v[j]
        idx=target_index.get(tuple(out))
        if idx is not None and neg<best[idx]: best[idx]=neg
    return best


def coordinate_columns(hs):
    rows=list(product(*[range(h) for h in hs]))
    cols=[]; groups=[]
    for j,h in enumerate(hs):
        g=[]
        for k in range(h):
            g.append(len(cols))
            cols.append(tuple(int(x[j]==k) for x in rows))
        groups.append(g)
    return rows,cols,groups


def all_maximal_dissociated(cols):
    n=len(cols); cache={}
    def isd(mask):
        if mask not in cache:
            cache[mask]=dissociated([cols[i] for i in range(n) if mask>>i&1])
        return cache[mask]
    out=[]; full=(1<<n)-1
    for mask in range(1<<n):
        if not isd(mask): continue
        rr=full^mask; maximal=True
        while rr:
            bit=rr & -rr
            if isd(mask|bit): maximal=False; break
            rr-=bit
        if maximal: out.append(mask)
    return out


def profile_from_maximal(cols,maximal,maxk):
    n=len(cols); out={k:10**9 for k in range(maxk+1)}
    for mask in maximal:
        basis=[cols[i] for i in range(n) if mask>>i&1]
        widths=widths_over_universe(basis,cols)
        assert all(w<99 for w in widths)
        for k in range(maxk+1):
            heavy=[cols[i] for i,w in enumerate(widths) if w>k]
            out[k]=min(out[k],rank_q(heavy))
    return out


def verify_heterogeneous():
    import math
    cases=[(2,3),(2,4),(2,2,3),(2,3,3)]
    results=[]
    for hs in cases:
        rows,cols,groups=coordinate_columns(hs)
        r=rank_q(cols); assert r==1+sum(h-1 for h in hs)
        maximal=all_maximal_dissociated(cols)
        expected=sum(math.prod(hs[j] for j in range(len(hs)) if j!=star) for star in range(len(hs)))
        assert len(maximal)==expected
        opt={k:10**9 for k in range(max(hs)+1)}
        maxstar=max(range(len(hs)),key=lambda j:hs[j]); maxstar_profiles=[]
        for mask in maximal:
            complete=[]; omitted={}
            for j,g in enumerate(groups):
                sel=[i for i in g if mask>>i&1]
                if len(sel)==len(g): complete.append(j)
                else:
                    miss=[i for i in g if not(mask>>i&1)]
                    assert len(miss)==1; omitted[j]=miss[0]
            assert len(complete)==1
            star=complete[0]
            basis=[cols[i] for i in range(len(cols)) if mask>>i&1]
            widths=widths_over_universe(basis,cols)
            for j,oi in omitted.items(): assert widths[oi]==hs[j]-1
            prof={}
            for k in opt:
                heavy=[cols[oi] for j,oi in omitted.items() if widths[oi]>k]
                prof[k]=rank_q(heavy); opt[k]=min(opt[k],prof[k])
            if star==maxstar: maxstar_profiles.append(prof)
        for k in opt:
            Nk=sum((h-1)>k for h in hs)
            assert opt[k]==max(0,Nk-1)
        assert any(all(p[k]==opt[k] for k in opt) for p in maxstar_profiles)
        results.append((hs,len(rows),len(cols),r,len(maximal),opt))
    return results


def direct_sum(A,B):
    da,db=len(A[0]),len(B[0])
    return [v+(0,)*db for v in A]+[(0,)*da+v for v in B]


def verify_direct_sum():
    # Two small coordinate-partition configurations with nonzero k=0 profile.
    _,A,_=coordinate_columns((2,2))
    _,B,_=coordinate_columns((2,2))
    MA=all_maximal_dissociated(A); MB=all_maximal_dissociated(B)
    pA=profile_from_maximal(A,MA,2); pB=profile_from_maximal(B,MB,2)
    V=direct_sum(A,B); MV=all_maximal_dissociated(V)
    pV=profile_from_maximal(V,MV,2)
    assert rank_q(V)==rank_q(A)+rank_q(B)
    assert all(pV[k]==pA[k]+pB[k] for k in pV)
    assert pA=={0:1,1:0,2:0} and pV=={0:2,1:0,2:0}
    return pA,pB,pV,len(MV)


BAD_S=[
(1,0,0,1,0),(1,0,0,0,1),(0,1,0,1,1),
(0,0,1,1,1),(1,0,1,1,1),(1,1,1,1,1)]
H=[
(0,0,1,0,0),(0,1,1,0,0),(0,1,0,1,0),(1,0,1,1,0),
(1,1,1,1,0),(0,1,0,0,1),(1,0,1,0,1),(1,1,1,0,1)]
V14=BAD_S+H


def verify_rank5():
    assert dissociated(BAD_S)
    assert rank_q(BAD_S)==5 and rank_q(H)==5
    wb=widths_over_universe(BAD_S,V14)
    bad_widths=wb[len(BAD_S):]
    assert bad_widths==[2,3,2,2,2,2,2,2]

    maximal=all_maximal_dissociated(V14)
    assert len(maximal)==623
    assert {m.bit_count() for m in maximal}=={6,7}
    prof=profile_from_maximal(V14,maximal,3)
    assert prof=={0:2,1:0,2:0,3:0}

    good=[
      (0,0,1,0,0),(0,1,0,1,0),(1,0,1,1,0),
      (1,1,1,1,0),(1,0,0,0,1),(0,1,0,1,1)]
    assert dissociated(good)
    wg=widths_over_universe(good,V14)
    assert all(w<=1 for w in wg)
    return bad_widths,len(maximal),prof,wg


def main():
    print('heterogeneous:')
    for x in verify_heterogeneous(): print(x)
    print('direct_sum:',verify_direct_sum())
    print('rank5:',verify_rank5())

if __name__=='__main__': main()
