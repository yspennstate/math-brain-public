"""Frozen v1: exact rational probabilities and prime-exponent logarithms."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
from pathlib import Path
import json, time

START = time.monotonic()
COUNT = 0
def check(x):
    global COUNT
    COUNT += 1
    assert x, COUNT
    assert time.monotonic()-START < 60

def factors(n):
    out = defaultdict(int)
    d = 2
    while d*d <= n:
        while n%d == 0:
            out[d] += 1
            n //= d
        d += 1
    if n>1: out[n] += 1
    return out

class Log:
    def __init__(self, terms=None): self.terms = {k:v for k,v in (terms or {}).items() if v}
    def __add__(self, other):
        z = defaultdict(F, self.terms)
        for k,v in other.terms.items(): z[k] += v
        return Log(z)
    def __neg__(self): return self.scale(-1)
    def __sub__(self, other): return self + (-other)
    def scale(self, a): return Log({k:v*a for k,v in self.terms.items()})
    def __eq__(self, other): return self.terms == other.terms
    def data(self): return {str(k):str(v) for k,v in sorted(self.terms.items())}

def log(x):
    x=F(x)
    z=defaultdict(F)
    for k,v in factors(x.numerator).items(): z[k] += v
    for k,v in factors(x.denominator).items(): z[k] -= v
    return Log(z)
def ent(p):
    z=Log()
    for v in p.values():
        if v: z=z-log(v).scale(v)
    return z
def kl(p,q):
    z=Log()
    for w,v in p.items():
        if v:
            check(q.get(w,0)>0)
            z=z+log(v/q[w]).scale(v)
    return z
def condition(p,k,y):
    mass=sum(p[w]*k[w][y] for w in p)
    return mass, {w:p[w]*k[w][y]/mass for w in p}

rational_cases=0
for weights in product(range(1,4),repeat=4):
    p={w:F(weights[w],sum(weights)) for w in range(4)}
    q={w:F(1,4) for w in range(4)}
    kp={w:{0:F(w+1,6),1:1-F(w+1,6)} for w in p}
    kq={w:{0:F(5-w,7),1:1-F(5-w,7)} for w in p}
    # Same-channel conserved divergence and entropy release.
    py={}; qy={}; rem=Log(); hrem=Log()
    for y in (0,1):
        py[y],pc=condition(p,kp,y)
        qy[y],qc=condition(q,kp,y)
        rem=rem+kl(pc,qc).scale(py[y])
        hrem=hrem+ent(pc).scale(py[y])
    check(kl(p,q)==kl(py,qy)+rem)
    joint={(w,y):p[w]*kp[w][y] for w in p for y in (0,1)}
    check(ent(p)-hrem == ent(p)+ent(py)-ent(joint))
    # Mismatched reveal kernels create exactly the stated injection.
    inj=Log(); rem=Log(); qy={}; switch=Log(); switched_rem=Log()
    r={w:F(w+1,10) for w in p}
    for w in p: inj=inj+kl(kp[w],kq[w]).scale(p[w])
    for y in (0,1):
        _,pc=condition(p,kp,y)
        qy[y],qc=condition(q,kq,y)
        rem=rem+kl(pc,qc).scale(py[y])
        switched_rem=switched_rem+kl(pc,r).scale(py[y])
        delta=Log()
        for w in p: delta=delta+log(qc[w]/r[w]).scale(pc[w])
        switch=switch+delta.scale(py[y])
    check(kl(p,q)+inj == kl(py,qy)+rem)
    check(kl(p,q)+inj+switch == kl(py,qy)+switched_rem)
    rational_cases += 1

def spectrum(table, remaining):
    N=len(table)
    return {s:sum((v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(table)),0)/F(N) for s in range(N)}

def child_table(table,i,y):
    out=[]
    for t in range(len(table)//2):
        x=(t&((1<<i)-1)) | (y<<i) | ((t>>i)<<(i+1))
        out.append(table[x])
    return out

def global_coeffs(table,coords):
    a=spectrum(table,coords)
    return {sum(1<<coords[i] for i in range(len(coords)) if s>>i&1):v for s,v in a.items()}

lift_cases=0
for mask in range(256):
    table=[1 if mask>>x&1 else -1 for x in range(8)]
    root=global_coeffs(table,[0,1,2])
    rootp={s:a*a for s,a in root.items() if a}
    # State: (root witness, current spectral set, physical history).
    states={(s,s,()):p for s,p in rootp.items()}
    nodes={(): (table,[0,1,2])}
    release=Log()
    erasure=Log()
    for depth in range(2):
        nextstates=defaultdict(F); nextnodes={}
        for hist,(tab,coords) in nodes.items():
            i=0 if depth==0 else (1 if hist[0]==0 else 2)
            j=coords.index(i)
            a=global_coeffs(tab,coords)
            b={y:global_coeffs(child_table(tab,j,y),[c for c in coords if c!=i]) for y in (0,1)}
            qT=defaultdict(F)
            for s,v in a.items(): qT[s&~(1<<i)]+=v*v
            node_mass=sum(v for (w,s,h),v in states.items() if h==hist)
            check(node_mass == F(1,2**depth))
            current=defaultdict(F); witness=defaultdict(F)
            for (w,s,h),v in states.items():
                if h==hist: current[s]+=v/node_mass; witness[w]+=v/node_mass
            for s,v in a.items(): check(current[s]==v*v)
            erasure=erasure+(ent(current)-ent(qT)).scale(node_mass)
            after_h=Log()
            for y in (0,1):
                nextnodes[hist+(y,)]=(child_table(tab,j,y),[c for c in coords if c!=i])
            for (w,s,h),v in states.items():
                if h!=hist: continue
                T=s&~(1<<i)
                for y in (0,1):
                    kernel=F(1,2)*b[y][T]**2/qT[T]
                    nextstates[w,T,h+(y,)]+=v*kernel
                check(sum(F(1,2)*b[y][T]**2/qT[T] for y in (0,1))==1)
            for y in (0,1):
                ch=hist+(y,); cm=sum(v for (w,s,h),v in nextstates.items() if h==ch)
                check(cm==node_mass/2)
                wp=defaultdict(F); sp=defaultdict(F)
                for (w,s,h),v in nextstates.items():
                    if h==ch: wp[w]+=v/cm; sp[s]+=v/cm
                for s,v in b[y].items(): check(sp[s]==v*v)
                after_h=after_h+ent(wp).scale(F(1,2))
            release=release+(ent(witness)-after_h).scale(node_mass)
        states={key:v for key,v in nextstates.items() if v}; nodes=nextnodes
    terminal=Log()
    leaf_spectral=Log()
    for hist in nodes:
        mass=sum(v for (w,s,h),v in states.items() if h==hist)
        wp=defaultdict(F)
        for (w,s,h),v in states.items():
            if h==hist: wp[w]+=v/mass
        terminal=terminal+ent(wp).scale(mass)
        tab,coords=nodes[hist]
        leaf_spectral=leaf_spectral+ent({s:a*a for s,a in global_coeffs(tab,coords).items()}).scale(mass)
    check(release+terminal==ent(rootp))
    check(terminal==erasure+leaf_spectral)
    lift_cases+=1

# Actual Boolean phase control: equal parent spectra, distinct named child spectra.
f=[1,1,1,-1]
g=[v*(-1 if x&2 else 1) for x,v in enumerate(f)]
check({s:a*a for s,a in spectrum(f,[0,1]).items()}=={s:a*a for s,a in spectrum(g,[0,1]).items()})
fp={s:a*a for s,a in spectrum(child_table(f,0,0),[1]).items()}
gp={s:a*a for s,a in spectrum(child_table(g,0,0),[1]).items()}
check(fp=={0:F(1),1:F(0)} and gp=={0:F(0),1:F(1)})
sign_cases=0
for mask in range(16):
    t=[1 if mask>>x&1 else -1 for x in range(4)]
    a=spectrum(t,[0,1])
    check(sum(v*v for v in a.values())==1)
    for y in (0,1): check(sum(v*v for v in spectrum(child_table(t,0,y),[1]).values())==1)
    sign_cases+=1

# Repeated information: W fair, first reveal W, second reveal same W.
check(ent({0:F(1,2),1:F(1,2)})==log(2))
check(ent({0:F(1)})==Log())
# Side conditioning: S=W xor L with W,L independent fair. I(W;L)=0,
# but I(W;L|S)=1; all four atoms have weight 1/4.
check(ent({(w,l):F(1,4) for w in (0,1) for l in (0,1)})==log(4))
# Explicit mismatched-channel unit injection, plus side-conditioned XOR entropy.
p={0:F(1,2),1:F(1,2)}
kp={w:{y:F(w==y) for y in (0,1)} for w in (0,1)}
kq={w:{y:F(1,2) for y in (0,1)} for w in (0,1)}
inj=Log(); rem=Log()
for w in p: inj=inj+kl(kp[w],kq[w]).scale(p[w])
for y in (0,1):
    mass,pc=condition(p,kp,y)
    _,qc=condition(p,kq,y)
    rem=rem+kl(pc,qc).scale(mass)
check(inj==log(2) and rem==log(2))
check(ent(p)==log(2) and ent({0:F(1)})==Log())
summary={"helper_version":"v1","status":"PASS","arithmetic":"Fraction; exact prime-exponent logarithms","assertions":COUNT,"rational_chain_cases":rational_cases,"physical_lift_cases":lift_cases,"two_bit_boolean_cases":sign_cases,"phase_control":{"parent":"uniform four spectral atoms","child_f":"empty atom","child_g":"coordinate-1 atom"},"runtime_seconds":time.monotonic()-START}
out=Path(__file__).resolve().parent.parent/'out'/'VALIDATION.json'
out.write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,indent=2))
