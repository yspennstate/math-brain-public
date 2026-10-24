import json,time
from fractions import Fraction as Q
from pathlib import Path
from check import fwht,upper_degrees,check_table
started=time.perf_counter()
rows=[]
assertions=0
for width in [1,2,3]:
    n=width+(1<<width)
    size=1<<n
    values=[]
    for x in range(size):
        address=x&((1<<width)-1)
        values.append(-1 if x&(1<<(width+address)) else 1)
    assertions+=check_table(values,n)
    a=fwht(values)
    d=upper_degrees(a,n)
    support=[s for s,v in enumerate(a) if v]
    assert a[0]==0 and len(support)==1<<(2*width)
    assert all(abs(a[s])==size//(1<<width) and d[s]==width+1 for s in support)
    assert all((s>>width).bit_count()==1 for s in support)
    influence=Q(sum(s.bit_count()*a[s]**2 for s in support),size*size)
    u=Q(sum(a[s]**2*(d[s]-s.bit_count()) for s in support),size*size)
    assert influence==1+Q(width,2) and u==Q(width,2)
    assert 2*influence+2*u-2==2*width
    assertions+=5
    rows.append({'a':width,'physical_n':n,'nonzero_coefficients':len(support),'I':str(influence),'U':str(u),'arithmetic_entropy_bound':2*width,'exact_entropy':2*width})
result={'complete':True,'assertions':assertions,'cases':3,'rows':rows,'elapsed_seconds':time.perf_counter()-started}
(Path(__file__).resolve().parents[1]/'out'/'check_address.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
