"""Additional exact data for low-degree rational-function hypotheses."""
from pathlib import Path
import json
import time
from escape import poisson_bounds

for label,p in [('085','17/20'),('093','93/100'),('097','97/100'),('099','99/100')]:
    path=Path(f'data/cert_m3_p{label}.json')
    if path.exists():
        continue
    start=time.monotonic()
    result=poisson_bounds([p]*3,64,90,True)
    result['seconds']=time.monotonic()-start
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(label,result['lower'][:46],result['width'][:16],flush=True)
