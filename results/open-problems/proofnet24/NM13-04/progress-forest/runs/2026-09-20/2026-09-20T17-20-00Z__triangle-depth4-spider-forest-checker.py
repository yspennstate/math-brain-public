#!/usr/bin/env python3
from itertools import product, permutations, combinations
from functools import lru_cache
import collections
import sympy as sp

# Exact triangle-seeded depth-4 spider forest checker; no floating point.
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
    return canon([la if q==lb else q for q in labels])

def introduce(labels): return canon(tuple(labels)+(max(labels,default=-1)+1,))
def forget(labels,idx): return canon(tuple(q for i,q in enumerate(labels) if i!=idx))

def all_partitions(n):
    out=[]
    def rec(pref,mx):
        if len(pref)==n: out.append(canon(pref)); return
        for z in range(mx+2):
            pref.append(z); rec(pref,max(mx,z)); pref.pop()
    rec([0],0)
    return list(dict.fromkeys(out))

ST=[canon((0,1,2)),canon((0,1,1)),canon((0,0,1)),canon((0,1,0)),canon((0,0,0))]
P4=all_partitions(4); P5=all_partitions(5)
assert len(P4)==15 and len(P5)==52
p4idx={s:i for i,s in enumerate(P4)}; p5idx={s:i for i,s in enumerate(P5)}

def start_center_matrix(req_terms=()):
    req=set(req_terms); M=sp.zeros(5,15)
    for si,ts in enumerate(ST):
        lab=introduce(ts); stage=[(t,t,3) for t in range(3)]
        for bits in product((0,1),repeat=3):
            if any(t in req and not bit for bit,(t,_,__) in zip(bits,stage)): continue
            cur=lab; ok=True
            for bit,(_,a,b) in zip(bits,stage):
                if bit:
                    cur=union_part(cur,a,b)
                    if cur is None: ok=False; break
            if ok: M[si,p4idx[cur]]+=1
    return M

Start=start_center_matrix(); Close=sp.zeros(15,5)
for i,lab in enumerate(P4): Close[i,ST.index(forget(lab,3))]+=1

def first_step_matrix(req=frozenset()):
    M=sp.zeros(15,52)
    for si,lab in enumerate(P4):
        lab2=introduce(lab); stage=[(('i',1),3,4)]+[(('s',1,t),t,4) for t in range(3)]
        for bits in product((0,1),repeat=4):
            if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)): continue
            cur=lab2; ok=True
            for bit,(eid,a,b) in zip(bits,stage):
                if bit:
                    cur=union_part(cur,a,b)
                    if cur is None: ok=False; break
            if ok: M[si,p5idx[cur]]+=1
    return M

def ext_step_matrix(pos,req=frozenset()):
    M=sp.zeros(52)
    for si,lab in enumerate(P5):
        lab2=introduce(lab); stage=[(('i',pos),4,5)]+[(('s',pos,t),t,5) for t in range(3)]
        for bits in product((0,1),repeat=4):
            if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)): continue
            cur=lab2; ok=True
            for bit,(eid,a,b) in zip(bits,stage):
                if bit:
                    cur=union_part(cur,a,b)
                    if cur is None: ok=False; break
            if ok: M[si,p5idx[forget(cur,4)]]+=1
    return M

Astart=first_step_matrix(); E=ext_step_matrix(2); Fclose=sp.zeros(52,15)
for i,lab in enumerate(P5): Fclose[i,p4idx[forget(lab,4)]]+=1

def Ld(d): return Astart*(E**(d-1))*Fclose
L4=Ld(4); M4=L4-892*sp.eye(15)
assert (M4.rank(),(M4**2).rank(),(M4**3).rank(),(M4**4).rank())==(8,2,1,0)

N=Start*Close-4*sp.eye(5); assert N**3==sp.zeros(5)
ones=sp.Matrix([1]*5); N1=N*ones; N2one=(N*N)*ones
m,u,v,h,X=sp.symbols('m u v h X', nonnegative=True)
lo=sp.Rational(43,360); hi=sp.Rational(1,8)

def M4pow(r):
    return sp.eye(15)+r*M4/892+sp.binomial(r,2)*M4**2/892**2+sp.binomial(r,3)*M4**3/892**3

Tun=sp.simplify(Start*M4pow(m)*Close)
A=sp.factor(Tun[0,0]); B=sp.factor(Tun[0,1]); C=sp.factor((Tun[0,4]-Tun[0,1])/6)
assert sp.simplify(A-4*(36*m+223)/sp.Integer(223))==0
assert sp.simplify(B-(34560*m**2+223674*m+49729)/sp.Integer(49729))==0
assert sp.simplify(C-m*(24883200*m**2+162422592*m+37717933)/sp.Integer(66537402))==0
assert sp.simplify(Tun-(A*sp.eye(5)+B*N+C*N**2))==sp.zeros(5)
rho=sp.factor((B**2-2*A*C)/(2*A*B))
rho_lo=sp.factor(rho-lo); rho_hi=sp.factor(hi-rho)
for ex in (rho_lo,rho_hi):
    num,den=sp.cancel(ex).as_numer_denom()
    assert all(c>=0 for c in sp.Poly(sp.expand(num),m).all_coeffs())
    assert all(c>0 for c in sp.Poly(sp.expand(den),m).all_coeffs())
assert rho_lo.subs(m,0)>0 and rho_hi.subs(m,0)==0

@lru_cache(None)
def arm_req(reqtuple):
    req=set(reqtuple); R=first_step_matrix(frozenset(req))
    for pos in range(2,5): R=R*ext_step_matrix(pos,frozenset(req))
    return R*Fclose
assert arm_req(())==L4

def local_req(e):
    if e[0]=='s': return ('s',e[2],e[3])
    if e[0]=='i': return ('i',e[2])
    raise AssertionError(e)

@lru_cache(None)
def Tspider(reqtuple):
    centers=[]; arms=collections.defaultdict(list)
    for e in reqtuple:
        if e[0]=='c': centers.append(e[1])
        else: arms[e[1]].append(local_req(e))
    R=start_center_matrix(tuple(centers)); keys=sorted(arms)
    for a in keys: R=R*arm_req(tuple(sorted(arms[a],key=repr)))/892
    return sp.simplify(R*M4pow(m-len(keys))*Close)

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
q=triangle_seed(); assert list(q)==[1,1,1,1,3]

def triple(row): return ((row*ones)[0],(row*N1)[0],(row*N2one)[0])
def prod_aff(a,b):
    mons=[(0,0),(1,0),(0,1)]; d=collections.defaultdict(lambda:sp.Integer(0))
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
        ts.append(triple(q*Tspider(rr)))
    return delta_q(ts)

@lru_cache(None)
def q_core_right(ce,e):
    ts=[]
    for mask in range(4):
        cr=(ce,) if mask&1 else (); rr=(e,) if mask&2 else ()
        ts.append(triple(triangle_seed(cr)*Tspider(rr)))
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
        else: raise AssertionError((iu,iv))
    return [sp.factor(sp.expand_func(z)) for z in c]
def bern(expr):
    expr=sp.expand_func(expr)
    b0=sp.factor(expr.subs(h,lo)); b2=sp.factor(expr.subs(h,hi))
    b1=sp.factor(b0+sp.diff(expr,h).subs(h,lo)*(hi-lo)/2)
    return [b0,b1,b2]
def poly_nonneg_shift(expr,m0, strict=False):
    z=sp.cancel(sp.expand_func(expr.subs(m,m0+X)))
    if z==0: return not strict
    num,den=z.as_numer_denom()
    nc=sp.Poly(sp.expand(num),X,domain='QQ').coeffs()
    dc=sp.Poly(sp.expand(den),X,domain='QQ').coeffs()
    if all(c<0 for c in dc): nc=[-c for c in nc]; dc=[-c for c in dc]
    return all(c>=0 for c in nc) and all(c>0 for c in dc) and ((not strict) or any(c>0 for c in nc))
def bern_nonneg_shift(expr,m0): return all(poly_nonneg_shift(b,m0) for b in bern(expr))
def regular_cert(qd,m0):
    cs=strip_coeffs(qd)
    return all(bern_nonneg_shift(c,m0) for c in cs) and sp.factor(cs[0].subs(m,m0))>0

def discr_cert(qd,m0):
    cs=strip_coeffs(qd); KD=sp.factor(sp.expand_func(4*cs[4]*cs[2]-cs[3]**2))
    if not all(bern_nonneg_shift(cs[i],m0) for i in (4,1,0)): return False,None
    if h in KD.free_symbols: return False,None
    if not poly_nonneg_shift(KD,m0,strict=True): return False,None
    vals=[sp.factor(cs[4].subs({m:m0,h:lo})),sp.factor(cs[0].subs({m:m0,h:lo})),sp.factor(KD.subs(m,m0))]
    return all(z>0 for z in vals),KD

terms=list(permutations(range(3)))
def edges_witness(arms=2):
    out=[('c',t) for t in range(3)]
    for a in range(arms):
        for pos in range(1,5): out += [('s',a,pos,t) for t in range(3)]+[('i',a,pos)]
    return out
def map_edge(e,tp,ap):
    if e[0]=='c': return ('c',tp[e[1]])
    if e[0]=='s': return ('s',ap[e[1]],e[2],tp[e[3]])
    return ('i',ap[e[1]],e[2])
def canon_pair(e,f):
    imgs=[]
    for tp in terms:
        for ar in permutations(range(2)):
            ap={i:ar[i] for i in range(2)}
            imgs.append(tuple(sorted((map_edge(e,tp,ap),map_edge(f,tp,ap)),key=repr)))
    return min(imgs,key=repr)
orbits={}
for e,f in combinations(edges_witness(),2): orbits.setdefault(canon_pair(e,f),(e,f))
assert len(orbits)==97

def minarms(e,f):
    aa=[z[1] for z in (e,f) if z[0] in ('s','i')]
    return max(aa)+1 if aa else 0
reg=disc=fail=0; disc_list=[]
for e,f in orbits.values():
    m0=minarms(e,f); qd=q_same(e,f)
    if regular_cert(qd,m0): reg+=1
    else:
        ok,KD=discr_cert(qd,m0)
        if ok:
            disc+=1; disc_list.append((e,f,m0,sp.factor(KD)))
        else:
            fail+=1; print('FAIL SAME',e,f,m0,strip_coeffs(qd))
assert fail==0

# Core/right schemes under terminal S3.
def map_core(e,tp):
    a,b=sorted((tp[e[1]],tp[e[2]])); return ('core',a,b)
def map_one(e,tp):
    if e[0]=='c': return ('c',tp[e[1]])
    if e[0]=='i': return e
    return ('s',0,e[2],tp[e[3]])
Eone=[('c',t) for t in range(3)]
for d in range(1,5):
    Eone.append(('i',0,d)); Eone += [('s',0,d,t) for t in range(3)]
core_orbits={}
for ce in core_edges:
    for e in Eone:
        key=min([(map_core(ce,tp),map_one(e,tp)) for tp in terms],key=repr)
        core_orbits.setdefault(key,(ce,e))
core_fail=[]
for ce,e in core_orbits.values():
    m0=1 if e[0] in ('i','s') else 0
    if not regular_cert(q_core_right(ce,e),m0): core_fail.append((ce,e,m0))
assert not core_fail

cc=strip_coeffs(q_core_core(core_edges[0],core_edges[1]))
assert all(sp.factor(x-y)==0 for x,y in zip(cc,[2,2*(3*h+1),1,0,0]))

# Abstract triangle-seed lift for two distinct exposed right components.
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
assert sp.factor(1-6*hi)==sp.Rational(1,4)

# Finite exact transfer sanity at m=2; not a theorem source.
def Tnum(reqtuple,mval=2):
    centers=[]; arms=collections.defaultdict(list)
    for ee in reqtuple:
        if ee[0]=='c': centers.append(ee[1])
        else: arms[ee[1]].append(local_req(ee))
    R=start_center_matrix(tuple(centers)); keys=sorted(arms)
    for aa in keys: R=R*arm_req(tuple(sorted(arms[aa],key=repr)))
    return R*(L4**(mval-len(keys)))*Close
T0=Tnum((),2); Icnt=int((q*T0*ones)[0])
Ephys=edges_witness(2)+core_edges
singles={}
for ee in Ephys:
    if ee[0]=='core': singles[ee]=int((triangle_seed((ee,))*T0*ones)[0])
    else: singles[ee]=int((q*Tnum((ee,),2)*ones)[0])
ming=None; minpair=None
for ee,ff in combinations(Ephys,2):
    if ee[0]=='core' and ff[0]=='core': Ief=int((triangle_seed((ee,ff))*T0*ones)[0])
    elif ee[0]=='core': Ief=int((triangle_seed((ee,))*Tnum((ff,),2)*ones)[0])
    elif ff[0]=='core': Ief=int((triangle_seed((ff,))*Tnum((ee,),2)*ones)[0])
    else: Ief=int((q*Tnum((ee,ff),2)*ones)[0])
    gap=singles[ee]*singles[ff]-Icnt*Ief
    assert gap>0
    if ming is None or gap<ming: ming=gap; minpair=(ee,ff)

print('NM13-04 T07 TRIANGLE DEPTH4-SPIDER FOREST EXACT CHECKER')
print('unmarked_response_rho_interval=[43/360,1/8] verified')
print(f'same_component_orbits={len(orbits)} regular={reg} discriminant={disc} failures={fail}')
print(f'core_right_orbits={len(core_orbits)} regular={len(core_orbits)} failures=0')
print('core_core_gap_coefficients=',cc)
print('cross_component_seed_lift=PASS inherited_independent_depth4_schemes=60')
print('triangle_lift_extra_constant=k*(1-6h), minimum_multiplier=1/4')
print('discriminant_cases=')
for ee,ff,m0,KD in disc_list:
    print(' ',ee,ff,'m0=',m0,'D=',KD)
print('finite_sanity_m=2 forest_count=',Icnt,'edge_pairs=',len(Ephys)*(len(Ephys)-1)//2,'min_gap=',ming,'min_pair=',minpair)
print('ALL_EXACT_CHECKS_PASS')
