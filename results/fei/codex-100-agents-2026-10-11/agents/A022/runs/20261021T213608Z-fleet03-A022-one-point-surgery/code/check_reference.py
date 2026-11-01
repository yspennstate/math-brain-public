"""A022 signed-reference identities; exact rational prime-log arithmetic."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
@lru_cache(None)
def factors(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1; n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out
def add(*terms):
    out={}
    for t in terms:
        for p,a in t.items(): out[p]=out.get(p,F(0))+a
    return {p:a for p,a in out.items() if a}
def mul(a,t): return {p:a*b for p,b in t.items() if a*b}
@lru_cache(None)
def log(q):
    q=F(q); assert q>0
    return add(factors(q.numerator),mul(-1,factors(q.denominator)))
def phi(q): return mul(-q,log(q)) if q else {}
def ent(ps): return add(*(phi(p) for p in ps))
def ce(ps,qs): return add(*(mul(-p,log(q)) for p,q in zip(ps,qs) if p))
def walsh(xs):
    a=list(map(F,xs)); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return [x/len(a) for x in a]
def chi(s,x): return (-1)**((s&x).bit_count())
checks=0; cases=0
def eq(a,b):
    global checks
    assert a==b,(a,b); checks+=1
def instance(b,vertices,controllers):
    global cases
    N=len(b); Z=len(controllers[0]); k=N.bit_length()-1; delta=F(1,N)
    bh=walsh(b); P=[a*a for a in bh]; assert all(P)
    q=len(vertices); ah=[walsh([1-2*v for v in a]) for a in controllers]
    al=[F(sum(a),Z) for a in controllers]; mu=[a[0] for a in ah]
    fs=[]; data=[F(0)]*N
    fhs=[]; ach=[walsh(a) for a in controllers]
    for z in range(Z):
        f=b[:]
        for v,a in zip(vertices,controllers): f[v]*=1-2*a[z]
        fs.append(f)
        fhs.append(walsh(f))
        for s,x in enumerate(fhs[-1]): data[s]+=x*x/Z
    # Direct joint transform, independently against signed point formula.
    rows=[walsh([fhs[z][s] for z in range(Z)]) for s in range(N)]
    joint=[[x*x for x in row] for row in rows]
    for s in range(N):
        for t in range(Z):
            pred=(bh[s] if t==0 else 0)-2*delta*sum(b[v]*chi(s,v)*ach[j][t] for j,v in enumerate(vertices))
            eq(rows[s][t],pred)
    R=[sum(joint[s][t] for s in range(N)) for t in range(Z)]
    V=delta*sum(1-u*u for u in mu)
    eq(R[0],1-V)
    for t in range(1,Z): eq(R[t],delta*sum(a[t]*a[t] for a in ah))
    # Exact entropy-chain identity retaining joint conditional KL.
    H=ent([x for row in joint for x in row]); HR=ent(R)
    KL=add(*(mul(joint[s][t],add(log(joint[s][t]),mul(-1,log(P[s]*R[t]))))
             for s in range(N) for t in range(Z) if joint[s][t]))
    eq(H,add(HR,ce(data,P),mul(-1,KL)))
    # Physical signed-cut formula, each cut edge oriented from edited vertex.
    ell=[mul(-1,log(x)) for x in P]
    K=[mul(delta,add(*(mul(chi(s,d),ell[s]) for s in range(N)))) for d in range(N)]
    cut={}
    for z in range(Z):
        D={v for v,a in zip(vertices,controllers) if a[z]}
        cut=add(cut,*(mul(F(-4,N*Z)*b[x]*b[y],K[x^y]) for x in D for y in range(N) if y not in D))
    eq(add(ce(data,P),mul(-1,ent(P))),cut)
    # Direct actual data boundary formula, with adjacent-edit correction.
    directI=sum(F(sum(fs[z][x]!=fs[z][x^(1<<i)] for x in range(N)),N*Z) for z in range(Z) for i in range(k))
    Ib=sum(P[s]*s.bit_count() for s in range(N))
    predI=Ib+2*delta*sum(al[j]*sum(b[v]*b[v^(1<<i)] for i in range(k)) for j,v in enumerate(vertices))
    predI-=4*delta*sum(b[v]*b[w]*F(sum(controllers[j][z]*controllers[l][z] for z in range(Z)),Z)
                       for j,v in enumerate(vertices) for l,w in enumerate(vertices) if j<l and (v^w).bit_count()==1)
    eq(directI,predI)
    if q==1:
        v=vertices[0]; alpha=al[0]; m=mu[0]
        J=add(mul(delta,add(*ell)),mul(-b[v],add(*(mul(bh[s]*chi(s,v),ell[s]) for s in range(N)))))
        eq(cut,mul(4*delta*alpha,J))
        L=mul(delta,ent([x*x for x in ah[0]]))
        exact=add(ent(P),L,mul(4*delta*alpha,J),mul(k*V,log(F(2))),phi(1-V),mul(-delta,phi(m*m)),mul(-1,KL))
        eq(H,exact)
    cases+=1

def main(pilot=False):
    start=time.monotonic()
    (ROOT/'out').mkdir(exist_ok=True)
    ctr2=[[int(bool(m&(1<<z))) for z in range(4)] for m in range(16)]
    ctr1=[[int(bool(m&(1<<z))) for z in range(2)] for m in range(4)]
    seeds=[]
    for m in range(256):
        b=[1-2*int(bool(m&(1<<x))) for x in range(8)]
        if all(walsh(b)): seeds.append(b)
    if pilot: seeds=seeds[:4]
    for b in seeds:
        for a in ctr2: instance(b,[0],[a])
        for a in ctr1:
            for c in ctr1: instance(b,[0,1],[a,c])
    if not pilot:
        for m in range(16):
            b=[1-2*int(bool(m&(1<<x))) for x in range(4)]
            if all(walsh(b)):
                for v in range(4):
                    for a in ctr1: instance(b,[v],[a])
        g=[-1]+[1]*7; b=[g[x&7]*g[x>>3] for x in range(64)]
        for v in [0,1]:
            for a in ctr2: instance(b,[v],[a])
        # Product-reference kernel has no cross-block couplings, exact logs.
        P=[x*x for x in walsh(b)]
        ell=[mul(-1,log(x)) for x in P]
        for d in range(64):
            K=mul(F(1,64),add(*(mul(chi(s,d),ell[s]) for s in range(64))))
            if d&7 and d>>3: eq(K,{})
    result={'status':'PASS','cases':cases,'exact_assertions':checks,'seconds':time.monotonic()-start,
            'arithmetic':'Fraction and canonical rational coefficients of log2(prime); no floating sign decisions',
            'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'pilot':pilot}
    (ROOT/'out'/('pilot.json' if pilot else 'exact_checks.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__':
    import sys
    main('--pilot' in sys.argv)
