from pathlib import Path
from fractions import Fraction as F
import runpy,json,time
RUN=Path(__file__).resolve().parents[1]
H=runpy.run_path(str(RUN.parent/'20261014T035704Z-fleet05-A021-rare-core-asymptotics/code/check.py'))
ln,ent,add,sub,mul,total,LN2=[H[x] for x in ('ln','ent','add','sub','mul','total','LN2')]
start=time.monotonic(); rows=[]
with (RUN/'out/owner_rows.jsonl').open('w',encoding='utf-8') as out:
    for m in range(4,33,2):
        n=1<<m; delta=F(1,n); root=F(1,1<<(m//2))
        he=total((ent(root-2*delta*t),F(n+(1<<(m//2))*t,2)) for t in (-1,1))
        ht=add(mul(LN2,F(3*m,4)),mul(he,F(1,4)))
        it=1+F(m,2)+F(m-1,2)*delta
        for k in (0,m):
            p=F(1,1<<k)
            activation=(F(0),F(0)) if not k else add(mul(LN2,(4*p-2*p*p)*k),mul(ln(1-p),-2*(1-p)**2))
            ht_activated=add(mul(ht,p),activation); it_activated=p*(it+k)
            s8=sub(mul(LN2,8*it_activated),ht_activated)
            lower=p*(3*m+1+4*k)
            assert s8[0]>=lower*LN2[1]
            bankroot=p*(3*m+2+3*k)*delta/4; remain=p*(3*m-1+3*k)*delta/4
            assert bankroot-remain==3*p*delta/4
            assert remain<=delta*lower/4
            excess_cap=p*m*delta/2
            assert excess_cap<=delta*lower/6
            assert F(5,12)*delta<=F(5,192)
            row=dict(m=m,activation_width=k,p=str(p),S8_nat_interval=[str(x) for x in s8],S8_lower_bits=str(lower),Rroot=str(bankroot),Rremain=str(remain),release=str(bankroot-remain),bank_surplus_fraction=str(delta/4),data_surplus_fraction=str(delta/6),data_excess_upper_bits=str(excess_cap),result='PASS')
            rows.append(row); out.write(json.dumps(row)+'\n'); out.flush()
            assert time.monotonic()-start<60
result=dict(result='PASS',cases=len(rows),elapsed_seconds=time.monotonic()-start,arithmetic='exact rational and certified log intervals',maximum_total_booked_fraction='5/192')
(RUN/'out/owner_validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
