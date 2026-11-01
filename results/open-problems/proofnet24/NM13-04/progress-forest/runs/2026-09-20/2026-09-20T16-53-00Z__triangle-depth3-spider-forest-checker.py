#!/usr/bin/env python3
from itertools import product, permutations, combinations
from functools import lru_cache
import collections
import sympy as sp

# Exact five-/fifteen-state forest transfer checker for the triangle-seeded
# pure depth-three spider family. No floating point is used.

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

def introduce(labels):
    return canon(tuple(labels)+(max(labels,default=-1)+1,))

def forget(labels,idx):
    return canon(tuple(z for i,z in enumerate(labels) if i!=idx))

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


@lru_cache(None)
def arm_matrix(k, req_edges=()):
    req=set(req_edges); M=sp.zeros(15)
    for si,lab in enumerate(P4):
        cur0=lab
        for _ in range(k): cur0=introduce(cur0)
        edges=[]
        for j in range(1,k+1):
            prev=3 if j==1 else 3+j-1
            vv=3+j
            edges.append((('i',j),prev,vv))
            for t in range(3): edges.append((('s',j,t),t,vv))
        for bits in product((0,1),repeat=4*k):
            if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,edges)): continue
            cur=cur0; ok=True
            for bit,(eid,a,b) in zip(bits,edges):
                if bit:
                    cur=union_part(cur,a,b)
                    if cur is None: ok=False; break
            if ok:
                for j in range(k,0,-1): cur=forget(cur,3+j)
                M[si,p4idx[cur]]+=1
    return M

Close=sp.zeros(15,5)
for i,lab in enumerate(P4): Close[i,ST.index(forget(lab,3))]+=1
Start=start_center_matrix()
L1,L2,L3=arm_matrix(1),arm_matrix(2),arm_matrix(3)
I15=sp.eye(15)
J,K,M=L1-5*I15,L2-28*I15,L3-158*I15
assert J**4==sp.zeros(15) and K**4==sp.zeros(15) and M**4==sp.zeros(15)
assert (M.rank(),(M**2).rank(),(M**3).rank(),(M**4).rank())==(8,2,1,0)
assert J*K==K*J and J*M==M*J and K*M==M*K
closure=(sp.Rational(82,7)*K + sp.Rational(73,1029)*K**2 - sp.Rational(1376,893025)*K**3
         -sp.Rational(254,7)*J + sp.Rational(282,343)*J*K - sp.Rational(4185,343)*J**2)
assert M==closure

S=Start*Close; N=S-4*sp.eye(5)
assert N**3==sp.zeros(5)
ones=sp.Matrix([1]*5); N1=N*ones; N2one=N*N*ones

m,u,v,h,X=sp.symbols('m u v h X', nonnegative=True)
lo=sp.Rational(43,360); hi=sp.Rational(1,8)

def Mpow(r):
    return sp.eye(15)+r*M/158+sp.binomial(r,2)*M**2/(158**2)+sp.binomial(r,3)*M**3/(158**3)

@lru_cache(None)
def Tdepth(msym, req_edges=()):
    center=[]; arms=collections.defaultdict(list)
    for e in req_edges:
        if e[0]=='c': center.append(e[1])
        elif e[0]=='i':
            _,idx,d=e; arms[idx].append(('i',d))
        elif e[0]=='s':
            _,idx,d,t=e; arms[idx].append(('s',d,t))
        else: raise AssertionError(e)
    keys=sorted(arms)
    Q=start_center_matrix(tuple(center))
    for idx in keys: Q=Q*arm_matrix(3,tuple(arms[idx]))
    return Q*Mpow(msym-len(keys))*Close/(sp.Integer(158)**len(keys))

Tun=Tdepth(m,())
A=sp.factor(sp.expand_func(Tun[0,0]))
B=sp.factor(sp.expand_func(Tun[0,1]))
C=sp.factor(sp.expand_func((Tun[0,4]-B)/6))
A0=(51*m+316)/sp.Integer(79)
B0=(3247*m**2+21322*m+6241)/sp.Integer(6241)
C0=m*(620177*m**2+4118189*m+1259235)/sp.Integer(2958234)
assert sp.factor(A-A0)==0 and sp.factor(B-B0)==0 and sp.factor(C-C0)==0
assert all(sp.simplify(z)==0 for z in Tun-(A*sp.eye(5)+B*N+C*N**2))
rho=sp.factor((B**2-2*A*C)/(2*A*B))
assert sp.factor(rho-(9391633*m**3+119901505*m**2+400505352*m+116850243)/(474*(51*m+316)*(3247*m**2+21322*m+6241)))==0
rho_lo=sp.factor(rho-lo); rho_hi=sp.factor(hi-rho)
for expr in (rho_lo,rho_hi):
    num,den=sp.fraction(sp.cancel(expr))
    assert den.subs(m,0)>0
    assert all(c>=0 for c in sp.Poly(sp.expand(num),m,domain='QQ').all_coeffs())
assert rho_lo.subs(m,0)>0 and rho_hi.subs(m,0)==0

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
        ts.append(triple(triangle_seed()*Tdepth(m,rr)))
    return delta_q(ts)

@lru_cache(None)
def q_core_right(ce,e):
    ts=[]
    for mask in range(4):
        cr=(ce,) if mask&1 else (); rr=(e,) if mask&2 else ()
        ts.append(triple(triangle_seed(cr)*Tdepth(m,rr)))
    return delta_q(ts)

def q_core_core(ce,cf):
    ts=[]
    for mask in range(4):
        cr=() if mask==0 else (ce,) if mask==1 else (cf,) if mask==2 else (ce,cf)
        ts.append(triple(triangle_seed(cr)))
    return delta_q(ts)

def strip_coeffs(qd):
    c=[sp.Integer(0)]*5
    for (iu,iv),coef in qd.items():
        if iv==0: c[iu]+=coef
        elif iv==1: c[iu+2]+=coef/2; c[iu+1]-=coef*h
        elif iv==2: c[iu+4]+=coef/4; c[iu+3]-=coef*h; c[iu+2]+=coef*h*h
        else: raise AssertionError
    return [sp.factor(sp.expand_func(z)) for z in c]

def bern(expr):
    expr=sp.expand_func(expr)
    b0=sp.factor(expr.subs(h,lo)); b2=sp.factor(expr.subs(h,hi))
    b1=sp.factor(b0+sp.diff(expr,h).subs(h,lo)*(hi-lo)/2)
    return [b0,b1,b2]

def poly_nonneg_shift(expr,m0):
    num,den=sp.fraction(sp.cancel(sp.expand_func(expr.subs(m,m0+X))))
    if den.free_symbols: return False
    return all(c>=0 for _,c in sp.Poly(sp.expand(num),X,domain='QQ').terms())

def bern_nonneg_shift(expr,m0): return all(poly_nonneg_shift(b,m0) for b in bern(expr))

def regular_cert(qd,m0):
    cs=strip_coeffs(qd)
    return all(bern_nonneg_shift(c,m0) for c in cs) and sp.factor(cs[0].subs(m,m0))>0

def discr_cert(qd,m0):
    cs=strip_coeffs(qd); KD=sp.factor(sp.expand_func(4*cs[4]*cs[2]-cs[3]**2))
    if not all(bern_nonneg_shift(cs[i],m0) for i in (4,1,0)): return False,None
    if not bern_nonneg_shift(KD,m0): return False,None
    vals=[sp.factor(cs[4].subs({m:m0,h:lo})),sp.factor(cs[0].subs({m:m0,h:lo})),sp.factor(KD.subs({m:m0,h:lo}))]
    return all(z>0 for z in vals),KD

terms=list(permutations(range(3)))
def edges_witness():
    E=[('c',t) for t in range(3)]
    for i in range(2):
        for d in range(1,4):
            E.append(('i',i,d)); E += [('s',i,d,t) for t in range(3)]
    return E

def map_edge(e,tp,ap):
    if e[0]=='c': return ('c',tp[e[1]])
    if e[0]=='i': return ('i',ap[e[1]],e[2])
    return ('s',ap[e[1]],e[2],tp[e[3]])

def canon_pair(e,f):
    imgs=[]
    for tp in terms:
        for ap in permutations(range(2)):
            imgs.append(tuple(sorted((map_edge(e,tp,ap),map_edge(f,tp,ap)),key=repr)))
    return min(imgs,key=repr)

same_orbits={}
for e,f in combinations(edges_witness(),2): same_orbits.setdefault(canon_pair(e,f),(e,f))
assert len(same_orbits)==58
same=[]
for e,f in same_orbits.values():
    ids=[z[1] for z in (e,f) if z[0] in ('i','s')]
    same.append((e,f,max(ids)+1 if ids else 0))
reg=disc=fail=0; disc_list=[]
for e,f,m0 in same:
    qd=q_same(e,f)
    if regular_cert(qd,m0): reg+=1
    else:
        ok,KD=discr_cert(qd,m0)
        if ok: disc+=1; disc_list.append((e,f,m0,sp.factor(KD)))
        else: fail+=1
assert (reg,disc,fail)==(52,6,0)

# Core/right local schemes under terminal S3.
def map_core(e,tp):
    a,b=sorted((tp[e[1]],tp[e[2]])); return ('core',a,b)
def map_one(e,tp):
    if e[0]=='c': return ('c',tp[e[1]])
    if e[0]=='i': return e
    return ('s',0,e[2],tp[e[3]])
Eone=[('c',t) for t in range(3)]
for d in range(1,4):
    Eone.append(('i',0,d)); Eone += [('s',0,d,t) for t in range(3)]
core_orbits={}
for ce in core_edges:
    for e in Eone:
        key=min([(map_core(ce,tp),map_one(e,tp)) for tp in terms],key=repr)
        core_orbits.setdefault(key,(ce,e))
assert len(core_orbits)==11
for ce,e in core_orbits.values():
    m0=1 if e[0] in ('i','s') else 0
    assert regular_cert(q_core_right(ce,e),m0)

cc=strip_coeffs(q_core_core(core_edges[0],core_edges[1]))
assert all(sp.factor(x-y)==0 for x,y in zip(cc,[2,2*(3*h+1),1,0,0]))

# Abstract seed-lift identity for two distinct exposed components in the C(x,z) algebra.
H,s,a,b,d,e,k=sp.symbols('H s a b d e k')
vsub=u**2/2-h*u

def Lind(Hs,ss): return Hs+ss*u+6*vsub
Dind=sp.expand(Lind(H+a,s+2*d)*Lind(H+b,s+2*e)-Lind(H,s)*Lind(H+a+b+k,s+2*d+2*e))

def Ltri(Hs,ss): return (Hs+ss+2)+(ss+6)*u+6*vsub
Dtri=sp.expand(Ltri(H+a,s+2*d)*Ltri(H+b,s+2*e)-Ltri(H,s)*Ltri(H+a+b+k,s+2*d+2*e))
L2c=4*d*e-3*k
L1c=2*a*e+2*b*d-k*(s-6*h)
C0c=a*b-H*k
assert sp.factor(Dind-(L2c*u**2+L1c*u+C0c))==0
assert sp.factor(Dtri-(L2c*u**2+(L1c+2*L2c)*u+(C0c+L1c+L2c+k*(1-6*h))))==0

print('NM13-04 T07 TRIANGLE DEPTH3-SPIDER FOREST EXACT CHECKER')
print('L3=158I+M; M^4=0; ranks=(8,2,1,0); old_tail_algebra_closure=PASS')
print('A_m=',A0)
print('B_m=',B0)
print('C_m=',C0)
print('rho_m=',rho)
print('rho_strip=43/360 < rho_m <= 1/8: PASS')
print('same_component_orbits=58 regular=52 discriminant=6 failures=0')
for item in disc_list: print('DISC',item)
print('core_right_orbits=11 regular=11 failures=0')
print('core_core_coeffs=',cc)
print('seed_lift: L2_tri=L2; L1_tri=L1+2L2; C0_tri=C0+L1+L2+k(1-6h): PASS')
print('Consumed companion condition: independent depth3 cross schemes have k,L2,L1,C0 > 0 on strip.')
print('Since h<=1/8, 1-6h>=1/4, hence triangle cross-component coefficients are strict.')
print('ALL_EXACT_CHECKS_PASS')
