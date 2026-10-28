from pathlib import Path
from fractions import Fraction as F
import json,time
root=Path(__file__).resolve().parents[1]
domain=[4,8,16,32,64,128,256]
spec={'helper_version':'A010-imbalance-v1','family':'same physical two-core family, s=4; equal clause activation 1/(r+s)','domain':domain,'case_count':7,'symmetry':'none','arithmetic':'Fraction exact generating function and inequality signs','memory_estimate_mb':30,'max_runtime_seconds':55}
(root/'IMBALANCE_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
t=time.perf_counter();rows=[];checks=0
for r in domain:
 s=4;N=r+s;p=1-F(1,N);c=F(1,15*N);b=p+c
 # Exact K-weighted mass for {z0,z2}; both group unions must be nonempty.
 q=r*c*b**(r-1)*(b**s-p**s)+s*c*b**(s-1)*(b**r-p**r)
 upper=2*r*s*c*c
 a=F(3,4)**r;d=F(3,4)**s;P=(1-a)**2*(1-d)**2/16
 I=F(5,4)-(a+d)/4-3*a*d/4+(r*a*(1+d)+s*d*(1+a))/6
 assert 0<q<=upper<1;assert P>F(1,81);assert F(5,4)<I<2
 checks+=3
 rows.append({'r':r,'s':s,'Q_target':str(q),'Q_upper':str(upper),'P_target':str(P),'I':str(I)})
result={'status':'PASS','checks':checks,'rows':rows,'seconds':time.perf_counter()-t,'all_parameter_proof':'REVIEW_AND_EXTENSION.md, imbalance section'}
(root/'out/IMBALANCE.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
