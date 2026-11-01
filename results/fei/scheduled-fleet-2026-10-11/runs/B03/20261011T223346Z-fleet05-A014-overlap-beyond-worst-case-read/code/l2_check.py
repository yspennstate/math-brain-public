from pathlib import Path
from fractions import Fraction as F
import json, time

RUN=Path(__file__).resolve().parents[1]
# Reuse only definitions, not the search entry point.
exec((RUN/'code/check.py').read_text(encoding='utf-8').split('parser=argparse.ArgumentParser()')[0])
rows=[]
for q in (2,3):
    pts,lines=plane(q); n=len(pts)
    masks=[sum(1<<i for i in line) for line in lines]
    def truth(x): return any(x&m==m for m in masks)
    for j in range(n):
        others=[i for i in range(n) if i!=j]; N=1<<(n-1)
        ids=[l for l,line in enumerate(lines) if j in line]
        actual=[[0]*N for _ in ids]; ideal=[[0]*N for _ in ids]
        for z in range(N):
            x=sum(((z>>i)&1)<<others[i] for i in range(n-1))
            xp=x|(1<<j)
            for k,l in enumerate(ids):
                block=masks[l]^(1<<j)
                ideal[k][z]=int(x&block==block)
            if truth(xp)!=truth(x):
                eligible=[k for k,l in enumerate(ids) if (x&masks[l]==masks[l])!=(xp&masks[l]==masks[l])]
                check(bool(eligible)); actual[min(eligible)][z]=1
        errors=[[u-v for u,v in zip(a,d)] for a,d in zip(ideal,actual)]
        check(all(all(e>=0 for e in row) for row in errors))
        ah=[fwht(row) for row in ideal]; dh=[fwht(row) for row in actual]
        eh=[fwht(row) for row in errors]
        alpha=F(sum(sum(row) for row in actual),N)
        fine_error=F(sum(sum(e*e for e in row) for row in errors),N)
        total_error=F(sum(sum(row[z] for row in errors)**2 for z in range(N)),N)
        D=q*q+q; m=q+1
        check(fine_error<=F(m*D,1<<(2*q)))
        check(total_error<=m*fine_error)
        epsilon=F(0)
        for t in range(N):
            total=sum(row[t] for row in dh); incoherent=sum(row[t]**2 for row in dh)
            epsilon+=max(F(0),F(total*total-4*incoherent,N*N)/alpha)
            if t:
                check(sum(row[t]!=0 for row in ah)<=1)
                error_bill=4*sum(row[t]**2 for row in eh)+2*sum(row[t] for row in eh)**2
                check(total*total<=4*incoherent+error_bill)
        check(epsilon<=alpha+(4*fine_error+2*total_error)/alpha)
        check(epsilon==0) # q=2,3 already have worst-event congestion <4.
        rows.append({'q':q,'j':j,'alpha':str(alpha),'sum_fine_error_norm2':str(fine_error),
                     'total_error_norm2':str(total_error),'epsilon4':str(epsilon)})
check(F(272,65536)<F(1,2))
check(17**4<2*16**4)
check(F(16**4,2**16)==1)
check(F(108+356,5)<93)
out={'helper':'A014-L2-repair-v1','assertions':ASSERTIONS,
     'elapsed_seconds':time.monotonic()-START,'rows':rows,'integer_constant_certificate':'PASS'}
(RUN/'out/l2_check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
