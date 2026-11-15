"""Independent exact audits of the Q2 partial lemmas and search incumbents."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import json,random,time,resource
from fractions import Fraction as Q
from itertools import combinations
import q2_search as s
from q1_core import exact,lump,serialize
begin=time.monotonic();counts=dict(networks=0,partitions=0,merged_source_entries=0,two_pair_entries=0,collinear_entries=0)

def energy(w,f,g):return sum(w[i][j]*(f[i]-f[j])*(g[i]-g[j]) for i in range(len(w)) for j in range(i))

def audit(w,full=True):
    n=len(w);x=exact(w);F=x['F'];pi=x['pi'];W=x['W'];T=x['t'];ts=list(map(max,F))
    phi=[[ts[i]-F[i][j] for j in range(n)] for i in range(n)]
    counts['networks']+=1
    for r in (1,2,3):
        if r>=n:continue
        for bs in s.partitions(n,n-r):
            z=exact(lump(w,bs));h=s.correction(F,bs);assert h==z['F'];counts['partitions']+=1
            f={i:a for a,b in enumerate(bs) for i in b}
            nonsingle=[b for b in bs if len(b)>1]
            if len(nonsingle)==1:
                B=nonsingle[0]
                # h_B is found independently by the exact killed system.
                S=[i for i in range(n) if i not in B];d=list(map(sum,w))
                L=[[((sum(w[i])-w[i][i]) if i==j else -w[i][j]) for j in range(n)] for i in range(n)]
                hv=s.solve([[L[i][j] for j in S] for i in S],[d[i] for i in S]);hit=[Q(0)]*n
                for i,v in zip(S,hv):hit[i]=v
                nu=[(d[i]-sum(L[i][j]*hit[j] for j in range(n)))/W for i in range(n)]
                assert sum(nu)==1 and all(v>=0 for v in nu) and all(nu[i]==0 for i in S)
                mean=sum(a*b for a,b in zip(pi,hit))
                for j in range(n):
                    assert hit[j]-mean==sum(nu[b]*F[j][b] for b in B)
                    assert h[f[B[0]]][f[j]]==hit[j]-mean<=ts[j]
                    counts['merged_source_entries']+=1
            if r==2 and sorted(len(b) for b in nonsingle)==[2,2]:
                for A in nonsingle:
                    for j in range(n):
                        assert h[f[A[0]]][f[j]]<=ts[j]+T
                        counts['two_pair_entries']+=1
            diffs=[(a,b[0]) for b in bs for a in b[1:]]
            betas=[[phi[i][a]-phi[i][b] for a,b in diffs] for i in range(n)]
            for i in range(n):
                for j in range(i,n):
                    bj=betas[j];bi=betas[i]
                    if not any(bj):
                        assert h[f[i]][f[j]]==F[i][j];continue
                    k=next(k for k,v in enumerate(bj) if v);lam=bi[k]/bj[k]
                    if any(a!=lam*b for a,b in zip(bi,bj)):continue
                    if lam<=0:
                        assert h[f[i]][f[j]]<=F[i][j]
                    else:
                        g=[a/lam for a in phi[i]];kk=phi[j];m=list(map(min,g,kk));mean=sum(a*b for a,b in zip(pi,m))
                        assert all(m[a]-m[b]==kk[a]-kk[b] for a,b in diffs)
                        a=[x-y for x,y in zip(g,m)];b=[x-y for x,y in zip(kk,m)]
                        assert all(x*y==0 for x,y in zip(a,b));assert energy(w,a,b)<=0
                        corrjj=h[f[j]][f[j]]-F[j][j]
                        assert energy(w,m,m)>=W*corrjj
                        assert energy(w,m,m)<=energy(w,g,m)+energy(w,kk,m)-energy(w,g,kk)
                        assert h[f[i]][f[j]]<=ts[i]+ts[j]-(1+lam)*mean<=ts[i]+ts[j]
                    counts['collinear_entries']+=1
    return x

rng=random.Random(78112)
for n in range(4,9):
    for trial in range(3):audit(s.random_w(n,rng))
    audit([[Q(1)]*n for _ in range(n)])
    print('AUDITED n',n,counts,flush=True)
with open('q2_best.json') as f:best=json.load(f)
for key,v in best.items():
    w=[[Q(a) for a in row] for row in v['w']];x=exact(w);z=exact(lump(w,v['partition']))
    assert x['t']==Q(v['T']) and z['t']==Q(v['That']) and z['t']/x['t']==Q(v['ratio'])
    assert s.correction(x['F'],v['partition'])==z['F']
# A concrete positive rank-two correction with nonparallel constraint vectors.
w=[[Q(1) if i!=j else Q(i+1) for j in range(7)] for i in range(7)]
bs=[[0,1],[2,3],[4],[5],[6]];x=exact(w);h=s.correction(x['F'],bs);witness=None
for i in range(7):
    for j in range(i+1,7):
        a=[x['F'][i][0]-x['F'][i][1],x['F'][i][2]-x['F'][i][3]]
        b=[x['F'][j][0]-x['F'][j][1],x['F'][j][2]-x['F'][j][3]]
        f={z:k for k,block in enumerate(bs) for z in block}
        if a[0]*b[1]!=a[1]*b[0] and h[f[i]][f[j]]>x['F'][i][j]:
            witness=serialize(dict(w=w,partition=bs,i=i,j=j,beta_i=a,beta_j=b,F=x['F'][i][j],Fhat=h[f[i]][f[j]]));break
    if witness:break
assert witness is not None
result=dict(counts=counts,nonparallel_witness=witness,seconds=time.monotonic()-begin,peak_RSS_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
with open('q2_audit_results.json','w') as f:json.dump(result,f,indent=2)
s.log('Independent exact audit PASSED: '+str(counts)+f'; elapsed {result["seconds"]:.3f}s; RSS {result["peak_RSS_bytes"]} bytes.')
print('ALL Q2 PARTIAL LEMMA AUDITS PASSED',counts,flush=True)
