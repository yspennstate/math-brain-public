"""Own direct full-grid Arb heat-content certificate, checkpointed per endpoint.

No solver imports. All 86 points use 192 full signed bins at 180-bit precision,
instead of paired symmetry and the author's mixed coarse/refined grid.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime
import ctypes
import hashlib
import json
import time
from flint import arb,ctx

HERE=Path(__file__).resolve().parent
OUT=HERE/'t067_own_endpoints'
OUT.mkdir(exist_ok=True)
ctx.prec=180
kernel=ctypes.windll.kernel32
kernel.GetCurrentProcess.restype=ctypes.c_void_p
kernel.SetPriorityClass.argtypes=[ctypes.c_void_p,ctypes.c_ulong]
kernel.SetProcessInformation.argtypes=[ctypes.c_void_p,ctypes.c_int,ctypes.c_void_p,ctypes.c_ulong]
process=kernel.GetCurrentProcess()
assert kernel.SetPriorityClass(process,0x4000)
class Throttle(ctypes.Structure):
    _fields_=[('Version',ctypes.c_ulong),('ControlMask',ctypes.c_ulong),('StateMask',ctypes.c_ulong)]
throttle=Throttle(1,1,0)
assert kernel.SetProcessInformation(process,4,ctypes.byref(throttle),ctypes.sizeof(throttle))
source_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
def A(f):
    f=F(f)
    return arb(f.numerator)/f.denominator
def upper(a):
    m,e=a.upper().man_exp()
    return F(int(m)*(1<<int(e))) if e>=0 else F(int(m),1<<-int(e))
def lower(a):
    return -upper(-a)
sqrt2=arb(2).sqrt()
norm=(2*arb.pi()).sqrt()
def phi(x):
    return (-x*x/2).exp()/norm
bins=[]
for j in range(-96,96):
    left,right=A(F(j,16)),A(F(j+1,16))
    mass=((right/sqrt2).erf()-(left/sqrt2).erf())/2
    first=phi(left)-phi(right)
    second=mass+left*phi(left)-right*phi(right)
    mean=first/mass
    variance=second-first*first/mass
    assert mass>0 and variance>0 and mean>left and mean<right
    bins.append((mass,mean,variance))
P=sum((w for w,_,_ in bins),arb(0))
D=sum((v for _,_,v in bins),arb(0))
assert 0<P and P<1 and D>0
baseline=Path('~/brain_workers/w682/checks/piecewise_raw_endpoint_verification.json')
saved=json.loads(baseline.read_text(encoding='utf-8'))['endpoint_g_upper']
start=time.monotonic()
completed=0
for i in range(86):
    point=F(10,100-i)
    dest=OUT/f'endpoint_{i:03d}.json'
    if dest.exists():
        old=json.loads(dest.read_text(encoding='utf-8'))
        assert old['source_sha256']==source_hash and old['s']==str(point)
        continue
    signal=A(point)
    alpha=3*(3*signal).sqrt()/2
    beta=3*signal.sqrt()/2
    coshes=[(beta*mean).cosh() for _,mean,_ in bins]
    Q=arb(0)
    for wi,mi,_ in bins:
        coefficient=2*(-9*signal/2-alpha*mi).exp()
        Q+=wi*sum((wj/(1+coefficient*c) for (wj,_,_),c in zip(bins,coshes)),arb(0))
    remainder=9*signal*P*D/10
    g_upper=upper(Q+remainder+1-P*P-arb(1)/3)
    g_lower=lower(Q-remainder-arb(1)/3)
    assert g_lower<g_upper
    original=F(saved[str(point)])
    assert g_lower<=original,'Independent bracket contradicts saved upper'
    result={'s':str(point),'g_upper':str(g_upper),'g_lower':str(g_lower),
        'source_sha256':source_hash,'precision':180,'full_signed_bins':192,
        'saved_upper_minus_own_upper':str(original-g_upper),
        'own_upper_at_most_saved':g_upper<=original,
        'at':datetime.now().astimezone().isoformat()}
    temp=dest.with_suffix('.part')
    temp.write_bytes((json.dumps(result,indent=2)+'\n').encode('utf-8'))
    temp.replace(dest)
    completed+=1
    if i%10==0 or i==85:
        print(json.dumps({'endpoint':i,'s':str(point),'own_upper_at_most_saved':g_upper<=original}),flush=True)
    if time.monotonic()-start>240:
        print('Checkpointed at 240 seconds; resume same script',flush=True)
        break
rows=[json.loads(p.read_text(encoding='utf-8')) for p in sorted(OUT.glob('endpoint_*.json'))]
summary={'at':datetime.now().astimezone().isoformat(),'completed':len(rows),'expected':86,
    'new_this_run':completed,'all_own_upper_at_most_saved':all(r['own_upper_at_most_saved'] for r in rows),
    'source_sha256':source_hash,'method':'Full signed 192-bin Arb conditional-mean quadrature; global Hessian error and entire Gaussian tail',
    'scope':'Independent endpoint enclosures conditional on the audited softmax Hessian bound; does not alone prove the BP comparison or theorem.'}
(HERE/'T067_ENDPOINTS_OWN_SUMMARY.json').write_bytes((json.dumps(summary,indent=2)+'\n').encode('utf-8'))
print(json.dumps(summary),flush=True)
