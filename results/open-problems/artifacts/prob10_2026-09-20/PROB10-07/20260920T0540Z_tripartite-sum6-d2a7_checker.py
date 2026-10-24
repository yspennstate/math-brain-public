#!/usr/bin/env python3
"""Exact certificate for PROB10-07 complete-tripartite width six.

Uniform measure on ALL forests. For (a,b) in {(1,5),(2,4),(3,3)}, prove
strict pairwise negative edge correlation in K_{a,b,n} for every n>=1.

Standard library only. Exact integer/Fraction arithmetic throughout.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial, gcd
from collections import defaultdict

FAMS=[(1,5),(2,4),(3,3)]


def canon_part(blocks):
    bs=[tuple(sorted(b)) for b in blocks if b]
    return tuple(sorted(bs,key=lambda b:(b[0],len(b),b)))


def all_partitions(n):
    parts=[((0,),)]
    for i in range(1,n):
        out=set()
        for p in parts:
            for j in range(len(p)):
                q=[list(b) for b in p]; q[j].append(i); out.add(canon_part(q))
            out.add(canon_part(list(p)+[(i,)]))
        parts=sorted(out)
    return parts


def blocks_map(p):
    return {v:k for k,b in enumerate(p) for v in b}


def merge_by_subset(p,S):
    mp=blocks_map(p); ids=[mp[v] for v in S]
    if len(set(ids))!=len(ids): return None
    if len(S)<2: return p
    blocks=[set(b) for b in p]; used=set(ids); merged=set()
    for j in used: merged |= blocks[j]
    return canon_part([blocks[j] for j in range(len(blocks)) if j not in used]+[merged])


def transfer_sparse(m,parts,pidx):
    rows=[]
    for p in parts:
        d=defaultdict(int)
        for mask in range(1<<m):
            S=[j for j in range(m) if (mask>>j)&1]
            r=merge_by_subset(p,S)
            if r is not None: d[pidx[r]]+=1
        rows.append(dict(d))
    return rows


def N_rows(M,base):
    out=[]
    for i,row in enumerate(M):
        r=dict(row); r[i]=r.get(i,0)-base
        if r.get(i)==0: r.pop(i,None)
        out.append(r)
    return out


def vec_mul(v,rows):
    out=[0]*len(v)
    for i,a in enumerate(v):
        if a:
            for j,c in rows[i].items(): out[j]+=a*c
    return out


def poly_trim(p):
    while len(p)>1 and p[-1]==0: p.pop()
    return p


def padd(a,b):
    out=[Fraction(0)]*max(len(a),len(b))
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    return poly_trim(out)


def psub(a,b): return padd(a,[-x for x in b])


def pmul(a,b):
    out=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return poly_trim(out)


def pscale(a,c): return poly_trim([c*x for x in a])


def peval(a,x):
    s=Fraction(0)
    for c in reversed(a): s=s*x+c
    return s


def binom_poly(j):
    p=[Fraction(1)]
    for r in range(j): p=pmul(p,[Fraction(-r),Fraction(1)])
    return pscale(p,Fraction(1,factorial(j)))


def count_poly(v,N,base,m):
    out=[Fraction(0)]; w=v[:]
    for j in range(m):
        s=sum(w)
        if s: out=padd(out,pscale(binom_poly(j),Fraction(s,base**j)))
        w=vec_mul(w,N)
    assert not any(w), 'N^m must vanish on every vector'
    return out


def primitive(poly):
    den=1
    for c in poly: den=den*c.denominator//gcd(den,c.denominator)
    ints=[int(c*den) for c in poly]; g=0
    for z in ints: g=gcd(g,abs(z))
    if g>1:
        ints=[z//g for z in ints]; den//=g
    return den,ints


def fixed_autos(a,b):
    A=list(range(a)); B=list(range(a,a+b)); out=[]
    for pa in permutations(A):
        for pb in permutations(B):
            mp={A[i]:pa[i] for i in range(a)}; mp.update({B[i]:pb[i] for i in range(b)}); out.append(mp)
    if a==b:
        for mapA in permutations(B):
            for mapB in permutations(A):
                mp={A[i]:mapA[i] for i in range(a)}; mp.update({B[i]:mapB[i] for i in range(b)}); out.append(mp)
    return out


def graph_edges(a,b,n):
    m=a+b
    E=[tuple(sorted((u,v))) for u in range(a) for v in range(a,a+b)]
    for r in range(m,m+n): E += [tuple(sorted((t,r))) for t in range(m)]
    return sorted(E)


def canonical_pair(pair,a,b,n=2):
    m=a+b; best=None
    for aut in fixed_autos(a,b):
        for pr in permutations(range(m,m+n)):
            mp=dict(aut); mp.update({old:new for old,new in zip(range(m,m+n),pr)})
            q=tuple(sorted(tuple(sorted((mp[u],mp[v]))) for u,v in pair))
            if best is None or q<best: best=q
    return best


def orbit_reps(a,b):
    E=graph_edges(a,b,2); d=defaultdict(int)
    for pair in combinations(E,2): d[canonical_pair(pair,a,b,2)]+=1
    return sorted(d),d


def forest_partition(m,V,E,mask):
    par=list(range(V))
    def find(x):
        while par[x]!=x:
            par[x]=par[par[x]]; x=par[x]
        return x
    chosen=[]
    for j,(u,v) in enumerate(E):
        if not ((mask>>j)&1): continue
        ru,rv=find(u),find(v)
        if ru==rv: return None,None
        par[rv]=ru; chosen.append(j)
    groups={}
    for t in range(m): groups.setdefault(find(t),[]).append(t)
    return canon_part(groups.values()),chosen


def initial_all(a,b,k,parts,pidx):
    m=a+b; E=graph_edges(a,b,k); V=m+k; q=len(parts)
    z0=[0]*q; ze=[[0]*q for _ in E]; zef={}
    for mask in range(1<<len(E)):
        p,chosen=forest_partition(m,V,E,mask)
        if p is None: continue
        pi=pidx[p]; z0[pi]+=1
        for i in chosen: ze[i][pi]+=1
        for i,j in combinations(chosen,2):
            key=(i,j) if i<j else (j,i)
            if key not in zef: zef[key]=[0]*q
            zef[key][pi]+=1
    return E,z0,ze,zef


def count_at(poly,base,x): return int(peval(poly,x)*(base**x))


def main():
    print('PROB10-07 exact complete-tripartite width-six certificate')
    print('scope=uniform measure on ALL forests; K_{a,b,n}, n>=1')
    print('families=',FAMS)
    print('arithmetic=exact integers/Fraction; no floating point')
    total_orbits=0
    for a,b in FAMS:
        m=a+b; base=m+1
        parts=all_partitions(m); pidx={p:i for i,p in enumerate(parts)}
        assert len(parts)==203
        M=transfer_sparse(m,parts,pidx); N=N_rows(M,base)
        w=[1]*len(parts); seen_nonzero=[]
        for r in range(1,m+1):
            w=vec_mul(w,N); seen_nonzero.append(any(w))
        assert seen_nonzero[m-2] and not seen_nonzero[m-1]
        reps,mults=orbit_reps(a,b); total_orbits+=len(reps)
        inits={k:initial_all(a,b,k,parts,pidx) for k in (0,1,2)}
        cache={}
        print(f'FAMILY K_{{{a},{b},n}} Bell={len(parts)} base={base} orbits={len(reps)} N^6=0')
        for oi,rep in enumerate(reps,1):
            rights=sorted({v for e in rep for v in e if v>=m}); k=len(rights)
            E,z0,ze,zef=inits[k]; idx={e:i for i,e in enumerate(E)}
            e,f=rep; ie,jf=idx[e],idx[f]; key=tuple(sorted((ie,jf)))
            vecs={'0':z0,'e':ze[ie],'f':ze[jf],'ef':zef.get(key,[0]*len(parts))}
            P={z:count_poly(v,N,base,m) for z,v in vecs.items()}
            R=psub(pmul(P['e'],P['f']),pmul(P['0'],P['ef']))
            den,ints=primitive(R)
            assert all(z>=0 for z in ints), (a,b,rep,ints)
            assert (peval(R,1)>0 if k==0 else peval(R,0)>0), (a,b,rep,k,R)
            cache[rep]=(k,R,P)
            print(f'  ORBIT {oi:02d} rep={rep} k={k} mult_n2={mults[rep]} den={den} coeff_low_to_high={ints}')
        for n in (1,2):
            E,z0,ze,zef=inits[n]
            Z=sum(z0); Ze=[sum(v) for v in ze]
            checked=0
            for i,j in combinations(range(len(E)),2):
                rep=canonical_pair((E[i],E[j]),a,b,2)
                k,R,P=cache[rep]; x=n-k
                assert x>=0
                key=(i,j)
                zef_ij=sum(zef.get(key,[0]*len(parts)))
                direct_delta=Ze[i]*Ze[j]-Z*zef_ij
                assert direct_delta>0
                expected=peval(R,x)*(base**(2*x))
                assert expected==direct_delta
                assert count_at(P['0'],base,x)==Z
                assert sorted((count_at(P['e'],base,x),count_at(P['f'],base,x)))==sorted((Ze[i],Ze[j]))
                assert count_at(P['ef'],base,x)==zef_ij
                checked+=1
            print(f'  BRUTE n={n}: edges={len(E)} pairs={checked} forests={Z} PASS')
        print(f'FAMILY K_{{{a},{b},n}} ALL_N_EXACT_PASS')
    print('total_edge_pair_orbits=',total_orbits)
    print('PROB10_07_TRIPARTITE_SUM6_EXACT_PASS')

if __name__=='__main__': main()
