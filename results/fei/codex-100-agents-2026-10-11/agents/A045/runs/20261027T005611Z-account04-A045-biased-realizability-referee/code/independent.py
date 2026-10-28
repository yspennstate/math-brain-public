"""Direct centered-moment reproduction; no checker imports or transform reuse."""
from pathlib import Path
from fractions import Fraction as F
from math import prod
import json,time
root=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0; rows=[]
main=json.loads((root/'out/CHECKS.json').read_text(encoding='utf-8'))
for rec in main['prime_boundary_records']:
    n=rec['n']; e=F(rec['e'])
    if e not in [F(1,64),F(1,1024),F(1,2**20)]:continue
    ps=[F(1,2)]*2+[e]*(n-2); means=[2*p-1 for p in ps]
    vs=[4*p*(1-p) for p in ps]; coeff=[]; masses=[]; js=[]
    xs=[tuple(1 if a>>i&1 else -1 for i in range(n)) for a in range(1<<n)]
    w=[prod(ps[i] if x[i]==1 else 1-ps[i] for i in range(n)) for x in xs]
    f=[1 if sum(y==1 for y in x)>=2 else -1 for x in xs]
    for s in range(1<<n):
        inds=[i for i in range(n) if s>>i&1]
        mom=sum(weight*y*prod(x[i]-means[i] for i in inds) for x,y,weight in zip(xs,f,w))
        v=prod(vs[i] for i in inds)
        c=mom/v; coeff.append(c); masses.append(v*c*c)
        j=0; a=abs(c)
        if a:
            while 2**j*a<=F(1,2):j+=1
        js.append(j)
    assert sum(masses)==1;checks+=1
    delta=sum((s.bit_count()-1)*masses[s] for s in range(1,1<<n))
    R=sum((s.bit_count()-2)*masses[s] for s in range(1,1<<n) if s.bit_count()>2)
    J1=sum(masses[1<<i]*js[1<<i] for i in range(n))
    Jh=sum(masses[s]*js[s] for s in range(1,1<<n) if s.bit_count()>=2)
    U=2*delta-J1
    assert delta==F(rec['Delta']) and R==F(rec['R']);checks+=2
    assert U==F(rec['reserve_upper_over_ln4']) and Jh==F(rec['Jhi_over_ln4']);checks+=2
    assert 0<U<=5*(n-2)*e and Jh>=F(9,64);checks+=2
    # Three specific row witnesses for EVERY block, implemented via explicit
    # assignments rather than collecting all threshold row tuples.
    for block in range(1,1<<n):
        A=[i for i in range(n) if block>>i&1];B=[i for i in range(n) if not block>>i&1]
        if len(A)<2 or not B:continue
        observed=[]
        for r in range(3):
            a=sum(1<<i for i in A[:r]);observed.append((f[a],f[a|1<<B[0]]))
        assert observed==[(-1,-1),(-1,1),(1,1)];checks+=1
    rows.append({'n':n,'epsilon':str(e),'exact_ratio_lower':str(F(9,320*(n-2))/e)})
    assert time.perf_counter()-start<55
out={'status':'PASS','checks':checks,'cases':len(rows),'seconds':round(time.perf_counter()-start,6),'rows':rows,'method':'Direct full physical centered moments, independent of tensor transform; explicit three-row block witnesses.'}
(root/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
