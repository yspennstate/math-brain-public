"""Frozen v1 exact seed-completion checks; no source implementation imports."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import hashlib, json, time

ROOT = Path(__file__).resolve().parents[1]
A = [1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1]
B = [1-int(bool(x)) for x in A]
checks = 0

def require(ok):
    global checks
    checks += 1
    assert ok, checks

def walsh(v):
    out = list(v)
    step = 1
    while step < len(out):
        for start in range(0,len(out),2*step):
            for j in range(start,start+step):
                x,y = out[j],out[j+step]
                out[j],out[j+step] = x+y,x-y
        step *= 2
    return out

def spectrum(v):
    return [Q(w*w,len(v)**2) for w in walsh(v)]

def energy(v):
    return sum((p*s.bit_count() for s,p in enumerate(spectrum(v))),Q(0))

def edge_energy(v):
    # Valid also for ternary rows: squared difference /4 on each directed edge.
    return sum((Q((x-v[j^(1<<i)])**2,4*len(v))
                for j,x in enumerate(v) for i in range(len(v).bit_length()-1)),Q(0))

def factor_integer(n):
    result = {}
    p = 2
    while p*p <= n:
        while n%p == 0:
            result[p] = result.get(p,0)+1
            n //= p
        p += 1
    if n>1: result[n] = result.get(n,0)+1
    return result

def log_vector(x):
    out = defaultdict(Q)
    for p,e in factor_integer(x.numerator).items():out[p] += e
    for p,e in factor_integer(x.denominator).items():out[p] -= e
    return out

def entropy(p):
    out = defaultdict(Q)
    for x in p:
        if x:
            for prime,e in log_vector(x).items():out[prime] -= x*e
    return {k:v for k,v in out.items() if v}

def add(*terms):
    out = defaultdict(Q)
    for scale,term in terms:
        for prime,c in term.items():out[prime] += scale*c
    return {k:v for k,v in out.items() if v}

def is_product(p):
    mass = sum(p)
    if not mass:return False
    d = len(p).bit_length()-1
    marg = [sum((v for j,v in enumerate(p) if j>>i&1),Q(0))/mass for i in range(d)]
    for j,x in enumerate(p):
        target = Q(1)
        for i,m in enumerate(marg):target *= m if j>>i&1 else 1-m
        if x/mass != target:return False
    return True

def as_json(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):as_json(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [as_json(v) for v in x]
    return x

def main():
    start = time.monotonic()
    pa,pb = spectrum(A),spectrum(B)
    wa,wb = sum(pa),sum(pb)
    ha,hb = entropy([p/wa for p in pa]),entropy([p/wb for p in pb])
    da,db = energy(A),energy(B)
    require((wa,wb,da,db)==(Q(5,8),Q(3,8),Q(23,16),Q(5,16)))
    require(all(a*a+b*b==1 and a*b==0 for a,b in zip(A,B)))
    require(is_product(pa) and not is_product(pb))
    require(ha=={2:Q(7,5),5:Q(1)})
    require(hb=={2:Q(3),3:Q(-1,2)})
    require(da==edge_energy(A) and db==edge_energy(B))
    hmass=entropy([wa,wb])
    hbase=add((1,hmass),(wa,ha),(wb,hb))
    require(hbase=={2:Q(5),3:Q(-9,16)})
    fixtures=[]
    # All seeds through three bits, including constants, parities and all phases.
    for n in range(4):
        length=1<<n
        for code in range(1<<length):
            h=[1-2*((code>>x)&1) for x in range(length)]
            ph=spectrum(h); hh=entropy(ph); ih=energy(h)
            # Layout u[0..3], seed[4..], address z[4+n].
            truth=[A[u]+z*B[u]*h[x] for z in [1,-1]
                   for x in range(length) for u in range(16)]
            require(all(v in (-1,1) for v in truth))
            p=spectrum(truth)
            expect=[]
            for branch in range(2):
                for j in range(length):
                    expect.extend([pa[s]*(j==0) if branch==0 else pb[s]*ph[j] for s in range(16)])
            require(p==expect)
            require(energy(truth)==Q(17,8)+wb*ih)
            require(energy(truth)==edge_energy(truth))
            require(entropy(p)==add((1,hbase),(wb,hh)))
            require(is_product(expect[:16*length]))
            require(not is_product(expect[16*length:]))
            require(energy([B[u]*h[x] for x in range(length) for u in range(16)])==db+wb*ih)
            if code in [0,1,(1<<length)-1]:
                fixtures.append(dict(n=n,code=code,H=entropy(p),I=energy(truth),conditional=add((wa,ha),(wb,hb),(wb,hh))))
    # Independent direct character transform for fixed fixtures.
    for h in [[1],[-1,1],[1,1,1,-1]]:
        v=[A[u]+z*B[u]*h[x] for z in [1,-1] for x in range(len(h)) for u in range(16)]
        direct=[sum(v[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(len(v))) for s in range(len(v))]
        require(direct==walsh(v))
    # Boundary and mass-modulus audit, not an all-dimensional proof.
    admitted=[]
    for e in range(1,11):
        for numerator in range(1,1<<e,4):
            q=Q(numerator,1<<e);comp=1-q
            if comp.numerator%4==1:admitted.append(q)
            require((comp.numerator%4==1)==(q==Q(1,2)))
    require(set(admitted)=={Q(1,2)})
    # Product-row norm congruence for every ternary table on <=3 bits.
    count=0
    import itertools
    for n in range(4):
        for row in itertools.product((-1,0,1),repeat=1<<n):
            p=spectrum(row)
            if sum(p) and is_product(p):
                require(sum(p).numerator%4==1);count+=1
    result=dict(status='PASS',helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                assertions=checks,seed_cases=sum(1<<(1<<n) for n in range(4)),
                ternary_product_rows=count,seconds=time.monotonic()-start,
                row_a=A,row_b=B,raw_a=walsh(A),raw_b=walsh(B),mass=[wa,wb],
                row_energy=[da,db],row_entropy=[ha,hb],base_entropy=hbase,
                base_influence=Q(17,8),fixtures=fixtures)
    (ROOT/'out/validation.json').write_text(json.dumps(as_json(result),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['status','assertions','seed_cases','ternary_product_rows','seconds']}))

if __name__=='__main__':main()
