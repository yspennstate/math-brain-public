"""Second representation: direct centered moments and unfactored products.
Uses only standard library, never imports A072 or the log certificate helper.
This is a second check by the same contributor, not independent agent review.
"""
from pathlib import Path
from fractions import Fraction as F
from math import prod
import json,time
ROOT=Path(__file__).resolve().parents[1]

def spectrum(table,p):
    n=len(p);out=[]
    for s in range(1<<n):
        moment=sum((table[x]*prod(p[i] if x>>i&1 else 1-p[i] for i in range(n))
          *prod(F((x>>i)&1)-p[i] for i in range(n) if s>>i&1) for x in range(1<<n)),F(0))
        out.append(moment**2/prod(p[i]*(1-p[i]) for i in range(n) if s>>i&1))
    assert sum(out)==1
    return out

def main():
    start=time.perf_counter();rows=[]
    for name in ['minimum_positive','exact_zero','taxfree_AND']:
        c=json.loads((ROOT/'out'/f'{name}.json').read_text())
        table=c['table'];p=list(map(F,c['biases']));parent=spectrum(table,p)
        assert parent==list(map(F,c['parent']['spectrum']))
        selected=[i for i in range(len(p)) if c['physical_block_mask']>>i&1]
        kept=[i for i in range(len(p)) if i not in selected]
        q=[F(0)]*(1<<len(kept))
        for s,m in enumerate(parent):q[sum(((s>>i)&1)<<j for j,i in enumerate(kept))]+=m
        assert q==list(map(F,c['marginal']))
        laws=[(F(c['orientation']),parent),(-2*F(c['orientation']),q)]
        for z,ch in enumerate(c['children']):
            sub=[]
            for y in range(1<<len(kept)):
                x=sum(((z>>j)&1)<<i for j,i in enumerate(selected))+sum(((y>>j)&1)<<i for j,i in enumerate(kept))
                sub.append(table[x])
            assert sub==ch['table']
            law=spectrum(sub,[p[i] for i in kept]);assert law==list(map(F,ch['spectrum']))
            wt=prod(p[i] if z>>j&1 else 1-p[i] for j,i in enumerate(selected))
            assert wt==F(ch['weight']);laws.append((c['orientation']*wt,law))
        # Reconstruct the entropy product without prime factorization.
        # Common L=4096 handles individual terms, including the equality case.
        L=4096;U=V=1
        for weight,law in laws:
            for mass in law:
                if not mass:continue
                exponent=-L*weight*mass;assert exponent.denominator==1
                exponent=int(exponent);a,b=mass.numerator,mass.denominator
                if exponent>=0:U*=a**exponent;V*=b**exponent
                else:U*=b**(-exponent);V*=a**(-exponent)
        saved=json.loads((ROOT/'out'/f'{name}_products.json').read_text())
        u=int(saved['U_hex'],16);v=int(saved['V_hex'],16)
        assert L%c['clearing_denominator']==0
        multiplier=L//c['clearing_denominator']
        assert U*v**multiplier==V*u**multiplier
        sign=(U>V)-(U<V);assert sign==c['sign']
        rows.append({'name':name,'direct_moments_match':True,'unfactored_entropy_product_match':True,'sign':sign})
    result={'cases':rows,'failures':0,'runtime_seconds':time.perf_counter()-start,
       'review_scope':'Second algorithm by A073; not independent agent acceptance'}
    assert result['runtime_seconds']<55
    (ROOT/'out/alternate_check.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
