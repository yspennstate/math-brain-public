from fractions import Fraction as F
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parent

def main():
    start=time.perf_counter()
    times=[F(1)+F(k,4) for k in range(5)]
    centers=[F(5,4)+F(2*j+1,4004) for j in range(1001)]
    rows=[]
    for n in (10,30,100,300,1000,10000):
        activation=F(1,n)
        assert activation*n==1
        for center in (centers[0],centers[500],centers[-1]):
            peak=1+max(1-n*abs(center-center),0)
            end=1+max(1-n*abs(center+F(1,n)-center),0)
            assert peak-end==1
        hit=sum(any(abs(t-center)<F(1,n) for t in times) for center in centers)
        fraction=hit/len(centers)
        continuum_bound=min(1.0,4*len(times)/n)
        assert fraction<=continuum_bound+2*len(times)/len(centers)
        rows.append({'n':n,'survival_probability_exact':str(activation),'restricted_scaled_mass_exact':'1',
                     'peak_to_endpoint_difference_exact':'1','fixed_time_grid_hit_fraction':fraction,
                     'continuum_fdd_union_bound':continuum_bound})
    result={'command':'python -X utf8 c0076_check.py','scales':len(rows),
            'center_grid_size':len(centers),'cases':rows,'elapsed_seconds':time.perf_counter()-start}
    (ROOT/'measurements').mkdir(exist_ok=True)
    (ROOT/'measurements'/'c0076.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
