import json
from fractions import Fraction
from collections import Counter
from pathlib import Path
from certify_pure import signature_interval,log_interval
from verify_slices import direct_transform,product_ok
ROOT=Path(__file__).resolve().parents[1]

def signature(W,denominator):
    from cover_search import prime_factors
    assert denominator&(denominator-1)==0
    sig=Counter({2:(denominator.bit_length()-1)*sum(a*a for a in W)})
    for a in W:
        if not a:continue
        for p,e in prime_factors(a*a).items():sig[p]-=a*a*e
    return tuple(sorted((p,v) for p,v in sig.items() if v))

def main():
    data=json.loads((ROOT/'out'/'mixed_cover_results.json').read_text());assert data['status']=='COMPLETE'
    log3lo,log3hi=log_interval(3)
    assert Fraction(16,3)-Fraction(3,2)*log3hi>Fraction(12,5)
    positive=equality=0;min_margin=None;certificates=[]
    for row in data['objective_signatures']:
        I=row['influence_numerator'];delta=Counter({2:Fraction(16*I,3),3:Fraction(-3*I,2)})
        for p,v in row['log_signature']:delta[p]-=v
        delta=tuple(sorted((p,v) for p,v in delta.items() if v))
        if not delta:
            equality+=1;certificates.append({'log_signature':row['log_signature'],'influence_numerator':I,'verdict':'EXACT_EQUALITY'});continue
        lo,hi=signature_interval(delta)
        assert lo>0,('candidate exceeds benchmark or precision insufficient',row,lo,hi)
        positive+=1;min_margin=lo if min_margin is None else min(min_margin,lo)
        certificates.append({'log_signature':row['log_signature'],'influence_numerator':I,'verdict':'STRICT_BELOW','margin_lower_rounded_1e12':str(Fraction(lo*10**12//1,10**12))})
    h=[list(row) for row in data['best']['slices_h']]
    h.sort(key=lambda row:sum(v*v for v in row),reverse=True)
    # Address labels sorted by weights0,1,1,2; slice signs can be changed
    # globally while leaving all squared spectra untouched.
    M=data['best']['mixed_mask'];x=(M&-M).bit_length()-1
    if __import__('math').prod(row[x] for row in h)==1:h[0]=[-v for v in h[0]]
    for x in range(16):
        values=[row[x] for row in h]
        if M>>x&1:assert all(abs(v)==1 for v in values) and __import__('math').prod(values)==-1
        else:assert sum(v!=0 for v in values)==1 and sum(v*v for v in values)==4
    truth=[]
    for x in range(16):
        for y in range(4):
            twice=sum(h[J][x]*(-1 if (y&J).bit_count()%2 else 1) for J in range(4))
            assert twice in(-2,2);truth.append(twice//2)
    W=direct_transform(truth)
    assert sum(v*v for v in W)==4096
    I_W=sum(s.bit_count()*v*v for s,v in enumerate(W))
    I_phys=sum(sum(truth[x]!=truth[x^(1<<j)] for x in range(64)) for j in range(6))
    assert Fraction(I_W,4096)==Fraction(I_phys,64)
    marginals=[]
    for J in range(4):
        data_coeff=direct_transform(h[J]);assert product_ok(data_coeff,4)
        norm=sum(v*v for v in data_coeff)
        marginals.append([str(Fraction(sum(v*v for s,v in enumerate(data_coeff) if s>>j&1),norm)) for j in range(4)])
    sig=signature(W,4096);delta=Counter({2:Fraction(16*I_W,3),3:Fraction(-3*I_W,2)})
    for p,v in sig:delta[p]-=v
    assert all(v==0 for v in delta.values())
    witness={'truth_table':truth,'bit_order':'addresses bits0,1; data bits2,3,4,5; physical masks0..63','partial_slices_h':h,'walsh_integers':W,'I':str(Fraction(I_W,4096)),'H_exact_signature':[(p,str(Fraction(v,4096))) for p,v in sig],'H_over_I_exact':'16/3-(3/2)log2(3)','conditional_product_marginals':marginals,'status':'EXACT_BOOLEAN_AND_RATIO_VERIFIED'}
    (ROOT/'out'/'maximizer_truth_table.json').write_text(json.dumps(witness,indent=2))
    bound={'status':'PASS','finite_target':'Every two-address conditional-product Boolean F on six uniform variables satisfies H<=Cstar I, Cstar=16/3-(3/2)log2(3); equality attained','mixed_objective_signatures':len(data['objective_signatures']),'strict_signatures':positive,'equality_signatures':equality,'minimum_strict_margin_lower_rounded_1e12':None if min_margin is None else str(Fraction(min_margin*10**12//1,10**12)),'pure_bound':'12/5<Cstar','all_mixed_bound':'2<Cstar','per_signature_certificates':certificates,'external_review':'PENDING A088/A094; author direct Walsh reproduction only'}
    (ROOT/'out'/'full_exact_certificate.json').write_text(json.dumps(bound,indent=2));print(json.dumps({k:v for k,v in bound.items() if k!='per_signature_certificates'}))
if __name__=='__main__':main()
