from itertools import permutations, product
import sympy as sp

N=5
x,L=sp.symbols('x L')
E=[(i,j) for i in range(N) for j in range(i+1,N)]
EI={e:k for k,e in enumerate(E)}
PERMS=list(permutations(range(N)))
STATES=list(product((-1,1), repeat=N))
SI={s:i for i,s in enumerate(STATES)}


def pmask(m,p):
    out=0
    for k,(a,b) in enumerate(E):
        if (m>>k)&1:
            u,v=sorted((p[a],p[b]))
            out |= 1<<EI[(u,v)]
    return out


def pebit(k,p):
    a,b=E[k]
    u,v=sorted((p[a],p[b]))
    return EI[(u,v)]


def canon(m):
    return min(pmask(m,p) for p in PERMS)


def auts(m):
    return [p for p in PERMS if pmask(m,p)==m]


def marked_stabilizer_size(m,k):
    a,b=E[k]
    pair={a,b}
    return sum(1 for p in auts(m) if {p[a],p[b]}==pair)


def pst(s,p):
    t=[0]*N
    for i in range(N):
        t[p[i]]=s[i]
    return tuple(t)


def neg(s):
    return tuple(-a for a in s)


def orbit_pairs(m):
    A=auts(m)
    seen=set(); ans=[]
    for s in STATES:
        if s in seen: continue
        O={pst(s,p) for p in A}
        M={neg(t) for t in O}
        seen |= O|M
        if O==M: continue
        ans.append((O,M) if min(O)<=min(M) else (M,O))
    return ans


def tanh_mult(h):
    if h==0: return sp.Integer(0)
    sg=1 if h>0 else -1
    a=abs(h)
    if a==1: t=x
    elif a==2: t=2*x/(1+x**2)
    elif a==3: t=(3*x+x**3)/(1+3*x**2)
    elif a==4: t=4*x*(1+x**2)/(1+6*x**2+x**4)
    else: raise ValueError(a)
    return sg*t


def edges(m):
    return [e for k,e in enumerate(E) if (m>>k)&1]


def Pmat(m):
    nbr={i:[] for i in range(N)}
    for a,b in edges(m):
        nbr[a].append(b); nbr[b].append(a)
    P=sp.zeros(2**N)
    for ii,s in enumerate(STATES):
        for v in range(N):
            h=sum(s[w] for w in nbr[v])
            pp=sp.cancel((1+tanh_mult(h))/2)
            t=list(s); t[v]=1
            P[ii,SI[tuple(t)]] += pp/N
            t=list(s); t[v]=-1
            P[ii,SI[tuple(t)]] += (1-pp)/N
    return P


def qpoly(m):
    P=Pmat(m)
    pairs=orbit_pairs(m)
    reps=[min(O) for O,M in pairs]
    Q=sp.zeros(len(pairs))
    for i,r in enumerate(reps):
        for j,(O,M) in enumerate(pairs):
            Q[i,j]=sp.cancel(sum(P[SI[r],SI[t]] for t in O)-sum(P[SI[r],SI[t]] for t in M))
    num=sp.together(Q.charpoly(L).as_expr()).as_numer_denom()[0]
    return sp.factor(sp.Poly(num,L,domain=sp.QQ[x]).primitive()[1].as_expr())


def factors(q):
    return [sp.factor(f) for f,mul in sp.factor_list(q,L)[1] for _ in range(mul)]


def monic(f):
    return sp.Poly(f,L,domain=sp.QQ.frac_field(x)).monic()


def top_interval(f,xv,eps=sp.Rational(1,10**12)):
    p=sp.Poly(sp.cancel(f.subs(x,xv)),L,domain=sp.QQ)
    ints=p.intervals(eps=eps)
    assert sum(mult for _,mult in ints)==p.degree()
    (a,b),_=ints[-1]
    return sp.Rational(a),sp.Rational(b)


def compare_top(f,g,xv):
    eps=sp.Rational(1,10**6)
    for _ in range(10):
        a,b=top_interval(f,xv,eps)
        c,d=top_interval(g,xv,eps)
        if a>d: return 1
        if c>b: return -1
        if a==b==c==d: return 0
        eps/=100
    raise AssertionError(('root separation failed',xv,a,b,c,d))


def resultant_roots_01(f,g):
    if monic(f)==monic(g): return []
    r=sp.Poly(sp.resultant(f,g,L),x,domain=sp.QQ)
    assert not r.is_zero
    for val in (0,1):
        d=sp.Poly(x-val,x,domain=sp.QQ)
        while r.degree()>0 and r.eval(val)==0:
            r=r.exquo(d)
    if r.degree()<=0: return []
    ans=[]
    for (a,b),mult in r.intervals(eps=sp.Rational(1,10**10)):
        a,b=sp.Rational(a),sp.Rational(b)
        if b<=0 or a>=1: continue
        if a<=0 or b>=1:
            a,b=map(sp.Rational,r.refine_root(a,b,eps=sp.Rational(1,10**20)))
        if 0<a and b<1:
            ans.append((a,b,mult))
    return ans


def certify_ge_01(f,g):
    if monic(f)==monic(g):
        return True,[],[sp.Rational(1,2)],[0]
    roots=resultant_roots_01(f,g)
    samples=[]; left=sp.Rational(0)
    for a,b,_ in roots:
        samples.append((left+a)/2); left=b
    samples.append((left+1)/2)
    signs=[compare_top(f,g,s) for s in samples]
    return min(signs)>=0,roots,samples,signs

# Three marked edge additions with trivial marked stabilizer.
TR=[(3,5,21),(21,8,58),(28,5,58)]
for s,k,t in TR:
    assert marked_stabilizer_size(s,k)==1
    assert canon(s|(1<<k))==t
print('marked_trivial_transitions',TR)

Q={m:qpoly(m) for m in (3,21,28,58)}
TOP={}
for m,q in Q.items():
    fs=factors(q)
    best=fs[0]
    for f in fs[1:]:
        if compare_top(f,best,sp.Rational(1,2))>0:
            best=f
    TOP[m]=best
    for f in fs:
        if monic(f)==monic(best): continue
        ok,roots,samples,signs=certify_ge_01(best,f)
        assert ok
    print('top_factor',m,sp.factor(best))

FA=25*(1+x**2)*L**2-40*(1+x**2)*L+16+14*x**2
FB=25*(1+x**2)*L**2-(40*(1+x**2)+5*x)*L+16+15*x**2+4*x
FC=25*(1+x**2)**2*L**2-40*(1+x**2)**2*L+16+29*x**2+15*x**4
assert monic(TOP[3])==monic(FA)
assert monic(TOP[28])==monic(FA)
assert monic(TOP[21])==monic(FB)
assert monic(TOP[58])==monic(FC)

for s,_,t in TR:
    ok,roots,samples,signs=certify_ge_01(TOP[t],TOP[s])
    assert ok
    print('edge_global',s,t,'PASS','interior_resultant_roots',len(roots),'signs',signs)

# Exact discriminants and radical-inequality reductions used in the on-page proof.
assert sp.factor(sp.discriminant(FA,L))==200*x**2*(1+x**2)
assert sp.factor(sp.discriminant(FB,L))==25*x**2*(4*x**2+5)
assert sp.factor(sp.discriminant(FC,L))==100*x**2*(1+x**2)**2*(x**2+3)

# A<B proof reduces after one legitimate squaring to 1-x^2>=0.
# B<C proof likewise reduces to 1-x^2>=0.
# The exact identities below record those reductions.
assert sp.expand(8*(1+x**2)+1-(4*x**2+5)) == 4*(1+x**2)
assert sp.expand(4*(x**2+3)+1-(4*x**2+5)) == 8

# Low-temperature endpoint ratios of target/source gaps.
A=sp.Rational(4,5)+sp.sqrt(2)*x/(5*sp.sqrt(1+x**2))
B=sp.Rational(4,5)+x*(1+sp.sqrt(4*x**2+5))/(10*(1+x**2))
C=sp.Rational(4,5)+x*sp.sqrt(x**2+3)/(5*(1+x**2))
assert sp.simplify(sp.limit((1-B)/(1-A),x,1,dir='-')-sp.Rational(2,3))==0
assert sp.simplify(sp.limit((1-C)/(1-B),x,1,dir='-')-sp.Rational(3,4))==0
assert sp.simplify(sp.limit((1-C)/(1-A),x,1,dir='-')-sp.Rational(1,2))==0
print('low_temp_gap_ratios','3->21',sp.Rational(2,3),'21->58',sp.Rational(3,4),'28->58',sp.Rational(1,2))
print('ALL_EXACT_CHECKS_PASS')
