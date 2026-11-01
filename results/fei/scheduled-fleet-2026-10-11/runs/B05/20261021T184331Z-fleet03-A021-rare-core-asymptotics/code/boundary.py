from fractions import Fraction as Q
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]; rows=[]; assertions=0
for m in range(4,102,2):
 for t in (0,m,3*m+1):
    # Exact bound for actual Uy minus the largest permitted final fraction.
    gap=Q(m,16)-Q(17,8)-Q(2,3)*(1+t)
    assert (gap>0)==(3*m>134+32*t); assertions+=1
    rows.append({'m':m,'t':t,'normalized_gap_lower':str(gap),'certified_failure':gap>0})
assert Q(44,16)-Q(17,8)-Q(2,3)<0; assertions+=1
assert Q(46,16)-Q(17,8)-Q(2,3)==Q(1,12); assertions+=1
obj={'status':'PASS','cases':len(rows),'assertions':assertions,'boundary_even_m_t0':46,'rows':rows}
(R/'out/BOUNDARY.json').write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({k:v for k,v in obj.items() if k!='rows'}))
