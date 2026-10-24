"""Exact X064 certificate: rational cut bookkeeping and spectra; no optimization."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

N=6
PAIRS=list(combinations(range(N),2)); TRIPLES=list(combinations(range(N),3))
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def tr(A): return sum(A[i][i] for i in range(len(A)))
def transpose(A): return [list(c) for c in zip(*A)]
def mm(A,B): return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def add(A,B): return [[a+b for a,b in zip(r,s)] for r,s in zip(A,B)]
def scale(A,c): return [[c*a for a in r] for r in A]
def det(A):
    if not A: return F(1)
    return sum((-1)**j*A[0][j]*det([r[:j]+r[j+1:] for r in A[1:]]) for j in range(len(A)))
def charpoly(A):
    n=len(A); B=eye(n); cs=[F(1)]
    for k in range(1,n+1):
        AB=mm(A,B); c=-tr(AB)/k; cs.append(c); B=add(AB,scale(eye(n),c))
    assert all(v==0 for row in B for v in row)
    return cs

def polyprod(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def house(v):
    d=sum(x*x for x in v)
    return [[F(i==j)-F(2*v[i]*v[j],d) for j in range(N)] for i in range(N)]
def cols(Q,ii): return [[r[i] for i in ii] for r in Q]
def law(U): return {J:det([U[i] for i in J])**2 for J in PAIRS}
def aggregate(U,V):
    return {M:sum(det([U[i]+[V[i][j]] for i in M])**2 for j in range(len(V[0]))) for M in TRIPLES}
def effects(U,V):
    out={}
    for M in TRIPLES:
        row=[det([U[i]+[V[i][j]] for i in M]) for j in range(len(V[0]))]
        out[M]=[[a*b for b in row] for a in row]
    return out

Q=eye(N)
for v in [(1,2,3,4,5,6),(2,-1,3,-2,1,4),(3,1,-2,4,2,-1)]: Q=mm(Q,house(v))
assert mm(transpose(Q),Q)==eye(N)
U=cols(Q,[2,3]); V=cols(Q,[0,1,4,5]); W=cols(Q,[0,1]); Z=cols(Q,[4,5])
h=law(U); a=law(W); c=law(Z); g=aggregate(U,W)
eff=effects(U,V)
assert sum(h.values())==sum(a.values())==sum(c.values())==1
assert sum(g.values())==2
checks=0; strengthened=0; spectra=[]; sharp=[]; distinct=set()
for e in range(N):
    allowed=[M for M in TRIPLES if e not in M]
    ue=sum(x*x for x in U[e]); ae=sum(x*x for x in W[e]); ce=sum(x*x for x in Z[e]); q=1-ue
    assert q>0 and q==ae+ce
    # g_e is P_(U perp)e/sqrt(q), so its projector is rational.
    gg=[[x*y/q for y in V[e]] for x in V[e]]
    PR=add(eye(4),scale(gg,-1))
    Ball=[[F(0)]*4 for _ in range(4)]
    for M in allowed: Ball=add(Ball,eff[M])
    assert Ball==scale(PR,q)
    for mask in range(1<<10):
        FF=[M for i,M in enumerate(allowed) if mask>>i&1]
        distinct.add(tuple(FF))
        degrees={J:sum(set(J)<=set(M) for M in FF) for J in PAIRS}
        S=sum(h[J]*max(degrees[J]-2,0) for J in PAIRS)
        C=sum(h[J]*min(degrees[J],2) for J in PAIRS)
        remaining=[M for M in allowed if M not in FF]
        shadow={J for J in PAIRS if any(set(J)<=set(M) for M in remaining)}
        assert S==q-sum(h[J] for J in shadow)
        gap=C-sum(g[M] for M in FF)
        assert gap>=ae*S/q>=0
        # The complementary spectral gap has the same sign and value at Z.
        CF=[M for M in TRIPLES if M not in FF]
        Ccomp=sum(h[J]*min(4-degrees[J],2) for J in PAIRS)
        gz=aggregate(U,Z) if mask==0 else gz
        assert Ccomp-sum(gz[M] for M in CF)==gap
        checks+=1
        if S>0: strengthened+=1
    assert 2*q-sum(g[M] for M in allowed)==ae
    sharp.append({'omitted_site':e,'full_five_site_cut_gap':str(ae),'strengthened_rhs':str(ae)})
    G=[[F(i==j)-U[e][i]*U[e][j] for j in range(2)] for i in range(2)]
    assert det(G)==q
    Gi=[[G[1][1]/q,-G[0][1]/q],[-G[1][0]/q,G[0][0]/q]]
    for R in combinations([i for i in range(N) if i!=e],3):
        FF=[M for M in allowed if len(set(M)&set(R))>=2]
        assert len(FF)==7
        B=[[F(0)]*4 for _ in range(4)]
        for M in FF: B=add(B,eff[M])
        C=mm(transpose([U[i] for i in R]),[U[i] for i in R])
        t=tr(mm(Gi,C)); d=det(C)/q
        expect=polyprod(polyprod([1,0],[1,-q*t,q*q*d]),[1,-q*(t-d)])
        assert charpoly(B)==expect
        S=sum(h[J] for J in PAIRS if set(J)<=set(R))
        assert S==q*d
        # The general operator lower bound is PSD: all principal minors.
        A=add(B,scale(PR,-S))
        for k in range(1,5):
            for I in combinations(range(4),k): assert det([[A[i][j] for j in I] for i in I])>=0
        spectra.append({'e':e,'R':R,'q':str(q),'angle_trace':str(t),'angle_product':str(d),
                        'characteristic_polynomial':list(map(str,expect))})

out={'status':'PASS','five_site_cut_checks_with_multiplicity':checks,
     'distinct_omitted_coordinate_cuts':len(distinct),'strictly_positive_strengthened_rhs_checks':strengthened,
     'localized_triangle_spectral_checks':len(spectra),'sharp_cases':sharp,'spectral_certificates':spectra,
     'scope':'Exact real rational self-checks supplement the arbitrary-complex analytic proof; no universal cut or diamond claim.'}
Path(__file__).with_name('verified_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['spectral_certificates','sharp_cases']}))
