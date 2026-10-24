from itertools import permutations
from fractions import Fraction as F
from pathlib import Path
import json
import math
import time

ROOT=Path(__file__).resolve().parent

def main():
    start=time.perf_counter()
    source=[(F(x,6),F(y,4)) for y in (1,3) for x in (1,3,5)]
    target=[(x+2,y) for x,y in source]
    eps=F(1,100)
    minima={sign:(float('inf'),[]) for sign in (-1,0,1)}
    for perm in permutations(range(6)):
        base=0.0; square=F(0)
        for i,j in enumerate(perm):
            d=target[j][0]-source[i][0]
            h=target[j][1]-source[i][1]
            base+=math.sqrt(float(d*d+h*h))/6
            square+=d*d/6
        for sign in (-1,0,1):
            cost=base+float(sign*eps*square)
            best,plans=minima[sign]
            if cost<best-1e-12:
                minima[sign]=(cost,[perm])
            elif abs(cost-best)<=1e-12:
                plans.append(perm)
    translation=tuple(range(6))
    reversal=(2,1,0,5,4,3)
    assert len(minima[0][1])==36
    assert minima[1][1]==[translation]
    assert minima[-1][1]==[reversal]
    squared_reversal=sum(((target[reversal[i]][0]-source[i][0])**2/6 for i in range(6)),F(0))
    assert squared_reversal==F(116,27)
    result={'command':'python -X utf8 p0336_check.py','bijections_checked':720,
            'euclidean_minimizers':len(minima[0][1]),'positive_tilt_minimizers':len(minima[1][1]),
            'negative_tilt_minimizers':len(minima[-1][1]),
            'grid_reversal_mean_d_squared_exact':str(squared_reversal),
            'tilt_epsilon_exact':str(eps),'elapsed_seconds':time.perf_counter()-start}
    (ROOT/'measurements').mkdir(exist_ok=True)
    (ROOT/'measurements'/'p0336.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
