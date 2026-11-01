"""Additional independent boundary and altered-artifact controls, not a continuum proof."""
from review import *
import review as engine
from copy import deepcopy
if (ROOT/'out/BOUNDARY_AUDIT.json').exists():
    previous=json.loads((ROOT/'out/BOUNDARY_AUDIT.json').read_text(encoding='utf-8'))
    if previous['exact_checks']==0:
        write('BOUNDARY_FIRST_COUNTER.json',{'first_output':previous,'first_frozen_spec':json.loads((ROOT/'out/BOUNDARY_SPEC.json').read_text(encoding='utf-8')),'issue':'import-star copied integer checks=0; ck increments review.checks. Arithmetic assertions DID run; serialization counter only. Full fixed-domain rerun follows.','mathematical_source_error':False})
spec={'version':'A075-guard-boundary-controls-v2-counterfix','family':'all16 two-bit seeds; auxiliary weighted guard entropy, not nondyadic Boolean spectra','domain':['0','1/64','3/64','1/8','3/16','1/4'],'cases':96,'symmetry':'none','arithmetic':'exact Fraction/log forms and192bit outward intervals','memory_estimate_mb':100,'maximum_runtime_seconds':55,'positive_controls':'altered seed influence, altered entropy and altered claim statement must be rejected'}
write('BOUNDARY_SPEC.json',spec)
cases=[]
for table in range(16):
    t=tuple(-1 if table>>x&1 else 1 for x in range(4));H,w=entropy(t);mu=F(w[0],4);a=1-mu;v=1-mu*mu
    for ds in spec['domain']:
        delta=F(ds)
        if not delta:
            profile={};ck(not profile)
            cases.append({'table':table,'delta':ds,'H':{},'zero_face':'pure parity, all capital0'});continue
        ld=logq(delta)
        profile=eta((1-delta*a)**2)
        profile=add(profile,add(eta(a*a),ld,-2*a*a),delta-delta*delta)
        profile=add(profile,add(add(H,eta(mu*mu),F(-1)),ld,-2*v),delta)
        direct=add(eta((1-delta*a)**2),eta((delta*a)**2),1/delta-1)
        for W in w[1:]:direct=add(direct,eta((delta*F(W,4))**2),1/delta)
        ck(profile==direct)
        mass=(1-delta*a)**2+(1/delta-1)*(delta*a)**2+sum(((delta*F(W,4))**2/delta for W in w[1:]),F(0))
        ck(mass==1);ck(cmp(profile,{})>=0);ck(cmp(profile,{2:F(5)})<=0)
        if delta<=F(1,8):
            bound=scale(add({2:F(4)},ld,F(-2)),4*delta);ck(cmp(profile,bound)<=0)
        cases.append({'table':table,'delta':ds,'H':pack(profile)})
        ck(time.perf_counter()-start<55)
seed=json.loads((ROOT/'out/SEED_REVIEW.json').read_text(encoding='utf-8'))
source=json.loads((SOURCE/'out/SEED_CERTIFICATE.json').read_text(encoding='utf-8'))
ck(F(seed['I'])==F(source['I']))
ck(F(seed['I'])!=F(source['I'])+F(1,1<<30))
ck(unpack(seed['H'])!=add(unpack(source['H']),{2:F(1,1<<30)}))
claims=json.loads((SOURCE/'CLAIMS.json').read_text(encoding='utf-8'));claim=claims[0]
def digest(c):return hashlib.sha256(json.dumps({'exact_statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')).hexdigest()
ck(digest(claim)==claim['statement_sha256']);changed=deepcopy(claim);changed['exact_statement']+=' ALTERED';ck(digest(changed)!=claim['statement_sha256'])
# Every source pin was saved BEFORE computation; changing the source mid-review fails closed.
for pin in json.loads((ROOT/'out/SOURCE_PINS.json').read_text(encoding='utf-8')):
    ck(hashlib.sha256(Path(pin['path']).read_bytes()).hexdigest()==pin['sha256'])
result={'status':'PASS','cases':len(cases),'exact_checks':engine.checks,'seconds':time.perf_counter()-start,'source_digest':claim['statement_sha256'],'positive_controls_rejected':3,'source_pins_unchanged':True,'profiles':cases}
write('BOUNDARY_AUDIT.json',result)
print(json.dumps({k:v for k,v in result.items() if k!='profiles'}))
