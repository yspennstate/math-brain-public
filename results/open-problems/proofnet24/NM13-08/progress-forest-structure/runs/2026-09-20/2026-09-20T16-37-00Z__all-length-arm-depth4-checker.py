from itertools import product, permutations, combinations, combinations_with_replacement
from functools import lru_cache
import collections, sympy as sp

# Exact generator/replay routines. The full monolithic run is deliberately not
# claimed as executed under the local wall cap; these routines were executed in
# staged chunks and their actual exact output is archived beside this file.
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
        for z in range(mx+2): pref.append(z); rec(pref,max(mx,z)); pref.pop()
    rec([0],0); return list(dict.fromkeys(out))

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

# all-length arm-tail closure
P=E**3-7*E**2+8*E-2*sp.eye(52)
assert P**3==sp.zeros(52) and (P.rank(),(P**2).rank(),(P**3).rank())==(20,5,0)
Ls={d:Ld(d) for d in range(1,13)}; s={d:Ls[d][0,0] for d in Ls}
assert [s[d] for d in range(1,13)]==[5,28,158,892,5036,28432,160520,906256,5116496,28886464,163085792,920741824]
for d in range(3,13): assert s[d]==6*s[d-1]-2*s[d-2]
J=Ls[1]-5*sp.eye(15); K=Ls[2]-28*sp.eye(15)
V=[K,K**2,K**3,J,J*K,J**2]
Bmat=sp.Matrix.hstack(*[b.reshape(225,1) for b in V]); assert Bmat.rank()==6
for d in range(1,10):
    sol=list(sp.linsolve((Bmat,(Ls[d]-s[d]*sp.eye(15)).reshape(225,1))))[0]
    assert all(not z.free_symbols for z in sol)
for a in V:
    for b in V:
        sol=list(sp.linsolve((Bmat,(a*b).reshape(225,1))))[0]
        assert all(not z.free_symbols for z in sol) and a*b==b*a
for inds in combinations_with_replacement(range(6),4):
    Q=sp.eye(15)
    for i in inds: Q=Q*V[i]
    assert Q==sp.zeros(15)

# pure depth-four spider atom
L4=Ls[4]; M4=L4-892*sp.eye(15)
assert (M4.rank(),(M4**2).rank(),(M4**3).rank(),(M4**4).rank())==(8,2,1,0)
N=Start*Close-4*sp.eye(5); assert N**3==sp.zeros(5)
ones=sp.Matrix([1]*5); N1=N*ones; N2one=(N*N)*ones; Q0=sp.Matrix([[1,0,0,0,0]])
m,n,X,Y,u,v,h=sp.symbols('m n X Y u v h', nonnegative=True)
lo=sp.Rational(43,360); hi=sp.Rational(1,8)
def M4pow(r): return sp.eye(15)+r*M4/892+sp.binomial(r,2)*M4**2/892**2+sp.binomial(r,3)*M4**3/892**3
Tun=sp.simplify(Start*M4pow(m)*Close)
A=sp.factor(Tun[0,0]); B=sp.factor(Tun[0,1]); C=sp.factor((Tun[0,4]-Tun[0,1])/6)
assert sp.simplify(A-4*(36*m+223)/223)==0
assert sp.simplify(B-(34560*m**2+223674*m+49729)/49729)==0
assert sp.simplify(C-m*(24883200*m**2+162422592*m+37717933)/66537402)==0
rho=sp.factor((B/A)/2-(C/A)/(B/A))
assert sp.simplify((rho-lo)-(7672320*m**3+115127982*m**2+476185503*m+2472973441)/(40140*(36*m+223)*(34560*m**2+223674*m+49729)))==0
assert sp.simplify((hi-rho)-m*(17985024*m**2+226610742*m+736408217)/(2676*(36*m+223)*(34560*m**2+223674*m+49729)))==0

@lru_cache(None)
def arm_req(reqtuple):
    req=set(reqtuple); R=first_step_matrix(frozenset(req))
    for pos in range(2,5): R=R*ext_step_matrix(pos,frozenset(req))
    return R*Fclose
assert arm_req(())==L4
def local_req(e):
    if e[0]=='s': return ('s',e[2],e[3])
    if e[0]=='i': return ('i',e[2])
    raise AssertionError
@lru_cache(None)
def Tspider(reqtuple):
    centers=[]; arms=collections.defaultdict(list)
    for e in reqtuple:
        if e[0]=='c': centers.append(e[1])
        else: arms[e[1]].append(local_req(e))
    R=start_center_matrix(tuple(centers)); keys=sorted(arms)
    for a in keys: R=R*arm_req(tuple(sorted(arms[a],key=repr)))/892
    return sp.simplify(R*M4pow(m-len(keys))*Close)

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
def q_same(e,f): return delta_q([triple(Q0*Tspider(r)) for r in [(),(e,),(f,),(e,f)]])
def strip_coeffs(qd):
    c=[sp.Integer(0)]*5
    for (iu,iv),coef in qd.items():
        if iv==0: c[iu]+=coef
        elif iv==1: c[iu+2]+=coef/2; c[iu+1]-=coef*h
        elif iv==2: c[iu+4]+=coef/4; c[iu+3]-=coef*h; c[iu+2]+=coef*h*h
    return [sp.factor(z) for z in c]
def bern(expr):
    b0=sp.factor(expr.subs(h,lo)); b2=sp.factor(expr.subs(h,hi)); b1=sp.factor(b0+sp.diff(expr,h).subs(h,lo)*(hi-lo)/2)
    return [b0,b1,b2]
def nonneg_shift(expr,m0):
    z=sp.cancel(expr.subs(m,m0+X))
    if z==0:return True
    num,den=z.as_numer_denom(); nc=sp.Poly(sp.expand(num),X).all_coeffs(); dc=sp.Poly(sp.expand(den),X).all_coeffs()
    if all(c<0 for c in dc): nc=[-c for c in nc]; dc=[-c for c in dc]
    return all(c>=0 for c in nc) and all(c>0 for c in dc)
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
reg=disc=eq=0
for e,f in orbits.values():
    m0=minarms(e,f); cs=strip_coeffs(q_same(e,f))
    if all(nonneg_shift(bb,m0) for cj in cs for bb in bern(cj)): reg+=1
    else:
        c0,c1,c2,c3,c4=cs; D=sp.factor(4*c4*c2-c3**2)
        assert h not in D.free_symbols and nonneg_shift(c4,m0)
        assert all(nonneg_shift(bb,m0) for bb in bern(c0)) and all(nonneg_shift(bb,m0) for bb in bern(c1))
        assert nonneg_shift(D,m0) and D.subs(m,m0)>0 and c4.subs(m,m0)>0; disc+=1
    if sp.factor(cs[0].subs(m,m0))==0:
        eq+=1; assert (e,f,m0)==(('c',0),('c',1),0)
assert (reg,disc,eq)==(82,15,1)

# one-edge response algebra / cross-component schemes
def Cextract(T):
    d=sp.factor(T[0,0]); x=tuple(sp.factor(T[0,j]/d) for j in range(1,4)); z=sp.factor(T[0,4]/d); t=sum(x)
    Cc=sp.Matrix([[1,x[0],x[1],x[2],z],[0,1,0,0,t-x[0]],[0,0,1,0,t-x[1]],[0,0,0,1,t-x[2]],[0,0,0,0,1]])
    assert sp.simplify(T/d-Cc)==sp.zeros(5); return d,x,z
def kappa(x,y): return sp.factor(sum(x)*sum(y)-sum(x[i]*y[i] for i in range(3)))
def subresp(R,var):
    d,x,z=R; return sp.factor(d.subs(m,var)),tuple(sp.factor(a.subs(m,var)) for a in x),sp.factor(z.subs(m,var))
def strict_pos_shift2(expr,m0,n0):
    z=sp.factor(expr.subs({m:m0+X,n:n0+Y})); num,den=sp.cancel(z).as_numer_denom(); assert num!=0
    nc=sp.Poly(sp.expand(num),X,Y).coeffs(); dc=sp.Poly(sp.expand(den),X,Y).coeffs()
    if all(c<0 for c in dc): nc=[-c for c in nc]; dc=[-c for c in dc]
    return all(c>0 for c in nc) and all(c>0 for c in dc),min(nc)
un=Cextract(Tspider(())); un_n=subresp(un,n)
defs={'c':lambda t:('c',t)}
for pos in range(1,5):
    defs[f's{pos}']=lambda t,pos=pos:('s',0,pos,t); defs[f'i{pos}']=lambda t,pos=pos:('i',0,pos)
spoke={'c'}|{f's{p}' for p in range(1,5)}; resp={}
for typ,fn in defs.items():
    for term in ([0,1] if typ in spoke else [0]): resp[(typ,term)]=Cextract(Tspider((fn(term),)))
names=list(defs); schemes=[]
for i,t1 in enumerate(names):
    for t2 in names[i:]:
        schemes.append((t1,t2,'same' if t1 in spoke and t2 in spoke else 'na'))
        if t1 in spoke and t2 in spoke: schemes.append((t1,t2,'diff'))
assert len(schemes)==60
mins={lab:None for lab in ('k','L2','L1','C0')}
for t1,t2,rel in schemes:
    term2=1 if rel=='diff' else 0; _,x,z=un; _,y,w=un_n
    _,xe,ze=resp[(t1,0)]; _,yf,wf=subresp(resp[(t2,term2 if t2 in spoke else 0)],n)
    delta=tuple(sp.factor(xe[i]-x[i]) for i in range(3)); eps=tuple(sp.factor(yf[i]-y[i]) for i in range(3))
    alpha=sp.factor(ze-z); beta=sp.factor(wf-w); d=sp.factor(sum(delta)); ee=sp.factor(sum(eps)); kk=sp.factor(kappa(delta,eps))
    aa=sp.factor(d+alpha+kappa(delta,y)); bb=sp.factor(ee+beta+kappa(x,eps)); H0=sp.factor(1+sum(x)+sum(y)+z+w+kappa(x,y)); s0=sp.factor(4+2*(sum(x)+sum(y)))
    vals={'k':kk,'L2':sp.factor(4*d*ee-3*kk),'L1':sp.factor(2*aa*ee+2*bb*d-kk*(s0-6*lo)),'C0':sp.factor(aa*bb-H0*kk)}
    m0=0 if t1=='c' else 1; n0=0 if t2=='c' else 1
    for lab,expr in vals.items():
        ok,mn=strict_pos_shift2(expr,m0,n0); assert ok
        if mins[lab] is None or mn<mins[lab][0]: mins[lab]=(mn,(t1,t2,rel))
assert mins=={'k':(sp.Integer(7672320),('c','c','same')),'L2':(sp.Integer(23887872),('c','c','diff')),'L1':(sp.Integer(687970713600),('c','c','diff')),'C0':(sp.Integer(2751882854400),('c','c','diff'))}

# finite exact matrix-DP sanity, m=2
@lru_cache(None)
def Tnum(reqtuple,mval=2):
    centers=[]; arms=collections.defaultdict(list)
    for e in reqtuple:
        if e[0]=='c': centers.append(e[1])
        else: arms[e[1]].append(local_req(e))
    R=start_center_matrix(tuple(centers)); keys=sorted(arms)
    for a in keys: R=R*arm_req(tuple(sorted(arms[a],key=repr)))
    return R*(L4**(mval-len(keys)))*Close
T0=Tnum((),2); Icnt=int((Q0*T0*ones)[0]); assert Icnt==111180256
Ephys=edges_witness(2); singles={e:int((Q0*Tnum((e,),2)*ones)[0]) for e in Ephys}; ming=None; minpair=None
for e,f in combinations(Ephys,2):
    Ief=int((Q0*Tnum((e,f),2)*ones)[0]); gap=singles[e]*singles[f]-Icnt*Ief
    if ming is None or gap<ming: ming=gap; minpair=(e,f)
assert ming==566808252288 and minpair==(('i',0,3),('i',1,3))
print('ALL_EXACT_CHECKS_PASS')
