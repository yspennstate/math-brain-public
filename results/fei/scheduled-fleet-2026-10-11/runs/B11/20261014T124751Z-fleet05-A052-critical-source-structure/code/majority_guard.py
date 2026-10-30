import json
from fractions import Fraction as F
from pathlib import Path
import check_flows as c
import phase_library as p
import exact_library as e
ROOT=Path(__file__).resolve().parents[1]
v=[1 if x.bit_count()>=2 else -1 for x in range(8)];w=e.direct(v)
H=p.entropy([F(x*x,64) for x in w]);I=F(sum(v[x]!=v[x^(1<<i)] for x in range(8) for i in range(3)),8)
c.ck(H=={2:F(2)});c.ck(I==F(3,2));c.ck(all(x==0 or abs(x)==4 for x in w))
pot=[F(-2)]*8;piv=[sum(v[x]!=v[x^(1<<i)] for i in range(3)) for x in range(8)]
charges=[pot[x]-F(5,2)+3*piv[x] for x in range(8)]
ok,pos,cert=c.flow(v,charges,6);c.ck(ok);c.ck(pos==6)
lo,hi=e.lnprime(2);c.ck(F(hi,1<<e.PREC)<F(3,4))
for E in range(256):
    boundary=sum(v[x]*v[x^(1<<i)] for x in range(8) for i in range(3) if x<(x^(1<<i)) and bool(E>>x&1)!=bool(E>>(x^(1<<i))&1))
    c.ck(-2*E.bit_count()-F(5,2)*E.bit_count()-3*boundary<=0)
E=sum(1<<x for x in range(8) if v[x]<0);delta=F(E.bit_count(),8)
edited=[-v[x] if E>>x&1 else v[x] for x in range(8)];c.ck(edited==[1]*8)
old=[F(x,8) for x in w];new=[F(x,8) for x in e.direct(edited)]
# Natural-log units: Bregman remainder includes a rational constant.
vec={};constant=F(0)
for a,z in zip(old,new):
    if z:vec=p.add(vec,p.lograt(z*z),-z*z)
    if a:
        vec=p.add(vec,p.lograt(a*a),a*a+2*a*(z-a));constant+=2*a*(z-a)
    constant+=3*(z-a)**2
c.ck(vec=={2:F(2)});c.ck(constant==4)
c.ck(c.sg(vec,constant)>0)
# Delta D ln2 = (4/N) W ln2 + R ln2 = 7 ln2.
Wvec={2:F(10)};Wconstant=F(-8)
identity=p.add(p.scale(Wvec,F(1,2)),vec);ic=F(1,2)*Wconstant+constant
c.ck(identity=={2:F(7)});c.ck(ic==0)
result={'status':'PASS','truth_values':v,'K':6,'lambda_for_rational_flow':'5/2','H':'2','I':'3/2','D':'-7',
        'feasible_positive_charge_vertices':pos,'flow_certificate':cert,
        'edit_vertices':[x for x in range(8) if E>>x&1],'actual_deficit_improvement':'7',
        'Bregman_remainder_natural_vector':p.enc(vec),'Bregman_remainder_natural_constant':str(constant),
        'assertions':c.checks}
(ROOT/'out/MAJORITY_GUARD.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','assertions':c.checks,'positive_sources':pos,'improvement':'7'}))
