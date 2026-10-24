from itertools import combinations, product, permutations
from functools import lru_cache
from fractions import Fraction
import collections

# NM13-04 / T07 exact checker.
# The theorem certified here is for
#   G = K3 join H,
# where every component of H is one of P_1,...,P_15,C3,C4,K4,
# with arbitrary independent component multiplicities.
# The finite computation classifies LOCAL marked-edge response types only;
# arbitrary multiplicities are handled analytically by the response strip.

# ---------- five terminal-partition states and path transfer ----------

def canon(labels):
    mp={}; out=[]; nxt=0
    for a in labels:
        if a not in mp:
            mp[a]=nxt; nxt+=1
        out.append(mp[a])
    return tuple(out)

ST=[canon((0,1,2)),canon((0,1,1)),canon((0,0,1)),canon((0,1,0)),canon((0,0,0))]

def union_part(labels,a,b):
    labels=list(labels)
    if labels[a]==labels[b]:
        return None
    la,lb=labels[a],labels[b]
    return canon([la if q==lb else q for q in labels])

def introduce(labels):
    return canon(tuple(labels)+(max(labels,default=-1)+1,))

def forget(labels,idx):
    return canon(tuple(q for i,q in enumerate(labels) if i!=idx))

@lru_cache(None)
def transfer_path(L, reqt=()):
    req=set(reqt); M=[[0]*5 for _ in range(5)]
    for si,ts in enumerate(ST):
        dp={introduce(ts):1}
        stage=[(('s',0,t),t,3) for t in range(3)]
        nd=collections.defaultdict(int)
        for lab,cnt in dp.items():
            for bits in product((0,1),repeat=3):
                if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)):
                    continue
                cur=lab; ok=True
                for bit,(eid,a,b) in zip(bits,stage):
                    if bit:
                        cur=union_part(cur,a,b)
                        if cur is None:
                            ok=False; break
                if ok:
                    nd[cur]+=cnt
        dp=nd
        for i in range(1,L):
            nd=collections.defaultdict(int)
            stage=[(('i',i-1,i),3,4)]+[(('s',i,t),t,4) for t in range(3)]
            for lab,cnt in dp.items():
                lab2=introduce(lab)
                for bits in product((0,1),repeat=4):
                    if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)):
                        continue
                    cur=lab2; ok=True
                    for bit,(eid,a,b) in zip(bits,stage):
                        if bit:
                            cur=union_part(cur,a,b)
                            if cur is None:
                                ok=False; break
                    if ok:
                        nd[forget(cur,3)]+=cnt
            dp=nd
        for lab,cnt in dp.items():
            M[si][ST.index(forget(lab,3))]+=cnt
    return tuple(tuple(r) for r in M)

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(5)) for j in range(5)) for i in range(5))

def rm(r,M):
    return tuple(sum(r[k]*M[k][j] for k in range(5)) for j in range(5))

def rv(r,c):
    return sum(r[i]*c[i] for i in range(5))

I=tuple(tuple(1 if i==j else 0 for j in range(5)) for i in range(5))
S=transfer_path(1)
N=tuple(tuple(S[i][j]-4*I[i][j] for j in range(5)) for i in range(5))
N2=mm(N,N)
assert mm(N2,N)==tuple(tuple(0 for _ in range(5)) for __ in range(5))
one=(1,1,1,1,1)
None1=tuple(rv(N[i],one) for i in range(5))
None2=tuple(rv(N2[i],one) for i in range(5))

def decompose(M):
    A=Fraction(M[0][0]); B=Fraction(M[0][1]); C=Fraction(M[0][4]-M[0][1],6)
    for i in range(5):
        for j in range(5):
            assert Fraction(M[i][j])==A*I[i][j]+B*N[i][j]+C*N2[i][j]
    return A,B,C

def rho_of(M):
    A,B,C=decompose(M)
    a=B/A; c=C/A
    return (a*a/2-c)/a

# ---------- triangle left-core seed ----------

CORE=[('c',0,1),('c',0,2),('c',1,2)]

def qcore(req=()):
    req={tuple(sorted(e)) for e in req}
    tri=[(0,1),(0,2),(1,2)]
    counts=[0]*5
    for bits in product((0,1),repeat=3):
        chosen=[tri[i] for i,b in enumerate(bits) if b]
        if not req.issubset(chosen):
            continue
        if len(chosen)==3:
            continue
        par=list(range(3))
        def fd(x):
            while par[x]!=x:
                par[x]=par[par[x]]; x=par[x]
            return x
        def un(a,b):
            a,b=fd(a),fd(b)
            if a!=b:
                par[b]=a
        for a,b in chosen:
            un(a,b)
        counts[ST.index(canon(tuple(fd(i) for i in range(3))))]+=1
    return tuple(counts)

Q0=qcore()
assert Q0==(1,1,1,1,3)
PERMS=list(permutations(range(3)))

# ---------- path local orbit classification ----------

def edges_path(L):
    return [('s',i,t) for i in range(L) for t in range(3)]+[('i',i,i+1) for i in range(L-1)]

def tright(e,L,p,rev):
    k,a,b=e
    if k=='s':
        return ('s',L-1-a if rev else a,p[b])
    i,j=a,b
    if rev:
        i,j=L-1-j,L-1-i
    return ('i',i,j)

def tcore(e,p):
    _,a,b=e; a,b=p[a],p[b]
    return ('c',min(a,b),max(a,b))

def samekey(pair,L):
    return min((tuple(sorted([tright(e,L,p,r) for e in pair],key=repr)) for p in PERMS for r in (0,1)),key=repr)

def crosskey(e,L,f,M):
    vals=[]
    for p in PERMS:
        for r1 in (0,1):
            for r2 in (0,1):
                a=tright(e,L,p,r1); b=tright(f,M,p,r2)
                vals.append(((L,a),(M,b)) if L<M else tuple(sorted(((L,a),(L,b)),key=repr)))
    return min(vals,key=repr)

def crkey(c,e,L):
    return min(((tcore(c,p),tright(e,L,p,r)) for p in PERMS for r in (0,1)),key=repr)

def path_reps(maxL=15):
    out=[]; seen={}
    for pair in combinations(CORE,2):
        key=min((tuple(sorted([tcore(e,p) for e in pair],key=repr)) for p in PERMS),key=repr)
        seen.setdefault(key,pair)
    out += [('cc',0,0,*pair) for pair in seen.values()]
    for L in range(1,maxL+1):
        seen={}
        for c in CORE:
            for e in edges_path(L):
                seen.setdefault(crkey(c,e,L),(c,e))
        out += [('cr',0,L,c,e) for c,e in seen.values()]
    for L in range(1,maxL+1):
        seen={}
        for pair in combinations(edges_path(L),2):
            seen.setdefault(samekey(pair,L),pair)
        out += [('same',L,L,*pair) for pair in seen.values()]
    for L in range(1,maxL+1):
        EL=edges_path(L)
        for M in range(L,maxL+1):
            seen={}; EM=edges_path(M)
            for e in EL:
                for f in EM:
                    seen.setdefault(crosskey(e,L,f,M),(e,f))
            out += [('cross',L,M,e,f) for e,f in seen.values()]
    return out

@lru_cache(None)
def path_singleM(L,e):
    return transfer_path(L,(e,))

@lru_cache(None)
def path_pairM(L,e,f):
    return transfer_path(L,tuple(sorted((e,f),key=repr)))

def triple_from_row(row):
    return (rv(row,one),rv(row,None1),rv(row,None2))

def path_quantity(rep,mask):
    typ,L,M,e,f=rep
    if typ=='cc':
        req=[]
        if mask&1: req.append((e[1],e[2]))
        if mask&2: req.append((f[1],f[2]))
        row=qcore(req)
    elif typ=='cr':
        row=qcore(((e[1],e[2]),) if mask&1 else ())
        row=rm(row,path_singleM(M,f) if mask&2 else transfer_path(M))
    elif typ=='same':
        row=Q0
        if mask==0: mat=transfer_path(L)
        elif mask==1: mat=path_singleM(L,e)
        elif mask==2: mat=path_singleM(L,f)
        else: mat=path_pairM(L,e,f)
        row=rm(row,mat)
    else:
        row=Q0
        row=rm(row,path_singleM(L,e) if mask&1 else transfer_path(L))
        row=rm(row,path_singleM(M,f) if mask&2 else transfer_path(M))
    return triple_from_row(row)

# ---------- response-polynomial utilities ----------

def qcoeff_from_quantities(qfun,rep):
    A,Ie,If,Ief=[qfun(rep,m) for m in range(4)]
    mons=((0,0),(1,0),(0,1))
    def mul(a,b):
        d=collections.defaultdict(int)
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                d[(mons[i][0]+mons[j][0],mons[i][1]+mons[j][1])]+=x*y
        return d
    p=mul(Ie,If); m=mul(A,Ief)
    for k,z in m.items():
        p[k]-=z
    return {k:z for k,z in p.items() if z}

def strip_coeffs(q):
    # After v=u^2/2-hu, returns c_j(h) for u^j, each as (const,h,h^2).
    c=[[Fraction(0),Fraction(0),Fraction(0)] for _ in range(5)]
    for (iu,iv),coef in q.items():
        coef=Fraction(coef)
        if iv==0:
            c[iu][0]+=coef
        elif iv==1:
            c[iu+2][0]+=coef/2
            c[iu+1][1]-=coef
        elif iv==2:
            c[iu+4][0]+=coef/4
            c[iu+3][1]-=coef
            c[iu+2][2]+=coef
        else:
            raise AssertionError
    return [tuple(z) for z in c]

def peval(p,x):
    return p[0]+p[1]*x+p[2]*x*x

def bern2(p,lo,hi):
    d=hi-lo
    b0=peval(p,lo)
    b2=peval(p,hi)
    b1=b0+(p[1]+2*p[2]*lo)*d/2
    return b0,b1,b2

def pscale(a,s):
    return tuple(x*s for x in a)

def pmul(a,b):
    z=[Fraction(0)]*5
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            z[i+j]+=x*y
    while len(z)>1 and z[-1]==0:
        z.pop()
    return tuple(z)

def psub(a,b):
    n=max(len(a),len(b))
    return tuple((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(n))

def certify_response_list(reps,qfun,lo,hi,allow_discriminant=True):
    regular=0; exceptional=[]; min_const=None; min_pos=None
    for rep in reps:
        sc=strip_coeffs(qcoeff_from_quantities(qfun,rep))
        allb=[]
        for p in sc:
            if p!=(0,0,0):
                allb.extend(bern2(p,lo,hi))
        const=sc[0][0]
        if const>0 and all(b>=0 for b in allb):
            regular+=1
            min_const=const if min_const is None else min(min_const,const)
            pos=[b for b in allb if b>0]
            if pos:
                z=min(pos)
                min_pos=z if min_pos is None else min(min_pos,z)
        else:
            exceptional.append((rep,sc))
    disc=[]; fail=[]
    if allow_discriminant:
        for rep,sc in exceptional:
            c0,c1,c2,c3,c4=sc
            D=psub(pscale(pmul(c4,c2),4),pmul(c3,c3))
            ok=(c4[1:]==(0,0) and c4[0]>0 and D and D[0]>0 and all(x==0 for x in D[1:])
                and all(b>=0 for p in (c0,c1) for b in bern2(p,lo,hi)) and c0[0]>0)
            if ok:
                disc.append((rep,D[0]))
            else:
                fail.append((rep,sc,D))
    else:
        fail=exceptional
    return regular,exceptional,disc,fail,min_const,min_pos

# ---------- generic exact component tables for C3,C4,K4 ----------

def component_tables(m,internal_edges):
    edges=[('s',i,t) for i in range(m) for t in range(3)]
    edges += [('i',min(a,b),max(a,b)) for a,b in internal_edges]
    E=len(edges); edge_index={e:i for i,e in enumerate(edges)}
    base=[[0]*5 for _ in range(5)]
    singles=[[[0]*5 for _ in range(5)] for __ in range(E)]
    pairs={}
    for si,ts in enumerate(ST):
        for mask in range(1<<E):
            par=list(range(3+m))
            def fd(x):
                while par[x]!=x:
                    par[x]=par[par[x]]; x=par[x]
                return x
            def un(a,b):
                a,b=fd(a),fd(b)
                if a==b:
                    return False
                par[b]=a
                return True
            for a in range(3):
                for b in range(a):
                    if ts[a]==ts[b]:
                        un(a,b)
            chosen=[]; ok=True
            for ei,e in enumerate(edges):
                if not ((mask>>ei)&1):
                    continue
                if e[0]=='s':
                    _,i,t=e; a=t; b=3+i
                else:
                    _,i,j=e; a=3+i; b=3+j
                if not un(a,b):
                    ok=False; break
                chosen.append(ei)
            if not ok:
                continue
            sj=ST.index(canon(tuple(fd(i) for i in range(3))))
            base[si][sj]+=1
            for e in chosen:
                singles[e][si][sj]+=1
            for aa in range(len(chosen)):
                for bb in range(aa+1,len(chosen)):
                    key=(chosen[aa],chosen[bb])
                    M=pairs.get(key)
                    if M is None:
                        M=[[0]*5 for _ in range(5)]; pairs[key]=M
                    M[si][sj]+=1
    def tup(M):
        return tuple(tuple(r) for r in M)
    base=tup(base); singles=[tup(x) for x in singles]; pairs={k:tup(v) for k,v in pairs.items()}
    zero=tuple(tuple(0 for _ in range(5)) for __ in range(5))
    def get(req=()):
        req=tuple(req)
        if len(req)==0:
            return base
        ids=sorted(edge_index[e] for e in req)
        if len(ids)==1:
            return singles[ids[0]]
        if len(ids)==2:
            return pairs.get(tuple(ids),zero)
        raise ValueError('only 0/1/2 marked edges needed')
    return tuple(edges),get

def d4_group():
    out=[]
    for shift in range(4):
        out.append(tuple((i+shift)%4 for i in range(4)))
        out.append(tuple((shift-i)%4 for i in range(4)))
    return tuple(dict.fromkeys(out))

atoms=[]
# name, m, internal edges, vertex automorphism group
atom_specs=[
    ('C3',3,((0,1),(0,2),(1,2)),tuple(permutations(range(3)))),
    ('C4',4,((0,1),(1,2),(2,3),(0,3)),d4_group()),
    ('K4',4,tuple(combinations(range(4),2)),tuple(permutations(range(4)))),
]
for name,m,ints,group in atom_specs:
    edges,get=component_tables(m,ints)
    atoms.append({'name':name,'m':m,'edges':edges,'get':get,'group':group})
atom_by_name={a['name']:a for a in atoms}

expected_transfers={
    'C3':(Fraction(178),Fraction(144),Fraction(41)),
    'C4':(Fraction(1014),Fraction(1096),Fraction(1384,3)),
    'K4':(Fraction(1763),Fraction(1952),Fraction(850)),
}
expected_rho={
    'C3':Fraction(1535,12816),
    'C4':Fraction(2767,23153),
    'K4':Fraction(203301,1720688),
}
for a in atoms:
    abc=decompose(a['get'](())); rho=rho_of(a['get'](()))
    assert abc==expected_transfers[a['name']]
    assert rho==expected_rho[a['name']]
    a['rho']=rho

# Predecessor endpoint rho_15 and strict ordering of every allowed component.
A15,B15,C15=decompose(transfer_path(15))
assert (A15,B15,C15)==(Fraction(136344403840),Fraction(550341138496),Fraction(3134382731200,3))
rho15=rho_of(transfer_path(15))
assert rho15==Fraction(13162845795778912063,109915919585249991540)
rhoK4=expected_rho['K4']; rhoC4=expected_rho['C4']; rhoC3=expected_rho['C3']
assert rhoK4 < rhoC4 < rho15 < rhoC3 < Fraction(1,8)
# all path rhos lie between rho15 and 1/8
path_rhos=[rho_of(transfer_path(L)) for L in range(1,16)]
assert all(path_rhos[i]>path_rhos[i+1]>0 for i in range(14))
assert path_rhos[0]==Fraction(1,8) and path_rhos[-1]==rho15

LO=rhoK4; HI=Fraction(1,8)

# ---------- generic atom local orbit classification ----------

def tatom(e,tp,rp):
    k,a,b=e
    if k=='s':
        return ('s',rp[a],tp[b])
    a,b=rp[a],rp[b]
    return ('i',min(a,b),max(a,b))

def key_core_atom(c,e,group):
    return min(((tcore(c,tp),tatom(e,tp,rp)) for tp in PERMS for rp in group),key=repr)

def key_same_atom(pair,group):
    return min((tuple(sorted((tatom(pair[0],tp,rp),tatom(pair[1],tp,rp)),key=repr))
                for tp in PERMS for rp in group),key=repr)

def key_cross_same_atom(e,f,group):
    return min((tuple(sorted((tatom(e,tp,r1),tatom(f,tp,r2)),key=repr))
                for tp in PERMS for r1 in group for r2 in group),key=repr)

def key_atom_path(e,group,L,f):
    return min(((tatom(e,tp,rp),tright(f,L,tp,rev))
                for tp in PERMS for rp in group for rev in (0,1)),key=repr)

def key_atom_atom(e,groupA,f,groupB):
    return min(((tatom(e,tp,rA),tatom(f,tp,rB))
                for tp in PERMS for rA in groupA for rB in groupB),key=repr)

def atom_new_reps(atom,prior_atoms):
    A=atom; out=[]; seen={}
    for c in CORE:
        for e in A['edges']:
            seen.setdefault(key_core_atom(c,e,A['group']),('core_atom',A['name'],None,c,e))
    n_core=len(seen); out+=list(seen.values())
    seen={}
    for pair in combinations(A['edges'],2):
        seen.setdefault(key_same_atom(pair,A['group']),('same_atom',A['name'],None,pair[0],pair[1]))
    n_same=len(seen); out+=list(seen.values())
    seen={}
    for e in A['edges']:
        for f in A['edges']:
            seen.setdefault(key_cross_same_atom(e,f,A['group']),('cross_atom',A['name'],A['name'],e,f))
    n_cross=len(seen); out+=list(seen.values())
    n_path=0
    for L in range(1,16):
        seen={}
        for e in A['edges']:
            for f in edges_path(L):
                seen.setdefault(key_atom_path(e,A['group'],L,f),('atom_path',A['name'],L,e,f))
        n_path+=len(seen); out+=list(seen.values())
    prior_counts={}
    for B in prior_atoms:
        seen={}
        for e in A['edges']:
            for f in B['edges']:
                seen.setdefault(key_atom_atom(e,A['group'],f,B['group']),('atom_atom',A['name'],B['name'],e,f))
        prior_counts[B['name']]=len(seen); out+=list(seen.values())
    return out,{'core':n_core,'same':n_same,'cross':n_cross,'path':n_path,'prior':prior_counts}

def atom_quantity(rep,mask):
    typ,Aname,Binfo,e,f=rep
    A=atom_by_name[Aname]
    if typ=='core_atom':
        req=[]
        if mask&1: req.append((e[1],e[2]))
        row=qcore(req)
        row=rm(row,A['get']((f,)) if mask&2 else A['get'](()))
    elif typ=='same_atom':
        row=Q0
        if mask==0: mat=A['get'](())
        elif mask==1: mat=A['get']((e,))
        elif mask==2: mat=A['get']((f,))
        else: mat=A['get'](tuple(sorted((e,f),key=repr)))
        row=rm(row,mat)
    elif typ=='cross_atom':
        row=Q0
        row=rm(row,A['get']((e,)) if mask&1 else A['get'](()))
        row=rm(row,A['get']((f,)) if mask&2 else A['get'](()))
    elif typ=='atom_path':
        L=Binfo
        row=Q0
        row=rm(row,A['get']((e,)) if mask&1 else A['get'](()))
        row=rm(row,path_singleM(L,f) if mask&2 else transfer_path(L))
    elif typ=='atom_atom':
        B=atom_by_name[Binfo]
        row=Q0
        row=rm(row,A['get']((e,)) if mask&1 else A['get'](()))
        row=rm(row,B['get']((f,)) if mask&2 else B['get'](()))
    else:
        raise AssertionError
    return triple_from_row(row)

# ---------- certify the full continuous strip ----------

pathRR=path_reps(15)
assert len(pathRR)==11017
preg,pexc,pdisc,pfail,pminc,pminb=certify_response_list(pathRR,path_quantity,LO,HI,True)
assert (preg,len(pexc),len(pdisc),len(pfail),pminc,pminb)==(10814,203,203,0,2,1)
assert min(D for _,D in pdisc)==16476912
print('path sector on widened K4 strip: reps=11017 regular=10814 discriminant=203 failures=0')
print('path min regular constant =',pminc,'min positive Bernstein =',pminb,'min discriminant =',min(D for _,D in pdisc))

expected_local={
    'C3':({'core':3,'same':6,'cross':4,'path':304,'prior':{}},317,13052,270),
    'C4':({'core':3,'same':9,'cross':4,'path':304,'prior':{'C3':5}},325,508152,3240),
    'K4':({'core':3,'same':7,'cross':4,'path':304,'prior':{'C3':5,'C4':5}},328,1312038,17118),
}
prior=[]
for A in atoms:
    rr,counts=atom_new_reps(A,prior)
    exp_counts,exp_total,exp_minc,exp_minb=expected_local[A['name']]
    assert counts==exp_counts and len(rr)==exp_total
    reg,exc,disc,fail,minc,minb=certify_response_list(rr,atom_quantity,LO,HI,True)
    assert reg==len(rr) and not exc and not disc and not fail
    assert minc==exp_minc and minb==exp_minb
    print(A['name'],'local sector:',counts,'total=',len(rr),'all Bernstein-positive; min constant=',minc,'min positive Bernstein=',minb)
    prior.append(A)

print('transfers:')
for A in atoms:
    print(' ',A['name'],decompose(A['get'](())),'rho=',A['rho'])
print('rho ordering margins:')
print(' rho_C4-rho_K4 =',rhoC4-rhoK4)
print(' rho_15-rho_C4 =',rho15-rhoC4)
print(' rho_C3-rho_15 =',rhoC3-rho15)
print(' 1/8-rho_C3 =',Fraction(1,8)-rhoC3)

# ---------- independent matrix-tree / component-partition sanity check ----------
# This does not reuse the transfer matrices. It checks every edge pair of the
# noncomplete graph K3 join (K4 disjoint K1), using contraction for required
# edges and a component-partition recurrence with Kirchhoff tree counts.

def det_bareiss(A):
    n=len(A)
    if n==0: return 1
    if n==1: return A[0][0]
    B=[row[:] for row in A]; sign=1; prev=1
    for k in range(n-1):
        if B[k][k]==0:
            r=next((r for r in range(k+1,n) if B[r][k]!=0),None)
            if r is None: return 0
            B[k],B[r]=B[r],B[k]; sign=-sign
        pivot=B[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                B[i][j]=(B[i][j]*pivot-B[i][k]*B[k][j])//prev
        prev=pivot
        for i in range(k+1,n): B[i][k]=0
        for j in range(k+1,n): B[k][j]=0
    return sign*B[n-1][n-1]

def forest_count_partition(n,edges):
    edges=tuple(edges)
    @lru_cache(None)
    def tau(mask):
        if mask & (mask-1)==0:
            return 1
        verts=[i for i in range(n) if (mask>>i)&1]
        idx={v:i for i,v in enumerate(verts)}; m=len(verts)
        L=[[0]*m for _ in range(m)]
        for a,b in edges:
            if ((mask>>a)&1) and ((mask>>b)&1):
                i,j=idx[a],idx[b]
                L[i][i]+=1; L[j][j]+=1; L[i][j]-=1; L[j][i]-=1
        return det_bareiss([row[:-1] for row in L[:-1]])
    @lru_cache(None)
    def F(mask):
        if mask==0:
            return 1
        first=mask & -mask; rest=mask^first; total=0; sub=rest
        while True:
            comp=sub|first
            total+=tau(comp)*F(mask^comp)
            if sub==0:
                break
            sub=(sub-1)&rest
        return total
    return F((1<<n)-1)

def contract_graph(n,edges,req):
    par=list(range(n)); rank=[0]*n
    def fd(x):
        while par[x]!=x:
            par[x]=par[par[x]]; x=par[x]
        return x
    def un(a,b):
        a,b=fd(a),fd(b)
        if a==b: return False
        if rank[a]<rank[b]: a,b=b,a
        par[b]=a
        if rank[a]==rank[b]: rank[a]+=1
        return True
    req=set(req)
    for ei in req:
        if not un(*edges[ei]):
            return 0,()
    roots={}
    for v in range(n):
        r=fd(v)
        if r not in roots:
            roots[r]=len(roots)
    new=[]
    for ei,(a,b) in enumerate(edges):
        if ei in req:
            continue
        a,b=roots[fd(a)],roots[fd(b)]
        if a!=b:
            new.append((a,b))
    return len(roots),tuple(new)

G=[]
for a in range(3):
    for b in range(a+1,3): G.append((a,b))
for a in range(3,7):
    for b in range(a+1,7): G.append((a,b))
for v in range(3,8):
    for t in range(3): G.append((t,v))
assert len(G)==24
Z=forest_count_partition(8,tuple(G))
# transfer cross-check for the total count only
row=rm(Q0,atom_by_name['K4']['get'](())); row=rm(row,S)
assert Z==rv(row,one)==177186
onecnt=[]
for i in range(len(G)):
    n,e=contract_graph(8,G,[i]); onecnt.append(forest_count_partition(n,e))
mins=None; maxs=None; argmin=None; argmax=None
for i in range(len(G)):
    for j in range(i+1,len(G)):
        n,e=contract_graph(8,G,[i,j]); two=forest_count_partition(n,e)
        D=onecnt[i]*onecnt[j]-Z*two
        if mins is None or D<mins:
            mins=D; argmin=(i,j)
        if maxs is None or D>maxs:
            maxs=D; argmax=(i,j)
assert mins==8118180 and maxs==1320302284
print('independent partition/Kirchhoff check K3 join (K4 disjoint K1): forests=',Z)
print(' independent all-pairs min gap=',mins,'pair=',argmin,'max gap=',maxs,'pair=',argmax)
print('ALL_EXACT_CHECKS_PASS')
