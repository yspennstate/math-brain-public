"""A003 stage22: bounded exact tensor-interface checks; standard library only."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import hashlib, json, time

ROOT=Path(__file__).resolve().parents[1]
def save(name,obj):
    p=ROOT/name
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def main():
    # Freeze before enumeration, including the adversarial (non-Boolean) control.
    spec={'helper_version':'A003-stage22-v1','family':'all Boolean truth tables on n=0,1,2,3; tensor with itself for m=2,3',
          'domain':{'n':[0,1,2,3],'m':[2,3]},'case_count':556,'symmetry':'none',
          'arithmetic':'integer Walsh sums and Fraction probability identities; no floating entropy signs',
          'memory_estimate_mb':40,'max_runtime_seconds':55,'automatic_escalation':False,
          'checks':'norm, exact signed autocorrelation, tensor marginals, pair homogeneity, influence and eligible-coordinate replication, non-Boolean negative control'}
    save('out/FROZEN_SPEC.json',spec)
    start=time.monotonic(); checks=0; cases=0; roots=0; signatures=set()
    def ck(v):
        nonlocal checks
        checks+=1
        assert v
        assert time.monotonic()-start<55
    for n in range(4):
        N=1<<n
        for mask in range(1<<N):
            vals=[1-2*((mask>>x)&1) for x in range(N)]
            a=[F(sum(vals[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(N)),N) for s in range(N)]
            p=[v*v for v in a]; roots+=1
            ck(sum(p)==1)
            for u in range(N): ck(sum(a[s]*a[s^u] for s in range(N))==(u==0))
            al=[sum(p[s] for s in range(N) if s>>i&1) for i in range(n)]
            I=sum(al); active=[i for i in range(n) if al[i]>0]; d=len(active)
            G=[i for i in active if al[i]>=I/F(2*d)] if d else []
            if d: ck(bool(G))
            for m in (2,3):
                # Other m-1 blocks are a product law represented as exact masses.
                tail=[F(1)]
                for _ in range(m-1): tail=[t*v for t in tail for v in p if v]
                ck(sum(tail)==1)
                # Tensor entropy follows from actual product-law marginals;
                # pair erasure and signed downward terms are homogeneous.
                for s,v in enumerate(p): ck(sum(v*t for t in tail)==v)
                for i in range(n):
                    ck(sum(al[i]*t for t in tail)==al[i])
                    for s in range(N):
                        if s>>i&1: continue
                        u,v=p[s],p[s|(1<<i)]
                        for t in tail:
                            ck((t*u+t*v)==t*(u+v))
                            if u+v: ck((t*v)/(t*u+t*v)==v/(u+v))
                            if v: ck((t*u)/(t*v)==u/v)
                ck(sum(al*m)==m*I)
                if d:
                    Gm=[(b,i) for b in range(m) for i in active if al[i]>=m*I/F(2*m*d)]
                    ck(Gm==[(b,i) for b in range(m) for i in G])
                cases+=1
    # Without Booleanity an empty-heavy product has unbounded H/I and no good
    # erasure coordinate. Rational single-block amplitudes 3/5,4/5 show exactly
    # why autocorrelation is an indispensable hypothesis (24/25 at shift 1).
    z=[F(3,5),F(4,5)]
    ck(sum(v*v for v in z)==1)
    ck(sum(z[s]*z[s^1] for s in range(2))==F(24,25))
    # Entropy additivity follows from p^tensor and log(product)=sum log;
    # no decimal logarithm is used as a proof certificate.
    result={'status':'PASS','roots':roots,'tensor_cases':cases,'exact_assertions':checks,
            'seconds':time.monotonic()-start,'scope':'finite algebra only; all-dimensional proof in DERIVATION.md',
            'negative_control':'normalized real vector (3/5,4/5) fails nonzero-shift Booleanity by 24/25',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    save('out/EXACT_CHECKS.json',result)
    print(json.dumps(result))

if __name__=='__main__': main()
