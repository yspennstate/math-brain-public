"""Frozen scalar and finite arithmetic sign certificates, v1.1."""
from profiles import *
start=time.perf_counter()
checks=0
def check(b):
    global checks
    assert b;checks+=1
def psi(d):return plus(constant(2-2*d),phi_ratio((1-d)**2,d*d,d))
boxes=[]
for j in range(256):
    lo=F(3,16)+F(j,20480);hi=F(3,16)+F(j+1,20480)
    al=(1-lo)**2;ah=(1-hi)**2;bl=lo*lo;bh=hi*hi
    bound=plus(constant(2-2*lo),plus(scale(log2(1+bh/ah),al/lo),scale(log2(1+al/bl),hi)))
    check(bound[1]*10<27*Q)
    boxes.append({'lo':str(lo),'hi':str(hi),'upper_scaled':bound[1]})
# Lower bound for the old-coordinate stability lemma.
for j in range(256):
    lo=F(3,16)+F(j,20480);hi=F(3,16)+F(j+1,20480)
    al=(1-lo)**2;ah=(1-hi)**2;bl=lo*lo;bh=hi*hi
    lower=plus(constant(2-2*hi),plus(scale(log2(1+bl/al),ah/hi),scale(log2(1+ah/bh),lo)))
    check(lower[0]*5>13*Q)
check(17**34<2**139)
check(7**2>2**5);check(3**12>2**19)
# Invariant scalar conditions for the alternating composition path.
check(F(25,8)**4*2*F(3,32)**3<1)
check(F(29,32)**3>F(2,3));check(F(75,256)<F(3,10))
check(2*F(3,10)**3<F(1,8))
check(F(219501,16777216)<F(1,64))
check(F(11,5)+F(65,98)+F(5,128)<3)
data=json.loads((ROOT/'out'/'PROFILES.json').read_text())
c2=data['composition'][1]
check(c2['minimum_interval'][1]*5<11*Q)
c1=data['composition'][0];check(c1['minimum_interval'][1]<3*Q)
check(next(c['ratio_interval'][1] for c in c2['classes'] if c['path']=='TB')*5<11*Q)
check(next(c['ratio_interval'][1] for c in c1['classes'] if c['path']=='T')<3*Q)
check(F(17,1024)+3*F(1,2**25)<F(1,10))
check(2+F(6*25+8,2**24)<F(5,2))
# Periodic-sequence endpoint; the interval is regenerated directly.
limit=psi(F(1,5))
result={'version':'certify.py/v1.1','scale_bits':P,'ln_terms':K,'assertions_passed':checks,'failed':0,'psi_boxes':boxes,'lex_limit_interval':limit,'runtime_seconds':time.perf_counter()-start}
(ROOT/'out'/'SCALAR_CERTIFICATES.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'assertions_passed':checks,'runtime_seconds':result['runtime_seconds'],'lex_limit_display':decimal(limit),'maximum_box_upper_display':decimal((0,max(r['upper_scaled'] for r in boxes)))[1]}))
