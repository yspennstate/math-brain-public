"""Own Arb arithmetic for stopped birth-forest sufficient inequalities."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime
from math import factorial
import hashlib,json,ctypes
from flint import arb,ctx
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
HERE=Path(__file__).resolve().parent
proof=Path('~/brain_workers/w674/T186/proofs/C014_C015_global_snapshot_forest.md')
digest=hashlib.sha256(proof.read_bytes()).hexdigest()
assert digest=='29593274c1dd79d14dfee5963e41bd24c26b2d51febaf77f5753bc8bb47e26d7'
ctx.prec=200
def A(x):
    x=F(x);return arb(x.numerator)/x.denominator
def lower(x):
    m,e=x.lower().man_exp()
    return F(int(m)*(1<<int(e))) if e>=0 else F(int(m),1<<-int(e))
rows=[]
for k,c0,theta,thetap,u,R,N,coef in [
    (4,'11.415','.1','.100001','1.223','.025305',4000000,5),
    (3,'9.053','.125','.125001','1.315','.042379',3000000,4)]:
    c0,theta,thetap,u,R=map(F,(c0,theta,thetap,u,R)); delta=F(1,10**6)
    assert 0<theta<thetap<1 and u>1-theta
    assert c0>=(k-1)/(1-thetap) and N>=k/(thetap-theta)
    assert F(k)/(1-thetap)<coef
    c,t,tp,v,r=map(A,(c0,theta,thetap,u,R))
    x=c*(v+r)
    Em=sum((x**j/factorial(j) for j in range(k)),arb(0))
    slackA=r-v*(-c*(1-tp)).exp()*Em
    slackB=t*v.log()+t+(1-t)*(1-t).log()-r-A(delta)
    assert slackA>0 and slackB>0
    rows.append({'k':k,'c0':str(c0),'theta':str(theta),'theta_plus':str(thetap),
        'u':str(u),'R':str(R),'n0':N,'delta':str(delta),'probability_coefficient':coef,
        'slack_A_lower':str(lower(slackA)),'slack_B_minus_delta_lower':str(lower(slackB)),
        'slack_A_lower_float':float(lower(slackA)),
        'slack_B_minus_delta_lower_float':float(lower(slackB))})
out={'at':datetime.now().astimezone().isoformat(),'proof_sha256':digest,
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'precision':200,'status':'PASS exact rational inputs and own Arb inequalities; no solver imports',
    'rows':rows,'analytic_scope':'Lead rederived deterministic stopped forest, single independent-edge witness probability, labelled SET generating functions, bounded monotone height iteration, c-uniform polynomial derivative bound, falling-factorial Riemann estimate and k-size union bound. No conditional red probabilities multiplied and no edge-monotonicity assumption about the strong core.',
    'admission':'Await w683 full exact-version review before frontier promotion.'}
(HERE/'T186_UPPER_CONSTANTS_RECEIPT.json').write_bytes((json.dumps(out,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'status':out['status'],'rows':[{k:r[k] for k in ['k','slack_A_lower_float','slack_B_minus_delta_lower_float']} for r in rows]}))
