from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import json,time
from check_pair import analyze,walsh
ROOT=Path(__file__).resolve().parents[1]
def main():
    start=time.perf_counter(); eligible=0; witness=None; checked=0
    for C in combinations(range(16),8):
        costs=[sum((s&v).bit_count()%2 for s in C) for v in range(16)]
        p=[costs[1<<i] for i in range(4)]
        checked+=1
        if not(all(x<=4 for x in p) and all(min(costs[v],8-costs[v])>=max(p[i] for i in range(4) if v>>i&1) for v in range(1,16))): continue
        eligible+=1
        table=sum(( ((x&C[y]).bit_count()%2) << (x+(y<<4))) for y in range(8) for x in range(16))
        a=walsh([1-2*((table>>x)&1) for x in range(128)])
        # Every nonzero numerator has magnitude16, as the injective-map formula predicts.
        assert all(a[s+(v<<4)]== (16*(-1)**((v&C.index(s)).bit_count()%2) if s in C else 0) for s in range(16) for v in range(8))
        data=analyze(7,table); assert data is not None
        failing=[pair for pair in data['pairs'] if pair['pair'][1]<4 and F(pair['gap_Q'])>0]
        if failing:
            witness={'C':C,'table':str(table),'detail':failing,'full_data':data}; break
        if time.perf_counter()-start>52: raise RuntimeError('frozen cap')
    out={'codes_checked':checked,'eligible':eligible,'witness':witness,'seconds':time.perf_counter()-start,'exhaustive':witness is None}
    (ROOT/'out/CODED.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='witness'}))
    if witness: print(json.dumps({k:v for k,v in witness.items() if k!='full_data'}))
if __name__=='__main__': main()
