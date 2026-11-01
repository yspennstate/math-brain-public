"""Frozen general guard v1; exact Walsh and physical-edge certificate."""
from pathlib import Path
import itertools,json,time
root=Path(__file__).resolve().parents[1];(root/'out').mkdir(exist_ok=True)
start=time.monotonic();count=zero=0
def fw(v):
    w=list(v);h=1
    while h<len(w):
        for j in range(0,len(w),h*2):
            for k in range(j,j+h):
                x,y=w[k],w[k+h];w[k],w[k+h]=x+y,x-y
        h*=2
    return w
for r,s in [(2,1),(1,2)]:
    for at,pt,ut,vt,gt in itertools.product(range(1<<(1<<r)),range(1<<(1<<s)),range(4),range(4),range(4)):
        if time.monotonic()-start>55:raise RuntimeError('55-second frozen cap')
        n=r+s+2+3;N=1<<n;bit=1<<(r+s);v=[]
        for x in range(N):
            A=(at>>(x&((1<<r)-1)))&1
            P=(pt>>((x>>r)&((1<<s)-1)))&1
            B=P*((x>>(r+s))&1);Y=(x>>(r+s+1))&1
            u=2*((ut>>((x>>(r+s+2))&1))&1)-1
            z=2*((vt>>((x>>(r+s+3))&1))&1)-1
            g=2*((gt>>((x>>(r+s+4))&1))&1)-1
            v.append(g if not Y else u if A else z if B else g)
        w=fw(v)
        cross=sum(abs(w[j]*w[j|bit]) for j in range(N) if not j&bit)
        d=sum(w[j|bit]**2 for j in range(N) if not j&bit)
        assert d==N*sum(v[x]!=v[x^bit] for x in range(N))
        assert 2*cross*(1<<r) <= (8*(1<<r)+8*at.bit_count())*d
        count+=1;zero+=d==0
result={'status':'PASS','cases':count,'exact_assertions':2*count,'zero_influence_cases':zero,
        'elapsed_seconds':time.monotonic()-start,'arithmetic':'integer Walsh; rational8+8a compared by cross multiplication'}
(root/'out/guard.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
