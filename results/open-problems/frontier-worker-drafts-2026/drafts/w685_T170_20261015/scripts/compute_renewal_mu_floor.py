from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
from datetime import datetime,timezone
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]

def main():
    path=ROOT/'logs/height_bridge_tail_certificate.json'
    point=json.loads(path.read_text(encoding='utf-8'))
    get=lambda key:Q(int(point[key]['n']),int(point[key]['d']))
    s,z=get('s'),get('z');d=21
    sqrt_scale=10**24;sqrt_lower=Q(isqrt(d*sqrt_scale**2),sqrt_scale)
    assert sqrt_lower**2<=d
    t=(z-1)/(z+1);assert 0<t<1
    log_lower=2*sum((t**(2*k+1)/Q(2*k+1)) for k in range(50))
    ratio=sqrt_lower*log_lower/s
    scale=10**12;units=ratio.numerator*scale//ratio.denominator;floor=Q(units,scale)
    assert floor>Q(73873348622,10**12)
    gain=floor*sqrt_lower/Q(331371710,10**9)-1
    assert gain>Q(217,10000)
    out=dict(at=datetime.now(timezone.utc).isoformat(),d=d,
             point_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
             floor_numerator=str(units),floor_denominator=str(scale),
             floor_decimal=f'{units//scale}.{units%scale:012d}',
             sqrt_lower={'n':str(sqrt_lower.numerator),'d':str(sqrt_lower.denominator)},
             logarithm_lower_method='2 sum k=0..49 ((z-1)/(z+1))^(2k+1)/(2k+1); every omitted term is positive',
             ceg_gain_lower_percent_millionths=str((gain*100*10**6).__floor__()),
             scope='exact downward floor of sqrt(d) log(z)/s only; FPP translation is a separate unaudited proof')
    (ROOT/'logs/height_renewal_mu_floor.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS exact diagonal ratio floor',out['floor_decimal'],'CEG gain > 2.17 percent',flush=True)
if __name__=='__main__':main()
