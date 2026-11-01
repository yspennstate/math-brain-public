"""Fixed finite-domain certificates for an original nonlinear-multiplier ledger."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import hashlib, itertools, json, sys, time

R=Path(__file__).resolve().parents[1]; O=R/'out'; PR=(2,3,5,7); Z=(0,0,0,0)
def save(n,x):
    O.mkdir(exist_ok=True,parents=True)
    (O/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def add(a,b,k=1): return tuple(x+k*y for x,y in zip(a,b))
def scale(a,k): return tuple(k*x for x in a)
def scalar(k): return (256*k,0,0,0)
def fw(t):
    a=list(t); step=1
    while step<len(a):
        for k in range(0,len(a),2*step):
            for j in range(step):
                u,v=a[k+j],a[k+j+step]; a[k+j],a[k+j+step]=u+v,u-v
        step*=2
    return a
def truth(n,code): return [1-2*((code>>x)&1) for x in range(1<<n)]
def encode(t): return sum((v<0)<<x for x,v in enumerate(t))
def restrict(n,code,i,b):
    return encode([v for x,v in enumerate(truth(n,code)) if (x>>i)&1==b])
def basis(vs):
    bs={}
    for v in vs:
        while v:
            j=v.bit_length()-1
            if j in bs:v^=bs[j]
            else:bs[j]=v;break
    return tuple(bs[j] for j in sorted(bs,reverse=True))
def reduce(v,bs):
    for b in bs:
        if v&(1<<(b.bit_length()-1)):v^=b
    return v
@lru_cache(None)
def entropy_hist(n,hist):
    a=[512*n,0,0,0]; N=1<<n
    for v,count in hist:
        if not v:continue
        z=v
        for j,p in enumerate(PR):
            e=0
            while z%p==0:z//=p;e+=1
            a[j]-=512*v*v*count*e//(N*N)
        assert z==1
    return tuple(a)
def ent(w):
    hist={}
    for v in w:hist[abs(v)]=hist.get(abs(v),0)+1
    return entropy_hist(len(w).bit_length()-1,tuple(sorted(hist.items())))
def info(n,code):
    t=truth(n,code); w=fw(t); N=1<<n
    assert sum(v*v for v in w)==N*N
    supp=[s for s,v in enumerate(w) if v]; a=supp[0]; bs=basis(s^a for s in supp)
    inf=tuple(sum(t[x]!=t[x^(1<<i)] for x in range(N)) for i in range(n))
    return dict(t=t,w=w,H=ent(w),a=a,bs=bs,r=len(bs),inf=inf,
                children=tuple(tuple(restrict(n,code,i,b) for b in (0,1)) for i in range(n)))
@lru_cache(None)
def small(n,code): return info(n,code)
def log_interval(p):
    k=p.bit_length()-1; u=F(p,1<<k); t=(u-1)/(u+1)
    def series(t):
        s=F(0); v=t
        for j in range(64):s+=2*v/(2*j+1);v*=t*t
        return s,s+2*v/(129*(1-t*t))
    lo,hi=series(t); l2,h2=series(F(1,3));return lo+k*l2,hi+k*h2
Q=1<<100
LOGS=tuple((int(lo*Q),-((-hi*Q).numerator//(-hi*Q).denominator)) for lo,hi in map(log_interval,PR))
@lru_cache(None)
def nonneg(a):
    if a==Z:return True
    lo=sum(v*LOGS[j][0 if v>=0 else 1] for j,v in enumerate(a))
    hi=sum(v*LOGS[j][1 if v>=0 else 0] for j,v in enumerate(a))
    assert lo>0 or hi<0,('unresolved exact sign',a,lo,hi)
    return lo>0
def freeze():
    save('spec.json',dict(helper_version='A017-fixed-multiplier-rank-ledger-v1',helper_sha256=sha(Path(__file__)),
      family='ALL Boolean f,c on3 physical bits, including queries in multiplier; ALL Boolean4-bit f with ONE fixed AND2 sign multiplier on original bits2,3 and query bits0,1',
      parameter_domain='n3:256*256=65536 ordered pairs and all3 queries; n4:65536 roots and all9 stopped two-query policies; translated defects m=2..8',
      case_count=dict(three_bit_pairs=65536,three_bit_queries=196608,four_bit_roots=65536,four_bit_stopped_policies=589824,defect_family_rows=7),
      symmetry='No quotient in n3. n4 uses ONE specified nonlinear multiplier, not all multipliers. Constant/character and bent endpoints retained separately.',
      arithmetic='Integer Walsh, integer prime-log entropy vectors with common denominator256, exact rational atanh64 logarithm bounds rounded outward at100bits, exact physical edge counts',
      pilot='n3 first8 f and all256 c; n4 first64 roots/all9 policies; m=2..4; fixed domain no growth',
      memory_estimate_MB=100,max_runtime_seconds=300,pilot_max_runtime_seconds=60,
      proof_failures_checked=['coherent coset mass preservation','affine rank monotonicity at BOTH children','nonnegative potential including endpoints','rank refund sign','queried influence transfer when c depends on query','all full terminal entropies','false universal original-influence admission']))
    print('FROZEN:65536 three-bit pairs;65536 four-bit roots;100MB;300s')
def run(pilot):
    sp=json.loads((O/'spec.json').read_text(encoding='utf-8'));assert sp['helper_sha256']==sha(Path(__file__))
    start=time.monotonic(); checks=0; pairs=queries=policies=0; maxrank=0
    for f in range(8 if pilot else 256):
        a=small(3,f)
        for c in range(256):
            b=small(3,c); g=small(3,f^c); E=add(g['H'],a['H'],-1); phi=add(scalar(b['r']),E)
            assert nonneg(phi) and nonneg(add(scalar(2*b['r']),phi,-1));checks+=2
            before={}; after={}; shift=reduce(b['a'],b['bs'])
            for s in range(8):
                q=reduce(s,b['bs']);before[q]=before.get(q,0)+a['w'][s]**2
                q=reduce(s,b['bs'])^shift;after[q]=after.get(q,0)+g['w'][s]**2
            assert before==after;checks+=1
            for i in range(3):
                ach=[small(2,v) for v in a['children'][i]];bch=[small(2,v) for v in b['children'][i]];gch=[small(2,v) for v in g['children'][i]]
                assert all(v['r']<=b['r'] for v in bch);checks+=2
                es=[add(x['H'],y['H'],-1) for x,y in zip(gch,ach)]
                ph=[add(scalar(v['r']),e) for v,e in zip(bch,es)]
                omega2=add(add(scale(E,2),es[0],-1),es[1],-1)
                drift2=add(add(scale(phi,2),ph[0],-1),ph[1],-1)
                refund2=2*b['r']-sum(v['r'] for v in bch)
                assert refund2>=0 and add(drift2,scalar(refund2),-1)==omega2;checks+=2
                assert all(g['children'][i][v]==(a['children'][i][v]^b['children'][i][v]) for v in (0,1));checks+=2
                transfer=sum(a['t'][x]*a['t'][x^(1<<i)] for x in range(8) if b['t'][x]!=b['t'][x^(1<<i)])
                assert g['inf'][i]-a['inf'][i]==transfer;checks+=1
                queries+=1
            pairs+=1;maxrank=max(maxrank,b['r'])
        if f%16==0:assert time.monotonic()-start<(60 if pilot else 300)
    ccode=encode([1-2*(((x>>2)&1)&((x>>3)&1)) for x in range(16)])
    for f in range(64 if pilot else 65536):
        a=info(4,f);g=info(4,f^ccode);E=add(g['H'],a['H'],-1);phi=add(scalar(2),E)
        assert nonneg(phi) and nonneg(add(scalar(4),phi,-1));checks+=2
        for i in (0,1):
            other=1-i; ai=[small(3,v) for v in a['children'][i]];gi=[small(3,v) for v in g['children'][i]]
            assert a['inf'][i]==g['inf'][i];checks+=1
            es=[add(gg['H'],aa['H'],-1) for aa,gg in zip(ai,gi)]
            ds=[add(scale(E,2),add(es[0],es[1]),-1)]
            for stopmask in range(4):
                leafE=Z; local=scale(ds[0],2); leafHg=Z; leafHf=Z
                for b in (0,1):
                    if stopmask&(1<<b):
                        leafE=add(leafE,scale(es[b],2));leafHg=add(leafHg,scale(gi[b]['H'],2));leafHf=add(leafHf,scale(ai[b]['H'],2))
                    else:
                        jj=other if other<i else other-1
                        ae=[small(2,v)['H'] for v in ai[b]['children'][jj]];ge=[small(2,v)['H'] for v in gi[b]['children'][jj]]
                        e=add(add(ge[0],ge[1]),add(ae[0],ae[1]),-1)
                        leafE=add(leafE,e);leafHg=add(leafHg,add(ge[0],ge[1]));leafHf=add(leafHf,add(ae[0],ae[1]))
                        local=add(local,add(scale(es[b],2),e,-1))
                assert local==add(scale(E,4),leafE,-1);checks+=1
                assert leafE==add(leafHg,leafHf,-1);checks+=1
                phileaf=add(scalar(8),leafE)
                assert local==add(scale(phi,4),phileaf,-1);checks+=1
                policies+=1
        # Ninth policy stops at root and retains both complete original functions.
        assert add(phi,phi,-1)==Z;policies+=1;checks+=1
        if f%512==0:assert time.monotonic()-start<(60 if pilot else 300)
    family=[]
    for m in range(2,5 if pilot else 9):
        n=m+1;N=1<<n; f=[1]*N;f[1]=-1;g=[1]*N;g[0]=-1;c=[-1 if x>>1==0 else 1 for x in range(N)]
        assert [u*v for u,v in zip(f,c)]==g
        assert fw(f)[0]==N-2 and fw(g)[0]==N-2
        assert sorted(v*v for v in fw(f))==sorted(v*v for v in fw(g))
        influence=sum(sum(g[x]!=g[x^(1<<i)] for x in range(N)) for i in range(n))
        assert F(influence,N)==F(m+1,1<<m)
        csmall=[-1]+[1]*((1<<m)-1);w=fw(csmall);supp=[s for s,v in enumerate(w) if v];a0=supp[0]
        assert len(basis(s^a0 for s in supp))==m
        ratio=F(m*(1<<m),m+1);assert ratio>=1<<(m-1)
        family.append(dict(m=m,potential=m,actual_influence=str(F(influence,N)),potential_over_actual_I=str(ratio),actual_query_correction=0));checks+=6
    result=dict(status='PASS',pilot=pilot,three_bit_pairs=pairs,three_bit_queries=queries,four_bit_roots=64 if pilot else 65536,
      stopped_policies=policies,assertions=checks,max_rank_seen=maxrank,defect_family=family,
      sign_cache=nonneg.cache_info()._asdict(),elapsed_seconds=time.monotonic()-start,
      scope='Exact finite verification plus separate analytic all-dimensional proof; author verification, independent review pending')
    save('pilot.json' if pilot else 'certificate.json',result)
    print(json.dumps({k:result[k] for k in ['status','pilot','three_bit_pairs','three_bit_queries','four_bit_roots','stopped_policies','assertions','elapsed_seconds']}))
if __name__=='__main__':
    if '--freeze' in sys.argv:freeze()
    else:run('--pilot' in sys.argv)
