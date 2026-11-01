#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial, gcd
from collections import defaultdict
FAMS=[(1,7),(2,6),(3,5),(4,4)]

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

def blocks_map(p): return {v:k for k,b in enumerate(p) for v in b}

def merge_by_subset(p,S):
    mp=blocks_map(p); ids=[mp[v] for v in S]
    if len(set(ids))!=len(ids): return None
    if len(S)<2: return p
    blocks=[set(b) for b in p]; used=set(ids); merged=set()
    for j in used: merged |= blocks[j]
    return canon_part([blocks[j] for j in range(len(blocks)) if j not in used]+[merged])

def build_target_table(m,parts,pidx):
    table=[]
    for p in parts:
        mp=blocks_map(p)
        row=[]
        for mask in range(1<<m):
            S=[j for j in range(m) if (mask>>j)&1]
            ids=[mp[v] for v in S]
            if len(set(ids))!=len(ids):
                row.append(-1); continue
            if len(S)<2:
                row.append(pidx[p]); continue
            blocks=[set(b) for b in p]; used=set(ids); merged=set()
            for j in used: merged |= blocks[j]
            q=canon_part([blocks[j] for j in range(len(blocks)) if j not in used]+[merged])
            row.append(pidx[q])
        table.append(row)
    return table

def transition_sparse(m,parts,pidx,required_mask=0,target_table=None):
    assert target_table is not None
    rows=[]
    masks=[mask for mask in range(1<<m) if (mask & required_mask)==required_mask]
    for ti in target_table:
        d=defaultdict(int)
        for mask in masks:
            q=ti[mask]
            if q>=0: d[q]+=1
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
    assert not any(w), 'N^m must vanish'
    return out

def primitive(poly):
    den=1
    for c in poly: den=den*c.denominator//gcd(den,c.denominator)
    ints=[int(c*den) for c in poly]; g=0
    for z in ints: g=gcd(g,abs(z))
    if g>1: ints=[z//g for z in ints]; den//=g
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

def core_edges(a,b): return sorted(tuple(sorted((u,v))) for u in range(a) for v in range(a,a+b))
def graph_edges(a,b,n):
    m=a+b; E=core_edges(a,b)
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
    for pair in combinations(E,2): d[canonical_pair(pair,a,b,2)] += 1
    return sorted(d),d

def core_vector(a,b,required_core,parts,pidx,cache):
    key=tuple(sorted(required_core))
    if key in cache: return cache[key][:]
    E=core_edges(a,b); eidx={e:i for i,e in enumerate(E)}; reqmask=sum(1<<eidx[e] for e in required_core); m=a+b
    out=[0]*len(parts)
    for mask in range(1<<len(E)):
        if (mask & reqmask)!=reqmask: continue
        par=list(range(m))
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]]; x=par[x]
            return x
        ok=True
        for j,(u,v) in enumerate(E):
            if not ((mask>>j)&1): continue
            ru,rv=find(u),find(v)
            if ru==rv: ok=False; break
            par[rv]=ru
        if not ok: continue
        groups={}
        for t in range(m): groups.setdefault(find(t),[]).append(t)
        out[pidx[canon_part(groups.values())]] += 1
    cache[key]=out[:]; return out

def initial_vector(a,b,k,required_edges,parts,pidx,Tcache,Ccache,target_table):
    m=a+b; core_req={e for e in required_edges if e[1]<m}; v=core_vector(a,b,core_req,parts,pidx,Ccache)
    for r in range(k):
        rv=m+r; reqmask=0
        for e in required_edges:
            if rv in e:
                t=e[0] if e[1]==rv else e[1]; reqmask|=(1<<t)
        if reqmask not in Tcache: Tcache[reqmask]=transition_sparse(m,parts,pidx,reqmask,target_table)
        v=vec_mul(v,Tcache[reqmask])
    return v

def brute_n1(a,b):
    E=graph_edges(a,b,1); V=a+b+1
    Z=0; Ze=[0]*len(E); Zef=defaultdict(int)
    for mask in range(1<<len(E)):
        par=list(range(V))
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]]; x=par[x]
            return x
        chosen=[]; ok=True
        for j,(u,v) in enumerate(E):
            if not ((mask>>j)&1): continue
            ru,rv=find(u),find(v)
            if ru==rv:
                ok=False; break
            par[rv]=ru; chosen.append(j)
        if not ok: continue
        Z+=1
        for i in chosen: Ze[i]+=1
        for i,j in combinations(chosen,2): Zef[(i,j)]+=1
    mind=None
    for i,j in combinations(range(len(E)),2):
        d=Ze[i]*Ze[j]-Z*Zef[(i,j)]
        assert d>0
        if mind is None or d<mind: mind=d
    return len(E), Z, len(E)*(len(E)-1)//2, mind

def main():
    print('PROB10-07 exact complete-tripartite width-eight certificate')
    print('scope=uniform measure on ALL forests; K_{a,b,n}, n>=1')
    print('families=',FAMS)
    print('arithmetic=exact integers/Fraction; no floating point')
    total=0; global_min=None
    m=8; base=9; parts=all_partitions(m); pidx={p:i for i,p in enumerate(parts)}
    assert len(parts)==4140
    target_table=build_target_table(m,parts,pidx)
    M=transition_sparse(m,parts,pidx,0,target_table); N=N_rows(M,base)
    w=[1]*len(parts); seen=[]
    for r in range(1,m+1): w=vec_mul(w,N); seen.append(any(w))
    assert seen[m-2] and not seen[m-1]
    Tcache={0:M}
    for a,b in FAMS:
        reps,mults=orbit_reps(a,b); total += len(reps); Ccache={}
        print(f'FAMILY K_{{{a},{b},n}} Bell={len(parts)} base={base} orbits={len(reps)} N^8=0')
        minpos=None; neg=0
        for oi,rep in enumerate(reps,1):
            rights=sorted({v for e in rep for v in e if v>=m}); k=len(rights); e,f=rep
            vecs={'0':initial_vector(a,b,k,set(),parts,pidx,Tcache,Ccache,target_table),'e':initial_vector(a,b,k,{e},parts,pidx,Tcache,Ccache,target_table),'f':initial_vector(a,b,k,{f},parts,pidx,Tcache,Ccache,target_table),'ef':initial_vector(a,b,k,{e,f},parts,pidx,Tcache,Ccache,target_table)}
            P={z:count_poly(v,N,base,m) for z,v in vecs.items()}; R=psub(pmul(P['e'],P['f']),pmul(P['0'],P['ef']))
            den,ints=primitive(R)
            if any(z<0 for z in ints):
                neg+=1; print('NEGATIVE_MONOMIAL',a,b,rep,k,den,ints)
            assert all(z>=0 for z in ints), (a,b,rep,k,ints)
            val=peval(R,1) if k==0 else peval(R,0); assert val>0, (a,b,rep,k,R)
            if minpos is None or val<minpos: minpos=val
            if global_min is None or val<global_min: global_min=val
            print(f'  ORBIT {oi:02d} rep={rep} k={k} den={den} coeff_low_to_high={ints}')
        print(f'FAMILY K_{{{a},{b},n}} ALL_N_EXACT_PASS min_physical_endpoint={minpos}')
        if (a,b)==(1,7):
            be,bz,bp,bmin=brute_n1(a,b)
            print(f'  DIRECT_BRUTE n=1 edges={be} forests={bz} pairs={bp} min_delta={bmin} ALL_PAIR_PASS')
    print('total_edge_pair_orbits=',total)
    print('global_min_physical_endpoint=',global_min)
    print('PROB10_07_TRIPARTITE_SUM8_EXACT_PASS')
if __name__=='__main__': main()
