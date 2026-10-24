from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,time,sys
R=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('rare_primitive',R/'code/pilot.py');V=importlib.util.module_from_spec(s);s.loader.exec_module(V)
def ex(x):return x,x
def add(*xs):return V.sumiv(xs)
def scale(x,a):return V.mul(x,ex(a))
def bern(p,q):return V.kl([p,1-p],[q,V.sub(ex(F(1)),q)])
def fmt(x):return [str(z) for z in x]
def ratio_floor(x):return str(F((x[0]*10**8).__floor__(),10**8))
def eta(x):return scale(V.log(ex(x)),-x) if x else ex(F(0))
start=time.perf_counter();rows=[];count=0
domain=[16] if '--pilot' in sys.argv else [16,24,32,64]
for n in domain:
    e=F(1,1<<n);m=1-e;v=1-m*m/4;L=n+1;r=1/(2*v);small=e/(2*v)
    g=lambda c:1-c-(1-r*c)**2*(1-small*c)**L
    lo,hi=v,F(1);assert g(lo)>0>g(hi);count+=1
    for _ in range(96):
        c=(lo+hi)/2
        if g(c)>0:lo=c
        else:hi=c
    assert g(lo)>0>g(hi);count+=1;c=(lo,hi)
    t=scale(c,r);h=V.div(V.sub(ex(F(1)),c),scale(V.sub(ex(F(1)),t),2))
    b0=V.div(h,add(ex(m*m/4),h));p=1/(1+m*m);q=(1+m*m)/4;W=(1-m*m)/2
    E=add(scale(bern(p,b0),q),scale(bern(p,t),q),scale(V.log(V.div(ex(F(1)),V.sub(ex(F(1)),t))),W))
    A=(1+m)**2/4;B=e*e/4
    phi=add(scale(V.log(ex(A+B)),A+B),scale(V.log(ex(A)),-A),scale(V.log(ex(B)),-B))
    rho=V.sub(add(V.L.evalformal(V.L.h(e/2)),ex(-e+e*e/2)),phi)
    assert E[0]>0 and E[1]<=3*e;count+=2
    assert rho[0]>=e*F(n-2,2);count+=1
    ratio=V.div(rho,E);assert ratio[0]>=F(n-2,6);count+=1
    assert hi-v<=L*e/2;count+=1
    Hmax=V.log(c)
    for a,mult in [(r,2),(small,L)]:
        theta=scale(c,a)
        Hmax=V.sub(Hmax,add(scale(V.log(theta),mult*a),scale(V.log(V.sub(ex(F(1)),theta)),mult*(1-a))))
    Hroot=add(scale(eta(m*m/4),2),scale(eta(F(1,4)),2),scale(eta(e*e/4),(1<<(n+2))-2))
    Aroot=V.sub(add(eta(v),eta(1-v),scale(Hmax,v)),Hroot)
    Hchild=add(eta((1-e/2)**2),scale(eta(e*e/4),(1<<(n+2))-1))
    TCchild=V.sub(scale(add(eta(e/2),eta(1-e/2)),n+2),Hchild)
    cube=V.div(V.sub(ex(F(1)),c),V.mul(V.sub(ex(F(1)),t),V.sub(ex(F(1)),t)))
    qY=add(ex(F(1,2)),scale(V.sub(ex(m*m/4),scale(V.mul(t,cube),F(1,2))),m/(1+m*m)))
    O=bern(F(1,2),qY)
    conversion_margin=V.sub(Aroot,add(O,TCchild))
    assert conversion_margin[1]<=-F(n-6,2)*e;count+=1
    rows.append({'n':n,'epsilon':str(e),'c_bracket':fmt(c),'erasure_KL_release':fmt(E),'rho':fmt(rho),'rho_over_release_strict_lower':ratio_floor(ratio),'analytic_ratio_lower':str(F(n-2,6)),
    'root_occupancy_KL':fmt(Aroot),'actual_mean_child_TC':fmt(TCchild),'occupancy_outcome_KL':fmt(O),'actual_conversion_margin':fmt(conversion_margin),'analytic_margin_upper':str(-F(n-6,2)*e),
    'retained_terminal_entropy_exact':'H(point defect on n+2 bits), with heavy atom swapped in the two actual children'})
elapsed=time.perf_counter()-start;assert elapsed<60
out={'status':'PASS','domain':domain,'assertions':count,'rows':rows,'runtime_seconds':elapsed,'all_n_proof':'RARE_OBSTRUCTION.md establishes rho/E>=(n-2)/6 for every n>=16; finite intervals are corroboration'}
(R/'out'/('RARE_PROJECTION_PILOT.json' if '--pilot' in sys.argv else 'RARE_PROJECTION_CERTIFICATE.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS','domain':domain,'assertions':count,'runtime_seconds':elapsed,'ratio_lower_bounds':[row['rho_over_release_strict_lower'] for row in rows]}))
