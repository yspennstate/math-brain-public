from itertools import product, permutations, combinations
from functools import lru_cache
import collections, hashlib
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

# Start a right component by retaining its center alongside the three terminals.
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

# A length-3 arm c-a-b-x. Each of a,b,x is also joined to all three terminals.
@lru_cache(None)
def arm3_matrix(req_edges=()):
    req=set(req_edges); M=sp.zeros(15)
    for si,lab in enumerate(P4):
        cur0=lab
        for _ in range(3): cur0=introduce(cur0)
        stage=[]
        for j in range(3):
            v=4+j; prev=3 if j==0 else v-1
            stage.append((('i',j),prev,v))
            for t in range(3): stage.append((('s',j,t),t,v))
        for bits in product((0,1),repeat=12):
            if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)): continue
            cur=cur0; ok=True
            for bit,(eid,a,b) in zip(bits,stage):
                if bit:
                    cur=union_part(cur,a,b)
                    if cur is None: ok=False; break
            if ok:
                for idx in (6,5,4): cur=forget(cur,idx)
                M[si,p4idx[cur]]+=1
    return M

Close=sp.zeros(15,5)
for i,lab in enumerate(P4): Close[i,ST.index(forget(lab,3))]+=1
Start=start_center_matrix()
L3=arm3_matrix()
M=L3-158*sp.eye(15)
assert M**4==sp.zeros(15)
assert (M.rank(),(M**2).rank(),(M**3).rank(),(M**4).rank())==(8,2,1,0)

S=Start*Close
N=S-4*sp.eye(5)
assert N**3==sp.zeros(5)
ones=sp.Matrix([1]*5); N1=N*ones; N2one=N*N*ones
Qtri=sp.Matrix([[1,1,1,1,3]])

n,m,u,v,h,X,Y=sp.symbols('n m u v h X Y', integer=True, nonnegative=True)

def Mpow(r):
    return sp.eye(15)+r*M/158+sp.binomial(r,2)*M**2/(158**2)+sp.binomial(r,3)*M**3/(158**3)

def classify_req(req_edges):
    center=[]; arms=collections.defaultdict(list)
    for e in req_edges:
        typ=e[0]
        if typ=='c': center.append(e[1])
        elif typ in ('a','b','x'):
            pos={'a':0,'b':1,'x':2}[typ]
            arms[e[1]].append(('s',pos,e[2]))
        elif typ in ('i1','i2','i3'):
            pos={'i1':0,'i2':1,'i3':2}[typ]
            arms[e[1]].append(('i',pos))
        else: raise AssertionError(e)
    return center,arms

@lru_cache(None)
def Tcomp(req_edges=()):
    center,arms=classify_req(req_edges)
    R=start_center_matrix(tuple(center))
    for old in sorted(arms): R=R*arm3_matrix(tuple(arms[old]))
    k=len(arms)
    return (R*Mpow(n-k)*Close/(158**k)).applyfunc(lambda z: sp.cancel(sp.expand_func(z)))

Tun=Tcomp(())
A=sp.factor(sp.expand_func(Tun[0,0]))
B=sp.factor(sp.expand_func(Tun[0,1]))
C=sp.factor(sp.expand_func((Tun[0,4]-Tun[0,1])/6))
A0=(51*n+316)/79
B0=(3247*n**2+21322*n+6241)/6241
C0=n*(620177*n**2+4118189*n+1259235)/2958234
assert sp.cancel(A-A0)==0 and sp.cancel(B-B0)==0 and sp.cancel(C-C0)==0
rho=sp.factor(sp.expand_func(B/(2*A)-C/B))
rho0=(9391633*n**3+119901505*n**2+400505352*n+116850243)/(474*(51*n+316)*(3247*n**2+21322*n+6241))
assert sp.cancel(rho-rho0)==0
lo=sp.Rational(43,360); hi=sp.Rational(1,8)
lo_diff=(964971*n**3+14619122*n**2+60943049*n+311600648)/(28440*(51*n+316)*(3247*n**2+21322*n+6241))
hi_diff=n*(1679957*n**2+21287318*n+70260783)/(1896*(51*n+316)*(3247*n**2+21322*n+6241))
assert sp.cancel(rho-lo-lo_diff)==0
assert sp.cancel(hi-rho-hi_diff)==0

def triple(seedrow,M5):
    row=seedrow*M5
    return tuple(sp.cancel(z) for z in ((row*ones)[0],(row*N1)[0],(row*N2one)[0]))

def prod_aff(a,b):
    mons=[(0,0),(1,0),(0,1)]; d=collections.defaultdict(lambda:sp.Integer(0))
    for i,aa in enumerate(a):
        for j,bb in enumerate(b): d[(mons[i][0]+mons[j][0],mons[i][1]+mons[j][1])]+=aa*bb
    return d

def delta_q(ts):
    x1=prod_aff(ts[1],ts[2]); x2=prod_aff(ts[0],ts[3]); out={}
    for k in set(x1)|set(x2):
        z=sp.cancel(x1.get(k,0)-x2.get(k,0))
        if z!=0: out[k]=z
    return out

@lru_cache(None)
def q_same(e,f):
    ts=[]
    for mask in range(4):
        req=() if mask==0 else (e,) if mask==1 else (f,) if mask==2 else (e,f)
        ts.append(triple(Qtri,Tcomp(req)))
    return delta_q(ts)

def strip_coeffs(qd):
    c=[sp.Integer(0)]*5
    for (iu,iv),coef in qd.items():
        if iv==0: c[iu]+=coef
        elif iv==1:
            c[iu+2]+=coef/2; c[iu+1]-=coef*h
        elif iv==2:
            c[iu+4]+=coef/4; c[iu+3]-=coef*h; c[iu+2]+=coef*h*h
        else: raise AssertionError
    return [sp.cancel(z) for z in c]

def bern2(expr):
    f=sp.cancel(expr)
    b0=sp.cancel(f.subs(h,lo)); b2=sp.cancel(f.subs(h,hi))
    b1=sp.cancel(b0+(hi-lo)*sp.diff(f,h).subs(h,lo)/2)
    return (b0,b1,b2)

def shift_poly(expr,n0):
    ex=sp.cancel(sp.expand_func(expr.subs(n,X+n0)))
    num,den=sp.together(ex).as_numer_denom()
    P=sp.Poly(sp.expand(num),X); Q=sp.Poly(sp.expand(den),X)
    assert all(c>=0 for c in Q.coeffs()) and Q.eval(0)>0
    return P

def regular_univar(qd,n0):
    cs=strip_coeffs(qd); bad=[]
    for j,c in enumerate(cs):
        for k,bv in enumerate(bern2(c)):
            P=shift_poly(bv,n0)
            if not all(cc>=0 for cc in P.coeffs()): bad.append((j,k,P.as_expr()))
    return cs,bad

terms=list(permutations(range(3)))
def edges_two_arms():
    E=[('c',t) for t in range(3)]
    for a in range(2):
        E += [('a',a,t) for t in range(3)]+[('b',a,t) for t in range(3)]+[('x',a,t) for t in range(3)]
        E += [('i1',a),('i2',a),('i3',a)]
    return E

def map_edge(e,tp,ap):
    if e[0]=='c': return ('c',tp[e[1]])
    if e[0] in ('a','b','x'): return (e[0],ap[e[1]],tp[e[2]])
    return (e[0],ap[e[1]])

def canon_same(e,f):
    ims=[]
    for tp in terms:
        for av in permutations(range(2)):
            ap={i:av[i] for i in range(2)}
            ee=map_edge(e,tp,ap); ff=map_edge(f,tp,ap)
            ims.append(tuple(sorted((ee,ff),key=repr)))
    return min(ims,key=repr)

same_orbits={}
for e,f in combinations(edges_two_arms(),2): same_orbits.setdefault(canon_same(e,f),(e,f))
assert len(same_orbits)==58
same_regular=0; same_disc=[]
for e,f in same_orbits.values():
    inds=[z[1] for z in (e,f) if z[0] in ('a','b','x','i1','i2','i3')]
    n0=max(inds)+1 if inds else 0
    cs,bad=regular_univar(q_same(e,f),n0)
    if not bad:
        same_regular+=1; continue
    assert all(j==3 for j,_,_ in bad)
    D=sp.factor(sp.expand_func(sp.cancel(4*cs[4]*cs[2]-cs[3]**2)))
    assert h not in D.free_symbols
    P=shift_poly(D,n0)
    assert all(cc>0 for cc in P.coeffs())
    same_disc.append((e,f,n0,D))
assert same_regular==52 and len(same_disc)==6

core_edges=[(0,1),(0,2),(1,2)]
def triangle_seed(req_edges=()):
    req={tuple(sorted(e)) for e in req_edges}; row=[0]*5
    for bits in product((0,1),repeat=3):
        chosen=[core_edges[i] for i,b in enumerate(bits) if b]
        if any(e not in chosen for e in req): continue
        if len(chosen)==3: continue
        lab=(0,1,2); ok=True
        for a,b in chosen:
            lab=union_part(lab,a,b)
            if lab is None: ok=False; break
        if ok: row[ST.index(canon(lab))]+=1
    return sp.Matrix([row])
assert triangle_seed(())==Qtri

@lru_cache(None)
def q_core_comp(core_e,comp_e):
    ts=[]
    for mask in range(4):
        seed=triangle_seed((core_e,)) if mask&1 else Qtri
        M5=Tcomp((comp_e,)) if mask&2 else Tun
        ts.append(triple(seed,M5))
    return delta_q(ts)

@lru_cache(None)
def q_core_core(e,f):
    ts=[]
    for mask in range(4):
        req=() if mask==0 else (e,) if mask==1 else (f,) if mask==2 else (e,f)
        ts.append(triple(triangle_seed(req),Tun))
    return delta_q(ts)

Eone=[('c',t) for t in range(3)]
Eone += [('a',0,t) for t in range(3)]+[('b',0,t) for t in range(3)]+[('x',0,t) for t in range(3)]+[('i1',0),('i2',0),('i3',0)]
def map_one(e,tp):
    if e[0]=='c': return ('c',tp[e[1]])
    if e[0] in ('a','b','x'): return (e[0],0,tp[e[2]])
    return e

def map_core(e,tp): return tuple(sorted((tp[e[0]],tp[e[1]])))
corecomp={}
for ce in core_edges:
    for fe in Eone:
        can=min([(map_core(ce,tp),map_one(fe,tp)) for tp in terms],key=repr)
        corecomp.setdefault(can,(ce,fe))
assert len(corecomp)==11
for ce,fe in corecomp.values():
    n0=0 if fe[0]=='c' else 1
    _,bad=regular_univar(q_core_comp(ce,fe),n0)
    assert not bad
_,bad=regular_univar(q_core_core((0,1),(0,2)),0)
assert not bad

# Strictness at u=0.
strict0=[]
for e,f in same_orbits.values():
    inds=[z[1] for z in (e,f) if z[0] in ('a','b','x','i1','i2','i3')]
    n0=max(inds)+1 if inds else 0
    c0=strip_coeffs(q_same(e,f))[0]
    assert h not in c0.free_symbols
    P=shift_poly(c0,n0)
    assert all(cc>=0 for cc in P.coeffs()) and P.eval(0)>0
    strict0.append(P.eval(0))
for ce,fe in corecomp.values():
    n0=0 if fe[0]=='c' else 1
    c0=strip_coeffs(q_core_comp(ce,fe))[0]
    assert h not in c0.free_symbols
    P=shift_poly(c0,n0); assert all(cc>=0 for cc in P.coeffs()) and P.eval(0)>0; strict0.append(P.eval(0))
c0=strip_coeffs(q_core_core((0,1),(0,2)))[0]
P=shift_poly(c0,0); assert all(cc>=0 for cc in P.coeffs()) and P.eval(0)>0; strict0.append(P.eval(0))
print('STRICT_U0_MIN_NUM_CONST',min(strict0))

print('NM13-04 DEPTH3 SAME/CORE CERTIFICATE')
print('ARM3_OPERATOR_PASS', (M.rank(),(M**2).rank(),(M**3).rank(),(M**4).rank()))
print('RHO_STRIP',lo,hi)
print('SAME_COMPONENT_ORBITS',len(same_orbits),'regular',same_regular,'discriminant',len(same_disc),'failures',0)
for j,(e,f,n0,D) in enumerate(same_disc,1): print('DISC',j,e,f,'n0',n0,'D',D)
print('CORE_COMPONENT_ORBITS',len(corecomp),'failures',0)
print('CORE_CORE_PASS')
print('ALL_EXACT_CHECKS_PASS')
