import math,json,pathlib
R=pathlib.Path(__file__).resolve().parent
assert 11**12<250000*4**12
def log_choose(n,k):
 return k*math.log(n)-math.lgamma(k+1)+sum(math.log1p(-i/n) for i in range(k))
J=(math.log(250000)-12)/5;results=[];a=12/5;A0=2*math.sqrt(32)
for target in [100,1000,10000,100000]:
 n=round((target/a)**3);k=target;r=4*k//5;m=2*k-r
 val=log_choose(k,r)+log_choose(n-k,k-r)-log_choose(n,k)+4*math.lgamma(k+1)-2*math.lgamma(m+1)-math.log(16)-2*A0*math.sqrt(k)
 results.append({'n':n,'k':k,'r':r,'normalized_log_lower_bound':val/k,'asymptotic_J':J,'tree_penalty_removed':val/k+2*A0/math.sqrt(k)})
assert results[-1]['normalized_log_lower_bound']>0
assert abs(results[-1]['tree_penalty_removed']-J)<.001
out={'exact_power_comparison':[11**12,250000*4**12],'J':J,'finite_lower_bounds':results,'scope':'Checks analytic combinatorial lower bound; does not generate n points or estimate the optimal mean.'}
(R/'overlap_check.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))
