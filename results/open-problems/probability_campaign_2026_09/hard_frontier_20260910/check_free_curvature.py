"""Bounded author controls: exact identities and independent density differentiation."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import sys, pathlib, json, hashlib
sys.path.insert(0,'~/<private-repo>/12_cognitive_architecture/audits/probability_publishability_20260910')
from verify import claim_assert, now
import sympy as sp
import mpmath as mp

state=json.loads(pathlib.Path('~/.claude/compute/compute_state.json').read_text(encoding='utf-8-sig'))
if state['status']=='distress' or state['mem_avail_mb']<8000 or state['cpu_pct']>85:
    raise SystemExit('Compute admission refused; no check result produced')
mp.mp.dps=80
a,y,b,t,M,r=sp.symbols('a y b t M r', real=True)
exact=[
    sp.cancel((b+2*a*y+y*y)/(a+y)-(a+y)-(b-a*a)/(a+y)),
    sp.expand((2*M-4*a)*(M-a)-sp.Rational(5,2)*M*(M-4*a)-(-M*M+8*a*M+8*a*a)/2),
    sp.expand(-4*(t-a)+sp.Rational(5,2)*(t-4*a)+sp.Rational(3,2)*t+6*a),
    sp.cancel(-4/(1-4*r)+3/(1-r)+(1+8*r)/((1-4*r)*(1-r))),
]
assert all(x==0 for x in exact),exact
mr=(t-4*r)/(1-4*r*r);ar=r*mr
assert sp.cancel(t-mr-4*ar*(1-ar)/mr)==0

laws=[
    ('point',[0],[1]),
    ('equal_pair',[-1,1],['0.5','0.5']),
    ('nearly_equal_pair',[-1,1],['0.49','0.51']),
    ('skew_pair',[-1,1],['0.1','0.9']),
    ('three_symmetric',[-1,0,1],['0.2','0.6','0.2']),
    ('three_skew',[-1,'0.2',1],['0.15','0.25','0.6']),
    ('five',[-1,'-0.5',0,'0.5',1],['0.07','0.13','0.19','0.23','0.38']),
]
rows=[];differences=[]
for name,xx,ww in laws:
    xs=list(map(mp.mpf,xx));ws=list(map(mp.mpf,ww));assert sum(ws)==1
    D=max(xs)-min(xs);mean=sum(w*x for x,w in zip(xs,ws))
    for factor in map(mp.mpf,['1.01','1.25','2','10']):
        tt=factor*D*D if D else factor
        def F(u,v): return sum(w/((u-x)**2+v*v) for x,w in zip(xs,ws))
        def C1(u,v): return sum(w*(u-x)/((u-x)**2+v*v)**2 for x,w in zip(xs,ws))
        u,v=mp.findroot(lambda u,v:(F(u,v)-1/tt,C1(u,v)),(mean,mp.sqrt(tt)),tol=mp.mpf('1e-65'),maxsteps=80)
        assert v>0
        den=[(u-x)**2+v*v for x in xs]
        Z=sum(w/q**2 for w,q in zip(ws,den))
        aa=sum(w*(u-x)**2/q**2 for x,w,q in zip(xs,ws,den))/Z
        bb=sum(w*(u-x)**4/q**2 for x,w,q in zip(xs,ws,den))/Z
        yy=v*v;mm=aa+yy
        assert abs(tt-mm-(bb-aa*aa)/mm)<mp.mpf('1e-55')
        assert bb+3*aa*aa <= D*D*aa+mp.mpf('1e-55')
        Fuu=sum(w*(6*(u-x)**2-2*v*v)/q**3 for x,w,q in zip(xs,ws,den))
        Fv=-2*v*Z
        v2=-Fuu/Fv
        psi1=1+tt*sum(w*(v*v-(u-x)**2)/q**2 for x,w,q in zip(xs,ws,den))
        p2=v2/(mp.pi*tt*psi1**2)
        target=-(tt-D*D)/(4*mp.pi*(tt-D*D/4)**mp.mpf('2.5'))
        assert p2<=target+mp.mpf('1e-50'),(name,str(tt),str(p2),str(target))
        if name in ('point','equal_pair'):assert abs(p2-target)<mp.mpf('1e-50')
        rows.append({'law':name,'time':mp.nstr(tt,20),'diameter':mp.nstr(D,20),'mode_parameter':mp.nstr(u,25),'density_second_derivative':mp.nstr(p2,35),'sharp_bound':mp.nstr(target,35),'ratio_to_bound':mp.nstr(p2/target,30)})
        if factor==2:
            def psi(uu,vv):return uu+tt*sum(w*(uu-x)/((uu-x)**2+vv*vv) for x,w in zip(xs,ws))
            xmode=psi(u,v);center=v/(mp.pi*tt)
            errors=[]
            for exponent in (5,6):
                h=mp.sqrt(tt)*mp.mpf(10)**(-exponent)
                values=[]
                for sign in (-1,1):
                    target_x=xmode+sign*h
                    uu,vv=mp.findroot(lambda uu,vv:(F(uu,vv)-1/tt,psi(uu,vv)-target_x),(u+sign*h/psi1,v),tol=mp.mpf('1e-65'),maxsteps=80)
                    assert vv>0
                    values.append(vv/(mp.pi*tt))
                numeric=(values[1]-2*center+values[0])/(h*h)
                relative=abs((numeric-p2)/p2)
                assert relative<mp.mpf('1e-8')
                errors.append(relative)
            assert errors[1] < errors[0]/20
            differences.append({'law':name,'physical_coordinate_finite_difference_relative_errors':[mp.nstr(e,30) for e in errors]})

out=pathlib.Path('~/<private-repo>/12_cognitive_architecture/audits/evidence/2026/09/10/probability_publishability/p0174_curvature_controls.json')
record={'at':now(),'scope':'Author mathematical controls, not a universal proof or novelty certificate','exact_symbolic_identities':5,'atomic_mode_cases':len(rows),'independent_physical_coordinate_cases':len(differences),'precision_decimal_digits':80,'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'rows':rows,'finite_difference_checks':differences,'status':'PASSED'}
claim_assert(out);out.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:record[k] for k in ['status','exact_symbolic_identities','atomic_mode_cases','independent_physical_coordinate_cases','precision_decimal_digits']}),flush=True)
