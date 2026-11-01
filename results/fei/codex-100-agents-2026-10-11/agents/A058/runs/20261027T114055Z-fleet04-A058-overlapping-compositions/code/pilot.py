import json,math
from fractions import Fraction as Q
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def walsh(a):
    a=a[:];h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
        h*=2
    return a
def profile(a):
    N=len(a);w=walsh(a);H=sum(-t*t/(N*N)*math.log2(t*t/(N*N)) for t in w if t)
    return H,sum(Q(t*t,N*N)*i.bit_count() for i,t in enumerate(w))
g0=[-1 if x==0 else 1 for x in range(8)]
g1=[-1 if x%4==0 else 1 for x in range(8)]
g=g0+g1;H,I=profile(g);H0,I0=profile(g0);H1,I1=profile(g1)
p=Q(sum(x!=y for x,y in zip(g0,g1)),8);D=H-(H0+H1)/2;A=Q(9,2);J=(I0+I1)/2
R=float(A*I);M=float(A*J);L=max(0,M-R+D)
uniform=L/M*(H0+H1)/2
order=sorted([(H0/float(A*I0),float(A*I0)/2,H0/2,0),(H1/float(A*I1),float(A*I1)/2,H1/2,1)])
left=L;optimal=0
for ratio,cap,bill,i in order:
    used=min(left,cap);optimal+=used*ratio;left-=used
out=dict(H=H,I=str(I),children=[dict(H=H0,I=str(I0)),dict(H=H1,I=str(I1))],p=str(p),D=D,local_excess=D-float(A*p),required_influence_principal_liquidation=L,uniform_stopped_entropy=uniform,optimal_stopped_entropy=optimal,improvement=uniform-optimal)
(root/'out').mkdir(exist_ok=True);(root/'out/PILOT.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
