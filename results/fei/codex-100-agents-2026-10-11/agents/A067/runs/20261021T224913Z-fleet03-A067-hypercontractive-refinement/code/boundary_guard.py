from fractions import Fraction as Q
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
def ln(x):
    z=(x-1)/(x+1)
    s=sum((2*z**(2*k+1)/(2*k+1) for k in range(30)),Q(0))
    return s,s+2*z**61/(61*(1-z*z))
ln2=ln(Q(2))
def log2(x):
    k=0
    while x<1:x*=2;k-=1
    while x>=2:x/=2;k+=1
    a,b=ln(x);return k+a/ln2[1],k+b/ln2[0]
v=[]
for x in range(16):
    y=x&3;w=(x>>2)&1;z=1-2*((x>>3)&1)
    b=-1 if y==3 else 1
    v.append(b+(z-1 if y==0 and w==0 else 0))
coeff=[sum(v[x]*(-1)**((x&s).bit_count()%2) for x in range(16)) for s in range(16)]
prob=[Q(a*a,256) for a in coeff]
assert sum(prob)==1
lo=hi=Q(0)
for p in prob:
    if p:
        a,b=log2(1/p);lo+=p*a;hi+=p*b
ix=Q(sum(v[x]!=v[x^(1<<j)] for x in range(16) for j in range(3)),16)
assert ix==Q(11,8)
reserve=(2*ix-hi,2*ix-lo)
assert reserve[1]<0
(R/'out/BOUNDARY_GUARD.json').write_text(json.dumps({'status':'PASS','m':1,'physical_core_influence':str(ix),'remaining_bank_lower':str(reserve[0]),'remaining_bank_upper':str(reserve[1]),'interpretation':'m>=2 is necessary for the stated no-query-allowance bank payment; not an FEI counterexample.'},indent=2),encoding='utf-8')
print('PASS: excluded m1 has S2-Dz<0; exact rational interval saved.')
