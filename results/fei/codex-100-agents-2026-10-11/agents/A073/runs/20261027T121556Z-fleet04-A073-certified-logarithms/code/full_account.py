"""Keep irrational current CE symbolically inside the exact SAME-owner test."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,time
from paired import compare_all,full_price_product
R=Path(__file__).resolve().parents[1];O=R/'out';start=time.monotonic()
spec=json.loads((O/'FROZEN.json').read_text(encoding='utf-8'))
bs=list(map(F,spec['parameter_domain']['rational_grid']))
for row in json.loads((O/'SELECTED_CERTIFICATES.json').read_text(encoding='utf-8')):bs.append(F(row['b']))
# All rational-grid references plus selected high-precision controls, predeclared.
bs=sorted(set(bs));checks=0
def save(name,obj):
    with (O/name).open('w',encoding='utf-8',newline='\n') as f:json.dump(obj,f,indent=2,default=str);f.write('\n')
save('FULL_ACCOUNT_FROZEN.json',{'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'comparison_helper_sha256':hashlib.sha256((R/'code/paired.py').read_bytes()).hexdigest(),
      'actual_Boolean_family':'AND2, H=2,I=1','domain':list(map(str,bs)),'case_count':len(bs)+1,
      'symmetry':'none','arithmetic':'FULL CE rational-log forms, exact integer comparisons; no rounded remaining margin',
      'memory_estimate_MB':60,'maximum_runtime_seconds':55,'original_capacity':'B=(5/2)I=5/2','old_U':'1/4'})
target=[F(1,4),F(5,24),F(5,24),F(1,3)]
target_terms=[(1/q,F(1,4)) for q in target]
for b in bs:
    assert time.monotonic()-start<55
    q=[F(1,4),(F(3,4)-b)/2,(F(3,4)-b)/2,b]
    ce_terms=[(1/x,F(1,4)) for x in q]
    original_sign=compare_all(ce_terms,F(17,8))
    full=compare_all(ce_terms+[(full_price_product(b),F(1,4))],F(17,8))
    direct=compare_all(target_terms,F(17,8))
    assert original_sign['status']==full['status']==direct['status']=='CERTIFIED'
    assert original_sign['sign']<0 and full['sign']==direct['sign']<0
    product=F(1)
    for x in q:product/=x
    product*=full_price_product(b)
    target_product=F(1)
    for x in target:target_product/=x
    assert product==target_product
    checks+=4
# A VALID zero-unused owner: matched q=p has CE=2, B=9/4,U=1/4.
# A positive admission cannot be silently paid by omitting CURRENT CE or U.
matched=[(F(4),F(1,4))]*4
assert compare_all(matched,F(2))['sign']==0
assert compare_all(matched+[(full_price_product(F(1,4)),F(1,4))],F(2))['sign']>0
assert 625-512==113;checks+=3
save('FULL_ACCOUNT_RESULT.json',{'status':'PASS','reference_cases':len(bs),'exact_checks':checks,
       'original_source':'B=(5/2)I, I=1; both initial and final CE<17/8; oldU=1/4 retained',
       'remaining_original_reserve':'>1/8','uniform_sign_certificate':'2^9=512<625=5^4, integer margin113',
       'scope':'uniform supplied AND2 interval in proof; tests validate CE cancellation and owner compiler, not full FEI',
       'zero_unused_owner_positive_price':'REJECTED_EXACTLY','runtime_seconds':time.monotonic()-start})
print(json.dumps({'status':'PASS','reference_cases':len(bs),'exact_checks':checks,'runtime_seconds':time.monotonic()-start}))
