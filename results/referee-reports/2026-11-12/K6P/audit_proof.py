"""Exact audit of every algebraic step in the minimum-potential proof.

The hitting matrices are solved target by target, independently of the
grounded Green formula.  All inequalities below use fractions.Fraction.
"""
from q1_core import *
from pathlib import Path
import random, json, time, resource

start=time.monotonic(); rng=random.Random(48291112)
counts={'networks':0,'merges':0,'entries':0,'minimum_lemmas':0}
family=[]

def energy(w,f,g):
    return sum(w[x][y]*(f[x]-f[y])*(g[x]-g[y])
               for x in range(len(w)) for y in range(x))

def audit(w):
    w=[[Q(z) for z in row] for row in w]; n=len(w)
    x=exact(w); pi=x['pi']; W=x['W']; F=x['F']; T=x['t']
    d=[sum(row) for row in w]
    L=[[(d[i] if i==j else Q(0))-w[i][j] for j in range(n)] for i in range(n)]
    ts=[max(row) for row in F]
    phi=[[ts[i]-F[i][k] for k in range(n)] for i in range(n)]
    for i in range(n):
        assert min(phi[i])==0
        assert sum(pi[k]*phi[i][k] for k in range(n))==ts[i]
        for k in range(n):
            assert sum(L[k][l]*phi[i][l] for l in range(n))==W*(k==i)-d[k]
        for j in range(n): assert energy(w,phi[i],phi[j])==-W*F[i][j]
    for pair in combinations(range(n),2):
        u,v=pair; ix=[k for k in range(n) if k not in pair]
        h=[Q(0)]*n; h[u]=Q(1)
        z=solve([[L[k][l] for l in ix] for k in ix],[w[k][u] for k in ix])
        for k,a in zip(ix,z): h[k]=a
        R=1/sum(w[u][k]*(1-h[k]) for k in range(n))
        p=sum(pi[k]*h[k] for k in range(n))
        bs=blocks(n,pair); y=exact(lump(w,bs)); fidx={k:a for a,b in enumerate(bs) for k in b}
        assert y['t']<2*T
        assert energy(w,h,h)==1/R
        beta=[phi[i][u]-phi[i][v] for i in range(n)]
        assert beta==[W*R*(h[i]-p) for i in range(n)]
        for i in range(n):
            for j in range(n):
                Cij=y['F'][fidx[i]][fidx[j]]
                assert Cij==F[i][j]+beta[i]*beta[j]/(W*R)
                assert Cij<=ts[i]+ts[j]
                counts['entries']+=1
                if beta[i]*beta[j]<=0:
                    assert Cij<=F[i][j]; continue
                sign=Q(1) if beta[i]>0 else Q(-1)
                bi,bj=sign*beta[i],sign*beta[j]
                u1,v1=(u,v) if sign>0 else (v,u)
                f=[a/bi for a in phi[i]]; g=[a/bj for a in phi[j]]
                m=[min(a,b) for a,b in zip(f,g)]
                a=[x-z for x,z in zip(f,m)]; b=[x-z for x,z in zip(g,m)]
                assert min(m)>=0 and all(x*y==0 for x,y in zip(a,b))
                assert f[u1]-f[v1]==g[u1]-g[v1]==m[u1]-m[v1]==1
                assert energy(w,a,b)<=0
                em=energy(w,m,m)
                assert em>=1/R
                middle=energy(w,f,m)+energy(w,g,m)-energy(w,f,g)
                assert middle==em-energy(w,a,b) and em<=middle
                pm=sum(pi[k]*m[k] for k in range(n))
                assert energy(w,f,m)==W/bi*(m[i]-pm)
                assert energy(w,g,m)==W/bj*(m[j]-pm)
                assert energy(w,f,g)==-W*F[i][j]/(bi*bj)
                assert m[i]<=(ts[j]-F[i][j])/bj
                assert m[j]<=(ts[i]-F[i][j])/bi
                upper=W/(bi*bj)*(ts[i]+ts[j]-F[i][j]-(bi+bj)*pm)
                assert middle<=upper
                assert bi*bj/(W*R)<=ts[i]+ts[j]-F[i][j]-(bi+bj)*pm
                assert Cij<=ts[i]+ts[j]-(bi+bj)*pm<ts[i]+ts[j]
                counts['minimum_lemmas']+=1
        counts['merges']+=1
    counts['networks']+=1

for n in (3,4,5,6):
    for rep in range(24):
        w=[[Q(0)]*n for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                z=Q(rng.randint(1,7))*Q(10)**rng.randint(-2,2)
                if i!=j and j!=i+1 and rng.random()<.45: z=Q(0)
                w[i][j]=w[j][i]=z
        audit(w)
    print('exact minimum-potential audit passed n =',n,flush=True)

for t in (2,10,100,1000,10**6):
    # States a,b,u,v.  A four-state tree with two holding leaves.
    w=[[Q(0)]*4 for _ in range(4)]
    w[0][0]=w[1][1]=Q(t-1)
    w[0][2]=w[2][0]=w[1][2]=w[2][1]=Q(1)
    w[2][3]=w[3][2]=Q(t*t); w[3][3]=Q(t**6)
    x=exact(w); y=exact(lump(w,[[0],[1],[2,3]]))
    W=t**6+2*t*t+2*t+2
    A=t**7+t**6+2*t**5+2*t**4+2*t**3+t*t+4*t+2
    B=2*t**7+4*t**3+2*t*t+4*t
    assert x['t']==Q(A,W) and y['t']==Q(B,W)
    assert x['pairs']==[(0,3),(1,3),(3,0),(3,1)]
    assert y['pairs']==[(0,1),(1,0)]
    audit(w)
    family.append({'t':t,'weights':w,'original':x['t'],'quotient':y['t'],
                   'ratio':y['t']/x['t'],'maximizers':x['pairs'],
                   'quotient_maximizers':y['pairs']})
    print('sharp family',t,'T =',x['t'],'That =',y['t'],
          'ratio =',format(float(y['t']/x['t']),'.15g'),flush=True)

result={'counts':counts,'family':family,
        'seconds':time.monotonic()-start,
        'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path('audit_proof_results.json').write_text(json.dumps(serialize(result),indent=2))
print('ALL CHECKS PASSED',counts,'seconds',result['seconds'],
      'maxrss_bytes',result['maxrss_bytes'],flush=True)
