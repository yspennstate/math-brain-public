# Archive reproducer for the exact staged computation executed in this run.
# The runtime calculations were executed incrementally; this monolithic form preserves the same exact routines/assertions.
from itertools import product, permutations, combinations
from functools import lru_cache
import collections
import sympy as sp

# Exact partition utilities.
def canon(labels):
    mp={}; out=[]; nxt=0
    for a in labels:
        if a not in mp:
            mp[a]=nxt; nxt+=1
        out.append(mp[a])
    return tuple(out)

def union_part(labels,a,b):
    labels=list(labels)
    if labels[a]==labels[b]: return None
    la,lb=labels[a],labels[b]
    return canon([la if q==lb else q for q in labels])

def introduce(labels): return canon(tuple(labels)+(max(labels,default=-1)+1,))
def forget(labels,idx): return canon(tuple(q for i,q in enumerate(labels) if i!=idx))

def all_partitions(n):
    out=[]
    def rec(pref,mx):
        if len(pref)==n:
            out.append(tuple(pref)); return
        for z in range(mx+2):
            pref.append(z); rec(pref,max(mx,z)); pref.pop()
    rec([0],0)
    return [canon(x) for x in out]

ST=[canon((0,1,2)),canon((0,1,1)),canon((0,0,1)),canon((0,1,0)),canon((0,0,0))]
P4=all_partitions(4); assert len(P4)==15
p4idx={s:i for i,s in enumerate(P4)}

# Three terminals plus retained spider center.
def start_center_matrix(req_terms=()):
    req=set(req_terms); M=sp.zeros(5,15)
    for si,ts in enumerate(ST):
        lab=introduce(ts)
        stage=[(t,t,3) for t in range(3)]
        for bits in product((0,1),repeat=3):
            if any(t in req and not bit for bit,(t,_,__) in zip(bits,stage)): continue
            cur=lab; ok=True
            for bit,(_,a,b) in zip(bits,stage):
                if bit:
                    cur=union_part(cur,a,b)
                    if cur is None: ok=False; break
            if ok: M[si,p4idx[cur]]+=1
    return M

# Direct leg of length 1: center--d, and d joined to three terminals.
def direct_matrix(req_edges=()):
    req=set(req_edges); M=sp.zeros(15)
    for si,lab in enumerate(P4):
        lab2=introduce(lab)
        stage=[(('di',),3,4)]+[(('ds',t),t,4) for t in range(3)]
        for bits in product((0,1),repeat=4):
            if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)): continue
            cur=lab2; ok=True
            for bit,(eid,a,b) in zip(bits,stage):
                if bit:
                    cur=union_part(cur,a,b)
                    if cur is None: ok=False; break
            if ok: M[si,p4idx[forget(cur,4)]]+=1
    return M

# Subdivided leg of length 2: center--b--x, with b,x each joined to three terminals.
def subdiv_matrix(req_edges=()):
    req=set(req_edges); M=sp.zeros(15)
    for si,lab in enumerate(P4):
        lab1=introduce(lab); lab2=introduce(lab1)
        stage=[(('i1',),3,4)]+[(('b',t),t,4) for t in range(3)] + [(('i2',),4,5)] + [(('x',t),t,5) for t in range(3)]
        for bits in product((0,1),repeat=8):
            if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)): continue
            cur=lab2; ok=True
            for bit,(eid,a,b) in zip(bits,stage):
                if bit:
                    cur=union_part(cur,a,b)
                    if cur is None: ok=False; break
            if ok:
                cur=forget(cur,5); cur=forget(cur,4)
                M[si,p4idx[cur]]+=1
    return M

Close=sp.zeros(15,5)
for i,lab in enumerate(P4): Close[i,ST.index(forget(lab,3))]+=1
Start=start_center_matrix()
L=direct_matrix(); B=subdiv_matrix()
J=L-5*sp.eye(15); K=B-28*sp.eye(15)
assert J**4==sp.zeros(15) and K**4==sp.zeros(15)
assert (J.rank(),(J**2).rank(),(J**3).rank(),(J**4).rank())==(8,2,1,0)
assert (K.rank(),(K**2).rank(),(K**3).rank(),(K**4).rank())==(8,2,1,0)
assert J*K==K*J
assert J*K**2 == sp.Rational(31,270)*K**3
assert J**2*K == sp.Rational(76,6075)*K**3
assert J**3 == sp.Rational(8,6075)*K**3

# Seven-dimensional algebra check.
vecs=[]
for M in [sp.eye(15),K,K**2,K**3,J,J*K,J**2]: vecs.append(M.reshape(225,1))
assert sp.Matrix.hstack(*vecs).rank()==7

# Terminal nilpotent algebra.
S=Start*Close; N=S-4*sp.eye(5); assert N**3==sp.zeros(5)
N2=N*N; ones=sp.Matrix([1]*5); N1=N*ones; N2one=N2*ones; Q0=sp.Matrix([[1,0,0,0,0]])

p,q,u,v,h,X,Y=sp.symbols('p q u v h X Y', integer=True, nonnegative=True)

def Jpow(r): return sp.eye(15)+r*J/5+sp.binomial(r,2)*J**2/25+sp.binomial(r,3)*J**3/125
def Kpow(r): return sp.eye(15)+r*K/28+sp.binomial(r,2)*K**2/(28**2)+sp.binomial(r,3)*K**3/(28**3)

@lru_cache(None)
def Tmix(psym,qsym,req_edges=()):
    center=[]; direct=collections.defaultdict(list); subdiv=collections.defaultdict(list)
    for e in req_edges:
        typ=e[0]
        if typ=='c': center.append(e[1])
        elif typ=='ds': direct[e[1]].append(('ds',e[2]))
        elif typ=='di': direct[e[1]].append(('di',))
        elif typ in ('b','x'): subdiv[e[1]].append((typ,e[2]))
        elif typ in ('i1','i2'): subdiv[e[1]].append((typ,))
        else: raise AssertionError(e)
    dkeys=sorted(direct); skeys=sorted(subdiv)
    dmap={old:i for i,old in enumerate(dkeys)}; smap={old:i for i,old in enumerate(skeys)}
    dreq=collections.defaultdict(list); sreq=collections.defaultdict(list)
    for old,rs in direct.items(): dreq[dmap[old]].extend(rs)
    for old,rs in subdiv.items(): sreq[smap[old]].extend(rs)
    kd=len(dkeys); ks=len(skeys)
    M=start_center_matrix(tuple(center))
    for i in range(kd): M=M*direct_matrix(tuple(dreq[i]))
    for i in range(ks): M=M*subdiv_matrix(tuple(sreq[i]))
    return sp.simplify(M*Jpow(psym-kd)*Kpow(qsym-ks)*Close/(5**kd*28**ks))

Tun=Tmix(p,q)
A=sp.factor(Tun[0,0]); BB=sp.factor(Tun[0,1]); C=sp.factor((Tun[0,4]-Tun[0,1])/6)
A_expected=(42*p+45*q+280)/70
B_expected=(1568*p**2+4830*p*q+12152*p+3375*q**2+22875*q+9800)/9800
C_expected=(175616*p**3+893760*p**2*q+1393952*p**2+1464750*p*q**2+5403090*p*q+1174432*p+759375*q**3+5229375*q**2+2341250*q)/8232000
assert sp.simplify(A-A_expected)==0 and sp.simplify(BB-B_expected)==0 and sp.simplify(C-C_expected)==0
rho=sp.factor((BB/A)/2-(C/A)/(BB/A))
rho_expected=(6607552*p**3+27462540*p**2*q+95579008*p**2+36092700*p*q**2+287818860*p*q+385696640*p+15271875*q**3+198665625*q**2+689500000*q+288120000)/(840*(42*p+45*q+280)*(1568*p**2+4830*p*q+12152*p+3375*q**2+22875*q+9800))
assert sp.simplify(rho-rho_expected)==0
lo=sp.Rational(43,360); hi=sp.Rational(1,8)
assert sp.simplify((hi-rho)-(153664*p**3+623280*p**2*q+2055256*p**2+806400*p*q**2+6240045*p*q+7395080*p+337500*q**3+4321875*q**2+14665000*q)/(420*(42*p+45*q+280)*(1568*p**2+4830*p*q+12152*p+3375*q**2+22875*q+9800)))==0
assert sp.simplify((rho-lo)-(8820*p**2*q+96040*p**2+18900*p*q**2+259959*p*q+902776*p+10125*q**3+171000*q**2+785400*q+3841600)/(252*(42*p+45*q+280)*(1568*p**2+4830*p*q+12152*p+3375*q**2+22875*q+9800)))==0

# Rayleigh response polynomial machinery.
def triple(row): return ((row*ones)[0],(row*N1)[0],(row*N2one)[0])
def prod_aff(a,b):
    mons=[(0,0),(1,0),(0,1)]; d=collections.defaultdict(lambda:0)
    for i,aa in enumerate(a):
        for j,bb in enumerate(b): d[(mons[i][0]+mons[j][0],mons[i][1]+mons[j][1])]+=sp.expand(aa*bb)
    return d
def delta_q(ts):
    x1=prod_aff(ts[1],ts[2]); x2=prod_aff(ts[0],ts[3]); out={}
    for k in set(x1)|set(x2):
        z=sp.factor(x1.get(k,0)-x2.get(k,0))
        if z!=0: out[k]=z
    return out

@lru_cache(None)
def q_same(e,f):
    ts=[]
    for mask in range(4):
        req=() if mask==0 else (e,) if mask==1 else (f,) if mask==2 else (e,f)
        ts.append(triple(Q0*Tmix(p,q,req)))
    return delta_q(ts)

# K1 singleton component is Tmix(0,0).
@lru_cache(None)
def Tsingleton(req_edges=()): return Tmix(sp.Integer(0),sp.Integer(0),req_edges)
@lru_cache(None)
def q_mixed_single(e,f):
    ts=[]
    for mask in range(4):
        M1=Tmix(p,q,(e,) if mask&1 else ())
        M2=Tsingleton((f,) if mask&2 else ())
        ts.append(triple(Q0*M1*M2))
    return delta_q(ts)

def q_single_same():
    e=('c',0); f=('c',1); ts=[]
    for mask in range(4):
        req=() if mask==0 else (e,) if mask==1 else (f,) if mask==2 else (e,f)
        ts.append(triple(Q0*Tsingleton(req)))
    return delta_q(ts)
def q_single_cross(e,f):
    ts=[]
    for mask in range(4):
        M1=Tsingleton((e,) if mask&1 else ())
        M2=Tsingleton((f,) if mask&2 else ())
        ts.append(triple(Q0*M1*M2))
    return delta_q(ts)

# Orbit generation for pairs inside one mixed spider.
terms=list(permutations(range(3)))
def edges_mixed(pd=2,qs=2):
    E=[('c',t) for t in range(3)]
    for i in range(pd): E += [('ds',i,t) for t in range(3)]+[('di',i)]
    for j in range(qs): E += [('b',j,t) for t in range(3)]+[('x',j,t) for t in range(3)]+[('i1',j),('i2',j)]
    return E

def map_edge(e,tp,dp,spm):
    typ=e[0]
    if typ=='c': return ('c',tp[e[1]])
    if typ=='ds': return ('ds',dp[e[1]],tp[e[2]])
    if typ=='di': return ('di',dp[e[1]])
    if typ in ('b','x'): return (typ,spm[e[1]],tp[e[2]])
    return (typ,spm[e[1]])

def canon_same(e,f):
    imgs=[]
    for tp in terms:
        for dpt in permutations(range(2)):
            dp={i:dpt[i] for i in range(2)}
            for spt in permutations(range(2)):
                spm={i:spt[i] for i in range(2)}
                ee=map_edge(e,tp,dp,spm); ff=map_edge(f,tp,dp,spm)
                imgs.append(tuple(sorted((ee,ff),key=repr)))
    return min(imgs,key=repr)

same_orbits={}
for e,f in combinations(edges_mixed(),2): same_orbits.setdefault(canon_same(e,f),(e,f))
assert len(same_orbits)==48
same_reps=[]
for e,f in same_orbits.values():
    ds=[z[1] for z in (e,f) if z[0] in ('ds','di')]
    ss=[z[1] for z in (e,f) if z[0] in ('b','x','i1','i2')]
    p0=max(ds)+1 if ds else 0; q0=max(ss)+1 if ss else 0
    same_reps.append((e,f,p0,q0))

# Mixed-spider edge versus a spoke in a separate singleton component.
Eone=[('c',t) for t in range(3)]+[('ds',0,t) for t in range(3)]+[('di',0)]+[('b',0,t) for t in range(3)]+[('x',0,t) for t in range(3)]+[('i1',0),('i2',0)]
def map_one(e,tp):
    if e[0]=='c': return ('c',tp[e[1]])
    if e[0] in ('ds','b','x'): return (e[0],0,tp[e[2]])
    return e
mixed_single_orbits={}
for e in Eone:
    for f in [('c',t) for t in range(3)]:
        c=min([(map_one(e,tp),('c',tp[f[1]])) for tp in terms],key=repr)
        mixed_single_orbits.setdefault(c,(e,f))
assert len(mixed_single_orbits)==11

# Strip certificate helpers.
def strip_coeffs(qd):
    c=[sp.Integer(0)]*5
    for (iu,iv),coef in qd.items():
        if iv==0: c[iu]+=coef
        elif iv==1: c[iu+2]+=coef/2; c[iu+1]-=coef*h
        elif iv==2: c[iu+4]+=coef/4; c[iu+3]-=coef*h; c[iu+2]+=coef*h*h
        else: raise AssertionError
    return [sp.factor(z) for z in c]

def bern(expr):
    b0=sp.factor(expr.subs(h,lo)); b2=sp.factor(expr.subs(h,hi))
    b1=sp.factor(b0+sp.diff(expr,h).subs(h,lo)*(hi-lo)/2)
    return [b0,b1,b2]

def shifted_nonnegative(expr,p0,q0):
    ex=sp.cancel(expr.subs({p:p0+X,q:q0+Y})); num,den=sp.fraction(ex)
    assert not den.free_symbols
    if den<0: num=-num
    P=sp.Poly(sp.expand(num),X,Y)
    return all(c>=0 for c in P.coeffs())

def regular(qd,p0,q0):
    for expr in strip_coeffs(qd):
        if expr==0: continue
        for b in bern(expr):
            if not shifted_nonnegative(b,p0,q0): return False
    return True

def discriminant(qd,p0,q0):
    sc=strip_coeffs(qd)
    q02=qd.get((0,2),0); q20=qd.get((2,0),0); q01=qd.get((0,1),0); q11=qd.get((1,1),0)
    KD=sp.factor(q02*(q20+q01/2)-q11*q11/4)
    assert q02!=0 and shifted_nonnegative(q02,p0,q0)
    assert KD!=0 and shifted_nonnegative(KD,p0,q0)
    assert shifted_nonnegative(sc[0],p0,q0)
    assert all(shifted_nonnegative(b,p0,q0) for b in bern(sc[1]))
    assert sp.factor(4*sc[4]*sc[2]-sc[3]**2-KD)==0
    return KD

regular_count=0; discrim=[]; zero_constant=[]
for e,f,p0,q0 in same_reps:
    qd=q_same(e,f)
    if regular(qd,p0,q0): regular_count+=1
    else: discrim.append((e,f,p0,q0,discriminant(qd,p0,q0)))
    if sp.factor(qd.get((0,0),0).subs({p:p0,q:q0}))==0: zero_constant.append((e,f,p0,q0))
assert regular_count==41 and len(discrim)==7
assert zero_constant==[(('c',0),('c',1),0,0)] or zero_constant==[(('c',0),('c',1),0,0)]

ms_regular=0
for e,f in mixed_single_orbits.values():
    p0=0 if e[0]=='c' else (1 if e[0] in ('ds','di') else 0)
    q0=0 if e[0] in ('c','ds','di') else 1
    assert regular(q_mixed_single(e,f),p0,q0); ms_regular+=1
assert ms_regular==11

# Singleton-only marked cases on the same strip.
for qd in [q_single_same(),q_single_cross(('c',0),('c',0)),q_single_cross(('c',0),('c',1))]:
    assert regular(qd,0,0)

# The equality case p=q=r=0 is K_{3,1}; if an unmarked atom remains, the center-center pair gains +4u+... .
cc=None
for e,f,p0,q0 in same_reps:
    if {e,f}=={('c',0),('c',1)} and p0==0 and q0==0:
        cc=q_same(e,f); break
assert cc is not None
ccsc=[sp.factor(z.subs({p:0,q:0})) for z in strip_coeffs(cc)]
assert ccsc[0]==0 and ccsc[1]==4

# Exact first branching member past the complete-nine baseline: p=0,q=3,r=0.
fac=28**3
Z=sp.factor((Q0*Tmix(p,q).subs({p:0,q:3})*ones)[0]*fac)
physical=[]
for e,f,p0,q0 in same_reps:
    if 0>=p0 and 3>=q0:
        val=sp.factor(q_same(e,f).get((0,0),0).subs({p:0,q:3})*fac**2)
        physical.append((val,e,f))
min_gap=min(physical,key=lambda z: sp.N(z[0]))
assert Z==2298452 and min_gap[0]==573003024

print('DIRECT_OPERATOR eigenvalue 5 nilpotent_ranks', (J.rank(),(J**2).rank(),(J**3).rank(),(J**4).rank()))
print('SUBDIV_OPERATOR eigenvalue 28 nilpotent_ranks', (K.rank(),(K**2).rank(),(K**3).rank(),(K**4).rank()))
print('COMMUTE', J*K==K*J)
print('ALGEBRA_RELATIONS', 'JK2=31/270 K3', 'J2K=76/6075 K3', 'J3=8/6075 K3', 'dimension=7')
print('A_pq =', A)
print('B_pq =', BB)
print('C_pq =', C)
print('rho_pq =', rho)
print('rho_minus_43_360 =', sp.factor(rho-lo))
print('one_8_minus_rho =', sp.factor(hi-rho))
print('SAME_MIXED_ORBITS', len(same_reps), 'regular', regular_count, 'discriminant', len(discrim))
for item in discrim:
    print('DISCRIM', item[0], item[1], 'p0q0', (item[2],item[3]), 'K=', item[4])
print('MIXED_SINGLETON_ORBITS', ms_regular, 'regular', ms_regular)
print('SINGLETON_ONLY_SCHEMES', 3, 'regular', 3)
print('ZERO_CONSTANT_CASES', zero_constant)
print('BRANCHING_CHECK p=0 q=3 r=0 vertices=10 edges=27 forests=', Z, 'min_gap=', min_gap[0], 'pair=', min_gap[1], min_gap[2])
print('ALL_EXACT_CHECKS_PASS')