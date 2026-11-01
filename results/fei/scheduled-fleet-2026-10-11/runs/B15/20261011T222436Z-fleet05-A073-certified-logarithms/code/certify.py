from pathlib import Path
from fractions import Fraction as F
import json,hashlib,time,importlib.util
from certified_logs import *
ROOT=Path(__file__).resolve().parents[1]
AGENTS=ROOT.parents[2]
SRC=AGENTS/'A072/runs/20261011T220909Z-fleet05-A072-exact-walsh-engine/EXACT_WALSH_INTERFACE.py'
spec=importlib.util.spec_from_file_location('a072',SRC);a072=importlib.util.module_from_spec(spec);spec.loader.exec_module(a072)

def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    return x

def compute(name,table,p,A,orientation=1):
    parent=a072.biased_certificate(table,p)
    B=[i for i in range(len(p)) if not A>>i&1]
    selected=[i for i in range(len(p)) if A>>i&1]
    q=[F(0)]*(1<<len(B))
    for s,m in enumerate(parent['spectrum']):q[sum(((s>>i)&1)<<j for j,i in enumerate(B))]+=m
    children=[];mixture=[F(0)]*len(q)
    for z in range(1<<len(selected)):
        child,cp=a072.restrict(table,p,A,z)
        weight=prod(p[i] if z>>j&1 else 1-p[i] for j,i in enumerate(selected))
        law=a072.biased_certificate(child,cp)['spectrum']
        children.append({'table':child,'weight':weight,'spectrum':law})
        for j,m in enumerate(law):mixture[j]+=weight*m
    assert q==mixture
    form={}
    # D_without_tax = M-J = H(parent)-2H(q)+E H(child).
    add_entropy(form,orientation,parent['spectrum']);add_entropy(form,-2*orientation,q)
    for c in children:add_entropy(form,orientation*c['weight'],c['spectrum'])
    form={k:v for k,v in form.items() if v}
    L,exps,U,V,sign,dyadic,exact=product_certificate(form)
    record={'name':name,'table':table,'biases':p,'physical_block_mask':A,'orientation':orientation,
      'parent':parent,'marginal':q,'children':children,'prime_log_coefficients':form,
      'clearing_denominator':L,'integer_exponents':exps,'sign':sign,
      'dyadic_margin_bits':dyadic,'dyadic_lower_exact':exact,
      'numerator_bit_length':U.bit_length(),'denominator_bit_length':V.bit_length(),
      'numerator_hex_sha256':hashlib.sha256(format(U,'x').encode()).hexdigest(),
      'denominator_hex_sha256':hashlib.sha256(format(V,'x').encode()).hexdigest()}
    if sign:
        bounds=form_bounds(form,8)
        assert bounds[0]>0 if sign>0 else bounds[1]<0
        scale=10**8
        floor=(bounds[0]*scale).numerator//(bounds[0]*scale).denominator
        upper=bounds[1]*scale
        ceiling=-((-upper.numerator)//upper.denominator)
        record.update({'independent_eight_term_interval_bits':bounds,'precision_refinements':0,
          'outward_decimal_interval_bits':(F(floor,scale),F(ceiling,scale))})
    else:
        assert not form and U==V==1
        record.update({'equality_proof':'All prime-log coefficients vanish exactly','precision_refinements':0})
    # Exact product bytes are saved, not just hashes.
    (ROOT/'out'/f'{name}_products.json').write_text(json.dumps({'U_hex':format(U,'x'),'V_hex':format(V,'x')},indent=2),encoding='utf-8')
    (ROOT/'out'/f'{name}.json').write_text(json.dumps(serial(record),indent=2),encoding='utf-8')
    return record

def main():
    start=time.perf_counter()
    cases=[compute('minimum_positive',[1,1,1,-1,1,1,1,1],(F(1,8),F(1,8),F(1,2)),4),
           compute('exact_zero',[1,-1,-1,-1,-1,1,1,1],(F(1,8),F(1,8),F(1,2)),4),
           compute('taxfree_AND',[1,1,1,-1],(F(1,8),F(1,4)),1,-1)]
    assert [c['sign'] for c in cases]==[1,0,1]
    # Comparison with the existing repaired strict bound, no precision increase.
    assert cases[2]['independent_eight_term_interval_bits'][0]>F(1195,10000)
    assert cases[0]['parent']['spectrum']==[F(x,4096) for x in [3969,7,7,49,1,7,7,49]]
    assert cases[0]['integer_exponents']=={2:-10240,3:-7938,7:-3969,31:-1922,5:3970,397:3970}
    # Signed and range-reduced cases, exact logs, and rejection behavior.
    for k in range(-12,13):assert log2_bounds(F(2)**k)==(F(k),F(k))
    assert log2_bounds(F(1,3))[1]<0
    elapsed=time.perf_counter()-start;assert elapsed<55
    result={'helper_version':VERSION,'case_count':3,'failures':0,'runtime_seconds':elapsed,
      'engine_source':str(SRC),'engine_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),
      'source_claims':'Selected-record verification, no full-grid acceptance','cases':cases}
    (ROOT/'LOG_SIGN_CERTIFICATE.json').write_text(json.dumps(serial(result),indent=2),encoding='utf-8')
    print(json.dumps({'cases':[{'name':c['name'],'sign':c['sign'],'divisor':c['clearing_denominator'],
       'dyadic_bits':serial(c['dyadic_margin_bits']),
       'interval_decimal_for_display':[float(t) for t in c.get('independent_eight_term_interval_bits',[])]} for c in cases],
       'runtime_seconds':elapsed},indent=2))
if __name__=='__main__':main()
