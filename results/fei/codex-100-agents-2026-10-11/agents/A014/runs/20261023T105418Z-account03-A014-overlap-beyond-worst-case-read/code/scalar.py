from pathlib import Path
from fractions import Fraction as F
import math,time,json
R=Path(__file__).resolve().parents[1];start=time.monotonic();count=0;assertions=0
def ck(condition):
    global assertions
    assertions+=1;assert condition
    if time.monotonic()-start>300:raise TimeoutError('Frozen scalar budget')
for n in range(4,129):
    for d in range(n//4):
        delta=n-1-d;a=F(1,48*(n-1));b=delta*a
        ck(b>=F(1,96));ck(delta>=F(3*n,4))
        for k in range(1,n+1):
            r0=max(0,(k-2*d-1)//2)
            lower=math.factorial(r0)*a**(r0+d+1)*b**(2*d+2)
            ck(lower**2*2**(9*n+40*(d+1))*n**(2*(d+1))>=1)
            ck(k//2<=r0+d+1);ck(k-2*r0<=2*d+2)
            count+=1
# Infinite family parameters checked on a fixed, nonadaptive scalar domain.
examples=[]
for m in range(6,129):
    n=2**m;d=n//(m+20)-1
    ck(d>=1);ck((d+1)*(m+20)<=n);ck(n>=4*(d+1))
    examples.append({'m':m,'n':str(n),'d':str(d),'eta':str(F((d+1)*(m+20),n))})
out={'scalar_n_d_k_cases':count,'explicit_family_cases':len(examples),'assertions':assertions,'elapsed_seconds':time.monotonic()-start,'examples':examples}
(R/'out/scalar.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in out.items() if k!='examples'}))
