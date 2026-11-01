from itertools import combinations, product, permutations
from functools import lru_cache
from fractions import Fraction
import collections, time
import sympy as sp

# Exact five-state three-terminal partition algebra and exact path/cycle frontier DPs.
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

@lru_cache(None)
def transfer_cycle(L,reqt=()):
    assert L>=3
    req=set(reqt); M=[[0]*5 for _ in range(5)]
    for si,ts in enumerate(ST):
        # Keep terminals and vertex 0. Add its three spokes.
        dp={introduce(ts):1}
        nd=collections.defaultdict(int); stage=[(('s',0,t),t,3) for t in range(3)]
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
        # Add vertex 1; keep terminals, vertex 0, and current endpoint.
        nd=collections.defaultdict(int)
        for lab,cnt in dp.items():
            lab2=introduce(lab)
            stage=[(('i',0,1),3,4)]+[(('s',1,t),t,4) for t in range(3)]
            for bits in product((0,1),repeat=4):
                if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)): continue
                cur=lab2; ok=True
                for bit,(eid,a,b) in zip(bits,stage):
                    if bit:
                        cur=union_part(cur,a,b)
                        if cur is None: ok=False; break
                if ok: nd[cur]+=cnt
        dp=nd
        # Extend tail; frontier is terminals + first vertex + previous endpoint.
        for i in range(2,L):
            nd=collections.defaultdict(int)
            for lab,cnt in dp.items():
                lab2=introduce(lab)
                stage=[(('i',i-1,i),4,5)]+[(('s',i,t),t,5) for t in range(3)]
                for bits in product((0,1),repeat=4):
                    if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)): continue
                    cur=lab2; ok=True
                    for bit,(eid,a,b) in zip(bits,stage):
                        if bit:
                            cur=union_part(cur,a,b)
                            if cur is None: ok=False; break
                    if ok: nd[forget(cur,4)]+=cnt
            dp=nd
        # Close last endpoint to vertex 0, then forget both right frontier vertices.
        nd=collections.defaultdict(int); close=('i',0,L-1)
        for lab,cnt in dp.items():
            for bit in (0,1):
                if close in req and not bit: continue
                cur=lab
                if bit:
                    cur=union_part(cur,3,4)
                    if cur is None: continue
                cur=forget(forget(cur,4),3); nd[cur]+=cnt
        for lab,cnt in nd.items(): M[si][ST.index(lab)]+=cnt
    return tuple(tuple(r) for r in M)

def mm(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def rm(r,M): return tuple(sum(r[k]*M[k][j] for k in range(len(r))) for j in range(len(M[0])))
def rv(r,c): return sum(r[i]*c[i] for i in range(len(r)))
I=tuple(tuple(1 if i==j else 0 for j in range(5)) for i in range(5))
S=transfer_path(1)
N=tuple(tuple(S[i][j]-4*I[i][j] for j in range(5)) for i in range(5)); N2=mm(N,N); N3=mm(N2,N)
assert N3==tuple(tuple(0 for _ in range(5)) for _ in range(5))
one=(1,1,1,1,1); None1=tuple(rv(N[i],one) for i in range(5)); None2=tuple(rv(N2[i],one) for i in range(5)); Q0=(1,0,0,0,0)

def decompose(M):
    A=M[0][0]; B=M[0][1]; C=Fraction(M[0][4]-B,6)
    assert all(Fraction(M[i][j])==A*I[i][j]+B*N[i][j]+C*N2[i][j] for i in range(5) for j in range(5))
    a=Fraction(B,A); c=C/Fraction(A); rho=(a*a/2-c)/a
    return A,B,C,rho

# ---------- New 52-state cycle-tail operator and all-length recurrence ----------
def all_partitions(n):
    out=[]
    def rec(pref,mx):
        if len(pref)==n:
            out.append(tuple(pref)); return
        for z in range(mx+2):
            pref.append(z); rec(pref,max(mx,z)); pref.pop()
    rec([0],0)
    return [canon(x) for x in out]

P5=all_partitions(5)
assert len(P5)==52 and len(set(P5))==52
pindex={s:i for i,s in enumerate(P5)}

def extend_frontier_state(lab):
    # One unmarked new cycle vertex: edge prev-new plus 3 spokes, then forget prev.
    out=collections.defaultdict(int); lab2=introduce(lab)
    stage=[('tail',4,5)]+[(f's{t}',t,5) for t in range(3)]
    for bits in product((0,1),repeat=4):
        cur=lab2; ok=True
        for bit,(_,a,b) in zip(bits,stage):
            if bit:
                cur=union_part(cur,a,b)
                if cur is None: ok=False; break
        if ok: out[forget(cur,4)]+=1
    return out

E=[[0]*52 for _ in range(52)]
for i,lab in enumerate(P5):
    for out,cnt in extend_frontier_state(lab).items(): E[i][pindex[out]]+=cnt
E=sp.Matrix(E)
Id52=sp.eye(52)
P=E**3-7*E**2+8*E-2*Id52  # p(E), p(lambda)=(lambda-1)(lambda^2-6lambda+2)
P2=P*P; P3=P2*P
assert P3==sp.zeros(52) and P2!=sp.zeros(52)
ranks=(P.rank(),P2.rank(),P3.rank())
assert ranks==(20,5,0)

# p, p^2, p^3 recurrence coefficients in ascending-lag recurrence form:
# X_n = c1 X_{n-1}+...+cd X_{n-d}.
def recurrence_from_poly(poly):
    d=len(poly)-1; assert poly[-1]==1
    return tuple(-poly[d-j] for j in range(1,d+1))

def conv(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    return z
p=[-2,8,-7,1]
p2=conv(p,p); p3=conv(p2,p)
recA=recurrence_from_poly(p)
recB=recurrence_from_poly(p2)
recC=recurrence_from_poly(p3)
assert recA==(7,-8,2)
assert recB==(14,-65,116,-92,32,-4)
assert recC==(21,-171,685,-1452,1734,-1196,468,-96,8)

ABCcycle={n:decompose(transfer_cycle(n))[:3] for n in range(3,26)}

def residual(seq,rec,n):
    return seq[n]-sum(rec[j-1]*seq[n-j] for j in range(1,len(rec)+1))
Aseq={n:ABCcycle[n][0] for n in ABCcycle}; Bseq={n:ABCcycle[n][1] for n in ABCcycle}; Cseq={n:ABCcycle[n][2] for n in ABCcycle}
# Nine consecutive zero residuals suffice for A and B because every residual is a matrix
# coefficient of powers of E and therefore itself obeys the order-9 p^3 recurrence.
assert all(residual(Aseq,recA,n)==0 for n in range(6,15))
assert all(residual(Bseq,recB,n)==0 for n in range(9,18))
# C recurrence is directly the p(E)^3 annihilator; check all available starting values too.
assert all(residual(Cseq,recC,n)==0 for n in range(12,26))

# ---------- Local-to-global response strip certificate for paths P1..P11 and cycles C3..C8 ----------
MAXP=11; MAXC=8
PERMS=list(permutations(range(3)))
def edges_P(L): return [('s',i,t) for i in range(L) for t in range(3)]+[('i',i,i+1) for i in range(L-1)]
def edges_C(L): return [('s',i,t) for i in range(L) for t in range(3)]+[('i',min(i,(i+1)%L),max(i,(i+1)%L)) for i in range(L)]
def trP(e,L,p,rev):
    k,a,b=e
    if k=='s': return ('s',L-1-a if rev else a,p[b])
    i,j=a,b
    if rev: i,j=L-1-j,L-1-i
    return ('i',i,j)
def key_sameP(pair,L): return min(tuple(sorted((trP(pair[0],L,p,r),trP(pair[1],L,p,r)),key=repr)) for p in PERMS for r in (0,1))
def key_crossP(e,L,f,M):
    vals=[]
    for p in PERMS:
        for r1 in (0,1):
            for r2 in (0,1):
                a,b=trP(e,L,p,r1),trP(f,M,p,r2)
                vals.append(((L,a),(M,b)) if L<M else tuple(sorted(((L,a),(L,b)),key=repr)))
    return min(vals,key=repr)
def path_reps():
    out=[]
    for L in range(1,MAXP+1):
        seen={}
        for pair in combinations(edges_P(L),2): seen.setdefault(key_sameP(pair,L),pair)
        out += [('sameP',L,L,*pair) for pair in seen.values()]
    for L in range(1,MAXP+1):
        for M in range(L,MAXP+1):
            seen={}
            for e in edges_P(L):
                for f in edges_P(M): seen.setdefault(key_crossP(e,L,f,M),(e,f))
            out += [('crossP',L,M,e,f) for e,f in seen.values()]
    return out

def cycle_reps_raw():
    # Raw cyclic/mixed representatives are intentionally retained: finite local enumeration,
    # followed by exact polynomial deduplication, is simpler and less error-prone than quotienting
    # all dihedral/terminal symmetries in this checker.
    out=[]
    for L in range(3,MAXC+1):
        ed=edges_C(L)
        for e,f in combinations(ed,2): out.append(('sameC',L,L,e,f))
    for L in range(3,MAXC+1):
        for M in range(L,MAXC+1):
            for e in edges_C(L):
                for f in edges_C(M): out.append(('crossC',L,M,e,f))
    for L in range(3,MAXC+1):
        for M in range(1,MAXP+1):
            for e in edges_C(L):
                for f in edges_P(M): out.append(('crossCP',L,M,e,f))
    return out

@lru_cache(None)
def singleP(L,e): return transfer_path(L,(e,))
@lru_cache(None)
def pairP(L,e,f): return transfer_path(L,tuple(sorted((e,f),key=repr)))
@lru_cache(None)
def singleC(L,e): return transfer_cycle(L,(e,))
@lru_cache(None)
def pairC(L,e,f): return transfer_cycle(L,tuple(sorted((e,f),key=repr)))
def triple(row): return (rv(row,one),rv(row,None1),rv(row,None2))
def prod_aff(a,b):
    d=collections.defaultdict(int); mons=[(0,0),(1,0),(0,1)]
    for i,x in enumerate(a):
        for j,z in enumerate(b): d[(mons[i][0]+mons[j][0],mons[i][1]+mons[j][1])]+=x*z
    return d
def delta_q(ts):
    q=prod_aff(ts[1],ts[2]); m=prod_aff(ts[0],ts[3])
    for k,z in m.items(): q[k]-=z
    return {k:z for k,z in q.items() if z}

def qrep(rep):
    typ,L,M,e,f=rep; ts=[]
    for mask in range(4):
        row=Q0
        if typ=='sameP':
            mat=transfer_path(L) if mask==0 else singleP(L,e) if mask==1 else singleP(L,f) if mask==2 else pairP(L,e,f)
            row=rm(row,mat)
        elif typ=='crossP':
            row=rm(row,singleP(L,e) if mask&1 else transfer_path(L)); row=rm(row,singleP(M,f) if mask&2 else transfer_path(M))
        elif typ=='sameC':
            mat=transfer_cycle(L) if mask==0 else singleC(L,e) if mask==1 else singleC(L,f) if mask==2 else pairC(L,e,f)
            row=rm(row,mat)
        elif typ=='crossC':
            row=rm(row,singleC(L,e) if mask&1 else transfer_cycle(L)); row=rm(row,singleC(M,f) if mask&2 else transfer_cycle(M))
        else:
            row=rm(row,singleC(L,e) if mask&1 else transfer_cycle(L)); row=rm(row,singleP(M,f) if mask&2 else transfer_path(M))
        ts.append(triple(row))
    return delta_q(ts)

rhop={L:decompose(transfer_path(L))[3] for L in range(1,MAXP+1)}
rhoc={L:decompose(transfer_cycle(L))[3] for L in range(3,MAXC+1)}
assert all(rhop[L]>rhop[L+1]>0 for L in range(1,MAXP))
assert all(rhoc[L]>rhoc[L+1]>0 for L in range(3,MAXC))
assert rhoc[MAXC] < rhop[MAXP] < rhop[1]==Fraction(1,8)
lo=rhoc[MAXC]; hi=Fraction(1,8)

def strip_coeffs(q):
    c=[[Fraction(0),Fraction(0),Fraction(0)] for _ in range(5)]
    for (iu,iv),coef0 in q.items():
        coef=Fraction(coef0)
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
    return b0,b1,b2
def discriminant_K(q):
    q02=Fraction(q.get((0,2),0)); q20=Fraction(q.get((2,0),0)); q01=Fraction(q.get((0,1),0)); q11=Fraction(q.get((1,1),0))
    return q02*(q20+q01/2)-q11*q11/4

t0=time.time(); PR=path_reps(); CR=cycle_reps_raw(); reps=PR+CR
unique={}
for rep in reps:
    q=qrep(rep); unique.setdefault(tuple(sorted(q.items())),(rep,q))
counts=collections.Counter(); failures=[]; minK=None
for rep,q in unique.values():
    sc=strip_coeffs(q); allb=[]
    for pol in sc:
        if pol!=(0,0,0): allb.extend(bern_h(pol))
    if sc[0][0]>0 and all(b>=0 for b in allb):
        counts['regular']+=1; continue
    if sc[0]==(0,0,0):
        ok=all(pol==(0,0,0) or all(b>=0 for b in bern_h(pol)) for pol in sc[1:])
        if ok and all(b>0 for b in bern_h(sc[1])):
            counts['zero']+=1; continue
    q02=Fraction(q.get((0,2),0)); K=discriminant_K(q)
    if q02>0 and K>0 and sc[0][0]>0 and all(b>=0 for b in bern_h(sc[1])):
        # Exact h-cancellation check of 4*c4*c2-c3^2=K.
        c4,c3,c2=sc[4],sc[3],sc[2]
        def pmul(a,b):
            z=[Fraction(0)]*5
            for i,x in enumerate(a):
                for j,y in enumerate(b): z[i+j]+=x*y
            return z
        lhs=[4*x for x in pmul(c4,c2)]; rhs=pmul(c3,c3); D=[lhs[i]-rhs[i] for i in range(5)]
        assert D[0]==K and all(x==0 for x in D[1:])
        counts['disc']+=1; minK=K if minK is None else min(minK,K); continue
    failures.append((rep,q,K))

assert len(PR)==3478
assert len(reps)==48704
assert len(unique)==4654
assert counts==collections.Counter({'regular':4571,'disc':82,'zero':1})
assert minK==207792
assert not failures

# Concrete first C8-only member G = bar(K3) join C8: exact forest count and minimum Rayleigh numerator.
TC8=transfer_cycle(8); Z=rv(rm(Q0,TC8),one); gaps=[]
for e,f in combinations(edges_C(8),2):
    Ze=rv(rm(Q0,singleC(8,e)),one); Zf=rv(rm(Q0,singleC(8,f)),one); Zef=rv(rm(Q0,pairC(8,e,f)),one)
    gaps.append(Ze*Zf-Z*Zef)
min_gap=min(gaps)
assert min_gap>0

print('cycle_tail_states',len(P5))
print('p(lambda)','lambda^3-7lambda^2+8lambda-2=(lambda-1)(lambda^2-6lambda+2)')
print('rank_pE_pE2_pE3',ranks)
print('cycle_A_recurrence',recA)
print('cycle_B_recurrence',recB)
print('cycle_C_recurrence',recC)
for L in range(3,MAXC+1):
    A,B,C,r=decompose(transfer_cycle(L)); print('C%d_transfer'%L,A,B,C,'rho',r)
print('strip',lo,hi)
print('local_reps',len(reps),'unique_polynomials',len(unique))
print('certificate_counts',dict(counts),'min_positive_K',minK,'failures',len(failures))
print('C8_physical','vertices',11,'edges',32,'forests',Z,'min_gap',min_gap)
print('elapsed_s',round(time.time()-t0,3))
print('ALL_EXACT_CHECKS_PASS')
