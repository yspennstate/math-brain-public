from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json, time, sys

START=time.monotonic(); CHECKS=0
OUT=Path(__file__).resolve().parents[1]/'out'
def ck(b):
    global CHECKS
    CHECKS+=1
    assert b
    if time.monotonic()-START>55: raise RuntimeError('frozen 55s cap')
def walsh(f):
    a=list(f); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for i in range(j,j+h): a[i],a[i+h]=a[i]+a[i+h],a[i]-a[i+h]
        h*=2
    return [Q(x,len(a)) for x in a]
def dot(a,b): return (a&b).bit_count()%2
def weights(c):
    return [sum(x*x for s,x in enumerate(c) if dot(s,v)) for v in range(len(c))]
def basis(c):
    w=weights(c); n=(len(c)-1).bit_length(); d=[w[1<<i] for i in range(n)]
    return all(x<=Q(1,2) for x in d) and all(min(w[v],1-w[v])>=max(d[i] for i in range(n) if v>>i&1) for v in range(1,len(c)))
def rank(values):
    piv={}
    for v in values:
        while v:
            b=v.bit_length()-1
            if b in piv:v^=piv[b]
            else:piv[b]=v;break
    return len(piv)
def affine_rank(c):
    a=[s for s,x in enumerate(c) if x]; return rank([s^a[0] for s in a])
# Exact entropy as a rational linear combination of log2(prime).
def entropy(masses):
    terms=Counter()
    for x in masses:
        if not x:continue
        for val,sign in [(x.numerator,-1),(x.denominator,1)]:
            p=2
            while p*p<=val:
                while val%p==0:terms[p]+=sign*x; val//=p
                p+=1
            if val>1:terms[val]+=sign*x
    return {p:q for p,q in terms.items() if q}
def add(*terms):
    ans=Counter()
    for scale,d in terms:
        for p,v in d.items():ans[p]+=scale*v
    return {p:v for p,v in ans.items() if v}
def activate(f,k): return list(f)+[1]*(len(f)*((1<<k)-1))
def tensor(f,t):
    out=[1]
    for _ in range(t):out=[a*b for b in f for a in out]
    return out
def fixture(f,k):
    n=(len(f)-1).bit_length(); c=walsh(f); F=activate(f,k); C=walsh(F)
    p=Q(1,1<<k); mu=c[0]; delta=1-mu; w=weights(c); W=weights(C)
    d=[w[1<<i] for i in range(n)]; D=[W[1<<i] for i in range(n+k)]
    for v in range(len(C)):
        ck(W[v]==(p*delta if v>>n else p*w[v]))
    ck(D==[p*x for x in d]+[p*delta]*k)
    # Direct physical influence independently verifies the Fourier marginals.
    for i,x in enumerate(D):ck(x==Q(sum(F[a]!=F[a^(1<<i)] for a in range(len(F))),len(F)))
    criterion=all(w[v]>=max(d[i] for i in range(n) if v>>i&1) for v in range(1,1<<n)) and (not d or delta>=max(d))
    ck(basis(C)==criterion)
    # Full coefficient ledger, including the exceptional root.
    expected=[]
    for z in range(1<<k):
        for s in range(1<<n):expected.append((1-p+p*mu if z==0 else p*(mu-1)) if s==0 else p*c[s])
    ck(C==expected)
    # Entropy reconstructed from multiplicities, no floating logarithms.
    ledger=[(1-p*delta)**2]+[p*p*delta*delta]*((1<<k)-1)
    ledger += [p*p*x*x for x in c[1:] for _ in range(1<<k)]
    ck(entropy([x*x for x in C])==entropy(ledger))
    # Tensor and activation criterion are checked with all directions, not just pairs.
    if basis(c) and d and delta>=max(d):ck(basis(C))
    if affine_rank(c)==n and n>0:ck(affine_rank(C)==n+k)
    return basis(C), affine_rank(C)

pilot='--pilot' in sys.argv
counts=Counter(); examples={}
for n in range(0,3 if pilot else 4):
    for mask in range(1<<(1<<n)):
        f=[1-2*((mask>>x)&1) for x in range(1<<n)]
        c=walsh(f); counts['seeds']+=1
        if len(set(f))==1:continue
        ismin,ar=fixture(f,2); counts['activation_fixtures']+=1
        counts['affine_minimal_activated']+=ismin
        if n<=2 and not pilot:
            for t,k in [(1,3),(2,2),(2,3)]:
                g=tensor(f,t); cg=walsh(g)
                ck(entropy([a*a for a in cg])==add((Q(t),entropy([a*a for a in c]))))
                ck(sum(weights(cg)[1<<i] for i in range(n*t))==t*sum(weights(c)[1<<i] for i in range(n)))
                if basis(c):ck(basis(cg))
                fixture(g,k); counts['tensor_extra_fixtures']+=1
# A balanced affine-minimal full-span seed has no balancing-bit debt.
if not pilot:
    bent=[1,1,1,-1]; ck(basis(walsh(bent))); ck(affine_rank(walsh(bent))==2)
    # Majority fails affine minimality before activation but meets the weaker
    # raw directional criterion: activation actually makes it affine-minimal.
    maj=[1 if x.bit_count()<2 else -1 for x in range(8)]
    examples['majority3_activation_minimal']=fixture(maj,2)[0]
    ck(examples['majority3_activation_minimal'])
    parity2=[1,-1,-1,1]
    examples['parity2_activation_minimal']=fixture(parity2,2)[0]
    ck(not examples['parity2_activation_minimal'])
    point=[-1]+[1]*7
    examples['point3_activation_minimal']=fixture(point,2)[0]
    ck(examples['point3_activation_minimal'])
    # The delta condition cannot fail for Boolean seeds: d_i<=1-mu.
    # Check that necessary universal side condition on every seed separately.
    for n in range(4):
        for mask in range(1<<(1<<n)):
            f=[1-2*((mask>>x)&1) for x in range(1<<n)]
            c=walsh(f); w=weights(c)
            for i in range(n):ck(w[1<<i]<=1-c[0])
    examples['delta_condition_universally_boolean']=True
result={'status':'PASS','proof_rung':'exact finite certificate; analytic general proof separate','counts':dict(counts),'assertions':CHECKS,'seconds':time.monotonic()-START,'examples':examples,'pilot':pilot}
(OUT/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
