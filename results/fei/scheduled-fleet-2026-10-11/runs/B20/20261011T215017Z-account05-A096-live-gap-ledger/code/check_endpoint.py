from fractions import Fraction as F
from pathlib import Path
import json, time
start=time.perf_counter()
checks=0
def check(v):
    global checks
    assert v
    checks+=1
def walsh(table):
    a=list(table); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                u,v=a[k],a[k+h]; a[k],a[k+h]=u+v,u-v
        h*=2
    return [F(v,len(a)) for v in a]
summary=[]; equality=[]; pairs=0; mass_cases=0
for n in range(3):
    N=1<<n
    tables=[[1 if (mask>>x)&1 else -1 for x in range(N)] for mask in range(1<<N)]
    spectra=[walsh(t) for t in tables]
    maximum=F(-100); minimum=F(100)
    for gi,a in enumerate(spectra):
        for hi,b in enumerate(spectra):
            pairs+=1
            A=sum((u*u for u,v in zip(a,b) if v),F(0))
            c=sum((u*v for u,v in zip(a,b)),F(0))
            corr=F(sum(u*v for u,v in zip(tables[gi],tables[hi])),N)
            check(c==corr)
            jlead=sum((u*u for u,v in zip(a,b) if not v),F(0))
            mlead=sum(((u-v)**2 for u,v in zip(a,b) if v),F(0))
            kappa=jlead-mlead
            check(kappa==2*(c-A))
            check(c*c<=A)
            check(kappa<=F(1,2))
            # Independently express the coefficient through physical mismatch d.
            d=F(sum(u!=v for u,v in zip(tables[gi],tables[hi])),N)
            check(kappa==2*(1-2*d-A))
            maximum=max(maximum,kappa); minimum=min(minimum,kappa)
            if kappa==F(1,2):
                check(all(u==v/2 for u,v in zip(a,b) if v))
                equality.append({'n':n,'G_table_mask':gi,'H_table_mask':hi,'A':str(A),'correlation':str(c)})
            for p in [F(1,8),F(1,32)]:
                masses=[]; q=[]
                for u,v in zip(a,b):
                    r0=((1-p)*v+p*u)**2
                    r1=p*(1-p)*(u-v)**2
                    qt=(1-p)*v*v+p*u*u
                    check(r0+r1==qt)
                    check(r0>=0 and r1>=0)
                    masses += [r0,r1]; q.append(qt)
                check(sum(masses)==1)
                check(sum(q)==1)
                mass_cases+=1
    summary.append({'n':n,'pairs':len(tables)**2,'max_kappa':str(maximum),'min_kappa':str(minimum)})
# Explicit equality witness: G has three +1 values, H constant +1.
a=walsh([-1,1,1,1]); b=walsh([1,1,1,1])
check(a[0]==F(1,2) and b[0]==1)
check(2*(a[0]-a[0]**2)==F(1,2))
result={'helper':'A096-BIASED-FIXED-PAIR-ENDPOINT-v1','ordered_pairs':pairs,'rational_mass_cases':mass_cases,'assertions_passed':checks,'elapsed_seconds':time.perf_counter()-start,'summary':summary,'equality_cases':equality,'logarithmic_sign_certificate':'Analytic asymptotic in REPORT.md; no floating logarithms used'}
out=Path(__file__).resolve().parent.parent/'out/ENDPOINT_CHECK.json'
out.write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='equality_cases'},indent=2))
