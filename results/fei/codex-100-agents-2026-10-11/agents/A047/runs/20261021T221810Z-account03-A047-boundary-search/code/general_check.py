from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1]
exec(compile((R/'code/certify.py').read_text(encoding='utf-8').split('cases=')[0],str(R/'code/certify.py'),'exec'))
for r in range(2,65):
 m=1<<(r+2);delta=F(1,1<<r);k=m*r;K=k*delta/2
 ck(K==2*r)
 for t in [F(1,4),F(1,2)]:
  v=1-(1-t)**2/4;u=delta/(4*v)
  ck(F(3,4)<v<=F(15,16) and 0<u<1)
  ck(k*u==r/v and 1/(1+k*u)<=F(1,1+r)<F(1,2))
  ck(F(2*r*r-1,1)/(2*r+F(5,4))>r-1)
for r in range(2,21):
 delta=F(1,1<<r);I=2*r*delta
 ck(hp(r)[1]<=4*I)
for j in range(17):ck(neg(plog(F(j,64)))[1]<=F(1,2))
ck(LN2[0]>F(1,2))
obj={'status':'PASS','assertions':CHECKS,'scalar_cases':162,'runtime_seconds':time.perf_counter()-START,'domain':'r2..64,t1/4,1/2; point-factor entropy r2..20; p-log grid0..1/4','not_exhaustive_boolean_check':True,'all_r_scope':'analytic proof with explicit m=2^(r+2), CE/I>r-1 and H<=4I'}
(R/'out/GENERAL_CHECK.json').write_text(json.dumps(obj,indent=2),encoding='utf-8');print(json.dumps(obj))
