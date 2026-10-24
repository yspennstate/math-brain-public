from itertools import product
from pathlib import Path
from fractions import Fraction as F
import json
import math
import time

ROOT=Path(__file__).resolve().parent

def variation(ps):
    overlap=0.0
    for bits in product((0,1),repeat=len(ps)):
        pb=math.prod(p if bit else 1-p for p,bit in zip(ps,bits))
        pn=math.exp(-sum(ps))*math.prod(p if bit else 1 for p,bit in zip(ps,bits))
        overlap+=min(pb,pn)
    return max(0.0,1-overlap)

def main():
    start=time.perf_counter()
    rows=[]
    for dim in (1,2,3,5,8):
        for scale in (0.0,0.01,0.1,0.5,1.0):
            ps=[scale*(i+1)/dim for i in range(dim)]
            actual=variation(ps)
            bound=sum(p*(1-math.exp(-p)) for p in ps)
            square=sum(p*p for p in ps)
            assert actual<=bound+1e-12<=square+2e-12
            if dim==1:
                assert abs(actual-bound)<1e-12
            rows.append({'dimension':dim,'scale':scale,'marked_tv':actual,'coupling_bound':bound,'sum_p_squared':square})
    p=F(1,2)
    P={(0,0):1-p,(1,0):p}
    Q={(0,0):1-p,(0,1):p}
    tv=sum((abs(P.get(x,F(0))-Q.get(x,F(0))) for x in set(P)|set(Q)),F(0))/2
    assert tv==p
    result={'command':'python -X utf8 p0088_check.py','marked_vector_cases':len(rows),
            'count_counterexample_tv_exact':'0','marked_counterexample_tv_exact':str(tv),
            'cases':rows,'elapsed_seconds':time.perf_counter()-start}
    (ROOT/'measurements').mkdir(exist_ok=True)
    (ROOT/'measurements'/'p0088.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))

if __name__=='__main__':
    main()
