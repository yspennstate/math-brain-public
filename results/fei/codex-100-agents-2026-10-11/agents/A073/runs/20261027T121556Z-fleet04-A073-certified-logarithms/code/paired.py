"""Exact simultaneous terminal comparison: retain negative prices and old U."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm,isqrt
import hashlib,json,time
R=Path(__file__).resolve().parents[1];O=R/'out'
def save(name,obj):
    with (O/name).open('w',encoding='utf-8',newline='\n') as f:json.dump(obj,f,indent=2,default=str);f.write('\n')
def full_price_product(b):
    incoming=[F(1,4),(F(3,4)-b)/2,(F(3,4)-b)/2,b]
    target=[F(1,4),F(5,24),F(5,24),F(1,3)]
    assert sum(incoming)==sum(target)==1
    value=F(1)
    for old,new in zip(incoming,target):value*=old/new
    return value
def compare_all(invoices,margin,limit=1000000):
    # Invoice (g,weight) denotes weight*log2(g); physical reach is IN weight.
    assert all(g>0 and weight>=0 for g,weight in invoices)
    scale=lcm(margin.denominator,*(weight.denominator for _,weight in invoices))
    exps=[int(scale*weight) for _,weight in invoices];threshold=int(scale*margin)
    bits=max(sum(g.numerator.bit_length()*e for (g,_),e in zip(invoices,exps))+max(-threshold,0),
             sum(g.denominator.bit_length()*e for (g,_),e in zip(invoices,exps))+max(threshold,0))
    if bits>limit:return {'status':'UNRESOLVED_RESOURCE_BOUND','estimated_bits':bits}
    left=right=1
    for (g,_),e in zip(invoices,exps):
        left*=g.numerator**e;right*=g.denominator**e
        common=gcd(left,right);left//=common;right//=common
    if threshold>=0:right<<=threshold
    else:left<<=-threshold
    return {'status':'CERTIFIED','sign':(left>right)-(left<right),'scale':scale,'estimated_bits':bits,
            'integer_left_hex':hex(left),'integer_right_hex':hex(right)}
def main():
    start=time.monotonic();count=0
    frozen=json.loads((O/'FROZEN.json').read_text(encoding='utf-8'))
    ms=frozen['parameter_domain']['dyadic_m']
    save('PAIRED_FROZEN.json',{'helper_version':'A073-paired-v1','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'family':'same fixed AND2 actual seed, two supplied terminal copies; calibrated references at adjacent dyadic sign brackets',
         'domain':{'dyadic_m':ms,'old_booking':'1/4','CURRENT margins':['-1/64','0','1/64']},
         'case_count':3*len(ms),'symmetry':'none','arithmetic':'independent integer radical root isolation; direct FULL CE likelihood products; common-denominator integer comparison',
         'memory_estimate_MB':60,'maximum_runtime_seconds':55,'precision_stop':'one exact integer comparison; explicit UNRESOLVED on size limit'})
    selected=[];maxbits=0
    for m in ms:
        assert time.monotonic()-start<55
        d=1<<m;k=(7*d-isqrt(24*d*d))//12
        if (7*d-12*k)**2<24*d*d:k-=1
        assert (7*d-12*k)**2>24*d*d>(7*d-12*(k+1))**2;count+=1
        bs=[F(k,d),F(k+1,d)];gs=[full_price_product(b) for b in bs]
        assert gs[0]<1<gs[1];count+=1
        for b,g in zip(bs,gs):
            assert g==F(27*b.numerator*(3*b.denominator-4*b.numerator)**2,25*b.denominator**3)
            # Reconstruction from true law: all four powers are p_s=1/4.
            assert b>=F(1,8) and b<=F(1,4);count+=2
        # Both terminal reaches=1/2 and supplied seed weight=3/8: log exponent3/64.
        # They may be two identical unchanged Boolean terminals; the seed weight is an explicitly SUPPLIED decomposition, not a new Boolean realization theorem.
        inv=[(g,F(3,64)) for g in gs]
        for margin in [F(-1,64),F(0),F(1,64)]:
            result=compare_all(inv,margin)
            assert result['status']=='CERTIFIED'
            # Independent compressed comparison: sum = (3/64)log2(gminus*gplus).
            product=gs[0]*gs[1];u=(F(64,3)*margin).numerator;v=(F(64,3)*margin).denominator
            left=product.numerator**v*2**max(-u,0);right=product.denominator**v*2**max(u,0)
            assert result['sign']==(left>right)-(left<right)
            maxbits=max(maxbits,result['estimated_bits']);count+=2
            if m in [4,58,160,512,1024]:selected.append({'m':m,'current_unused_B_minus_C_minus_U':str(margin),'old_U_retained':'1/4','both_terminal_reaches':['1/2','1/2'],'seed_weight':'3/8',**result})
    # Direct exact equality, zero weights, EMPTY invoice, and size holds must remain distinct verdicts.
    for inv,margin,expected in [([],F(0),0),([],F(1),-1),([(F(2),F(1))],F(1),0),
                                ([(F(1,2),F(1)),(F(2),F(1))],F(0),0),([(F(7,5),F(0))],F(0),0)]:
        assert compare_all(inv,margin)['sign']==expected;count+=1
    assert compare_all([(F(7,5),F(1000001))],F(0))['status']=='UNRESOLVED_RESOURCE_BOUND';count+=1
    # Produce native-core Lean fixtures for the actual first binary64 alias.
    d=1<<58;k=(7*d-isqrt(24*d*d))//12
    if (7*d-12*k)**2<24*d*d:k-=1
    lean=f'''-- Concrete AND2 sign controls; no imports, no logarithm approximation.
theorem negative_neighbor : 27 * ({k}:Nat) * (3*{d}-4*{k})^2 < 25*({d}:Nat)^3 := by decide
theorem positive_neighbor : 25*({d}:Nat)^3 < 27 * ({k+1}:Nat) * (3*{d}-4*{k+1})^2 := by decide
#print axioms negative_neighbor
#print axioms positive_neighbor
'''
    (R/'code/InvoiceSigns.lean').write_text(lean,encoding='utf-8')
    save('PAIRED_CERTIFICATES.json',selected)
    result={'status':'PASS','exact_checks':count,'paired_budget_cases':3*len(ms),'dyadic_brackets':len(ms),'maximum_integer_bit_estimate':maxbits,
            'independence':'Separate radical/full-likelihood representation by A073; independent-agent A085 source review, not outside acceptance of new bound',
            'both_full_terminals':'retained; signed prices combined BEFORE budget verdict; old U not refunded',
            'runtime_seconds':time.monotonic()-start}
    save('PAIRED_RESULT.json',result);print(json.dumps(result))
if __name__=='__main__':main()
