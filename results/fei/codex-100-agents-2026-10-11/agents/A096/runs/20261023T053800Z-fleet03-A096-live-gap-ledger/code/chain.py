import json,time
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0; x=F(9,14336)
for L in range(1,65):
    mu=F((-1)**L,4)
    # Actual tail t has3 negative entries out of8; sign reversal has5.
    negatives=3 if L%2==0 else 5
    size=8
    for k in reversed(range(L)):
        sign=(-1)**k; sibling=F(3*sign,4)
        d=(mu-sibling)/2
        assert d*d==F(1,4)
        assert x/(F(3,8)*(1-mu*mu)+x)==F(1,561)
        assert x/(F(3,8)*(1-sibling*sibling)+x)==F(3,787)
        assert abs(mu)<1 and abs(sibling)<1
        # Sibling point sign has1 or7 negative auxiliary assignments,
        # independent of every unqueried chain bit.
        sibling_negative=(1 if sign==1 else 7)*(size//8)
        negatives+=sibling_negative;size*=2
        mu=(mu+sibling)/2
        assert mu==F((-1)**k,4)==1-F(2*negatives,size)
        checks+=5
assert 561**64*63**2>560**64*64**2
result={'status':'PASS','chains':64,'prefix_recurrences':2080,'assertions':checks+1,'x':str(x),'retained_epsilon':'1/561','sibling_epsilon':'3/787','path_log_lower_bound':'L/561','two_round_budget_exceeded_at_L64':True,'integer_comparison':'561^64*63^2 >560^64*64^2','runtime_seconds':time.perf_counter()-start,'full_truth_tables_materialized':False,'analytic_all_L_extension':'DERIVATION.md section3'}
(ROOT/'out/CHAIN_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
