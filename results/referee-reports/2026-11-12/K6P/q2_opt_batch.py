"""Sequential optimization runs; whole batch guarded at 220 seconds."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import time
import q2_search as s
begin=time.monotonic()
for n in range(4,9):
    for r in (2,3):
        if time.monotonic()-begin>205:break
        s.START=time.monotonic();s.LIMIT=min(18,220-(s.START-begin))
        s.run_opt(n,r,11220+n*10+r)
