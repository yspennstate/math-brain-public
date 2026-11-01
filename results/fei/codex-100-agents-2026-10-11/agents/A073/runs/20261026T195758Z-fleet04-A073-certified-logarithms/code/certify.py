"""A073 stage23: bounded exact certificates; no external writes or imports."""
from pathlib import Path
from fractions import Fraction as Q
import json, hashlib, time

R=Path(__file__).resolve().parents[1]
O=R/'out'
O.mkdir(exist_ok=True)
def save(name,obj):
    (O/name).write_text(json.dumps(obj,indent=2,default=str)+'\n',encoding='utf-8')

spec={'helper_version':'A073-stage23-v2','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'family':'All Boolean truth tables on exactly 3 bits (includes all smaller cores); scalar original-account envelopes',
      'domain':'256 masks; t in [0,1] analytic; 257 rational boundary probes',
      'case_count':256,'symmetry':'none','arithmetic':'Python unbounded integers and Fraction; integer log-product signs; no floating point',
      'memory_estimate_MB':40,'maximum_runtime_seconds':55,'dimension_escalation':False,
      'precision_stop':'integer signs only; no logarithm precision refinement'}
save('FROZEN_v2.json',spec)
start=time.monotonic()
checks=0
signs=[]
def sign(name,left,right):
    global checks
    assert left>right, name
    checks+=1
    signs.append({'name':name,'integer_encoding':'hexadecimal', 'lhs':hex(left),'rhs':hex(right),'integer_margin':hex(left-right)})

# Each sign certifies one logarithm comparison by monotonicity of log_2.
sign('log2(7/6)<25/112',2**25*6**112,7**112)
sign('log2(7/6)<67/300',2**67*6**300,7**300)
sign('log2(8/7)<1/5',2*7**5,8**5)
sign('point3 supplier factor >25/8: 36log2(3)>57',3**36,2**57)
# Scalar budget guards: these refute only the respective coarse envelopes.
sign('29-generation lower envelope at t=11/32 is <-1/64',7**6699,2**1488*6**6699)
sign('16-generation refined envelope at t=1/128 is negative',
     7**2032*8**127,2**456*6**2032*7**127)

rows=[]
for mask in range(256):
    assert time.monotonic()-start<55
    truth=[-1 if (mask>>x)&1 else 1 for x in range(8)]
    w=[sum(truth[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(8)) for s in range(8)]
    k=[z//2 for z in w]
    assert all(z%2==0 for z in w)
    # p_s=k_s^2/16 instead of unreduced Walsh masses w_s^2/64.
    a=[z*z for z in k]
    assert sum(a)==16
    I=sum(Q(s.bit_count()*a[s],16) for s in range(8))
    Iedges=Q(sum(truth[x]!=truth[x^(1<<j)] for j in range(3) for x in range(8)),8)
    assert I==Iedges
    mu=Q(w[0],8)
    # H=4-sum a_s log2(a_s)/16.  Clear 128 for S4-(25/8)(1-|mu|).
    A=128*(4*I-4-Q(25,8)*(1-abs(mu)))
    assert A.denominator==1
    P=1
    for z in a:
        if z:P*=z**(8*z)
    A=int(A)
    left=P*(2**max(A,0));right=2**max(-A,0)
    assert left>=right
    if I:assert left>right
    rows.append({'truth_mask':mask,'walsh_numerators':w,'influence':str(I),'mean':str(mu),
                 'target':'4I-H >= (25/8)(1-|mean|)',
                 'integer_lhs':str(left),'integer_rhs':str(right),'strict':left>right})
    checks+=6

# Exact polynomial identities and boundary cases. They supplement the analytic proof.
for j in range(257):
    t=Q(j,256);m=min(t,1-t)
    b28=Q(3,4)+2*t-Q(25,4)*t*(1-t)
    assert b28==Q(25,4)*(t-Q(17,50))**2+Q(11,400)
    assert b28>=Q(11,400)
    # Supplier slack is booked before the 15 fresh-generation bills.
    tensor=2*t+Q(25,16)*m-Q(71,20)*t*(1-t)
    if t<=Q(1,2):
        assert tensor==t/Q(80)+Q(71,20)*t*t
    else:
        assert tensor>=Q(9,40)  # loose positive bound from t>=1/2
    assert tensor>=0
    checks+=4

# Check the scalar counterguards independently as rational coefficient identities.
t=Q(11,32)
assert Q(3,4)+2*t==Q(1472,1024)
assert 29*t*(1-t)==Q(6699,1024)
assert Q(1472,1024)+Q(1,64)==Q(1488,1024)
t=Q(1,128)
# Refined envelope/t=57/16-(1-t)(16log2(7/6)+log2(8/7)).
assert Q(57,16)/(1-t)==Q(456,127)
checks+=4
save('FACTOR_CERTIFICATES.json',rows)
save('INTEGER_SIGNS.json',signs)
save('RESULT.json',{'status':'PASS','truth_tables':256,'checks':checks,
                    'factor_certificate':'S4(g)>=(25/8)(1-|Eg|), all <=3-bit g',
                    'conditional_generations':28,'conditional_reserve_after_old_quarter': '11/400',
                    'tensor_generations':15,'tensor_reserve_after_old_quarter':'3/4',
                    'guard_scope':'29 and16 guards concern lower-envelope insufficiency ONLY, not actual failing histories or FEI',
                    'runtime_seconds':time.monotonic()-start})
print(json.dumps({'status':'PASS','checks':checks,'truth_tables':256,'runtime_seconds':time.monotonic()-start}))
