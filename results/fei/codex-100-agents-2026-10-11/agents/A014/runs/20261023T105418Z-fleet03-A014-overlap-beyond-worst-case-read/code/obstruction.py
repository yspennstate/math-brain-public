from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(x):
    global checks
    checks+=1;assert x
    if time.monotonic()-start>60:raise TimeoutError('Frozen obstruction budget')
for r in range(1,129):
    n=8*r;d=2*r-2;delta=6*r+1;Zlower=F(n*delta,32*(n-1));mass=F(1,48*(n-1))**r
    ck(n>=4*(d+1));ck(delta>=F(3*n,4));ck(6*r+(-1)**r>0)
    if r>=8:ck(Zlower>=1);ck(mass<=F(1,n)**r)
rows=[]
for r in (1,2):
    n=8*r;A=(1<<(2*r))-1;C=[]
    edges=[(u,v) for u in range(n) for v in range(u+1,n) if u>=2*r or v>=2*r or (u//2==v//2)]
    em=[(1<<u)|(1<<v) for u,v in edges]
    for x in range(1<<n):
        actual=int(not any(x&e==e for e in em))
        # Independent product-sector description: B empty, or A empty and B a singleton.
        sectors=int((x&~A==0 and all(x&(3<<(2*j))!=(3<<(2*j)) for j in range(r))) or (x&A==0 and (x&~A).bit_count()==1))
        ck(actual==sectors);C.append(actual)
    ck(sum(C)==3**r+6*r)
    coefficient=F(sum(c*(-1 if (x&A).bit_count()%2 else 1) for x,c in enumerate(C)),1<<n)
    ck(coefficient==F(6*r+(-1)**r,1<<n))
    boundary=sum(C[x]!=C[x^(1<<i)] for x in range(1<<n) for i in range(n))//2
    s=F(sum(C),1<<n);mu=F(sum(x.bit_count()*c for x,c in enumerate(C)),sum(C));I=F(boundary,1<<(n-1))
    ck(I==2*s*(n-2*mu));rows.append({'r':r,'n':n,'Chat_A':str(coefficient),'I':str(I),'s':str(s)})
out={'scalar_cases':128,'actual_Boolean_inputs':2**8+2**16,'assertions':checks,'elapsed_seconds':time.monotonic()-start,'rows':rows}
(R/'out/obstruction.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
