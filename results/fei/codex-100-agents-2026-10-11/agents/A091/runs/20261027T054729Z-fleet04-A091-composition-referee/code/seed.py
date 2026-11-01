from pathlib import Path
import json,math
ROOT=Path(__file__).resolve().parents[1]
def eta(x): return -x*math.log2(x) if x>0 else 0.
def compose(m,H,I,n,K,J):
    a=(1+n)/2; b=(1+m)/2; v=1-m*m; w=1-n*n; out=(1-m-n-m*n)/2
    E=eta(out*out)+a*a*(H-eta(m*m))+eta(a*a)*v+b*b*(K-eta(n*n))+eta(b*b)*w
    E+=.25*(w*(H-eta(m*m))+v*(K-eta(n*n)))+.5*v*w
    return out,E,a*I+b*J
rows=[]
for orientation in [1,-1]:
    m,H,I=0.,0.,1.
    for d in range(11):
        rows.append(dict(orientation=orientation,depth=d,n=2**d,mean=m,H=H,I=I,ratio=H/I))
        m,H,I=compose(m,H,I,orientation*m,H,I)
(ROOT/'out/SEED_DISCOVERY.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print(json.dumps(sorted(rows,key=lambda r:r['ratio'],reverse=True)[:4]))
