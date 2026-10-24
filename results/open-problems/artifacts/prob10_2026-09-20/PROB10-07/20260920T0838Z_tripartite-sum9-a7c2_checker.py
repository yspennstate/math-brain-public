#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial, gcd
from collections import defaultdict

FAMS=[(1,8),(2,7),(3,6),(4,5)]
MTERM=9
BASE=10


def canon_part(blocks):
    bs=[tuple(sorted(b)) for b in blocks if b]
    return tuple(sorted(bs,key=lambda b:(b[0],len(b),b)))


def all_partitions(n):
    parts=[((0,),)]
    for i in range(1,n):
        out=set()
        for p in parts:
            for j in range(len(p)):
                q=[list(b) for b in p]
                q[j].append(i)
                out.add(canon_part(q))
            out.add(canon_part(list(p)+[(i,)]))
        parts=sorted(out)
    return parts


def merge_block_indices(p,selected):
    if len(selected)<2:
        return p
    ss=set(selected)
    merged=set()
    rem=[]
    for i,b in enumerate(p):
        if i in ss:
            merged.update(b)
        else:
            rem.append(set(b))
    rem.append(merged)
    return canon_part(rem)


def transition_rows(parts,pidx,required_mask=0):
    """Exact fresh-third-part-vertex operator.

    Required terminals are forced spokes. An optional selected block contributes
    its block size because exactly one of its terminals may be chosen. If two
    required terminals already lie in one block, the row is zero (forced cycle).
    """
    req_vertices=[i for i in range(MTERM) if (required_mask>>i)&1]
    rows=[]
    for p in parts:
        bmap={v:bi for bi,b in enumerate(p) for v in b}
        req_blocks=[bmap[v] for v in req_vertices]
        if len(set(req_blocks))!=len(req_blocks):
            rows.append({})
            continue
        reqset=set(req_blocks)
        optional=[i for i in range(len(p)) if i not in reqset]
        d=defaultdict(int)
        for sm in range(1<<len(optional)):
            selected=list(reqset)
            weight=1
            for j,bi in enumerate(optional):
                if (sm>>j)&1:
                    selected.append(bi)
                    weight*=len(p[bi])
            q=p if len(selected)<2 else merge_block_indices(p,selected)
            d[pidx[q]]+=weight
        rows.append(dict(d))
    return rows


def N_rows(M,base):
    out=[]
    for i,row in enumerate(M):
        r=dict(row)
        r[i]=r.get(i,0)-base
        if r.get(i)==0:
            r.pop(i,None)
        out.append(r)
    return out


def vec_mul(v,rows):
    out=[0]*len(v)
    for i,a in enumerate(v):
        if a:
            for j,c in rows[i].items():
                out[j]+=a*c
    return out


def mat_vec(rows,u):
    out=[0]*len(rows)
    for i,row in enumerate(rows):
        s=0
        for j,c in row.items():
            s+=c*u[j]
        out[i]=s
    return out


def poly_trim(p):
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p


def padd(a,b):
    out=[Fraction(0)]*max(len(a),len(b))
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    return poly_trim(out)


def psub(a,b):
    return padd(a,[-x for x in b])


def pmul(a,b):
    out=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return poly_trim(out)


def pscale(a,c):
    return poly_trim([c*x for x in a])


def peval(a,x):
    s=Fraction(0)
    for c in reversed(a):
        s=s*x+c
    return s


def binom_poly(j):
    p=[Fraction(1)]
    for r in range(j):
        p=pmul(p,[Fraction(-r),Fraction(1)])
    return pscale(p,Fraction(1,factorial(j)))


def primitive(poly):
    den=1
    for c in poly:
        den=den*c.denominator//gcd(den,c.denominator)
    ints=[int(c*den) for c in poly]
    g=0
    for z in ints:
        g=gcd(g,abs(z))
    if g>1:
        ints=[z//g for z in ints]
        den//=g
    return den,ints


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


def core_edges(a,b):
    return sorted(tuple(sorted((u,v))) for u in range(a) for v in range(a,a+b))


def graph_edges(a,b,n):
    m=a+b
    E=core_edges(a,b)
    for r in range(m,m+n):
        E += [tuple(sorted((t,r))) for t in range(m)]
    return sorted(E)


def transform_pair(pair,mp):
    return tuple(sorted(tuple(sorted((mp[u],mp[v]))) for u,v in pair))


def orbit_reps(a,b):
    m=a+b
    E=graph_edges(a,b,2)
    unseen=set(tuple(sorted(pair)) for pair in combinations(E,2))
    autos=fixed_autos(a,b)
    rperms=[{m:m,m+1:m+1},{m:m+1,m+1:m}]
    reps=[]; mults={}
    while unseen:
        seed=min(unseen)
        orb=set()
        for aut in autos:
            for rp in rperms:
                mp=dict(aut); mp.update(rp)
                orb.add(transform_pair(seed,mp))
        rep=min(orb)
        reps.append(rep)
        mults[rep]=len(orb)
        unseen.difference_update(orb)
    assert sum(mults.values())==len(E)*(len(E)-1)//2
    return sorted(reps),mults


def core_vectors_needed(a,b,reqsets,parts,pidx):
    E=core_edges(a,b)
    eidx={e:i for i,e in enumerate(E)}
    req_masks={req:sum(1<<eidx[e] for e in req) for req in reqsets}
    vecs={req:[0]*len(parts) for req in reqsets}
    forests=0
    for mask in range(1<<len(E)):
        par=list(range(MTERM))
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]]
                x=par[x]
            return x
        ok=True
        for j,(u,v) in enumerate(E):
            if (mask>>j)&1:
                ru,rv=find(u),find(v)
                if ru==rv:
                    ok=False
                    break
                par[rv]=ru
        if not ok:
            continue
        forests+=1
        groups={}
        for t in range(MTERM):
            groups.setdefault(find(t),[]).append(t)
        pi=pidx[canon_part(groups.values())]
        for req,rm in req_masks.items():
            if (mask&rm)==rm:
                vecs[req][pi]+=1
    return vecs,forests


def brute_n1(a,b):
    E=graph_edges(a,b,1)
    V=a+b+1
    Z=0; Ze=[0]*len(E); Zef=defaultdict(int)
    for mask in range(1<<len(E)):
        par=list(range(V))
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]]
                x=par[x]
            return x
        chosen=[]; ok=True
        for j,(u,v) in enumerate(E):
            if (mask>>j)&1:
                ru,rv=find(u),find(v)
                if ru==rv:
                    ok=False
                    break
                par[rv]=ru
                chosen.append(j)
        if not ok:
            continue
        Z+=1
        for i in chosen: Ze[i]+=1
        for i,j in combinations(chosen,2): Zef[(i,j)]+=1
    mind=None
    for i,j in combinations(range(len(E)),2):
        d=Ze[i]*Ze[j]-Z*Zef[(i,j)]
        assert d>0
        if mind is None or d<mind:
            mind=d
    return len(E),Z,len(E)*(len(E)-1)//2,mind


def main():
    print('PROB10-07 exact complete-tripartite width-nine certificate')
    print('scope=uniform measure on ALL forests; K_{a,b,n}, n>=1')
    print('families=',FAMS)
    print('arithmetic=exact integers/Fraction; no floating-point sign decisions')

    parts=all_partitions(MTERM)
    pidx={p:i for i,p in enumerate(parts)}
    assert len(parts)==21147
    M=transition_rows(parts,pidx,0)
    N=N_rows(M,BASE)
    print('Bell(9)=',len(parts),'unmarked_sparse_entries=',sum(len(r) for r in M))

    # Exact right moments U_j=N^j 1. Strict coarsening proves N^9=0;
    # this executable additionally verifies the endpoint vectors.
    U=[[1]*len(parts)]
    for j in range(1,MTERM+1):
        U.append(mat_vec(N,U[-1]))
    assert any(U[8]) and not any(U[9])
    print('N^8*1_nonzero=',sum(1 for x in U[8] if x),'N^9*1_nonzero=',sum(1 for x in U[9] if x))

    all_reps={}
    forced_masks={0}
    core_reqsets={}
    for fam in FAMS:
        a,b=fam
        reps,mults=orbit_reps(a,b)
        all_reps[fam]=(reps,mults)
        reqs=set()
        for rep in reps:
            e,f=rep
            for cond in [set(),{e},{f},{e,f}]:
                reqs.add(frozenset(ed for ed in cond if ed[1]<MTERM))
                rights=sorted({v for ed in cond for v in ed if v>=MTERM})
                for rv in rights:
                    rm=0
                    for ed in cond:
                        if rv in ed:
                            t=ed[0] if ed[1]==rv else ed[1]
                            rm|=1<<t
                    forced_masks.add(rm)
        core_reqsets[fam]=reqs

    Tcache={0:M}
    for rm in sorted(forced_masks):
        if rm:
            Tcache[rm]=transition_rows(parts,pidx,rm)
    print('forced_masks=',sorted(forced_masks))

    binoms=[binom_poly(j) for j in range(MTERM)]
    def count_poly(v):
        out=[Fraction(0)]
        for j in range(MTERM):
            s=sum(a*b for a,b in zip(v,U[j]))
            if s:
                out=padd(out,pscale(binoms[j],Fraction(s,BASE**j)))
        return out

    def initial_vec(corevec,required_edges):
        rights=sorted({v for ed in required_edges for v in ed if v>=MTERM})
        v=corevec[:]
        for rv in rights:
            rm=0
            for ed in required_edges:
                if rv in ed:
                    t=ed[0] if ed[1]==rv else ed[1]
                    rm|=1<<t
            v=vec_mul(v,Tcache[rm])
        return v

    total_orbits=0
    global_min=None
    for fam in FAMS:
        a,b=fam
        cvecs,core_forest_count=core_vectors_needed(a,b,core_reqsets[fam],parts,pidx)
        reps,mults=all_reps[fam]
        total_orbits+=len(reps)
        print(f'FAMILY K_{{{a},{b},n}} core_forests={core_forest_count} orbits={len(reps)}')
        fam_min=None
        for oi,rep in enumerate(reps,1):
            rights=sorted({v for ed in rep for v in ed if v>=MTERM})
            k=len(rights)
            e,f=rep
            P={}
            for tag,cond in [('0',set()),('e',{e}),('f',{f}),('ef',{e,f})]:
                core_req=frozenset(ed for ed in cond if ed[1]<MTERM)
                v=initial_vec(cvecs[core_req],cond)
                P[tag]=count_poly(v)
            R=psub(pmul(P['e'],P['f']),pmul(P['0'],P['ef']))
            den,ints=primitive(R)
            assert all(z>=0 for z in ints),(fam,rep,ints)
            first_x=1 if k==0 else 0
            val=peval(R,first_x)
            assert val>0,(fam,rep,val)
            if fam_min is None or val<fam_min: fam_min=val
            if global_min is None or val<global_min: global_min=val
            print(f'  ORBIT {oi:02d} rep={rep} k={k} den={den} degree={len(ints)-1} min_coeff={min(ints)} max_coeff={max(ints)} first_physical={val}')
        print(f'FAMILY K_{{{a},{b},n}} ALL_N_EXACT_PASS min_first_physical={fam_min}')

    assert total_orbits==55
    be,bz,bp,bmin=brute_n1(1,8)
    assert (be,bz,bp)==(17,30618,136)
    print(f'DIRECT_BRUTE K_{{1,8,1}} edges={be} forests={bz} pairs={bp} min_delta={bmin} ALL_PAIR_PASS')
    print('total_edge_pair_orbits=',total_orbits)
    print('global_min_first_physical=',global_min)
    print('PROB10_07_TRIPARTITE_SUM9_EXACT_PASS')


if __name__=='__main__':
    main()
