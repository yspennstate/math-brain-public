from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1]
start=time.monotonic();out=[]
def convolution(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
for w in [4,5]:
    m=1<<w;n=w*m;q=Q(1,m);s=1-q;e=2*q*s**(m-1);c=2*s**m-1;I=n*e
    factor=[s]+[Q(comb(w,j))*q*q/s for j in range(1,w+1)]
    assert sum(factor)==1;checks=1
    nu=[Q(1)];outside=[Q(1)]
    for block in range(m):
        if block==m-1:outside=nu[:]
        nu=convolution(nu,factor)
    U=[Q(comb(w-1,j),1<<(w-1)) for j in range(w)]
    mu=convolution(outside,U)
    W=[c*c]+[4*s**m*x for x in nu[1:]]
    r=[(1-Q(j,n))*W[j]+Q(j+1,n)*W[j+1] for j in range(n)]
    assert sum(W)==sum(mu)==sum(r)==1;checks+=3
    assert sum(j*W[j] for j in range(n+1))==I;checks+=1
    assert mu==[Q(j+1)*W[j+1]/I for j in range(n)];checks+=1
    assert mu[0]==e and sum(j*mu[j] for j in range(n))==w-Q(1,2);checks+=2
    assert r[0]>=Q(1,16)>=e;checks+=2
    for j in range(1,n):
        assert mu[j]<=(2*q/s+2*s*j)*nu[j];checks+=1
        if j<=n//2:assert mu[j]<=4*(j+1)*r[j];checks+=1
        assert r[j]>=e*mu[j];checks+=1
    assert sum(mu[n//2+1:])<=Q(2,m);checks+=1
    out.append({'w':w,'dimension':n,'degree_packets':n,'exact_assertions':checks})
ans={'cases':out,'assertions':sum(x['exact_assertions'] for x in out),'runtime_seconds':time.monotonic()-start}
assert ans['runtime_seconds']<60
(R/'out/DEGREE_REVIEW.json').write_text(json.dumps(ans,indent=2)+'\n')
print(json.dumps(ans))
