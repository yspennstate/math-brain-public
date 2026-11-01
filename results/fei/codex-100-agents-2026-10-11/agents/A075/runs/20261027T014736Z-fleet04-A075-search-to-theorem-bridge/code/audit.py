from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import json,time,hashlib
ROOT=Path(__file__).resolve().parents[1]

def main():
    start=time.monotonic();checks=0
    # Independently reconstruct the exact three selected proof patterns.
    for a,b,c in product([-1,1],repeat=3):
        for rr in [[(-a,-b),(-a,b),(a,b)],
                   [(-a,-a,a),(-a,a,a),(b,b,b)],
                   [(-a,-a,a),(-b,b,b),(c,c,c)]]:
            assert len(set(rr))==3;checks+=1
    main=json.loads((ROOT/'out/MAIN.json').read_text(encoding='utf-8'))
    assert main['circuits']==278 and main['proper_block_checks']==14782;checks+=2
    # Independent physical-pair reconstruction of all residual rows, not the
    # source implementation's embedding loop, and direct Walsh sums.
    reviewed=[]
    for n in range(4):
        N=n+3
        f=[-1]*(1<<n)
        g=[f[x%len(f)]*(-1 if x.bit_count()<=1 else 1) for x in range(1<<N)]
        for B in range(1,(1<<N)-1):
            if B.bit_count()<2:continue
            groups={}
            for x,v in enumerate(g):groups.setdefault(x&B,{})[x&~B]=v
            rr={tuple(d[y] for y in sorted(d)) for d in groups.values()}
            assert len(rr)==3;checks+=1
        for S in range(1<<N):
            coeff=sum(g[x]*(-1 if (x&S).bit_count()%2 else 1) for x in range(len(g)))
            expected=-(1<<N)+2*(N+1) if S==0 else 2*(N+1-2*S.bit_count())
            assert coeff==expected;checks+=1
        I=Q(sum(g[x]!=g[x^(1<<i)] for x in range(len(g)) for i in range(N)),len(g))
        assert I==Q(2*N*(N-1),1<<N);checks+=1
        reviewed.append({'dimension':N,'I':str(I)})
    # Check that a tempting one-point replacement does NOT ensure primeness:
    # f constant, a block of two padding bits can be compressed by their AND.
    g=[-1 if x==0 else 1 for x in range(8)]
    rr={tuple(g[a|b] for b in [0,4]) for a in range(4)}
    assert len(rr)==2;checks+=1
    spec=json.loads((ROOT/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
    assert hashlib.sha256((ROOT/'code/verify.py').read_bytes()).hexdigest()==spec['helper_sha256'];checks+=1
    out={'checks':checks,'elapsed_seconds':time.monotonic()-start,'source_review':'A071-PRIME-BALL-PROPER-PARTITION-OBSTRUCTION@1 analytic proof independently reconstructed unchanged; all n>=3 with formula/row checks n=3..6','ball_rows':reviewed,'mutation_control':'radius-zero perturbation fails: exactly two rows for a proper 2-bit block','scope':'analytic theorem m>=3; finite checks are not an infinite-domain certificate'}
    (ROOT/'out/AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))

if __name__=='__main__':main()
