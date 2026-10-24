#!/usr/bin/env python3
"""Exact certificate for PROB10-07 complete-tripartite families.

Uniform measure on all forests.  For (a,b) in {(1,3),(2,2),(1,4),(2,3)},
prove pairwise negative edge correlation in K_{a,b,n} for every n>=1.

Standard library only.  The proof uses the exact terminal-partition transfer
for the n repeated vertices, exact rational polynomial arithmetic, complete
edge-pair orbit enumeration, and direct brute-force regression for n=1,2.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial

FAMS = [(1,3),(2,2),(1,4),(2,3)]


def canon_part(blocks):
    bs = [tuple(sorted(b)) for b in blocks if b]
    return tuple(sorted(bs, key=lambda b: (b[0], len(b), b)))


def all_partitions(n):
    parts = [((0,),)]
    for i in range(1, n):
        out = set()
        for p in parts:
            for j in range(len(p)):
                q = [list(b) for b in p]
                q[j].append(i)
                out.add(canon_part(q))
            out.add(canon_part(list(p) + [(i,)]))
        parts = sorted(out)
    return parts


def blocks_map(p):
    mp = {}
    for k,b in enumerate(p):
        for v in b:
            mp[v] = k
    return mp


def merge_by_subset(p, S):
    mp = blocks_map(p)
    ids = [mp[v] for v in S]
    if len(set(ids)) != len(ids):
        return None
    if len(S) < 2:
        return p
    blocks = [set(b) for b in p]
    used = sorted(set(ids))
    merged = set()
    for j in used:
        merged |= blocks[j]
    new = [blocks[j] for j in range(len(blocks)) if j not in used] + [merged]
    return canon_part(new)


def transfer(m, parts, pidx):
    q = len(parts)
    M = [[0]*q for _ in range(q)]
    for i,p in enumerate(parts):
        for mask in range(1<<m):
            S = [j for j in range(m) if (mask>>j)&1]
            r = merge_by_subset(p,S)
            if r is not None:
                M[i][pidx[r]] += 1
    return M


def matmul(A,B):
    n, k, m = len(A), len(B), len(B[0])
    out = [[0]*m for _ in range(n)]
    for i in range(n):
        for t in range(k):
            a=A[i][t]
            if not a: continue
            Bt=B[t]
            for j in range(m):
                if Bt[j]: out[i][j] += a*Bt[j]
    return out


def identity(n):
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]


def poly_trim(p):
    q=p[:]
    while len(q)>1 and q[-1]==0: q.pop()
    return q


def poly_add(a,b):
    n=max(len(a),len(b)); out=[Fraction(0) for _ in range(n)]
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    return poly_trim(out)


def poly_sub(a,b):
    n=max(len(a),len(b)); out=[Fraction(0) for _ in range(n)]
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]-=x
    return poly_trim(out)


def poly_mul(a,b):
    out=[Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return poly_trim(out)


def poly_scale(a,c): return poly_trim([c*x for x in a])


def poly_eval(a,x):
    s=Fraction(0)
    for c in reversed(a): s=s*x+c
    return s


def binom_poly(j):
    p=[Fraction(1)]
    for r in range(j): p=poly_mul(p,[Fraction(-r),Fraction(1)])
    return poly_scale(p,Fraction(1,factorial(j)))


def dsu_partition(m, edges):
    verts=set(range(m))
    for u,v in edges: verts.add(u); verts.add(v)
    par={v:v for v in verts}
    def find(x):
        while par[x]!=x:
            par[x]=par[par[x]]; x=par[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a==b: return False
        par[b]=a; return True
    for e in edges:
        if not union(*e): return None
    groups={}
    for i in range(m): groups.setdefault(find(i),[]).append(i)
    return canon_part(groups.values())


def fixed_autos(a,b):
    A=list(range(a)); B=list(range(a,a+b)); out=[]
    for pa in permutations(A):
        for pb in permutations(B):
            mp={A[i]:pa[i] for i in range(a)}
            mp.update({B[i]:pb[i] for i in range(b)})
            out.append(mp)
    if a==b:
        for mapA in permutations(B):
            for mapB in permutations(A):
                mp={A[i]:mapA[i] for i in range(a)}
                mp.update({B[i]:mapB[i] for i in range(b)})
                out.append(mp)
    return out


def graph_edges(a,b,n):
    m=a+b
    E=[tuple(sorted((u,v))) for u in range(a) for v in range(a,a+b)]
    for r in range(m,m+n):
        E.extend(tuple(sorted((t,r))) for t in range(m))
    return sorted(E)


def canonical_pair(pair,a,b,n=2):
    m=a+b; best=None
    for aut in fixed_autos(a,b):
        for pr in permutations(range(m,m+n)):
            mp=dict(aut)
            for old,new in zip(range(m,m+n),pr): mp[old]=new
            q=tuple(sorted(tuple(sorted((mp[u],mp[v]))) for u,v in pair))
            if best is None or q<best: best=q
    return best


def orbit_reps(a,b):
    E=graph_edges(a,b,2); d={}
    for pair in combinations(E,2): d.setdefault(canonical_pair(pair,a,b),0); d[canonical_pair(pair,a,b)]+=1
    return sorted(d),d


def initial_vectors(a,b,rep,parts,pidx):
    m=a+b
    core=[tuple(sorted((u,v))) for u in range(a) for v in range(a,a+b)]
    rights=sorted({v for e in rep for v in e if v>=m})
    k=len(rights)
    star=[]
    for r in range(m,m+k):
        star.extend(tuple(sorted((t,r))) for t in range(m))
    E=core+star
    e,f=rep
    reqs={'0':set(),'e':{e},'f':{f},'ef':{e,f}}
    out={z:[0]*len(parts) for z in reqs}
    for mask in range(1<<len(E)):
        chosen=[E[j] for j in range(len(E)) if (mask>>j)&1]
        C=set(chosen)
        p=dsu_partition(m,chosen)
        if p is None: continue
        pi=pidx[p]
        for z,req in reqs.items():
            if req.issubset(C): out[z][pi]+=1
    return k,out


def scalar_v_Nj_1(v,N,j):
    w=[int(x) for x in v]
    if j==0: return sum(w)
    for _ in range(j):
        nw=[0]*len(w)
        for i,a in enumerate(w):
            if not a: continue
            for t,c in enumerate(N[i]):
                if c: nw[t]+=a*c
        w=nw
    return sum(w)


def normalized_count_poly(v,N,base,m):
    out=[Fraction(0)]
    for j in range(m):
        s=scalar_v_Nj_1(v,N,j)
        if s:
            out=poly_add(out,poly_scale(binom_poly(j),Fraction(s,base**j)))
    return out


def rayleigh_poly(vecs,N,base,m):
    P={z:normalized_count_poly(vecs[z],N,base,m) for z in vecs}
    return poly_sub(poly_mul(P['e'],P['f']),poly_mul(P['0'],P['ef'])),P


def primitive_coeffs(poly):
    from math import gcd
    den=1
    for c in poly:
        den=den*c.denominator//gcd(den,c.denominator)
    ints=[int(c*den) for c in poly]
    g=0
    for z in ints: g=gcd(g,abs(z))
    if g>1:
        ints=[z//g for z in ints]; den//=g
    return den,ints


def brute_counts(a,b,n):
    E=graph_edges(a,b,n); m=len(E)
    Z=0; Ze=[0]*m; Zef=[[0]*m for _ in range(m)]
    V=a+b+n
    for mask in range(1<<m):
        par=list(range(V))
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]]; x=par[x]
            return x
        ok=True; chosen=[]
        for j,(u,v) in enumerate(E):
            if not ((mask>>j)&1): continue
            ru,rv=find(u),find(v)
            if ru==rv: ok=False; break
            par[rv]=ru; chosen.append(j)
        if not ok: continue
        Z+=1
        for i in chosen: Ze[i]+=1
        for i,j in combinations(chosen,2): Zef[i][j]+=1; Zef[j][i]+=1
    return E,Z,Ze,Zef


def transfer_counts_for_n(a,b,rep,n,polys,k):
    x=n-k
    assert x>=0
    base=a+b+1
    scale=base**x
    return {z:int(poly_eval(polys[z],x)*scale) for z in polys}


def main():
    print('PROB10-07 exact terminal-partition certificate')
    print('scope=uniform measure on ALL forests; families K_{a,b,n}, n>=1')
    print('families=',FAMS)
    print('arithmetic=exact integers/Fraction; no floating point')
    total_orbits=0
    for a,b in FAMS:
        m=a+b; base=m+1
        parts=all_partitions(m); pidx={p:i for i,p in enumerate(parts)}
        M=transfer(m,parts,pidx)
        assert all(M[i][i]==base for i in range(len(parts)))
        N=[[M[i][j]-(base if i==j else 0) for j in range(len(parts))] for i in range(len(parts))]
        P=identity(len(parts))
        prev_nonzero=False
        for r in range(1,m+1):
            P=matmul(P,N)
            nonzero=any(any(row) for row in P)
            if r==m-1: prev_nonzero=nonzero
            if r==m: assert not nonzero
        assert prev_nonzero
        reps,mults=orbit_reps(a,b)
        total_orbits+=len(reps)
        print(f'FAMILY K_{{{a},{b},n}}: m={m} Bell={len(parts)} base={base} orbits={len(reps)} N^{m}=0')
        cache={}
        for oi,rep in enumerate(reps,1):
            k,vecs=initial_vectors(a,b,rep,parts,pidx)
            R,polys=rayleigh_poly(vecs,N,base,m)
            den,ints=primitive_coeffs(R)
            assert all(z>=0 for z in ints), (a,b,rep,ints)
            if k==0:
                assert poly_eval(R,1)>0
            else:
                assert poly_eval(R,0)>0
            cache[rep]=(k,R,polys)
            print(f'  ORBIT {oi:02d} rep={rep} k={k} multiplicity_at_n2={mults[rep]} denominator={den} coeff_low_to_high={ints}')
        for n in (1,2):
            E,Z,Ze,Zef=brute_counts(a,b,n)
            checked=0
            for i,j in combinations(range(len(E)),2):
                rep=canonical_pair((E[i],E[j]),a,b,n=2)
                k,R,polys=cache[rep]
                tc=transfer_counts_for_n(a,b,rep,n,polys,k)
                assert tc['0']==Z
                assert sorted((tc['e'],tc['f']))==sorted((Ze[i],Ze[j]))
                assert tc['ef']==Zef[i][j]
                delta=Ze[i]*Ze[j]-Z*Zef[i][j]
                assert delta>0
                expected=poly_eval(R,n-k)*(base**(2*(n-k)))
                assert expected==delta
                checked+=1
            print(f'  BRUTE n={n}: edges={len(E)} pairs={checked} forests={Z} PASS')
        print(f'FAMILY K_{{{a},{b},n}} ALL_N_EXACT_PASS')
    print('total_edge_pair_orbits=',total_orbits)
    print('PROB10_07_TRIPARTITE_SUM5_EXACT_PASS')

if __name__=='__main__': main()
