"""A085 independent exact audit. No author code imports; fixed domains only."""
from fractions import Fraction as F
from pathlib import Path
from math import lcm, prod
import json, time, hashlib

ROOT = Path(__file__).resolve().parents[1]
start = time.perf_counter()
checks = 0
def ck(test):
    global checks
    checks += 1
    assert test, checks
    assert time.perf_counter()-start < 55

def log_sign(terms):
    """Sign of sum c log2(x), via integer powers; never evaluates log."""
    den = lcm(*(c.denominator for c, x in terms))
    ratio = F(1)
    for c, x in terms:
        assert x > 0
        ratio *= x ** int(c*den)
    return (ratio > 1)-(ratio < 1)

def delta(a,t,b,z):
    return [(a,b/z),(t-a,(t-b)/(t-z))]

# Source statement is reviewed unchanged, and proof text separately.
source = Path(r'agents\A097\runs\20261023T143952Z-fleet03-A097-cross-route-transfer')
claims = json.loads((source/'CLAIMS.json').read_text(encoding='utf-8'))
claim = claims[0]
ck(hashlib.sha256(claim['exact_statement'].encode()).hexdigest() == claim['statement_sha256'])
receipts = []
for name in ['PROOF.md','CLAIMS.json','REPORT.md']:
    data=(source/name).read_bytes()
    receipts.append({'path':str(source/name),'sha256':hashlib.sha256(data).hexdigest()})
(ROOT/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')

# Full rational profile grid. Trial points stay interior; endpoints audited analytically.
profiles=trials=0
for T in range(2,9):
    t=F(T,8)
    for A in range(1,T):
        a=F(A,8)
        for L in range(2,T):
            ell=F(L,8)
            for B in range(1,L):
                b=F(B,8); zstar=max(a,ell)
                profiles+=1
                ck(0<a<t and 0<b<ell<t)
                # Independent differentiation algebra (the missing factor t).
                for Z in range(L,T):
                    z=F(Z,8); trials+=1
                    ck(-a/z+(t-a)/(t-z)==t*(z-a)/(z*(t-z)))
                    ck(log_sign(delta(a,t,b,z)+[(-c,x) for c,x in delta(a,t,b,zstar)])>=0)
                    ck((z==zstar) == (log_sign(delta(a,t,b,z)+[(-c,x) for c,x in delta(a,t,b,zstar)])==0))
                # Include asymmetric ghost profiles: their zero true mass must stay in normalization.
                p=[1-t,a/3,2*a/3,(t-a)/2,(t-a)/2,F(0)]
                q=[1-t,b/4,3*b/4,(t-b)/5,3*(t-b)/5,(t-b)/5]
                qp=[q[0],q[1]*zstar/b,q[2]*zstar/b,
                    q[3]*(t-zstar)/(t-b),q[4]*(t-zstar)/(t-b),q[5]*(t-zstar)/(t-b)]
                ck(sum(p)==sum(q)==sum(qp)==1)
                ck(qp[-1]>0)
                full=[(p[i],q[i]/qp[i]) for i in range(1,6)]
                ck(log_sign(full+[(-c,x) for c,x in delta(a,t,b,zstar)])==0)

def walsh(table):
    N=len(table)
    return [F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(table)),N) for s in range(N)]

# Actual dimension-minimal seed for an interior calibrated two-cell class.
p=[x*x for x in walsh([-1,1,1,1])]
ck(p==[F(1,4)]*4)
small=0
for n in [0,1]:
    for bits in range(1<<(1<<n)):
        law=[x*x for x in walsh([1 if bits>>x&1 else -1 for x in range(1<<n)])]
        for mask in range(1<<(len(law)-1)):
            a=sum((law[i] for i in range(1,len(law)) if mask>>(i-1)&1),F(0))
            ck(not (0<a<1-law[0]));small+=1

# Both physical children of A097's actual three-bit seed.
g=[-1 if x in [0,7] else 1 for x in range(8)]
ck([x*x for x in walsh(g)]==[F(1,4),0,0,F(1,4),0,F(1,4),F(1,4),0])
for sign in [0,1]:
    child=[g[(x<<1)|sign] for x in range(4)]
    ck([x*x for x in walsh(child)]==p)

# Algebraic sign boundary: Delta(b)=1/4 log2(432 b(3/4-b)^2/25).
a=F(1,4); t=F(3,4); ell=F(1,3)
def poly(b): return 432*b*(t-b)**2-25
ck(poly(F(1,8))<0<poly(F(1,4)))
ck(log_sign(delta(a,t,F(1,4),ell))==1)
ck(log_sign(delta(a,t,F(1,8),ell))==-1)
for k in range(1,49):
    b=F(k,144)
    ck(poly(b)==432*(b-F(1,3))*(b*b-F(7,6)*b+F(25,144)))

# Isolate bcrit dyadically by exact monotonic polynomial bisection.
lo=F(0); hi=F(1,4); brackets=[]
for m in range(3,161):
    mid=(lo+hi)/2
    ck(poly(mid)!=0) # Irrationality supplies all-m nonvanishing in the proof.
    if poly(mid)<0: lo=mid
    else: hi=mid
    ck(hi-lo==F(1,2**m))
    ck(poly(lo)<0<poly(hi))
    if m>=4:
        ck(0<lo<hi<ell)
        ck(log_sign(delta(a,t,lo,ell))==-1)
        ck(log_sign(delta(a,t,hi,ell))==1)
        ck(sum(abs(x-y) for x,y in zip([F(1,4),(t-lo)/2,(t-lo)/2,lo],
                  [F(1,4),(t-hi)/2,(t-hi)/2,hi]))/2==hi-lo)
        brackets.append({'m':m,'lo':str(lo),'hi':str(hi),'same_binary64':float(lo)==float(hi),
                         'exact_signs':[-1,1]})
aliases=[row for row in brackets if row['same_binary64']]
ck(bool(aliases))

# Full-query erratum at the smallest actual counterexample: matched AND2.
parentCE=F(2); meanChildCE=F(1); erasure=F(1); occupationKL=F(0)
ck(erasure+meanChildCE-parentCE==-occupationKL)
ck(meanChildCE-parentCE != -occupationKL)
# Original-owner substitution, all signed releases included exactly once.
owner_checks=0
for B in [F(2),F(3)]:
    for C in [F(1),F(3,2)]:
        for U in [F(0),F(1,4)]:
            for S in [F(-1,4),F(0),F(1,4),F(3,2)]:
                ck(B-(C+S)-U==(B-C-U)-S)
                ck((C+S+U<=B)==(S<=B-C-U));owner_checks+=1

result={'status':'PASS','exact_assertions':checks,'profiles':profiles,'trial_points':trials,
        'minimality_cases_n0_n1':small,'dyadic_brackets':len(brackets),'owner_cases':owner_checks,
        'first_binary64_alias_in_frozen_grid':aliases[0],
        'seconds':time.perf_counter()-start,'sign_arithmetic':'Fraction and integer powers; no numerical log signs',
        'full_FEI':'OPEN','formal_scope':'separate Lean algebra check only'}
(ROOT/'out/DYADIC_BRACKETS.json').write_text(json.dumps(brackets,indent=2),encoding='utf-8')
(ROOT/'out/CHECKS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
