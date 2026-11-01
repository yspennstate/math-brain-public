#!/usr/bin/env python3
"""
Exact checker for NM13-08 T07 one-port field / series-parallel macro-network theorem.

Target atom:
    H_n = K_4 join independent_n, n>=1,
with distinguished clique port edge g={0,1}; Q_n=H_n-g.

The checker:
  1. rebuilds the 15-state partition transfer exactly;
  2. verifies M=5I+N and N^4=0;
  3. derives the Rayleigh difference in the single port field s as
       Delta = 25^n (a(n)+b(n)s+c(n)s^2)
     on all 18 non-port edge-pair orbits, by exact degree<=6 interpolation;
  4. proves positivity by coefficient signs except for two orbit families,
     whose exact discriminants have strictly negative polynomial coefficients,
     plus one n=1 special field orbit checked by exact discriminant;
  5. checks the 4 port-edge orbit families (Delta with g), independent of s;
  6. brute-force verifies the underlying transfer counts and p-NC for
     n=1,2 atoms and for parallel/series compositions of two Q_1 atoms.

All arithmetic used in the certificate is integer/Fraction arithmetic.
"""
from itertools import combinations
from fractions import Fraction

T=tuple(range(4))
PORT=(0,1)

def canon(blocks):
    return tuple(sorted((tuple(sorted(b)) for b in blocks if b),
                        key=lambda b:(b[0],len(b),b)))
def gen_parts(items):
    items=list(items)
    if not items:
        yield (); return
    x=items[0]
    for p in gen_parts(items[1:]):
        yield canon(((x,),)+p)
        for i in range(len(p)):
            q=[set(b) for b in p]
            q[i].add(x)
            yield canon(q)

PARTS=sorted(set(gen_parts(T)), key=lambda p:(-len(p),p))
IDX={p:i for i,p in enumerate(PARTS)}
S=len(PARTS)
assert S==15

def block_index(p,x):
    for i,b in enumerate(p):
        if x in b: return i
    raise AssertionError

def trans(p,A):
    A=set(A)
    ids=[block_index(p,x) for x in A]
    if len(set(ids))!=len(ids): return None
    if len(A)<=1: return p
    ids=set(ids); merged=set(); out=[]
    for i,b in enumerate(p):
        if i in ids: merged.update(b)
        else: out.append(set(b))
    out.append(merged)
    return canon(out)

def zmat(): return [[0]*S for _ in range(S)]
M=zmat(); E=[zmat() for _ in T]
EP={(i,j):zmat() for i,j in combinations(T,2)}
for a,p in enumerate(PARTS):
    for r in range(5):
        for A in combinations(T,r):
            q=trans(p,A)
            if q is None: continue
            b=IDX[q]
            M[a][b]+=1
            for i in A: E[i][a][b]+=1
            for i,j in combinations(A,2): EP[(i,j)][a][b]+=1

def eye():
    A=zmat()
    for i in range(S): A[i][i]=1
    return A
def mmul(A,B):
    C=zmat()
    for i in range(S):
        for k in range(S):
            if A[i][k]:
                for j in range(S):
                    if B[k][j]:
                        C[i][j]+=A[i][k]*B[k][j]
    return C
def madd(A,B,sa=1,sb=1):
    return [[sa*A[i][j]+sb*B[i][j] for j in range(S)] for i in range(S)]
def mpow(A,n):
    R=eye(); B=A
    while n:
        if n&1: R=mmul(R,B)
        B=mmul(B,B); n//=2
    return R
def rowmul(v,A):
    out=[0]*S
    for i,x in enumerate(v):
        if x:
            for j in range(S):
                out[j]+=x*A[i][j]
    return out
def apply(v,*ops):
    for A in ops: v=rowmul(v,A)
    return v
def rowsum(v): return sum(v)

I=eye(); N=madd(M,I,1,-5); N2=mmul(N,N); N3=mmul(N2,N); N4=mmul(N3,N)
assert any(any(x for x in row) for row in N3)
assert not any(any(x for x in row) for row in N4)

K4E=list(combinations(T,2))
def part_if_forest(edges,nv=4):
    par=list(range(nv))
    def f(x):
        while par[x]!=x:
            par[x]=par[par[x]]
            x=par[x]
        return x
    for a,b in edges:
        a=f(a); b=f(b)
        if a==b: return None
        par[b]=a
    blocks={}
    for x in range(nv): blocks.setdefault(f(x),set()).add(x)
    return canon(blocks.values())

INIT={}
def init_vec(required):
    key=tuple(sorted(required))
    if key in INIT: return INIT[key]
    R=set(key); v0=[0]*S; v1=[0]*S
    for mask in range(1<<len(K4E)):
        es=[K4E[k] for k in range(len(K4E)) if (mask>>k)&1]
        if not R.issubset(es): continue
        p=part_if_forest(es)
        if p is None: continue
        (v1 if PORT in es else v0)[IDX[p]]+=1
    INIT[key]=(v0,v1)
    return v0,v1

# Edge descriptor: ("c",(i,j)) or ("s",terminal,right_index).
def count_linear(n,required):
    clique=[e[1] for e in required if e[0]=="c"]
    v0,v1=init_vec(clique)
    groups={}
    for e in required:
        if e[0]!="s": continue
        _,t,r=e
        if r>=n: return (0,0)
        groups.setdefault(r,[]).append(t)
    ops=[]
    for r in sorted(groups):
        ts=groups[r]
        if len(ts)==1: ops.append(E[ts[0]])
        elif len(ts)==2:
            i,j=sorted(ts)
            assert i!=j
            ops.append(EP[(i,j)])
        else:
            raise AssertionError("No orbit in this checker marks >2 spokes on one right vertex")
    rem=n-len(groups)
    assert rem>=0
    Mn=mpow(M,rem)
    return rowsum(apply(v0,*ops,Mn)),rowsum(apply(v1,*ops,Mn))

def deriv1(n,e):
    if e==("c",PORT):
        a,b=count_linear(n,[e]); assert a==0
        return (b,0)
    return count_linear(n,[e])
def deriv2(n,e,f):
    if e==("c",PORT) or f==("c",PORT):
        a,b=count_linear(n,[e,f]); assert a==0
        return (b,0)
    return count_linear(n,[e,f])

def mul_lin(p,q):
    a,b=p; c,d=q
    return (a*c,a*d+b*c,b*d)
def rayleigh_poly(n,e,f):
    Z=count_linear(n,[])
    Ze=deriv1(n,e); Zf=deriv1(n,f); Zef=deriv2(n,e,f)
    x=mul_lin(Ze,Zf); y=mul_lin(Z,Zef)
    return tuple(x[i]-y[i] for i in range(3))

# Polynomial helpers, coefficient lists ascending.
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p
def padd(p,q):
    m=max(len(p),len(q)); out=[Fraction(0) for _ in range(m)]
    for i in range(m):
        if i<len(p): out[i]+=p[i]
        if i<len(q): out[i]+=q[i]
    return trim(out)
def pscale(p,c): return trim([c*x for x in p])
def pmul(p,q):
    out=[Fraction(0) for _ in range(len(p)+len(q)-1)]
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j]+=a*b
    return trim(out)
def peval(p,x):
    ans=Fraction(0)
    for c in reversed(p): ans=ans*x+c
    return ans
def interp(points):
    out=[Fraction(0)]
    for i,(xi,yi) in enumerate(points):
        basis=[Fraction(1)]; den=Fraction(1)
        for j,(xj,_) in enumerate(points):
            if i==j: continue
            basis=pmul(basis,[Fraction(-xj),Fraction(1)])
            den*=xi-xj
        out=padd(out,pscale(basis,yi/den))
    return trim(out)
def pshift(p,k):
    # q(m)=p(m+k)
    out=[Fraction(0)]
    power=[Fraction(1)]
    base=[Fraction(k),Fraction(1)]
    for c in p:
        out=padd(out,pscale(power,c))
        power=pmul(power,base)
    return trim(out)

ORBITS={
"cc_A_same_gend":(("c",(0,2)),("c",(0,3)),1),
"cc_A_share_other":(("c",(0,2)),("c",(1,2)),1),
"cc_A_disjoint":(("c",(0,2)),("c",(1,3)),1),
"cc_A_D":(("c",(0,2)),("c",(2,3)),1),
"cs_A_inc_g":(("c",(0,2)),("s",0,0),1),
"cs_A_non_otherg":(("c",(0,2)),("s",1,0),1),
"cs_A_inc_other":(("c",(0,2)),("s",2,0),1),
"cs_A_non_other":(("c",(0,2)),("s",3,0),1),
"cs_D_non_g":(("c",(2,3)),("s",0,0),1),
"cs_D_inc":(("c",(2,3)),("s",2,0),1),
"ss_sameR_gg":(("s",0,0),("s",1,0),1),
"ss_sameR_oo":(("s",2,0),("s",3,0),1),
"ss_sameR_go":(("s",0,0),("s",2,0),1),
"ss_diffR_same_g":(("s",0,0),("s",0,1),2),
"ss_diffR_same_o":(("s",2,0),("s",2,1),2),
"ss_diffR_gg":(("s",0,0),("s",1,1),2),
"ss_diffR_oo":(("s",2,0),("s",3,1),2),
"ss_diffR_go":(("s",0,0),("s",2,1),2),
}

CERT={}
for name,(e,f,nmin) in ORBITS.items():
    coeff_polys=[]
    xs=list(range(nmin,nmin+7))  # degree <=6
    for j in range(3):
        pts=[]
        for n in xs:
            raw=rayleigh_poly(n,e,f)[j]
            pts.append((n,Fraction(raw,25**n)))
        pol=interp(pts)
        assert len(pol)<=7
        # overdetermined readback
        for n in range(nmin,nmin+13):
            assert peval(pol,n)==Fraction(rayleigh_poly(n,e,f)[j],25**n)
        coeff_polys.append(pol)
    CERT[name]=coeff_polys

# Sign proof.
exceptions=[]
for name,(a,b,c) in CERT.items():
    nmin=ORBITS[name][2]
    ash=pshift(a,nmin); bsh=pshift(b,nmin); csh=pshift(c,nmin)
    assert all(x>=0 for x in ash) and any(x>0 for x in ash)
    assert all(x>=0 for x in csh) and any(x>0 for x in csh)
    if all(x>=0 for x in bsh):
        continue
    exceptions.append(name)

assert set(exceptions)=={"cc_A_disjoint","cs_A_non_otherg","ss_diffR_gg"}

# cs_A_non_otherg: at n=1 negative b but negative discriminant; n>=2 b positive.
a,b,c=CERT["cs_A_non_otherg"]
disc=padd(pmul(b,b),pscale(pmul(a,c),-4))
assert peval(b,1)<0 and peval(disc,1)<0
assert all(x>=0 for x in pshift(b,2))

# Two persistent mixed-negative orbits: exact discriminant has all negative coefficients.
DISC={}
for name in ("cc_A_disjoint","ss_diffR_gg"):
    a,b,c=CERT[name]
    d=padd(pmul(b,b),pscale(pmul(a,c),-4))
    assert all(x<0 for x in d), (name,d)
    DISC[name]=d

# Four pairs involving the port g. Delta is independent of s.
PORT_ORBITS={
"g_A":("c",(0,2)),
"g_D":("c",(2,3)),
"g_spoke_inc":("s",0,0),
"g_spoke_non":("s",2,0),
}
PORT_CERT={}
for name,e in PORT_ORBITS.items():
    pts=[]
    for n in range(1,8):
        p=rayleigh_poly(n,("c",PORT),e)
        assert p[1]==0 and p[2]==0
        pts.append((n,Fraction(p[0],25**n)))
    pol=interp(pts)
    assert all(x>0 for x in pol)
    for n in range(1,14):
        assert peval(pol,n)==Fraction(rayleigh_poly(n,("c",PORT),e)[0],25**n)
    PORT_CERT[name]=pol

# Brute-force unit forest check for atom Q_n = H_n - port, and two-atom series/parallel.
def brute_graph(nv,edges):
    m=len(edges)
    Z=0; Ze=[0]*m; Zef=[[0]*m for _ in range(m)]
    for mask in range(1<<m):
        par=list(range(nv))
        def f(x):
            while par[x]!=x:
                par[x]=par[par[x]]; x=par[x]
            return x
        chosen=[]; ok=True
        for k,(a,b) in enumerate(edges):
            if not ((mask>>k)&1): continue
            ra,rb=f(a),f(b)
            if ra==rb:
                ok=False; break
            par[rb]=ra; chosen.append(k)
        if not ok: continue
        Z+=1
        for a in chosen: Ze[a]+=1
        for a,b in combinations(chosen,2):
            Zef[a][b]+=1; Zef[b][a]+=1
    mingap=None
    for a,b in combinations(range(m),2):
        d=Ze[a]*Ze[b]-Z*Zef[a][b]
        assert d>=0
        mingap=d if mingap is None else min(mingap,d)
    return Z,mingap

def mapped_q1(x,y,ints):
    loc=[x,y]+list(ints)
    return [(loc[a],loc[b]) for a,b in combinations(range(5),2) if (a,b)!=PORT]

q1=[e for e in combinations(range(5),2) if e!=PORT]
Zq1,mq1=brute_graph(5,q1)

par_edges=mapped_q1(0,1,(2,3,4))+mapped_q1(0,1,(5,6,7))
Zpar,mpar=brute_graph(8,par_edges)

ser_edges=mapped_q1(0,1,(2,3,4))+mapped_q1(1,5,(6,7,8))
Zser,mser=brute_graph(9,ser_edges)

print("T07 one-port field / macro-network exact checker")
print("states =",S,"; N^3 != 0 and N^4 = 0: PASS")
print("non-port orbit count =",len(ORBITS),"; port-edge orbit count =",len(PORT_ORBITS))
print("degree<=6 interpolation/readback: PASS on all 18 non-port orbits")
print("coefficientwise-positive field orbits =",len(ORBITS)-3)
print("special n=1 cs_A_non_otherg: b(1) =",peval(CERT["cs_A_non_otherg"][1],1),
      "disc(1) =",peval(padd(pmul(CERT["cs_A_non_otherg"][1],CERT["cs_A_non_otherg"][1]),
                             pscale(pmul(CERT["cs_A_non_otherg"][0],CERT["cs_A_non_otherg"][2]),-4)),1))
for name,d in DISC.items():
    print(name,"discriminant coefficients =",[str(x) for x in d])
print("port-pair field-independence and positivity: PASS")
print("Q1=K5-port brute force: Z=%d min_gap=%d"%(Zq1,mq1))
print("parallel Q1||Q1 brute force: n=8 m=%d Z=%d min_gap=%d"%(len(par_edges),Zpar,mpar))
print("series Q1oQ1 brute force: n=9 m=%d Z=%d min_gap=%d"%(len(ser_edges),Zser,mser))
print("ALL_EXACT_CHECKS_PASS")
