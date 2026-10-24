from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,time,math
R=Path(__file__).resolve().parents[1];t0=time.perf_counter();assertions=0
def ck(x):
    global assertions
    assertions+=1;assert x
def fwht(v):
    a=v[:];h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                u,v=a[k],a[k+h];a[k],a[k+h]=u+v,u-v
        h*=2
    return a
real=[]
for N in (4,16,64):
    k=(N.bit_length()-1)//2
    p0=F(1,4);p1=F(1,4*N)
    ck(2*p0+2*N*p1==1)
    IX=N*2*p1;Is=p0+N*p1
    ck(IX==Is==F(1,2))
    conditional=1+k;H=2+k
    ck(conditional>3*IX);ck(H>=3*(IX+Is))
    if N>=16:ck(H>3*(IX+Is))
    real.append({'N':N,'H_exact':H,'H_conditional_exact':conditional,'I_X_exact':str(IX),'I_selector_exact':str(Is),'conditional_ratio_exact':2*conditional})
counts=[];total=0
for n in (1,2,3):
    N=1<<n;count=0
    for mask in range(1<<N):
        if mask.bit_count()!=N//2:continue
        b=[1-2*((mask>>x)&1) for x in range(N)];a=fwht(b);ck(a[0]==0)
        f=[1 if not (x&1) else b[x>>1] for x in range(2*N)];fa=fwht(f)
        p=[F(v*v,(2*N)**2) for v in fa];core=[F(v*v,N*N) for v in a]
        ck(p[0]==p[1]==F(1,4))
        for T in range(1,N):ck(p[2*T]==p[2*T+1]==core[T]/4)
        ck(sum(p)==1);ck(sum(core)==1)
        IX=sum(F((s>>1).bit_count())*v for s,v in enumerate(p));Ib=sum(F(s.bit_count())*v for s,v in enumerate(core))
        ck(IX==Ib/2)
        ck(sum(v for s,v in enumerate(p) if s&1)==F(1,2))
        # Conditional X spectrum given either selector label is identical:
        cond0=[2*p[2*T] for T in range(N)];cond1=[2*p[2*T+1] for T in range(N)]
        ck(cond0==cond1);ck(cond0[0]==F(1,2))
        for T in range(1,N):ck(cond0[T]==core[T]/2)
        # This exact mass partition proves H(cond)=1+H(core)/2.
        count+=1;total+=1
    counts.append({'n':n,'balanced_cores':count})
ck(total==78)
physical=[]
for m in (1,2,3,4):
    M=1<<m;N=M*M;L=4*N
    wp=(M+1)**2;wm=(M-1)**2
    prod=(wp**wp)*(wm**wm)
    ck(L**(8*L)*3**(9*m*L)<=prod**8*(1<<(32*m*L)))
    physical.append({'m':m,'physical_Kstar_certificate':'exact integer-product PASS','equality':m==1})
out={'result':'PASS','assertions':assertions,'runtime_seconds':time.perf_counter()-t0,'matched_real_controls':real,'balanced_cores':counts,'total_balanced_cores':total,'physical_Kstar_certificates':physical}
(R/'out/extension_validation.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
