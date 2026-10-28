"""Exact bounded verification of the independent quadratic contrast reference.

Integer Walsh coefficients and Fraction identities are certificates. Entropy
signs are checked as rational linear combinations of prime logarithms, with
rational atanh remainders. Floating values never decide a sign.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
import argparse, hashlib, itertools, json, time

HERE = Path(__file__).resolve().parent.parent
START = time.monotonic()
CHECKS = 0

def check(x, label):
    global CHECKS
    CHECKS += 1
    if not x:
        raise AssertionError(label)

def walsh(a):
    a = list(a)
    s = 1
    while s < len(a):
        for i in range(0, len(a), 2*s):
            for j in range(i, i+s):
                x, y = a[j], a[j+s]
                a[j], a[j+s] = x+y, x-y
        s *= 2
    return [F(x, len(a)) for x in a]

def influence(a):
    n = (len(a)-1).bit_length()
    return [F(sum(a[x] != a[x ^ (1 << j)] for x in range(len(a))), len(a)) for j in range(n)]

@lru_cache(None)
def factors(n):
    out = []
    k = 2
    while k*k <= n:
        e = 0
        while n % k == 0:
            e += 1
            n //= k
        if e:
            out.append((k,e))
        k += 1
    if n > 1:
        out.append((n,1))
    return tuple(out)

def addlog(out, coefficient, x):
    if not coefficient or x == 1:
        return
    check(x > 0, 'log positive')
    for p,e in factors(x.numerator):
        out[p] += coefficient*e
    for p,e in factors(x.denominator):
        out[p] -= coefficient*e

def entropy(a):
    out = defaultdict(F)
    for p in a:
        if p:
            addlog(out, -p, p)
    return dict(out)

def ce(p,q):
    out = defaultdict(F)
    for x,y in zip(p,q):
        if x:
            check(y > 0, 'reference support')
            addlog(out, -x, y)
    return dict(out)

def combine(*terms):
    out = defaultdict(F)
    for c,a in terms:
        for p,v in a.items():
            out[p] += c*v
    return {p:v for p,v in out.items() if v}

@lru_cache(None)
def ln_interval(n):
    # No range reduction is needed for the small prime factors in this domain.
    # Use dyadic reduction to keep the atanh parameter <= 1/3.
    k = n.bit_length()-1
    y = F(n, 1 << k)
    def series(y):
        t = (y-1)/(y+1)
        t2 = t*t
        z = t
        s = F(0)
        N = 48
        for j in range(N):
            s += 2*z/(2*j+1)
            z *= t2
        rem = 2*abs(z)/((2*N+1)*(1-t2))
        return s-rem, s+rem
    a,b = series(y)
    if k:
        c,d = series(F(2))
        a,b = a+k*c,b+k*d
    return a,b

SIGN_CACHE = {}
def nonnegative(expr, label):
    key = tuple(sorted(expr.items()))
    if key in SIGN_CACHE:
        check(SIGN_CACHE[key],label)
        return
    if not expr:
        SIGN_CACHE[key] = True
        check(True,label)
        return
    lo = F(0)
    hi = F(0)
    for p,c in expr.items():
        a,b = ln_interval(p)
        lo += c*(a if c >= 0 else b)
        hi += c*(b if c >= 0 else a)
    check(lo >= 0, label + ' unresolved interval ' + str((lo,hi)))
    SIGN_CACHE[key] = True

def rank(rows):
    rows = list(rows)
    r = 0
    for j in range(len(rows)):
        z = next((k for k in range(r,len(rows)) if rows[k] >> j & 1), None)
        if z is None:
            continue
        rows[r], rows[z] = rows[z], rows[r]
        for k in range(len(rows)):
            if k != r and rows[k] >> j & 1:
                rows[k] ^= rows[r]
        r += 1
    return r

def quadratic(m, code):
    terms = [0] + [1 << i for i in range(m)] + [(1 << i)|(1 << j) for i in range(m) for j in range(i+1,m)]
    selected = [t for k,t in enumerate(terms) if code >> k & 1]
    vals = [(-1)**sum((z & t) == t for t in selected) for z in range(1 << m)]
    rows = [sum(1 << j for j in range(m) if j != i and ((1 << i)|(1 << j)) in selected) for i in range(m)]
    return vals,rank(rows)

def run_case(gp,gm,beta,r):
    a,c,t = walsh(gp),walsh(gm),walsh(beta)
    nx,nz = len(gp),len(beta)
    b = t[0]
    p = (1+b)/2
    d = F(sum(x != y for x,y in zip(gp,gm)),nx)
    u,v = [(x+y)/2 for x,y in zip(a,c)],[(x-y)/2 for x,y in zip(a,c)]
    pp,pm = [x*x for x in a],[x*x for x in c]
    M = [p*x+(1-p)*y for x,y in zip(pp,pm)]
    C = [d*x*x for x in t]
    C[0] += 1-d
    check(sum(M)==sum(C)==1,'marginal normalization')
    check(all(x*x==F(1,1 << r) for x in t if x),'quadratic flatness')
    check(sum(bool(x) for x in t)==1 << r,'quadratic support size')
    check(entropy([x*x for x in t])=={2:F(r)} or r==0 and not any(entropy([x*x for x in t]).values()),'quadratic entropy rank')
    f = [gp[x] if beta[z]==1 else gm[x] for z in range(nz) for x in range(nx)]
    coeff = walsh(f)
    P = [x*x for x in coeff]
    for z in range(nz):
        for x in range(nx):
            check(coeff[z*nx+x] == (u[x]+b*v[x] if z==0 else v[x]*t[z]),'physical Walsh coefficient')
    for x in range(nx):
        check(sum(P[z*nx+x] for z in range(nz))==M[x],'data spectral marginal')
    for z in range(nz):
        check(sum(P[z*nx+x] for x in range(nx))==C[z],'control spectral marginal')
    # Exact-spectrum references exercise all normalizers and zero atoms.
    R = [M[x]*C[z] for z in range(nz) for x in range(nx)]
    check(sum(R)==1,'full reference normalization')
    gamma = ce(P,R)
    HM,HC = entropy(M),entropy(C)
    check(combine((1,gamma),(-1,HM),(-1,HC))=={},'product reference exact cost')
    nonnegative(combine((1,gamma),(-1,entropy(P))),'Gibbs nonnegative')
    avg = combine((p,entropy(pp)),(1-p,entropy(pm)))
    JS = combine((1,HM),(-1,avg))
    nonnegative(JS,'spectral Jensen Shannon')
    ip,im,ib,iff = influence(gp),influence(gm),influence(beta),influence(f)
    e = [x*y for x,y in zip(gp,gm)]
    ie = sum(influence(e))
    for j in range(len(ip)):
        check(iff[j]==p*ip[j]+(1-p)*im[j],'data influence identity')
    for j in range(len(ib)):
        check(iff[len(ip)+j]==d*ib[j],'control influence identity')
    check(F(r)<=2*sum(ib),'rank influence inequality')
    check(4*d*(1-d)<=ie,'disagreement Poincare')
    check(ie<=sum(ip)+sum(im),'product boundary union')
    nonnegative(combine((1, {2:ie}),(-1,entropy([d,1-d]))),'output entropy tensorization')
    nonnegative(combine((1,{2:3*ie}),(-1,JS)),'rare signed spectral mixing <=3 product influence')
    nonnegative(combine((1,entropy([d,1-d])),(1,{2:d*r}),(-1,HC)),'latent activation control entropy')
    nonnegative(combine((1,avg),(1,{2:4*ie+2*d*sum(ib)}),(-1,gamma)),'complete reference payment')
    if abs(b)<1:
        check(min(p,1-p)>=F(1,4),'nonconstant quadratic physical branch weights')
        check(ie<=4*sum(iff[:len(ip)]),'one original terminal reserve capacity')
    # Two other inherited references: a fixed full-support reference and one
    # distinct softened branch. This checks that exact-spectrum renewal is not used.
    qp = [F(1,nx)]*nx
    qm = [(x+F(1,nx))/2 for x in pm]
    Q = [p*x+(1-p)*y for x,y in zip(qp,qm)]
    gap = combine((1,ce(M,Q)),(-p,ce(pp,qp)),(-(1-p),ce(pm,qm)))
    nonnegative(combine((1,JS),(-1,gap)),'inherited reference logsum contraction')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pilot',action='store_true')
    args = ap.parse_args()
    completed = 0
    fixtures = 0
    status = 'PASS'
    error = None
    try:
        for i,j,k in itertools.product(range(16),range(16),range(16)):
            if time.monotonic()-START>55:
                raise TimeoutError('frozen wall-clock limit')
            gp = [1 if i >> x & 1 else -1 for x in range(4)]
            gm = [1 if j >> x & 1 else -1 for x in range(4)]
            beta,r = quadratic(2,k)
            run_case(gp,gm,beta,r)
            completed += 1
            if args.pilot and completed==256:
                break
        if not args.pilot:
            for q,(a,c),m in itertools.product([1,3,5],[(1,1),(2,1),(1,2)],[2,3,4]):
                if time.monotonic()-START>55:
                    raise TimeoutError('frozen wall-clock limit')
                gp,gm = [],[]
                for x in range(1 << (q+1)):
                    xx = 1 if x & 1 else -1
                    ell = sum(1 if x >> j & 1 else -1 for j in range(1,q+1))
                    gp.append(1 if (a+c)*xx+ell>=0 else -1)
                    gm.append(1 if (a-c)*xx+ell>=0 else -1)
                terms = [0]+[1 << i for i in range(m)]+[(1 << i)|(1 << j) for i in range(m) for j in range(i+1,m)]
                selected = [(1 << i)|(1 << (i+1)) for i in range(0,m-1,2)]
                if m%2:
                    selected.append(1 << (m-1))
                code = sum(1 << terms.index(t) for t in selected)
                beta,r = quadratic(m,code)
                run_case(gp,gm,beta,r)
                fixtures += 1
    except Exception as exc:
        status='UNRESOLVED' if isinstance(exc,TimeoutError) else 'FAIL'
        error=repr(exc)
    result={'status':status,'main_cases':completed,'targeted_cases':fixtures,'assertions':CHECKS,'seconds':time.monotonic()-START,'arithmetic':'integer/Fraction + 48-term rational atanh prime-log certificates','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'sign_certificates':len(SIGN_CACHE),'error':error}
    out=HERE/'out'
    out.mkdir(exist_ok=True)
    name='pilot.json' if args.pilot else 'verification.json'
    (out/name).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result),flush=True)
    if status!='PASS':
        raise SystemExit(1)

if __name__=='__main__':
    main()
