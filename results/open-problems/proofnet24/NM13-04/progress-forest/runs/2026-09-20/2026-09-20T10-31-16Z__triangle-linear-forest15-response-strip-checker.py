from itertools import combinations, product, permutations
from functools import lru_cache
from fractions import Fraction
import collections, sys, time, math
import sympy as sp

# NM13-04 / T07 exact checker for the triangle-seeded response-strip theorem.
# It certifies K3 join H for every linear forest H whose path components have
# order at most maxL (default 15). The finite computation is only a complete
# local marked-edge orbit classification; component multiplicities are unbounded
# and are handled analytically by the 2D response strip.

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
            nd=collections.defaultdict(int); stage=[(('i',i-1,i),3,4)]+[(('s',i,t),t,4) for t in range(3)]
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
S=transfer_path(1); N=tuple(tuple(S[i][j]-4*I[i][j] for j in range(5)) for i in range(5)); N2=mm(N,N); N3=mm(N2,N); assert N3==tuple(tuple(0 for j in range(5)) for i in range(5))
one=(1,1,1,1,1); None2=tuple(rv(N2[i],one) for i in range(5)); None1=tuple(rv(N[i],one) for i in range(5))

def qcore(req=()):
    req={tuple(sorted(e)) for e in req}; tri=[(0,1),(0,2),(1,2)]; counts=[0]*5
    for bits in product((0,1),repeat=3):
        chosen=[tri[i] for i,b in enumerate(bits) if b]
        if not req.issubset(chosen): continue
        if len(chosen)==3: continue
        par=list(range(3))
        def fd(x):
            while par[x]!=x: par[x]=par[par[x]]; x=par[x]
            return x
        def jn(a,b):
            a,b=fd(a),fd(b)
            if a!=b: par[b]=a
        for a,b in chosen: jn(a,b)
        counts[ST.index(canon(tuple(fd(i) for i in range(3))))]+=1
    return tuple(counts)
Q0=qcore(); assert Q0==(1,1,1,1,3)
CORE=[('c',0,1),('c',0,2),('c',1,2)]
def edges_L(L): return [('s',i,t) for i in range(L) for t in range(3)]+[('i',i,i+1) for i in range(L-1)]
def tright(e,L,p,rev):
    k,a,b=e
    if k=='s': return ('s',L-1-a if rev else a,p[b])
    i,j=a,b
    if rev: i,j=L-1-j,L-1-i
    return ('i',i,j)
def tcore(e,p):
    _,a,b=e; a,b=p[a],p[b]; return ('c',min(a,b),max(a,b))
PERMS=list(permutations(range(3)))
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
def crkey(c,e,L): return min(((tcore(c,p),tright(e,L,p,r)) for p in PERMS for r in (0,1)),key=repr)
def reps(maxL):
    out=[]; seen={}
    for pair in combinations(CORE,2):
        key=min((tuple(sorted([tcore(e,p) for e in pair],key=repr)) for p in PERMS),key=repr); seen.setdefault(key,pair)
    out += [('cc',0,0,*pair) for pair in seen.values()]
    for L in range(1,maxL+1):
        seen={}
        for c in CORE:
          for e in edges_L(L): seen.setdefault(crkey(c,e,L),(c,e))
        out += [('cr',0,L,c,e) for c,e in seen.values()]
    for L in range(1,maxL+1):
        seen={}
        for pair in combinations(edges_L(L),2): seen.setdefault(samekey(pair,L),pair)
        out += [('same',L,L,*pair) for pair in seen.values()]
    for L in range(1,maxL+1):
      EL=edges_L(L)
      for M in range(L,maxL+1):
        seen={}; EM=edges_L(M)
        for e in EL:
          for f in EM: seen.setdefault(crosskey(e,L,f,M),(e,f))
        out += [('cross',L,M,e,f) for e,f in seen.values()]
    return out

def triple_from_row(row): return (rv(row,one),rv(row,None1),rv(row,None2))
@lru_cache(None)
def singleM(L,e): return transfer_path(L,(e,))
@lru_cache(None)
def pairM(L,e,f): return transfer_path(L,tuple(sorted((e,f),key=repr)))

def quantity(rep,mask):
    typ,L,M,e,f=rep
    if typ=='cc':
        req=[]
        if mask&1:req.append((e[1],e[2]))
        if mask&2:req.append((f[1],f[2]))
        row=qcore(req)
    elif typ=='cr':
        row=qcore(((e[1],e[2]),) if mask&1 else ())
        row=rm(row,singleM(M,f) if mask&2 else transfer_path(M))
    elif typ=='same':
        row=Q0
        if mask==0: mat=transfer_path(L)
        elif mask==1: mat=singleM(L,e)
        elif mask==2: mat=singleM(L,f)
        else: mat=pairM(L,e,f)
        row=rm(row,mat)
    else:
        row=Q0
        row=rm(row,singleM(L,e) if mask&1 else transfer_path(L))
        row=rm(row,singleM(M,f) if mask&2 else transfer_path(M))
    return triple_from_row(row)

def qcoeff(rep):
    ts=[quantity(rep,m) for m in range(4)]
    A,Ie,If,Ief=ts[0],ts[1],ts[2],ts[3]
    def prod(a,b):
        d=collections.defaultdict(int); mons=[(0,0),(1,0),(0,1)]
        for i,x in enumerate(a):
          for j,z in enumerate(b): d[(mons[i][0]+mons[j][0],mons[i][1]+mons[j][1])]+=x*z
        return d
    p=prod(Ie,If); m=prod(A,Ief)
    for k,z in m.items(): p[k]-=z
    return {k:z for k,z in p.items() if z}

def strip_coeffs(q):
    c=[[Fraction(0),Fraction(0),Fraction(0)] for _ in range(5)]
    for (iu,iv),coef in q.items():
        coef=Fraction(coef)
        if iv==0: c[iu][0]+=coef
        elif iv==1:
            c[iu+2][0]+=coef*Fraction(1,2); c[iu+1][1]-=coef
        elif iv==2:
            c[iu+4][0]+=coef*Fraction(1,4); c[iu+3][1]-=coef; c[iu+2][2]+=coef
        else: raise AssertionError
    return [tuple(z) for z in c]
def peval(p,x): return p[0]+p[1]*x+p[2]*x*x
def bern_h(p,lo,hi):
    d=hi-lo; b0=peval(p,lo); b2=peval(p,hi); deriv=p[1]+2*p[2]*lo; b1=b0+deriv*d/2
    return (b0,b1,b2)
def pscale(a,s): return tuple(x*s for x in a)
def pmul(a,b):
    z=[Fraction(0)]*5
    for i,x in enumerate(a):
      for j,y in enumerate(b): z[i+j]+=x*y
    while len(z)>1 and z[-1]==0:z.pop()
    return tuple(z)
def psub(a,b):
    n=max(len(a),len(b)); return tuple((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(n))

def run(maxL):
    t=time.time(); ABC={}; rhos={}
    for L in range(1,maxL+1):
        M=transfer_path(L); A=M[0][0]; B=M[0][1]; C=Fraction(M[0][4]-B,6); ABC[L]=(A,B,C)
        for i in range(5):
          for j in range(5): assert Fraction(M[i][j])==A*I[i][j]+B*N[i][j]+C*N2[i][j]
        a=Fraction(B,A); c=C/Fraction(A); rhos[L]=(a*a/2-c)/a
    assert all(rhos[L]>rhos[L+1]>0 for L in range(1,maxL))
    lo=min(rhos.values()); hi=max(rhos.values())
    rr=reps(maxL); print('maxL',maxL,'ABC_last',ABC[maxL],'rho_last',rhos[maxL]); print('reps',len(rr),'build_s',round(time.time()-t,2),flush=True)
    regular=0; exc=[]; minb=None; minc=None
    for idx,rep in enumerate(rr):
        sc=strip_coeffs(qcoeff(rep)); allb=[]
        for p in sc:
            if p!=(0,0,0): allb.extend(bern_h(p,lo,hi))
        const=sc[0][0]
        if all(b>=0 for b in allb) and const>0:
            regular+=1; minc=const if minc is None else min(minc,const)
            pos=[b for b in allb if b>0]
            if pos: minb=min(pos) if minb is None else min(minb,min(pos))
        else: exc.append((rep,sc))
        if idx%1000==0: print('processed',idx,flush=True)
    fail=[]; Dvals=[]; byL=collections.Counter()
    for rep,sc in exc:
        c0,c1,c2,c3,c4=sc
        ok=(c4[1:]==(0,0) and c4[0]>0 and all(b>0 for p in (c0,c1,c2) for b in bern_h(p,lo,hi)) and all(b>0 for b in bern_h(tuple(-x for x in c3),lo,hi)))
        D=psub(pscale(pmul(c4,c2),4),pmul(c3,c3))
        ok=ok and D[0]>0 and all(x==0 for x in D[1:])
        if ok:
            Dvals.append(D[0]); byL[rep[1]]+=1
        else: fail.append((rep,sc,D))
    print('regular',regular,'exceptions',len(exc),'certified',len(Dvals),'fail',len(fail))
    print('min_regular_constant',minc,'min_positive_bernstein',minb)
    print('exception_counts_by_path_length',dict(sorted(byL.items())))
    if Dvals: print('min_discriminant_margin',min(Dvals),'all_h_independent',True)
    old=[rep for rep in rr if max(rep[1],rep[2])<=7]
    oldexc=[rep for rep,sc in exc if max(rep[1],rep[2])<=7]
    print('max7_regression_reps',len(old),'exceptions',len(oldexc))
    assert len(old)==749 and len(oldexc)==13
    if maxL==15:
        assert len(rr)==11017 and regular==10814 and len(exc)==203 and not fail
        assert byL==collections.Counter({4:1,5:2,6:4,7:6,8:9,9:12,10:16,11:20,12:25,13:30,14:36,15:42})
        assert minc==2 and minb==1
    print('elapsed_s',round(time.time()-t,2))
    print('ALL_EXACT_CHECKS_PASS' if not fail else 'FAILURES_PRESENT')
    return fail

if __name__=='__main__': run(int(sys.argv[1]) if len(sys.argv)>1 else 15)
