from itertools import product, permutations, combinations
from functools import lru_cache
import collections
import sympy as sp

# partition utilities
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
        if len(pref)==n: out.append(tuple(pref)); return
        for z in range(mx+2):
            pref.append(z); rec(pref,max(mx,z)); pref.pop()
    rec([0],0)
    return [canon(x) for x in out]
ST=[canon((0,1,2)),canon((0,1,1)),canon((0,0,1)),canon((0,1,0)),canon((0,0,0))]
P4=all_partitions(4); p4idx={s:i for i,s in enumerate(P4)}

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
assert J**4==sp.zeros(15) and K**4==sp.zeros(15) and J*K==K*J
assert J*K**2 == sp.Rational(31,270)*K**3
assert J**2*K == sp.Rational(76,6075)*K**3
assert J**3 == sp.Rational(8,6075)*K**3
S=Start*Close; N=S-4*sp.eye(5); assert N**3==sp.zeros(5)
ones=sp.Matrix([1]*5); N1=N*ones; N2one=N*N*ones
p,q,u,v,h,X,Y=sp.symbols('p q u v h X Y', nonnegative=True)

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
        rr=() if mask==0 else (e,) if mask==1 else (f,) if mask==2 else (e,f)
        ts.append(triple(triangle_seed()*Tmix(p,q,rr)))
    return delta_q(ts)
@lru_cache(None)
def q_core_mixed(e,f):
    ts=[]
    for mask in range(4):
        cr=(e,) if mask&1 else (); rr=(f,) if mask&2 else ()
        ts.append(triple(triangle_seed(cr)*Tmix(p,q,rr)))
    return delta_q(ts)

def q_core_core(e,f):
    ts=[]
    for mask in range(4):
        cr=() if mask==0 else (e,) if mask==1 else (f,) if mask==2 else (e,f)
        ts.append(triple(triangle_seed(cr)))
    return delta_q(ts)

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
def map_core(e,tp):
    a,b=sorted((tp[e[1]],tp[e[2]])); return ('core',a,b)
core_mixed_orbits={}
for ce in core_edges:
    for e in Eone:
        c=min([(map_core(ce,tp),map_one(e,tp)) for tp in terms],key=repr)
        core_mixed_orbits.setdefault(c,(ce,e))
assert len(core_mixed_orbits)==11

def minreq_edge(e):
    if e[0] in ('ds','di'): return (e[1]+1,0)
    if e[0] in ('b','x','i1','i2'): return (0,e[1]+1)
    return (0,0)
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
def expr_nonneg_shift(expr,p0,q0,with_h=True):
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
        ok,bad=expr_nonneg_shift(ck,p0,q0,True)
        if not ok: return False,(ck,bad)
    c0=sp.factor(cs[0].subs({p:p0,q:q0}))
    if c0<=0: return False,('c0',c0)
    return True,c0

def discr_cert(qd,p0,q0):
    cs=strip_coeffs(qd)
    KD=sp.factor(4*cs[4]*cs[2]-cs[3]**2)
    for idx in (4,1,0):
        ok,bad=expr_nonneg_shift(cs[idx],p0,q0,True)
        if not ok: return False,(f'c{idx}',bad,KD)
    ok,bad=expr_nonneg_shift(KD,p0,q0,True)
    if not ok: return False,('KD',bad,KD)
    vals=[sp.factor(cs[4].subs({p:p0,q:q0,h:lo})), sp.factor(KD.subs({p:p0,q:q0,h:lo})), sp.factor(cs[0].subs({p:p0,q:q0,h:lo}))]
    if not all(vv>0 for vv in vals): return False,('strict',vals,KD)
    return True,KD

print('core_mixed_orbits',len(core_mixed_orbits))
reg2=disc2=fail2=0; failures2=[]; dlist2=[]
for i,(ce,e) in enumerate(core_mixed_orbits.values()):
    p0,q0=minreq_edge(e); qd=q_core_mixed(ce,e)
    ok,info=regular_cert(qd,p0,q0)
    if ok: reg2+=1
    else:
        ok2,info2=discr_cert(qd,p0,q0)
        if ok2: disc2+=1; dlist2.append((ce,e,p0,q0,info2))
        else: fail2+=1; failures2.append((ce,e,p0,q0,info,info2))
    print('coremixed',i+1,'reg',reg2,'disc',disc2,'fail',fail2,flush=True)
assert (reg2,disc2,fail2)==(11,0,0)
print('COREMIXED_FINAL',reg2,disc2,fail2)
assert regular_cert(q_core_core(core_edges[0],core_edges[1]),0,0)[0]
print('CORECORE_FULL_STRIP_PASS')

# New exact cross-component seed-lift identity. NM13-08's independent-terminal
# certificate supplies k,L2,L1,C >=0 on h in [43/360,1/8]. Replacing the
# independent seed by the triangle seed changes a,b,H0,s0 as below.
d,e0,k,a,b,H0,s0,hh=sp.symbols('d e0 k a b H0 s0 hh')
L2=4*d*e0-3*k
L1=2*a*e0+2*b*d-k*(s0-6*hh)
C0=a*b-H0*k
at=a+2*d; bt=b+2*e0; Ht=H0+s0+2; st=s0+6
L2t=sp.expand(4*d*e0-3*k)
L1t=sp.expand(2*at*e0+2*bt*d-k*(st-6*hh))
C0t=sp.expand(at*bt-Ht*k)
assert sp.expand(L2t-L2)==0
assert sp.expand(L1t-(L1+2*L2))==0
assert sp.expand(C0t-(C0+L1+L2+k*(1-6*hh)))==0
assert sp.Rational(1)-6*sp.Rational(1,8)>0
print('CROSS_SEED_LIFT L2t=L2')
print('CROSS_SEED_LIFT L1t=L1+2L2')
print('CROSS_SEED_LIFT C0t=C0+L1+L2+k(1-6h)')
print('since h<=1/8, 1-6h>=1/4 >0')
print('TRIANGLE_CORE_AND_CROSS_FULL_STRIP_PASS')
print('ALL_EXACT_CHECKS_PASS')
