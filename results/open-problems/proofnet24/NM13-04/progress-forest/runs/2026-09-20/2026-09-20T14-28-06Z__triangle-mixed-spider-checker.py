from itertools import product, permutations, combinations
from functools import lru_cache
import collections
import sympy as sp

# Exact partition utilities.
def canon(labels):
    mp={}; out=[]; nxt=0
    for a in labels:
        if a not in mp: mp[a]=nxt; nxt+=1
        out.append(mp[a])
    return tuple(out)

def union_part(labels,a,b):
    labels=list(labels)
    if labels[a]==labels[b]: return None
    la,lb=labels[a],labels[b]
    return canon([la if z==lb else z for z in labels])

def introduce(labels): return canon(tuple(labels)+(max(labels,default=-1)+1,))
def forget(labels,idx): return canon(tuple(z for i,z in enumerate(labels) if i!=idx))
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
Start=start_center_matrix(); L=direct_matrix(); B=subdiv_matrix()
J=L-5*sp.eye(15); K=B-28*sp.eye(15)
assert J**4==sp.zeros(15) and K**4==sp.zeros(15)
assert J*K==K*J
assert J*K**2 == sp.Rational(31,270)*K**3
assert J**2*K == sp.Rational(76,6075)*K**3
assert J**3 == sp.Rational(8,6075)*K**3
assert sp.Matrix.hstack(*[M.reshape(225,1) for M in [sp.eye(15),K,K**2,K**3,J,J*K,J**2]]).rank()==7

S=Start*Close; N=S-4*sp.eye(5); assert N**3==sp.zeros(5)
ones=sp.Matrix([1]*5); N1=N*ones; N2one=N*N*ones
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

@lru_cache(None)
def Tsingleton(req_edges=()): return Tmix(sp.Integer(0),sp.Integer(0),req_edges)

# Triangle seed and conditionals.
core_edges=[('core',0,1),('core',0,2),('core',1,2)]
def triangle_seed(req_core=()):
    req=set(req_core); counts=[0]*5
    for bits in product((0,1),repeat=3):
        if any(e in req and not bit for e,bit in zip(core_edges,bits)): continue
        if all(bits): continue
        lab=(0,1,2); ok=True
        for bit,e in zip(bits,core_edges):
            if bit:
                lab=union_part(lab,e[1],e[2])
                if lab is None: ok=False; break
        if ok: counts[ST.index(canon(lab))]+=1
    return sp.Matrix([counts])
assert list(triangle_seed())==[1,1,1,1,3]

def split_req(reqs):
    return tuple(e for e in reqs if e[0]=='core'), tuple(e for e in reqs if e[0]!='core')
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
        cr,rr=split_req(req)
        ts.append(triple(triangle_seed(cr)*Tmix(p,q,rr)))
    return delta_q(ts)
@lru_cache(None)
def q_mixed_single(e,f):
    ts=[]
    for mask in range(4):
        reqe=(e,) if mask&1 else (); reqf=(('c',f[1]),) if mask&2 else ()
        ts.append(triple(triangle_seed()*Tmix(p,q,reqe)*Tsingleton(reqf)))
    return delta_q(ts)
@lru_cache(None)
def q_core_mixed(e,f):
    ts=[]
    for mask in range(4):
        cr=(e,) if mask&1 else (); rr=(f,) if mask&2 else ()
        ts.append(triple(triangle_seed(cr)*Tmix(p,q,rr)))
    return delta_q(ts)
@lru_cache(None)
def q_core_single(e,f):
    ts=[]
    for mask in range(4):
        cr=(e,) if mask&1 else (); rr=(('c',f[1]),) if mask&2 else ()
        ts.append(triple(triangle_seed(cr)*Tsingleton(rr)))
    return delta_q(ts)
def q_core_core(e,f):
    ts=[]
    for mask in range(4):
        cr=() if mask==0 else (e,) if mask==1 else (f,) if mask==2 else (e,f)
        ts.append(triple(triangle_seed(cr)))
    return delta_q(ts)
def q_single_same(e,f):
    ts=[]
    for mask in range(4):
        rr=() if mask==0 else (('c',e[1]),) if mask==1 else (('c',f[1]),) if mask==2 else (('c',e[1]),('c',f[1]))
        ts.append(triple(triangle_seed()*Tsingleton(rr)))
    return delta_q(ts)
def q_single_cross(e,f):
    ts=[]
    for mask in range(4):
        M1=Tsingleton((('c',e[1]),) if mask&1 else ())
        M2=Tsingleton((('c',f[1]),) if mask&2 else ())
        ts.append(triple(triangle_seed()*M1*M2))
    return delta_q(ts)

# Orbit generation.
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
                sm={i:spt[i] for i in range(2)}
                imgs.append(tuple(sorted((map_edge(e,tp,dp,sm),map_edge(f,tp,dp,sm)),key=repr)))
    return min(imgs,key=repr)
same_orbits={}
for e,f in combinations(edges_mixed(),2): same_orbits.setdefault(canon_same(e,f),(e,f))
assert len(same_orbits)==48
same_reps=[]
for e,f in same_orbits.values():
    ds=[z[1] for z in (e,f) if z[0] in ('ds','di')]
    ss=[z[1] for z in (e,f) if z[0] in ('b','x','i1','i2')]
    same_reps.append((e,f,max(ds)+1 if ds else 0,max(ss)+1 if ss else 0))
Eone=[('c',t) for t in range(3)]+[('ds',0,t) for t in range(3)]+[('di',0)]+[('b',0,t) for t in range(3)]+[('x',0,t) for t in range(3)]+[('i1',0),('i2',0)]
def map_one(e,tp):
    if e[0]=='c': return ('c',tp[e[1]])
    if e[0] in ('ds','b','x'): return (e[0],0,tp[e[2]])
    return e
mixed_single_orbits={}
for e in Eone:
    for t in range(3):
        c=min([(map_one(e,tp),('s',tp[t])) for tp in terms],key=repr)
        mixed_single_orbits.setdefault(c,(e,('s',t)))
assert len(mixed_single_orbits)==11
core_mixed_orbits={}
def map_core(e,tp):
    a,b=sorted((tp[e[1]],tp[e[2]])); return ('core',a,b)
for ce in core_edges:
    for e in Eone:
        c=min([(map_core(ce,tp),map_one(e,tp)) for tp in terms],key=repr)
        core_mixed_orbits.setdefault(c,(ce,e))
assert len(core_mixed_orbits)==11
core_single_orbits={}
for ce in core_edges:
    for t in range(3):
        c=min([(map_core(ce,tp),('s',tp[t])) for tp in terms],key=repr)
        core_single_orbits.setdefault(c,(ce,('s',t)))
assert len(core_single_orbits)==2
print('orbit_counts',len(same_orbits),len(mixed_single_orbits),len(core_mixed_orbits),len(core_single_orbits))

# Response strip / certificate helpers.
lo=sp.Rational(43,360); hi=sp.Rational(1,8)
def strip_coeffs(qd):
    c=[sp.Integer(0)]*5
    for (iu,iv),coef in qd.items():
        if iv==0: c[iu]+=coef
        elif iv==1: c[iu+2]+=coef/2; c[iu+1]-=coef*h
        elif iv==2: c[iu+4]+=coef/4; c[iu+3]-=coef*h; c[iu+2]+=coef*h*h
        else: raise AssertionError
    return [sp.factor(z) for z in c]
def bern(expr):
    expr=sp.expand(expr)
    b0=sp.factor(expr.subs(h,lo)); b2=sp.factor(expr.subs(h,hi))
    b1=sp.factor(b0+sp.diff(expr,h).subs(h,lo)*(hi-lo)/2)
    return [b0,b1,b2]
def poly_nonneg(expr,vars):
    num,den=sp.fraction(sp.cancel(expr))
    if den.free_symbols: return False,('den',den)
    P=sp.Poly(sp.expand(num),*vars,domain='QQ')
    bad=[(mon,coef) for mon,coef in P.terms() if coef<0]
    return not bad,bad[:3]
def expr_nonneg_shift(expr,p0,q0,with_h=False):
    es=sp.expand(expr.subs({p:p0+X,q:q0+Y}))
    if with_h:
        for b in bern(es):
            ok,bad=poly_nonneg(b,(X,Y))
            if not ok: return False,bad
        return True,None
    return poly_nonneg(es,(X,Y))
def regular_cert(qd,p0,q0):
    cs=strip_coeffs(qd)
    for ck in cs:
        ok,bad=expr_nonneg_shift(ck,p0,q0,with_h=True)
        if not ok: return False,(ck,bad)
    c0=sp.factor(cs[0].subs({p:p0,q:q0}))
    if c0<=0: return False,('c0',c0)
    return True,c0
def minreq_edge(e):
    if e[0] in ('ds','di'): return (e[1]+1,0)
    if e[0] in ('b','x','i1','i2'): return (0,e[1]+1)
    return (0,0)

# Reconstruct the exact unmarked mixed-spider response from the two-tail algebra.
Tun=Tmix(p,q)
A=sp.factor(Tun[0,0]); BB=sp.factor(Tun[0,1]); C=sp.factor((Tun[0,4]-Tun[0,1])/6)
A_expected=(42*p+45*q+280)/70
B_expected=(1568*p**2+4830*p*q+12152*p+3375*q**2+22875*q+9800)/9800
C_expected=(175616*p**3+893760*p**2*q+1393952*p**2+1464750*p*q**2+5403090*p*q+1174432*p+759375*q**3+5229375*q**2+2341250*q)/8232000
assert sp.simplify(A-A_expected)==0 and sp.simplify(BB-B_expected)==0 and sp.simplify(C-C_expected)==0
rho=sp.factor((BB/A)/2-(C/A)/(BB/A))
rho_expected=(6607552*p**3+27462540*p**2*q+95579008*p**2+36092700*p*q**2+287818860*p*q+385696640*p+15271875*q**3+198665625*q**2+689500000*q+288120000)/(840*(42*p+45*q+280)*(1568*p**2+4830*p*q+12152*p+3375*q**2+22875*q+9800))
assert sp.simplify(rho-rho_expected)==0
rho_lo_num=8820*p**2*q+96040*p**2+18900*p*q**2+259959*p*q+902776*p+10125*q**3+171000*q**2+785400*q+3841600
rho_hi_num=153664*p**3+623280*p**2*q+2055256*p**2+806400*p*q**2+6240045*p*q+7395080*p+337500*q**3+4321875*q**2+14665000*q
D=(42*p+45*q+280)*(1568*p**2+4830*p*q+12152*p+3375*q**2+22875*q+9800)
assert sp.simplify((rho-lo)-rho_lo_num/(252*D))==0
assert sp.simplify((hi-rho)-rho_hi_num/(420*D))==0
print('ALGEBRA J4=K4=0 COMMUTE=True DIMENSION=7')
print('A_pq=',A); print('B_pq=',BB); print('C_pq=',C)
print('RHO_STRIP 43/360 < rho_pq <= 1/8 exact')

# If the mixed spider is exposed, every remaining unmarked component is K1, so h=1/8 exactly.
def fixed_coeffs(qd): return [sp.factor(z.subs(h,hi)) for z in strip_coeffs(qd)]
def fixed_regular(qd,p0,q0):
    cs=fixed_coeffs(qd)
    for ck in cs:
        ok,bad=expr_nonneg_shift(ck,p0,q0,with_h=False)
        if not ok: return False,(ck,bad)
    c0=sp.factor(cs[0].subs({p:p0,q:q0}))
    if c0<=0: return False,('c0',c0)
    return True,c0
def fixed_discr(qd,p0,q0):
    sc=fixed_coeffs(qd); c4,c3,c2=sc[4],sc[3],sc[2]
    KD=sp.factor(4*c4*c2-c3**2)
    checks={}
    checks['c4']=expr_nonneg_shift(c4,p0,q0,False)[0] and sp.factor(c4.subs({p:p0,q:q0}))>0
    checks['KD']=expr_nonneg_shift(KD,p0,q0,False)[0] and sp.factor(KD.subs({p:p0,q:q0}))>0
    checks['c1']=expr_nonneg_shift(sc[1],p0,q0,False)[0]
    checks['c0']=expr_nonneg_shift(sc[0],p0,q0,False)[0] and sp.factor(sc[0].subs({p:p0,q:q0}))>0
    return all(checks.values()),checks,KD

reg=disc=fail=0; discs=[]; fails=[]
for k,(e,f,p0,q0) in enumerate(same_reps):
    qd=q_same(e,f); ok,info=fixed_regular(qd,p0,q0)
    if ok: reg+=1
    else:
        ok2,checks,KD=fixed_discr(qd,p0,q0)
        if ok2: disc+=1; discs.append((e,f,p0,q0,KD))
        else: fail+=1; fails.append((e,f,p0,q0,info,checks))
    if (k+1)%8==0: print('same progress',k+1,'reg',reg,'disc',disc,'fail',fail,flush=True)
assert (reg,disc,fail)==(45,3,0)
print('same FINAL',reg,disc,fail)
for x in discs: print('DISC',x[0],x[1],x[2],x[3],x[4])

reg=disc=fail=0
for e,f in mixed_single_orbits.values():
    p0,q0=minreq_edge(e); qd=q_mixed_single(e,f); ok,_=fixed_regular(qd,p0,q0)
    if ok: reg+=1
    else:
        ok2,_,_=fixed_discr(qd,p0,q0); disc+=int(ok2); fail+=int(not ok2)
assert (reg,disc,fail)==(11,0,0)
print('mixed_single FINAL',reg,disc,fail)
reg=disc=fail=0
for ce,e in core_mixed_orbits.values():
    p0,q0=minreq_edge(e); qd=q_core_mixed(ce,e); ok,_=fixed_regular(qd,p0,q0)
    if ok: reg+=1
    else:
        ok2,_,_=fixed_discr(qd,p0,q0); disc+=int(ok2); fail+=int(not ok2)
assert (reg,disc,fail)==(11,0,0)
print('core_mixed FINAL',reg,disc,fail)

# If the mixed spider remains unmarked, it and the remaining K1 atoms lie in the full strip.
universal=[]
for ce,e in core_single_orbits.values(): universal.append(('core_single',ce,e,regular_cert(q_core_single(ce,e),0,0)))
universal.append(('core_core',regular_cert(q_core_core(core_edges[0],core_edges[1]),0,0)))
universal.append(('single_same',regular_cert(q_single_same(('s',0),('s',1)),0,0)))
universal.append(('single_cross_same_terminal',regular_cert(q_single_cross(('s',0),('s',0)),0,0)))
universal.append(('single_cross_different_terminal',regular_cert(q_single_cross(('s',0),('s',1)),0,0)))
for z in universal: print('UNIVERSAL',z)
assert all(z[-1][0] for z in universal)
print('TOTAL_SCHEMES=76 REGULAR=73 DISCRIMINANT=3 FAIL=0')
print('ALL_EXACT_CHECKS_PASS')
