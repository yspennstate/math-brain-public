from itertools import product
from functools import lru_cache
import collections
import sympy as sp

# ---------- partition utilities ----------
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

# ---------- exact star tail ----------
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

def leaf_matrix(req_edges=()):
    req=set(req_edges); M=sp.zeros(15)
    for si,lab in enumerate(P4):
        lab2=introduce(lab)
        stage=[(('i',),3,4)]+[(('s',t),t,4) for t in range(3)]
        for bits in product((0,1),repeat=4):
            if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)): continue
            cur=lab2; ok=True
            for bit,(eid,a,b) in zip(bits,stage):
                if bit:
                    cur=union_part(cur,a,b)
                    if cur is None: ok=False; break
            if ok: M[si,p4idx[forget(cur,4)]]+=1
    return M

Close=sp.zeros(15,5)
for i,lab in enumerate(P4): Close[i,ST.index(forget(lab,3))]+=1
Start=start_center_matrix(); L=leaf_matrix(); J=L-5*sp.eye(15)
assert J**4==sp.zeros(15) and J**3!=sp.zeros(15)
assert (J.rank(),(J**2).rank(),(J**3).rank(),(J**4).rank())==(8,2,1,0)

S=Start*Close
I5=sp.eye(5); N=S-4*I5; N2=N*N
assert N2*N==sp.zeros(5)
ones=sp.Matrix([1]*5); N1=N*ones; N2one=N2*ones

m,n,u,v,h=sp.symbols('m n u v h', integer=True, nonnegative=True)
x,y=sp.symbols('x y', nonnegative=True)

def Lnorm_power(r):
    return sp.eye(15)+r*J/5+sp.binomial(r,2)*(J**2)/25+sp.binomial(r,3)*(J**3)/125

@lru_cache(None)
def Tnorm(msym, req_edges=()):
    center=[]; byleaf=collections.defaultdict(list)
    for e in req_edges:
        if e[0]=='c': center.append(e[1])
        elif e[0]=='s': byleaf[e[1]].append(('s',e[2]))
        elif e[0]=='i': byleaf[e[1]].append(('i',))
        else: raise AssertionError(e)
    leaves=sorted(byleaf); remap={old:i for i,old in enumerate(leaves)}
    req2=collections.defaultdict(list)
    for old,rs in byleaf.items(): req2[remap[old]].extend(rs)
    k=len(leaves)
    M=start_center_matrix(tuple(center))
    for i in range(k): M=M*leaf_matrix(tuple(req2[i]))
    return sp.simplify(M*Lnorm_power(msym-k)*Close/(5**k))

Tun=Tnorm(m)
A=sp.factor(Tun[0,0]); B=sp.factor(Tun[0,1]); C=sp.factor((Tun[0,4]-Tun[0,1])/6)
assert sp.simplify(A-(3*m+20)/5)==0
assert sp.simplify(B-(4*m**2+31*m+25)/25)==0
assert sp.simplify(C-m*(16*m**2+127*m+107)/750)==0
rho=sp.factor((B/A)/2-(C/A)/(B/A))
assert sp.simplify(rho-(43*m**3+622*m**2+2510*m+1875)/(30*(3*m+20)*(4*m**2+31*m+25)))==0

# ---------- left triangle seed with optional required core edges ----------
CORE=((0,1),(0,2),(1,2))
@lru_cache(None)
def seed(req_edges=()):
    req=set(req_edges); row=sp.zeros(1,5)
    for bits in product((0,1), repeat=3):
        if any(e in req and not bit for bit,e in zip(bits,CORE)): continue
        cur=ST[0]; ok=True
        for bit,(a,b) in zip(bits,CORE):
            if bit:
                cur=union_part(cur,a,b)
                if cur is None: ok=False; break
        if ok: row[0,ST.index(cur)] += 1
    return row
Q=seed(())
assert tuple(Q)==(1,1,1,1,3)

def triple(row): return ((row*ones)[0],(row*N1)[0],(row*N2one)[0])

def prod_aff(a,b):
    mons=[(0,0),(1,0),(0,1)]; d=collections.defaultdict(lambda:sp.Integer(0))
    for i,p in enumerate(a):
        for j,q in enumerate(b): d[(mons[i][0]+mons[j][0],mons[i][1]+mons[j][1])]+=sp.expand(p*q)
    return d

def delta_q(ts):
    a=prod_aff(ts[1],ts[2]); b=prod_aff(ts[0],ts[3]); out={}
    for k in set(a)|set(b):
        z=sp.factor(a.get(k,0)-b.get(k,0))
        if z!=0: out[k]=z
    return out

@lru_cache(None)
def q_same(e,f):
    ts=[]
    for mask in range(4):
        req=() if mask==0 else (e,) if mask==1 else (f,) if mask==2 else (e,f)
        ts.append(triple(Q*Tnorm(m,req)))
    return delta_q(ts)

@lru_cache(None)
def q_cross(e,f):
    ts=[]
    for mask in range(4):
        M1=Tnorm(m,(e,) if mask&1 else ())
        M2=Tnorm(m,(f,) if mask&2 else ()).subs(m,n)
        ts.append(triple(Q*M1*M2))
    return delta_q(ts)

@lru_cache(None)
def q_core_core(e,f):
    ts=[]
    for mask in range(4):
        req=() if mask==0 else (e,) if mask==1 else (f,) if mask==2 else (e,f)
        ts.append(triple(seed(req)))
    return delta_q(ts)

@lru_cache(None)
def q_core_star(ecore, estar):
    ts=[]
    for mask in range(4):
        row=seed((ecore,) if mask&1 else ()) * Tnorm(m,(estar,) if mask&2 else ())
        ts.append(triple(row))
    return delta_q(ts)

same_types=[
('cc_diff',('c',0),('c',1),0),('cs_same',('c',0),('s',0,0),1),('cs_diff',('c',0),('s',0,1),1),
('ci',('c',0),('i',0),1),('ss_sameleaf_diff',('s',0,0),('s',0,1),1),('ss_diffleaf_same',('s',0,0),('s',1,0),2),
('ss_diffleaf_diff',('s',0,0),('s',1,1),2),('si_sameleaf',('s',0,0),('i',0),1),('si_diffleaf',('s',0,0),('i',1),2),
('ii_diffleaf',('i',0),('i',1),2),]
cross_types=[
('cc_same',('c',0),('c',0),0,0),('cc_diff',('c',0),('c',1),0,0),('cs_same',('c',0),('s',0,0),0,1),
('cs_diff',('c',0),('s',0,1),0,1),('sc_same',('s',0,0),('c',0),1,0),('sc_diff',('s',0,0),('c',1),1,0),
('ci',('c',0),('i',0),0,1),('ic',('i',0),('c',0),1,0),('ss_same',('s',0,0),('s',0,0),1,1),
('ss_diff',('s',0,0),('s',0,1),1,1),('si',('s',0,0),('i',0),1,1),('is',('i',0),('s',0,0),1,1),('ii',('i',0),('i',0),1,1),]
core_star_types=[
('core_c_incident',(0,1),('c',0),0),
('core_c_opposite',(0,1),('c',2),0),
('core_s_incident',(0,1),('s',0,0),1),
('core_s_opposite',(0,1),('s',0,2),1),
('core_i',(0,1),('i',0),1),
]

lo=sp.Rational(43,360); hi=sp.Rational(1,8)
def strip_coeffs(q):
    c=[sp.Integer(0)]*5
    for (iu,iv),coef in q.items():
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

def shifted_coeff_nonnegative(expr,m0=None,n0=None):
    sub={}; gens=[]
    if m0 is not None: sub[m]=m0+x; gens.append(x)
    if n0 is not None: sub[n]=n0+y; gens.append(y)
    ex=sp.cancel(expr.subs(sub)); num,den=sp.fraction(ex)
    assert not (den.free_symbols & set(gens)) and not den.free_symbols
    if den<0: num=-num
    if not gens:
        return sp.Rational(num)>=0
    P=sp.Poly(sp.expand(num),*gens)
    return all(c>=0 for c in P.coeffs())

def regular(q,m0=None,n0=None):
    for expr in strip_coeffs(q):
        if expr==0: continue
        for b in bern(expr):
            if not shifted_coeff_nonnegative(b,m0,n0): return False
    return True

def physical_constant(q, subs):
    z=q.get((0,0),0)
    return sp.factor(z.subs(subs) if hasattr(z,'subs') else z)

results=[]; failures=[]
qcc=q_core_core(CORE[0],CORE[1])
(results if regular(qcc) else failures).append(('core_core',qcc,None,None))
for name,ec,es,m0 in core_star_types:
    q=q_core_star(ec,es)
    (results if regular(q,m0) else failures).append((name,q,m0,None))
for name,e,f,m0 in same_types:
    q=q_same(e,f)
    (results if regular(q,m0) else failures).append(('same_'+name,q,m0,None))
for name,e,f,m0,n0 in cross_types:
    q=q_cross(e,f)
    (results if regular(q,m0,n0) else failures).append(('cross_'+name,q,m0,n0))

print('seed',tuple(Q))
print('star_rho',rho)
print('regular_count',len(results),'fail_count',len(failures))
print('failures',[z[0] for z in failures])

repairs=[]
for name,q,m0,n0 in failures:
    sc=strip_coeffs(q)
    if n0 is not None:
        print('UNHANDLED two-size failure',name); continue
    q02=q.get((0,2),0); q20=q.get((2,0),0); q01=q.get((0,1),0); q11=q.get((1,1),0)
    K=sp.factor(q02*(q20+q01/2)-q11*q11/4)
    ident=sp.factor(4*sc[4]*sc[2]-sc[3]**2-K)
    good=(ident==0 and shifted_coeff_nonnegative(q02,m0) and shifted_coeff_nonnegative(K,m0)
          and shifted_coeff_nonnegative(sc[0],m0)
          and all(shifted_coeff_nonnegative(b,m0) for b in bern(sc[1])))
    print('repair',name,'good',good,'K=',K)
    if good: repairs.append((name,K))

strict=[]
strict.append(('core_core',physical_constant(qcc,{})))
for name,ec,es,m0 in core_star_types: strict.append((name,physical_constant(q_core_star(ec,es),{m:m0})))
for name,e,f,m0 in same_types: strict.append(('same_'+name,physical_constant(q_same(e,f),{m:m0})))
for name,e,f,m0,n0 in cross_types: strict.append(('cross_'+name,physical_constant(q_cross(e,f),{m:m0,n:n0})))
print('min_constants', sorted(strict,key=lambda z:sp.Rational(z[1]))[:8])
assert all(sp.Rational(z)>0 for _,z in strict)
assert len(results)+len(repairs)==1+len(core_star_types)+len(same_types)+len(cross_types)

# Direct all-forest sanity check: K3 join S_2 (6 vertices, 14 edges).
verts=list(range(6)); edges=[]
edges += [(0,1),(0,2),(1,2)]
for center,leaves in [(3,[4,5])]:
    comp=[center]+leaves
    for w in comp:
        for t in range(3): edges.append((t,w))
    for leaf in leaves: edges.append((center,leaf))
E=len(edges)
print('sanity_graph V,E',len(verts),E)

def acyclic_subset(mask):
    parent=list(range(len(verts)))
    def find(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]; a=parent[a]
        return a
    def union(a,b):
        a=find(a); b=find(b)
        if a==b:return False
        parent[b]=a; return True
    for i,(a,b) in enumerate(edges):
        if (mask>>i)&1:
            if not union(a,b): return False
    return True

Z=0; Ie=[0]*E; Ief=[[0]*E for _ in range(E)]
for mask in range(1<<E):
    if not acyclic_subset(mask): continue
    Z+=1
    inc=[i for i in range(E) if (mask>>i)&1]
    for i in inc: Ie[i]+=1
    for aa in range(len(inc)):
        for bb in range(aa+1,len(inc)):
            i,j=inc[aa],inc[bb]; Ief[i][j]+=1
gaps=[]
for i in range(E):
    for j in range(i+1,E): gaps.append(Ie[i]*Ie[j]-Z*Ief[i][j])
print('sanity_Z',Z,'min_gap',min(gaps),'max_gap',max(gaps))
assert min(gaps)>0

print('ALL_EXACT_CHECKS_PASS')
