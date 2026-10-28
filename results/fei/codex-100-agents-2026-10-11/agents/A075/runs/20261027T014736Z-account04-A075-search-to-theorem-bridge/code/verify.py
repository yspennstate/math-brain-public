from pathlib import Path
from fractions import Fraction as Q
import json, time, sys, hashlib

ROOT = Path(__file__).resolve().parents[1]

def walsh(t):
    a = list(t)
    s = 1
    while s < len(a):
        for start in range(0, len(a), 2*s):
            for j in range(start, start+s):
                u,v = a[j],a[j+s]
                a[j],a[j+s] = u+v,u-v
        s *= 2
    return a

def rows(t,N,B):
    inside=[i for i in range(N) if B>>i&1]
    outside=[i for i in range(N) if not B>>i&1]
    def embed(v,ids):
        return sum(((v>>j)&1)<<i for j,i in enumerate(ids))
    return {tuple(t[embed(a,inside)|embed(b,outside)] for b in range(1<<len(outside))) for a in range(1<<len(inside))}

def witness(t,n,m,B):
    N=n+m
    pad=[i for i in range(n,N) if B>>i&1]
    old=[i for i in range(n) if B>>i&1]
    outside=[i for i in range(N) if not B>>i&1]
    if len(pad)>=2:
        assignments=[0,1<<pad[0],(1<<pad[0])|(1<<pad[1])]
        columns=[0,1<<outside[0]]
        case='two-padding'
    elif len(pad)==1:
        otherpad=[i for i in range(n,N) if not B>>i&1]
        assert len(otherpad)>=2 and old
        assignments=[0,1<<pad[0],1<<old[0],(1<<pad[0])|(1<<old[0])]
        columns=[0,1<<otherpad[0],(1<<otherpad[0])|(1<<otherpad[1])]
        case='one-padding'
    else:
        assert len(old)>=2
        assignments=[0,1<<old[0],(1<<old[0])|(1<<old[1])]
        columns=[0,1<<n,(1<<n)|(1<<(n+1))]
        case='no-padding'
    rs={tuple(t[a|b] for b in columns) for a in assignments}
    assert len(rs)>=3,(n,m,B,case,rs)
    return case

def verify(n,mask,m, main):
    N=n+m
    f=[1 if mask>>x&1 else -1 for x in range(1<<n)]
    t=[f[x&((1<<n)-1)]*(-1 if x.bit_count()<=1 else 1) for x in range(1<<N)]
    checks=0; cases={}; rowcounts=[]
    for B in range(1, (1<<N)-1):
        if B.bit_count()<2:continue
        count=len(rows(t,N,B));rowcounts.append(count)
        if main:
            assert count>=3,(n,mask,m,B,count)
            c=witness(t,n,m,B);cases[c]=cases.get(c,0)+1;checks+=2
    a=walsh(t); af=walsh(f)
    assert sum(v*v for v in a)==len(t)**2;checks+=1
    assert all(a[S]==sum(v*(-1 if (x&S).bit_count()%2 else 1) for x,v in enumerate(t)) for S in range(1<<N));checks+=1
    I=Q(sum(S.bit_count()*a[S]**2 for S in range(1<<N)),len(t)**2)
    If=Q(sum(S.bit_count()*af[S]**2 for S in range(1<<n)),len(f)**2)
    edges=Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t)) for i in range(N)),len(t))
    assert I==edges;checks+=1
    delta=Q(N+1,1<<N)
    assert abs(I-If)<=2*N*delta;checks+=1
    # L2 coefficient perturbation and total-variation estimate, squared exactly.
    diff=sum((Q(a[S],len(t))-(Q(af[S],len(f)) if S<(1<<n) else 0))**2 for S in range(1<<N))
    assert diff==4*delta;checks+=1
    tv=sum(abs(Q(a[S]**2,len(t)**2)-(Q(af[S]**2,len(f)**2) if S<(1<<n) else 0)) for S in range(1<<N))/2
    assert tv*tv<=4*delta;checks+=1
    if main:
        # Two fixed padding bits equal one recover the original complete f.
        assert all(t[x|(1<<n)|(1<<(n+1))]==f[x] for x in range(1<<n));checks+=1
    return {'n':n,'mask':mask,'m':m,'checks':checks,'proper_blocks':len(rowcounts),'min_rows':min(rowcounts,default=None),'witness_cases':cases,'I':str(I),'I_original':str(If),'delta':str(delta),'tv':str(tv),'prime':all(c>=3 for c in rowcounts)}

def run(mode):
    start=time.monotonic();results=[]
    domain=range(3) if mode in ['pilot','boundary'] else range(4)
    for n in domain:
        for mask in range(1<<(1<<n)):
            for m in (range(3) if mode=='boundary' else [3]):
                assert time.monotonic()-start<55,'frozen runtime cap'
                results.append(verify(n,mask,m,mode!='boundary'))
        (ROOT/'out'/f'{mode.upper()}_PARTIAL.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
    out={'mode':mode,'circuits':len(results),'checks':sum(r['checks'] for r in results),'proper_block_checks':sum(r['proper_blocks'] for r in results),'elapsed_seconds':time.monotonic()-start,'all_prime':all(r['prime'] for r in results),'results':results}
    (ROOT/'out'/f'{mode.upper()}.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='results'}))

if __name__=='__main__':run(sys.argv[1])
