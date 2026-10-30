from pathlib import Path
from fractions import Fraction as Q
import json,time
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261012T010436Z-fleet05-A018-shared-data-collision-law/code/check_lead.py'
ns={'__file__':str(OLD),'__name__':'arithmetic_only'}
exec(compile(OLD.read_text(encoding='utf8').split("\nresult={'helper_version'")[0],str(OLD),'exec'),ns)
start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1;assert x
ck(Q(2**4-4,3*2*1)==2)
ck([Q(5,8)-Q(1,2),-1,2]==[Q(1,8),-1,2])
lnlo,lnhi=ns['ln'](2);ck(lnlo>Q(2,3))
ck(Q(5,8)<lnlo)
ck(2**128*11**73<3**127*5**80)
ck(2**16>3**9)
out={'status':'PASS','checks':checks,'elapsed_seconds':time.perf_counter()-start,'gate_constant':'4+5/(8ln2)','gate_constant_interval':[str(4+Q(5,8)/lnhi),str(4+Q(5,8)/lnlo)],'quadratic_square':'5/8-(1/2+d-2d^2)=2(d-1/4)^2','negative_uniform_prior_change':'2^128*11^73<3^127*5^80','selector_rate4_not_sufficient_for_profile_alone':'2^16>3^9; Psi(1/2)=3-(9/8)log2(3)>1'}
(ROOT/'out/ANALYTIC_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':'PASS','checks':checks,'elapsed_seconds':out['elapsed_seconds']}))
