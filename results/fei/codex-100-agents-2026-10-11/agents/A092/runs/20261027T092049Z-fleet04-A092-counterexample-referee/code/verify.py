"""A092 independent literal truth-table and summary-encoding audit, stdlib only."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib, itertools, json, time, sys

ROOT=Path(__file__).resolve().parents[1]
def save(name,obj):
    (ROOT/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')

def run(pilot=False):
    start=time.perf_counter(); checks=0; constructions=0; blocks=0
    def ck(p):
        nonlocal checks
        checks+=1
        if not p: raise AssertionError(checks)
    def walsh(f):
        a=list(f); h=1
        while h<len(a):
            for j in range(0,len(a),2*h):
                for i in range(j,j+h):
                    u,v=a[i],a[i+h]; a[i],a[i+h]=u+v,u-v
            h*=2
        return a
    ranges=range(1,3) if pilot else range(1,4)
    for n in ranges:
        for mask in range(1<<(1<<n)):
            g=[1-2*((mask>>x)&1) for x in range(1<<n)]
            Ig=Q(sum(g[x]!=g[x^(1<<i)] for x in range(1<<n) for i in range(n)),1<<n)
            D0=sum(g[0]!=g[1<<i] for i in range(n))
            D1=sum(g[1<<j]!=g[(1<<j)|(1<<i)] for i in range(n) for j in range(n) if j!=i)
            for k in (2,3):
                N=n+k; L=1<<N; constructions+=1
                f=[g[y&((1<<n)-1)]*(-1 if y.bit_count()<=1 else 1) for y in range(L)]
                edges=[sum(f[y]!=f[y^(1<<i)] for y in range(L)) for i in range(N)]
                actual=Q(sum(edges),L)
                predicted=Ig+Q(2,L)*(N*(N-1)-2*k*D0-2*D1)
                ck(actual==predicted)
                ck(Q(sum(edges[n:]),L)==Q(2*k*(N-1),L))
                a=walsh(f)
                ck(sum(t*t for t in a)==L*L)
                for i in range(N):
                    ck(Q(sum(a[s]*a[s] for s in range(L) if s>>i&1),L*L)==Q(edges[i],L))
                # Direct character transform supplies a separate Fourier implementation.
                ck(a==[sum(v*(-1 if (s&y).bit_count()%2 else 1) for y,v in enumerate(f)) for s in range(L)])
                for A in range(1,L-1):
                    if A.bit_count()<2: continue
                    av=[i for i in range(N) if A>>i&1]; bv=[i for i in range(N) if not A>>i&1]
                    def embed(t,inds): return sum(((t>>j)&1)<<i for j,i in enumerate(inds))
                    rows={tuple(f[embed(u,av)|embed(v,bv)] for v in range(1<<len(bv))) for u in range(1<<len(av))}
                    ck(len(rows)>=3); blocks+=1
                rows={tuple(f[x|(z<<n)] for x in range(1<<n)) for z in range(1<<k)}
                ck(len(rows)==3)
    enc=[]
    # Every assignment of a two-bit code to every vertex; no row-constant assumption.
    for k in ((2,) if pilot else (2,3)):
        M=1<<k; cls=[min(z.bit_count(),2) for z in range(M)]
        ee=[(z,z^(1<<i)) for z in range(M) for i in range(k) if not z>>i&1]
        valid=0; best=None; minimizers=0; split_valid=0
        for code in itertools.product(range(4),repeat=M):
            owner={}; ok=True
            for z,c in enumerate(code):
                if c in owner and owner[c]!=cls[z]: ok=False; break
                owner[c]=cls[z]
            if not ok: continue
            valid+=1
            bill=sum((code[u]^code[v]).bit_count() for u,v in ee)
            ck(bill>=k*k)
            if any(len({code[z] for z in range(M) if cls[z]==r})>1 for r in range(3)): split_valid+=1
            if best is None or bill<best: best=bill; minimizers=1
            elif bill==best: minimizers+=1
        ck(best==k*k)
        chain=[0 if z.bit_count()==0 else 1 if z.bit_count()==1 else 3 for z in range(M)]
        ck(sum((chain[u]^chain[v]).bit_count() for u,v in ee)==k*k)
        enc.append(dict(k=k,all_encodings=4**M,valid=valid,split_valid=split_valid,min_boundary_bill=best,minimizers=minimizers,influence=str(Q(best,1<<(k-1)))))
    # Original exact schedule, tested as integer arithmetic, not a floating logarithm.
    for n in range(1,33):
        for m in range(1,33):
            s=n+m; N=8*(s+2)
            ck(s+2<=2**s)
            ck(Q(2*N)*Q(2)**(n-N//4)<=Q(1,2**m))
    result=dict(status='PASS',pilot=pilot,constructions=constructions,proper_blocks=blocks,exact_assertions=checks,encodings=enc,seconds=time.perf_counter()-start,helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    save('PILOT.json' if pilot else 'RESULT.json',result)
    print(json.dumps(result))
if __name__=='__main__':
    (ROOT/'out').mkdir(exist_ok=True)
    run('--pilot' in sys.argv)
