# Independent exact check of a STRAT5 quartic SOS certificate (pure Python Fractions; no sympy, no solver).
# 1. Rebuild poly(z, x) from the stated formula with a dict-based polynomial class.
# 2. Every z-monomial of poly must have a record with positive scale.
# 3. scale * m^T (M/den) m must equal that z-monomial's ternary quartic in x, exactly.
# 4. M must be PSD (exact LDL with Fractions).
# What this does NOT check: that poly is the right functional (that is the derivation in RESULT.md).
import json, sys
from fractions import Fraction as F
NV=7  # z0..z3, x0..x2
def var(i):
    e=[0]*NV; e[i]=1; return {tuple(e):F(1)}
def const(c): return {tuple([0]*NV):F(c)}
def add(*ps):
    r={}
    for p in ps:
        for k,v in p.items():
            r[k]=r.get(k,0)+v
    return {k:v for k,v in r.items() if v!=0}
def mul(a,b):
    r={}
    for ka,va in a.items():
        for kb,vb in b.items():
            k=tuple(x+y for x,y in zip(ka,kb)); r[k]=r.get(k,0)+va*vb
    return {k:v for k,v in r.items() if v!=0}
def sc(c,p): c=F(c); return {k:c*v for k,v in p.items()} if c else {}
def mulm(*ps):
    r=const(1)
    for p in ps: r=mul(r,p)
    return r
def sm(ps):
    return add(*ps) if ps else {}
z=[var(i) for i in range(4)]; xi=[var(4+i) for i in range(3)]
U=[sm([sc((5-j) if i<j else -j, z[j-1]) for j in range(1,5)]) for i in range(5)]
t=sm([mul(u,u) for u in U]); q=sm([mulm(u,u,u,u) for u in U]); d=sm([mulm(u,u,u) for u in U])
p=sc(-1,mul(U[0],U[4])); delta=add(U[0],sc(-1,U[4]))
W=[sm([mul(add(U[4],sc(-1,U[j+1])),xi[j]) for j in range(3)])]+[mul(delta,xi[j]) for j in range(3)]
W+=[sm([mul(add(U[j+1],sc(-1,U[0])),xi[j]) for j in range(3)])]
zeta=sm([mul(w,w) for w in W])
cf=sm([mulm(U[i],U[i],W[i],W[i]) for i in range(5)])
ef=sm([mulm(U[i],U[i],W[i]) for i in range(5)])
ff=sm([mulm(U[i],W[i],W[i]) for i in range(5)])
hh=sm([mulm(W[i],W[i],W[i]) for i in range(5)])
b4=sm([mulm(W[i],W[i],W[i],W[i]) for i in range(5)])
v=add(U[0],U[4])
lu=sc(F(14,9),add(mul(q,zeta),mul(t,cf),sc(F(-1,5),mulm(t,t,zeta))))
lw=sc(F(14,9),add(mul(t,b4),mul(cf,zeta),sc(F(-1,5),mulm(t,zeta,zeta))))
qb=add(sc(F(2,9),add(mulm(q,zeta,zeta),mulm(t,t,b4),sc(2,mulm(t,cf,zeta)),sc(F(-2,5),mulm(t,t,zeta,zeta)))),sc(F(-4,3),mulm(t,cf,zeta)))
qb=add(qb,sc(F(10,3),add(mulm(ef,ef,zeta),mulm(t,ff,ff))),sc(2,mulm(d,ff,zeta)),sc(2,mulm(t,ef,hh)))
rb=add(sc(F(58,45),mulm(t,t,t,zeta,zeta)),sc(F(-40,9),mulm(t,t,t,b4)),sc(F(-299,72),mulm(t,t,cf,zeta)))
alpha=add(sc(140,mul(p,q)),sc(-28,mulm(p,t,t)),sc(-47,mul(q,t)),sc(13,mulm(t,t,t)),sc(24,mul(d,d)))
enum=add(mul(alpha,zeta),mul(add(sc(140,mul(p,t)),sc(-41,mul(t,t))),cf),sc(6,mulm(t,ef,ef)),sc(18,mulm(t,d,ff)))
path=sys.argv[1]; D=json.load(open(path)); r=F(D['r'])
s7=add(sc(7,t),sc(-5,mul(v,v)))
poly=add(mul(enum,zeta),sc(F(9,2)*r,add(mulm(t,add(sc(20,p),sc(-1,t)),lw),sc(-1,mulm(s7,lu,zeta)),sc(2,mul(t,qb)))))
poly=add(poly,sc(F(9,2)*r*r,add(sc(-1,mulm(t,s7,lw)),sc(2,rb))))
coeff={}
for k,c in poly.items():
    zz,xx=k[:4],k[4:]; assert sum(zz)==10 and sum(xx)==4
    coeff.setdefault(zz,{})[xx]=c
mons=[tuple(m) for m in D['monomials']]
def psd(M):
    M=[row[:] for row in M]
    while M:
        piv=M[0][0]
        if piv<0: return False
        if piv==0:
            if any(M[0][j]!=0 for j in range(1,len(M))): return False
            M=[row[1:] for row in M[1:]]; continue
        M=[[M[i][j]-M[i][0]*M[0][j]/piv for j in range(1,len(M))] for i in range(1,len(M))]
    return True
recs={tuple(rr['monomial']):rr for rr in D['records']}
missing=[zz for zz in coeff if zz not in recs]
bad_match=0; bad_psd=0; bad_scale=0
for zz,ct in coeff.items():
    if zz not in recs: continue
    rr=recs[zz]; scale=F(rr['scale']); den=rr['denominator']
    mat=rr['matrix']; mat=json.loads(mat) if isinstance(mat,str) else mat
    M=[[F(x,den) for x in row] for row in mat]
    if scale<=0: bad_scale+=1
    if not psd(M): bad_psd+=1
    got={}
    for i in range(6):
        for j in range(6):
            m=tuple(a+b for a,b in zip(mons[i],mons[j])); got[m]=got.get(m,0)+M[i][j]*scale
    got={k:v for k,v in got.items() if v!=0}
    if got!=ct: bad_match+=1
print(path,'r',r,'z-monomials in poly',len(coeff),'records',len(recs),'missing',len(missing),
      'bad match',bad_match,'not PSD',bad_psd,'bad scale',bad_scale,'failed listed',len(D['failed']))
print('CERTIFICATE CHECKS' if not (missing or bad_match or bad_psd or bad_scale) else 'CERTIFICATE FAILS')
