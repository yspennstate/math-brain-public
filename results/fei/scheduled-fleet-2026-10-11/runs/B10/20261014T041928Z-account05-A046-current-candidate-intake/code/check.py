from pathlib import Path
from fractions import Fraction as Q
import runpy,itertools,json,time
ROOT=Path(__file__).resolve().parents[1]
src=ROOT.parent/'20261014T012528Z-account05-A046-current-candidate-intake'/'code'/'layers.py'
h=runpy.run_path(str(src));node=h['node'];phi=h['phi'];log=h['log'];fmt=h['fmt'];add=h['add'];mul=h['mul'];sub=h['sub'];rows=h['rows'];coef=h['coeff'];ZERO=h['ZERO']
start=time.perf_counter();out=[];checks=0
for j,L,(R,T) in itertools.product((1,2,4),(1,3),((4,4),(4,8),(8,16))):
    q,r=Q(1,2**R),Q(1,2**T);eta=Q(1,2**(L+R+T));e=q+r-q*r-eta;rho=Q(1,2**(j-1));d=rho*e/2
    assert e<=Q(1,8) and eta<=Q(8,25)*e*e;checks+=2
    G=(None,R,T,L);H=(0,R,T,L);qn=bn=Q(0);nonconst=ZERO
    for mask,count in rows((0,R,T,L)):
        a,b=coef(G,mask),coef(H,mask)
        for core in (0,1):
            if mask==0 and core==0:continue
            g=a if core else Q(mask==0)-a
            hh=b if core else Q(mask==0)-b
            delta=hh-g;u=g+rho*delta/2;v=-rho*delta/2
            qn+=count*(u*u+v*v);bn+=count*v*v;nonconst=add(nonconst,mul(count,phi(u*u,v*v)))
    assert qn==2*eta-eta*eta-rho*eta*e+rho*rho*(e-e*e/2)
    assert bn==rho*rho*e*(2-e)/4;checks+=2
    constant=phi((1-eta-d)**2,d*d)
    reconstructed=add(add(constant,nonconst),(2*(1-rho)*d,2*(1-rho)*d))
    B,J,actuald=node((j,R,T,L),0);assert actuald==d
    assert sub(B,reconstructed)[0]<=0<=sub(B,reconstructed)[1];checks+=2
    packet_bound=add(mul(d*d,log(1/(d*d))),mul(d*d,(Q(0),Q(3,2))))
    # The last term deliberately uses c=log2(euler)<3/2, with an outward enclosure.
    packet_bound=add(packet_bound,mul(bn,add(log((2*eta+rho*rho*e)/bn),(Q(0),Q(3,2)))))
    packet_bound=add(packet_bound,(2*(1-rho)*d,2*(1-rho)*d))
    assert B[1]<Q(1781,480)*d;checks+=1
    out.append({'j':j,'L':L,'R':R,'T':T,'e':str(e),'eta':str(eta),'Q_nonconstant_exact':str(qn),'b_nonconstant_exact':str(bn),'B_over_d_outward':fmt(mul(1/d,B)),'universal_small_e_bound':'1781/480','constant_row_mass':[str((1-eta-d)**2),str(d*d)]})
    (ROOT/'out'/'SPECTRAL_CHECK.json').write_text(json.dumps({'status':'IN_PROGRESS','cases':out},indent=2)+'\n',encoding='utf-8')
    if time.perf_counter()-start>55:raise SystemExit('pilot budget stop; incomplete certificate')
summary={'status':'PASS','actual_grouped_nodes':len(out),'recorded_assertions':checks,'runtime_seconds':time.perf_counter()-start,'cases':out}
(ROOT/'out'/'SPECTRAL_CHECK.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k!='cases'}))
