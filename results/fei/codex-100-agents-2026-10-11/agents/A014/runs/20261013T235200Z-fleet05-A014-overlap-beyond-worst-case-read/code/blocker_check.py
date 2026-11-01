from pathlib import Path
from fractions import Fraction as F
import json, time
RUN=Path(__file__).resolve().parents[1]
start=time.monotonic(); assertions=0
def ck(x):
    global assertions
    assert x
    assertions+=1
def walsh(values):
    a=list(values); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h]; a[j],a[j+h]=u+v,u-v
        h*=2
    return a
rows=[]
for w,m in [(2,m) for m in range(1,5)]+[(3,m) for m in range(1,4)]:
    n=w*m; edges=[((1<<w)-1)<<(w*l) for l in range(m)]
    p=F(1,1<<w); c=(1-p)**(m-1); alpha=2*p*c
    values=[int(any(x&e==e for e in edges)) for x in range(1<<n)]
    hats=walsh(values)
    # +/-1 output is 2*values-1: all nonempty coefficients double.
    mass={A:F(4*h*h,1<<(2*n)) for A,h in enumerate(hats) if A}
    bad=sum((A.bit_count()*v for A,v in mass.items()
             if not any(A&e==A for e in edges)),F(0))
    influence=sum((A.bit_count()*v for A,v in mass.items()),F(0))
    ck(influence==n*alpha); ck(bad==influence*(1-c))
    for j in range(n):
        owner=j//w; residual_edge=edges[owner]^(1<<j)
        other=[k for k in range(n) if k!=j]
        xs=[sum(((z>>k)&1)<<other[k] for k in range(n-1)) for z in range(1<<(n-1))]
        d=[values[x|(1<<j)]-values[x] for x in xs]
        blocked=[int(x&residual_edge==residual_edge)*int(not any(x&e==e for l,e in enumerate(edges) if l!=owner)) for x in xs]
        ck(d==blocked)
        dh=walsh(d); size=len(d)
        off=F(0)
        for T,h in enumerate(dh):
            full=sum(((T>>k)&1)<<other[k] for k in range(n-1))|(1<<j)
            if not any(full&e==full for e in edges): off+=F(h*h,size*size)
        ck(off==alpha*(1-c))
    rows.append({'w':w,'m':m,'n':n,'influence':str(influence),'conditioned_residual_norm2':'0','off_clause_degree_mass':str(bad),'off_clause_degree_mass_over_influence':str(1-c)})
    (RUN/'out/blocker_checkpoint.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
symbolic=[]
for w in (2,3,4,8):
    p=F(1,1<<w)
    for m in range(1,65):
        c=(1-p)**(m-1)
        empty=(1-p)**2/(1-p)
        each_nonempty=p*p/(1-p)
        ck(empty==1-p)
        ck(((1<<w)-1)*each_nonempty==p)
        ck(empty+((1<<w)-1)*each_nonempty==1)
        symbolic.append({'w':w,'m':m,'c':str(c),'bad_over_I':str(1-c),'outside_normalized_empty_mass_per_block':str(empty),'outside_normalized_each_nonempty_mass':str(each_nonempty),'derivative_entropy_lower_bound_bits':str(F(w-1)+(m-1)*p*w)})
ck(F(1)-F(3,4)**3==F(37,64))
result={'helper':'A014-blocker-spectrum-v1','assertions':assertions,'full_spectra':len(rows),'symbolic_certificates':len(symbolic),'elapsed_seconds':time.monotonic()-start,'rows':rows,'symbolic':symbolic}
(RUN/'out/blocker_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('rows','symbolic')}))
