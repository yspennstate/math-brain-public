"""Sequential short search batches, saved before execution."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import time
import q2_search as s
for n in (5,6,7):
    s.START=time.monotonic();s.run_exact('random',n)
for n in (4,5,6,7):
    s.START=time.monotonic();s.run_exact('structured',n)
