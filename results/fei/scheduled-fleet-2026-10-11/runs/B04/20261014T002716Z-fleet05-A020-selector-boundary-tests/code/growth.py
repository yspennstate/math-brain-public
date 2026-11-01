from pathlib import Path
from fractions import Fraction as Q
import json
ROOT=Path(__file__).resolve().parents[1]
rows=[]
for k in range(2,33):
    r=k*k;delta=Q(1,1<<k);J=r*delta;I=(r+k)*delta;L=k*(r-1)*delta
    assert L/I==k-1 and L/J==k*(1-Q(1,r))
    rows.append(dict(k=k,r=r,n=k+r,I=str(I),private_I=str(J),minimum_character_loss=str(L),loss_over_I=str(L/I),truth_table_constructed=False))
(ROOT/'out'/'growth.json').write_text(json.dumps(dict(cases=31,status='PASS',rows=rows),indent=2))
print('PASS 31 exact formula specializations')
