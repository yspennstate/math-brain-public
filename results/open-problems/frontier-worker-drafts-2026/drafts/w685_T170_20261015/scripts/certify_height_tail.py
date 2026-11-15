from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json
from certify_bounds import sqrt_bounds,log_bounds,exact,floor_decimal
ROOT=Path(__file__).resolve().parents[1]
p=[r for r in json.loads((ROOT/'scripts/hybrid2_certificate_parameters.json').read_text(encoding='utf-8'))['rows'] if r['d']==21][0]
z=Q(p['z_n'],p['z_d']);d=21;upper=Q(203083967073,2748779069440)
sqlo,_=sqrt_bounds(d);loglo,_=log_bounds(z)
critical=sqlo*loglo/upper;scale=10**6;s=Q((critical*scale).__floor__()-1,scale);a=s+1;t=Q(7,5)
r=Q(d)*(z+t**4/z)/(a*t);assert 0<r<Q(9,10)
test=sqlo*loglo/s;assert test>upper
k=400;tail=t*r**k/(1-r);ratio_upper=Q(9,10)
tail_bound=t*ratio_upper**k/(1-ratio_upper)
assert tail<=tail_bound<Q(1,10**15)
obj=dict(at=datetime.now(timezone.utc).isoformat(),d=d,z=exact(z),s=exact(s),t=exact(t),r=exact(r),r_upper='9/10',length_cutoff=k,baseline_tail_bound=exact(tail_bound),baseline_tail_upper='1/10^15',test_time_ratio_lower=exact(test),axis_upper=exact(upper),test_margin=exact(test-upper),historical_axis_context='The axis_upper and test_margin refer to the superseded five-slab comparison, not the current dimension frontier.',scope='An exact scalar bridge tail and fixed parameter point only; separate scalar-mass, norm, interval and full-path artifacts carry their own claims and review status.')
(ROOT/'logs/height_bridge_tail_certificate.json').write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
print('PASS scalar tail: r floor',floor_decimal(r),'K400 tail<1e-15; positive test margin floor',floor_decimal(test-upper),'; no FPP bound claimed.')
