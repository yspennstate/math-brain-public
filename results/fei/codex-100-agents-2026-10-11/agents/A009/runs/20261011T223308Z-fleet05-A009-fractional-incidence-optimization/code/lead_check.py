from fractions import Fraction as F
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1]
start=time.perf_counter(); count=0
def ck(x):
    global count
    assert x
    count+=1
ck(F(7,6)**4<2)
ck(F(3,2)**2>2)
ck(F(13,48)>F(1,4))
ck(F(1,2)-F(11,48)==F(13,48))
ck((1+F(11,48))-F(1,2)==F(35,48))
ck(F(48,5)*F(35,48)==7)
ck(1/(2*(1+F(11,48)))==F(24,59))
sun=[]
for m in range(1,13):
    b=1-F(1,2**m); lam=[F(1,2**i) for i in range(1,m+1)]
    q=[z/b for z in lam]
    ck(sum(q)==1); ck(sum(lam)==b); ck(all(z>0 and z<=1 for z in lam))
    ck(F(m*(m+1),2**m)<=F(3,2))
    pressure_upper=F(192,5)*b+F(11,5)*F(m*(m+1),2*2**m)
    I=1+F(m-1,2**m)
    ck(pressure_upper<41*I)
    sun.append({'m':m,'lambda':list(map(str,lam)),'core_piece_mass':list(map(str,q)),'I':str(I),'pressure_upper':str(pressure_upper)})
plane=[]
for Q in [16,32,64,128,256]:
    k=Q+1; N=Q*k; eps=F(N,2**(Q-1))
    ck(eps<F(1,2)); ck(F(1,k*(1-eps))<=F(2,k))
    ck(F(Q+2,2*Q)<1)
    ck(k*F(1,k)==1)
    plane.append({'Q':Q,'points':Q*Q,'lines':N,'read':k,'uniform_lambda':str(F(1,k)),'epsilon':str(eps),'alpha_lower':str(k*F(1,2**(Q-1))*(1-eps)),'piece_mass_upper':str(F(1,k*(1-eps))),'pressure_lower':'7 I log2((Q+1)/2)','scope':'all-feasible-weight analytic lower bound; exact finite bound arithmetic; no truth-table enumeration'})
out={'assertions':count,'runtime_seconds':time.perf_counter()-start,'status':'PASS','sunflower':sun,'affine_plane':plane}
(R/'out'/'LEAD_CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
cert=json.loads((R/'WEIGHT_CERTIFICATE.json').read_text())
cert['lead_direction']={'sunflower_global_rule':'lambda_l=2^-l; first-positive-index derivative tie','sunflower_pressure_bound':'<41 I','affine_plane_all_weight_obstruction':'pressure >=7 I log2((Q+1)/2), prime powers Q>=16','uniform_affine_upper':'<=7 I log2(Q+1)','scope':'positive coordinatewise pressure only; not full conditioned residual, PI-J, or FEI disproof','finite_exact_bound_checks':plane}
(R/'WEIGHT_CERTIFICATE.json').write_text(json.dumps(cert,indent=2),encoding='utf-8')
print(json.dumps({'assertions':count,'status':'PASS','runtime_seconds':out['runtime_seconds']}))
