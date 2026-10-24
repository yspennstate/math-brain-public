from itertools import combinations, product, permutations
from functools import lru_cache
from fractions import Fraction
import collections, time

# Exact terminal-partition algebra (five partitions of three terminals).
def canon(labels):
    mp={}; out=[]; nxt=0
    for a in labels:
        if a not in mp: mp[a]=nxt; nxt+=1
        out.append(mp[a])
    return tuple(out)
ST=[canon((0,1,2)),canon((0,1,1)),canon((0,0,1)),canon((0,1,0)),canon((0,0,0))]
def union_part(labels,a,b):
    labels=list(labels)
    if labels[a]==labels[b]: return None
    la,lb=labels[a],labels[b]
    return canon([la if q==lb else q for q in labels])
def introduce(labels): return canon(tuple(labels)+(max(labels,default=-1)+1,))
def forget(labels,idx): return canon(tuple(q for i,q in enumerate(labels) if i!=idx))

@lru_cache(None)
def transfer_path(L, reqt=()):
    req=set(reqt); M=[[0]*5 for _ in range(5)]
    for si,ts in enumerate(ST):
        dp={introduce(ts):1}
        stage=[(('s',0,t),t,3) for t in range(3)]; nd=collections.defaultdict(int)
        for lab,cnt in dp.items():
            for bits in product((0,1),repeat=3):
                if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)): continue
                cur=lab; ok=True
                for bit,(eid,a,b) in zip(bits,stage):
                    if bit:
                        cur=union_part(cur,a,b)
                        if cur is None: ok=False; break
                if ok: nd[cur]+=cnt
        dp=nd
        for i in range(1,L):
            nd=collections.defaultdict(int)
            stage=[(('i',i-1,i),3,4)]+[(('s',i,t),t,4) for t in range(3)]
            for lab,cnt in dp.items():
                lab2=introduce(lab)
                for bits in product((0,1),repeat=4):
                    if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)): continue
                    cur=lab2; ok=True
                    for bit,(eid,a,b) in zip(bits,stage):
                        if bit:
                            cur=union_part(cur,a,b)
                            if cur is None: ok=False; break
                    if ok: nd[forget(cur,3)]+=cnt
            dp=nd
        for lab,cnt in dp.items(): M[si][ST.index(forget(lab,3))]+=cnt
    return tuple(tuple(r) for r in M)

def mm(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(5)) for j in range(5)) for i in range(5))
def rm(r,M): return tuple(sum(r[k]*M[k][j] for k in range(5)) for j in range(5))
def rv(r,c): return sum(r[i]*c[i] for i in range(5))
I=tuple(tuple(1 if i==j else 0 for j in range(5)) for i in range(5))
S=transfer_path(1); N=tuple(tuple(S[i][j]-4*I[i][j] for j in range(5)) for i in range(5)); N2=mm(N,N); N3=mm(N2,N)
assert N3==tuple(tuple(0 for _ in range(5)) for _ in range(5))
one=(1,1,1,1,1); None1=tuple(rv(N[i],one) for i in range(5)); None2=tuple(rv(N2[i],one) for i in range(5))
Q0=(1,0,0,0,0)

def mat_to_tuple(M): return tuple(tuple(r) for r in M)

# Small atom precomputation: all empty/single/pair required-edge matrices in one pass.
def precompute_atom(n_right, internal_edges):
    edges=[]
    for i in range(n_right):
        for t in range(3): edges.append(('s',i,t))
    for a,b in internal_edges:
        if a>b: a,b=b,a
        edges.append(('i',a,b))
    keys=[()]+[(e,) for e in edges]+[tuple(sorted((e,f),key=repr)) for e,f in combinations(edges,2)]
    mats={k:[[0]*5 for _ in range(5)] for k in keys}
    def endpoints(e):
        if e[0]=='s':
            _,i,t=e; return t,3+i
        _,a,b=e; return 3+a,3+b
    m=len(edges)
    for si,ts in enumerate(ST):
        base=list(range(3+n_right))
        def find(par,x):
            while par[x]!=x:
                par[x]=par[par[x]]; x=par[x]
            return x
        for a in range(3):
            for b in range(a):
                if ts[a]==ts[b]:
                    ra,rb=find(base,a),find(base,b)
                    if ra!=rb: base[rb]=ra
        for mask in range(1<<m):
            par=base[:]; chosen=[]; ok=True
            for k,e in enumerate(edges):
                if mask>>k & 1:
                    a,b=endpoints(e); ra,rb=find(par,a),find(par,b)
                    if ra==rb: ok=False; break
                    par[rb]=ra; chosen.append(e)
            if not ok: continue
            out=canon(tuple(find(par,t) for t in range(3))); oi=ST.index(out)
            mats[()][si][oi]+=1
            for e in chosen: mats[(e,)][si][oi]+=1
            for e,f in combinations(chosen,2): mats[tuple(sorted((e,f),key=repr))][si][oi]+=1
    return edges,{k:mat_to_tuple(M) for k,M in mats.items()}

E3,M3=precompute_atom(3,[(0,1),(1,2),(0,2)])
E4,M4=precompute_atom(4,[(0,1),(1,2),(2,3),(3,0)])
def atomM(tp,req=()):
    key=tuple(sorted(req,key=repr))
    return M3[key] if tp=='C3' else M4[key]

def decompose(M):
    A=M[0][0]; B=M[0][1]; C=Fraction(M[0][4]-B,6)
    for i in range(5):
        for j in range(5):
            assert Fraction(M[i][j])==A*I[i][j]+B*N[i][j]+C*N2[i][j]
    a=Fraction(B,A); c=C/Fraction(A)
    rho=(a*a/2-c)/a
    return A,B,C,rho
A3,B3,C3,rho3=decompose(M3[()]); A4,B4,C4,rho4=decompose(M4[()])
ABC={}; rhos={}
for L in range(1,12):
    A,B,C,r=decompose(transfer_path(L)); ABC[L]=(A,B,C); rhos[L]=r
assert all(rhos[L]>rhos[L+1]>0 for L in range(1,11))
assert rho4<rho3<rhos[11]<rhos[1]==Fraction(1,8)
lo,hi=rho4,Fraction(1,8)

# New exact sign lemma. If Q=sum q_ij u^i v^j is quadratic and v=u^2/2-hu,
# then 4*c4*c2-c3^2 = q02*(q20+q01/2)-q11^2/4, independent of h.
def strip_coeffs(q):
    c=[[Fraction(0),Fraction(0),Fraction(0)] for _ in range(5)] # coefficients in 1,h,h^2
    for (iu,iv),coef in q.items():
        coef=Fraction(coef)
        if iv==0: c[iu][0]+=coef
        elif iv==1:
            c[iu+2][0]+=coef/2; c[iu+1][1]-=coef
        elif iv==2:
            c[iu+4][0]+=coef/4; c[iu+3][1]-=coef; c[iu+2][2]+=coef
        else: raise AssertionError
    return [tuple(z) for z in c]
def peval(p,x): return p[0]+p[1]*x+p[2]*x*x
def bern_h(p):
    d=hi-lo; b0=peval(p,lo); b2=peval(p,hi); deriv=p[1]+2*p[2]*lo; b1=b0+deriv*d/2
    return (b0,b1,b2)
def discriminant_K(q):
    q02=Fraction(q.get((0,2),0)); q20=Fraction(q.get((2,0),0)); q01=Fraction(q.get((0,1),0)); q11=Fraction(q.get((1,1),0))
    return q02*(q20+q01/2)-q11*q11/4
# direct coefficient identity check on formal symbols is encoded arithmetically below for every Q;
# c4=q02/4,c3=q11/2-q02*h,c2=q20+q01/2-q11*h+q02*h^2.

def edges_L(L): return [('s',i,t) for i in range(L) for t in range(3)]+[('i',i,i+1) for i in range(L-1)]
PERMS=list(permutations(range(3)))
def tright(e,L,p,rev):
    k,a,b=e
    if k=='s': return ('s',L-1-a if rev else a,p[b])
    i,j=a,b
    if rev: i,j=L-1-j,L-1-i
    return ('i',i,j)
def samekey(pair,L): return min((tuple(sorted([tright(e,L,p,r) for e in pair],key=repr)) for p in PERMS for r in (0,1)),key=repr)
def crosskey(e,L,f,M):
    vals=[]
    for p in PERMS:
        for r1 in (0,1):
            for r2 in (0,1):
                a=tright(e,L,p,r1); b=tright(f,M,p,r2)
                vals.append(((L,a),(M,b)) if L<M else tuple(sorted(((L,a),(L,b)),key=repr)))
    return min(vals,key=repr)
def path_reps(maxL=11):
    out=[]
    for L in range(1,maxL+1):
        seen={}
        for pair in combinations(edges_L(L),2): seen.setdefault(samekey(pair,L),pair)
        out += [('sameP',L,L,*pair) for pair in seen.values()]
    for L in range(1,maxL+1):
        EL=edges_L(L)
        for M in range(L,maxL+1):
            seen={}; EM=edges_L(M)
            for e in EL:
                for f in EM: seen.setdefault(crosskey(e,L,f,M),(e,f))
            out += [('crossP',L,M,e,f) for e,f in seen.values()]
    return out

@lru_cache(None)
def singleP(L,e): return transfer_path(L,(e,))
@lru_cache(None)
def pairP(L,e,f): return transfer_path(L,tuple(sorted((e,f),key=repr)))
def triple(row): return (rv(row,one),rv(row,None1),rv(row,None2))
def prod_aff(a,b):
    d=collections.defaultdict(int); mons=[(0,0),(1,0),(0,1)]
    for i,x in enumerate(a):
        for j,z in enumerate(b): d[(mons[i][0]+mons[j][0],mons[i][1]+mons[j][1])]+=x*z
    return d
def delta_q(ts):
    p=prod_aff(ts[1],ts[2]); m=prod_aff(ts[0],ts[3])
    for k,z in m.items(): p[k]-=z
    return {k:z for k,z in p.items() if z}

def q_path(rep):
    typ,L,M,e,f=rep; ts=[]
    for mask in range(4):
        row=Q0
        if typ=='sameP':
            if mask==0: mat=transfer_path(L)
            elif mask==1: mat=singleP(L,e)
            elif mask==2: mat=singleP(L,f)
            else: mat=pairP(L,e,f)
            row=rm(row,mat)
        else:
            row=rm(row,singleP(L,e) if mask&1 else transfer_path(L))
            row=rm(row,singleP(M,f) if mask&2 else transfer_path(M))
        ts.append(triple(row))
    return delta_q(ts)

atoms={'C3':E3,'C4':E4}
def mixed_reps():
    out=[]
    for tp,eds in atoms.items():
        for e,f in combinations(eds,2): out.append(('sameA',tp,tp,e,f))
    names=list(atoms)
    for i,tp1 in enumerate(names):
        for tp2 in names[i:]:
            for e in atoms[tp1]:
                for f in atoms[tp2]: out.append(('crossA',tp1,tp2,e,f))
    for tp,eds in atoms.items():
        for L in range(1,12):
            for e in eds:
                for f in edges_L(L): out.append(('crossAP',tp,L,e,f))
    return out

def q_mixed(rep):
    typ,a,b,e,f=rep; ts=[]
    for mask in range(4):
        row=Q0
        if typ=='sameA':
            req=[]
            if mask&1:req.append(e)
            if mask&2:req.append(f)
            row=rm(row,atomM(a,req))
        elif typ=='crossA':
            row=rm(row,atomM(a,(e,)) if mask&1 else atomM(a))
            row=rm(row,atomM(b,(f,)) if mask&2 else atomM(b))
        else:
            row=rm(row,atomM(a,(e,)) if mask&1 else atomM(a))
            row=rm(row,singleP(b,f) if mask&2 else transfer_path(b))
        ts.append(triple(row))
    return delta_q(ts)

# Exact local certificate. Finite local list + strip transfer covers arbitrary multiplicities.
t0=time.time(); PR=path_reps(); MR=mixed_reps(); unique={}
for rep in PR:
    qv=q_path(rep); unique.setdefault(tuple(sorted(qv.items())),('path',rep,qv))
for rep in MR:
    qv=q_mixed(rep); unique.setdefault(tuple(sorted(qv.items())),('mixed',rep,qv))
counts=collections.Counter(); failures=[]; minK=None
for origin,rep,qv in unique.values():
    sc=strip_coeffs(qv); allb=[]
    for p in sc:
        if p!=(0,0,0): allb.extend(bern_h(p))
    if sc[0][0]>0 and all(b>=0 for b in allb):
        counts[(origin,'regular')]+=1; continue
    if sc[0]==(0,0,0):
        ok=all(p==(0,0,0) or all(b>=0 for b in bern_h(p)) for p in sc[1:])
        if ok and all(b>0 for b in bern_h(sc[1])):
            counts[(origin,'zero')]+=1; continue
    q02=Fraction(qv.get((0,2),0)); K=discriminant_K(qv)
    # c0=q00 and c1(h)=q10-q01*h; Bernstein endpoints suffice (linear).
    if q02>0 and K>0 and sc[0][0]>=0 and all(b>=0 for b in bern_h(sc[1])):
        # verify the advertised h-cancellation exactly from strip coefficients.
        c4,c3,c2=sc[4],sc[3],sc[2]
        def pmul2(a,b):
            z=[Fraction(0)]*5
            for i,x in enumerate(a):
                for j,w in enumerate(b): z[i+j]+=x*w
            return z
        lhs=pmul2(c4,c2); lhs=[4*x for x in lhs]
        rhs=pmul2(c3,c3); D=[lhs[i]-rhs[i] for i in range(5)]
        assert D[0]==K and all(x==0 for x in D[1:])
        counts[(origin,'discriminant')]+=1
        minK=K if minK is None else min(minK,K)
        continue
    failures.append((origin,rep,qv,sc,K))

# Independent brute-force checks for new cyclic members.
def physical_graph(c3=0,c4=0,r=0):
    edges=[]; nxt=3
    for _ in range(c3):
        vv=list(range(nxt,nxt+3)); nxt+=3
        for x in vv:
            for t in range(3): edges.append((t,x))
        edges += [(vv[0],vv[1]),(vv[1],vv[2]),(vv[0],vv[2])]
    for _ in range(c4):
        vv=list(range(nxt,nxt+4)); nxt+=4
        for x in vv:
            for t in range(3): edges.append((t,x))
        edges += [(vv[0],vv[1]),(vv[1],vv[2]),(vv[2],vv[3]),(vv[0],vv[3])]
    for _ in range(r):
        x=nxt; nxt+=1
        for t in range(3): edges.append((t,x))
    return nxt,edges

def brute(n,edges):
    m=len(edges); Z=0; Ze=[0]*m; Zef=[[0]*m for _ in range(m)]
    for mask in range(1<<m):
        par=list(range(n))
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]]; x=par[x]
            return x
        chosen=[]; ok=True
        for k,(a,b) in enumerate(edges):
            if mask>>k & 1:
                ra,rb=find(a),find(b)
                if ra==rb: ok=False; break
                par[rb]=ra; chosen.append(k)
        if not ok: continue
        Z+=1
        for i in chosen: Ze[i]+=1
        for aa in range(len(chosen)):
            for bb in range(aa+1,len(chosen)):
                i,j=chosen[aa],chosen[bb]; Zef[i][j]+=1; Zef[j][i]+=1
    mg=min(Ze[i]*Ze[j]-Z*Zef[i][j] for i,j in combinations(range(m),2))
    return Z,mg
checks=[]
for params in [(0,1,0),(0,1,1),(1,0,0)]:
    n,ed=physical_graph(*params); Z,mg=brute(n,ed); assert mg>=0; checks.append((params,n,len(ed),Z,mg))

print('C3_transfer',A3,B3,C3,'rho',rho3)
print('C4_transfer',A4,B4,C4,'rho',rho4)
print('P11_transfer',ABC[11],'rho',rhos[11])
print('rho_order',rho4,'<',rho3,'<',rhos[11],'< ... <',rhos[1])
print('strip_discriminant_identity','K=q02*(q20+q01/2)-q11^2/4; h cancels')
print('path_reps',len(PR),'mixed_raw_reps',len(MR),'total_local_reps',len(PR)+len(MR))
print('unique_polynomials',len(unique))
print('certificate_counts',dict(counts))
print('min_positive_K',minK)
print('failures',len(failures))
for c in checks: print('brute',c)
print('elapsed_s',round(time.time()-t0,2))
assert len(PR)==3478 and len(MR)==7862 and len(unique)==3842
assert counts[('path','regular')]==3402 and counts[('path','zero')]==1 and counts[('path','discriminant')]==75
assert counts[('mixed','regular')]==363 and counts[('mixed','discriminant')]==1
assert not failures
print('ALL_EXACT_CHECKS_PASS')
