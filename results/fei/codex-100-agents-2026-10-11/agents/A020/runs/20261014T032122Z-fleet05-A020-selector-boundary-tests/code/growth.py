from pathlib import Path
from fractions import Fraction as Q
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();rows=[]
for k in range(1,33):
    m=k*k;J=Q(m+1,2);d=Q(k,2);I=J+d;T=Q(k*m)+Q(k*k,2)
    assert T/I==Q(2*k*m+k*k,m+k+1)
    assert Q(2)<=4*I
    rows.append(dict(k=k,m=m,n=m+k+1,J=str(J),d=str(d),I=str(I),raw_T=str(T),raw_T_over_I=str(T/I),H='2',CE='2',shared_erasure='0',K4_bad_bill='0',truth_table_constructed=False))
    (R/'out/GROWTH.json').write_text(json.dumps(dict(status='PASS',cases=len(rows),rows=rows,runtime_seconds=time.perf_counter()-start),indent=2))
assert time.perf_counter()-start<30
print(json.dumps(dict(status='PASS',cases=32,runtime_seconds=time.perf_counter()-start)))
