"""A041 v1: exact Fraction product Fourier and pivotal-noise validation."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, time, hashlib

ROOT = Path(__file__).resolve().parents[1]
START = time.monotonic()
assertions = 0
def check(v):
    global assertions
    assert v
    assertions += 1

def spectrum(values, qs):
    # Output u_S = hat(h)(S) / sqrt(prod_{j in S} q_j(1-q_j)).
    # Means in absent bits; finite differences in present bits.
    a = list(map(F, values))
    for i, q in enumerate(qs):
        step = 1 << i
        for base in range(0, len(a), 2*step):
            for j in range(step):
                lo, hi = a[base+j], a[base+j+step]
                a[base+j] = (1-q)*lo+q*hi
                a[base+j+step] = hi-lo
    probs = []
    for mask, u in enumerate(a):
        factor = F(1)
        for i, q in enumerate(qs):
            if mask >> i & 1:
                factor *= q*(1-q)
        probs.append(u*u*factor)
    return probs

def mass(mask, qs):
    p = F(1)
    for i, q in enumerate(qs):
        p *= q if mask >> i & 1 else 1-q
    return p

def expand(mask, i):
    return (mask & ((1<<i)-1)) | ((mask >> i) << (i+1))

def case(weights, qs, threshold, label, physical=False):
    n = len(qs)
    vals = [2*int(sum(w for j,w in enumerate(weights) if x>>j&1)
                   >= threshold)-1 for x in range(1<<n)]
    ps = spectrum(vals, qs)
    check(sum(ps)==1)
    mean = sum(mass(x,qs)*vals[x] for x in range(1<<n))
    check(ps[0]==mean*mean)
    influence = sum(mask.bit_count()*p for mask,p in enumerate(ps))
    variance = 1-ps[0]
    deficit = influence-variance
    check(deficit==sum((s.bit_count()-1)*ps[s]
                       for s in range(1,1<<n)))
    score_max = F(0)
    noise_tests = 0
    for i, wi in enumerate(weights):
        rest = [j for j in range(n) if j!=i]
        qr = [qs[j] for j in rest]
        ds = [(vals[expand(x,i)|(1<<i)]-vals[expand(x,i)])//2
              for x in range(1<<(n-1))]
        check(all(d in (0,1) for d in ds))
        rho = sum(mass(x,qr)*ds[x] for x in range(len(ds)))
        dp = spectrum(ds, qr)
        check(sum(dp)==rho)
        ii = sum(ps[s] for s in range(1<<n) if s>>i&1)
        check(ii==4*qs[i]*(1-qs[i])*rho)
        check(ps[1<<i]==4*qs[i]*(1-qs[i])*rho*rho)
        for b in range(len(ds)):
            check(ps[expand(b,i)|(1<<i)]==4*qs[i]*(1-qs[i])*dp[b])
        if not rho:
            continue
        # k=0..6 frozen, not increased after observations.
        for k in range(7):
            r = 1 << k
            um = sum(1<<a for a,j in enumerate(rest) if weights[j]*r>=wi)
            L = 2*sum(min(qr[a],1-qr[a]) for a in range(n-1) if um>>a&1)
            prior = F(1,(k+1)*(k+2))
            # Check half-open interval fiber chains by exhaustive comparable
            # endpoints, plus cardinal-step exclusion at r or more steps.
            if n<=4:
                for a in range(len(ds)):
                    if not ds[a]:
                        continue
                    for b in range(len(ds)):
                        if ds[b] and (a & ~um)==(b & ~um) and a&b==a:
                            check((b^a).bit_count()<r)
            for b in range(len(ds)):
                score = prior*prior*L/F(r*r*((b&um).bit_count()+1))
                score_max = max(score_max,score)
            if not L:
                continue
            for eps in (F(1,4),F(1,2),F(1)):
                cov = sum(p*(1-eps)**((b&um).bit_count())
                          for b,p in enumerate(dp))
                check(0<=cov<=rho)
                # Exact rational squared form; all quantities nonnegative.
                check(cov*cov*eps*L<=r*r*rho*rho)
                noise_tests += 1
                if physical and k in (0,1):
                    direct = F(0)
                    for x in range(len(ds)):
                        if not ds[x]:
                            continue
                        for y in range(len(ds)):
                            if not ds[y]:
                                continue
                            ker = F(1)
                            for a,q in enumerate(qr):
                                if um>>a&1:
                                    ker *= ((1-eps)*int((x>>a&1)==(y>>a&1))
                                            +eps*(q if y>>a&1 else 1-q))
                                else:
                                    ker *= int((x>>a&1)==(y>>a&1))
                            direct += mass(x,qr)*ker
                    check(direct==cov)
    return {'label':label,'n':n,'noise_tests':noise_tests,
            'I':str(influence),'V':str(variance),'Delta':str(deficit),
            'max_multiscale_score_tested':str(score_max)}

rows = []
for qs in product((F(1,8),F(1,2),F(7,8)), repeat=3):
    for t in range(1,9):
        rows.append(case((1,2,4),qs,t,'small-cube',physical=(qs==(F(1,8),)*3)))
for qs in ((F(1,2),)*4,(F(1,8),F(1,4),F(3,4),F(7,8))):
    for t in range(1,13):
        rows.append(case((1,2,3,5),qs,t,'four-bit',physical=(t==6)))
for m in range(2,7):
    q = F(1,m*m)
    a = q**m
    q0 = (m-1)*a/(1+(m-1)*a)
    row = case((m,)+(1,)*m,(q0,)+(q,)*m,m,'weighted-global-control')
    check(F(row['max_multiscale_score_tested'])<1)
    # All k>=7 have score <=n/4^k, so they also have score <1.
    check(F(m+1,4**7)<1)
    rows.append(row)
for m in range(2,6):
    for q in (F(1,8),F(1,32)):
        a = q**m
        q0 = a/(1+a)
        row = case((m,)+(1,)*m,(q0,)+(q,)*m,m,'weighted-local-control')
        check(F(row['max_multiscale_score_tested'])<1)
        rows.append(row)
check(len(rows)==253)
out = {'helper_version':'A041-v1','arithmetic':'fractions.Fraction only',
       'case_count':len(rows),'assertions':assertions,'rows':rows,
       'elapsed_seconds':time.monotonic()-START,
       'scope':'Finite sanity checks; analytic proof supplies all weights/biases/scales.',
       'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'out'/'EXACT_VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
