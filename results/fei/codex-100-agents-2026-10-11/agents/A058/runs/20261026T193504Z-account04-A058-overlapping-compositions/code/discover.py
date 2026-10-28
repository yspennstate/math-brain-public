import json, math, time
from fractions import Fraction as Q
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def ent(ps):
    return sum(-float(x)*math.log2(float(x)) for x in ps if x)
def walsh(a):
    a=a[:]; h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return a
rows=[]; start=time.monotonic()
for n in range(4,11):
    N=1<<n; k=round(N*(math.sqrt(5)-1)/2)
    w=walsh([-1 if x<k else 1 for x in range(N)])
    p=Q(k,N); H=ent([Q(x*x,N*N) for x in w]); I=sum(Q(x*x,N*N)*j.bit_count() for j,x in enumerate(w))
    for d in range(9):
        rows.append(dict(n=n,k=k,depth=d,variables=n*(1<<d),H=H,I=float(I),ratio=H/float(I),excess=H-6*float(I)))
        v=4*p*(1-p); m=1-2*p*p
        H=ent([m*m,p*p*v,p*p*v,v*v/4])+2*float(p)*(H-ent([(1-2*p)**2,v]))
        I=2*p*I; p=1-p*p
assert len(rows)==63
out={'elapsed_s':time.monotonic()-start,'rows':rows,'best':max(rows,key=lambda r:r['ratio'])}
(root/'out').mkdir(exist_ok=True)
(root/'out'/'DISCOVERY.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out['best']))
