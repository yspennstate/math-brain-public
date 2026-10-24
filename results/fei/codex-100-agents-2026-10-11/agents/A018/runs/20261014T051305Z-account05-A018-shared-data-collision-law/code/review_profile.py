from pathlib import Path
from fractions import Fraction as Q
import json,time
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261012T010436Z-account05-A018-shared-data-collision-law/code/check_lead.py'
ns={'__file__':str(OLD),'__name__':'arithmetic_only'}
exec(compile(OLD.read_text(encoding='utf8').split("\nresult={'helper_version'")[0],str(OLD),'exec'),ns)
start=time.perf_counter();checks=0
def ck(v):
 global checks
 checks+=1;assert v;assert time.perf_counter()-start<60
l2,h2=ns['ln_grid'](2)
def divint(lo,hi,denlo,denhi):
 xs=[lo/denlo,lo/denhi,hi/denlo,hi/denhi]
 return min(xs),max(xs)
def vals(d):
 p={1-d:-2*(1-d)**2,d:-2*d*d,1-2*d:(1-2*d)**2}
 dp={1-d:4*(1-d),d:-4*d,1-2*d:-4*(1-2*d)}
 pl,ph=ns['grid'](p);gl,gh=divint(pl,ph,l2*d,h2*d)
 gl+=4-4*d;gh+=4-4*d
 nl,nh=ns['grid'](ns['add']((d,dp),(-1,p),(-4*d*d,{2:1})))
 dl,dh=divint(nl,nh,l2*d*d,h2*d*d)
 return gl,gh,dl,dh
ck(7**126>3**60*2**256);ck(3**5<2**8)
lo=Q(1,8);hi=Q(1,4);ck(vals(lo)[2]>0 and vals(hi)[3]<0)
steps=[]
for i in range(24):
 mid=(lo+hi)/2;_,_,dl,dh=vals(mid);ck(dl>0 or dh<0)
 steps.append({'mid':str(mid),'derivative_interval':[str(dl),str(dh)]})
 if dl>0:lo=mid
 else:hi=mid
gl,gh,dl,dh=vals(lo);lower=gl;upper=gh+max(Q(0),dh)*(hi-lo)
ck(lower>Q(4872,1000) and upper<Q(4873,1000))
out={'status':'PASS','checks':checks,'bisections':24,'maximizer_bracket':[str(lo),str(hi)],'Gamma_interval':[str(lower),str(upper)],'certified_simple_interval':['4872/1000','4873/1000'],'elapsed_seconds':time.perf_counter()-start,'independence':'A018 positive-series strict-concavity proof and own80-bit arithmetic; no A060 utility/checker imported','review_scope':'Fine profile supremum/unique root/enclosure and dyadic Boolean realizability only; coarse release and tensor ledger clauses not independently reviewed here','steps':steps}
(ROOT/'out/PROFILE_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:out[k] for k in ('status','checks','bisections','certified_simple_interval','elapsed_seconds')}))
