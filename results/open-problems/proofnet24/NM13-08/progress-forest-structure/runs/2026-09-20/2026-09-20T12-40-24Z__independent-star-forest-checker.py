from itertools import product, combinations
from functools import lru_cache
from fractions import Fraction
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

# Three terminals: five connectivity states.
ST=[canon((0,1,2)),canon((0,1,1)),canon((0,0,1)),canon((0,1,0)),canon((0,0,0))]
P4=all_partitions(4); assert len(P4)==15
p4idx={s:i for i,s in enumerate(P4)}

# ---------- exact 15-state star-leaf tail ----------
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
Start=start_center_matrix()
L=leaf_matrix(); J=L-5*sp.eye(15)
assert J**4==sp.zeros(15) and J**3!=sp.zeros(15)
assert (J.rank(),(J**2).rank(),(J**3).rank(),(J**4).rank())==(8,2,1,0)

def mat_tuple(M): return tuple(tuple(int(M[i,j]) for j in range(M.cols)) for i in range(M.rows))
S=mat_tuple(Start*Close)
I5=tuple(tuple(1 if i==j else 0 for j in range(5)) for i in range(5))
def mm(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
N=tuple(tuple(S[i][j]-4*I5[i][j] for j in range(5)) for i in range(5)); N2=mm(N,N); N3=mm(N2,N)
assert all(x==0 for row in N3 for x in row)
Nsp=sp.Matrix(N); N2sp=sp.Matrix(N2)
ones=sp.Matrix([1]*5); N1=Nsp*ones; N2one=N2sp*ones; Q0=sp.Matrix([[1,0,0,0,0]])

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
assert sp.simplify((rho-sp.Rational(43,360))-(5*m**2+47*m+200)/(72*(3*m+20)*(4*m**2+31*m+25)))==0
assert sp.simplify((sp.Rational(1,8)-rho)-m*(8*m**2+107*m+385)/(120*(3*m+20)*(4*m**2+31*m+25)))==0

@lru_cache(None)
def transfer_star(mm, reqt=()):
    req=set(reqt); M=[[0]*5 for _ in range(5)]
    for si,ts in enumerate(ST):
        dp={introduce(ts):1}; nd=collections.defaultdict(int)
        stage=[(('c',t),t,3) for t in range(3)]
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
        for i in range(mm):
            nd=collections.defaultdict(int)
            stage=[(('i',i),3,4)]+[(('s',i,t),t,4) for t in range(3)]
            for lab,cnt in dp.items():
                lab2=introduce(lab)
                for bits in product((0,1),repeat=4):
                    if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)): continue
                    cur=lab2; ok=True
                    for bit,(eid,a,b) in zip(bits,stage):
                        if bit:
                            cur=union_part(cur,a,b)
                            if cur is None: ok=False; break
                    if ok: nd[forget(cur,4)]+=cnt
            dp=nd
        for lab,cnt in dp.items(): M[si][ST.index(forget(lab,3))]+=cnt
    return tuple(tuple(r) for r in M)

def eval_mat(Ms,mm):
    return tuple(tuple(sp.Rational(Ms[i,j].subs(m,mm)) for j in range(5)) for i in range(5))
def norm_direct(mm,req):
    D=transfer_star(mm,tuple(req)); return tuple(tuple(sp.Rational(D[i][j],5**mm) for j in range(5)) for i in range(5))

def triple(row): return ((row*ones)[0],(row*N1)[0],(row*N2one)[0])
def prod_aff(a,b):
    mons=[(0,0),(1,0),(0,1)]; d=collections.defaultdict(lambda:0)
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
        ts.append(triple(Q0*Tnorm(m,req)))
    return delta_q(ts)
@lru_cache(None)
def q_cross(e,f):
    ts=[]
    for mask in range(4):
        M1=Tnorm(m,(e,) if mask&1 else ())
        M2=Tnorm(m,(f,) if mask&2 else ()).subs(m,n)
        ts.append(triple(Q0*M1*M2))
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

patterns=set([()])
for _,e,f,m0 in same_types:
    patterns.add((e,)); patterns.add((f,)); patterns.add((e,f))
for req in patterns:
    leaves=[e[1] for e in req if e[0] in ('s','i')]; mmin=(max(leaves)+1 if leaves else 0)
    for mm in range(mmin,6): assert eval_mat(Tnorm(m,req),mm)==norm_direct(mm,req)

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
def shifted_coeff_nonnegative(expr,m0,n0=None):
    sub={m:m0+x}; gens=[x]
    if n0 is not None: sub[n]=n0+y; gens.append(y)
    ex=sp.cancel(expr.subs(sub)); num,den=sp.fraction(ex)
    assert not den.free_symbols
    if den<0: num=-num
    P=sp.Poly(sp.expand(num),*gens)
    return all(c>=0 for c in P.coeffs())
def regular(q,m0,n0=None):
    for expr in strip_coeffs(q):
        if expr==0: continue
        for b in bern(expr):
            if not shifted_coeff_nonnegative(b,m0,n0): return False
    return True

same_results=[]
for name,e,f,m0 in same_types:
    q=q_same(e,f)
    if regular(q,m0): same_results.append((name,'REGULAR'))
    else:
        assert name=='ss_diffleaf_diff'
        sc=strip_coeffs(q); q02=q[(0,2)]; q20=q[(2,0)]; q01=q[(0,1)]; q11=q[(1,1)]
        K=sp.factor(q02*(q20+q01/2)-q11*q11/4)
        assert sp.simplify(K-108*(573*m**2+7832*m+30144)/9765625)==0
        assert shifted_coeff_nonnegative(q02,m0) and shifted_coeff_nonnegative(K,m0) and shifted_coeff_nonnegative(sc[0],m0)
        assert all(shifted_coeff_nonnegative(b,m0) for b in bern(sc[1]))
        assert sp.factor(4*sc[4]*sc[2]-sc[3]**2-K)==0
        same_results.append((name,'DISCRIMINANT'))

cross_results=[]
for name,e,f,m0,n0 in cross_types:
    q=q_cross(e,f); assert regular(q,m0,n0); cross_results.append((name,'REGULAR'))
assert collections.Counter(z for _,z in same_results+cross_results)==collections.Counter({'REGULAR':22,'DISCRIMINANT':1})

qcc=q_same(('c',0),('c',1))
assert sp.factor(qcc[(0,0)])==m*(16*m**3+131*m**2+373*m+380)/625
for name,e,f,m0 in same_types[1:]: assert q_same(e,f)[(0,0)].subs(m,m0)>0
for name,e,f,m0,n0 in cross_types: assert q_cross(e,f)[(0,0)].subs({m:m0,n:n0})>0

def rv_tuple(r,c): return sum(r[i]*c[i] for i in range(len(r)))
def rm_tuple(r,M): return tuple(sum(r[k]*M[k][j] for k in range(len(r))) for j in range(len(M[0])))
one_tuple=(1,1,1,1,1); Q0_tuple=(1,0,0,0,0)
def star_edges(mm): return [('c',t) for t in range(3)]+[('s',i,t) for i in range(mm) for t in range(3)]+[('i',i) for i in range(mm)]
def physical(mm):
    Z=rv_tuple(rm_tuple(Q0_tuple,transfer_star(mm)),one_tuple); gaps=[]
    for e,f in combinations(star_edges(mm),2):
        Ze=rv_tuple(rm_tuple(Q0_tuple,transfer_star(mm,(e,))),one_tuple)
        Zf=rv_tuple(rm_tuple(Q0_tuple,transfer_star(mm,(f,))),one_tuple)
        Zef=rv_tuple(rm_tuple(Q0_tuple,transfer_star(mm,tuple(sorted((e,f),key=repr)))),one_tuple)
        gaps.append(Ze*Zf-Z*Zef)
    return Z,min(gaps)
Z3,g3=physical(3); Z6,g6=physical(6)
assert (Z3,g3)==(5701,80404)
assert (Z6,g6)==(2090000,4923437500)

print('leaf_tail_states',len(P4))
print('rank_J_J2_J3_J4',(J.rank(),(J**2).rank(),(J**3).rank(),(J**4).rank()))
print('unmarked_A_over_5m',A)
print('unmarked_B_over_5m',B)
print('unmarked_C_over_5m',C)
print('rho_m',rho)
print('rho_lower_gap',sp.factor(rho-sp.Rational(43,360)))
print('rho_upper_gap',sp.factor(sp.Rational(1,8)-rho))
print('same_pair_types',same_results)
print('cross_pair_types',cross_results)
print('certificate_counts',dict(collections.Counter(z for _,z in same_results+cross_results)))
print('exceptional_K',108*(573*m**2+7832*m+30144)/9765625)
print('physical_m3',{'vertices':7,'edges':15,'forests':Z3,'min_gap':g3})
print('physical_m6',{'vertices':10,'edges':27,'forests':Z6,'min_gap':g6})
print('ALL_EXACT_CHECKS_PASS')
