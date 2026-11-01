"""Frozen A076-controls-v1: exact spectra; floating entropies are diagnostics."""
from fractions import Fraction as Q
from math import comb, log2
from pathlib import Path
import json, time, hashlib

ROOT = Path(__file__).resolve().parents[1]
start = time.perf_counter()
checks = 0
rows = []

def check(a, b):
    global checks
    assert a == b, (a, b)
    checks += 1

def fwht(v):
    a = v.copy()
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                u, v = a[j], a[j+h]
                a[j], a[j+h] = u+v, u-v
        h *= 2
    return [Q(x, len(a)) for x in a]

def H(ps):
    return sum(-float(p)*log2(float(p)) for p in ps if p)

def validate(label, n, truth, expected):
    coeff = fwht(truth)
    for s, c in enumerate(coeff):
        check(c, expected(s))
    check(sum(c*c for c in coeff), Q(1))
    spectral_I = sum(s.bit_count()*c*c for s,c in enumerate(coeff))
    edge_I = sum(Q(sum(truth[x] != truth[x^(1<<i)] for x in range(1<<n)), 1<<n) for i in range(n))
    check(spectral_I, edge_I)
    rows.append(dict(family=label,n=n,H_diagnostic=H([c*c for c in coeff]),I_exact=str(spectral_I)))
    return coeff, spectral_I

def threshold(n, r, k):
    # bits use chi=(-1)^bit. Thus coefficients have (-1)^j at j set bits.
    return Q(sum((1 if j+ell >= r else -1)*(-1)**j*comb(k,j)*comb(n-k,ell)
                 for j in range(k+1) for ell in range(n-k+1)), 1<<n)

for n in range(1,10):
    for r in range(n+2):
        truth = [1 if x.bit_count() >= r else -1 for x in range(1<<n)]
        coeff, influence = validate(f'threshold({n},{r})',n,truth,lambda s: threshold(n,r,s.bit_count()))
        check(influence, Q(n*comb(n-1,r-1),1<<(n-1)) if 1<=r<=n else Q(0))
        if n%2 and r==(n+1)//2:
            m=(n-1)//2
            for k in range(n+1):
                if k%2==0: target=Q(0)
                else:
                    j=(k-1)//2
                    target=-(-1)**j*Q(comb(2*m,m)*comb(m,j),(1<<(2*m))*comb(2*m,2*j))
                check(threshold(n,r,k),target)

for w in range(1,5):
    for t in range(1,5):
        n = w*t
        if n>12: continue
        mask=(1<<w)-1
        # active tribe consists of all 0 bits; f=1-2*no-active.
        truth=[1 if any((x>>(w*j))&mask == 0 for j in range(t)) else -1 for x in range(1<<n)]
        q=Q(1,1<<w); b=1-q; a=b**t
        def expected(s):
            if s==0: return 1-2*a
            k=sum(bool((s>>(w*j))&mask) for j in range(t))
            return -2*(-q)**k*b**(t-k)
        coeff,influence=validate(f'tribes({w},{t})',n,truth,expected)
        check(influence,2*t*w*q*b**(t-1))
        grouped = {0:(1-2*a)**2}
        for k in range(1,t+1):
            grouped[k]=comb(t,k)*((1<<w)-1)**k*4*q**(2*k)*b**(2*(t-k))
        check(sum(grouped.values()),Q(1))
        for k in range(t+1):
            check(sum(c*c for s,c in enumerate(coeff) if sum(bool((s>>(w*j))&mask) for j in range(t))==k),grouped[k])
        closed=H([(1-2*a)**2])+8*w*t*float(q*a)-8*float(t*b*a-t*a*a)*log2(float(b))-8*float(a-a*a)
        assert abs(closed-rows[-1]['H_diagnostic'])<1e-10
        # Independent enumeration of each conditional Fourier fiber U|T.
        c0=1-4*a+4*a*a/b
        active_empty=4*q*a*a/b
        residual={}
        for s,c in enumerate(coeff): residual[s>>w]=residual.get(s>>w,Q(0))+c*c
        check(residual[0],c0)
        M=0.0
        for T,mass in residual.items():
            if not mass: continue
            conditional=[]
            for U in range(1<<w):
                p=coeff[(T<<w)|U]**2/mass
                target=((1-2*a)**2/c0 if U==0 else 4*q*q*b**(2*t-2)/c0) if T==0 else (b if U==0 else q*q/b)
                check(p,target)
                conditional.append(p)
            M+=float(mass)*H(conditional)
        Lsub=(1<<w)-1
        u=active_empty/c0 if c0 else Q(0)
        Mformula=float(c0)*H([u,1-u])+float(1-c0)*H([q,b])+float(4*q*a)*log2(Lsub)
        assert abs(M-Mformula)<1e-10
        prev=b**(t-1)
        Hprev=H([(1-2*prev)**2])+8*w*(t-1)*float(q*prev)-8*float((t-1)*b*prev-(t-1)*prev*prev)*log2(float(b))-8*float(prev-prev*prev)
        L=closed-float(b)*Hprev
        rows[-1].update(M_A_diagnostic=M,J_A_diagnostic=L-M,L_A_diagnostic=L,I_A_exact=str(w*2*q*b**(t-1)),Delta_A_exact='0')

def maj3(v): return 1 if sum(v)>0 else -1

def recursive_value(x, depth):
    if depth==0: return 1 if x&1 else -1
    m=3**(depth-1)
    return maj3([recursive_value(x>>(j*m),depth-1) for j in range(3)])

def rec_coeff(s,depth):
    if depth==0: return Q(-1) if s==1 else Q(0)
    m=3**(depth-1); mask=(1<<m)-1
    blocks=[(s>>(j*m))&mask for j in range(3)]
    k=sum(bool(v) for v in blocks)
    if k==1: outer=Q(1,2)
    elif k==3: outer=Q(-1,2)
    else: return Q(0)
    for v in blocks:
        if v: outer*=rec_coeff(v,depth-1)
    return outer

for depth in (1,2):
    n=3**depth
    coeff,influence=validate(f'recursive-majority3({depth})',n,[recursive_value(x,depth) for x in range(1<<n)],lambda s:rec_coeff(s,depth))
    check(influence,Q(3,2)**depth)
    # Every nonzero squared coefficient is 4^-number_of_active_internal_nodes.
    entropy=Q(0)
    for c in coeff:
        if c:
            den=(c*c).denominator
            check(den & (den-1),0)
            entropy+=c*c*(den.bit_length()-1)
    check(entropy,4*(influence-1))
    rows[-1]['H_exact']=str(entropy)

n=15
def mixed_value(x):
    return maj3([1 if ((x>>(5*j))&31).bit_count()>=3 else -1 for j in range(3)])
def mixed_coeff(s):
    blocks=[(s>>(5*j))&31 for j in range(3)]
    k=sum(bool(v) for v in blocks)
    if k not in (1,3): return Q(0)
    z=Q(1 if k==1 else -1,2)
    for v in blocks:
        if v:z*=threshold(5,3,v.bit_count())
    return z
coeff,influence=validate('majority3-of-majority5',n,[mixed_value(x) for x in range(1<<n)],mixed_coeff)
check(influence,Q(45,16))
hm5=H([threshold(5,3,s.bit_count())**2 for s in range(32)])
assert abs(rows[-1]['H_diagnostic']-(2+1.5*hm5))<1e-10

output=dict(helper_version='A076-controls-v2-block-extension',case_count=len(rows),exact_assertions=checks,
            elapsed_seconds=time.perf_counter()-start,rows=rows,
            code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            conclusion='Exact rational checks passed. Entropy decimals are diagnostic only.')
(ROOT/'out'/'VALIDATION.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in output.items() if k!='rows'},indent=2))
