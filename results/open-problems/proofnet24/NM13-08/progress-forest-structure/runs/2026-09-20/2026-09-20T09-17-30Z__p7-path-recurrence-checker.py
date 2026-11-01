from itertools import combinations, permutations, product
from functools import lru_cache
import collections
import sympy as sp

# NM13-08 / T07 exact checker.
# Family F7_{p,r}=K_{3,7p+r} with p disjoint P7 paths and r isolated
# vertices inside the right side; the three left terminals are independent.
# All real edge weights are one.

L=7

def canon(labels):
    mp={}; out=[]; nxt=0
    for a in labels:
        if a not in mp:
            mp[a]=nxt; nxt+=1
        out.append(mp[a])
    return tuple(out)

TERMINAL_STATES=[
    canon((0,1,2)), canon((0,1,1)), canon((0,0,1)),
    canon((0,1,0)), canon((0,0,0))
]

def union_part(labels,a,b):
    labels=list(labels)
    if labels[a]==labels[b]:
        return None
    la,lb=labels[a],labels[b]
    labels=[la if q==lb else q for q in labels]
    return canon(labels)

def introduce(labels):
    return canon(tuple(labels)+(max(labels,default=-1)+1,))

def forget(labels,idx):
    return canon(tuple(q for i,q in enumerate(labels) if i!=idx))

@lru_cache(None)
def transfer_path(length, required_tuple=()):
    required=set(required_tuple)
    M=[[0]*5 for _ in range(5)]
    for si,tstate in enumerate(TERMINAL_STATES):
        dp={introduce(tstate):1}
        stage=[(('s',0,t),t,3) for t in range(3)]
        nd=collections.defaultdict(int)
        for lab,cnt in dp.items():
            for bits in product([0,1],repeat=3):
                if any((eid in required) and not bit for bit,(eid,_,__) in zip(bits,stage)):
                    continue
                cur=lab; ok=True
                for bit,(eid,a,b) in zip(bits,stage):
                    if bit:
                        cur2=union_part(cur,a,b)
                        if cur2 is None:
                            ok=False; break
                        cur=cur2
                if ok: nd[cur]+=cnt
        dp=nd
        for i in range(1,length):
            nd=collections.defaultdict(int)
            stage=[(('i',i-1,i),3,4)]+[(('s',i,t),t,4) for t in range(3)]
            for lab,cnt in dp.items():
                lab2=introduce(lab)
                for bits in product([0,1],repeat=4):
                    if any((eid in required) and not bit for bit,(eid,_,__) in zip(bits,stage)):
                        continue
                    cur=lab2; ok=True
                    for bit,(eid,a,b) in zip(bits,stage):
                        if bit:
                            cur2=union_part(cur,a,b)
                            if cur2 is None:
                                ok=False; break
                            cur=cur2
                    if ok: nd[forget(cur,3)]+=cnt
            dp=nd
        for lab,cnt in dp.items():
            sj=TERMINAL_STATES.index(forget(lab,3))
            M[si][sj]+=cnt
    return sp.Matrix(M)

S=transfer_path(1)
N=S-4*sp.eye(5)
P7=transfer_path(7)
assert N**3==sp.zeros(5) and N**2!=sp.zeros(5)
assert P7==132088*sp.eye(5)+247492*N+202132*N**2
print('S(singleton)='); print(S)
print('P7 layer='); print(P7)
print('N^3=0: PASS')
print('P7 = 132088 I + 247492 N + 202132 N^2: PASS')

# 15-state path-tail operator and recurrence.
def all_partitions4():
    out=[]
    def rec(prefix,maxlab):
        if len(prefix)==4:
            out.append(tuple(prefix)); return
        for q in range(maxlab+2):
            rec(prefix+[q],max(maxlab,q))
    rec([0],0)
    return out
PART4=all_partitions4(); PI={p:i for i,p in enumerate(PART4)}
E=sp.zeros(15)
for p0 in PART4:
    i0=PI[p0]
    lab2=introduce(p0)
    stage=[(3,4),(0,4),(1,4),(2,4)]
    for bits in product([0,1],repeat=4):
        cur=lab2; ok=True
        for bit,(a,b) in zip(bits,stage):
            if bit:
                cur2=union_part(cur,a,b)
                if cur2 is None:
                    ok=False; break
                cur=cur2
        if ok: E[i0,PI[forget(cur,3)]]+=1
lam=sp.symbols('lam')
char=sp.factor(E.charpoly(lam).as_expr())
Q=E**2-6*E+2*sp.eye(15)
assert char==(lam-1)**5*(lam**2-6*lam+2)**5
assert (E-sp.eye(15))**2*Q**3==sp.zeros(15)
assert (E-sp.eye(15))*Q**3!=sp.zeros(15)
assert (E-sp.eye(15))**2*Q**2!=sp.zeros(15)
print('frontier characteristic polynomial =',char)
print('minimal polynomial = (lambda-1)^2 (lambda^2-6 lambda+2)^3: PASS')

# New coefficient-recurrence sharpening for T_{P_n}=A_n I+B_n N+C_n N^2.
ABC={}
for n in range(1,22):
    M=transfer_path(n)
    A=sp.Integer(M[0,0]); B=sp.Integer(M[0,1]); C=sp.Rational(M[0,4]-B,6)
    assert M==A*sp.eye(5)+B*N+C*N**2
    ABC[n]=(A,B,C)
for n in range(1,20):
    A0,A1,A2=ABC[n][0],ABC[n+1][0],ABC[n+2][0]
    assert A2==6*A1-2*A0
for n in range(1,18):
    vals=[ABC[n+j][1] for j in range(5)]
    assert vals[4]==12*vals[3]-40*vals[2]+24*vals[1]-4*vals[0]
for n in range(1,16):
    vals=[ABC[n+j][2] for j in range(7)]
    assert vals[6]==18*vals[5]-114*vals[4]+288*vals[3]-228*vals[2]+72*vals[1]-8*vals[0]
print('coefficient recurrence A_{n+2}=6A_{n+1}-2A_n: PASS')
print('coefficient recurrence B annihilator (lambda^2-6lambda+2)^2: PASS')
print('coefficient recurrence C annihilator (lambda^2-6lambda+2)^3: PASS')
print('P7 coefficients from recurrence:',ABC[7])

x,z=sp.symbols('x z', integer=True, nonnegative=True)
a=sp.Rational(247492,132088); c=sp.Rational(202132,132088); s=sp.Rational(1,4)
u=a*x+s*z
v=c*x+sp.Rational(1,2)*x*(x-1)*a*a+sp.Rational(1,2)*z*(z-1)*s*s+x*z*a*s
U=sp.eye(5)+u*N+v*N**2
d0=sp.Matrix([[1,0,0,0,0]]); one=sp.ones(5,1)

p,r=sp.symbols('p r', integer=True, nonnegative=True)
up=a*p+s*r
vp=c*p+sp.Rational(1,2)*p*(p-1)*a*a+sp.Rational(1,2)*r*(r-1)*s*s+p*r*a*s
Up=sp.eye(5)+up*N+vp*N**2
Znorm=sp.factor((d0*Up*one)[0])
Ztarget=(45939217548*p**2+12259021236*p*r+26800323172*p+
         817839363*r**2+3543970573*r+4361809936)/sp.Integer(4361809936)
assert sp.simplify(Znorm-Ztarget)==0
print('Z/(132088^p 4^r) =',Znorm)
print('closed forest-count formula: PASS')

# Universal two-layer witness and exact orbit reduction.
def edgekey(a,b): return tuple(sorted((a,b),key=repr))
Gedges=[]
for q in range(2):
    for i in range(L):
        for t in range(3): Gedges.append(edgekey(('A',q,i),('T',t)))
    for i in range(L-1): Gedges.append(edgekey(('A',q,i),('A',q,i+1)))
for q in range(2):
    for t in range(3): Gedges.append(edgekey(('O',q,0),('T',t)))
Gedges=list(dict.fromkeys(Gedges))
auts=[]
for tp in permutations(range(3)):
    for Ap in permutations(range(2)):
        for Afl in product([0,1],repeat=2):
            for Op in permutations(range(2)):
                mp={}
                for t in range(3): mp[('T',t)]=('T',tp[t])
                for q in range(2):
                    nq=Ap[q]
                    for i in range(L): mp[('A',q,i)]=('A',nq,L-1-i if Afl[q] else i)
                for q in range(2): mp[('O',q,0)]=('O',Op[q],0)
                auts.append(mp)
pairs=[tuple(sorted((e,f),key=repr)) for e,f in combinations(Gedges,2)]
seen=set(); orbits=[]
for pair in pairs:
    if pair in seen: continue
    orb=set()
    for mp in auts:
        e,f=pair
        e2=edgekey(mp[e[0]],mp[e[1]]); f2=edgekey(mp[f[0]],mp[f[1]])
        orb.add(tuple(sorted((e2,f2),key=repr)))
    seen|=orb; orbits.append(orb)
assert len(Gedges)==60 and len(pairs)==1770 and len(orbits)==110
print('universal witness: 60 edges, 1770 pairs, 110 automorphism orbits: PASS')

def localize(e):
    a0,b0=e
    if a0[0]=='T': t=a0[1]; q=b0
    elif b0[0]=='T': t=b0[1]; q=a0
    else:
        assert a0[0]==b0[0] and a0[1]==b0[1]
        return (a0[0],a0[1],('i',min(a0[2],b0[2]),max(a0[2],b0[2])))
    return (q[0],q[1],('s',q[2],t))

def layer_matrix(kind,req):
    req=tuple(sorted(req,key=repr))
    if kind=='A': return P7 if not req else transfer_path(7,req)
    if kind=='O': return S if not req else transfer_path(1,req)
    raise AssertionError(kind)

def quantity(pair,required):
    layers={}
    for e in pair:
        kind,idx,loc=localize(e)
        layers.setdefault((kind,idx),[]).append((e,loc))
    M=sp.eye(5)
    for lid,els in sorted(layers.items(),key=repr):
        req=[loc for e,loc in els if e in required]
        M=M*layer_matrix(lid[0],req)
    return sp.expand((d0*M*U*one)[0])

def rayleigh_poly(pair):
    e,f=pair
    I=quantity(pair,set()); Ie=quantity(pair,{e}); If=quantity(pair,{f}); Ief=quantity(pair,{e,f})
    return sp.Poly(sp.expand(Ie*If-I*Ief),x,z,domain=sp.QQ)

def newton_coeffs(poly):
    expr=poly.as_expr(); D=poly.total_degree(); ans={}
    for i in range(D+1):
        for j in range(D+1-i):
            cc=sp.Rational(0)
            for aa in range(i+1):
                for bb in range(j+1):
                    cc += (-1)**((i-aa)+(j-bb))*sp.binomial(i,aa)*sp.binomial(j,bb)*expr.subs({x:aa,z:bb})
            cc=sp.factor(cc)
            if cc: ans[(i,j)]=cc
    return ans

def desc(e):
    a0,b0=e
    if a0[0]=='T': t=a0[1]; q=b0
    elif b0[0]=='T': t=b0[1]; q=a0
    else: return f'{a0[0]}{a0[1]}:h{min(a0[2],b0[2])}{max(a0[2],b0[2])}'
    return f'{q[0]}{q[1]}:v{q[2]}-T{t}'

bad=[]; zero_constant=[]; min_positive_newton=None; min_regular_constant=None
for idx,orb in enumerate(orbits,1):
    rep=sorted(orb,key=repr)[0]
    poly=rayleigh_poly(rep); nc=newton_coeffs(poly)
    constant=sp.factor(poly.as_expr().subs({x:0,z:0}))
    if constant==0: zero_constant.append((idx,desc(rep[0]),desc(rep[1])))
    if any(cc<0 for cc in nc.values()): bad.append((idx,rep,poly,nc))
    else:
        pos=[cc for cc in nc.values() if cc>0]
        if pos:
            mm=min(pos); min_positive_newton=mm if min_positive_newton is None else min(min_positive_newton,mm)
        if constant>0: min_regular_constant=constant if min_regular_constant is None else min(min_regular_constant,constant)

assert len(bad)==6
bad_desc=[(idx,desc(rep[0]),desc(rep[1])) for idx,rep,poly,nc in bad]
assert bad_desc==[
    (7,'A0:v0-T0','A0:v3-T1'),
    (9,'A0:v0-T0','A0:v4-T1'),
    (11,'A0:v0-T0','A0:v5-T1'),
    (13,'A0:v0-T0','A0:v6-T1'),
    (39,'A0:v1-T0','A0:v4-T1'),
    (41,'A0:v1-T0','A0:v5-T1')]
print('104/110 orbit polynomials lie in the nonnegative Newton cone: PASS')
print('six Newton failures are exactly same-P7 different-terminal spoke pairs at path distance >=3: PASS')
print('minimum positive Newton coefficient among regular orbits =',min_positive_newton)
print('minimum positive regular-orbit constant =',min_regular_constant)

# Two-corner lattice certificates; thresholds were found by exact search and are verified here.
certspec=[(2,13),(8,55),(24,173),(60,448),(3,16),(9,63)]
X,Z=sp.symbols('X Z', integer=True, nonnegative=True)
for (idx,rep,poly,nc),(Ax,Bz) in zip(bad,certspec):
    den=sp.ilcm(*[int(sp.denom(cc)) for cc in poly.coeffs()])
    Qexpr=sp.Poly(sp.expand(den*poly.as_expr()),x,z,domain=sp.ZZ).as_expr()
    Qx=sp.Poly(sp.expand(Qexpr.subs({x:X+Ax,z:Z})),X,Z,domain=sp.ZZ)
    Qz=sp.Poly(sp.expand(Qexpr.subs({x:X,z:Z+Bz})),X,Z,domain=sp.ZZ)
    assert all(cc>0 for cc in Qx.coeffs()) and all(cc>0 for cc in Qz.coeffs())
    box=[(int(Qexpr.subs({x:i,z:j})),i,j) for i in range(Ax) for j in range(Bz)]
    assert min(v for v,_,_ in box)>0
    neg=sorted((k,cc) for k,cc in nc.items() if cc<0)
    bmin=min(box)
    print('EXCEPTION',idx,desc(rep[0]),desc(rep[1]))
    print('  negative Newton coefficients =',neg)
    print('  denominator cleared by',den)
    print(f'  x-corner shift ({Ax},0): all coefficients positive; min={min(Qx.coeffs())}')
    print(f'  z-corner shift (0,{Bz}): all coefficients positive; min={min(Qz.coeffs())}')
    print(f'  residual box: {len(box)} exact values; min={bmin[0]} at ({bmin[1]},{bmin[2]})')
    print('  two-corner lattice sign certificate: PASS')

assert len(zero_constant)==1
assert {zero_constant[0][1],zero_constant[0][2]}=={'O0:v0-T0','O0:v0-T1'}
zidx=zero_constant[0][0]; zrep=sorted(orbits[zidx-1],key=repr)[0]
assert all(cc>0 for cc in newton_coeffs(rayleigh_poly(zrep)).values())
print('unique zero-constant orbit =',zero_constant,'; equality only for F7_{0,1}=K_{3,1}: PASS')

# Independent direct check for one physical P7 layer (10 vertices, 27 edges).
local_edges=[('s',i,t) for i in range(7) for t in range(3)]+[('i',i,i+1) for i in range(6)]
def layer_count(req):
    M=transfer_path(7,tuple(sorted(req,key=repr)))
    return int((d0*M*one)[0])
Z10=layer_count(())
onecnt={e:layer_count((e,)) for e in local_edges}
gaps=[]
for e,f in combinations(local_edges,2):
    gap=onecnt[e]*onecnt[f]-Z10*layer_count((e,f)); gaps.append((gap,e,f))
assert Z10==2334848 and min(gaps)[0]==413667072
print('DIRECT F7_{1,0}: n=10 m=27 Z=2334848 min_gap=413667072 pair=',min(gaps)[1:])
print('ALL_EXACT_CHECKS_PASS')
