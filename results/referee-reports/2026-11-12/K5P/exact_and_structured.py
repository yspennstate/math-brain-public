"""Exact random tests, rank-one identity audit, and structured families.

Every numerical quantity used for a conclusion here is a Fraction.
"""
from q1_core import *
from pathlib import Path
import random, json, time, resource

start=time.monotonic(); rng=random.Random(202611122145)
stats=[]; best_records=[]; identity_count=0; exact_networks=0

def check(w,label,identity=False):
    global identity_count,exact_networks
    w=[[Q(v) for v in row] for row in w]
    n=len(w); x,allpairs=exact_scan(w); exact_networks+=1
    if identity:
        d=list(map(sum,w)); W=sum(d)
        L=[[(d[i] if i==j else Q(0))-w[i][j] for j in range(n)] for i in range(n)]
        for pair in combinations(range(n),2):
            u,v=pair; ix=[k for k in range(n) if k not in pair]
            h=[Q(0)]*n; h[u]=Q(1)
            z=solve([[L[i][j] for j in ix] for i in ix],[w[i][u] for i in ix])
            for i,a in zip(ix,z): h[i]=a
            R=1/sum(w[u][k]*(1-h[k]) for k in range(n))
            p=sum(x['pi'][k]*h[k] for k in range(n))
            bs=blocks(n,pair); y=exact(lump(w,bs)); f={k:a for a,b in enumerate(bs) for k in b}
            for i in range(n):
                for j in range(n):
                    assert y['F'][f[i]][f[j]]==x['F'][i][j]+W*R*(h[i]-p)*(h[j]-p)
                    identity_count+=1
            assert all(y['F'][a][-1]<=x['t'] for a in range(n-1))
    return {'label':label,'n':n,'ratio':allpairs[0][0],'pair':allpairs[0][1],
            't':x['t'],'that':allpairs[0][2],'weights':w}

for n in (3,4,5,6):
    best=None
    for rep in range(100):
        w=[[Q(0)]*n for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                z=Q(rng.randint(1,9))*Q(10)**rng.randint(-3,3)
                if i!=j and j!=i+1 and rng.random()<.4: z=Q(0)
                w[i][j]=w[j][i]=z
        a=check(w,f'random-{n}-{rep}',identity=rep<10)
        if best is None or a['ratio']>best['ratio']: best=a
    best_records.append(best)
    print('exact random',n,'networks',100,'best',float(best['ratio']),'pair',best['pair'],flush=True)

families=[]
for n in (3,4,5,6):
    for t in (2,10,100):
        for kind in ('path','star','two-cliques','cycle'):
            w=[[Q(0)]*n for _ in range(n)]
            def edge(i,j,z): w[i][j]=w[j][i]=Q(z)
            if kind=='path':
                for i in range(n-1): edge(i,i+1,t**i)
            elif kind=='star':
                for i in range(n-1): edge(i,n-1,t**i)
            elif kind=='cycle':
                for i in range(n): edge(i,(i+1)%n,t**i)
            else:
                k=n//2
                for i in range(n):
                    for j in range(i+1,n):
                        if (i<k)==(j<k): edge(i,j,t**2)
                edge(k-1,k,1)
            for i in range(n): w[i][i]=Q((t-1)*max(1,sum(w[i])))
            w[-1][-1]+=Q(t**(n+3))
            a=check(w,f'{kind}-n{n}-t{t}')
            families.append(a)
        # Parallel branches between light and heavy hubs, includes K4 seed.
        if n>=4:
            w=[[Q(0)]*n for _ in range(n)]
            u,v=n-2,n-1
            for i in range(n-2):
                w[i][u]=w[u][i]=Q(1); w[i][v]=w[v][i]=Q(t)
                w[i][i]=Q(t*t-1)
            w[v][v]=Q(t**6)
            families.append(check(w,f'parallel-leaves-n{n}-t{t}'))

# The supplied fork comb, reconstructed here without executing its top-level
# loop or its obsolete Windows sys.path insertion.
def fork(N,t):
    r=t**3; al=t
    names=['a','b','c']+[f'z{k}' for k in range(N+1)]+[f'y{k}' for k in range(N)]
    ix={s:i for i,s in enumerate(names)}; n=len(names); w=[[Q(0)]*n for _ in range(n)]
    def add(a,b,z):
        i,j=ix[a],ix[b]; w[i][j]+=Q(z)
        if i!=j: w[j][i]+=Q(z)
    add('a','z0',1); add('a','a',t-1)
    for k in range(N):
        add(f'z{k}',f'z{k+1}',r**(k+1)); add(f'y{k}',f'z{k+1}',al*r**(k+1))
        add(f'y{k}',f'y{k}',(t-1)*al*r**(k+1))
    add('b',f'z{N}',al*r**(N+1)); add('b','b',(t-1)*al*r**(N+1))
    add('c',f'z{N}',r**(N+2)); add('c','c',(N+2)*r**(N+4))
    return w

for N in (0,1,2):
    for t in (2,10,100): families.append(check(fork(N,t),f'fork-N{N}-t{t}'))
for kind in ('path','star','two-cliques','cycle','parallel-leaves','fork'):
    a=max((a for a in families if a['label'].startswith(kind)),key=lambda a:a['ratio'])
    print('structured best',kind,a['label'],float(a['ratio']),a['pair'],flush=True)
assert all(a['ratio']<=2 for a in best_records+families)
Path('exact_and_structured_results.json').write_text(json.dumps(serialize(
    {'random_best':best_records,'families':families,'identity_entries':identity_count,
     'networks':exact_networks}),indent=2))
print('networks',exact_networks,'identity entries',identity_count,
      'seconds',time.monotonic()-start,'maxrss_bytes',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,flush=True)
