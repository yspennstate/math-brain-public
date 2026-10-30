"""Independent v1 compressed exact controller/mean overlap check."""
from fractions import Fraction as Q
from pathlib import Path
import itertools,json,time
root=Path(__file__).resolve().parents[1];(root/'out').mkdir(exist_ok=True)
start=time.monotonic();count=0
def w(v):
    # Direct character sums; independent of the butterfly checker.
    return [sum(Q(z)*(-1 if (x&s).bit_count()%2 else 1) for x,z in enumerate(v))/len(v) for s in range(len(v))]
for r in range(0,7):
    if time.monotonic()-start>55:raise RuntimeError('frozen 55-second cap')
    a=Q(1,2**r)
    av=[Q(x==0) for x in range(1<<r)]
    ya=w([y*A for y in [0,1] for A in av])
    yn=w([y*(1-A) for y in [0,1] for A in av])
    ky=w([1-y*A for y in [0,1] for A in av])
    assert sum(abs(x*y) for x,y in zip(ya,yn))==a*(1-a);count+=1
    assert sum(abs(x*y) for x,y in zip(ky,yn))==(1-a)*(1+a)/2;count+=1
    assert yn[0]==(1-a)/2;count+=1
grid=[Q(i,4) for i in range(-4,5)]
for a in [Q(0),Q(1,2),Q(1,4),Q(1,8),Q(1,64)]:
    for m,n,ell in itertools.product(grid,repeat=3):
        T=1-m*n;V=1-m*m
        assert abs(n-m)<=T;assert V<=2*T;count+=2
        M=(1-a)*m+a*ell
        bound=(1-a)*(1+a)*V/2+abs(n-m)*((1-a)*max(abs(m),abs(M))/2+a*(1-a)*abs(ell-m)/2)
        assert bound<=Q(5,2)*(1-a)*T;count+=1
out={'status':'PASS','exact_assertions':count,'controller_widths':[0,6],
     'mean_grid':'all triples in {-1,-3/4,...,1}; a=0,1/2,1/4,1/8,1/64',
     'arithmetic':'Fraction; direct Fourier character sums, no Walsh butterfly',
     'elapsed_seconds':time.monotonic()-start}
(root/'out/overlap.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
