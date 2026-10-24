from itertools import product, permutations, combinations
from functools import lru_cache
import collections, sympy as sp

# Exact partition-state transfer for three terminals plus one retained center.
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

def introduce(labels):
    return canon(tuple(labels)+(max(labels,default=-1)+1,))

def forget(labels,idx):
    return canon(tuple(q for i,q in enumerate(labels) if i!=idx))

def all_partitions(n):
    out=[]
    def rec(pref,mx):
        if len(pref)==n:
            out.append(canon(pref)); return
        for z in range(mx+2):
            pref.append(z); rec(pref,max(mx,z)); pref.pop()
    rec([0],0)
    return list(dict.fromkeys(out))

ST=[canon((0,1,2)),canon((0,1,1)),canon((0,0,1)),
    canon((0,1,0)),canon((0,0,0))]
P4=all_partitions(4)
assert len(P4)==15
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

def arm_matrix(length, req_edges=()):
    """One center-rooted arm of given length; every new arm vertex meets all 3 terminals."""
    req=set(req_edges); M=sp.zeros(15)
    for si,lab in enumerate(P4):
        cur0=lab
        for _ in range(length): cur0=introduce(cur0)
        stage=[]; prev=3
        for pos in range(1,length+1):
            idx=3+pos
            stage.append(((f'i{pos}',),prev,idx))
            stage += [((f's{pos}',t),t,idx) for t in range(3)]
            prev=idx
        for bits in product((0,1),repeat=4*length):
            if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)): continue
            cur=cur0; ok=True
            for bit,(eid,a,b) in zip(bits,stage):
                if bit:
                    cur=union_part(cur,a,b)
                    if cur is None: ok=False; break
            if ok:
                for idx in range(3+length,3,-1): cur=forget(cur,idx)
                M[si,p4idx[cur]]+=1
    return M

Close=sp.zeros(15,5)
for i,lab in enumerate(P4):
    Close[i,ST.index(forget(lab,3))]+=1

Start=start_center_matrix()
L1=arm_matrix(1); L2=arm_matrix(2); L3=arm_matrix(3)
J=L1-5*sp.eye(15); K=L2-28*sp.eye(15); M=L3-158*sp.eye(15)

# New depth-three closure.
assert J**4==sp.zeros(15) and K**4==sp.zeros(15) and M**4==sp.zeros(15)
assert (M.rank(),(M**2).rank(),(M**3).rank(),(M**4).rank())==(8,2,1,0)
assert J*M==M*J and K*M==M*K
assert M == (sp.Rational(82,7)*K + sp.Rational(73,1029)*K**2
             - sp.Rational(1376,893025)*K**3 - sp.Rational(254,7)*J
             + sp.Rational(282,343)*J*K - sp.Rational(4185,343)*J**2)
basis=[sp.eye(15),K,K**2,K**3,J,J*K,J**2]
assert sp.Matrix.hstack(*[b.reshape(225,1) for b in basis]).rank()==7

# Five terminal-state nilpotent algebra.
S=Start*Close; N=S-4*sp.eye(5)
assert N**3==sp.zeros(5)
N2=N*N; ones=sp.Matrix([1]*5); N1=N*ones; N2one=N2*ones
Q0=sp.Matrix([[1,0,0,0,0]])

m,n,X,Y,u,v,h=sp.symbols('m n X Y u v h', nonnegative=True)
lo=sp.Rational(43,360); hi=sp.Rational(1,8)

def Mpow(r):
    return (sp.eye(15)+r*M/158+sp.binomial(r,2)*M**2/(158**2)
            +sp.binomial(r,3)*M**3/(158**3))

Tun=sp.simplify(Start*Mpow(m)*Close)
A=sp.factor(Tun[0,0]); B=sp.factor(Tun[0,1]); C=sp.factor((Tun[0,4]-Tun[0,1])/6)
assert sp.simplify(A-(51*m+316)/79)==0
assert sp.simplify(B-(3247*m**2+21322*m+6241)/6241)==0
assert sp.simplify(C-m*(620177*m**2+4118189*m+1259235)/2958234)==0
rho=sp.factor((B/A)/2-(C/A)/(B/A))
rho_expected=(9391633*m**3+119901505*m**2+400505352*m+116850243)/(474*(51*m+316)*(3247*m**2+21322*m+6241))
assert sp.simplify(rho-rho_expected)==0
assert sp.simplify((rho-lo)-(964971*m**3+14619122*m**2+60943049*m+311600648)/(28440*(51*m+316)*(3247*m**2+21322*m+6241)))==0
assert sp.simplify((hi-rho)-m*(1679957*m**2+21287318*m+70260783)/(1896*(51*m+316)*(3247*m**2+21322*m+6241)))==0

def arm3_all_required():
    edgeids=[]
    for pos in range(1,4):
        edgeids.append((f'i{pos}',))
        edgeids += [(f's{pos}',t) for t in range(3)]
    mats={():sp.zeros(15)}
    for e in edgeids: mats[(e,)]=sp.zeros(15)
    for e,f in combinations(edgeids,2):
        mats[tuple(sorted((e,f),key=repr))]=sp.zeros(15)
    for si,lab in enumerate(P4):
        cur0=lab
        for _ in range(3): cur0=introduce(cur0)
        stage=[]; prev=3
        for pos in range(1,4):
            idx=3+pos
            stage.append(((f'i{pos}',),prev,idx))
            stage += [((f's{pos}',t),t,idx) for t in range(3)]
            prev=idx
        for bits in product((0,1),repeat=12):
            cur=cur0; ok=True; chosen=[]
            for bit,(eid,a,b) in zip(bits,stage):
                if bit:
                    cur=union_part(cur,a,b)
                    if cur is None: ok=False; break
                    chosen.append(eid)
            if not ok: continue
            for idx in range(6,3,-1): cur=forget(cur,idx)
            oi=p4idx[cur]
            mats[()][si,oi]+=1
            for e in chosen: mats[(e,)][si,oi]+=1
            for e,f in combinations(chosen,2):
                mats[tuple(sorted((e,f),key=repr))][si,oi]+=1
    return mats

ARM3_REQ=arm3_all_required()
assert ARM3_REQ[()]==L3
@lru_cache(None)
def arm3_req(req_tuple):
    return ARM3_REQ[tuple(sorted(req_tuple,key=repr))]

def local_req(e):
    if e[0]=='s': return (f's{e[2]}',e[3])
    if e[0]=='i': return (f'i{e[2]}',)
    raise AssertionError(e)

@lru_cache(None)
def Tspider(req_edges_tuple):
    req_edges=list(req_edges_tuple)
    centers=[]; arms=collections.defaultdict(list)
    for e in req_edges:
        if e[0]=='c': centers.append(e[1])
        else: arms[e[1]].append(local_req(e))
    keys=sorted(arms)
    R=start_center_matrix(tuple(centers))
    for a in keys:
        R=R*arm3_req(tuple(sorted(arms[a],key=repr)))/158
    R=R*Mpow(m-len(keys))*Close
    return sp.simplify(R)

assert sp.simplify(Tspider(())-Tun)==sp.zeros(5)

def triple(row):
    return ((row*ones)[0],(row*N1)[0],(row*N2one)[0])

def prod_aff(a,b):
    mons=[(0,0),(1,0),(0,1)]
    d=collections.defaultdict(lambda:sp.Integer(0))
    for i,aa in enumerate(a):
        for j,bb in enumerate(b):
            d[(mons[i][0]+mons[j][0],mons[i][1]+mons[j][1])] += sp.expand(aa*bb)
    return d

def delta_q(ts):
    x1=prod_aff(ts[1],ts[2]); x2=prod_aff(ts[0],ts[3]); out={}
    for k in set(x1)|set(x2):
        z=sp.factor(x1.get(k,0)-x2.get(k,0))
        if z!=0: out[k]=z
    return out

@lru_cache(None)
def q_same(e,f):
    reqs=[(),(e,),(f,),(e,f)]
    ts=[triple(Q0*Tspider(tuple(req))) for req in reqs]
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
    return [sp.factor(z) for z in c]

def bern(expr):
    b0=sp.factor(expr.subs(h,lo)); b2=sp.factor(expr.subs(h,hi))
    b1=sp.factor(b0+sp.diff(expr,h).subs(h,lo)*(hi-lo)/2)
    return [b0,b1,b2]

def nonneg_shift(expr,m0):
    z=sp.factor(expr.subs(m,m0+X))
    if z==0: return True
    num,den=sp.cancel(z).as_numer_denom()
    nc=sp.Poly(sp.expand(num),X).all_coeffs()
    dc=sp.Poly(sp.expand(den),X).all_coeffs()
    if all(c<0 for c in dc): nc=[-c for c in nc]; dc=[-c for c in dc]
    return all(c>=0 for c in nc) and all(c>0 for c in dc)

terms=list(permutations(range(3)))
def edges_witness(arms=2):
    E=[('c',t) for t in range(3)]
    for a in range(arms):
        for pos in range(1,4):
            E += [('s',a,pos,t) for t in range(3)] + [('i',a,pos)]
    return E

def map_edge(e,tp,ap):
    if e[0]=='c': return ('c',tp[e[1]])
    if e[0]=='s': return ('s',ap[e[1]],e[2],tp[e[3]])
    return ('i',ap[e[1]],e[2])

def canon_pair(e,f):
    imgs=[]
    for tp in terms:
        for ar in permutations(range(2)):
            ap={i:ar[i] for i in range(2)}
            ee=map_edge(e,tp,ap); ff=map_edge(f,tp,ap)
            imgs.append(tuple(sorted((ee,ff),key=repr)))
    return min(imgs,key=repr)

orbits={}
for e,f in combinations(edges_witness(),2):
    orbits.setdefault(canon_pair(e,f),(e,f))
assert len(orbits)==58

def minarms(e,f):
    aa=[z[1] for z in (e,f) if z[0] in ('s','i')]
    return max(aa)+1 if aa else 0

import sys, re
MODE=sys.argv[1] if len(sys.argv)>1 else 'core'

def run_core():
    print("CORE PASS")
    print("length3_arm_scalar=158")
    print("length3_nilpotent_rank_profile=8,2,1,0")
    print("length3_in_old_7d_tail_algebra=PASS")
    print("M_relation=82/7 K + 73/1029 K^2 - 1376/893025 K^3 - 254/7 J + 282/343 JK - 4185/343 J^2")
    print("unmarked_transfer_A=",A)
    print("unmarked_transfer_B=",B)
    print("unmarked_transfer_C=",C)
    print("rho=",rho)
    print("rho_minus_43_over_360=",sp.factor(rho-lo))
    print("one_eighth_minus_rho=",sp.factor(hi-rho))
    print("ALL_EXACT_CHECKS_PASS_CORE")

def run_same(batch):
    cuts=[0,15,30,45,58]
    a,b=cuts[batch],cuts[batch+1]
    reps=list(orbits.values())[a:b]
    reg=disc=eq=0
    for e,f in reps:
        m0=minarms(e,f); cs=strip_coeffs(q_same(e,f))
        ok=all(nonneg_shift(bb,m0) for cj in cs for bb in bern(cj))
        if ok:
            reg+=1
            print("REG",repr(e),repr(f),"m0",m0)
        else:
            c0,c1,c2,c3,c4=cs
            D=sp.factor(4*c4*c2-c3**2)
            assert h not in D.free_symbols
            assert nonneg_shift(c4,m0)
            assert all(nonneg_shift(bb,m0) for bb in bern(c0))
            assert all(nonneg_shift(bb,m0) for bb in bern(c1))
            assert nonneg_shift(D,m0)
            assert D.subs(m,m0)>0 and c4.subs(m,m0)>0
            disc+=1
            print("DISC",repr(e),repr(f),"m0",m0,"K=",D)
        if sp.factor(cs[0].subs(m,m0))==0:
            eq+=1
            assert (e,f,m0)==(('c',0),('c',1),0)
            print("BOUNDARY_EQUALITY",repr(e),repr(f),"c0=",sp.factor(cs[0]))
    print(f"SAME_BATCH {batch} range={a}:{b} regular={reg} disc={disc} eq={eq} PASS")

def Cextract_local(T):
    d=sp.factor(T[0,0]); assert d!=0
    for i in range(5): assert sp.simplify(T[i,i]-d)==0
    x=tuple(sp.factor(T[0,j]/d) for j in range(1,4)); z=sp.factor(T[0,4]/d)
    t=sum(x)
    Cc=sp.Matrix([[1,x[0],x[1],x[2],z],
                  [0,1,0,0,t-x[0]],[0,0,1,0,t-x[1]],
                  [0,0,0,1,t-x[2]],[0,0,0,0,1]])
    assert sp.simplify(T/d-Cc)==sp.zeros(5)
    return d,x,z

def kappa_local(x,y):
    return sp.factor(sum(x)*sum(y)-sum(x[i]*y[i] for i in range(3)))

def sub_resp_local(R,var):
    d,x,z=R
    return sp.factor(d.subs(m,var)),tuple(sp.factor(a.subs(m,var)) for a in x),sp.factor(z.subs(m,var))

def strict_pos_shift2(expr,m0,n0):
    z=sp.factor(expr.subs({m:m0+X,n:n0+Y}))
    num,den=sp.cancel(z).as_numer_denom()
    assert num!=0
    nc=sp.Poly(sp.expand(num),X,Y).coeffs()
    dc=sp.Poly(sp.expand(den),X,Y).coeffs()
    if all(c<0 for c in dc): nc=[-c for c in nc]; dc=[-c for c in dc]
    return all(c>0 for c in nc) and all(c>0 for c in dc),min(nc)

def run_cross():
    un=Cextract_local(Tspider(()))
    defs={'c':lambda t:('c',t),
          's1':lambda t:('s',0,1,t),'s2':lambda t:('s',0,2,t),'s3':lambda t:('s',0,3,t),
          'i1':lambda t:('i',0,1),'i2':lambda t:('i',0,2),'i3':lambda t:('i',0,3)}
    spoke={'c','s1','s2','s3'}
    resp={}
    for typ,fn in defs.items():
        for term in ([0,1] if typ in spoke else [0]):
            resp[(typ,term)]=Cextract_local(Tspider((fn(term),)))
    names=list(defs); schemes=[]
    for i,t1 in enumerate(names):
        for t2 in names[i:]:
            schemes.append((t1,t2,'same' if t1 in spoke and t2 in spoke else 'na'))
            if t1 in spoke and t2 in spoke: schemes.append((t1,t2,'diff'))
    assert len(schemes)==38
    mins={lab:None for lab in ('k','L2','L1','C0')}
    un_n=sub_resp_local(un,n)
    for t1,t2,rel in schemes:
        term2=1 if rel=='diff' else 0
        _,x,z=un; _,y,w=un_n
        _,xe,ze=resp[(t1,0)]
        _,yf,wf=sub_resp_local(resp[(t2,term2 if t2 in spoke else 0)],n)
        delta=tuple(sp.factor(xe[i]-x[i]) for i in range(3))
        eps=tuple(sp.factor(yf[i]-y[i]) for i in range(3))
        alpha=sp.factor(ze-z); beta=sp.factor(wf-w)
        d=sp.factor(sum(delta)); e=sp.factor(sum(eps)); kk=sp.factor(kappa_local(delta,eps))
        aa=sp.factor(d+alpha+kappa_local(delta,y)); bb=sp.factor(e+beta+kappa_local(x,eps))
        H0=sp.factor(1+sum(x)+sum(y)+z+w+kappa_local(x,y))
        s0=sp.factor(4+2*(sum(x)+sum(y)))
        vals={'k':kk,'L2':sp.factor(4*d*e-3*kk),
              'L1':sp.factor(2*aa*e+2*bb*d-kk*(s0-6*lo)),
              'C0':sp.factor(aa*bb-H0*kk)}
        m0=0 if t1=='c' else 1; n0=0 if t2=='c' else 1
        for lab,expr in vals.items():
            ok,mn=strict_pos_shift2(expr,m0,n0); assert ok
            if mins[lab] is None or mn<mins[lab][0]: mins[lab]=(mn,(t1,t2,rel))
    expected={'k':(sp.Integer(242182),('c','c','same')),
              'L2':(sp.Integer(751689),('c','c','diff')),
              'L1':(sp.Integer(5742903960),('c','c','diff')),
              'C0':(sp.Integer(3046929601),('c','c','diff'))}
    assert mins==expected
    print("CROSS schemes=38 failures=0 PASS")
    for lab in ('k','L2','L1','C0'):
        print("CROSS_MIN",lab,mins[lab][0],mins[lab][1])
    print("ALL_EXACT_CHECKS_PASS_CROSS")

@lru_cache(None)
def Tspider_num(req_edges_tuple,mval=3):
    req_edges=list(req_edges_tuple); centers=[]; arms=collections.defaultdict(list)
    for e in req_edges:
        if e[0]=='c': centers.append(e[1])
        else: arms[e[1]].append(local_req(e))
    keys=sorted(arms)
    R=start_center_matrix(tuple(centers))
    for a in keys: R=R*arm3_req(tuple(sorted(arms[a],key=repr)))
    R=R*(L3**(mval-len(keys)))*Close
    return R

def run_finite():
    mval=3
    T0=Tspider_num((),mval)
    I=int((Q0*T0*ones)[0])
    assert I==735464752
    E=edges_witness(3); singles={}
    for e in E: singles[e]=int((Q0*Tspider_num((e,),mval)*ones)[0])
    ming=None; minpair=None; cnt=0
    for e,f in combinations(E,2):
        Ief=int((Q0*Tspider_num((e,f),mval)*ones)[0])
        gap=singles[e]*singles[f]-I*Ief
        cnt+=1
        if ming is None or gap<ming: ming=gap; minpair=(e,f)
    assert cnt==741 and ming==22756321142304
    assert minpair==(('i',0,2),('i',1,3))
    print("FINITE m=3 vertices=13 edges=39 forests=",I,"pairs=",cnt)
    print("FINITE min_gap=",ming,"pair=",minpair)
    print("ALL_EXACT_CHECKS_PASS_FINITE")

def run_aggregate(path):
    txt=open(path).read()
    rows=re.findall(r"SAME_BATCH \d+ range=\d+:\d+ regular=(\d+) disc=(\d+) eq=(\d+) PASS",txt)
    assert len(rows)==4
    sr=sum(int(r[0]) for r in rows); sd=sum(int(r[1]) for r in rows); se=sum(int(r[2]) for r in rows)
    assert (sr,sd,se)==(50,8,1)
    assert "ALL_EXACT_CHECKS_PASS_CORE" in txt
    assert "ALL_EXACT_CHECKS_PASS_CROSS" in txt
    assert "ALL_EXACT_CHECKS_PASS_FINITE" in txt
    print("AGGREGATE same_regular=50 same_discriminant=8 boundary_equalities=1")
    print("AGGREGATE cross_schemes=38 finite_pairs=741")
    print("ALL_EXACT_CHECKS_PASS")

if MODE=='core': run_core()
elif MODE=='same': run_same(int(sys.argv[2]))
elif MODE=='cross': run_cross()
elif MODE=='finite': run_finite()
elif MODE=='aggregate': run_aggregate(sys.argv[2])
else: raise SystemExit("unknown mode")
