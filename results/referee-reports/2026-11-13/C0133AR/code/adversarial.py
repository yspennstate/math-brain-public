"""A non-IID elliptic counterexample and independent trap product arithmetic."""
import math,json,os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if os.getpriority(os.PRIO_PROCESS,0)<10:os.setpriority(os.PRIO_PROCESS,0,10)
rows=[];elapsed=0
for k in range(1,31):
 R=2**k;peak_time=elapsed+R
 assert peak_time==3*R-4
 rows.append(dict(k=k,R=R,peak_time=peak_time,peak_ratio=R/peak_time))
 elapsed+=2*R
# eps_(x,y),i = 2^(-|x|-|y|-i-8); preferred arrow is prescribed
# by the kth departure from that site along the chosen excursion path.
# Sum over ALL sites and cookie indices = 3*3*1/256.
error_sum=3*3*3/256
p=1/16
for i in range(1,100):p*=(1-3*2**(-i-4))**2
p_log=math.exp(-math.log(16)+2*math.fsum(math.log1p(-3*2**(-i-4)) for i in range(1,100)))
assert abs(p-p_log)<1e-15
result=dict(excursion_peaks=rows,positive_event_lower_bound=1-error_sum,
 limiting_limsup=1/3,liminf=0,submitted_trap_probability=p,via_logs=p_log)
(ROOT/"data/adversarial.json").write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k!="excursion_peaks"},indent=2))
