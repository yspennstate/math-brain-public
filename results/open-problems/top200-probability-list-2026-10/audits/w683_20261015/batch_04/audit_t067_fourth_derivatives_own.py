"""Own exact radial-fourth polynomials and Bernstein certificate replay."""
from pathlib import Path
from fractions import Fraction
from hashlib import sha256
from datetime import datetime
import json,time
import sympy as S
from audit_t067_softmax_own import bernstein_coeffs,split_half,variables

started=time.monotonic()
u,v,t=variables
x,y=S.symbols('x y')
p=[x,y,1-x-y]
h=[0,t,1]
def diff(f,direction):
    m=sum(p[i]*direction[i] for i in range(3))
    return S.Poly(S.expand(x*(direction[0]-m)*S.diff(f,x)+y*(direction[1]-m)*S.diff(f,y)),x,y,t).as_expr()
A=9*sum(q*q for q in p)-3
Q=S.expand(A*A)
dh=[Q]
for k in range(4):dh.append(diff(dh[-1],h))
unit=[[int(i==j) for i in range(3)] for j in range(3)]
V=[diff(dh[2],e) for e in unit]
assert S.expand(sum(V))==0
N=S.Rational(2,3)*(1-t+t*t)
polys={'Gv_-1':8-diff(Q,unit[0])/2,'Gv_+1':8+diff(Q,unit[0])/2,
       'D2_-1':20*N-dh[2],'D2_+1':20*N+dh[2],
       'D4_-1':99*N*N-dh[4],'D4_+1':99*N*N+dh[4],
       'D3_squared':38**2*N**3-dh[3]**2,
       'D3_mixed_squared':38**2*N*N-sum(z*z for z in V)}
assert dh[2].subs({x:S.Rational(1,2),y:S.Rational(1,2),t:1})!=0
source=Path('~/brain_workers/w682/checks/fourth_derivative_v1/report.json')
assert sha256(source.read_bytes()).hexdigest()=='ea392acae0bb563dbc963e902f17423b2387a589a3bd337763740d874a5c27bf'
report=json.loads(source.read_text())
assert report['status']=='EXACT BERNSTEIN COVER PASS',report['status']
outpath=Path('checks/t067_fourth_derivatives_own.json')
results=[]
for job in report['jobs']:
    name=job['name']; degree=tuple(n-1 for n in job['shape'])
    expr=S.Poly(S.expand(polys[name]),x,y,t).as_expr().subs({x:u,y:(1-u)*v},simultaneous=True)
    coeffs,power=bernstein_coeffs(expr,degree)
    stored={tuple(e):Fraction(a) for e,a in job['root_power_terms']}
    assert power==stored,name
    paths=[leaf['path'] for leaf in job['leaves']]
    assert len(paths)==len(set(paths))
    assert all(set(path)<=set('01') for path in paths)
    assert all(not b.startswith(a) for i,a in enumerate(paths) for j,b in enumerate(paths) if i!=j)
    assert sum((Fraction(1,2**len(path)) for path in paths),Fraction())==1
    count=zero=0; minimum=None
    # Reuse only our independent midpoint subdivisions along common prefixes.
    cache={'':coeffs}
    for path in sorted(paths):
        for depth in range(1,len(path)+1):
            prefix=path[:depth]
            if prefix not in cache:cache[prefix]=split_half(cache[prefix[:-1]],degree,(depth-1)%3,prefix[-1])
        leaf=cache[path]
        m=min(leaf.values()); assert m>=0,(name,path,m)
        minimum=m if minimum is None else min(minimum,m)
        count+=len(leaf); zero+=sum(q==0 for q in leaf.values())
    results.append({'name':name,'leaves':len(paths),'coefficients':count,'minimum':str(minimum),'zeros':zero,'power_terms':len(power)})
    receipt={'at':datetime.now().astimezone().isoformat(),'source_sha256':sha256(source.read_bytes()).hexdigest(),'own_script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'method':'Own repeated polynomial softmax vector fields; own Fraction tensor conversion and exact midpoint split','jobs':results,'complete':len(results)==8,'total_leaves':sum(r['leaves'] for r in results),'zero_hessian_negative_control_rejected':True,'seconds':time.monotonic()-started}
    outpath.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
    print(name+' PASS '+str(len(paths))+' leaves',flush=True)
    if time.monotonic()-started>480 and len(results)<8:raise RuntimeError('Eight-minute chunk complete; saved prefix receipt, resume with explicit remaining jobs')
assert receipt['total_leaves']==124
print('ALL 124 LEAVES PASS',flush=True)
