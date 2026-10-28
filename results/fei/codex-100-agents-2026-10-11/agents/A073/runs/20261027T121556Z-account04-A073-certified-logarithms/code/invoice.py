"""Exact A085 invoice; zero-aware signed log bounds; no external writes/imports."""
from fractions import Fraction as F
from pathlib import Path
import json,time,hashlib,sys
R=Path(__file__).resolve().parents[1];O=R/'out';O.mkdir(exist_ok=True)
def save(name,obj):
    with (O/name).open('w',encoding='utf-8',newline='\n') as f:json.dump(obj,f,indent=2,default=str);f.write('\n')
def likelihood(b):return F(432,25)*b*(F(3,4)-b)**2
def polynomial(k,d):return 27*k*(3*d-4*k)**2-25*d**3
def bracket(m):
    d=1<<m;lo=d//8;hi=d//4
    def quad(k):return 144*k*k-168*k*d+25*d*d
    assert quad(lo)>0>quad(hi)
    while hi-lo>1:
        mid=(hi+lo)//2
        if quad(mid)>0:lo=mid
        else:hi=mid
    return lo,d
def enclosure(b,beta=F(1),reach=F(1)):
    assert 0<b<=F(1,3) and beta>=0 and reach>=0
    g=likelihood(b);assert g>0
    if g==1 or not beta or not reach:return F(0),F(0)
    # For ALL g>0: (g-1)/g <= ln(g) <= g-1.
    # 2/3 < ln(2) < 25/36, obtained from the z=1/3 positive atanh series.
    low,high=(g-1)/g,g-1
    vals=[x/y for x in (low,high) for y in (F(2,3),F(25,36))]
    return beta*reach*min(vals)/4,beta*reach*max(vals)/4
def budget_sign(b,beta,reach,margin):
    """Sign(actual full reached price minus CURRENT unused B-C-U).

    Zero weights and exact equality are handled; a size hold is UNRESOLVED.
    No release is credited again and no influence bank is renewed.
    """
    assert beta>=0 and reach>=0
    weight=beta*reach
    if not weight:return (0>margin)-(0<margin),0
    g=likelihood(b);assert g>0
    exponent=4*margin/weight;u,v=exponent.numerator,exponent.denominator
    estimated=max(g.numerator.bit_length()*v+max(-u,0),g.denominator.bit_length()*v+max(u,0))
    if estimated>1000000:return 'UNRESOLVED_RESOURCE_BOUND',estimated
    left=g.numerator**v;right=g.denominator**v
    if u>=0:right<<=u
    else:left<<=-u
    return (left>right)-(left<right),estimated
def dyadic_lower(x):
    assert x>0
    e=max(0,x.denominator.bit_length()-x.numerator.bit_length()+1)
    while x<=F(1,1<<e):e+=1
    return e
def main():
    start=time.monotonic();checks=0
    ms=list(range(4,161))+[512,1024]
    grid=sorted({F(k,d) for d in range(1,65) for k in range(1,d) if F(1,8)<=F(k,d)<=F(1,4)})
    spec={'helper_version':'A073-invoice-v1','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'actual_Boolean_family':'Fixed AND2 truth (-1,1,1,1); varied calibrated normalized references q_b',
          'parameter_domain':{'dyadic_m':ms,'rational_grid':list(map(str,grid))},
          'case_count':2*len(ms)+len(grid),'symmetry':'none; Boolean dimension stays2',
          'arithmetic':'integer binary root isolation, Fraction likelihoods, exact integer product budget signs, rational ln enclosures',
          'memory_estimate_MB':60,'maximum_runtime_seconds':55,'integer_product_bit_limit':1000000,
          'precision_stop':'exact polynomial/product sign; fixed integral enclosure, no numerical refinement'}
    save('FROZEN.json',spec)
    # ln2 upper uses geometric positive tail from z=1/3; independently exact constants.
    z=F(1,3)
    assert 2*z+2*z**3/(3*(1-z*z))==F(25,36);checks+=1
    cases=[];first_alias=None;fixture=None;maximum_bits=0;budget_cases=0
    for m in ms:
        k,d=bracket(m)
        assert polynomial(k,d)<0<polynomial(k+1,d);checks+=1
        low,high=F(k,d),F(k+1,d)
        alias=float(low)==float(high)
        if alias and first_alias is None:first_alias=m
        for name,b in [('minus',low),('plus',high)]:
            cases.append((b,{'m':m,'neighbor':name,'unreduced_numerator':k+(name=='plus'),'unreduced_denominator':d}))
        if m==58:
            fixture={'m':58,'bminus':str(low),'bplus':str(high),'binary64_equal':alias,
                     'weighted_price_enclosures':[[str(x) for x in enclosure(b,F(3,8))] for b in [low,high]],
                     'rigorous_magnitude_dyadic_exponents':[dyadic_lower(min(abs(x) for x in enclosure(b,F(3,8)))) for b in [low,high]]}
    assert first_alias==58;checks+=1
    cases.extend((b,{'rational_grid':True}) for b in grid)
    rows=[]
    for b,meta in cases:
        assert time.monotonic()-start<55
        k,d=b.numerator,b.denominator;g=likelihood(b);n=polynomial(k,d)
        assert g-1==F(n,25*d**3)
        assert n==(3*k-d)*(144*k*k-168*k*d+25*d*d)
        assert n and g<=F(27,25)
        assert abs(3*k-d)>=F(d,4)
        assert abs(g-1)>=F(1,100*d*d)
        lo,hi=enclosure(b)
        sg=(n>0)-(n<0)
        assert (lo>0 and hi>0) if sg>0 else (lo<0 and hi<0)
        assert min(abs(lo),abs(hi))>=F(1,300*d*d)
        lo3,hi3=enclosure(b,F(3,8))
        assert min(abs(lo3),abs(hi3))>=F(1,800*d*d)
        checks+=8
        for beta in [F(1),F(3,8)]:
            for reach in [F(1),F(1,2)]:
                for margin in [F(-1,64),F(0),F(1,64)]:
                    sign,bits=budget_sign(b,beta,reach,margin)
                    assert isinstance(sign,int)
                    maximum_bits=max(maximum_bits,bits)
                    l,h=enclosure(b,beta,reach)
                    if h<margin:assert sign<0
                    elif l>margin:assert sign>0
                    if not margin:assert sign==sg
                    checks+=1;budget_cases+=1
        if meta.get('m') in [4,58,160,512,1024]:
            rows.append({'b':str(b),'polynomial_numerator':str(n),'integer_factorization':[str(3*k-d),str(144*k*k-168*k*d+25*d*d)],
                         'likelihood':str(g),'price_enclosure':[str(lo),str(hi)],'weight3_over8_enclosure':[str(lo3),str(hi3)],
                         'magnitude_lower_bound':str(F(1,300*d*d)),**meta})
    # Boundary/equality/zero-reach controls, outside the strict incoming interior when b=1/3.
    assert enclosure(F(1,3))==(F(0),F(0))
    for beta,reach,margin,expected in [(F(1),F(1),F(0),0),(F(0),F(1),F(0),0),(F(1),F(0),F(1),-1),(F(0),F(1),F(-1),1)]:
        assert budget_sign(F(1,3),beta,reach,margin)[0]==expected;checks+=1
    assert budget_sign(F(1,8),F(1),F(1),F(1,1000001))[0]=='UNRESOLVED_RESOURCE_BOUND';checks+=1
    # Actual Boolean spectrum and minimal dimensions, direct transform.
    truth=[-1,1,1,1]
    walsh=[sum(truth[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(4)) for s in range(4)]
    assert [F(w*w,16) for w in walsh]==[F(1,4)]*4
    assert sum(F(s.bit_count()*w*w,16) for s,w in enumerate(walsh))==1;checks+=2
    for nvar in [0,1]:
        size=1<<nvar
        for mask in range(1<<size):
            t=[1-2*((mask>>x)&1) for x in range(size)]
            p=[F(sum(t[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(size))**2,size**2) for s in range(size)]
            assert sum(x!=0 for x in p)==1;checks+=1
    save('SELECTED_CERTIFICATES.json',rows);save('M58_FIXTURE.json',fixture)
    save('RESULT.json',{'status':'PASS','exact_checks':checks,'reference_cases':len(cases),'dyadic_brackets':len(ms),
                       'budget_comparisons':budget_cases,'maximum_integer_bit_estimate':maximum_bits,'first_binary64_alias_in_fixed_sequence':first_alias,
                       'all_rational_theorem':'For 1/8<=b=k/d<=1/4: |Delta|>=1/(300d^2); |(3/8)Delta|>=1/(800d^2)',
                       'all_m_consequence':'On dyadic brackets m>=4, 2m+11 absolute precision bits suffice at weight3/8; exact integer sign needs no log refinement',
                       'runtime_seconds':time.monotonic()-start,'FEI':'OPEN; no universal source or constant improvement'})
    print(json.dumps({'status':'PASS','exact_checks':checks,'reference_cases':len(cases),'budget_comparisons':budget_cases,'runtime_seconds':time.monotonic()-start}))
if __name__=='__main__':main()
