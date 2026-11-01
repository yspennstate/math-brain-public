#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial, gcd
from collections import defaultdict
import hashlib

FAMILIES=[(1,2),(1,3),(2,2),(1,4),(2,3),(1,5),(2,4),(3,3),(1,6),(2,5),(3,4),(1,7),(2,6),(3,5),(4,4),(1,8),(2,7),(3,6),(4,5)]

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
    ss=set(selected); merged=set(); rem=[]
    for i,b in enumerate(p):
        if i in ss: merged.update(b)
        else: rem.append(set(b))
    rem.append(merged)
    return canon_part(rem)

def transition_rows(parts,pidx,mterm,required_mask=0):
    req_vertices=[i for i in range(mterm) if (required_mask>>i)&1]
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
            selected=list(reqset); weight=1
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
        r=dict(row); r[i]=r.get(i,0)-base
        if r.get(i)==0:r.pop(i,None)
        out.append(r)
    return out

def vec_mul(v,rows):
    out=[0]*len(v)
    for i,a in enumerate(v):
        if a:
            for j,c in rows[i].items(): out[j]+=a*c
    return out

def mat_vec(rows,u):
    return [sum(c*u[j] for j,c in row.items()) for row in rows]

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def padd(a,b):
    out=[Fraction(0)]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    return trim(out)

def psub(a,b):return padd(a,[-x for x in b])

def pmul(a,b):
    out=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return trim(out)

def pscale(a,c):return trim([c*x for x in a])

def peval(a,x):
    s=Fraction(0)
    for c in reversed(a):s=s*x+c
    return s

def binom_poly(j):
    p=[Fraction(1)]
    for r in range(j):p=pmul(p,[Fraction(-r),Fraction(1)])
    return pscale(p,Fraction(1,factorial(j)))

def primitive(poly):
    den=1
    for c in poly:den=den*c.denominator//gcd(den,c.denominator)
    ints=[int(c*den) for c in poly]; g=0
    for z in ints:g=gcd(g,abs(z))
    if g>1:
        ints=[z//g for z in ints]; den//=g
    return den,ints

def fixed_autos(a,b):
    A=list(range(a));B=list(range(a,a+b));out=[]
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
    m=a+b;E=core_edges(a,b)
    for r in range(m,m+n):E += [tuple(sorted((t,r))) for t in range(m)]
    return sorted(E)

def transform_pair(pair,mp):
    return tuple(sorted(tuple(sorted((mp[u],mp[v]))) for u,v in pair))

def orbit_reps(a,b):
    m=a+b;E=graph_edges(a,b,2)
    unseen=set(tuple(sorted(pair)) for pair in combinations(E,2))
    autos=fixed_autos(a,b);rperms=[{m:m,m+1:m+1},{m:m+1,m+1:m}]
    reps=[];mults={}
    while unseen:
        seed=min(unseen);orb=set()
        for aut in autos:
            for rp in rperms:
                mp=dict(aut);mp.update(rp);orb.add(transform_pair(seed,mp))
        rep=min(orb);reps.append(rep);mults[rep]=len(orb);unseen.difference_update(orb)
    assert sum(mults.values())==len(E)*(len(E)-1)//2
    return sorted(reps),mults

def core_vectors_needed(a,b,reqsets,parts,pidx,mterm):
    E=core_edges(a,b);eidx={e:i for i,e in enumerate(E)}
    req_masks={req:sum(1<<eidx[e] for e in req) for req in reqsets}
    vecs={req:[0]*len(parts) for req in reqsets};forests=0
    for mask in range(1<<len(E)):
        par=list(range(mterm))
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]];x=par[x]
            return x
        ok=True
        for j,(u,v) in enumerate(E):
            if (mask>>j)&1:
                ru,rv=find(u),find(v)
                if ru==rv:ok=False;break
                par[rv]=ru
        if not ok:continue
        forests+=1;groups={}
        for t in range(mterm):groups.setdefault(find(t),[]).append(t)
        pi=pidx[canon_part(groups.values())]
        for req,rm in req_masks.items():
            if (mask&rm)==rm:vecs[req][pi]+=1
    return vecs,forests

COMMON={}
TCACHE={}
def get_common(mterm):
    if mterm in COMMON:
        return COMMON[mterm]
    base=mterm+1
    parts=all_partitions(mterm);pidx={p:i for i,p in enumerate(parts)}
    M=transition_rows(parts,pidx,mterm,0);N=N_rows(M,base)
    U=[[1]*len(parts)]
    for _ in range(mterm):U.append(mat_vec(N,U[-1]))
    assert any(U[mterm-1]) and not any(U[mterm])
    binoms=[binom_poly(j) for j in range(mterm)]
    COMMON[mterm]=(base,parts,pidx,M,U,binoms)
    TCACHE[(mterm,0)]=M
    return COMMON[mterm]

def get_T(mterm,mask,parts,pidx,M):
    key=(mterm,mask)
    if key not in TCACHE:
        TCACHE[key]=M if mask==0 else transition_rows(parts,pidx,mterm,mask)
    return TCACHE[key]

def family_certificate(a,b):
    mterm=a+b
    base,parts,pidx,M,U,binoms=get_common(mterm)
    reps,mults=orbit_reps(a,b)
    reqs=set()
    for rep in reps:
        e,f=rep
        for cond in [set(),{e},{f},{e,f}]:
            reqs.add(frozenset(ed for ed in cond if ed[1]<mterm))
    def count_poly(v):
        out=[Fraction(0)]
        for j in range(mterm):
            ss=sum(aa*bb for aa,bb in zip(v,U[j]))
            if ss:out=padd(out,pscale(binoms[j],Fraction(ss,base**j)))
        return out
    cvecs,core_forest_count=core_vectors_needed(a,b,reqs,parts,pidx,mterm)
    infos=[]
    for rep in reps:
        rights_all=sorted({v for ed in rep for v in ed if v>=mterm})
        k=len(rights_all);e,f=rep;P={}
        for tag,cond in [('0',set()),('e',{e}),('f',{f}),('ef',{e,f})]:
            core_req=frozenset(ed for ed in cond if ed[1]<mterm)
            v=cvecs[core_req][:]
            # CORRECTED RULE: every repeated-side vertex touched by the full pair
            # is processed in every conditioning event; no forced spoke means M.
            for rv in rights_all:
                rm=0
                for ed in cond:
                    if rv in ed:
                        t=ed[0] if ed[1]==rv else ed[1]
                        rm|=1<<t
                v=vec_mul(v,get_T(mterm,rm,parts,pidx,M))
            P[tag]=count_poly(v)
        R=psub(pmul(P['e'],P['f']),pmul(P['0'],P['ef']))
        den,ints=primitive(R);first_x=1 if k==0 else 0;first=peval(R,first_x)
        assert min(ints)>=0 and first>0,(a,b,rep,ints,first)
        txt=','.join(map(str,ints))
        infos.append((rep,k,len(ints)-1,den,min(ints),max(ints),first,hashlib.sha256(txt.encode()).hexdigest()))
    return len(parts),core_forest_count,infos

def pair_prediction(a,b,n,rep,old_omission=False):
    mterm=a+b
    base,parts,pidx,M,U,binoms=get_common(mterm)
    e,f=rep
    reqs=set(frozenset(ed for ed in cond if ed[1]<mterm) for cond in [set(),{e},{f},{e,f}])
    cvecs,_=core_vectors_needed(a,b,reqs,parts,pidx,mterm)
    def count_poly(v):
        out=[Fraction(0)]
        for j in range(mterm):
            ss=sum(aa*bb for aa,bb in zip(v,U[j]))
            if ss:out=padd(out,pscale(binoms[j],Fraction(ss,base**j)))
        return out
    rights_all=sorted({v for ed in rep for v in ed if v>=mterm})
    k=len(rights_all); x=n-k
    P={}
    for tag,cond in [('0',set()),('e',{e}),('f',{f}),('ef',{e,f})]:
        core_req=frozenset(ed for ed in cond if ed[1]<mterm)
        v=cvecs[core_req][:]
        rights = sorted({v for ed in cond for v in ed if v>=mterm}) if old_omission else rights_all
        for rv in rights:
            rm=0
            for ed in cond:
                if rv in ed:
                    t=ed[0] if ed[1]==rv else ed[1]
                    rm|=1<<t
            v=vec_mul(v,get_T(mterm,rm,parts,pidx,M))
        P[tag]=count_poly(v)
    return tuple(int(base**x*peval(P[tag],x)) for tag in ('0','e','f','ef'))

def direct_marked_tuple(a,b,n,e,f):
    E=graph_edges(a,b,n);V=a+b+n;idx={ed:i for i,ed in enumerate(E)}
    ie=idx[tuple(sorted(e))];jf=idx[tuple(sorted(f))]
    Z=Ze=Zf=Zef=0
    for mask in range(1<<len(E)):
        par=list(range(V))
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]];x=par[x]
            return x
        ok=True
        for j,(u,v) in enumerate(E):
            if (mask>>j)&1:
                ru,rv=find(u),find(v)
                if ru==rv:ok=False;break
                par[rv]=ru
        if not ok:continue
        Z+=1;ae=(mask>>ie)&1;af=(mask>>jf)&1
        Ze+=ae;Zf+=af;Zef+=ae*af
    return (Z,Ze,Zf,Zef)

def brute_all_pairs(a,b,n):
    E=graph_edges(a,b,n);V=a+b+n
    Z=0;Ze=[0]*len(E);Zef=defaultdict(int)
    for mask in range(1<<len(E)):
        par=list(range(V));chosen=[];ok=True
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]];x=par[x]
            return x
        for j,(u,v) in enumerate(E):
            if (mask>>j)&1:
                ru,rv=find(u),find(v)
                if ru==rv:ok=False;break
                par[rv]=ru;chosen.append(j)
        if not ok:continue
        Z+=1
        for i in chosen:Ze[i]+=1
        for i,j in combinations(chosen,2):Zef[(i,j)]+=1
    mind=None
    for i,j in combinations(range(len(E)),2):
        d=Ze[i]*Ze[j]-Z*Zef[(i,j)]
        assert d>0,(a,b,n,i,j,d)
        if mind is None or d<mind:mind=d
    return len(E),Z,len(E)*(len(E)-1)//2,mind

def main():
    print('PROB10-07 corrected complete-tripartite certificate')
    print('scope=uniform measure on ALL forests of K_{a,b,n}; all n>=1; a<=b; a+b<=9')
    print('critical_rule=all repeated-side vertices touched by full marked pair are processed in every condition; T_empty=M')
    total=0; global_first=None
    for a,b in FAMILIES:
        bell,core_count,infos=family_certificate(a,b)
        total+=len(infos)
        fam_first=min(z[6] for z in infos)
        global_first=fam_first if global_first is None or fam_first<global_first else global_first
        fam_digest=hashlib.sha256('\n'.join(z[7] for z in infos).encode()).hexdigest()
        fam_min_coeff=min(z[4] for z in infos)
        fam_max_degree=max(z[2] for z in infos)
        zero_coeff_orbits=sum(1 for z in infos if z[4]==0)
        print(f'FAMILY K_{{{a},{b},n}} Bell={bell} core_forests={core_count} orbits={len(infos)} ALL_N_EXACT_PASS min_first={fam_first} min_primitive_coeff={fam_min_coeff} zero_min_coeff_orbits={zero_coeff_orbits} max_degree={fam_max_degree} orbit_digest={fam_digest}')
    # Exact witness that the old tripartite omission rule was wrong and the corrected rule matches the original model.
    witness=((0,3),(1,4))
    direct=direct_marked_tuple(1,2,2,*witness)
    corrected=pair_prediction(1,2,2,witness,False)
    old=pair_prediction(1,2,2,witness,True)
    assert direct==corrected==(134,48,52,18)
    assert old==(4,9,10,18) and old!=direct
    print('CORRECTION_WITNESS K_{1,2,2} pair=',witness,'direct=',direct,'corrected=',corrected,'old_omission=',old,'delta=',direct[1]*direct[2]-direct[0]*direct[3])
    # independent original-model regressions; K_{2,2,2} exercises two distinguished repeated vertices.
    for fam in [(1,2,2),(1,3,2),(2,2,2),(1,8,1)]:
        e,z,p,d=brute_all_pairs(*fam)
        print(f'DIRECT_BRUTE K_{{{fam[0]},{fam[1]},{fam[2]}}} edges={e} forests={z} pairs={p} min_delta={d} ALL_PAIR_PASS')
    print('total_edge_pair_orbits=',total)
    print('global_min_first_physical=',global_first)
    print('PROB10_07_TRIPARTITE_CORRECTED_SUM9_EXACT_PASS')

if __name__=='__main__':main()
